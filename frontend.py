import tkinter
import array
import info
import matplotlib.pyplot as plt
import numpy
import math

class ReturnValue:
    def __init__(self):

        self.root = tkinter.Tk()    
        self.root.geometry("500x500")

        # creates and places average labels and fields
        self.L1 = tkinter.Label(self.root, text="Admission Average")
        self.L1.grid(row=1, column=4)
        self.avg = tkinter.Entry(self.root, bd=3)
        self.avg.grid(row=1, column=5)


        # creates and places aif labels and fields
        self.L2 = tkinter.Label(self.root, text="Aif Score")
        self.L2.grid(row=2, column=4)
        self.aif = tkinter.Entry (self.root, bd = 3)
        self.aif.grid (row=2, column = 5)

        # creates and places interview labels and fields
        self.L3 = tkinter.Label(self.root, text="Interview Score")
        self.L3.grid(row=3, column=4)
        self.inter = tkinter.Entry (self.root, bd = 3)
        self.inter.grid (row=3, column = 5)

        # creates and places adjustment labels and fields
        self.L4 = tkinter.Label(self.root, text="Adjustment")
        self.L4.grid(row=4, column=4)
        self.adj = tkinter.Entry(self.root, bd=3)
        self.adj.grid(row=4, column=5)

        # creates and places the optionmenu's labels and fields
        self.L5 = tkinter.Label(self.root, text="Select your program")
        self.L5.grid(row=5, column=4)
        self.label = tkinter.StringVar()
        self.holder = info.programList()
        self.holder = self.holder[0]
        self.label.set(self.holder)
        self.menu = tkinter.OptionMenu(self.root, self.label, *info.programList())
        self.menu.grid(row=5, column=5)

        # creates submit button
        self.button = tkinter.Button(
            self.root, text="submit", command=self.returnValues
            )
        self.button.grid(row=6, column=5)


        # creates main window
        self.root.mainloop()

    #gets the values from the textboxes and optionmenu and returns them
    def returnValues(self):
        avg= float(self.avg.get())
        aif = float(self.aif.get())
        inter = float(self.inter.get())
        adj = float(self.adj.get())
        menu= self.label.get()
        self.score = str(avg + aif + inter-adj), menu



def score():
    score = ReturnValue().score
    return score


# creates the plot
def displayPlot (func, columnNum, cPoint, topPoint, bottomPoint, percentage, score):

    fig = plt.figure()
    ax = fig.add_subplot(111)
    numberOfEntries = info.nonZeroCount(columnNum)

    # the data
    x = numpy.arange(0,numberOfEntries)
    y = info.returnData(columnNum)

    # plots the data
    plt.plot (x,y, color = 'red')
  
    # plots the function
    plt.plot(x, func(x), color = 'green')

    # fills the area under the function 
    plt.fill_between (x, func(x), alpha = 0.2)

    # draws the line from the top of the curve to the bottom
    xValues = [cPoint, cPoint]
    yValues = [0, func(cPoint)]
    plt.plot (xValues, yValues)

    # the percentage is [0,100]
    if (score<bottomPoint):
        percentage = 0
    elif (topPoint<score):
        percentage = 100

    # creates and formats the message 
    holder = "you are above " + str(round(percentage,1)) + "%"+ " of applicants" 
    ax.text(0.95, 0.95, holder,
        verticalalignment='top', horizontalalignment='right',
        transform=ax.transAxes,
        color='green', fontsize=10)

    # plots the percentage message 
    plt.axis([0, numberOfEntries, bottomPoint * 0.9, topPoint * 1.1])

    # displays the plot
    plt.show()