from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc


block2 = html.Div(
    className="block-2",
    children=[
        dbc.Card(
            style={'background-color': '#153654', 'border': '1px solid white'},
            children=[
                dbc.CardHeader(
                    html.H2(children="Who's active?", className='display-4', style={'color': 'white'})
                ),
                dbc.CardBody(
                    children=[
                        dbc.Container(
                            className="body-section-2-subsection-1",
                            children=[
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            className="mb-3",
                                            width={"xl": 3, "lg": 6, "md": 6},
                                            children=[
                                                html.H3(id="seniors_active_count", className='display-4', style={'color': 'white'}),
                                                html.H3(children="Seniors (55+) Served", className='display-5', style={'color': 'white'}),
                                                html.Div(
                                                    className='housed_plots',
                                                    children=dcc.Graph(id='senior_active_race_plot', config={'displayModeBar': False}),
                                                ),
                                            ]
                                        ),
                                        dbc.Col(
                                            className="mb-3",
                                            width={"xl": 3, "lg": 6, "md": 6},
                                            children=[
                                                html.H3(id="families_active_count", className='display-4', style={'color': 'white'}),
                                                html.H3(children="Families Served", className='display-5', style={'color': 'white'}),
                                                html.Div(
                                                    className='housed_plots',
                                                    children=dcc.Graph(id='families_active_race_plot', config={'displayModeBar': False}),
                                                ),
                                            ]
                                        ),
                                        dbc.Col(
                                            className="mb-3",
                                            width={"xl": 3, "lg": 6, "md": 6},
                                            children=[
                                                html.H3(id="tay_active_count", className='display-4', style={'color': 'white'}),
                                                html.H3(children="TAY (18-24) Served", className='display-5', style={'color': 'white'}),
                                                html.Div(
                                                    className='housed_plots',
                                                    children=dcc.Graph(id='tay_active_race_plot', config={'displayModeBar': False}),
                                                ),
                                            ]
                                        ),
                                        dbc.Col(
                                            className="mb-3",
                                            width={"xl": 3, "lg": 6, "md": 6},
                                            children=[
                                                html.H3(id="veterans_active_count", className='display-4', style={'color': 'white'}),
                                                html.H3(children="Veterans Served", className='display-5', style={'color': 'white'}),
                                                html.Div(
                                                    className='housed_plots',
                                                    children=dcc.Graph(id='veteran_active_race_plot', config={'displayModeBar': False}),
                                                ),
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        dbc.CardBody(
                            className="body-section-2-subsection-2",
                            children=[
                                html.Div(
                                    className='active-card active-card-center d-flex flex-column mb-3 justify-content-around align-items-center',
                                    children=[
                                        html.Div(className='active-card align-self-stretch', id='active-card-center', children=[
                                            html.Div(className='card active-card-container', children=[
                                                html.Div(className='active-card-top', children=[
                                                    html.Div(id="active_count", className="active-metric-1 display-4", style={'color': '#153654'}),
                                                    html.Div(className="active-text-1 display-4", children="Total Active Clients", style={'color': '#153654'}),
                                                ]),
                                            ]),
                                        ]),
                                        html.Div(className='active-graph', children=[dcc.Graph(id='active_counts_pie')]),
                                    ]
                                ),
                            ]
                        ),
                    ]
                ),
            ],
            className="w-100",
        ),
    ]
)