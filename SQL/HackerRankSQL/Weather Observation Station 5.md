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


