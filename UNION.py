import sqlite3

connection = sqlite3.connect("residential_comple.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS department1 (
               id INTEGER NOT NULL,
               name TEXT NOT NULL,
               department INTEGER NOT NULL,
               position INTEGER NOT NULL,
               salary INTEGER NOT NULL
               )
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS 'department2' (
               id INTEGER NOT NULL,
               name TEXT NOT NULL,
               department INTEGER NOT NULL,
               position INTEGER NOT NULL,
               salary INTEGER NOT NULL
               )
''')

def create(table_name, id, name, department, position, salary):
    cursor.execute(f"INSERT INTO {table_name} (id, name, department, position, salary) VALUES (? ,?,?,?,?)", (id, name, department, position, salary))
    connection.commit()

create('department1', 1, ',',4564564,500,1000  )
create('department2', 2, ',,,,,,,,,',33333,333300,33000  )


values_tables = cursor.execute("SELECT name, position, salary FROM department1 WHERE salary > 50000 "
                     "UNION "
                     "SELECT name, position, salary FROM department2 WHERE salary <= 100000")
print(values_tables.fetchall())

connection.close()
