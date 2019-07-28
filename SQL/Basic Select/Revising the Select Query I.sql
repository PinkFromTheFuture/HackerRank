-- https://www.hackerrank.com/challenges/revising-the-select-query/problem
-- implemented for MySQL

SELECT *
FROM `CITY`
WHERE `CITY`.`POPULATION` > 100000
AND COUNTRYCODE = "USA"
;
