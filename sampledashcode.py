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

# Create a line chart using plotly
figure = go.Figure()

figure.add_trace(go.Scatter(
    x=dates, 
    y=sp500_values, 
    mode='lines', 
    name='S&P 500 Index'
))

# Add title and labels
figure.update_layout(
    title="S&P 500 Index Over Time",
    xaxis_title="Date",
    yaxis_title="S&P 500 Index",
)

# Define the layout of the app
app.layout = html.Div([
    html.H1("S&P 500 Index Over Time"),
    dcc.Graph(figure=figure)
])

# Run the app on a specified port (render will handle port binding)
if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
