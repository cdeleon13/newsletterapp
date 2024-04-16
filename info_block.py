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
                    html.Div(timeline_content, style={"border-left": f"2px solid #708090", "padding-left":"2vw", "margin-left":"1vw"}),                       
                ], width=8, style={"border": "2px solid #20AF90"}),
            ], style={"padding-bottom":"1vw"}, className="d-flex align-items-stretch"),
            ]),
    ],
)




# info_block = html.Div(
#     children=[
#         html.Div(
#             title="Inclusive Procurement",
#             children=[
#             dbc.Row([
#                 dbc.Col(html.H1("Inclusive Procurement", className='display-4', style={"background-color": "#0075C2", 'color': 'white', "display": "flex", "alignItems": "center", "justify-content":"center", "height": "100%"}), width=4),
#                 dbc.Col([
#                     html.P("""
#                         The RTFH designed a comprehensive inclusive procurement strategy to
#                         award state resources to prevent and end homelessness across the
#                         Continuum of Care. Some of the essential design components
#                         incorporated into the Inclusive Procurement strategy include:""", 
#                         style={"color": "darkslategrey", "font-weight":"light"}),
#                     inclusive_procurement,
#                     html.Div([
#                       html.H5("Leading by Example!", style={"padding-top":"1vw"}),
#                       html.P("""
#                              The RTFH hopes that its thoughtful approach to procurement serves as
#                              a model to other funders in the San Diego area. If all funders take similar
#                              approaches, the diversity of service providers in San Diego is sure to grow!""")
#                 ])                 
#                 ], width=8, style={"border": "2px solid #0075C2"}),
#             ], style={"padding-bottom":"1vw"}, className="d-flex align-items-stretch"),
#         ]),
        
