import mysql.connector


myconn = mysql.connector.connect(
    host="localhost" ,
    user = "root" ,
    passwd = "toor" , 
    database='mydatabase'
)

mycursor = myconn.cursor()

mycursor.execute(" SELECT * FROM movies WHERE name='vikins' ")

result = mycursor.fetchone()

print(result)





