SELECT country, city, COUNT(*) AS customer_count FROM customer
GROUP BY country, city;

SELECT c.name, c.city, c.country FROM customer c
JOIN paper_subscription ps ON c.id = ps.customer_id
WHERE ps.status = 'Active';

SELECT c.name, a.name, COUNT(ar.date) AS number_of_reads FROM customer c 
JOIN article_reads ar ON c.id =  ar.customer_id 
JOIN article a ON ar.article_id = a.id
GROUP BY c.name, a.name;

SELECT c.name, COUNT(DISTINCT a.name) AS number_of_distinct_articles FROM customer c 
JOIN article_reads ar ON c.id =  ar.customer_id 
JOIN article a ON ar.article_id = a.id
GROUP BY c.name
ORDER BY number_of_distinct_articles DESC
LIMIT 10;

SELECT c.name, COUNT(DISTINCT a.name) AS number_of_distinct_articles FROM customer c 
JOIN article_reads ar ON c.id =  ar.customer_id 
JOIN article a ON ar.article_id = a.id
JOIN paper_subscription ps ON c.id = ps.customer_id
GROUP BY c.name
HAVING number_of_distinct_articles > 200 AND ps.status = 'Inactive'
ORDER BY number_of_distinct_articles DESC;

SELECT c.country, a.id AS article_id, COUNT(ar.date) AS total_reads FROM customer c 
JOIN article_reads ar ON c.id = ar.customer_id 
JOIN article a ON a.id = ar.article_id
GROUP BY c.country, a.id; 

SELECT DISTINCT c.country,a.name FROM customer c
JOIN article a ON c.id = a.id 
JOIN article_reads ar ON a.id = ar.customer_id 
GROUP BY c.country
ORDER BY COUNT(ar.article_id) desc;