#         # Row for Training and Education
#         html.Div(
#             title="Training and Education",
#             children=[
#             dbc.Row([
#                 dbc.Col(html.H1("Training and Education", className='display-4', style={"background-color": "#20AF90", 'color': 'white', "display": "flex", "alignItems": "center", "justify-content":"center", "height": "100%"}), width=4),
#                 dbc.Col([
#                     html.P("""
#                         The RTFH facilitated community listening sessions to gather insights into the training and 
#                         educational needs of the CoC to advance its equity objectives. Sessions centered around 
#                         identifying knowledge gaps, discussing desired transformations within the Continuum of Care, 
#                         and ensuring the provision of high-quality care specifically tailored to the needs of people 
#                         of color, with a particular focus on the Black people.""", 
#                         style={"color": "darkslategrey", "font-weight":"light"}),
#                     html.Ul([
#                         html.Li("The CoC membership set a goal for itself to be an Anti-Racist CoC.", style={"color": "darkslategrey", "font-weight":"light"}),
#                         html.Li("The Continuum of Care began this work by determining their values and exploring bias in the system.", style={"color": "darkslategrey", "font-weight":"light"}),
#                         html.Li("This work will continue in more targeted efforts and led by the membership through 2024.", style={"color": "darkslategrey", "font-weight":"light"}),
#                         html.Li("Authentic and honest conversations…….", style={"color": "darkslategrey", "font-weight":"light"}),
#                         html.Li("Not rushing the work-bias to act", style={"color": "darkslategrey", "font-weight":"light"}),
#                     ]),
#                     html.P("""
#                             The RTFH also incorporated an Equity track in the RTFH Conference. Member driven work: The RTFH is proud 
#                             that the bold goal of becoming an Anti-racist Continuum of Care was developed and is being driven by the 
#                             CoC membership.""", 
#                             style={"color": "darkslategrey", "font-weight":"light"}),
#                     html.H4("The Cultural Shift", className='display-6', style={"color":"#708090"}),
#                     html.Div(timeline_content, style={"border-left": f"2px solid #708090", "padding-left":"2vw", "margin-left":"1vw"}),                       
#                 ], width=8, style={"border": "2px solid #20AF90"}),
#             ], style={"padding-bottom":"1vw"}, className="d-flex align-items-stretch"),
#             ]),
#     ],
# )
#################################################################################
# Old text
        # dbc.Row([
        #     dbc.Col([html.H1("Supporting Black Led Organizations", className='display-4', style={"background-color": "#8D3188", 'color':'white', "display": "flex", "alignItems": "center", "justify-content":"center", "height": "100%"})],  width=4),
        #     dbc.Col([
        #         html.P("""
        #             The RTFH leadership strategized with black leaders in the fields of community organizing, 
        #             faith-based organizations, and reentry organizations who manage trusted community referral 
        #             networks for black people at risk of homelessness. The Ad Hoc Committee supported taking the 
        #             time to complete foundational work to map how these organizations support black people with 
        #             the goal of identifying coordinating partnership opportunities.""", 
        #             style={"color": "darkslategrey", "font-weight":"light"}),
        #         html.P("""
        #             The RTFH is expanding Coordinated Entry access points to include black led grassroots organizations 
        #             to ensure that black people at risk of homelessness have trusted community referral networks so that 
        #             they do not fall through the cracks of the homeless response system. Community Partnership: The work 
        #             to reduce the disparities experienced by black San Diegans experiencing homelessness does not begin 
        #             with the Continuum of Care, it begins in the community. Understanding, supporting, and not disrupting 
        #             the good work of these informal systems will help the Continuum of Care develop meaningful collaborations 
        #             between funders, informal partners, and homeless service providers.""", 
        #             style={"color": "darkslategrey", "font-weight":"light"}),
        #         html.P("""
        #             Our journey towards creating an inclusive and equitable community began with the acknowledgment that 
        #             black-led organizations play a pivotal role in driving social change. Recognizing this, we undertook an 
        #             informal system mapping to understand the landscape and identify avenues for support and collaboration. 
        #             This foundational work involved the partnership of notable stakeholders, each bringing unique perspectives and 
        #             strengths to the table:
        #             """, style={"color":"darkslategrey", "font-weight":"light"}),
        #         html.Ul([
        #             html.Li("BAPAC", style={"color":"darkslategrey", "font-weight":"light"}),
        #             html.Li("Monarch School", style={"color":"darkslategrey", "font-weight":"light"}),
        #             html.Li("Bishop Cornelius Bowser (Charity Apolistic Church and Founder of Shaphat)", style={"color":"darkslategrey", "font-weight":"light"}),
        #             html.Li("Meridian Baptist Church", style={"color":"darkslategrey", "font-weight":"light"}),
        #             html.Li("All of Us or None", style={"color":"darkslategrey", "font-weight":"light"}),
        #             html.Li("VVSD", style={"color":"darkslategrey", "font-weight":"light"}),
        #             html.Li("Eliza King", style={"color":"darkslategrey", "font-weight":"light"}),
        #         ], style={"padding-left": "20px"}),  # Adjust padding as needed
        #         html.P(
        #             """
        #             These collaborations have been instrumental in laying the groundwork for 
        #             further action, ensuring that our efforts are rooted in the needs and aspirations 
        #             of the communities we aim to serve.""", style={"color":"darkslategrey", "font-weight":"light"}
        #         ),
        #     ], width=8, style={"border": "2px solid #8D3188"})
        # ], style={"padding-bottom":"1vw"}, className="d-flex align-items-stretch"),
        # dbc.Row([
        #     dbc.Col([html.H1("Center the Voices of People with Lived Experience", className='display-4', style={"background-color": "#F8C02A", 'color':'white', "display": "flex", "alignItems": "center", "justify-content":"center", "height": "100%"})], width=4),
        #     dbc.Col([
        #         html.P("""
        #                 The RTFH identified funding to ensure that all people with lived experience are compensated 
        #                 for the time participating in committee work. People with lived experience who are leaders on 
        #                 the Ad Hoc Committee provided guidance on how to eliminate tokenism and achieve authentic community 
        #                 engagement.""", 
        #                 style={"color": "darkslategrey", "font-weight":"light"}),
        #         html.P("""
        #                 The RTFH has confirmed seats for people with lived experience on all of the CoC’s committees. 
        #                 Incorporating into application process.. thinking strategically about the deliberate and open 
        #                 pathways to recruitment. Authentic Engagement of People with Lived Experience: The RTFH has 
        #                 collaborated closely with leaders from the Ad Hoc Committee, who bring invaluable lived experience, 
        #                 to devise meaningful strategies for genuinely amplifying the voices and influence of individuals with 
        #                 lived experience. In many instances, communities face the risk of tokenism by engaging only a select 
        #                 few individuals with lived experience, merely to fulfill a checkbox requirement, without truly seeking 
        #                 to diversify representation across various subpopulations with distinct experiences. Conversely, 
        #                 individuals with lived experience are occasionally placed into decision-making roles without the 
        #                 necessary context and support for meaningful engagement. The RTFH is committed to avoiding these pitfalls 
        #                 in designing strategies for people with lived experience to authentically engage in every part of Continuum 
        #                 of Care work.""", 
        #                 style={"color": "darkslategrey", "font-weight":"light"}),
        #     ], width=8, style={"border": "2px solid #F8C02A"})
        # ], style={"padding-bottom":"1vw"}, className="d-flex align-items-stretch"),
        # dbc.Row([
        #     dbc.Col([html.H1("Transforming the Crisis Response System", className='display-4', style={"background-color": "#00CED1", 'color':'white', "display": "flex", "alignItems": "center", "justify-content":"center", "height": "100%"})], width=4),
        #     dbc.Col([
        #         html.P("""
        #                 The Ad Hoc Committee conducted a deep exploration of the results from the CBPP data analysis referenced 
        #                 in the Data Dashboard section. The committee is helping to design a pilot program using proxies for race 
        #                 to target housing resources to black San Diegans. Determining program eligibility using proxies for race 
        #                 involves identifying and leveraging indicators or characteristics strongly correlated with race to ensure 
        #                 equitable access to housing.""", 
        #                 style={"color": "darkslategrey", "font-weight":"light"}),
        #         html.P("""
        #                 Bold and Transformative Work: The RTFH, alongside the Ad Hoc Committee, has dedicated extensive time and 
        #                 effort to meticulously examine methodologies and indicators suitable as proxies for race in San Diego. 
        #                 This initiative aims to address historical disparities faced by Black people, who have often been marginalized 
        #                 in accessing permanent supportive housing resources due to deep-seated mistrust in mainstream systems, 
        #                 including the homeless system. Through collaborative efforts with community partners, we have identified 
        #                 proxies relevant to San Diego, offering innovative approaches to effectively target housing to Black 
        #                 individuals in unprecedented ways. This pilot also involves the redesign of a Rapid Rehousing strategy, 
        #                 which in its current permutation falls short of meeting the diverse needs of the CoC. While this undertaking 
        #                 demands substantial time and resources from the RTFH, we firmly believe it is a worthwhile investment. 
        #                 Through these strategic pilot efforts, we aspire to create pathways that address the longstanding inequities 
        #                 faced by Black San Diegans experiencing homelessness.""", 
        #                 style={"color": "darkslategrey", "font-weight":"light"}),
        #     ], width=8, style={"border": "2px solid #00CED1"}),
        # ], style={"padding-bottom":"1vw"}, className="d-flex align-items-stretch")
