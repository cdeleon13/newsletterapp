from dash import Dash, html, dcc, Input, Output, page_registry, page_container, register_page, callback
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd

from datetime import datetime
import dash_bootstrap_components as dbc

### Local modules
# from data_loader import load_newsletter_data
# from newsletter_filters import filters_section
from block1 import block1
from block2 import block2
from block3 import block3
from racial_equity_block import accordion_block
from pit_racial_equity_block import pit_re_block
# from navbar import navbar
# from racial_equity_filters import re_filters_section

import requests
from io import StringIO

register_page(__name__, path='/', title='HMIS Data Dashboard', name='HMIS Data Dashboard')

###
# | data_loader.py
###

def load_data():
    base_url = 'https://raw.githubusercontent.com/cdeleon13/newsletterapp/main/assets/'

    newsletter_housed_counts_by_destination_url = base_url + 'newsletter_housed_counts_by_destination_by_race.csv'
    newsletter_housed_counts_by_destination_df = pd.read_csv(StringIO(requests.get(newsletter_housed_counts_by_destination_url).text))

    newsletter_counts_by_race_url = base_url + 'newsletter_counts_by_race.csv'
    newsletter_counts_by_race_df1 = pd.read_csv(StringIO(requests.get(newsletter_counts_by_race_url).text))
    old_cols = [x for x in newsletter_counts_by_race_df1.columns if 'by Race' in x]
    new_cols = [x.replace(" by Race", "") for x in newsletter_counts_by_race_df1 if 'by Race' in x]
    newsletter_counts_by_race_df1 = newsletter_counts_by_race_df1.rename(columns=dict(zip(old_cols, new_cols)))

    newsletter_active_counts_by_proj_type_by_race_url = base_url + 'newsletter_active_counts_by_proj_type_by_race.csv'
    newsletter_active_counts_by_proj_type_by_race = pd.read_csv(newsletter_active_counts_by_proj_type_by_race_url)

    newsletter_active_counts_by_proj_type_by_race_url = base_url + 'newsletter_active_counts_by_proj_type_by_race.csv'
    newsletter_active_counts_by_proj_type_by_race = pd.read_csv(StringIO(requests.get(newsletter_active_counts_by_proj_type_by_race_url).text))

    #
    pit_data_likely_url = base_url + 'pit_data_likely_df.csv'
    pit_data_likely_df = pd.read_csv(StringIO(requests.get(pit_data_likely_url).text))
    pit_data_url = base_url + 'pit_data_df.csv'
    pit_data_df = pd.read_csv(StringIO(requests.get(pit_data_url).text))
    
    race_picklist = sorted(list(newsletter_counts_by_race_df1['static_demographics.race_text'].unique()))
    return (
        newsletter_housed_counts_by_destination_df, 
        newsletter_counts_by_race_df1, 
        newsletter_active_counts_by_proj_type_by_race, 
        pit_data_likely_df,
        pit_data_df,
        race_picklist)


(newsletter_housed_counts_by_destination_df, 
newsletter_counts_by_race_df1, 
newsletter_active_counts_by_proj_type_by_race, 
pit_data_likely_df,
pit_data_df,
race_picklist) = load_data()


###
# | END
# | data_loader.py
###

###
# | newsletter_filters.py
###
# reporting_window_group = html.Div([
#     dcc.Dropdown(
#         id='report-window',
#         options=[{'label': window, 'value': window} for window in newsletter_counts_by_race_df1["Reporting Window"].unique()],
#         value='Monthly',
#         placeholder="Select a reporting window",
#     ),
#     html.Div(id="output"),
# ], className="radio-group")


dropdown_options = [{'label': race, 'value': race} for race in race_picklist]
dropdown_value = [x for x in race_picklist if x not in ["Client doesn't know", "Client refused", 'Client prefers not to answer', "Data not collected"]]

reporting_year_options = list(newsletter_counts_by_race_df1['Reporting Year'].unique())

filters_section = dbc.Card(
    [
        dbc.CardHeader("Filters"),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col([
                            html.P("Select Reporting Period", className='filter_titles'),
                            dcc.Dropdown(
                                options=reporting_year_options,
                                value=2023,
                                id='year-slider'
                            )],
                            width=12, sm=12, md=12, lg=12, xl=12
                        ),
                    ]
                ),
            ]
        ),
    ],
    className="my-3"
)
###
# | END |
# | newsletter_filters.py
###

# color_dict = {}
# color_palette = px.colors.qualitative.Plotly

layout =  dbc.Container(
                children=[
                    dcc.Loading(
                        id="loading-1",
                        type="default",
                        children=[
                            filters_section,
                            html.Div(
                                className="container",
                                children=[
                                    html.Div(
                                        children=[block1], className='mb-3'
                                    ),
                                    html.Div(
                                        children=[block2], className='mb-3'
                                    ),
                                    html.Div(
                                        children=[block3], className='mb-3'
                                    ),
                                ]
                            ),
                        ]
                    ),
                ], style={"z-index":-1}
            )

