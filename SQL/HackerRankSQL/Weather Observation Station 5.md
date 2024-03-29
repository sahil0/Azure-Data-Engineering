Weather Observation Station 5

![Weather Observation Station 5](https://github.com/sahil0/Azure-Data-Engineering/assets/22682814/4db45ef2-bc7a-4513-9e5e-e7302081db39)



```
WITH RankedCities AS (
    SELECT 
        CITY,
        LENGTH(CITY) AS CityLength,
        ROW_NUMBER() OVER (ORDER BY LENGTH(CITY), CITY) AS CityRankAsc,
        ROW_NUMBER() OVER (ORDER BY LENGTH(CITY) DESC, CITY) AS CityRankDesc

    FROM STATION
)
SELECT CITY, CityLength
FROM RankedCities
WHERE CityRankAsc = 1 OR CityRankDesc=1
```
Weather Observation Station 6:

Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

```
-- WITH CTE AS(
-- SELECT CITY
-- FROM STATION
-- WHERE CITY LIKE 'A%' OR CITY LIKE 'E%' OR CITY LIKE 'I%' OR CITY LIKE 'O%' OR CITY LIKE 'U%'
-- )
-- SELECT DISTINCT CITY FROM CTE

SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[aeiouAEIOU]'
```
Weather Observation Station 7:

Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

```

SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '[aeiouAEIOU]$'

```
Weather Observation Station 8:

Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
```

select distinct(CITY) from STATION 
WHERE CITY REGEXP '^[aeiouAEIOU]' AND CITY REGEXP '[aeiouAEIOU]$';
```

Weather Observation Station 9:

Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.


```
SELECT DISTINCT CITY 
FROM STATION 
WHERE CITY NOT RLIKE '^[aeiouAEIOU].*$'
```
Weather Observation Station 10:

Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.


```
SELECT DISTINCT CITY FROM STATION
WHERE CITY NOT RLIKE '[aeiouAEIOU]$'
```
OR
```
SELECT DISTINCT CITY FROM STATION
WHERE CITY NOT REGEXP  '[aeiouAEIOU]$'
```

Weather Observation Station 11:

Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.


```
SELECT DISTINCT city FROM station WHERE city RLIKE '^[^aeiouAEIOU].*|.*[^AEIOUaeiou]$';
```

Weather Observation Station 12:

Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.
```
SELECT DISTINCT city FROM station WHERE city RLIKE '^[^aeiouAEIOU].*'
AND CITY RLIKE '.*[^AEIOUaeiou]$'
```
