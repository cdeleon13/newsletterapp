import dash_bootstrap_components as dbc
from dash import html

pit_re_block = html.Div(
    children=[
        html.Div(
            className="re-block-1",
            children=[
                html.H2(
                        children=[html.P("PIT Population Percent Statement", className='display-6', style={"color":"white","background-color":"#0075C2"})]
                ),
                html.H1(
                        children=[html.P(id="race_equity_pit_statement", className='display-4', style={"color":"#0075C2"})]
                ), 
                html.H2(
                        children=[html.P("Racial Equity Statement on Sheltered PIT Data", className='display-6', style={"color":"white","background-color":"#F8C02A"})]
                ),
                html.H1(
                        children=[html.P(id="sheltered_pit_1", className='display-4', style={"color":"#F8C02A"})]
                ), 
                html.H2(
                        children=[html.P("Racial Equity Statement on Unsheltered PIT Data", className='display-6', style={"color":"white","background-color":"#8D3188"})]
                ),
                html.H1(
                        children=[html.P(id="unsheltered_pit_1", className='display-4', style={"color":"#8D3188"})]
                ),
                html.P("*The logic for constructing these equity statements was adopted from the Community Action Plan.") 
            ],
            style={"height": "100%"}
        ),
    ]
)
