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
rating_genre_var = dbc.Col(
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
groth_var =  dbc.Col(
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
            font_color='white' ,# set font color to white
            
            
        )
    ),
      width={"size": 5, "order": "last","offset": 1 },
      style={"margin-left": "100px"}
      
)
con_type_items = [
    dbc.DropdownMenuItem("Film",id="0"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("TV Films",id="1"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("TV Series",id="2"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Video",id="3"),
]

con_type = dbc.DropdownMenu(
    label="Types",
    size="sm",
    children=con_type_items,
    toggle_style={
        "textTransform": "uppercase",
        "background": "#000000A0",
    },
    toggleClassName="fst-italic border border-dark",
)
top_active_var = dbc.Col(
           [       
              dbc.Row(
            dbc.Col(
                con_type,
                width={"size": 50},
                style={"backgroundColor": "transparent"}
             ),
            justify="start",
            style={"margin-up": "100px"}
        )
            ,dcc.Graph(
         id='top_active-graph',
        figure=top_active().update_layout(
            geo=dict(
                bgcolor='rgba(0,0,0,0.01)', # set background color to black
                showland=True,
                showocean=True,
                oceancolor='rgba(0,0,0,0.07)'
            ),
            plot_bgcolor='rgba(0,0,0,0.01)', # set plot background color to black
            paper_bgcolor='rgba(0,0,0,0.7)', # set paper background color to black
            font_color='white', # set font color to white
        )
    )],
    width=6,
    )

actor_dirctor_items = [
    dbc.DropdownMenuItem("Actors",id="actors"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Directors",id="directors"),
]
actor_dirctor = dbc.DropdownMenu(
    label="Actors / Directors",
    size="sm",
    children=actor_dirctor_items,
    toggle_style={
        "textTransform": "uppercase",
        "background": "#000000A0",
    },
    toggleClassName="fst-italic border border-dark",
)


pop_act_dirct_var = dbc.Col(
    [
        dbc.Row(
            dbc.Col(
                actor_dirctor,
                width={"size": 50},
                style={"backgroundColor": "transparent"}
             ),
            justify="start",
            style={"margin-up": "100px"}
        ),
        dcc.Graph(
            id='pop_act_dirct-graph',
            figure=pop_act_dirct().update_layout(
                geo=dict(
                    bgcolor='rgba(0,0,0,0.01)',
                    showland=True,
                    showocean=True,
                    oceancolor='rgba(0,0,0,0.07)'
                ),
                plot_bgcolor='rgba(0,0,0,0.01)',
                paper_bgcolor='rgba(0,0,0,0.7)',
                font_color='white',
            )
        )
    ],
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
                        rating_genre_var,  
                        groth_var,     
                    ]
                
                ),
                 html.Br(),
                dbc.Row([
                        pop_act_dirct_var,
                        top_active_var
                        ])
            ],
            fluid=True,
            style={
                "padding": '10px 30px',
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



@app.callback(
    Output('pop_act_dirct-graph', 'figure'),
    Output('top_active-graph', 'figure'),
    
    [Input("actors", "n_clicks"),
     Input("directors", "n_clicks"),
     Input("0", "n_clicks"),
     Input("1", "n_clicks"),
     Input("2", "n_clicks"),
     Input("3", "n_clicks"),]
)
def update_act_dect(*args):
    # Define the logic to update the graph based on the selected option
    typ=0
    ctx = dash.callback_context
    if not ctx.triggered:
        f = open("message.txt","w+")
        selected_option = "actors"
        f.write(selected_option)
        f.close()   
    elif ctx.triggered[0]["prop_id"].split(".")[0]=="actors" or ctx.triggered[0]["prop_id"].split(".")[0]=="directors":
        selected_option = ctx.triggered[0]["prop_id"].split(".")[0]
        txt=selected_option
        f = open("message.txt","w+")
        f.write(selected_option)
        f.close()
    else:
        selected_option = ctx.triggered[0]["prop_id"].split(".")[0]
        typ=int(selected_option)
    f = open("message.txt","r")
    txt=f.read()
    f.close()
    

    
    data = pop_act_dirct(txt)
    fig = data.update_layout(
        geo=dict(
            bgcolor='rgba(0,0,0,0.01)',
            showland=True,
            showocean=True,
            oceancolor='rgba(0,0,0,0.07)'
        ),
        plot_bgcolor='rgba(0,0,0,0.01)',
        paper_bgcolor='rgba(0,0,0,0.7)',
        font_color='white'
    
    )
    data2 = top_active(col=txt,chois=typ)
    fig2 = data2.update_layout(
        geo=dict(
            bgcolor='rgba(0,0,0,0.01)',
            showland=True,
            showocean=True,
            oceancolor='rgba(0,0,0,0.07)'
        ),
        plot_bgcolor='rgba(0,0,0,0.01)',
        paper_bgcolor='rgba(0,0,0,0.7)',
        font_color='white'
    
    )
    return fig,fig2
if __name__ == "__main__":
    app.run_server(debug=True)