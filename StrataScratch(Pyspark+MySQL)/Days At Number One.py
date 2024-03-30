(* Find the number of days a US track has stayed in the 1st position for both the US and worldwide rankings on the same day. Output the track name and the number
of days in the 1st position. Order your output alphabetically by track name.
If the region 'US' appears in dataset, it should be included in the worldwide ranking. *)
Pyspark:
# Import your libraries
import pyspark
from pyspark.sql.functions import col,coalesce,count
# Start writing code
us_rank=spotify_daily_rankings_2017_us.withColumnRenamed('trackname','us_trackname')
w_rank=spotify_worldwide_daily_song_ranking
df=us_rank.join(w_rank,us_rank.position==w_rank.position,'inner')
df=df.filter((col("region")=="us") & (us_rank.date==w_rank.date) & ((w_rank.position==1) | (us_rank.position==1))).withColumn("trackname", coalesce(us_rank.us_trackname, w_rank.trackname))
df=df.groupby("trackname").agg(count("*").alias('n_days_on_n1_position')).orderBy("trackname")
# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()


MySQL:
select  COALESCE(WR.trackname,DR.trackname) AS trackname,count(*)
from spotify_daily_rankings_2017_us AS DR
join spotify_worldwide_daily_song_ranking AS WR ON WR.position=DR.position
where region='us' and DR.date=WR.date and (WR.position=1 or DR.position=1)
group by trackname;


