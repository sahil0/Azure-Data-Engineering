Find the top 10 users that have traveled the greatest distance. Output their id, name and a total distance traveled.

Pyspark:
# Import your libraries
import pyspark
from pyspark.sql.functions import sum,desc
# Start writing code
df=lyft_rides_log.join(lyft_users,lyft_users.id==lyft_rides_log.user_id,'inner').select(lyft_users.id,lyft_users.name,lyft_rides_log.distance)
df=df.groupBy("id","name").agg(sum(df.distance).alias("distance")).orderBy(desc("distance")).limit(10)
# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()

MySQL:
WITH DistanceTrave AS(select U.id,U.name,sum(distance) AS total_dist 
from lyft_rides_log AS L
join lyft_users AS U ON U.id=L.user_id
group by U.id,U.name
)
select * from DistanceTrave
order by total_dist desc
LIMIT 10
