import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html
import webbrowser
from PyMovieDb import IMDB
import json

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(id="search-input", type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", id="search-button", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://plotly.com",
                style={"textDecoration": "none"},
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        navbar,
        html.Br(),
        html.H1("Test App"),
        html.Div(id="output-div"),
    ]
)

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

# callback to redirect user to Google with the input value
@app.callback(
    Output("output-div", "children"),
    [Input("search-button", "n_clicks")],
    [State("search-input", "value")],
)
def redirect_to_google(n_clicks, input_value):
    imdb = IMDB()
    if n_clicks > 0 and input_value:
        string = imdb.search(input_value)
        if string=='{\n  "result_count": 0,\n  "results": []\n}':
            url='https://www.imdb.com/title/tt029046rr502/?ref_=fn_al_tt_1'
        else:
            res=json.loads(string)
            url=res["results"][0]['url']
        webbrowser.open(url, new=2)
    return ""

if __name__ == "__main__":
    app.run_server(debug=True)
