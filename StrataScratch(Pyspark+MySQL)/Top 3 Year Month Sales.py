The sales team wants to find out which months had the highest sales. Based on the sales data provided, you must determine the top three year-month combinations for sales.
Your output should include the top three monthly sales in the format YYYY-MM as well as the corresponding cumulative sales.

Pyspark:
# Import your libraries
import pyspark
from pyspark.sql.functions import date_format,col,sum,desc
# Start writing code
df=fct_customer_sales
df=df.withColumn('order_date',date_format(df.order_date,'yyyy-MM'))
df=df.groupBy(df.order_date).agg(sum(df.order_value).alias('total_sales')).orderBy(desc(col("total_sales"))).limit(3)
# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()


Mysql:
with cte as(select date_format(order_date,'%Y-%m') AS combo_date,order_value
from fct_customer_sales
)
select combo_date,sum(order_value) AS val from cte 
group by combo_date
order by val desc
limit 3;

