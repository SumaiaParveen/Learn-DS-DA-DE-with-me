import pandas as pd
from textblob import TextBlob

# Create a dataset with customer, age, gender, product, product category, and comment
data = {'Customer': ['Alice','Bob','Charlie','David','Eve'],
        'Age': [25,31,35,28,22],
        'Gender':['F','M','M','M','F'],
        'Product':['Apple Watch Series 6','Macbook Pro','AirPods Pro','Apple Watch Series 6','iPad'],
        'Product_Category':['Electronics','Electronics','Electronics','Electronics','Electronics'],
        'Comment':['Great product','Good performance','Not satisfied','Not satisfied','Could be better']
        }
df = pd.DataFrame(data)

# Add CSAT_Score column

"""applying the TextBlob library to the 'Comment' column of the dataframe. It is using the 'sentiment.polarity' method to extract the sentiment polarity of each comment, which is a value between -1 and 1 representing negative, neutral and positive sentiments respectively. The result is then assigned to a new column called 'CSAT_Score' in the dataframe."""
df['CSAT_Score'] = df['Comment'].apply(lambda x: TextBlob(x).sentiment.polarity)

"""applying a lambda function to the 'CSAT_Score' column, which segments the sentiment into positive, neutral, and negative by assigning scores of 4, 3, and 2 respectively. It checks if the value in the 'CSAT_Score' column is greater than 0, if so, it assigns a score of 4 for positive sentiment. If it's equal to 0, it assigns a score of 3 for neutral sentiment. If it's less than 0, it assigns a score of 2 for negative sentiment."""
df['CSAT_Score'] = df['CSAT_Score'].apply(lambda x: 4 if x > 0 else (2 if x < 0 else 3))

# Group the dataframe by product and compute the mean
df_grouped = df.groupby(['Product']).mean()

# Reset the index
df_grouped = df_grouped.reset_index()

# Add CSAT_Percentage column
df_grouped['CSAT_Percentage'] = df_grouped['CSAT_Score']*100

# Print the input table
print("Input Table:")
display(df)

# Print the output table
print("Output Table:")
display(df_grouped)
