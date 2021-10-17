import sqlite3

conn = sqlite3.connect("example.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS team(
	team_code int PRIMARY KEY
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS employee(
	employee_code int PRIMARY KEY,
	first_name varchar(255) NOT NULL,
	last_name varchar(255) NOT NULL,
	gender char(1) NOT NULL,
	age int NOT NULL,
	position varchar(255) NOT NULL,
	salary numeric(12, 2) NOT NULL,
	team_code int REFERENCES team(team_code)
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS customer(
	customer_code int PRIMARY KEY,
	repr_first_name varchar(255) NOT NULL,
	repr_last_name varchar(255) NOT NULL,
	email varchar(255),
	phone_number varchar(15),
	country varchar(63)
);""")

cur.execute("""CREATE TABLE IF NOT EXISTS project(
	project_code int PRIMARY KEY,
	name varchar(255) NOT NULL,
	cost numeric(48, 2) NOT NULL,
	customer_code int REFERENCES customer(customer_code),
	team_code int REFERENCES team(team_code)
);""")

conn.commit()
conn.close()
