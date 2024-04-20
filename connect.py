import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "B!tCamp2024!",
    database = "testing"
)

mycursor = mydb.cursor()

mycursor.execute("drop table if exists test")

mydb.commit

mycursor.execute("create table test (name VARCHAR(255), x int, y int, z int)")

sqlFormula = "insert into test (x, y, z, name) values (%s, %s, %s, %s)"

i = 0

while i < 100:
    a = "test" + str(i)
    datapoint = (i, 100 - i + 9 * i%10, 2*i + 3, a)
    mycursor.execute(sqlFormula, datapoint)
    i+= 1
mydb.commit()



mycursor.execute("select name, x, y from test")

myresult = mycursor.fetchall()

xcoords = []
ycoords = []

for row in myresult:
    xcoords.append(row[1])
    ycoords.append(row[2])
x = np.array(xcoords)
y = np.array(ycoords)

plt.scatter(x, y)
plt.show()

