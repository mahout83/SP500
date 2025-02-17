import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import yfinance as yf

# Fetch S&P 500 data from Yahoo Finance
sp500 = yf.download("^GSPC", start="1928-01-01")

# Reset index to make 'Date' a column
sp500.reset_index(inplace=True)

# Check column names (debugging step)
print(sp500.columns)

# Create a Dash app
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children="S&P 500 Index Over Time"),

    dcc.Graph(
        id="sp500-graph",
        figure=px.line(
            sp500,
            x="Date",  # Ensure 'Date' is in the columns of the DataFrame
            y="Close",  # Ensure 'Close' is in the columns of the DataFrame
            title="S&P 500 Closing Price Over Time",
            labels={"Date": "Year", "Close": "Closing Price (USD)"},
            markers=True
        ).update_traces(line=dict(width=1))  # Set thinner line thickness
    )
])

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
