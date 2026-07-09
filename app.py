import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv('data/daily_sales_data_final.csv')

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values(by='date')

fig = px.line(df, x='date', y='sales', 
              title='Pink Morsel Sales Over Time',
              labels={'date': 'Date', 'sales': 'Sales ($)'})

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods: Pink Morsel Sales Analysis"),
    html.P("Visualizing sales trends before and after the price increase on Jan 15, 2021."),
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])


if __name__ == '__main__':
    app.run(debug=True)