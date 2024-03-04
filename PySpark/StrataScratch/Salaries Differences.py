Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. 
Output just the absolute difference in salaries.

# Import your libraries
from pyspark.sql.functions import col,max,min,abs



df = db_employee.join(db_dept, db_employee.department_id == db_dept.id, 'inner').where(col('department').isin('engineering', 'marketing')).groupby().pivot('department').agg(max('salary')).select(abs(col('engineering') - col('marketing')).alias('salary_difference'))


# To validate your solution, convert your final pySpark df to a pandas df
df.toPandas()

