select title, (
		case
			when title like '%Dinosaur%' then 'Dino er gøy'
			else 'filmer uten dino er kjipt'
		end) as rating from film
		order by rating asc;
	
select distinct first_name from actor;

select distinct on (first_name) first_name, last_name from actor
order by first_name;

select rental_id, return_date from rental
where return_date is not null
order by return_date desc;

select rental_id, return_date from rental
where return_date is not null
order by return_date desc
limit 1;

select rental_id, return_date from rental
where return_date is not null
order by return_date desc
offset 1
limit 3;


select 
	first_name,
	last_name
from
	customer
where 
	address_id = (
		select 
			address_id 
		from
			address
		where 
			city_id = (
				select 
					city_id 
				from 
					city
				where 
					city = 'York'));
				
	

select f.title from film f
join film_category fc on f.film_id = fc.film_id
join category c on fc.category_id = c.category_id
where c.name = 'Comedy';

select * from payment cross join rental;

select count(*) from payment cross join rental;

select f.title, a.first_name, a.last_name from film f 
cross join actor a;

select c.first_name, c.last_name, a.address, a.address2, a.district from customer c
join address a on c.address_id = a.address_id;

select f.title, c.name as category from film f
join film_category fc on f.film_id = fc.film_id 
join category c on c.category_id = fc.category_id;

select a.first_name, a.last_name, f.title from actor a 
join film_actor fa on a.actor_id = fa.actor_id 
join film f on f.film_id = fa.film_id;

-- 22

select distinct a.first_name, a.last_name, c.name as category from actor a 
join film_actor fa on fa.actor_id = a.actor_id 
join film_category fc on fc.film_id = fa.film_id
join category c on c.category_id = fc.category_id;

--23

select c.city, a.address, a.address2 from city c 
left join address a ON a.city_id = c.city_id
order by city;

--24

select c.city, a.address, a.address2 from city c 
full join address a ON a.city_id = c.city_id
where a.address is null;

--25

select i.inventory_id, i.film_id, f.title from inventory i 
right join film f on f.film_id = i.film_id;

--26

select i.inventory_id, i.film_id, f.title from inventory i 
right join film f on f.film_id = i.film_id
where i.inventory_id is null;

--27

select count(*) from inventory i
full join film f on f.film_id = i.film_id;

--28

select c.customer_id, min(r.rental_date) from customer c 
join rental r on r.customer_id = c.customer_id
group by c.customer_id;

--30

select f.title, c.name from film f
join film_category fc on fc.film_id = f.film_id
join category c on c.category_id = fc.category_id 
where char_length(c.name) > 8;

--31

select first_name, last_name from actor
where first_name = 'Christian';

--32

select * from payment
where amount > 8.00;

--33

select * from payment
where amount between 5 and 6;

--34

select * from payment p 
where amount < 1 or amount > 10
order by amount desc;

--35

select a.first_name, a.last_name, f.title from film f 
join film_actor fa using(film_id)
join actor a using(actor_id)
where f.replacement_cost > 25
order by f.title;

--36

select amount from payment
where payment_id in 
(
select payment_id from payment
order by amount desc
limit 10
)
order by amount asc;

--37

select c.first_name, c.last_name from customer c
where 
	exists (select 1 from payment p2
	where p2.customer_id = c.customer_id
	and amount = 0)
order by first_name;
	
--38

select c.first_name, c.last_name from customer c 
where c.customer_id in 
(
	select customer_id from payment p
	where amount = 0
)
order by first_name;

--39 

select c.first_name, c.last_name from customer c 
where customer_id = any 
(
	select customer_id from payment p 
	where amount = 0
)
order by first_name;

select * from rental
where rental_date between '2005-05-27' and '2005-05-29';

--41

select f.title from film f
join inventory i on f.film_id = i.film_id
join rental r on r.inventory_id = i.inventory_id
where r.rental_date  between '2005-05-27' and '2005-05-29';

--42

select s.first_name, avg(p.amount) from payment p 
join staff s on s.staff_id = p.staff_id
group by s.first_name;

--43

select count(amount) from payment p
where p.amount > (
	select avg(amount) from payment p2
	where p2.staff_id = p.staff_id
);


--44

select a.first_name, a.last_name from actor a
where a.first_name like 'E%';

--45

select first_name, last_name from actor
where first_name like '%E%';

--46

select f.title, a.first_name, a.last_name from film f 
join film_actor fa on fa.film_id = f.film_id 
join actor a on a.actor_id = fa.actor_id
where f.description like '%rocodile%'
order by f.title;

--47

select first_name, last_name from staff s 
where picture is null;

--48

select rental_id from rental r 
where return_date is null;

--49

select first_name, last_name from customer c 
where first_name = 'Kim' or last_name = 'Kim';

--50

select f.title from film f
join film_category fc on fc.film_id = f.film_id 
join category c on c.category_id = fc.category_id
where c."name" in ('Action', 'Drama');

--51

select avg(amount) from payment p;

--52

select max(amount) from payment;

--53

select min(amount) from payment;

--54

select c.first_name from customer c 
where c.first_name like 
(
select distinct a.first_name from actor a
where a.first_name = c.first_name
)
and c.customer_id like  
(
	select r.customer_id from rental r
	where r.customer_id = c.customer_id
);

--56

select f.rating, f.rental_rate, count(film_id) from film f 
group by rating, rental_rate
order by rating;

--57

select rating, rental_rate, count(film_id) from film f 
group by grouping sets 
(
(rating, rental_rate),
rating, rental_rate
)
order by rating;

--58

select rating, rental_rate, count(film_id) from film f 
group by cube (rating, rental_rate);

--59

select extract(year from rental_date) as year,extract(month from rental_date) as month, rental_date from rental r 
group by rental_date;

