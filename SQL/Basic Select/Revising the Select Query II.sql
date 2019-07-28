-- https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
-- implemented for MySQL

SELECT `CITY`.`NAME`
FROM `CITY`
WHERE `CITY`.`POPULATION` > 120000
AND COUNTRYCODE = "USA"
;
