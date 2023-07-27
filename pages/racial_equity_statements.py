# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output, page_registry, page_container, register_page, callback
import plotly.express as px
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

register_page(
    __name__,
    path='/equity-statements',
    title='Equity Statements',
    name='Equity Statements'
)

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
    newsletter_active_counts_by_proj_type_by_race = pd.read_csv(StringIO(requests.get(newsletter_active_counts_by_proj_type_by_race_url).text))

    # 
    binary_race_data_counts_url = base_url + 'binary_race_data_counts_df.csv'
    binary_race_data_counts_df = pd.read_csv(StringIO(requests.get(binary_race_data_counts_url).text))
    
    binary_race_likeliness_data_url = base_url + 'binary_race_likeliness_data_df.csv'
    binary_race_likeliness_data_df = pd.read_csv(StringIO(requests.get(binary_race_likeliness_data_url).text))

    #
    active_binary_race_data_counts_url = base_url + 'active_binary_race_data_counts_df.csv'
    active_binary_race_data_counts_df = pd.read_csv(StringIO(requests.get(active_binary_race_data_counts_url).text))

    active_binary_race_likeliness_data_url = base_url + 'active_binary_race_likeliness_data_df.csv'
    active_binary_race_likeliness_data_df = pd.read_csv(StringIO(requests.get(active_binary_race_likeliness_data_url).text))

    #
    housed_binary_race_data_counts_url = base_url + 'housed_binary_race_data_counts_df.csv'
    housed_binary_race_data_counts_df = pd.read_csv(StringIO(requests.get(housed_binary_race_data_counts_url).text))

    housed_binary_race_likeliness_data_url = base_url + 'housed_binary_race_likeliness_data_df.csv'
    housed_binary_race_likeliness_data_df = pd.read_csv(StringIO(requests.get(housed_binary_race_likeliness_data_url).text))

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
        binary_race_data_counts_df, 
        binary_race_likeliness_data_df,
        active_binary_race_data_counts_df,
        active_binary_race_likeliness_data_df,
        housed_binary_race_data_counts_df,
        housed_binary_race_likeliness_data_df,
        pit_data_likely_df,
        pit_data_df,
        race_picklist)


(newsletter_housed_counts_by_destination_df, 
newsletter_counts_by_race_df1, 
newsletter_active_counts_by_proj_type_by_race, 
binary_race_data_counts_df, 
binary_race_likeliness_data_df,
active_binary_race_data_counts_df,
active_binary_race_likeliness_data_df,
housed_binary_race_data_counts_df,
housed_binary_race_likeliness_data_df,
pit_data_likely_df,
pit_data_df,
race_picklist) = load_data()

###
# | END
# | data_loader.py
###

###
# | racial_equity_filters.py
###
years_list = sorted(list(set(binary_race_data_counts_df['Year']).union(set(binary_race_likeliness_data_df['Year']))))
proj_type_list = sorted([x for x in list(set(binary_race_data_counts_df.columns).union(set(binary_race_likeliness_data_df.columns))) if x not in ['Binary Race Variable',  'Unnamed: 0', 'Year']])
race_variable_list = sorted(list(set(binary_race_data_counts_df['Binary Race Variable']).union(set(binary_race_likeliness_data_df['Binary Race Variable']))))

hmis_re_filters_section = dbc.Card(
    [
        dbc.CardHeader("Filters"),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col([
                            html.P("Select Reporting Year", className='filter_titles'),
                            dcc.Dropdown(
                                options=years_list,
                                value=years_list[-1],
                                id='hmis-racial-equity-select-year'
                            )],
                            width=12, sm=12, md=12, lg=4, xl=4
                        ),
                        dbc.Col([
                            html.P("Select Project Type", className='filter_titles'),
                            dcc.Dropdown(
                                options=proj_type_list,
                                value=proj_type_list[0],
                                id='hmis-racial-equity-select-project-type'
                            )],
                            width=12, sm=12, md=12, lg=4, xl=4
                        ),
                        dbc.Col([
                            html.P("Select Race", className='filter_titles'),
                            dcc.Dropdown(
                                options=race_variable_list,
                                value=race_variable_list[0],
                                id='hmis-racial-equity-select-race'
                            )],
                            width=12, sm=12, md=12, lg=4, xl=4
                        ),                        
                    ]
                ),
            ]
        ),
    ],
    className="my-3"
)

