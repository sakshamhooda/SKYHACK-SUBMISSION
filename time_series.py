import matplotlib.pyplot as plt

# Step 1: Data Preparation
# Convert the dates to a datetime format and sort the data by date
final_merged_data['scheduled_departure_dtl'] = pd.to_datetime(final_merged_data['scheduled_departure_dtl'])
time_series_data = final_merged_data[['scheduled_departure_dtl', 'score']].dropna()
time_series_data = time_series_data.sort_values('scheduled_departure_dtl')

# Step 2: Trend Analysis
# Plot the F&B satisfaction scores over time to identify any trends
plt.figure(figsize=(15, 6))
plt.plot(time_series_data['scheduled_departure_dtl'], time_series_data['score'], marker='o', linestyle='')
plt.xlabel('Scheduled Departure Date')
plt.ylabel('F&B Satisfaction Score')
plt.title('Time-Series Analysis of F&B Satisfaction Scores')
plt.show()

import statsmodels.api as sm

# Resample the data by month to get the mean F&B satisfaction score for each month
time_series_data['scheduled_departure_dtl'] = pd.to_datetime(time_series_data['scheduled_departure_dtl'])
time_series_data.set_index('scheduled_departure_dtl', inplace=True)
resampled_data = time_series_data.resample('M').mean()

# Decompose the time-series data to identify trends and seasonality
decomposition = sm.tsa.seasonal_decompose(resampled_data.dropna(), model='additive')

# Extract the trend, seasonal, and residual components
trend = decomposition.trend.dropna()
seasonal = decomposition.seasonal.dropna()
residual = decomposition.resid.dropna()

# Show the first few values of each component to understand their behavior
trend.head(), seasonal.head(), residual.head()

# Recreate the 'time_series_data' variable
time_series_data = final_merged_data[['scheduled_departure_dtl', 'score']].dropna()
time_series_data = time_series_data.sort_values('scheduled_departure_dtl')

# Convert the dates to a datetime format and set it as index for time-series analysis
time_series_data['scheduled_departure_dtl'] = pd.to_datetime(time_series_data['scheduled_departure_dtl'])
time_series_data.set_index('scheduled_departure_dtl', inplace=True)

# Resample the data by month to get the mean F&B satisfaction score for each month
resampled_data = time_series_data.resample('M').mean()

# Decompose the time-series data to identify trends and seasonality
decomposition = sm.tsa.seasonal_decompose(resampled_data.dropna(), model='additive')

# Extract the trend, seasonal, and residual components
trend = decomposition.trend.dropna()
seasonal = decomposition.seasonal.dropna()
residual = decomposition.resid.dropna()

# Show the first few values of each component to understand their behavior
trend.head(), seasonal.head(), residual.head()

# Specify the period for seasonal decomposition (12 for monthly data representing a full yearly cycle)
period = 12

# Attempt seasonal decomposition again
try:
    decomposition = sm.tsa.seasonal_decompose(resampled_data.dropna(), model='additive', period=period)
    
    # Extract the trend, seasonal, and residual components
    trend = decomposition.trend.dropna()
    seasonal = decomposition.seasonal.dropna()
    residual = decomposition.resid.dropna()
    
    # Show the first few values of each component to understand their behavior
    trend.head(), seasonal.head(), residual.head()
except ValueError as e:
    str(e)
