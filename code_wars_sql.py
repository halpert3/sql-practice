"""
You have access to a table of monsters as follows:

** monsters table schema **

id
name
legs
arms
characteristics
Your task is to make a new table where each column should contain the length of the string in the column to its right 
(last column should contain length of string in the first column). Remember some column values are not currently strings.
Column order and titles should remain unchanged:

** output table schema **

id
name
legs
arms
characteristics
""" 
SELECT 
  LENGTH(name) AS id,
  LENGTH(CAST(legs AS text)) AS name,
  LENGTH(CAST(arms AS text)) AS legs,
  LENGTH(characteristics) AS arms,
  LENGTH(CAST(id AS text)) AS characteristics
FROM monsters

## A short cut for CAST seems to be ::
# LENGTH(legs::text) AS name





"""
SQL Basics: Raise to the Power - 7th kyu

Given the following table 'decimals':

** decimals table schema **

id
number1
number2
Return a table with one column (result) which is the output of number1 raised to the power of number2.
"""

SELECT POWER(number1, number2) AS result
FROM decimals

# or 

SELECT
  number1 ^ number2 AS Result
FROM
  decimals



"""

SQL Basics: Simple HAVING- 6th

For this challenge you need to create a simple HAVING statement, you want to count how many people have the same age and return 
the groups with 10 or more people who have that age.

people table schema

id
name
age

return table schema

age
total_people
"""
SELECT 
  age,
  COUNT(id) total_people
FROM 
  people
GROUP BY
  age
HAVING 
  COUNT(id) > 9; 
  # even though I rename COUNT(id) AS total_people above, touble_people > 9 doesn't work. Need COUNT(id) > 9 






"""
SQL Basics: Truncating - 7th kyu

Given the following table 'decimals':

** decimals table schema **

id
number1
number2
Return a table with one column (towardzero) where the values are the result of number1 + number2 truncated towards zero.
"""


SELECT TRUNC(number1 + number2, 1) AS towardzero 
FROM decimals


"""
SQL Basics: Up and Down - 7th kyu

Given a table of random numbers as follows:

** numbers table schema **

id
number1
number2

Your job is to return table with similar structure and headings, where if the sum of a column is odd, the column shows the 
minimum value for that column, and when the sum is even, it shows the max value. You must use a case statement.

** output table schema **

number1
number2
"""
SELECT 
CASE 
  WHEN SUM(number1)%2 = 0 THEN MAX(number1) ELSE MIN(number1)
  END AS number1,
CASE 
  WHEN SUM(number2)%2 = 0 THEN MAX(number1) ELSE MIN(number2)
  END AS number2
FROM numbers






"""Given the following table 'decimals':

** decimals table schema **

id
number1
number2

Return a table with two columns (cuberoot, logarithm) where the values in cuberoot are the cube root of those provided in 
number1 and the values in logarithm are changed to the natural logarithm of those in number2.
"""


SELECT 
  cbrt(number1) as cuberoot,
  ln(number2) as logarithm
FROM decimals






"""
Given a demographics table in the following format:

** demographics table schema **

id
name
birthday
race
you need to return the same table where all text fields (name & race) are changed to the ascii code of their first byte.

e.g. Verlie = 86 Warren = 87 Horace = 72 Tracy = 84
"""

SELECT ASCII(name) as name, ASCII(race) as race, id, birthday
FROM demographics








"""
SQL Basics: Simple GROUP BY

For this challenge you need to create a simple GROUP BY statement, you want to group all the people by their age and 
count the people who have the same age.

people table schema
id
name
age

SELECT table schema
age [group by]
people_count (people count)
"""

SELECT age, COUNT(people) AS people_count
FROM people
GROUP BY age;





"""
For this challenge you need to create a simple DISTINCT statement, you want to find all the unique ages.

people table schema
id
name
age
 table schema
age (distinct)
"""

SELECT DISTINCT age
FROM people 





"""
For this challenge you need to create a simple SELECT statement that will return all columns from the products table, and 
join to the companies table so that you can return the company name. 

You should return all product fields as well as the company name as "company_name".
"""

SELECT 
    products.*,
    companies.name AS company_name
FROM products
INNER JOIN companies ON products.company_id = companies.id

# alternative
SELECT p.*,
       c.name AS company_name
  FROM products p,
       companies c
 WHERE c.id = p.company_id



# -- For this challenge you need to create a UNION statement, there are two tables ussales and eusales 
# -- the parent company tracks each sale at its respective location in each table, you must all filter the sale price so it 
# -- only returns rows with a sale greater than 50.00. You have been tasked with combining that data for future analysis. 
# -- Order by location (US before EU), then by id.

# -- (us/eu)sales table schema

# -- id
# -- name
# -- price
# -- card_name
# -- card_number
# -- transaction_date

# -- resultant table schema
# -- location (EU for eusales and US for ussales)
# -- id
# -- name
# -- price (greater than 50.00)
# -- card_name
# -- card_number
# -- transaction_date

ALTER TABLE eusales
ADD location CHAR(2);
UPDATE eusales SET location = 'eu';
ALTER TABLE ussales
ADD location CHAR(2)
UPDATE ussales SET location = 'us';
SELECT * FROM eusales
UNION ALL 
SELECT * FROM ussales;



# -- For this challenge you need to create a simple SUM statement that will sum all the ages.

# -- people table schema
# -- id
# -- name
# -- age
# --  table schema
# -- age_sum (sum of ages)


SELECT SUM(age) as age_sum 
FROM people





# --SQL Basics: Simple table totaling.

# /*For this challenge you need to create a simple query to display each unique clan with their total points and ranked by their 
# total points.

# people
# --
# name
# points
# clan

# You should then return a table that resembles below

# rank
# clan
# total_points
# total_people

# The query must rank each clan by their total_points, you must return each unqiue clan and if there is no clan name 
# (i.e. it's an empty string) you must replace it with [no clan specified], you must sum the total_points for each clan and 
# the total_people within that clan.
#  */

SELECT 
    RANK() OVER (ORDER BY SUM(points) DESC) AS rank,
    COUNT(name) as total_people, 
    SUM(points) as total_points, 
    COALESCE(NULLIF(clan,''), '[no clan specified]') AS clan 
FROM people
GROUP BY clan

# --alternative
SELECT 
  row_number() over (order by sum(points) desc) "rank",
  CASE WHEN clan = '' THEN '[no clan specified]' else clan END "clan", 
  sum(points) "total_points", 
  count(*) "total_people" 
 from 
 people 
 group by 
   clan 
 order by 
   sum(points) desc;