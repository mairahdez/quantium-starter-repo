import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px


df = pd.read_csv('data/daily_sales_data_final.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

app = dash.Dash(__name__)


app.layout = html.Div(className='main-container', children=[
    html.H1("Soul Foods: Pink Morsel Sales Analysis"),
    
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'All', 'value': 'all'},
            {'label': 'North', 'value': 'north'},
            {'label': 'South', 'value': 'south'},
            {'label': 'East', 'value': 'east'},
            {'label': 'West', 'value': 'west'}
        ],
        value='all',  
        inline=True
    ),
    
    dcc.Graph(id='sales-line-chart')
])


@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    filtered_df = df
    if selected_region != 'all':
        filtered_df = df[df['region'] == selected_region]
        
    fig = px.line(filtered_df, x='date', y='sales', title=f'Sales in {selected_region.capitalize()} Region')
    return fig

if __name__ == '__main__':
    app.run(debug=True)