color_dict = {
    'Native Hawaiian or Pacific Islander': '#0075C2',
    'Asian or Asian American': '#00CED1',
    'White': '#F8C02A',
    'Data not collected': '#1AF2C3',
    "Client doesn't know":  '#20AF90',
    'American Indian, Alaska Native, or Indigenous':'#FFDA7A', 
    'Multi-Racial':'#C92DC0', 
    'Black, African American, or African': '#8D3188',
    'Client refused':'#1AF2C3',
    'Client prefers not to answer':'#07896D'
    }



color_palette = [
    '#F8C02A',
    '#FFDA7A',
    '#CB9300',
    '#8D3188',
    '#C92DC0',
    '#6C1867',
    '#20AF90',
    '#1AF2C3',
    '#07896D',
    '#00CED1',
    '#10FBFF',
    '#009092',
    '#0075C2',
    '#0098FC',
    '#005187'
    ]

@callback(
    Output('active_counts_pie', 'figure'),
    Input('year-slider', 'value'),
    )
def update_figure1(selected_year):
    filtered_df = newsletter_active_counts_by_proj_type_by_race[newsletter_active_counts_by_proj_type_by_race['Reporting Year'] == selected_year].reset_index(drop=True)
    
    fig = px.pie(filtered_df, names="Project Type", values="Active Clients Count", labels='abbrev', hole=.7, color_discrete_sequence=px.colors.qualitative.Vivid[:len(filtered_df)],)
    # active_client_count = filtered_df['Active Clients Count'].sum()
    fig.update_layout({
        'plot_bgcolor': 'rgba(0,0,0,0)',
        'paper_bgcolor': 'rgba(0,0,0,0)',
        'legend_font': {"color":"rgba(0,0,0,0.95)"},
        "legend_title_text":"HMIS Project Types",
        "legend_title_side":"top",
        "legend_orientation":"h",
        "legend_yanchor":"top",
        "legend_y":0,
        "legend_xanchor":"center",
        "legend_x":0.5,
        "legend_font_size": 10,
        })

    fig.update_traces(
        textposition="auto",
        insidetextorientation="horizontal", 
        insidetextfont_color="white",
        outsidetextfont_color="white",
    )

    return fig


@callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value'),
    )
def update_figure2(selected_year):
    filtered_df = newsletter_housed_counts_by_destination_df[newsletter_housed_counts_by_destination_df['Reporting Year'] == selected_year].reset_index(drop=True)

    # Sort the dataframe by 'clients.unique_identifier' in descending order
    filtered_df = filtered_df.sort_values('clients.unique_identifier', ascending=True)

    # # Create color_dict and assign a color to each category in names argument
    # for i, name in enumerate(filtered_df['static_demographics.race_text'].unique()):
    #     if name not in color_dict:
    #         color_dict[name] = color_palette[i % len(color_palette)]

    fig = px.bar(filtered_df, y='Permanent Destination', x='clients.unique_identifier', orientation='h', text_auto=True, color='static_demographics.race_text', color_discrete_map=color_dict)
    fig.update_layout({
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)',
    'legend_bgcolor': "rgba(1,1,1,1)",
    "showlegend":False,
    'yaxis_title':"",
    'uniformtext_minsize': 12,
    'uniformtext_mode': 'hide',
    })
    fig.update_traces(textposition='inside', hovertemplate='%{value:.0f}')
    fig.update_xaxes(visible=False)
    fig.update_yaxes(
        tickmode="array",
        categoryorder="total ascending",
        ticklabelposition="outside",
        tickfont=dict(color="black"), matches=None, showticklabels=True, visible=True
    )

    return fig

@callback(
    Output('fth_race_plot', 'figure'),
    Output('housed_race_plot', 'figure'),
    Output('new_entries_race_plot', 'figure'),
    Output('new_referrals_race_plot', 'figure'),
    Input('year-slider', 'value'),
)
def update_(selected_year):
    temp_df = newsletter_counts_by_race_df1[newsletter_counts_by_race_df1['Reporting Year']==selected_year].reset_index(drop=True)

    donut_plot_d = {}
    for col in [x for x in temp_df.columns if 'Count' in x]:
        count_by_race_df = temp_df[['static_demographics.race_text',col]].copy()

        fig = px.pie(count_by_race_df, names='static_demographics.race_text', values=col, hole=0.7)

        # Get the list of colors corresponding to each race category
        colors = [color_dict.get(name, 'gray') for name in count_by_race_df['static_demographics.race_text'].unique()]
        # Set the colors for each sector
        fig.update_traces(marker=dict(colors=colors))

        fig.update_layout({
            'showlegend':False,
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'margin_b':0,
            'margin_l':0,
            'margin_t':0,
            'margin_r':0,
            'uniformtext_minsize': 12,
            'uniformtext_mode': 'hide',
        })

        # Update the color of each trace using the color_dict
        for i, name in enumerate(count_by_race_df['static_demographics.race_text'].unique()):
            fig.update_traces(selector=dict(name=name), marker=dict(colors=[color_dict[name]]))

        fig.update_traces(textposition='inside', hovertemplate='%{label}<br>%{value:.0f}')

        donut_plot_d[col] = fig

    return (
        donut_plot_d['FTH Count'],
        donut_plot_d['Housed Count'],
        donut_plot_d['New Program Entries Count'],
        donut_plot_d['New Referrals Count']
    )

