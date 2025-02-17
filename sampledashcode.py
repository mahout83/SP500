import plotly.graph_objects as go
import yfinance as yf
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Fetch S&P 500 data from Yahoo Finance
data = yf.download('^GSPC', start="1928-01-01", end="2025-01-01", auto_adjust=True)

# Convert Date and Close to lists
dates = data.index.to_pydatetime().tolist()  # Convert index to a list of datetime objects
sp500_values = data['Close'].values.tolist()  # Convert the 'Close' column to a list

# Initialize Dash app
app = dash.Dash(__name__)

# Create layout
app.layout = html.Div([
    dcc.Graph(
        id='line-chart',
        figure={
            'data': [
                go.Scatter(
                    x=dates,
                    y=sp500_values,
                    mode='lines',
                    name='S&P 500 Index'
                )
            ],
            'layout': go.Layout(
                title='S&P 500 Index Over Time',
                xaxis={'title': 'Date'},
                yaxis={'title': 'S&P 500 Index'}
            )
        }
    )
])

# Run the app on port 8050
if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host='0.0.0.0')
