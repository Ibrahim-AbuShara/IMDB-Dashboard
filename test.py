import dash
from dash import  dcc
import plotly.graph_objects as go
from dash import html

# Create the figures for each BAN
counter_var = go.Figure(go.Indicator(
    mode="number",
    value=38338,
    number={'valueformat': ',', 'font': {'size': 60}},
    title={"text": "Total IMDB Content"}
)).update_layout(
            geo=dict(
                bgcolor='rgba(76, 76, 76, 0.3137)', # set background color to black
                showland=True,
                showocean=True,
                oceancolor='rgba(76, 76, 76, 0.3137)'
            ),
            plot_bgcolor='rgba(76, 76, 76, 0.3137)', # set plot background color to black
            paper_bgcolor='rgba(76, 76, 76, 0.3137)', # set paper background color to black
            font_color='white',)

min_var = go.Figure(go.Indicator(
    mode="number",
    value=1.6,
    number={'valueformat': ',.2f', 'font': {'size': 60}},
    title={"text": "Minimum Rate"}
)).update_layout(
            geo=dict(
                bgcolor='rgba(76, 76, 76, 0.3137)', # set background color to black
                showland=True,
                showocean=True,
                oceancolor='rgba(76, 76, 76, 0.3137)'
            ),
            plot_bgcolor='rgba(76, 76, 76, 0.3137)', # set plot background color to black
            paper_bgcolor='rgba(76, 76, 76, 0.3137)', # set paper background color to black
            font_color='white',)

avg_var = go.Figure(go.Indicator(
    mode="number",
    value=6.188351311336717,
    number={'valueformat': ',.2f', 'font': {'size': 60}},
    title={"text": "Average Rate"}
)).update_layout(
            geo=dict(
                bgcolor='rgba(76, 76, 76, 0.3137)', # set background color to black
                showland=True,
                showocean=True,
                oceancolor='rgba(76, 76, 76, 0.3137)'
            ),
            plot_bgcolor='rgba(76, 76, 76, 0.3137)', # set plot background color to black
            paper_bgcolor='rgba(76, 76, 76, 0.3137)', # set paper background color to black
            font_color='white',)
max_var=go.Figure(go.Indicator(
    mode="number",
    value=9.5,
    number={'valueformat': ',.2f', 'font': {'size': 60}},
    title={"text": "Maximum Rate",}
)).update_layout(
            geo=dict(
                bgcolor='rgba(76, 76, 76, 0.3137)', # set background color to black
                showland=True,
                showocean=True,
                oceancolor='rgba(76, 76, 76, 0.3137)'
            ),
            plot_bgcolor='rgba(76, 76, 76, 0.3137)', # set plot background color to black
            paper_bgcolor='rgba(76, 76, 76, 0.3137)', # set paper background color to black
            font_color='white',)
# Define the layout for the dashboard
dashboard = html.Div(
    children=[
        html.H1("BAN Dashboard"),
        html.Div(
            children=[
                dcc.Graph(id='ban1', figure=counter_var, style={'background-color': 'rgba(0,0,0,0.7)', 'width': '30%'}),
                dcc.Graph(id='ban2', figure=min_var, style={'background-color': 'rgba(0,0,0,0.7)', 'width': '30%'}),
                dcc.Graph(id='ban3', figure=avg_var, style={'background-color': 'rgba(0,0,0,0.7)', 'width': '30%'}),
                dcc.Graph(id='ban3', figure=max_var, style={'background-color': 'rgba(0,0,0,0.7)', 'width': '30%'}),
            ],
            className="row",
            style={"display": "flex", "justify-content": "space-between"}
        )
    ],
    style={"background-color": "black", "padding": "20px"}
)

# Create the Dash app
app = dash.Dash(__name__)
app.title = "BANDashboard"

# Define the app layout
app.layout = html.Div(children=[dashboard])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
