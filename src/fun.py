from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff
from dash.dependencies import Input,Output,State
import pandas as pd
import ast


imdb=pd.read_csv('imdb1.csv',index_col=0)
imdb['actors'] = imdb['actors'].fillna('[]')
imdb['directors'] = imdb['directors'].fillna('[]')
convert_to_list = lambda x: ast.literal_eval(x)
converted = lambda x: x[0].split(',') if len(x)!=0 else ['Unknown']
imdb['actors'] = imdb['actors'].apply(convert_to_list)
imdb['actors'] = imdb['actors'].apply(converted)
imdb['directors'] = imdb['directors'].apply(convert_to_list)
imdb['directors'] = imdb['directors'].apply(converted)
films = imdb[imdb['type'] == "Film"].sort_values('weighted_rating', ascending=False)
# TV_Films = imdb[imdb['type'] == "TV Films"].sort_values('weighted_rating', ascending=False)
# TV_Series = imdb[imdb['type'] == "TV Series"].sort_values('weighted_rating', ascending=False)
# Video= imdb[imdb['type'] == "Video"].sort_values('weighted_rating', ascending=False)



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
            ).update_layout(title_font_size=24,)
def compare_avg_rating (col="averageRating"):
        f=imdb.copy()
        f[col]=f[col].round()
        movies = f.sort_values(col, ascending=False)
        high_votes = movies.groupby(col).max(numeric_only=True)
        low_votes = movies.groupby(col).min(numeric_only=True)
        movies['min_numVotes']=movies.groupby(col)['numVotes'].transform('min')
        min_votes = movies[movies['numVotes'] == movies['min_numVotes']]
        low_votes=min_votes.drop_duplicates(col).drop(columns=['min_numVotes'])
        movies['max_numVotes']=movies.groupby(col)['numVotes'].transform('max')
        max_votes = movies[movies['numVotes'] == movies['max_numVotes']]
        high_votes=max_votes.drop_duplicates(col).drop(columns=['max_numVotes'])
        high_votes.reset_index(inplace=True)
        low_votes.reset_index(inplace=True)
        low_high=pd.concat([low_votes,high_votes],ignore_index=True)
        low_high.drop_duplicates('tconst',inplace=True)
        low_high=low_high[low_high[col]!=10.0]
        low_high.sort_values([col,'numVotes'],inplace=True,ascending=True)
        fig2 = px.scatter(
            low_high,
            x=col,
            y='numVotes',
            hover_data=['title', 'numVotes', col,'type'],
            color=col,
            size='numVotes',
            size_max=60,
            color_continuous_scale="ylorrd",
            title=f'{col} vs Number of Votes'
            
            
        )

        fig2.update_traces(textposition='top center', textfont=dict(size=14), marker=dict(sizemin=7))
        fig2.update_layout(
            xaxis_title='Average Rating',
            font_size=14,
            font_family='Arial',
            title_font_size=18,
            annotations=[
                dict(
                    x=row[col],
                    y=row['numVotes'],
                    text=row['title'],
                    textangle=20,
                    font=dict(size=8),
                    showarrow=False
                ) for index, row in low_high.iterrows()
            ],
            height=600
        )
        return fig2

def rating_genre(col="Rating per Genre"):
    top=films.sort_values("weighted_rating",ascending =False).head(10)
    if col !="top":
        genre_highest_ratings = imdb.groupby('genre')['weighted_rating'].mean().reset_index().sort_values("weighted_rating",ascending=False)

        fig = px.bar(genre_highest_ratings, x='weighted_rating',
                    y='genre',
                    orientation='h',
                    color="weighted_rating",
                    title='Highest Rating by Genre',
                    color_continuous_scale='orrd'
                    )
    else:
        fig = px.bar(top, x='title',
                    y='weighted_rating',
                    color="weighted_rating",
                    title='Top 10 Movies',
                    color_continuous_scale='orrd',
                    hover_data=["title","averageRating","weighted_rating"]
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
        width=750, 
        height=600,
        plot_bgcolor='#f8f8f8',
        font_family='Arial',
        font_size=14,
        title_font_size=18,
        legend_title='Rating',
        legend_font_size=14,
        margin=dict(l=80, r=20, t=80, b=20)
    )

    
    return fig

