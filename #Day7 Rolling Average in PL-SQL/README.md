### Calculating Rolling Average/Rolling Mean/Moving Average

**Eaxmaple**: We want to track the daily sales of your store to identify trends and make informed decisions about inventory and marketing. However, daily sales can be volatile and hard to interpret, so you want to smooth out the data by calculating rolling averages.

Our task is to calculate the 2-day and 7-day rolling averages for daily sales, and display the results in a way that is easy to understand and compare. This will allow us to identify trends and patterns over time, and make more informed decisions about the business.

To complete this task, we will need to:

- Create a table to store the daily sales data, including the date and quantity sold.
- Insert dummy data into the table to represent a week's worth of sales.
- Calculate the 2-day and 7-day rolling averages for each day, and display the results in separate columns.
- Order the results by date to make it easier to track the trends over time.

Input table:

|ORDER_DATE| ORDER_QUANTITY|
| -------- | ------------- |
|2022-01-01|  10           |            
|2022-01-02|  20           |          
|2022-01-03|  15           |           
|2022-01-04|  25           |           
|2022-01-05|  30           |         
|2022-01-06|  35           |           
|2022-01-07|  40           |         
|2022-01-08|  45           |          
|2022-01-09|  50           |    
|2022-01-10|  55           |  

Output table:

|ORDER_DATE| ORDER_QUANTITY|TWO_DAY_ROLLING_AVERAGE  |SEVEN_DAY_ROLLING_AVERAGE |
| -------- | ------------- |------------------------ | ------------------------ |
|2022-01-01|  10           |             10          |        10                |
|2022-01-02|  20           |             15          |        15.71             |
|2022-01-03|  15           |             17.5        |        16.43             |
|2022-01-04|  25           |             20          |        20                |
|2022-01-05|  30           |             27.5        |        22.86             |
|2022-01-06|  35           |             32.5        |        26                |
|2022-01-07|  40           |             37.5        |        29.57             |
|2022-01-08|  45           |             42.5        |        33                |
|2022-01-09|  50           |             47.5        |        36.57             |
|2022-01-10|  55           |             52.5        |        40                |
