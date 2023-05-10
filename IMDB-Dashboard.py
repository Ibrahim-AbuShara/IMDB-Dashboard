import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from dash.dependencies import Input,Output,State
import pandas as pd
from fun import  *

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
        figure=rating_genre().update_layout(
            geo=dict(
                bgcolor='rgba(0,0,0,0.01)', # set background color to black
                showland=True,
                showocean=True,
                oceancolor='rgba(0,0,0,0.07)'
            ),
            plot_bgcolor='rgba(0,0,0,0.01)', # set plot background color to black
            paper_bgcolor='rgba(0,0,0,0.7)', # set paper background color to black
            font_color='white' # set font color to white
        )
    ),
    width=6
)

# Movie Budgets Graph
movie_budgets =  dbc.Col(
    dcc.Graph(
        figure=groth().update_layout(
            geo=dict(
                bgcolor='rgba(0,0,0,0.01)', # set background color to black
                showland=True,
                showocean=True,
                oceancolor='rgba(0,0,0,0.07)'
            ),
            plot_bgcolor='rgba(0,0,0,0.01)', # set plot background color to black
            paper_bgcolor='rgba(0,0,0,0.7)', # set paper background color to black
            font_color='white' # set font color to white
        )
    ),
      width={"size": 3, "order": "last", "offset": 1},
)
movie_budgets2 = dbc.Col(
                    dcc.Graph(
        figure=dur_type().update_layout(
            geo=dict(
                bgcolor='rgba(0,0,0,0.01)', # set background color to black
                showland=True,
                showocean=True,
                oceancolor='rgba(0,0,0,0.07)'
            ),
            plot_bgcolor='rgba(0,0,0,0.01)', # set plot background color to black
            paper_bgcolor='rgba(0,0,0,0.7)', # set paper background color to black
            font_color='white' # set font color to white
        )
    ),
    width=6)

movie_budgets3 = dbc.Col(
                    dcc.Graph(
        figure=dur_type().update_layout(
            geo=dict(
                bgcolor='rgba(0,0,0,0.01)', # set background color to black
                showland=True,
                showocean=True,
                oceancolor='rgba(0,0,0,0.07)'
            ),
            plot_bgcolor='rgba(0,0,0,0.01)', # set plot background color to black
            paper_bgcolor='rgba(0,0,0,0.7)', # set paper background color to black
            font_color='white' # set font color to white
        )
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
                # "height": "8000px",
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
        "background-repeat": "repeat",
        "backdrop-filter": "blur(1px)",
    }
)



# @app.callback(
#     Output(component_id='d_id',component_property='figure'),
#     Output(component_id='d2_id',component_property='figure'),
#     State(component_id='s_id',component_property='value'),
#     State(component_id='drop_id',component_property='value'),
#     Input(component_id='submit-id',component_property='n_clicks')

# )
# def call (year,cont,inpu):
#   if cont == None or cont==[] :
#     filtered_df = df[(df.year == year)]
#   else:  
#     filtered_df = df[(df.year == year) & (df.continent.isin(cont))]

#   fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
#                      size="pop", color="continent", hover_name="country",
#                      log_x=True, size_max=55)
  
#   fig2 = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
#                      size="pop", color="continent", hover_name="country",
#                      log_x=True, size_max=55)

#   fig.update_layout(transition_duration=500)

#   return fig,fig2


if __name__ == "__main__":
    app.run_server(debug=True)