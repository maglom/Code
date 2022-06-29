SELECT COUNT(*) as 'Total number of rows' FROM food;

SELECT COUNT( DISTINCT food_type) as 'Number of non-null food types' FROM food
WHERE food_type NOTNULL;

SELECT food_type, SUM(food_price)  FROM food
GROUP BY food_type
ORDER BY food_price DESC;

SELECT food_type, food_rating, AVG(food_price) FROM food
GROUP BY food_type, food_rating
ORDER BY food_type, food_rating DESC;

SELECT food_rating, food_name, MIN(food_price) FROM food
GROUP BY food_rating;

SELECT food_type, COUNT(food_name) FROM food
GROUP BY food_type
HAVING COUNT(food_name) > 1; 
