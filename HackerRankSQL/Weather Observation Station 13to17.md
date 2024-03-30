
#### Weather Observation Station 13.


Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.

*/
```
SELECT ROUND(SUM(LAT_N) ,4) FROM STATION WHERE LAT_N > 38.7880 AND LAT_N < 137.2345

SELECT CAST(SUM(LAT_N) AS DECIMAL(18,4)) FROM STATION WHERE LAT_N > 38.7880 AND LAT_N < 137.2345
```




#### Weather Observation Station 14.

Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 137.2345 AND  Truncate your answer to  4 decimal places.

*/
```
SELECT ROUND(SUM(LAT_N) ,4) FROM STATION WHERE LAT_N > 38.7880 AND LAT_N < 137.2345

SELECT CAST(SUM(LAT_N) AS DECIMAL(18,4)) FROM STATION WHERE LAT_N > 38.7880 AND LAT_N < 137.2345
```

#### Weather Observation Station 15.

Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137.2345  Truncate your answer to  4 decimal places.

```
SELECT CAST(LONG_W AS DECIMAL(18,4)) FROM STATION WHERE LAT_N=(SELECT MAX(LAT_N) FROM STATION WHERE LAT_N<137.2345)

SELECT ROUND(LONG_W,4) FROM STATION WHERE LAT_N=(SELECT MAX(LAT_N) FROM STATION WHERE LAT_N<137.2345)
```

#### Weather Observation Station 16.


Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780.Round your answer to 4 decimal places.

```
SELECT ROUND(MIN(LAT_N),4) FROM STATION WHERE LAT_N > 38.7780
```



#### Weather Observation Station 17.


Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than 38.7780
```
SELECT ROUND(LONG_W,4) FROM STATION WHERE LAT_N=(SELECT MIN(LAT_N) FROM STATION WHERE LAT_N > 38.7780)
```
