import dash
import plotly.graph_objects as go
import yfinance as yf
from dash import dcc, html

# Initialize the Dash app
app = dash.Dash(__name__)

# Fetch S&P 500 data from Yahoo Finance
data = yf.download('^GSPC', start="1928-01-01", end="2025-01-01", auto_adjust=True)

# Convert Date and Close to lists
dates = data.index.to_pydatetime().tolist()  # Convert index to a list of datetime objects
sp500_values = data['Close'].values.tolist()  # Convert the 'Close' column to a list

# Create a Plotly line chart
figure = go.Figure()

figure.add_trace(go.Scatter(
    x=dates, 
    y=sp500_values, 
    mode='lines', 
    name='S&P 500 Index'
))

# Update layout for the figure
figure.update_layout(
    title="S&P 500 Index Over Time",
    xaxis_title="Date",
    yaxis_title="S&P 500 Index",
)

# Set the layout using Dash's Graph component
app.layout = html.Div([
    dcc.Graph(
        id='sp500-graph',
        figure=figure
    )
])

# Run the Dash app on the specified port
if __name__ == '__main__':
    app.run_server(debug=True, port=8050, host='0.0.0.0')
