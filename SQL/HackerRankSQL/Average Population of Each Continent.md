Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and 
their respective average city populations (CITY.Population) rounded down to the nearest integer.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.



```
SELECT  C.CONTINENT,FLOOR(AVG(CT.POPULATION)) FROM CITY AS CT
JOIN COUNTRY AS C ON CT.COUNTRYCODE=C.CODE
GROUP BY C.CONTINENT

```
