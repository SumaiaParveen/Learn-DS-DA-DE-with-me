import pandas as pd
from textblob import TextBlob

# Create a dummy dataset
data = {'Customer': ['Alice','Bob','Charlie','David','Eve'],
        'Age': [25,31,35,28,22],
        'Gender':['F','M','M','M','F'],
        'Product':['Apple Watch Series 6','Macbook Pro','AirPods Pro','Apple Watch Series 6','iPad'],
        'Product_Category':['Electronics','Electronics','Electronics','Electronics','Electronics'],
        'Comment':['Great product','Good performance','Not satisfied','Not satisfied','Could be better']
        }
df = pd.DataFrame(data)

# Use TextBlob to extract the sentiment of the comment
df['CSAT_Score'] = df['Comment'].apply(lambda x: TextBlob(x).sentiment.polarity)

# Assign a score based on the sentiment
df['CSAT_Score'] = df['CSAT_Score'].apply(lambda x: 4 if x > 0 else (2 if x < 0 else 3))

# group the dataset by product
grouped = df.groupby(['Product'])

# Create a list to store the data
data = []

# Iterate through each group
for name, group in grouped:
    csat_score = group['CSAT_Score'].mean()
    csat_percentage = (group['CSAT_Score'] == 4).sum() / group.shape[0] * 100
    data.append([name, csat_score,csat_percentage])

# Create a dataframe from the data
df_results = pd.DataFrame(data, columns=['Product', 'CSAT_Score','CSAT_Percentage'])
