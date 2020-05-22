def correction(str):
    if str.find('&') != -1:
        str=str.replace('&','and')
        return str
    return str
def unique (lst_region):
    res=[]
    for str in lst_region:
        if str not in res:
            res.append(str)
    return res
def to_float(str):
    lst = str.split(",")
    if (len(lst) == 2):
        return lst[0]+"."+lst[1]
    if(str.rfind('')==0):
        return "null"
    return str
def null(str):
    if (str.rfind('') == 0):
        return "null"
    return str

import csv
import cx_Oracle

username = "SYSTEM"
password = "2805052001"
database = "T/xe"

try:
    connection = cx_Oracle.connect(username, password, database)
except cx_Oracle.DatabaseError as exception:
    print('Failed to connect to %s\n', database)
    print(exception)
    exit(1)
cursor = connection.cursor ()

lst_region=[]
lst_country=[]
lst_migration=[]
lst_gdp=[]
lst_type_country = []
lst_pop_destiny = []

with open('world.csv') as world:
    reader = csv.reader(world, delimiter=',')
    for row in reader:
        lst_region.append([correction(row[1])])
        lst_country.append((correction(row[0]),correction(row[1])))
        if (null(row[2])!= "null" and null(row[3])!= "null"):
            lst_pop_destiny.append((correction(row[0]),row[2],row[3]))
            print(row[2],row[3])
        if (to_float(row[6])!="null"):
            lst_migration.append((correction(row[0]), to_float(row[6])))
        if (null(row[8])!= "null"):
            lst_gdp.append((correction(row[0]), row[8]))
        if (to_float(row[17]) != "null" and to_float(row[18]) != "null" and to_float(row[19]) != "null"):
            lst_type_country.append((correction(row[0]),to_float(row[17]),to_float(row[18]),to_float(row[19])))


insert_query = '''insert into region (region) values (trim(:1))'''
cursor.prepare(insert_query)
cursor.executemany(None,unique(lst_region[1:]))
connection.commit()

insert_query = '''insert into country (country,region1) values (trim(:1),trim(:2))'''
cursor.prepare(insert_query)
cursor.executemany(None,lst_country[1:])
connection.commit()



insert_query = '''insert into pop_destiny (country_fk,population,area,add_date) values (trim(:1),:2,:3,TO_DATE('2020/05/2', 'yyyy/mm/dd'))'''
cursor.prepare(insert_query)
cursor.executemany(None,lst_pop_destiny[1:])
connection.commit()



insert_query = '''insert into net_migration (country_fk,net_migration,add_date) values (trim(:1),:2,TO_DATE('2020/05/2', 'yyyy/mm/dd'))'''
cursor.prepare(insert_query)
cursor.executemany(None,lst_migration[1:])
connection.commit()


insert_query = '''insert into gdp (country_fk,gdp,add_date) values (trim(:1),:2,TO_DATE('2020/05/2', 'yyyy/mm/dd'))'''
cursor.prepare(insert_query)
cursor.executemany(None,lst_gdp[1:])
connection.commit()


insert_query = '''insert into country_type (country_fk,agriculture,industry,services,add_date) values (trim(:1),:2,:3,:4,TO_DATE('2020/05/2', 'yyyy/mm/dd'))'''
cursor.prepare(insert_query)
print(lst_type_country[1:])
cursor.executemany(None,lst_type_country[1:])
connection.commit()


cursor.close()
connection.close()
