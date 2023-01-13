"""This script allows you to see the NPS, Promoters Percentage, Passives Percentage, and Detractors Percentage for each product. It's a way to see which product is performing well and which one requires improvement."""

import pandas as pd

# Create a dummy dataset
data = {'Customer': ['John','Mike','Amy','Jessica','David','Julie','Brian','Nancy','Steve','Karen'],
        'Age': [25,31,35,28,22,29,32,40,38,27],
        'Gender':['M','M','F','F','M','F','M','F','M','F'],
        'Product':['Shampoo','Laptop','Smartphone','Shampoo','Smartphone','Shampoo','Smartphone','Laptop','Smartphone','Shampoo'],
        'Score': [8, 9, 6, 7, 8, 9, 5, 8, 9, 7],
        'Comment':['Great product','Good performance','Not satisfied','Nice fragrance','Could be better','Loved it','Too expensive','Good value for money','Good battery life','Not as expected']
        }
df = pd.DataFrame(data)

# group the dataset by product
grouped = df.groupby(['Product'])

# Create a list to store the data
data = []

# Iterate through each group
for name, group in grouped:
    promoters = group[group['Score'] >= 9].count()[0]
    passives = group[(group['Score'] < 9) & (group['Score'] > 6)].count()[0]
    detractors = group[group['Score'] <= 6].count()[0]
    nps = (promoters - detractors) / (promoters + passives + detractors) * 100
    data.append([name, nps, (promoters / (promoters + passives + detractors))*100, (passives / (promoters + passives + detractors))*100, (detractors / (promoters + passives + detractors))*100])

# Create a dataframe from the data
df_results = pd.DataFrame(data, columns=['Product', 'NPS', 'Promoters Percentage', 'Passives Percentage', 'Detractors Percentage'])
