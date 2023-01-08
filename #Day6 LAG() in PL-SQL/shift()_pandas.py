import pandas as pd

# Create a DataFrame with store_id, sale_date, and total_sales columns
df = pd.DataFrame({'store_id': [1, 1, 1, 2, 2],
                   'sale_date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-01', '2022-01-03'],
                   'total_sales': [100, 120, 130, 90, 110]})

# Shift the values in the total_sales column by one row
df['prev_sales'] = df['total_sales'].shift(periods=1)
print(df)

"""the prev_sales column contains the total_sales value from the preceding row (ordered by index) for each store. If the current row is the first row within its group (defined by the store_id column), the prev_sales column contains NaN values."""


