# pit_racial_equity_block.py
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
                html.Div(id='equity_statements'),  # Container for conditionally displayed content
            ],
            style={"height": "100%"}
        ),
    ]
)
