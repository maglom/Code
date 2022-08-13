import csv
import psycopg2

conn = psycopg2.connect(
    "dbname=postgres user=postgres password=mysecretpassword", port=5544)

cur = conn.cursor()


def create_table():
    cur.execute(
        "CREATE TABLE oscar_winners (id serial PRIMARY KEY, year integer, age integer, name varchar, movie varchar);")
    conn.commit()


def get_youngest_oscar_winner():
    cur.execute(
        'SELECT name, year, age, movie FROM oscar_winners ORDER BY age LIMIT 1;')
    return cur.fetchall()


def winners_by_age(age):
    cur.execute('SELECT * FROM oscar_winners WHERE age = %s;', [age])
    ls = []
    result = cur.fetchall()
    for i in result:
        ls.append(list(i))
    return ls


def winners_by_name(name):
    cur.execute('SELECT name FROM oscar_winners WHERE name like %s;', [name])
    ls = []
    result = cur.fetchall()
    for i in result:
        ls.append(i[0])
    return ls


def multiple_oscar_winners(num_oscars):
    cur.execute(
        'select name, count(id) from oscar_winners group by name having count(id) >= %s;', [num_oscars])
    dic = {}
    for i in cur.fetchall():
        dic[i[0]] = i[1]
    return dic


def write_oscar_winner(name, age, year, movie):
    cur.execute('insert into oscar_winners(name, age, year, movie) values(%s, %s, %s, %s)', [
                name, age, year, movie])
    conn.commit()


with open('ETL/oscar_age_female.csv', 'r') as file:
    reader = csv.reader(file)
    ls = []
    for c,list in enumerate(reader):
        if len(list) > 5:
            list[4] = list[4] + list[5]    
        lss = []
        for item in list:
            lss.append(item.strip().strip('"').strip('"'))
        ls.append(lss)

with open('ETL/oscar_age_female1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for i in ls:
        writer.writerow(i)

with open('ETL\oscar_age_female1.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        write_oscar_winner(row['Name'], row['Age'], row['Year'], row['Movie']) 


cur.close()
conn.close()
