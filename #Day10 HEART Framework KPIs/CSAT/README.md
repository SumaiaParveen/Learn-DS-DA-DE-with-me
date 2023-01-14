### Customer Satisfaction Score (CSAT)

The Customer Satisfaction Score (CSAT) is a metric used to measure customer satisfaction with a particular product or service. It is often used in the Heart framework, which is a customer satisfaction model that focuses on three main areas: Head (customer satisfaction with the product or service), Heart (customer loyalty and engagement), and Hands (customer behavior and actions).

In the Heart framework, CSAT is considered to be a measure of a customer's satisfaction with the product or service, and it is typically used in conjunction with other metrics such as **Net Promoter Score (NPS)** and **Customer Effort Score (CES)**.

The CSAT score is usually calculated by asking customers a simple question like "How satisfied are you with our product/service?" on a scale of 1-5 or 1-10. The scores are then averaged to get a CSAT score for a particular product or service.

It's a quick and easy way to understand how customers feel about your product or service at a given point in time, and it can be used to track changes over time and identify areas where improvements can be made.

Here are some examples of questions that can be asked to measure customer satisfaction on an e-commerce book site:

- How satisfied are you with the overall shopping experience on our website?
- How easy was it to find the book you were looking for?
- How satisfied are you with the product descriptions and images?
- How satisfied are you with the delivery time and packaging of your order?
- How satisfied are you with the customer service you received?
- How likely are you to recommend our website to a friend or family member?
- How likely are you to purchase from us again in the future?
- How satisfied are you with the pricing and value for money of the books on our website?
- How satisfied are you with the checkout process and payment options?
- How satisfied are you with the return and refund policy?

### Example

We want to calculate CSAT from this dataset:

| Customer | Age | Gender | Product              | Product Category | Comment          |
|----------|-----|--------|----------------------|------------------|------------------|
| Alice    | 25  | F      | Apple Watch Series 6 | Electronics      | Great product    |
| Bob      | 31  | M      | Macbook Pro          | Electronics      | Good performance |
| Charlie  | 35  | M      | AirPods Pro          | Electronics      | Not satisfied    |
| David    | 28  | M      | Apple Watch Series 6 | Electronics      | Not satisfied    |
| Eve      | 22  | F      | iPad                 | Electronics      | Could be better  |

there are several ways to calculate the CSAT (Customer Satisfaction Score) from a dataset, such as:

- Using sentiment analysis libraries to classify customer comments as positive or negative, and then calculating the percentage of positive comments.
- Using a Likert scale question to calculate the average score.
- Using a combination of both methods, where customers are asked to leave a comment and also rate their satisfaction on a scale.
- Using survey tools and asking customers to rate their satisfaction, then calculating the average score.
- Using Natural Language Processing techniques like Latent Sentiment Analysis.
- Using Machine Learning algorithms to classify the comments as positive or negative based on the training data.
- Using a combination of multiple methods to get a more accurate and well-rounded understanding of customer satisfaction.

The choice of method will depend on the specific needs of the analysis and the data available.

*We will compute the CSAT score using the 'Comment' column in Python.* [See the full solution here.](https://github.com/SumaiaParveen/Learn-DS-DA-DE-with-me/blob/main/%23Day10%20HEART%20Framework%20KPIs/CSAT/Sentiment%20Analysis%20for%20CSAT.py)

### Output

|              Product |  Age | CSAT_Score | CSAT_Percentage | 
|---------------------:|-----:|-----------:|----------------:|
|          AirPods Pro | 35.0 |        2.0 |           0.0 |   
| Apple Watch Series 6 | 26.5 |        3.0 |           50.0 |   
|          Macbook Pro | 31.0 |        4.0 |           100.0 |   
|                 iPad | 22.0 |        4.0 |           100.0 |   


The CSAT (Customer Satisfaction Score) was calculated by using the TextBlob library to classify the customer's comments as positive or negative.

The TextBlob library uses a pre-trained model to classify the sentiment of a given text as positive or negative. It extracts the sentiment of each customer's comment, and assigns a score of 4 for positive sentiment, 3 for neutral sentiment, and 2 for negative sentiment. This score is added to the dataset as the "CSAT_Score" column.

The dataset is then grouped by product, and for each group, the average CSAT score and the percentage of comments that have a score of 4 (positive sentiment) are calculated and added to a list.

The percentage for AirPods Pro is 0% which indicates that none of the comments for the Airpods pro are positive,
and the percentage for Apple Watch Series 6 is 50% which indicates that half of the comments are positive while the other half are not,
and the percentage for Macbook Pro and iPad are 100% which indicates that all the comments are positive.

*It's important to note that this is a simple way to calculate the CSAT score using TextBlob, the score might not be accurate for all cases and you might want to consider using other libraries or techniques to perform a more accurate sentiment analysis.*

Also, it's worth mentioning that a high CSAT score does not necessarily mean that the customers are completely satisfied with the product or service, and a low score does not necessarily mean that the customers are completely unsatisfied. It's just an indicator of the general sentiment of the customers.
