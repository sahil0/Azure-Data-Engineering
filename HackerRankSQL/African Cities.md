
> Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

> Note: CITY.CountryCode and COUNTRY.Code are matching key columns





```

SELECT CT.NAME FROM CITY AS CT JOIN COUNTRY AS C ON CT.COUNTRYCODE=C.CODE
WHERE C.CONTINENT='Africa'

```
