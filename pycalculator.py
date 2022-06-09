from tkinter import *


class Calculator:

    def __init__(self,window):
        self.window = window
        window.title("PyCalculator")
        self.equation = Entry(window,width = 36, borderwidth = 5)
        self.equation.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
        self.botton()

    def addButton(self,value):
        return Button(self.window,text = value, width = 9, command = lambda:self.click(str(value)))


    def botton(self):
        b0 = self.addButton(0)
        b1 = self.addButton(1)
        b2 = self.addButton(2)
        b3 = self.addButton(3)
        b4 = self.addButton(4)
        b5 = self.addButton(5)
        b6 = self.addButton(6)
        b7 = self.addButton(7)
        b8 = self.addButton(8)
        b9 = self.addButton(9)
        b_add = self.addButton("+")
        b_sub = self.addButton("-")
        b_mul = self.addButton("*")
        b_div = self.addButton("/")
        b_eql = self.addButton("=")
        b_clc = self.addButton("Clear")

        row3 = [b7,b8,b9,b_add]
        row2 = [b4,b5,b6,b_sub]
        row1 = [b1,b2,b3,b_mul]
        row4 = [b_clc,b0,b_eql,b_div]

        r = 1
        for row in [row1,row2,row3,row4]:
            c = 0
            for buttn in row:
                buttn.grid(row = r, column = c, columnspan = 1)
                c += 1
            r += 1


    def click(self,value):

        get_equation = str(self.equation.get())

        if value == "Clear":
            self.equation.delete(-1,END)
        elif value == "=":
            ans = str(eval(get_equation))
            self.equation.delete(-1,END)
            self.equation.insert(0,ans)
        else:
            self.equation.delete(0,END)
            self.equation.insert(0,get_equation + value)



if __name__ == "__main__":

    root = Tk()

    gui = Calculator(root)
    root.mainloop()