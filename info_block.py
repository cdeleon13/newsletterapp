import dash_bootstrap_components as dbc
from dash import html

inclusive_procurement = html.Div(
    style={
        'display': 'flex',
        'flex-direction': 'row',
        "justify-content":"center",
        "flex-wrap":"wrap",
        "gap":"0",
        "flex-grow":"1 1 1 1",
        "align-items":"stretch",
        "padding": "0 27.5%",
        "margin":"0",
        "box-sizing": "border-box"  # Ensures padding and border are included in dimensions
    },
    children=[
        dbc.Row([
            dbc.Col(
                html.Div(
                    html.H5("Weighting and Valuing Equity", className='text-center training_pie', style={"padding-bottom":"1vw"}),
                    style={
                        "color": "white",
                        "background-color": "#8D3188",
                    #     "margin": "0",
                    #     "padding": "0",
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "flex-end",
                        "flex-direction": "column",
                        "border": "5px solid #8D3188",
                        "border-radius": "100% 0 0 0",
                        "width": "14vw",
                        "height": "14vw"
                    }
                    ),
                md=6, sm=6, xs=6,
            ),
            dbc.Col(
                html.Div(
                    html.H5("Simplified Application Processes", className='text-center training_pie', style={"padding-bottom":"1vw"}),
                    style={
                        "color": "white",
                        "background-color": "#00CED1",
                        # "margin": "0",
                        # "padding": "0",
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "flex-end",
                        "flex-direction": "column",
                        "border": "5px solid #00CED1",
                        "border-radius": "0 100% 0 0",
                        "width": "14vw",
                        "height": "14vw"
                    }),
                md=6, sm=6, xs=6
            ),
        ]),
        dbc.Row([
            dbc.Col(
                html.Div(
                    html.H5("Capacity Building Support", className='text-center training_pie', style={"padding-top":"1vw"}),
                    style={
                        "color": "white",
                        "background-color": "#F8C02A",
                        # "margin": "0",
                        # "padding": "0",
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "flex-start",
                        "flex-direction": "column",
                        "border": "5px solid #F8C02A",
                        "border-radius": "0 0 0 100%",
                        "width": "14vw",
                        "height": "14vw"
                    }),
                md=6, sm=6, xs=6
            ),
            dbc.Col(
                html.Div(
                    html.H5("Transparent and Targeted Communication", className='text-center training_pie', style={"padding-top":"1vw"}),
                    style={
                        "color": "white",
                        "background-color": "#0075C2",
                        # "margin": "0",
                        # "padding": "0",
                        "display": "flex",
                        "align-items": "center",
                        "justify-content": "flex-start",
                        "flex-direction": "column",
                        "border": "5px solid #0075C2",
                        "border-radius": "0 0 100% 0",
                        "width": "14vw",
                        "height": "14vw"
                    }),
                md=6, sm=6, xs=6
            )
        ], style={"padding-top":"2px"})
    ]
)


timeline_events = [
    # Previous events remain unchanged
    {
        "date": "July 25, 2023",
        "session": "CoC Listening Session",
        "description": """
            This session was attended by 48 individuals from 25 organizations, 
            and provided a platform for fostering a collective understanding of the 
            challenges and opportunities in advancing racial equity.""",
        "color": "#20AF90"
    },
    {
        "date": "October 12, 2023",
        "session": "Cultural Shift Session",
        "description": """
            Building on the momentum, the Cultural Shift Session witnessed an overwhelming participation 
            of 107 individuals from 33 organizations. This gathering was a testament to the growing 
            commitment among stakeholders to engage in meaningful dialogue and action towards cultural 
            transformation.""",
        "color": "#20AF90"
    },
    # Updated "Stakeholder Meetings" event
    {
        "date": "Year-Round",
        "session": "Stakeholder Meetings",
        "description": """
            Our engagement extended to meetings with key stakeholders, including:""",
        "color": "#20AF90",
        "stakeholders": [
            "City of San Diego Equity Officer",
            "County of San Diego Equity Officer",
            "City of San Diego Districts 4 and 9",
            "CAPH Implementation Team",
            "San Diego Housing Commission",
            "City of San Diego",
            "RTFH",
            "County of San Diego"
        ],
        "additional_info": """
            These meetings were crucial in aligning efforts and forging partnerships across 
            different levels of governance and sectors, underscoring the collective resolve 
            to achieve racial equity."""
    },
    # Add other events similarly
]

timeline_content = []
for event in timeline_events:
    card_content = [
        html.Div(event["date"], className='display-6', style={"color": event["color"]}),
        html.Div([
            html.P(event["session"], className='display-5', style={"color": event["color"]}),
            html.P(event["description"], style={"color": "darkslategrey", "font-weight": "light"}),
            # Check if stakeholders list exists and render it
            html.Ul([html.Li(stakeholder, style={"color": "darkslategrey", "font-weight": "light"}) for stakeholder in event.get("stakeholders", [])]) if "stakeholders" in event else None,
            html.P(event.get("additional_info", ""), style={"color": "darkslategrey", "font-weight": "light"}) if "additional_info" in event else None,
        ], style={"padding-left":"10vw"})
    ]
    timeline_content.append(html.Div(card_content, className="mb-3"))
info_block = html.Div(
    children=[
        html.Div(
            title="Inclusive Procurement",
            children=[
            dbc.Row([
                dbc.Col(html.H1("Inclusive Procurement", className='display-4', style={"background-color": "#0075C2", 'color': 'white', "display": "flex", "alignItems": "center", "justify-content":"center", "height": "100%"}), width=4),
                dbc.Col([
                    html.P("""
                        The RTFH designed a comprehensive inclusive procurement strategy to
                        award state resources to prevent and end homelessness across the
                        Continuum of Care. Some of the essential design components
                        incorporated into the Inclusive Procurement strategy include:""", 
                        style={"color": "darkslategrey", "font-weight":"light"}),
                    inclusive_procurement,
                    html.Div([
                      html.H5("Leading by Example!", style={"padding-top":"1vw"}),
                      html.P("""
                             The RTFH hopes that its thoughtful approach to procurement serves as
                             a model to other funders in the San Diego area. If all funders take similar
                             approaches, the diversity of service providers in San Diego is sure to grow!""")
                ])                 
                ], width=8, style={"border": "2px solid #0075C2"}),
            ], style={"padding-bottom":"1vw"}, className="d-flex align-items-stretch"),
        ]),
        
        # Row for Training and Education
        html.Div(
            title="Training and Education",
            children=[
            dbc.Row([
                dbc.Col(html.H1("Training and Education", className='display-4', style={"background-color": "#20AF90", 'color': 'white', "display": "flex", "alignItems": "center", "justify-content":"center", "height": "100%"}), width=4),
                dbc.Col([
                    html.H4("The Cultural Shift", className='display-6', style={"color":"#708090"}),
                    html.Img(src="assets/action_items_timeline.png", style={"width":"100%"})
                #     html.Div(timeline_content, style={"border-left": f"2px solid #708090", "padding-left":"2vw", "margin-left":"1vw"}),                       
                ], width=8, style={"border": "2px solid #20AF90"}),
            ], style={"padding-bottom":"1vw"}, className="d-flex align-items-stretch"),
            ]),
    ],
)
