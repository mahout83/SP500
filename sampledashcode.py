import yfinance as yf
import plotly.express as px

# Fetching data for S&P 500
data = yf.download("^GSPC", start="2000-01-01", end="2025-01-01")

# Resetting the multi-index to a single index for easier plotting
data.reset_index(inplace=True)

# Display the data structure to understand column names
print(data.columns)

# Plotting
figure = px.line(data, x='Date', y='Close', title='S&P 500 Index Over Time')

# Show the figure
figure.show()
