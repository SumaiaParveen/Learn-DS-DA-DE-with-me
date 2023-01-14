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
| Alice    | 25  | F      | iPhone               | Electronics      | Great product    |
| Bob      | 31  | M      | Macbook Pro          | Electronics      | Good performance |
| Charlie  | 35  | M      | AirPods Pro          | Electronics      | Not satisfied    |
| David    | 28  | M      | Apple Watch Series 6 | Electronics      | Nice design      |
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

*We will compute the CSAT score using the 'Comment' column in Python.* [See the full solution here.]()

### Output

| Customer | Age | Gender | Product              | Product_Category | Comment          | CSAT_Score | CSAT_Percentage |
|----------|-----|--------|----------------------|------------------|------------------|------------|-----------------|
| Alice    | 25  | F      | iPhone               | Electronics      | Great product    | 1          | 60.0            |
| Bob      | 31  | M      | Macbook Pro          | Electronics      | Good performance | 1          | 60.0            |
| Charlie  | 35  | M      | AirPods Pro          | Electronics      | Not satisfied    | 0          | 60.0            |
| David    | 28  | M      | Apple Watch Series 6 | Electronics      | Nice design      | 1          | 60.0            |
| Eve      | 22  | F      | iPad                 | Electronics      | Could be better  | 0          | 60.0            |


The CSAT (Customer Satisfaction Score) was calculated by using the TextBlob library to classify the customer's comments as positive or negative.

The TextBlob library uses a pre-trained model to classify the sentiment of a given text as positive or negative. Based on the example provided, The function calculate_csat was used to calculate the score for each customer's comment, a score of greater than 0 is considered as positive and less than 0 is considered as negative.

The final dataframe shows that there are 4 positive comments and 2 negative comments, which gives an overall CSAT percentage of 80%. This means that 80% of the customers are satisfied with the product or service.

*It's important to note that this is a simple way to calculate the CSAT score using TextBlob, the score might not be accurate for all cases and you might want to consider using other libraries or techniques to perform a more accurate sentiment analysis.*

Also, it's worth mentioning that a high CSAT score does not necessarily mean that the customers are completely satisfied with the product or service, and a low score does not necessarily mean that the customers are completely unsatisfied. It's just an indicator of the general sentiment of the customers.
