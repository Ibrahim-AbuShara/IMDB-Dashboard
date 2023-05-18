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
IMDB_LOGO = "https://ia.media-imdb.com/images/M/MV5BMTk3ODA4Mjc0NF5BMl5BcG5nXkFtZTgwNDc1MzQ2OTE@._V1_.png"

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
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
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=IMDB_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("IMDb Dashboard", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="#",
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



map_var = dbc.Col(
    dcc.Graph(
        figure=world_map().update_layout(
            geo=dict(
                bgcolor='rgba(0,0,0,0.01)',  # set background color to black
                showland=True,
                showocean=True,
                oceancolor='rgba(0,0,0,0.07)'
            ),
            plot_bgcolor='rgba(0,0,0,0.01)',  # set plot background color to black
            paper_bgcolor='rgba(0,0,0,0.7)',  # set paper background color to black
            font_color='white'  # set font color to white
        ),
        style={'width': '90%', 'height': '85vh', 'margin': 'auto'}  # center the graph and set width and height
    ),
    width={'size': 10, 'offset': 1, 'order': 'first'}  # adjust width and offset to center the column
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
    width=5
)

# Movie Budgets Graph
comp_var =  dbc.Col(
    dcc.Graph(
        figure=compare_avg_rating().update_layout(
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
      width=6
     
      
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

dur_content_var = dbc.Col(
           [       
            dcc.Graph(
        figure=dur_content().update_layout(
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


dur_type_var = dbc.Col(
           [       
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
            font_color='white', # set font color to white
        )
    )],
    width=6,
    )
type_items = [
    dbc.DropdownMenuItem("Film",id="00"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("TV Films",id="11"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("TV Series",id="22"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Video",id="33"),
]

button = dbc.DropdownMenu(
    label="type",
    size="sm",
    children=type_items,
    toggle_style={
        "textTransform": "uppercase",
        "background": "#000000A0",
        "position": "sticky",
        "bottom": "1000px",
        "right": "5px",
        "z-index": "10000"
    },
    toggleClassName="fst-italic border border-dark",
)

# Update the layout
rating_over_years_var = dbc.Col(
    [
        dcc.Graph(
             id='rating_over_years-graph',
            figure=rating_over_years().update_layout(
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
        ),
        button
    ],
    width=6
)

groth_var = dbc.Col(
    [
        dcc.Graph(
            figure=groth().update_layout(
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

map_header = html.H3(
    "Header 1",
    className="header",
    style={
        "border": "1px solid #000000",
        "padding": "10px",
        "background-color": "#000000A0",
        "font-family": "Arial, sans-serif",
        "color": "white",
        "border-radius": "10px",
        "position": "relative",
       
    }
)

# App layout
app.layout = html.Div(
    [
        navbar,
        dbc.Container(
            [
                html.Br(),
                map_header,

                dbc.Row(
                    [
                        map_var
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        comp_var,     
                        rating_genre_var
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        pop_act_dirct_var,
                        top_active_var
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        dur_content_var,
                        dur_type_var
                    ]
                ),
                html.Br(),
                dbc.Row(
                    [
                        rating_over_years_var,
                        groth_var
                    ]
                )
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
    
@app.callback(
    Output('rating_over_years-graph', 'figure'),
    
    [
     Input("00", "n_clicks"),
     Input("11", "n_clicks"),
     Input("22", "n_clicks"),
     Input("33", "n_clicks"),
     ]
)
def update_roy(*args):
    # Define the logic to update the graph based on the selected option
    ctx = dash.callback_context
    if not ctx.triggered:
        typ=0
    else:
        selected_option = ctx.triggered[0]["prop_id"].split(".")[0][0]
        print(selected_option)
        typ=int(selected_option)
   
    
    data = rating_over_years(typ)
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
    
    return fig                               
if __name__ == "__main__":
    app.run_server(debug=True)