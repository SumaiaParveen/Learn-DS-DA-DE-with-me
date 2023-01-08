-- Create the table
create table orders (
  order_date date,
  order_quantity number
);

-- Insert dummy data into the table
insert into orders (order_date, order_quantity)
values (to_date('2022-01-01', 'yyyy-mm-dd'), 10);
insert into orders (order_date, order_quantity)
values (to_date('2022-01-02', 'yyyy-mm-dd'), 20);
insert into orders (order_date, order_quantity)
values (to_date('2022-01-03', 'yyyy-mm-dd'), 15);
insert into orders (order_date, order_quantity)
values (to_date('2022-01-04', 'yyyy-mm-dd'), 25);
insert into orders (order_date, order_quantity)
values (to_date('2022-01-05', 'yyyy-mm-dd'), 30);
insert into orders (order_date, order_quantity)
values (to_date('2022-01-06', 'yyyy-mm-dd'), 35);
insert into orders (order_date, order_quantity)
values (to_date('2022-01-07', 'yyyy-mm-dd'), 40);
insert into orders (order_date, order_quantity)
values (to_date('2022-01-08', 'yyyy-mm-dd'), 45);
insert into orders (order_date, order_quantity)
values (to_date('2022-01-09', 'yyyy-mm-dd'), 50);
insert into orders (order_date, order_quantity)
values (to_date('2022-01-10', 'yyyy-mm-dd'), 55);

-- Calculate the 2-day and 7-day rolling averages and display the results

-- Calculate the 2-day and 7-day rolling averages and display the results
select o1.order_date, o1.order_quantity, round((o1.order_quantity + o2.order_quantity) / 2, 2) as two_day_rolling_average, round((o1.order_quantity + o2.order_quantity + o3.order_quantity + o4.order_quantity + o5.order_quantity + o6.order_quantity + o7.order_quantity) / 7, 2) as seven_day_rolling_average
from orders o1
left join orders o2 on o2.order_date = o1.order_date - interval '1' day
left join orders o3 on o3.order_date = o1.order_date - interval '2' day
left join orders o4 on o4.order_date = o1.order_date - interval '3' day
left join orders o5 on o5.order_date = o1.order_date - interval '4' day
left join orders o6 on o6.order_date = o1.order_date - interval '5' day
left join orders o7 on o7.order_date = o1.order_date - interval '6' day
order by o1.order_date;
