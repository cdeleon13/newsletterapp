# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output, page_registry, page_container
import plotly.express as px
import pandas as pd

from datetime import datetime
import dash_bootstrap_components as dbc

### Local modules
# from data_loader import load_newsletter_data
# from newsletter_filters import filters_section
from block1 import block1
from block2 import block2
from block3 import block3
from racial_equity_block import accordion_block
from pit_racial_equity_block import pit_re_block
# from navbar import navbar
# from racial_equity_filters import re_filters_section

import requests
from io import StringIO

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True, suppress_callback_exceptions=True)
app.title = "HMIS Newsletter Dashboard"
server = app.server

# Specify the favicon
favicon = "path/to/favicon.ico"

# List comprehension to create nav items for each page
nav_items = [
    dbc.NavItem(
        dbc.NavLink(
            dcc.Link(f"{page['name']}", href=page["relative_path"], className="white-link")
        )
    ) for page in page_registry.values()]




import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

RTFH_LOGO = "assets/rtfh_logo.png"

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                html.Img(src=RTFH_LOGO, height="80vh"), href="/", className="navbar-brand"
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                dbc.Nav(
                    nav_items,
                    className="ml-auto",  # Align the links to the right
                    navbar=True,
                ),
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-3",
)


app.layout = html.Div([
    navbar,
    page_container,
    html.Footer(
        html.Img(
            src="assets/navbar_bg.png",
            style={"width": "100%", "height": "auto", "object-fit": "cover"}
        ),
        style={"background-color":"white"},
    ),
])

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