pit_re_filters_section = dbc.Card(
    [
        dbc.CardHeader("Filters"),
        dbc.CardBody(
            [
                dbc.Row(
                    [
                        dbc.Col([
                            html.P("Select Reporting Year", className='filter_titles'),
                            dcc.Dropdown(
                                options=years_list,
                                value=years_list[-1],
                                id='pit-racial-equity-select-year'
                            )],
                            width=12, sm=12, md=12, lg=6, xl=6
                        ),
                        dbc.Col([
                            html.P("Select Race", className='filter_titles'),
                            dcc.Dropdown(
                                options=race_variable_list,
                                value=race_variable_list[0],
                                id='pit-racial-equity-select-race'
                            )],
                            width=12, sm=12, md=12, lg=6, xl=6
                        ),                        
                    ]
                ), 
            ],
        ),
    ],
    className="my-3"
)

###
# | END
# | racial_equity_filters.py
###


layout = dbc.Container(
    children=[
        dbc.Tabs([
            dbc.Tab(
                dbc.Container(
                    children=[
                        hmis_re_filters_section,
                        accordion_block
                    ]
                ),
                label='HMIS Data Racial Equity Statements',active_label_style={'color':'grey', 'font-weight':'bolder'}, label_style={'color': 'white'}),
            dbc.Tab(
                dbc.Container(
                    children=[
                        pit_re_filters_section,
                        pit_re_block
                    ]
                ),
                label='PIT Data Racial Equity Statements',active_label_style={'color':'grey', 'font-weight':'bolder'}, label_style={'color': 'white'}),
        ]
        ),
    ]
)

@callback(
Output(component_id='fth_likely_statement', component_property='children'),
Output(component_id='fth_compare_pop_percent', component_property='children'),
Output(component_id='active_likely_statement', component_property='children'),
Output(component_id='active_compare_pop_percent', component_property='children'),
Output(component_id='housed_likely_statement', component_property='children'),
Output(component_id='housed_compare_pop_percent', component_property='children'),
Input('hmis-racial-equity-select-year', 'value'),
Input('hmis-racial-equity-select-project-type', 'value'),
Input('hmis-racial-equity-select-race', 'value')
)
def racial_equity_data(selected_year, project_type, race_option):
    population_percent = {
        "White":.746,
        "Black, African American, or African":.056,
        'American Indian, Alaska Native, or Indigenous':.014,
        'Asian or Asian American':.129,
        'Native Hawaiian or Pacific Islander':0.006,
        'Multi-Racial':.049
    }
    #First Time Homeless
    likely_metric = binary_race_likeliness_data_df[(binary_race_likeliness_data_df['Year'].values==selected_year) & (binary_race_likeliness_data_df['Binary Race Variable'].values==race_option)][project_type].values[0]
    compare_pop_percent = binary_race_data_counts_df[(binary_race_data_counts_df['Year'].values==selected_year) & (binary_race_data_counts_df['Binary Race Variable'].values==race_option)][project_type].values[0]/(binary_race_data_counts_df[(binary_race_data_counts_df['Year'].values==selected_year) & (binary_race_data_counts_df['Binary Race Variable'].values==race_option)][project_type].values[0] + binary_race_data_counts_df[(binary_race_data_counts_df['Year'].values==selected_year) & (binary_race_data_counts_df['Binary Race Variable'].values==f"Non-{race_option}")][project_type].values[0])
    likely_metric_statement = f"{race_option} clients are {'{:.0f}'.format(likely_metric)} times more likely to be First Time Homeless in {project_type} than Non-{race_option} clients"
    compare_pop_percent_statement = f"{race_option} clients make up {'{:.0%}'.format(population_percent[race_option])} of the general population in San Diego County but make up {'{:.0%}'.format(compare_pop_percent)} in {project_type} programs in HMIS."
    
    # Active 
    active_likely_metric = active_binary_race_likeliness_data_df[(active_binary_race_likeliness_data_df['Year'].values==selected_year) & (active_binary_race_likeliness_data_df['Binary Race Variable'].values==race_option)][project_type].values[0]
    active_compare_pop_percent = active_binary_race_data_counts_df[(active_binary_race_data_counts_df['Year'].values==selected_year) & (active_binary_race_data_counts_df['Binary Race Variable'].values==race_option)][project_type].values[0]/(active_binary_race_data_counts_df[(active_binary_race_data_counts_df['Year'].values==selected_year) & (active_binary_race_data_counts_df['Binary Race Variable'].values==race_option)][project_type].values[0] + active_binary_race_data_counts_df[(active_binary_race_data_counts_df['Year'].values==selected_year) & (active_binary_race_data_counts_df['Binary Race Variable'].values==f"Non-{race_option}")][project_type].values[0])
    active_likely_metric_statement = f"{race_option} clients are {'{:.0f}'.format(active_likely_metric)} times more likely to be Active in an HMIS {project_type} program than Non-{race_option} clients"
    active_compare_pop_percent_statement = f"{race_option} clients make up {'{:.0%}'.format(population_percent[race_option])} of the general population in San Diego County but make up {'{:.0%}'.format(active_compare_pop_percent)} in {project_type} programs in HMIS."

    #Housed
    housed_likely_metric = housed_binary_race_likeliness_data_df[(housed_binary_race_likeliness_data_df['Year'].values==selected_year) & (housed_binary_race_likeliness_data_df['Binary Race Variable'].values==race_option)][project_type].values[0]
    housed_compare_pop_percent = housed_binary_race_data_counts_df[(housed_binary_race_data_counts_df['Year'].values==selected_year) & (housed_binary_race_data_counts_df['Binary Race Variable'].values==race_option)][project_type].values[0]/(housed_binary_race_data_counts_df[(housed_binary_race_data_counts_df['Year'].values==selected_year) & (housed_binary_race_data_counts_df['Binary Race Variable'].values==race_option)][project_type].values[0] + housed_binary_race_data_counts_df[(housed_binary_race_data_counts_df['Year'].values==selected_year) & (housed_binary_race_data_counts_df['Binary Race Variable'].values==f"Non-{race_option}")][project_type].values[0])
    housed_likely_metric_statement = f"{race_option} clients are {'{:.0f}'.format(housed_likely_metric)} times more likely to be Housed through a {project_type} than Non-{race_option} clients"
    housed_compare_pop_percent_statement = f"{race_option} clients make up {'{:.0%}'.format(population_percent[race_option])} of the general population in San Diego County but make up {'{:.0%}'.format(housed_compare_pop_percent)} in {project_type} programs in HMIS."

    return likely_metric_statement,compare_pop_percent_statement, active_likely_metric_statement, active_compare_pop_percent_statement, housed_likely_metric_statement, housed_compare_pop_percent_statement

