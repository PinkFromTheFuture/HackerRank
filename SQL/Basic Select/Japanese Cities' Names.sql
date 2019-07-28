-- https://www.hackerrank.com/challenges/japanese-cities-name/problem
-- implemented for MySQL

SELECT `CITY`.`NAME`
FROM `CITY`
WHERE `CITY`.`COUNTRYCODE` = 'JPN'
;
