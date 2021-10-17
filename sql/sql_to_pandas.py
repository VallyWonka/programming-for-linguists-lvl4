import pandas as pd
import numpy as np

teams = {"team_code": [1, 2]}

employees = {
    "employee_code": [1, 2, 3, 4, 5],
    "first_name": ["John", "Jane", "Eliza", "Bob", "Bone"],
    "last_name": ["Doe", "Doe", "Pancakes", "Pancakes", "Hilda"],
    "gender": ["m", "f", "f", "m", "f"],
    "age": [20, 35, 45, 45, 145],
    "position": ["Junior", "Senior", "Junior", "Middle", "Senior"],
    "salary": [300, 1200, 200, 300, 12000000],
    "team_code": [1, 1, 2, 2, 2]
}

customers = {
    "customer_code": [1, 2],
    "repr_first_name": ["Jesse", "Kelly"],
    "repr_last_name": ["McNamara", "Sims"],
    "email": ["heyhens@plumbella.com", "kayla@sims.com"],
    "phone_number": ["+008005553535", "+018005553535"],
    "country": ["UK", "USA"]
}

projects = {
    "project_code": [1],
    "name": ["Stanley Humphrey's Portfolio"],
    "cost": [2500.12],
    "customer_code": [2],
    "team_code": [2]
}

team = pd.DataFrame(teams)
employee = pd.DataFrame(employees)
customer = pd.DataFrame(customers)
project = pd.DataFrame(projects)

print("Who is the highest-paid employee?")
print(employee[["first_name", "last_name"]][employee["salary"] == employee["salary"].max()])
print()

print("Show which projects the employees are working on, if any.")
print(pd.merge(employee[["first_name", "last_name", "team_code"]], project[["name", "team_code"]],
               on="team_code"))
print()

print("Show all customers and their projects.")
print(pd.merge(customer[["repr_first_name", "repr_last_name", "customer_code"]], project[["name", "customer_code"]],
               on="customer_code",
               how="left"))
print()

print("What is the average salary in each of the teams?")
print(employee.groupby("team_code").agg({"salary": np.mean}))
print()

print("How big are the teams?")
print(employee.groupby("team_code").size())
print()
