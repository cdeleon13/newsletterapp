import dash_bootstrap_components as dbc
from dash import html

pit_re_block = html.Div(
    children=[
        html.Div(
            className="re-block-1",
            children=[
                dbc.Card(
                    children=[
                        dbc.CardHeader("Racial Equity Statements on Sheltered PIT Data", className='display-4 text-white'),
                        dbc.CardBody(
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            dbc.Card(
                                                children=[
                                                    dbc.CardHeader(children="Population Percent Statement"),
                                                    dbc.CardBody(html.P(id='sheltered_pit_2'))
                                                ], className="mb-3"
                                            ),
                                        ),
                                        dbc.Col(
                                            dbc.Card(
                                                children=[
                                                    dbc.CardHeader("Likelihood Statement"),
                                                    dbc.CardBody(html.P(id='sheltered_pit_1'))
                                                ]
                                            ),
                                        )
                                    ]
                                )
                            ],                                                    
                        )
                    ], color="#334E58", outline=False, style={"margin":"1vw 0"}
                ),   
                
                dbc.Card(
                    children=[
                        dbc.CardHeader("Racial Equity Statements on Unsheltered PIT Data", className='display-4 text-dark'),
                        dbc.CardBody(
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            dbc.Card(
                                                children=[
                                                    dbc.CardHeader("Population Percent Statement"),
                                                    dbc.CardBody(html.P(id='unsheltered_pit_2'))
                                                ],
                                            ),
                                        ),
                                        dbc.Col(
                                            dbc.Card(
                                                children=[
                                                    dbc.CardHeader("Likelihood Statement"),
                                                    dbc.CardBody(html.P(id='unsheltered_pit_1'))
                                                ]
                                            ),
                                        )
                                    ]
                                )
                            ]                                                        
                        )
                    ], color="#BED9EC", outline=False, style={"margin":"1vw 0"}
                ),
            ],
            style={"height": "100%"}
        ),
    ]
)
