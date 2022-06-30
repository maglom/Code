CREATE TABLE food (
	food_name TEXT,
	food_type TEXT,
	food_rating INTEGER CHECK ((food_rating) >= 1 AND (food_rating) <= 5),
	food_price INTEGER NOT NULL
);

INSERT INTO food (food_name, food_type, food_rating, food_price)
VALUES 
	("Cheese", "Topping", 5, 19),
	("Chicken", "Meat", 4, 50),
	("Tortilla", "Container", 2, 20),
	("Corn", "Topping", 3, 5),
	("Salad", "Greens", 1, 7),
	("Sauce", "Dressing", 5, 25),
	("Beans", "Ingredient", 3, 15),
	("Tacospice", "Spice", 2, 30),
	("Bellpepper", "Greens", 3, 23),
	("Sourcream", "Dressing", 5, 29);

SELECT DISTINCT food_type FROM food
ORDER BY food_type DESC;

SELECT * FROM food
WHERE food_price > 25;

SELECT * FROM food
WHERE food_price > 20 AND (food_rating = 1 OR food_rating = 4);

SELECT * FROM food
WHERE food_price > 10 AND food_rating BETWEEN 1 AND 4;

SELECT * FROM food
WHERE food_price > 10 AND food_rating IN (1, 2, 3, 4);

SELECT food_name, food_type, food_price FROM food;

SELECT food_name, food_type, food_price FROM food
ORDER BY food_price DESC
LIMIT 3;

SELECT * FROM food
WHERE food_name LIKE 'S%';