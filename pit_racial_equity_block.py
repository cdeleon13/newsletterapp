import dash_bootstrap_components as dbc
from dash import html

pit_re_block = html.Div(
    children=[
        html.Div(
            className="re-block-1",
            children=[
                dbc.Card(
                    [
                        dbc.CardHeader("Racial Equity Statements for PIT Data", className='display-4'),
                        dbc.CardBody(
                            [
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Card(
                                                [
                                                    dbc.CardHeader("Sheltered PIT Data", className='display-5'),
                                                    dbc.CardBody(
                                                        children=[
                                                            html.P(id='sheltered_pit_2'),
                                                            html.P(id='sheltered_pit_1'),
                                                            
                                                        ]
                                                    )
                                                ], 
                                            ),
                                            width=12, sm=12, md=6, lg=6, xl=6
                                        ),
                                        dbc.Col(
                                            dbc.Card(
                                                [
                                                    dbc.CardHeader("Unsheltered PIT Data", className='display-5'),
                                                    dbc.CardBody(
                                                        children=[
                                                            html.P(id='unsheltered_pit_2'),
                                                            html.P(id='unsheltered_pit_1'),
                                                        ]
                                                    )
                                                ],
                                            ),
                                            width=12, sm=12, md=6, lg=6, xl=6
                                        ),
                                    ],
                                ),
                            ],
                            style={"height": "100%"}
                        ),
                    ],
                    style={
                        "background-color": "#BED9EC",
                        "border-color": "#36413E",
                        "opacity": "0.9",
                    }
                ),
            ],
            style={"height": "100%"}
        ),
    ]
)