@callback(
    Output('senior_active_race_plot', 'figure'),
    Output('veteran_active_race_plot', 'figure'),
    Output('families_active_race_plot', 'figure'),
    Output('tay_active_race_plot', 'figure'),
    Output('senior_housed_race_plot', 'figure'),
    Output('veteran_housed_race_plot', 'figure'),
    Output('tay_housed_race_plot', 'figure'),
    Output('families_housed_race_plot', 'figure'),
    Input('year-slider', 'value'),
)
def update_housed_race_plots(selected_year):

    temp_df = newsletter_counts_by_race_df1[newsletter_counts_by_race_df1['Reporting Year']==selected_year].reset_index(drop=True)
    
    bar_plot_d = {}
    for col in  [x for x in temp_df.columns if ('Housed' in x or 'Active' in x) and x!='Housed Count' and x!='Active Count']:
        count_by_race_df = temp_df[['Reporting Year', 'static_demographics.race_text', col]].copy()

        count_by_race_df = count_by_race_df.sort_values(col, ascending=True)

        # # Create color_dict and assign a color to each category in names argument
        # for i, name in enumerate(count_by_race_df['static_demographics.race_text'].unique()):
        #     if name not in color_dict:
        #         color_dict[name] = color_palette[i % len(color_palette)]

        fig = px.bar(count_by_race_df, x=col, y='Reporting Year', orientation='h', text_auto=True, color_discrete_map=color_dict, color='static_demographics.race_text')
        fig.update_layout({
            'plot_bgcolor': 'rgba(0,0,0,0)',
            'paper_bgcolor': 'rgba(0,0,0,0)',
            'margin_b':0,
            'margin_l':0,
            'margin_t':0,
            'margin_r':0,
            'xaxis': {
            #     'range': [0, 1],
                'showgrid': False, # thin lines in the background
                'zeroline': False, # thick line at x=0
                'visible': False,  # numbers below
            }, # the same for yaxis
            'yaxis': {
            #     'range': [0, 1],
                'showgrid': False, # thin lines in the background
                'zeroline': False, # thick line at x=0
                'visible': False,  # numbers below
            }, # the same for yaxis
            'barmode':'stack',
            # 'barnorm':'percent',
            'showlegend':False,
            'uniformtext_minsize':16, 
            "uniformtext_mode":'hide', 
            "autosize":False,
            # 'config': {'displayModeBar': False}
        })

        fig.update_traces(textposition='inside', hovertemplate='%{value:.0f}')

        bar_plot_d[col] = fig
    return (
        bar_plot_d['Active Seniors Count'], 
        bar_plot_d['Active Veterans Count'], 
        bar_plot_d['Active TAY Count'], 
        bar_plot_d['Active Families Count'],
        bar_plot_d['Housed Seniors Count'], 
        bar_plot_d['Housed Veterans Count'], 
        bar_plot_d['Housed TAY Count'], 
        bar_plot_d['Housed Families Count'])

@callback(
    Output(component_id='fth_count', component_property='children'),
    Output(component_id='housed_count', component_property='children'),
    Output(component_id='new_entries_count', component_property='children'),
    Output(component_id='new_referrals_count', component_property='children'),
    Output(component_id='seniors_active_count', component_property='children'),
    Output(component_id='tay_active_count', component_property='children'),
    Output(component_id='families_active_count', component_property='children'),
    Output(component_id='veterans_active_count', component_property='children'),
    Output(component_id='housed_count_1', component_property='children'),
    Output(component_id='senior_housed_count', component_property='children'),
    Output(component_id='tay_housed_count', component_property='children'),
    Output(component_id='families_housed_count', component_property='children'),
    Output(component_id='veterans_housed_count', component_property='children'),
    Output(component_id='active_count', component_property='children'),
    Input('year-slider', 'value'),
    )
def update_metrics(selected_year):
    temp_df = newsletter_counts_by_race_df1[newsletter_counts_by_race_df1['Reporting Year']==selected_year]
    d = {col: temp_df[col].sum() for col in temp_df if 'Count' in col}
    return (
        d['FTH Count'], 
        d['Housed Count'], 
        d['New Program Entries Count'], 
        d['New Referrals Count'],
        d['Active Seniors Count'], 
        d['Active TAY Count'],
        d['Active Families Count'],
        d['Active Veterans Count'],
        d['Housed Count'], 
        d['Housed Seniors Count'],
        d['Housed TAY Count'],
        d['Housed Families Count'],
        d['Housed Veterans Count'],
        d['Active Count'],
        )

