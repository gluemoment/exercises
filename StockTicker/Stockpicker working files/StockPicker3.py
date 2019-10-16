import dash
import dash_core_components as dcc
import dash_html_components as html
# Add an import for Input/Output
from dash.dependencies import Input, Output
# Add an import for pandas_datareader and datetime
import pandas_datareader.data as web
from datetime import datetime


app = dash.Dash()

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol:'),
    dcc.Input(id ='my_ticker_symbol',
        value ='TSLA' # sets a default value
    ),
    dcc.Graph(
# Add an ID to the graph
        id='my_graph',
figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ],
        }
    )
])
# Add a callback function
@app.callback(
    Output('my_graph', 'figure'),
    [Input('my_ticker_symbol', 'value')])
def update_graph(stock_ticker):
    # Use datareader and datetime to define a DataFrame
    start = datetime(2017, 1, 1)
    end = datetime(2017, 12, 31)
    df = web.DataReader(stock_ticker,'iex',start,end)
    # Change the output data
    fig = {
        'data': [
            {'x': df.index, 'y': df.close}
        ],
        'layout': {'title':stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()
