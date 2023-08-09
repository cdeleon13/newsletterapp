import dash_bootstrap_components as dbc
from dash import html

accordion_block = html.Div(
    children=[
        html.Div(
            className="re-block-1",
            children=[
                dbc.Card([
                    dbc.CardHeader(["Racial Equity Statements on First Time Homeless in HMIS"], className='display-4 text-white'),
                    dbc.CardBody(
                        children=[
                            dbc.Row(
                                children=[
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardHeader(["Population Percent Statement"], className='display-5'),
                                            dbc.CardBody([
                                                html.P(id="fth_compare_pop_percent"),
                                            ])
                                        ]),
                                    ]),
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardHeader(["Likelihood Statement"], className='display-5'),
                                            dbc.CardBody([
                                                html.P(id="fth_likely_statement"),
                                            ])
                                        ])
                                    ]),
                                ]
                            )
                        ],
                    )
                ], style={
                    'margin':'15px 0',
                    "background-color":'#4485a1'
                    }),
                dbc.Card([
                    dbc.CardHeader(["Racial Equity Statements on Active Clients in HMIS"], className='display-4 text-white'),
                    dbc.CardBody(
                        children=[
                            dbc.Row(
                                children=[
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardHeader(["Population Percent Statement"], className='display-5'),
                                            dbc.CardBody([
                                                html.P(id="active_compare_pop_percent"),
                                            ])
                                        ]),
                                    ]),
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardHeader(["Likelihood Statement"], className='display-5'),
                                            dbc.CardBody(
                                                children=[
                                                    html.P(id="active_likely_statement"),
                                                ]
                                            )
                                        ])
                                    ]),
                                ]
                            )
                        ],
                    )
                ], style={
                    'margin':'15px 0',
                    "background-color":'#F6C033'
                    }),
                dbc.Card([
                    dbc.CardHeader(["Racial Equity Statements on Housed Clients in HMIS"], className='display-4 text-white'),
                    dbc.CardBody(
                        children=[
                            dbc.Row(
                                children=[
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardHeader(["Population Percent Statement"], className='display-5'),
                                            dbc.CardBody([
                                                html.P(id="housed_compare_pop_percent"),
                                            ])
                                        ]),
                                    ]),
                                    dbc.Col([
                                        dbc.Card([
                                            dbc.CardHeader(["Likelihood Statement"], className='display-5'),
                                            dbc.CardBody(
                                                children=[
                                                    html.P(id="housed_likely_statement"),
                                                ]
                                            )
                                        ])
                                    ]),
                                ]
                            )
                        ],
                    )
                ], style={
                    'margin':'15px 0',
                    'background-color':'#71a6c5'
                    }),
            ]
        )
    ]
)

