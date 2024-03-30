Consider p1 at (a, b) and p2 at (c, d) and  to be two points on a 2D plane.

 a   happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
 b   happens to equal the minimum value in Western Longitude (LONG_W in STATION).
 c   happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
 d   happens to equal the maximum value in Western Longitude (LONG_W in STATION).

/*
  Definition: The distance between two points measured along axes at right angles. In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|
 |x1 - x2| + |y1 - y2|.
*/

Query: 
  ```
with cte as(
select min(LAT_N) AS x1,min(LONG_W) as y1,max(LAT_N) as x2,max(LONG_W) as y2 from STATION
    )
select ROUND(abs(x1-x2) + abs(y1-y2),4) from cte
  
  ```
