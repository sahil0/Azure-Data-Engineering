# Import your libraries
import pyspark
from pyspark.sql.functions import mean,expr,to_date,col, when, min, max,row_number,first,avg
from pyspark.sql.window import Window
from pyspark.sql import functions as F
# # Start writing code
fb_load=facebook_web_log.filter(col('action').isin('page_load')).orderBy('user_id')
fb_load=fb_load.select(col("user_id").alias('load_user_id'), col("timestamp").alias('load_timestamp')) 
fb_exit=facebook_web_log.filter(col('action').isin('page_exit')).orderBy('user_id')
fb_exit=fb_exit.select(col("user_id").alias('exit_user_id'), col("timestamp").alias('exit_timestamp'))
df=fb_load.join(fb_exit,fb_load.load_user_id==fb_exit.exit_user_id,"left").filter(col('load_timestamp')<col('exit_timestamp'))
df=df.withColumn("date_load",to_date(col('load_timestamp'))).groupBy("load_user_id","date_load").agg(max("load_timestamp").alias("timestamp_load"),min("exit_timestamp").alias("timestamp_exit")).withColumn('duration',col("timestamp_exit")-col("timestamp_load")).filter(col("duration")>F.expr("INTERVAL 0 days")).groupBy("load_user_id").agg(mean("duration").alias("duration"))

# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()
