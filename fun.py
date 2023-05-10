import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from dash.dependencies import Input,Output,State
import pandas as pd
imdb=pd.read_csv('imdb.csv',index_col=0)
films = imdb[imdb['type'] == "Film"].sort_values('weighted_rating', ascending=False)
TV_Films = imdb[imdb['type'] == "TV Films"].sort_values('weighted_rating', ascending=False)
TV_Series = imdb[imdb['type'] == "TV Series"].sort_values('weighted_rating', ascending=False)
Video= imdb[imdb['type'] == "Video"].sort_values('weighted_rating', ascending=False)


def world_map():
    content_By_country=imdb['country'].value_counts().to_frame().reset_index().rename(columns={"index": "country", "country": "Nof.content"})
    return px.choropleth(
                content_By_country, 
                locations='country',
                locationmode='country names', 
                color='Nof.content', 
                hover_name='country',
                title='Content per Country',
                color_continuous_scale='emrld'
            )
    
def dur_content ():
    return px.scatter(
        imdb,
        x='duration',
        y='weighted_rating',
        hover_data=['title','numVotes','averageRating'],
        color='type',
        color_continuous_scale="Viridis"
        )

def compare_avg_rating ():
        f=imdb.copy()
        f['averageRating']=f['averageRating'].round()
        movies = f.sort_values('averageRating', ascending=False)
        high_votes = movies.groupby('averageRating').max()
        low_votes = movies.groupby('averageRating').min()
        movies['min_numVotes']=movies.groupby('averageRating')['numVotes'].transform('min')
        min_votes = movies[movies['numVotes'] == movies['min_numVotes']]
        low_votes=min_votes.drop_duplicates('averageRating').drop(columns=['min_numVotes'])
        movies['max_numVotes']=movies.groupby('averageRating')['numVotes'].transform('max')
        max_votes = movies[movies['numVotes'] == movies['max_numVotes']]
        high_votes=max_votes.drop_duplicates('averageRating').drop(columns=['max_numVotes'])
        high_votes.reset_index(inplace=True)
        low_votes.reset_index(inplace=True)
        low_high=pd.concat([low_votes,high_votes],ignore_index=True)
        low_high.drop_duplicates('tconst',inplace=True)
        low_high=low_high[low_high['averageRating']!=10.0]
        low_high.sort_values(['averageRating','numVotes'],inplace=True,ascending=True)
        fig2 = px.scatter(
            low_high,
            x='averageRating',
            y='numVotes',
            hover_data=['title', 'numVotes', 'averageRating','type'],
            color='averageRating',
            size='numVotes',
            size_max=60,
            color_continuous_scale="ylorrd"
            
        )

        fig2.update_traces(textposition='top center', textfont=dict(size=9), marker=dict(sizemin=7))
        fig2.update_layout(
            xaxis_title='Average Rating',
            annotations=[
                dict(
                    x=row['averageRating'],
                    y=row['numVotes'],
                    text=row['title'],
                    textangle=20,
                    font=dict(size=8),
                    showarrow=False
                ) for index, row in low_high.iterrows()
            ]
        )
        return fig2

def dur_type():
    # Create a hierarchical index of movies by genre and MPAA rating
    movies_by_genre_rating = imdb.groupby(['type', 'duration'])['tconst'].count().reset_index()

    # Create a sunburst chart of movies by genre and MPAA rating
    fig = px.sunburst(movies_by_genre_rating, path=['type', 'duration'], values='tconst',
                    title='Distribution of Content Durations by Type')

    hovertemplate = 'Duration: %{label} min<br>Nof.%{parent}: %{value}<br>'

    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(margin=dict(l=50, r=50, b=100, t=100),
                  showlegend=False, annotations=[dict(text='', x=0.5, y=0.5, font_size=20, showarrow=False)])

# Set domain of pie chart
    fig.update_layout(
        annotations=[dict(text='', x=0.5, y=0.5, font_size=20, showarrow=False)],
       
        showlegend=False,
        margin=dict(l=40, r=10, t=40, b=40),
        template="plotly_white",

)
    return fig

def rating_genre():
    genre_highest_ratings = imdb.groupby('genre')['weighted_rating'].mean().reset_index().sort_values("weighted_rating",ascending=False)

    fig = px.bar(genre_highest_ratings, x='weighted_rating',
                 y='genre',
                 orientation='h',
                 color="weighted_rating",
                title='Highest Rating by Genre',
                color_continuous_scale='orrd'
                )

    fig.update_layout(
        xaxis_title='Weighted Rating',
        yaxis_title='Genre',
        yaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=1,
            categoryorder='max ascending',
        ),
        width=850, 
        height=625,
        plot_bgcolor='#f8f8f8',
        font_family='Arial',
        font_size=16,
        title_font_size=18,
        legend_title='Weighted Rating',
        legend_font_size=14,
        margin=dict(l=80, r=20, t=80, b=20)
    )

    
    return fig


def groth():
    moves_per_year = imdb.groupby('year')['title'].count().reset_index()
    group_labels = ['Year']
    fig = ff.create_distplot([imdb["year"].values.tolist()], group_labels,
                            colors =  ['#FFCC33'], bin_size=1)

    # update the layout and axis labels
    fig.update_layout(title='Trend of IMDb Data Growth',
                    xaxis_title='Year',
                    yaxis_title='Density',
                    title_font_size=20,
                    font_family='Arial',
                    font_size=14,
                    plot_bgcolor='#f8f8f8',
                    margin=dict(l=80, r=20, t=80, b=20),
                    width=640,
                    height=500,
                    ),
                    

    fig.update_xaxes(tickmode='linear', tick0=1900, dtick=10)
    fig.update_yaxes(title_text='Density of Titles', tickformat=',.2%', exponentformat='none', showexponent='none')
    return fig

