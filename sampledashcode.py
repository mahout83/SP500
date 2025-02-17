import os
import dash
import plotly.graph_objects as go
import yfinance as yf

# Fetch S&P 500 data from Yahoo Finance
data = yf.download('^GSPC', start="1928-01-01", end="2025-01-01", auto_adjust=True)

# Convert Date and Close to lists
dates = data.index.to_pydatetime().tolist()
sp500_values = data['Close'].values.tolist()

# Create a line chart using plotly
figure = go.Figure()
figure.add_trace(go.Scatter(
    x=dates, 
    y=sp500_values, 
    mode='lines', 
    name='S&P 500 Index'
))

# Create Dash app
app = dash.Dash(__name__)

app.layout = go.Figure(figure)

# Get the port from the environment variable
port = int(os.environ.get('PORT', 8050))

# Run the app on the specified port
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=port)
