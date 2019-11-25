import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df1 = pd.read_csv('IMDB/clean_data.csv')
df1 = df1[['Movie_Name','Year','Votes','Genre','Runtime','Synopsis','Gross Amount','Rating','Metascore']]
asd = df1.groupby('Year',as_index=False)
qaz = asd['Gross Amount'].sum()*1000000
s2 = qaz.astype('int64')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div([
    html.H1(children='IMDb Romance Movies', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Graph(
        id='Metascore_and_Rating_Graph',
        figure={
            'data': [
                go.Scatter(
                    x=df1['Metascore'],
                    y=df1['Rating'],
                    hovertext=df1['Movie_Name'],
                    hoverinfo="text",
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    }
                )
            ],
            'layout': go.Layout(
                title='Metascore and Rating',
                xaxis={'title': 'Metascore'},
                yaxis={'title': 'Rating'},
                hovermode='closest'
            )
        }
    ),
    dcc.Markdown(children='This is where i would write about the previous graph'),
    
    dcc.Graph(
        id='Line_Graph_date_and_gross_amount',
        figure={
            'data': [
               go.Scatter(

                    x=s2['Year'],
                    y=s2['Rating'],
                    hovertext=df1['Movie_Name'],
                    hoverinfo="text",
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    }
                )
            ],
            'layout': go.Layout(
                    
    )
        }
)
]
)

if __name__ == '__main__':
    app.run_server(debug=True)