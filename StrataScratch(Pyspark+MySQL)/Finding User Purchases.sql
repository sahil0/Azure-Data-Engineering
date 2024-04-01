-- Write a query that'll identify returning active users. A returning active user 
-- is a user that has made a second purchase within 7 days of any other
-- of their purchases. Output a list of user_ids of these returning active users.

--------------------------------------------------Pyspark-------------------------------------------------------

# Import your libraries
import pyspark
from pyspark.sql.functions import col,to_date,months_between,round,datediff,abs,lag
from pyspark.sql.window import Window

# Start writing code
df = amazon_transactions.withColumn("previous_date",lag('created_at',1).over(Window.partitionBy("user_id").orderBy('created_at')))
df=df.withColumn('day_diff',datediff("created_at","previous_date")).select('user_id').filter(col('day_diff')<7).distinct()
df.toPandas()

  
--------------------------------------------------SQL-------------------------------------------------------


  
with cte as(select *,lag(created_at,1,0) over(partition by user_id order by created_at) AS previous_date from amazon_transactions
),
days_difference as(
select user_id,datediff(created_at,previous_date) AS day_difference from cte
)
select DISTINCT user_id from days_difference  where day_difference<7 
order by user_id;


