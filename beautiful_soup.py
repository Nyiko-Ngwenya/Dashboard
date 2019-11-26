import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df1 = pd.read_csv('IMDB/clean_data.csv')
df1 = df1[['Movie_Name','Year','Votes','Genre','Runtime','Synopsis','Gross Amount','Rating','Metascore']]
#this is for rounding up my ratings
new_list_rating = df1['Rating'].round()
#this is will groupby the information by year
asd = df1.groupby('Year',as_index=False)
#this will sum the gross amount
qaz = asd['Gross Amount'].sum()
qaz['Gross Amount'] = qaz['Gross Amount']*1000000
s2 = qaz.astype('int64')

qaz2 = asd['Runtime'].mean()
qaz2['Runtime'] = qaz2['Runtime']
s22 = qaz2.astype('int64')

qaz23 = asd['Rating'].mean()
qaz23['Rating'] = qaz23['Rating']
s223 = qaz23.astype('int64')

zxc = new_list_rating.value_counts()
zxc = pd.DataFrame(zxc)



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
        id='Metascore_and_Rating_Graph1',
        figure={
            'data': [
                go.Scatter(
                    x=df1['Rating'],
                    y=df1['Gross Amount'],
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
                yaxis={'title': 'Gross Amount'},
                hovermode='closest'
            )
        }
    ),
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
                    y=s2['Gross Amount'],
                    mode='lines',
                    opacity=0.7,
                )
            ],
            'layout': go.Layout(
                 title='Gross amount over the years',
                xaxis={'title': 'Years'},
                yaxis={'title': 'Gross Amount'},
                hovermode='closest'   
    )
        }
),
    dcc.Markdown(children='This is where i would write about the previous graph'),

    dcc.Graph(
        id='Line_Graph_date_and_gross_amount2',
        figure={
            'data': [
               go.Pie(
                   values=zxc['Rating'],
                   labels = [str(i)+'/10 Rating' for i in zxc.index]
                )
            ],
            'layout': go.Layout(
                 title='Pie chart showing the spread of ratings',
                hovermode='closest'   
    )
        }
),
    dcc.Markdown(children='This is where i would write about the previous graph'),
    dcc.Graph(
        id='Line_Graph_date_and_gross_amount3',
        figure={
            'data': [
               go.Scatter(
                    x=s22['Year'],
                    y=s22['Runtime'],
                    mode='lines',
                    opacity=0.7,
                )
            ],
            'layout': go.Layout(
                 title='Gross amount over the years',
                xaxis={'title': 'Years'},
                yaxis={'title': 'Runtime'},
                hovermode='closest'   
    )
        }
), dcc.Markdown(children='This is where i would write about the previous graph'),
dcc.Graph(
        id='Line_Graph_date_and_gross_amount4',
        figure={
            'data': [
               go.Scatter(

                    x=s223['Year'],
                    y=s223['Rating'],
                    mode='lines',
                    opacity=0.7,
                )
            ],
            'layout': go.Layout(
                 title='Gross amount over the years',
                xaxis={'title': 'Years'},
                yaxis={'title': 'Rating'},
                hovermode='closest'   
    )
        }
)

]
)

if __name__ == '__main__':
    app.run_server(debug=True)