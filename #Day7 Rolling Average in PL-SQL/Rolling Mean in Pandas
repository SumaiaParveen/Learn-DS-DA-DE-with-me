import pandas as pd

# Create the table
df = pd.DataFrame({'order_date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08', '2022-01-09', '2022-01-10'],
                   'order_quantity': [10, 20, 15, 25, 30, 35, 40, 45, 50, 55]})

# Convert the order_date column to a datetime data type
df['order_date'] = pd.to_datetime(df['order_date'])

# Set the order_date column as the index
df.set_index('order_date', inplace=True)

# Calculate the 2-day and 7-day rolling averages and display the results
df['two_day_rolling_average'] = df['order_quantity'].rolling(2).mean()
df['seven_day_rolling_average'] = df['order_quantity'].rolling(7).mean()
