import sqlite3
connection = sqlite3.connect('shows.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Movies
              (MovieName TEXT,Actor TEXT,Actress TEXT, Year INT,Director TEXT)''')
INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)
VALUES ('KRK', 'Vijay Sethupathi', 'Samantha', 2022,'Viki' );
INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)
VALUES ('Valimai', 'Ajith', 'Huma Qureshi', 2022,'Vinoth' );
INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)
VALUES ('Master', 'Vijay', 'Malvika Mohan', 2021,'Loki' );
INSERT INTO Movies (MovieName,Actor,Actress,Year,Director)
VALUES ('Don', 'SK', 'Priyanka Mohan', 2022,'Cibi Chakaravarthi' );
cursor.execute('''SELECT * from Movies''')
result = cursor.fetchone();
print(result)
connection.commit()
connection.close()
