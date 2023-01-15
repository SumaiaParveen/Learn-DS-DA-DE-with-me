import pandas as pd

# create a dummy dataset for this problem
data = {
    'Customer': ['John','Mike','Amy','Jessica','David','Julie','Brian','Nancy','Steve','Karen'],
    'Age': [25,31,35,28,22,29,32,40,38,27],
    'Gender':['M','M','F','F','M','F','M','F','M','F'],
    'Product':['Shampoo','Laptop','Smartphone','Shampoo','Smartphone','Shampoo','Smartphone','Laptop','Smartphone','Shampoo'],
    'Order_Date': ['2020-01-01','2020-01-15','2020-02-01','2020-03-01','2020-04-01','2020-05-01','2020-06-01','2020-07-01','2020-08-01','2020-09-01'],
        'Order_Number': [100,101,102,103,104,105,106,107,108,109], 
        'Repeat_Purchase': [1,0,0,1,0,1,0,1,0,1]
}
df = pd.DataFrame(data)

# Convert the 'Order_Date' column to datetime type
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Group the data by customer
grouped = df.groupby(['Customer'])

# Create a list to store the data
data = []

"""is iterating through each group of the dataframe, which is grouped by 'Customer'. For each group, it is counting the number of purchases that are repeat purchases (where the Repeat_Purchase column is equal to 1) and storing this value in the variable repeat_purchases. It is also storing the total number of purchases in the group in the variable total_purchases. Then, it is calculating the repeat purchase rate (RPR) by dividing the number of repeat purchases by the total number of purchases and storing this value in the variable rpr. Finally, it is appending a list containing the product name and the RPR value to the data list. This code is creating a list of the RPR for each product."""
for name, group in grouped:
    repeat_purchases = group[group['Repeat_Purchase'] == 1]['Repeat_Purchase'].count()
    total_purchases = group.shape[0]
    rpr = repeat_purchases/total_purchases
    data.append([name, rpr])

# Create a dataframe from the data
df_rpr = pd.DataFrame(data, columns=['Customer', 'RPR'])


display(df_rpr )
