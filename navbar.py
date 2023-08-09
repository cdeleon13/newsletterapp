import dash_bootstrap_components as dbc
from dash import dcc, html, page_registry

# List comprehension to create nav items for each page
nav_items = [
    dbc.NavItem(
        dbc.NavLink(
            dcc.Link(f"{page['name']}", href=page["relative_path"])
        )
    ) for page in page_registry.values()
]

navbar = dbc.NavbarSimple(
    children=nav_items,  # Pass the list of nav items here
    brand="RTFHSD",
    brand_href="#",
    color="primary",
    dark=True,
)
