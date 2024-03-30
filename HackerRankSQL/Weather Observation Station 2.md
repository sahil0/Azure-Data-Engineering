Query the following two values from the STATION table:

The sum of all values in LAT_N rounded to a scale of  decimal places.
The sum of all values in LONG_W rounded to a scale of  decimal places.
Input Format

The STATION table is described as follows:



where LAT_N is the northern latitude and LONG_W is the western longitude.

Output Format

Your results must be in the form:

lat lon
where  is the sum of all values in LAT_N and  is the sum of all values in LONG_W. Both results must be rounded to a scale of  decimal places.


```
SELECT ROUND(sum(LAT_N),2),ROUND(sum(LONG_W),2) FROM STATION

SELECT  CAST(SUM(LAT_N) AS DECIMAL(18, 2)),CAST(SUM(LONG_W) AS DECIMAL(18,2)) FROM STATION
```