def pop_act_dirct(col="actors"):
    if col == "directors":
        Yt='Director'
        slicer=0
    else:
        Yt="Actor"
        slicer=1
        
    imdb_actors = imdb.explode(col)

    # count the number of movies for each actor
    actor_counts = imdb_actors[col].value_counts().reset_index()
   

    # rename the columns
    actor_counts.columns = [Yt, 'Movie Count']

    # filter the top 15 actors by movie count
    top_15_actors = actor_counts[slicer:].head(15)

    # create a horizontal bar chart using Plotly Express
    fig = px.bar(top_15_actors.sort_values('Movie Count', ascending=False), x='Movie Count', y=Yt,
                orientation='h', color=Yt, text='Movie Count',title=f"{Yt}s' Content Count")

    # update the layout
    fig.update_layout(
        xaxis_title=f"Count of {Yt}'s Content",
        yaxis_title=Yt,
        yaxis=dict(
            tickmode='linear',
            tick0=0,
            dtick=1,
            categoryorder='max ascending'
            
        ),
        plot_bgcolor='#f8f8f8',
        font_family='Arial',
        font_size=12,
        title_font_size=18,
        legend_font_size=14,
        margin=dict(l=80, r=20, t=80, b=20)
    )

    return fig

def top_active(col="actors",chois=0):
    # calculate the average rating for each actor and genre
    imdb_actors = imdb.explode(col)
    imdb_actors= imdb_actors[imdb_actors[col]!='Unknown']
    actor_ratings = imdb_actors.groupby([col, 'type']).agg({'weighted_rating': 'mean'}).reset_index()

    # get the top 10 actors in each genre
    top_actors = {}
    for content_type in imdb['type'].unique():
        imdb_content = imdb[imdb['type'] == content_type]
        actor_counts = imdb_content.explode(col)[col].value_counts().reset_index().rename(columns={'index': col, col: 'count'})
        actor_counts=actor_counts[actor_counts[col]!='Unknown']
        top_actors_list = actor_counts.head(10)[col].tolist()
        top_actors[content_type] = top_actors_list

    # create a grouped bar chart
    lst=[]

    # add a trace for each content type and actor
    for content_type in imdb['type'].unique():
        actors = top_actors[content_type]
        actor_ratings_content = actor_ratings[(actor_ratings['type'] == content_type) & (actor_ratings[col].isin(actors))]
        actor_ratings_content = actor_ratings_content.sort_values(by='weighted_rating', ascending=False)

        x = actor_ratings_content[col].tolist()
        y = actor_ratings_content['weighted_rating'].tolist()
        
        lst.append((x,y,content_type))

    fig = go.Figure(
        go.Bar(
        x=lst[chois][0],
        y=lst[chois][1],
        name=lst[chois][2],
    ))

    

    # update the layout
    fig.update_layout(
        title=f'Top 10 {col} by {lst[chois][2]} on  Rating',
        font_family='Arial',
        font_size=12,
        title_font_size=18,
        xaxis_title=col,
        yaxis_title='Rating',
        barmode='group',
        margin=dict(l=100, r=20, t=80, b=20)
    )
    return fig
    
def dur_content ():
    return px.scatter(
        imdb,
        x='duration',
        y='weighted_rating',
        hover_data=['title','numVotes','averageRating'],
        color='type',
        color_continuous_scale="Viridis",
        title="Correlation between the duration of a Content and its rating"
        ).update_layout(
        xaxis_title='Duration in minutes',
        margin=dict(l=40, r=10, t=40, b=40),
        
            
        )



def dur_type():
    # Create a hierarchical index of movies by genre and MPAA rating
    movies_by_genre_rating = imdb.groupby(['type', 'duration'])['tconst'].count().reset_index()

    # Create a sunburst chart of movies by genre and MPAA rating
    fig = px.sunburst(movies_by_genre_rating, path=['type', 'duration'], values='tconst',
                    title='\nDistribution of Content Durations by Type')

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


def rating_over_years(typ=0):
  # Group the data by year and calculate the average weighted rating for each year
    average_rating = imdb.groupby(['year', 'type'])['weighted_rating'].mean().reset_index()

    # Create separate lines for each type of movie with non-empty data
    lines = []
    colors = ['#FFCC33',"#ff704d",'#ff8533','#66d9ff',]  # Custom colors for each line
    for movie_type in imdb['type'].unique():
        data = average_rating[average_rating['type'] == movie_type]
        
        if not data.empty:
            line = go.Scatter(x=data['year'], y=data['weighted_rating'], mode='lines', name=movie_type,
                               line=dict(color=colors[typ])) 
            lines.append(line)

    # Create the layout for the line chart
    name=imdb['type'].unique()[typ]
    layout = go.Layout(
        title=f'Average Rating of {name} Over the Years',
        xaxis=dict(title='Year'),
        yaxis=dict(title='Average Rating'),
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        title_font_size=20,
        font_family='Arial',
        
    )

    # Create the figure with the lines and layout
    figure = go.Figure(data=lines[typ], layout=layout)

    # Show the line chart
    return figure


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
                    
                    # width=640,
                    # height=500,
                    ),
                    

    fig.update_xaxes(tickmode='linear', tick0=1900, dtick=10)
    fig.update_yaxes(title_text='Density of Titles', tickformat=',.2%', exponentformat='none', showexponent='none')
    return fig




