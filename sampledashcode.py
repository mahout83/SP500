import yfinance as yf
import plotly.express as px

# Download data
data = yf.download('^GSPC', start='2020-01-01', end='2023-01-01')

# Reset the index to make 'Date' a column
data = data.reset_index()

# Create the plot
figure = px.line(data, x='Date', y='Close', title='S&P 500 Index Over Time')

# Show the figure
figure.show()
