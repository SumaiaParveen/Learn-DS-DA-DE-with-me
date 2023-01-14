# Import pandas library
import pandas as pd

# Define the data
data = {'Customer': ['Alice','Bob','Charlie','David','Eve'],
        'Age': [25,31,35,28,22],
        'Gender':['F','M','M','M','F'],
        'Product':['iPhone','Macbook Pro','AirPods Pro','Apple Watch Series 6','iPad'],
        'Product_Category':['Electronics','Electronics','Electronics','Electronics','Electronics'],
        'Comment':['Great product','Good performance','Not satisfied','Nice design','Could be better']
        }

# Create a dataframe from the data
df = pd.DataFrame(data)

from textblob import TextBlob

# Create an empty list to store the sentiment scores
sentiment_scores = []

# Iterate through each comment
for comment in df['Comment']:
    # Use TextBlob to extract the sentiment of the comment
    sentiment = TextBlob(comment).sentiment.polarity
    # Assign a score based on the sentiment
    if sentiment > 0:
        score = 4
    elif sentiment == 0:
        score = 3
    else:
        score = 2
    # Append the score to the list
    sentiment_scores.append(score)

# Add the sentiment scores to the dataframe
df['CSAT'] = sentiment_scores

# Calculate the mean of the CSAT column to get the overall CSAT score
csat_score = df['CSAT'].mean()
print("CSAT Score:", csat_score)
