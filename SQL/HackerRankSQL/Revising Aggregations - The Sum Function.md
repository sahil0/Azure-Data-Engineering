![image](https://github.com/sahil0/Azure-Data-Engineering/assets/22682814/3cb12149-eabd-4999-80da-f51e807bc86f)


Query the total population of all cities in CITY where District is California.

```
select sum(population) from CITY where District='California'
```



## Average Population:

>. Query the average population for all cities in CITY, rounded down to the nearest integer.


```
select floor(avg(population)) from CITY
```

>. Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.
```
select sum(population) from CITY where COUNTRYCODE='JPN'
```
## Population Density Difference

> Query the difference between the maximum and minimum populations in CITY.
```
select max(population) - min(population) from CITY

```
