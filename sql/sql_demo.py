import sqlite3

conn = sqlite3.connect("example.db")
cur = conn.cursor()

print("Who is the highest-paid employee?")
cur.execute("SELECT first_name, last_name FROM employee WHERE salary = (SELECT MAX(salary) FROM employee);")
print(cur.fetchall())
print()

print("Show which projects the employees are working on, if any.")
cur.execute("""SELECT employee.first_name, employee.last_name, project.name
                FROM employee JOIN project ON project.team_code = employee.team_code;""")
print(cur.fetchall())
print()

print("Show all customers and their projects.")
cur.execute("""SELECT customer.repr_first_name, customer.repr_last_name, project.name
                FROM customer LEFT JOIN project ON project.customer_code = customer.customer_code;""")
print(cur.fetchall())
print()

print("What is the average salary in each of the teams?")
cur.execute("SELECT team_code, AVG(salary) FROM employee GROUP BY team_code;")
print(cur.fetchall())
print()

print("How big are the teams?")
cur.execute("SELECT team_code, COUNT(*) FROM employee GROUP BY team_code;")
print(cur.fetchall())
print()

conn.close()
