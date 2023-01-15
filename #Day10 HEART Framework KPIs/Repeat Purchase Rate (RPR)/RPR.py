import pandas as pd

data = {
    'Customer': ['John','Mike','Amy','Jessica','David','Julie','Brian','Nancy','Steve','Karen','John','Mike','Amy','Jessica','David','Julie','Brian','Nancy','Steve','Karen'],
    'Age': [25,31,35,28,22,29,32,40,38,27,25,31,35,28,22,29,32,40,38,27],
    'Gender':['M','M','F','F','M','F','M','F','M','F','M','M','F','F','M','F','M','F','M','F'],
    'Product':['Shampoo','Laptop','Smartphone','Shampoo','Smartphone','Shampoo','Smartphone','Laptop','Smartphone','Shampoo','Shampoo','Laptop','Notebook','Shampoo','Smartphone','Shampoo','Smartphone','Laptop','Smartphone','Pen'],
    'Order_Date': ['2020-01-01','2020-01-15','2020-02-01','2020-03-01','2020-04-01','2020-05-01','2020-06-01','2020-07-01','2020-08-01','2020-09-01','2020-10-01','2020-11-01','2020-12-01','2021-01-01','2021-02-01','2021-03-01','2021-04-01','2021-05-01','2021-06-01','2021-07-01'],
        'Order_Number': [100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119]
}
df = pd.DataFrame(data)

"""creates a new column in the dataframe called 'Repeat_Purchase' and assigns a boolean value to each row indicating whether the combination of 'Customer' and 'Product' values in that row is duplicated in the dataframe (i.e. whether the customer has made a repeat purchase of that product)."""
df['Repeat_Purchase'] = df.duplicated(subset=['Customer','Product'], keep=False)

"""converts the boolean values in the 'Repeat_Purchase' column to 1s and 0s, with 1 indicating a repeat purchase and 0 indicating a new purchase."""
df['Repeat_Purchase'] = df['Repeat_Purchase'].apply(lambda x: 1 if x else 0)

# Group the data by customer
grouped = df.groupby(['Product'])

# Create a list to store the data
data = []

"""is iterating through each group of the dataframe, which is grouped by 'Product'. For each group, it is counting the number of purchases that are repeat purchases (where the Repeat_Purchase column is equal to 1) and storing this value in the variable repeat_purchases. It is also storing the total number of purchases in the group in the variable total_purchases. Then, it is calculating the repeat purchase rate (RPR) by dividing the number of repeat purchases by the total number of purchases and storing this value in the variable rpr. Finally, it is appending a list containing the product name and the RPR value to the data list. This code is creating a list of the RPR for each product."""
for name, group in grouped:
    repeat_purchases = group[group['Repeat_Purchase'] == 1]['Repeat_Purchase'].count()
    total_purchases = group.shape[0]
    rpr = repeat_purchases/total_purchases
    data.append([name, rpr])

# Create a dataframe from the data
df_rpr = pd.DataFrame(data, columns=['Product', 'RPR'])

display(df_rpr)
