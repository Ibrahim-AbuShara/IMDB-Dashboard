import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Navbar
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="https://ia.media-imdb.com/images/M/MV5BMTk3ODA4Mjc0NF5BMl5BcG5nXkFtZTgwNDc1MzQ2OTE@._V1_.png",
                                         height="35px")),
                        dbc.Col(dbc.NavbarBrand("IMDb Dashboard", className="ml-auto")),
                    ],
                    align="center",
                 
                ),
               
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
            dbc.Collapse(
                dbc.Nav(
                    [
                        dbc.NavItem(dbc.NavLink("Home", href="/", active="exact")),
                        dbc.DropdownMenu(
                            [
                                dbc.DropdownMenuItem("Action", href="#", className="animated fadeInUp"),
                                dbc.DropdownMenuItem("Comedy", href="#", className="animated fadeInUp"),
                                dbc.DropdownMenuItem("Drama", href="#", className="animated fadeInUp"),
                            ],
                            nav=True,
                            in_navbar=True,
                            label="Genres",
                        ),
                    ],
                    className="ml-auto",
                    navbar=True,
                ),
                id="navbar-collapse",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    sticky='top'
)

# Movie Popularity Graph
movie_popularity = dbc.Col(
                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Bar(
                                    x=["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"],
                                    y=[10, 8, 6, 4, 2],
                                    marker=dict(color='indianred')
                                )
                            ],
                            layout=go.Layout(
                                xaxis=dict(showgrid=False),
                                yaxis=dict(showgrid=False),
                                plot_bgcolor='rgba(0,0,0,0)', # set opacity of the plot background
                                paper_bgcolor='rgba(0,0,0,0.7)', # set opacity of the paper background
                                font=dict(color='white')
                            )
                        ),
                        config=dict(displayModeBar=False),
                        style={"height": "350px"}
                    ),
                    width=6
                )

# Movie Budgets Graph
movie_budgets = dbc.Col(
                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Bar(
                                    x=["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"],
                                    y=[5000000, 3000000, 8000000, 6000000, 4000000],
                                    marker=dict(color='mediumseagreen')
                                )
                            ],
                            layout=go.Layout(
                                xaxis=dict(showgrid=False),
                                yaxis=dict(showgrid=False),
                                plot_bgcolor='rgba(0,0,0,0)', # set opacity of the plot background
                                paper_bgcolor='rgba(0,0,0,0.7)', # set opacity of the paper background
                                font=dict(color='white')
                            )
                        ),
                        config=dict(displayModeBar=False),
                        style={"height": "350px"}
                    ),
                    width=6
                )
movie_budgets2 = dbc.Col(
                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Bar(
                                    x=["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"],
                                    y=[5000000, 3000000, 8000000, 6000000, 4000000],
                                    marker=dict(color='mediumseagreen')
                                )
                            ],
                            layout=go.Layout(
                                xaxis=dict(showgrid=False),
                                yaxis=dict(showgrid=False),
                                plot_bgcolor='rgba(0,0,0,0)', # set opacity of the plot background
                                paper_bgcolor='rgba(0,0,0,0.7)', # set opacity of the paper background
                                font=dict(color='white')
                            )
                        ),
                        config=dict(displayModeBar=False),
                        style={"height": "350px"}
                    ),
                    width=6
                )
movie_budgets3 = dbc.Col(
                    dcc.Graph(
                        figure=go.Figure(
                            data=[
                                go.Bar(
                                    x=["Movie 1", "Movie 2", "Movie 3", "Movie 4", "Movie 5"],
                                    y=[5000000, 3000000, 8000000, 6000000, 4000000],
                                    marker=dict(color='mediumseagreen')
                                )
                            ],
                            layout=go.Layout(
                                xaxis=dict(showgrid=False),
                                yaxis=dict(showgrid=False),
                                plot_bgcolor='rgba(0,0,0,0)', # set opacity of the plot background
                                paper_bgcolor='rgba(0,0,0,0.7)', # set opacity of the paper background
                                font=dict(color='white')
                            )
                        ),
                        config=dict(displayModeBar=False),
                        style={"height": "350px"}
                    ),
                    width=6
                )

# App layout
app.layout = html.Div(
    [
        navbar,
        dbc.Container(
            [
                html.Br(),
                dbc.Row(
                    [
                        movie_popularity,
                        movie_budgets,
                        
                           
                    ]
                
                ),
                 html.Br(),
                dbc.Row([movie_budgets2,
                        movie_budgets3])
            ],
            fluid=True,
            style={
                "padding": "0px",
                "background-repeat": "no-repeat",
                "background-size": "cover",
                "height": "800px",
                "background-position": "center center",
                "background-attachment": "fixed",
                "position": "relative",
                "backdrop-filter": "blur(5px)",
            }
        ),
    ],
    style={
        "background-color": "rgba(0, 0, 0, 0.5)",
        "position": "relative",
        "z-index": "1",
        "background-image": "url('https://wallpapercave.com/wp/wp5483697.jpg')",
        "backdrop-filter": "blur(1px)",
    }
)

if __name__ == "__main__":
    app.run_server(debug=True)