-- For this challenge you need to create a UNION statement, there are two tables ussales and eusales 
-- the parent company tracks each sale at its respective location in each table, you must all filter the sale price so it 
-- only returns rows with a sale greater than 50.00. You have been tasked with combining that data for future analysis. 
-- Order by location (US before EU), then by id.

-- (us/eu)sales table schema

-- id
-- name
-- price
-- card_name
-- card_number
-- transaction_date

-- resultant table schema
-- location (EU for eusales and US for ussales)
-- id
-- name
-- price (greater than 50.00)
-- card_name
-- card_number
-- transaction_date

ALTER TABLE eusales
ADD location CHAR(2);
UPDATE eusales SET location = 'eu';
ALTER TABLE ussales
ADD location CHAR(2)
UPDATE ussales SET location = 'us';
SELECT * FROM eusales
UNION ALL 
SELECT * FROM ussales;



-- For this challenge you need to create a simple SUM statement that will sum all the ages.

-- people table schema
-- id
-- name
-- age
-- select table schema
-- age_sum (sum of ages)


SELECT SUM(age) as age_sum 
FROM people





--SQL Basics: Simple table totaling.

/*For this challenge you need to create a simple query to display each unique clan with their total points and ranked by their 
total points.

people
--
name
points
clan

You should then return a table that resembles below

rank
clan
total_points
total_people

The query must rank each clan by their total_points, you must return each unqiue clan and if there is no clan name 
(i.e. it's an empty string) you must replace it with [no clan specified], you must sum the total_points for each clan and 
the total_people within that clan.
 */

SELECT 
    RANK() OVER (ORDER BY SUM(points) DESC) AS rank,
    COUNT(name) as total_people, 
    SUM(points) as total_points, 
    COALESCE(NULLIF(clan,''), '[no clan specified]') AS clan 
FROM people
GROUP BY clan

--alternative
-- SELECT 
--   row_number() over (order by sum(points) desc) "rank",
--   CASE WHEN clan = '' THEN '[no clan specified]' else clan END "clan", 
--   sum(points) "total_points", 
--   count(*) "total_people" 
-- from 
--   people 
-- group by 
--   clan 
-- order by 
--   sum(points) desc;