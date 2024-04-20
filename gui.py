import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "B!tCamp2024!",
    database = "testing"
)

mycursor = mydb.cursor()

xslot = str("")
yslot = str("")
graphType = str("")
window = tk.Tk()

def newPopup(message):
    popup = tk.Toplevel(window)
    popup.geometry("750x250")
    popup.title("Error")
    tk.Label(popup, text = message).place(x=150,y=80)

def getx_from_table(column: str):
    global xslot
    xslot = column

def gety_from_table(column: str):
    global yslot
    yslot = column

def choose_plot(type: str):
    global graphType
    graphType = type

def plotData():
    if(xslot == str("")) or (yslot == str("")) or (graphType == str("")):
        newPopup("Please selected data and graph first")
        return
    
    mycommand = "select " + xslot + ", " + yslot + " from test"

    mycursor.execute(mycommand)

    myresult = mycursor.fetchall()

    xcoords = []
    ycoords = []

    for row in myresult:
        xcoords.append(row[0])
        ycoords.append(row[1])
    x = np.array(xcoords)
    y = np.array(ycoords)

    if(graphType == "plot"):
        plt.plot(x, y)
    elif(graphType == "scatter"):
        plt.scatter(x,y)
    elif(graphType == "bar"):
        plt.bar(x,y)
    else:
        return
    plt.xlabel(xslot)
    plt.ylabel(yslot)
    plt.show()

    



window.title('window')

datax1 = tk.Button(window, text = 'x axis: x', width = 25, command = lambda: getx_from_table("x"))
datax1.pack()
datax2 = tk.Button(window, text = 'x axis: y', width = 25, command = lambda: getx_from_table("y"))
datax2.pack()
datax3 = tk.Button(window, text = 'x axis: z', width = 25, command = lambda: getx_from_table("z"))
datax3.pack()
datay1 = tk.Button(window, text = 'y axis: x', width = 25, command = lambda: gety_from_table("x"))
datay1.pack()
datay2 = tk.Button(window, text = 'y axis: y', width = 25, command = lambda: gety_from_table("y"))
datay2.pack()
datay3 = tk.Button(window, text = 'y axis: z', width = 25, command = lambda: gety_from_table("z"))
datay3.pack()
graphs1 = tk.Button(window, text = 'Scatterplot', width = 25, command = lambda: choose_plot("scatter"))
graphs1.pack()
graphs2 = tk.Button(window, text = 'Linechart', width = 25, command = lambda: choose_plot("plot"))
graphs2.pack()
graphs3 = tk.Button(window, text = 'Bargraph', width = 25, command = lambda: choose_plot("bar"))
graphs3.pack()
button5 = tk.Button(window, text = 'graph', width = 25, command = plotData)
button5.pack()

window.mainloop()