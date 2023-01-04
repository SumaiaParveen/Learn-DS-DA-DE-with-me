from scipy.stats import mannwhitneyu
import pandas as pd

"""This code creates a pandas DataFrame with two columns: time and satisfaction. The time column contains the time period (before or after the change in product features) and the satisfaction column contains the satisfaction levels of customers on a scale (e.g., 1 to 10)"""
  
# Creating DataFrame manually
data = pd.DataFrame({
    'time': ['before', 'before', 'before', 'before', 'before', 'before', 'before', 'before', 'before', 'after', 'after', 'after', 'after', 'after', 'after', 'after', 'after'],
    'satisfaction': [4, 5, 6, 6, 5, 4, 3, 2, 1, 4, 5, 6, 6, 5, 4, 3, 2]
})

# Create a new column containing ordinal values as per the test assumption
data['satisfaction_rank'] = data['satisfaction'].rank()

"""Next, we need to split the data into two groups based on the time period (before or after the change in product features)"""

before_group = data[data['time'] == 'before']['satisfaction_rank']
after_group = data[data['time'] == 'after']['satisfaction_rank']

"""Call the mannwhitneyu() function and pass it the two groups of data as arguments. The function will return a tuple with two values: the Mann-Whitney U statistic and the p-value. The p-value is the probability that the observed difference between the two groups is due to chance, and a smaller p-value indicates a stronger evidence of a significant difference between the groups."""

u, p = mannwhitneyu(before_group, after_group)
print(f'Mann-Whitney U statistic: {u}')
print(f'p-value: {p}')

"""To interpret the results of the Mann-Whitney U test, we need to compare the p-value to a significance level (e.g., 0.05). If the p-value is less than the significance level, we can conclude that there is a significant difference between the two groups. If the p-value is greater than the significance level, we can conclude that there is not a significant difference between the two groups."""

if p < 0.05:
    print('There is a significant difference between the two groups.')
else:
    print('There is not a significant difference between the two groups.')
