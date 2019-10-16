import dash
import dash_core_components as dcc
import dash_html_components as html
# Add an import for Input/Output
from dash.dependencies import Input, Output, State
# Add an import for pandas_datareader and datetime
import pandas_datareader.data as web
from datetime import datetime
#import pandas
import pandas as pd

app = dash.Dash()

# read a .csv file, make a dataframe, and build a list of Dropdown options
#Data source: http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange=NYSE&render=download
nsdq = pd.read_csv('/Users/RussellJones1/Desktop/Python/StockTicker/companylist.csv')

nsdq.set_index('Symbol', inplace=True)
options = []
for tic in nsdq.index:
    options.append({'label':'{} {}'.format(tic,nsdq.loc[tic]['Name']), 'value':tic})

app.layout = html.Div([
    html.H1('Stock Ticker Dashboard'),
    html.Div([
        # add styles to enlarge the input box and make room for DatePickerRange
        html.H3('Select stock symbols:',style={'paddingRight':'30px'}),

        # replace dcc.Input with dcc.Options, set options=options
        dcc.Dropdown(
            id='my_ticker_symbol',
            options=options,
            value=['TSLA'],
            multi=True
        )
    # widen the Div to fit multiple inputs
    ], style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
    # add a Div to contain the DatePickerRange
    html.Div([
        html.H3('Select start and end dates:'),
        dcc.DatePickerRange(
            id='my_date_picker',
            min_date_allowed = datetime(2015, 1, 1),
            max_date_allowed = datetime.today(),
            start_date = datetime(2018, 1, 1),
            end_date = datetime.today()
        )
    ], style={'display':'inline-block'}),
    # add a Button element
    html.Div([
            html.Button(
                id='submit-button',
                n_clicks=0,
                children='Submit',
                style={'fontSize':24,'marfinLeft':'30px'}
            ),

    ], style={'display':'inline-block'}),

    dcc.Graph(
        # Add an ID to the graph
        id='my_graph',
        figure={
            'data': [
                {'x': [1,2], 'y': [3,1]}
            ]
        }
    )
])
# Add a callback function
@app.callback(
    # add inputs from the DatePickerRange component
    Output('my_graph', 'figure'),
    # add a button input, and move previous inputs to State
    [Input('submit-button','n_clicks')],
    [State('my_ticker_symbol', 'value'),
            State('my_date_picker', 'start_date'),
            State('my_date_picker', 'end_date')
    ])
# pass n_clicks inot the output function
def update_graph(n_clicks,stock_ticker,start_date, end_date):
    # Use datareader and datetime to define a DataFrame
    start = datetime.strptime(start_date[:10], '%Y-%m-%d')
    end = datetime.strptime(end_date[:10], '%Y-%m-%d')
    # since stock_ticker is now a list of symbols, create a list of traces
    traces = []
    for tic in stock_ticker:
        df = web.DataReader(tic,'iex',start,end)
        traces.append({'x':df.index, 'y': df.close, 'name':tic})

    fig = {
        'data': traces,
        #[{'x': df.index, 'y': df['close']}],
        'layout': {'title':', '.join(stock_ticker)+' Closing Prices'}
        #stock_ticker}
    }
    return fig

if __name__ == '__main__':
    app.run_server()