--60

select extract(year from rental_date) as year,extract(month from rental_date) as month, extract(day from rental_date) as day, sum(rental_id) 
from rental r
group by rollup (year, month, day);

--61

1) 126 262 179
2)  2 496 881

--62

select customer_id, sum(amount) from payment p 
group by customer_id;

--63

select f.title, sum(p.amount) from film f 
join inventory i using (film_id)
join rental r using (inventory_id)
join payment p using(rental_id)
group by f.title
order by sum desc;

--64

select a.first_name, a.last_name, sum(amount) from actor a 
join film_actor fa using(actor_id)
join film f using(film_id)
join inventory i using(film_id)
join store s using(store_id)
join staff s2 on s2.staff_id = s.manager_staff_id
join payment p using(staff_id)
group by a.first_name, a.last_name
order by sum desc;

--65

select amount, count(payment_id) from payment p 
group by amount;

--66

select staff_id, sum(amount) from payment p 
group by staff_id;

--67

select
	a.first_name, a.last_name, sum(amount), count (rental_id) from actor a 
	join film_actor fa using(actor_id)
	join film f using(film_id)
	join inventory i using(film_id)
	join store s using(store_id)
	join staff s2 on s2.staff_id = s.manager_staff_id
	join payment p using(staff_id)
group by
	a.first_name, a.last_name
order by
	sum desc;
	
--68

select
	c.first_name, c.last_name, ca.name, count(rental_id)
from
	customer c 
	join rental r using(customer_id)
	join inventory i using(inventory_id)
	join film f using(film_id)
	join film_category fc using(film_id)
	join category ca using(category_id)
	where c.first_name = 'Wade'
	group by c.first_name, c.last_name, ca.name
	order by count desc;
	
--69

	select 
		c.first_name, r.rental_date, count(rental_id) from customer c 
	join 
		rental r using(customer_id)
	join 
		inventory i using(inventory_id)
	join 
		film f using(film_id)
	join 
		film_category fc using(film_id)
	join 
		category ca using(category_id)
	where
		c.first_name = 'Wade'
	group by 
		c.first_name, r.rental_date
	having 
		r.rental_date between '2005-07-23' and '2005-08-23'
	order by 
		r.rental_date;
	
--71
	
select 
	c.first_name,
	sum(p.amount)
from
	customer c 
join
	payment p using(customer_id)
group by
	c.first_name
having
	sum(p.amount) > 180
order by
	sum;
	
--72

select 
	c.first_name, c.last_name
from
	customer c
where customer_id =
(select customer_id
from payment p 
where p.customer_id = c.customer_id  
group by customer_id
having sum(amount) > 200)

select 
	c.first_name, c.last_name, sum(p.amount)
from
	customer c 
join
	payment p ON p.customer_id = c.customer_id
group by 
	c.first_name, c.last_name 
having 
	sum(p.amount) > 200;

--73

select 
	f.title, count(a.actor_id)  
from
	actor a 
join
	film_actor fa using(actor_id)
join
	film f using(film_id)
group by
	f.title 
having 
	count(a.actor_id) > 5;

--74

select 
	a.first_name, a.last_name, count(f.film_id)
from
	actor a 
join
	film_actor fa using(actor_id)
join
	film f using(film_id)
group by
	a.first_name, a.last_name 
having 
	count(f.film_id) > 20;
	
DQL: Combining queries
1.

select
	first_name, last_name
from
	customer c 
where 
	c.customer_id = (
		select
			customer_id
		from
			payment p 
		where 
			p.customer_id = c.customer_id 
		group by
			customer_id 
		having 
			sum(amount) > 180
	)
	union 
	select 
		first_name, last_name 
	from
		customer c
	where
		customer_id = (
			select
				p.customer_id 
			from
				payment p
			where 
				p.customer_id = c.customer_id 
			group by
				customer_id
			having 
				sum(amount) < 300
		);
	
2.

select
	first_name, last_name
from
	customer c 
where 
	customer_id = (
		select 
			customer_id 
		from
			payment p 
		where 
			p.customer_id = c.customer_id 
		group by 
			customer_id 
		having 
			sum(amount) > 180
	)
intersect
select 
	first_name, last_name  
from
	customer c2 
where 
	customer_id = (
		select
			customer_id 
		from
			payment p2 
		where 
			p2.customer_id = c2.customer_id 
		group by 
			customer_id 
		having 
			sum(amount) < 190
	);

3.

select 
	first_name, last_name
from
	customer c 
where 
	customer_id = (
		select 
			customer_id 
		from
			payment p 
		where 
			p.customer_id = c.customer_id 
		group by 
			customer_id 
		having 
			sum(amount) > 180
	)
except 
select 
	first_name, last_name 
from
	customer c2 
where 
	customer_id = (
		select 
			customer_id 
		from
			payment p2 
		where 
			p2.customer_id = c2.customer_id 
		group by
			customer_id 
		having 
			sum(amount) < 190
	);
	
4.

with 
	big_doggos as (
		select 
			'Big Doggos' as type ,customer_id, sum(amount)
		from
			payment p 
		group by 
			customer_id
		having 
			sum(amount) > 120)
,
	smol_puppers as (
		select 
			'Smol Puppers' as type,customer_id, sum(amount) 
		from
			payment p2 
		group by
			customer_id 
		having 
			sum(amount) < 80)
,
	doggos as (
		select 
			'Doggos' as type, customer_id, sum(amount) 
		from
			payment p2 
		group by
			customer_id 
		having 
			sum(amount) > 79 and sum(amount) < 121)
select * from big_doggos
union
select * from doggos
union
select * from smol_puppers
order by sum
having ;

7.



