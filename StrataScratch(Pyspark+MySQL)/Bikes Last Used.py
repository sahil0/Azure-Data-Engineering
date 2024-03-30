#Find the last time each bike was in use.
#Output both the bike number and the date-timestamp of the bike's last use (i.e., the date-time the bike was returned). 
#Order the results by bikes that were most recently used.


# Import your libraries
import pyspark
from pyspark.sql.functions import col,max,desc
# Start writing code
dc_bikeshare_q1_2012=dc_bikeshare_q1_2012.groupBy("bike_number").agg(max("end_time").alias("last_used")).orderBy(desc("last_used"))


Mysql:
WITH LastUsed AS(select  DISTINCT bike_number,
end_time AS last_used,
dense_rank() over(PARTITION By bike_number order By end_time desc) AS  rnk
from dc_bikeshare_q1_2012
)
select bike_number,last_used from LastUsed where rnk=1 order by last_used desc
