from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

block3 = html.Div(
            className="block-3",
            children=[
                dbc.Card(
                    style={'background-color': 'white', 'border': 'solid 1px white', 'color':'8D3188'},
                    children=[
                        dbc.CardHeader(html.H2(children="Who found housing?", className='display-4', style={"font-weight":"bolder"}), style={"font-weight":"bolder","background-color":'#8D3188', "color":"white"}),
                        dbc.CardBody(
                            children=[
                                dbc.Row(
                                    className="d-flex align-items-stretch mb-3",
                                    children=[
                                        dbc.Col(
                                            # className="card",
                                            width={"xl": 4, "md": 6, "sm": 12},
                                            children=[
                                                html.Div(                                                
                                                    children=[
                                                        html.H3(
                                                            id="housed_count_1",
                                                            className="metric display-4",
                                                            style={"font-weight":"bolder","background-color":'#8D3188', "color":"white"}
                                                        ),
                                                        html.H3(children="Persons Housed", className='display-4', style={"font-weight":"bolder","background-color":'#8D3188', "color":"white"}),
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                style={"font-weight":"bolder","background-color":'#8D3188', "color":"white"}),
                                dbc.Row(
                                    className="d-flex align-items-center",
                                    children=[
                                        dbc.Col(
                                            width={"xl": 4, "md": 6, "sm": 12},
                                            children=[
                                                html.Div(
                                                    className="section-3-subsection-2-top",
                                                    children=[
                                                        html.Div(
                                                            className="house-card",
                                                            children=[
                                                                html.Div(
                                                                    className="arrow-up",
                                                                    children=""
                                                                ),
                                                                html.Div(
                                                                    className="housed-metrics",
                                                                    children=[
                                                                        html.H4(
                                                                            className='display-5',
                                                                            id="senior_housed_count"
                                                                        ),
                                                                        html.H4(
                                                                            className="bar display-5",
                                                                            children="|",
                                                                        ),
                                                                        html.H4(
                                                                            className='display-5',
                                                                            children="Seniors"
                                                                            ),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="housed_plots display-4 mb-3",
                                                                    children=dcc.Graph(
                                                                        id="senior_housed_race_plot"
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        html.Div(
                                                            className="house-card",
                                                            children=[
                                                                html.Div(
                                                                    className="arrow-up",
                                                                    children=""
                                                                ),
                                                                html.Div(
                                                                    className="housed-metrics",
                                                                    children=[
                                                                        html.H4(
                                                                            id="tay_housed_count",
                                                                            className="display-5"
                                                                        ),
                                                                        html.H4(
                                                                            className="bar display-5",
                                                                            children="|",
                                                                        ),
                                                                        html.H4(
                                                                            children="Families",
                                                                            className="display-5"
                                                                        ),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="housed_plots display-4 mb-3",
                                                                    children=dcc.Graph(
                                                                        id="families_housed_race_plot"
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Col(
                                            width={"xl": 4, "md": 12, "sm": 12},
                                            children=[
                                                html.Div(
                                                    className="section-3-subsection-2-bottom",
                                                    children=[
                                                        html.Div(
                                                            className="house-card",
                                                            children=[
                                                                html.Div(
                                                                    className="arrow-up",
                                                                    children=""
                                                                ),
                                                                html.Div(
                                                                    className="housed-metrics",
                                                                    children=[
                                                                        html.H4(
                                                                            className='display-5',
                                                                            id="families_housed_count"
                                                                        ),
                                                                        html.H4(
                                                                            className="bar display-5",
                                                                            children="|",
                                                                        ),
                                                                        html.H4(
                                                                            className='display-5',
                                                                            children="TAY 18-24"
                                                                        ),
                                                                    ],
                                                                ),
                                                                html.Div(
                                                                    className="housed_plots display-4 mb-3",
                                                                    children=dcc.Graph(
                                                                        id="tay_housed_race_plot",
                                                                        style={
                                                                            "width": "auto",
                                                                            "height": "10vh",
                                                                        },
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                        html.Div(
                                                            className="house-card",
                                                            children=[
                                                                html.Div(
                                                                    className="arrow-up",
                                                                    children=""
                                                                ),
                                                                html.Div(
                                                                    className="housed-metrics",
                                                                    children=[
                                                                        html.H4(
                                                                            className='display-5',
                                                                            id="veterans_housed_count"
                                                                        ),
                                                                        html.H4(
                                                                            className="bar display-5",
                                                                            children="|",
                                                                        ),
                                                                html.H4(className='display-5', children="Veterans"),
                                                            ], #style={"font-weight":"bolder","background-color":'#8D3188', "color":"white"}
                                                        ),
                                                        html.Div(
                                                            className="housed_plots display-4 mb-3",
                                                            children=dcc.Graph(
                                                                id="veteran_housed_race_plot"
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ], 
                                ),
                                dbc.Row(
                                    children=[
                                        dbc.Col(
                                            width={"xl": 12, "md": 12, "sm": 12},
                                            children=[
                                                html.Div(
                                                    className="body-section-3-subsection-3",
                                                    children=[dcc.Graph(id="graph-with-slider")],
                                                )
                                            ],
                                        )
                                    ],
                                    className="mt-3",
                                ),
                            ]
                        ),
                    ],
                    className="w-100",
                )
            ]   
        )
    ]
)
