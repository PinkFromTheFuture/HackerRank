-- https://www.hackerrank.com/challenges/weather-observation-station-3/problem
-- implemented for MySQL

SELECT
    `STATION`.`CITY`
FROM `STATION`
WHERE `STATION`.`ID` % 2 = 0
GROUP BY `STATION`.`CITY`
;
