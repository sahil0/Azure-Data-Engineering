![Weather Observation Station 5](https://github.com/sahil0/Azure-Data-Engineering/assets/22682814/4db45ef2-bc7a-4513-9e5e-e7302081db39)



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
