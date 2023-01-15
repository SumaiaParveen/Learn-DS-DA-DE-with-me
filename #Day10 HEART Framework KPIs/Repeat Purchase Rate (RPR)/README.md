### Repeat Purchase Rate (RPR)

#### RPR of Products

Repeat Purchase Rate (RPR) is a metric that is used to measure the percentage of customers who return to make repeat purchases of a particular product or service. It is calculated by dividing the number of repeat purchases by the total number of purchases made by customers for that product or service. For example, if a product has a RPR of 0.8, it means that 80% of the purchases made for that product were repeat purchases, while 20% were new customers.

How to compute RPR of products from the following dataset?

| Customer | Age | Gender |    Product | Order_Date | Order_Number |
|---------:|----:|-------:|-----------:|-----------:|-------------:|
|     John |  25 |      M |    Shampoo | 2020-01-01 |          100 |
|     Mike |  31 |      M |     Laptop | 2020-01-15 |          101 |
|      Amy |  35 |      F | Smartphone | 2020-02-01 |          102 |
|  Jessica |  28 |      F |    Shampoo | 2020-03-01 |          103 |
|    David |  22 |      M | Smartphone | 2020-04-01 |          104 |
|    Julie |  29 |      F |    Shampoo | 2020-05-01 |          105 |
|    Brian |  32 |      M | Smartphone | 2020-06-01 |          106 |
|    Nancy |  40 |      F |     Laptop | 2020-07-01 |          107 |
|    Steve |  38 |      M | Smartphone | 2020-08-01 |          108 |
|    Karen |  27 |      F |    Shampoo | 2020-09-01 |          109 |
|     John |  25 |      M |    Shampoo | 2020-10-01 |          110 |
|     Mike |  31 |      M |     Laptop | 2020-11-01 |          111 |
|      Amy |  35 |      F |   Notebook | 2020-12-01 |          112 |
|  Jessica |  28 |      F |    Shampoo | 2021-01-01 |          113 |
|    David |  22 |      M | Smartphone | 2021-02-01 |          114 |
|    Julie |  29 |      F |    Shampoo | 2021-03-01 |          115 |
|    Brian |  32 |      M | Smartphone | 2021-04-01 |          116 |
|    Nancy |  40 |      F |     Laptop | 2021-05-01 |          117 |
|    Steve |  38 |      M | Smartphone | 2021-06-01 |          118 |
|    Karen |  27 |      F |        Pen | 2021-07-01 |          119 |

- Step1: Creating labels whether the orders are repeat or new
- Step2: Calculating RPR = (Number of Repeat Purchases of a Product) / (Total Number of Purchases of a Product)

#### Output

|    Product |      RPR |
|-----------:|---------:|
|     Laptop | 1.000000 |
|   Notebook | 0.000000 |
|        Pen | 0.000000 |
|    Shampoo | 0.857143 |
| Smartphone | 0.857143 |

From this output, we can see that for products like Laptop and Shampoo have a RPR of 1, which means that 100% of their purchases are repeat purchases. On the other hand, products like Notebook and, Pen have a RPR of 0, which means that none of their purchases are repeat purchases.
