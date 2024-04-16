# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output, page_registry, page_container, register_page, callback
import plotly.express as px
import pandas as pd

from datetime import datetime
import dash_bootstrap_components as dbc
from dash import html

### Local modules
# from data_loader import load_newsletter_data
# from newsletter_filters import filters_section
from block1 import block1
from block2 import block2
from block3 import block3
from pit_racial_equity_block import pit_re_block


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

# def load_data():
#     base_url = '/Users/cristiandeleon/multi_page_newsletter_dashboard_v2/env/Interactive Newsletter Files/assets/2024-03-20/'

#     newsletter_housed_counts_by_destination_url = base_url + 'newsletter_housed_counts_by_destination_by_race.csv'
#     newsletter_housed_counts_by_destination_df = pd.read_csv(newsletter_housed_counts_by_destination_url)

#     newsletter_counts_by_race_url = base_url + 'newsletter_counts_by_race.csv'
#     newsletter_counts_by_race_df1 = pd.read_csv(newsletter_counts_by_race_url)
#     old_cols = [x for x in newsletter_counts_by_race_df1.columns if 'by Race' in x]
#     new_cols = [x.replace(" by Race", "") for x in newsletter_counts_by_race_df1 if 'by Race' in x]
#     newsletter_counts_by_race_df1 = newsletter_counts_by_race_df1.rename(columns=dict(zip(old_cols, new_cols)))

#     newsletter_active_counts_by_proj_type_by_race_url = base_url + 'newsletter_active_counts_by_proj_type_by_race.csv'
#     newsletter_active_counts_by_proj_type_by_race = pd.read_csv(newsletter_active_counts_by_proj_type_by_race_url)

#     pit_data_likely_url = base_url + 'pit_data_likely_df.csv'
#     pit_data_likely_df = pd.read_csv(pit_data_likely_url)
#     pit_data_url = base_url + 'pit_data_df.csv'
#     pit_data_df = pd.read_csv(pit_data_url)
    
#     race_picklist = sorted(list(newsletter_counts_by_race_df1['static_demographics.race_text'].unique()))
#     return (
#         newsletter_housed_counts_by_destination_df, 
#         newsletter_counts_by_race_df1, 
#         newsletter_active_counts_by_proj_type_by_race, 
#         pit_data_likely_df,
#         pit_data_df,
#         race_picklist)


# (newsletter_housed_counts_by_destination_df, 
# newsletter_counts_by_race_df1, 
# newsletter_active_counts_by_proj_type_by_race, 
# pit_data_likely_df,
# pit_data_df,
# race_picklist) = load_data()

###
# | END
# | data_loader.py
###

###
# | racial_equity_filters.py
###
years_list = sorted(list(set(pit_data_likely_df['Year']).union(set(pit_data_likely_df['Year']))))
# proj_type_list = sorted([x for x in list(set(binary_race_data_counts_df.columns).union(set(binary_race_likeliness_data_df.columns))) if x not in ['Binary Race Variable',  'Unnamed: 0', 'Year']])
race_variable_list = [x for x in sorted(pit_data_likely_df['Race'].unique()) if not x.startswith('Non-')]


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
                                value="Black, African American, or African",
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
        pit_re_filters_section,
        pit_re_block
    ], style={"z-index":-1}
)


@callback(
Output(component_id='sheltered_pit_1', component_property='children'),
Output(component_id='unsheltered_pit_1', component_property='children'),
Output(component_id='race_equity_pit_statement', component_property='children'),
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
    if race_option in ["Black, African American, or African", "White"]:
        sheltered_pit_1 = pit_data_likely_df[(pit_data_likely_df['Year'].values==selected_year) & (pit_data_likely_df['Race'].values==race_option) & (pit_data_likely_df['index'].values=='Sheltered')]['Likely Metric'].values[0]
        if sheltered_pit_1>1:
            sheltered_likely_metric_statement = f"{race_option} clients are {'{:.1f}'.format(sheltered_pit_1)} times more likely to experience Sheltered Homelessness than Non-{race_option} clients"
        elif sheltered_pit_1>0 and sheltered_pit_1<1:
            sheltered_likely_metric_statement = f"{race_option} clients are {'{:.1f}'.format(sheltered_pit_1)} times less likely to be Sheltered Homeless than Non-{race_option} clients"
        elif sheltered_pit_1==1:
            sheltered_likely_metric_statement = f"{race_option} clients are as likely to be Sheltered Homeless than Non-{race_option} clients"
        else: 
            sheltered_likely_metric_statement = "No data available."

        unsheltered_pit_1 = pit_data_likely_df[(pit_data_likely_df['Year'].values==selected_year) & (pit_data_likely_df['Race'].values==race_option) & (pit_data_likely_df['index'].values=='Unsheltered')]['Likely Metric'].values[0]
        if unsheltered_pit_1>1:
            unsheltered_likely_metric_statement = f"{race_option} clients are {'{:.1f}'.format(unsheltered_pit_1)} times more likely to experience Unsheltered Homelessness than Non-{race_option} clients"
        elif unsheltered_pit_1>0 and unsheltered_pit_1<1:
            unsheltered_likely_metric_statement = f"{race_option} clients are {'{:.1f}'.format(unsheltered_pit_1)} times more likely to experience Unsheltered Homelessness than Non-{race_option} clients"
        elif unsheltered_pit_1==1:
            unsheltered_likely_metric_statement = f"{race_option} clients are {'{:.1f}'.format(unsheltered_pit_1)} times more likely to experience Unsheltered Homelessness than Non-{race_option} clients"
        else:
            unsheltered_likely_metric_statement = "No data available."
    else:
        sheltered_likely_metric_statement = "There is not sufficient data to make this assessment."
        unsheltered_likely_metric_statement = "There is not sufficient data to make this assessment."

    # Compare population percent statement
    total_pit_data = pit_data_df[(pit_data_df['Year'].values==selected_year) & (pit_data_df['static_demographics.race_text'].values==race_option)]['Total'].values[0]/pit_data_df[(pit_data_df['Year'].values==selected_year)]['Total'].sum()
    if total_pit_data>0:
        compare_pop_percent_statement = [html.B(f"{race_option} clients"),f" make up {'{:.1%}'.format(population_percent[race_option])} of the general population in San Diego County but ", html.B(f"make up {'{:.1%}'.format(total_pit_data)} of the Homeless population."),]
        # compare_pop_percent_statement = f"<b>{race_option} clients</b> make up {'{:.1%}'.format(population_percent[race_option])} of the general population in San Diego County but <b>make up {'{:.1%}'.format(total_pit_data)} of the Homeless population</b>."
    else:
        compare_pop_percent_statement = "No data available."


    # return sheltered_likely_metric_statement, sheltered_compare_pop_percent_statement, unsheltered_likely_metric_statement, unsheltered_compare_pop_percent_statement
    return sheltered_likely_metric_statement, unsheltered_likely_metric_statement, compare_pop_percent_statement
