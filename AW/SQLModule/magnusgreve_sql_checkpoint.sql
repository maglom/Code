Theory

1.

The keywords in a sql query are executed in this order:
from where group by having select

You have to keep this in mind when writing the query.

2.

A primary key is a unique identifier. This can be one column or multiple columns. 
Usually the first column in a table is named x_id and is the primary key. 
in a junction table you have two id columns which together are the primary key.
The primary key can be 

3.

no it is not necessary. You can  do regular joins on other fields than FK/PK.

4.

A full join will you all the data from both the table and match where possible. no data is discarded. 
A inner join will only return the data which has a match between tables.

DDL

create table north (
	id serial primary key,
	row1 text,
	row2 text,
	row3 text,
);

create table northwest (
	sid serial,
	pid serial,
	data text,
	primary key (sid, pid)
);

create table measurements (
	nw serial,
	ne serial,
	se serial,
	sw serial,
	height int,
	weight int,
	primary key(nw, ne, se, sw)
);

create table northeast(
	id serial,
	data1 text,
	data2 text,
	data3 text,
	primary key(id)
);

create table southeast(
	id serial,
	data text,
	primary key(id)
);

create table southwest(
	id serial,
	data text,
	primary key(id)
);

alter table north add foreign key (id) references northwest(sid);

alter table northwest add unique (pid);

alter table measurements add foreign key (nw) references northwest(pid);

alter table measurements add foreign key (ne) references northeast(id);

alter table measurements add foreign key (se) references southeast(id);

alter table measurements add foreign key (sw) references southwest(id);

DQL

1.

select contacttypeid, name from person.contacttype c
where name like '%Manager%';

2.

select p.businessentityid, concat_ws(', ', p.firstname, p.middlename, p.lastname) as name from person.person p 
left join person.businessentitycontact b using(businessentityid)
left join person.contacttype c using(contacttypeid)
where c.name = 'Purchasing Manager'
order by name desc;

3.

select c.contacttypeid, c.name, count(*) from person.businessentitycontact b
left join person.contacttype c on c.contacttypeid = b.contacttypeid 
group by c.contacttypeid, c."name" 
having count(*) > 20;

4.

select productid from production.product p
where lower(name) like '%crankset%'

5. 

select addressid from person.address a 
where city = 'London'

6.

select count(*) from sales.salesorderheader s 
left join sales.salesorderdetail sa using(salesorderid)
where shiptoaddressid in (
	select addressid from person.address a 
	where city = 'London')
and sa.productid in (
	select productid from production.product p
	where lower(name) like '%crankset%'	
);

LVL 2 DVDrental

1.

select concat_ws(' ', a.first_name, a.last_name) as name, sum(p.amount) from actor a 
left join film_actor fa using(actor_id)
left join film f using(film_id)
left join inventory i using(film_id)
left join rental r using(inventory_id)
left join payment p using(rental_id)
where p.amount > 3 
group by name
having sum(p.amount) > 49;

2.

select * from (
	select customer_id, min(rental_date) as first_rental_date from rental
	group by customer_id) rental1
	left join lateral
	(
	select rental_date as next_rental_date from rental
	where customer_id = rental1.customer_id and rental_date > rental1.first_rental_date
	order by rental_date asc
	limit 1
	)rental2 on true;


LVL 2 Adventureworks

1.

select p.lastname, p.firstname, rate * 37,5 as current_weekly_salary, date(ratechangedate) from person.person p 
left join humanresources.employee e using(businessentityid)
left join humanresources.employeepayhistory e2 using(businessentityid)