@callback(
Output(component_id='sheltered_pit_1', component_property='children'),
Output(component_id='sheltered_pit_2', component_property='children'),
Output(component_id='unsheltered_pit_1', component_property='children'),
Output(component_id='unsheltered_pit_2', component_property='children'),
Input('pit-racial-equity-select-year', 'value'),
Input('pit-racial-equity-select-race', 'value')
)
def racial_equity_pit_data(selected_year, race_option):
    population_percent = {
        "White":.746,
        "Black, African American, or African":.056,
        'American Indian, Alaska Native, or Indigenous':.014,
        'Asian or Asian American':.129,
        'Native Hawaiian or Pacific Islander':0.006,
        'Multi-Racial':.049
    }
    sheltered_pit_1 = pit_data_likely_df[(pit_data_likely_df['Year'].values==selected_year) & (pit_data_likely_df['Race'].values==race_option) & (pit_data_likely_df['index'].values=='Sheltered')]['Likely Metric'].values[0]
    sheltered_likely_metric_statement = f"{race_option} clients are {'{:.0f}'.format(sheltered_pit_1)} times more likely to be Sheltered Homeless than Non-{race_option} clients"
    sheltered_pit_2 = pit_data_df[(pit_data_df['Year'].values==selected_year) & (pit_data_df['static_demographics.race_text'].values==race_option)]['Sheltered'].values[0]/pit_data_df[(pit_data_df['Year'].values==selected_year)]['Sheltered'].sum()
    sheltered_compare_pop_percent_statement = f"{race_option} clients make up {'{:.0%}'.format(population_percent[race_option])} of the general population in San Diego County but make up {'{:.0%}'.format(sheltered_pit_2)} of the Sheltered Homeless population."
    unsheltered_pit_1 = pit_data_likely_df[(pit_data_likely_df['Year'].values==selected_year) & (pit_data_likely_df['Race'].values==race_option) & (pit_data_likely_df['index'].values=='Unsheltered')]['Likely Metric'].values[0]
    unsheltered_likely_metric_statement = f"{race_option} clients are {'{:.0f}'.format(unsheltered_pit_1)} times more likely to be Unsheltered Homeless than Non-{race_option} clients"
    unsheltered_pit_2 = pit_data_df[(pit_data_df['Year'].values==selected_year) & (pit_data_df['static_demographics.race_text'].values==race_option)]['Unsheltered'].values[0]/pit_data_df[(pit_data_df['Year'].values==selected_year)]['Unsheltered'].sum()
    unsheltered_compare_pop_percent_statement = f"{race_option} clients make up {'{:.0%}'.format(population_percent[race_option])} of the general population in San Diego County but make up {'{:.0%}'.format(unsheltered_pit_2)} of the Unsheltered Homeless population."
    return sheltered_likely_metric_statement, sheltered_compare_pop_percent_statement, unsheltered_likely_metric_statement, unsheltered_compare_pop_percent_statement
