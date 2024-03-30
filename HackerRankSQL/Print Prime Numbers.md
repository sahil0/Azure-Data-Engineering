Write a query to print all prime numbers less than or equal to . Print your result on a single line, and use the ampersand () character as your separator (instead of a space).

For example, the output for all prime numbers  would be:

2&3&5&7
```
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/]
/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
CREATE TABLE PRIME_NUM(NUM INT);
DECLARE @N INT;
DECLARE @DIVIDER INT;
DECLARE @PRIMECHECK BIT;
SELECT @N=1;
WHILE @N <=1000
    BEGIN
    SELECT @DIVIDER =@N-1;
    SELECT @PRIMECHECK=1;
    -- CHECEK IF ALL THE NUMBERE BELOW THE MAIN NUMBER ANY OF THEM DIVIDE THAT NUMBER
    --- IF ANY NUMBER IS DIVIDING OBVIOUSLY ITS NOT PRIME 
    ---PRIMECHECK IS TO KEEP TRACK
    WHILE @DIVIDER >1
        BEGIN
        IF @N % @DIVIDER=0
            SELECT @PRIMECHECK=0;
        SELECT @DIVIDER=@DIVIDER-1
        END
    IF @PRIMECHECK=1 AND @N<>1
        INSERT INTO PRIME_NUM (NUM) VALUES (@N);
    SELECT @N=@N+1
    END
SELECT STRING_AGG(NUM,'&') FROM PRIME_NUM;
        

```
