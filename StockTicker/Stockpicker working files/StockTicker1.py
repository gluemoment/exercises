# perform the basic imports
import dash
import dash_core_components as dcc
import dash_html_components as html
# launch the application
app = dash.Dash()
# Create a Div to contain basic headers, an input box, and our graph
app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.H3('Enter a stock symbol:'),
    dcc.Input(id ='my_ticker_symbol',
        value ='TSLA' # sets a default value 
    ),
    dcc.Graph(id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ]
        }
    )
])
# Add the server clause
if __name__ == '__main__':
    app.run_server()
