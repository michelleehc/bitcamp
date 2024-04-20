import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

mydb = mysql.connector.connect(
    host = "localhost",
    user =  "root",
    passwd = "B!tCamp2024!",
    database = "testing"
)

mycursor = mydb.cursor()








def get_x_y_plot():
    mycommand = "select x, y from test"
    mycursor.execute(mycommand)

    myresult = mycursor.fetchall()

    xcoords = []
    ycoords = []

    for row in myresult:
        xcoords.append(row[0])
        ycoords.append(row[1])
    x = np.array(xcoords)
    y = np.array(ycoords)

    plt.scatter(x, y)
    plt.show()
def get_y_z_plot():
    mycommand = "select y, z from test"
    mycursor.execute(mycommand)

    myresult = mycursor.fetchall()

    xcoords = []
    ycoords = []

    for row in myresult:
        xcoords.append(row[0])
        ycoords.append(row[1])
    x = np.array(xcoords)
    y = np.array(ycoords)

    plt.scatter(x, y)
    plt.show()
def get_x_y_line():
    mycommand = "select x, y from test"
    mycursor.execute(mycommand)

    myresult = mycursor.fetchall()

    xcoords = []
    ycoords = []

    for row in myresult:
        xcoords.append(row[0])
        ycoords.append(row[1])
    x = np.array(xcoords)
    y = np.array(ycoords)

    plt.plot(x, y)
    plt.show()

window = tk.Tk()

window.title('window')

button1 = tk.Button(window, text = 'Graph xy', width = 25, command = get_x_y_plot)
button1.pack()
button2 = tk.Button(window, text = 'Graph yz', width = 25, command = get_y_z_plot)
button2.pack()
button3 = tk.Button(window, text = 'Line xy', width = 25, command = get_x_y_line)
button3.pack()

window.mainloop()