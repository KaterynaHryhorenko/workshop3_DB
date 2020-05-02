import cx_Oracle
import csv


username = "SYSTEM"
password = "2805052001"
database = "T/xe"

try:
    connection = cx_Oracle.connect(username, password, database)
except cx_Oracle.DatabaseError as exception:
    print('Failed to connect to %s\n', database)
    print(exception)
    exit(1)

cur = connection.cursor()

cur.execute('''
SELECT
    TRIM(region) AS region
FROM
    region
    ''')


with open( "region.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Region"])
    for row in cur:
        writer.writerow(row)

cur.execute('''
SELECT
    TRIM(country) AS country,
    TRIM(region1) AS region
FROM
    country
''')
with open( "country.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Country","Region"])
    for row in cur:
        writer.writerow(row)

cur.execute('''
SELECT
    TRIM(country_fk) AS country,
    gdp AS gdp,
    add_date
FROM
    gdp
''')
with open( "gdp.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Country","GDP","Add Date"])
    for row in cur:
        writer.writerow(row)

cur.execute('''
SELECT
    TRIM(country_fk),
    net_migration,
    add_date
FROM
    net_migration
''')
with open( "net_migration.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Country","Net Migration","Add Date"])
    for row in cur:
        writer.writerow(row)

cur.execute('''
SELECT
    TRIM(country_fk) AS country,
    agriculture,
    industry,
    services,
    add_date
FROM
    country_type
''')
with open( "country_type.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Country","Agriculture","Industry","Services","Add Date"])
    for row in cur:
        writer.writerow(row)

cur.execute('''
SELECT
    TRIM(country_fk),
    population,
    area,
    add_date
FROM
    pop_destiny
''')
with open( "pop_destiny.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Country","Population","Area","Add Date"])
    for row in cur:
        writer.writerow(row)
cur.close()


connection.close()
