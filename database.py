import mysql.connector

con = mysql.connector.connect(
    host='localhost' , user='root' , password='' , database='login_sistem'
)

cursor = con.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
        Id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
        Username TEXT NOT NULL,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL,
        Cpassword TEXT NOT NULL

               )""")

print('conexao ao banco de dados feita com sucesso.')
