# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output, page_registry, page_container, register_page, callback
import plotly.express as px
import pandas as pd

from datetime import datetime
import dash_bootstrap_components as dbc
from dash import html

### Local modules
# from data_loader import load_newsletter_data
# from newsletter_filters import filters_section
from block1 import block1
from block2 import block2
from block3 import block3
from racial_equity_block import accordion_block
from pit_racial_equity_block import pit_re_block
from info_block import info_block
# from navbar import navbar
# from racial_equity_filters import re_filters_section

import requests
from io import StringIO

register_page(
    __name__,
    path='/info-page',
    title='Action Items',
    name='Action Items'
)

layout = dbc.Container(
    children=[
        info_block
    ], style={"z-index":-1}
)
