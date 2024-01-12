We define an employee's total earnings to be their monthly  worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.
```

WITH CREATECOL AS(
SELECT salary*months AS EARNINGS
FROM EMPLOYEE 
)
SELECT CONCAT((SELECT MAX(EARNINGS) FROM CREATECOL), ' ', (SELECT COUNT(*) FROM (SELECT RANK() OVER (ORDER BY EARNINGS DESC) AS DenseRank
FROM CREATECOL) R WHERE  R.DenseRank = 1)
             )

-- select concat((select max(months*salary) from employee), ' ',
--               (select count(*) from
--                (select rank() over (order by months*salary desc) as  
 
--                  rnk from employee) t where t.rnk = 1)
--                );


```
