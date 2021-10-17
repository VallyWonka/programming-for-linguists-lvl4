import sqlite3

conn = sqlite3.connect("example.db")
cur = conn.cursor()

teams = [
    "1",
    "2"
]

employees = [
    ("1", "John", "Doe", "m", "20", "Junior", "300", "1"),
    ("2", "Jane", "Doe", "f", "35", "Senior", "1200", "1"),
    ("3", "Eliza", "Pancakes", "f", "45", "Junior", "200", "2"),
    ("4", "Bob", "Pancakes", "m", "45", "Middle", "300", "2"),
    ("5", "Bone", "Hilda", "f", "145", "Senior", "12000000", "2")
]

customers = [
    ("1", "Jesse", "McNamara", "heyhens@plumbella.com", "+008005553535", "UK"),
    ("2", "Kelly", "Sims", "kayla@sims.com", "+018005553535", "USA")
]

projects = [
    ("1", "Stanley Humphrey's Portfolio", "2500.12", "2", "2")
]

cur.executemany("INSERT INTO team VALUES(?);", teams)
cur.executemany("INSERT INTO employee VALUES(?, ?, ?, ?, ?, ?, ?, ?);", employees)
cur.executemany("INSERT INTO customer VALUES(?, ?, ?, ?, ?, ?);", customers)
cur.executemany("INSERT INTO project VALUES(?, ?, ?, ?, ?);", projects)
conn.commit()
conn.close()
