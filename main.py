import math as math
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Calculator")

def btnPress(numvar):
    global equation
    equation = equation + str(numvar)
    inputText.set(equation)

def btnClear():
    global equation
    equation = ""
    inputText.set("")

def btnEqual():
    global equation
    result = str(eval(equation))
    inputText.set(result)
    equation = ""

equation = ""

inputText = StringVar()


entryfield = Entry(root, font = ('arial', 40, 'bold'), textvariable = inputText, width = 18, justify = LEFT)
entryfield.grid(row = 0, column = 0)
entryfield.config(font=("Courier", 12))
keyframe = tk.Frame(root)
keyframe.grid(row = 1, column = 0)
btn1 = tk.Button(keyframe, text="1", width=4, height=2, command = lambda: btnPress(1))
btn1.grid(row = 4, column = 0)
btn2 = tk.Button(keyframe, text="2", width=4, height=2, command = lambda: btnPress(2))
btn2.grid(row = 4, column = 1)
btn3 = tk.Button(keyframe, text="3", width=4, height=2, command = lambda: btnPress(3))
btn3.grid(row = 4, column = 2)
btn4 = tk.Button(keyframe, text="4", width=4, height=2, command = lambda: btnPress(4))
btn4.grid(row = 3, column = 0)
btn5 = tk.Button(keyframe, text="5", width=4, height=2, command = lambda: btnPress(5))
btn5.grid(row = 3, column = 1)
btn6 = tk.Button(keyframe, text="6", width=4, height=2, command = lambda: btnPress(6))
btn6.grid(row = 3, column = 2)
btn7 = tk.Button(keyframe, text="7", width=4, height=2, command = lambda: btnPress(7))
btn7.grid(row = 2, column = 0)
btn8 = tk.Button(keyframe, text="8", width=4, height=2, command = lambda: btnPress(8))
btn8.grid(row = 2, column = 1)
btn9 = tk.Button(keyframe, text="9", width=4, height=2, command = lambda: btnPress(9))
btn9.grid(row = 2, column = 2)
btn0 = tk.Button(keyframe, text="0", width=4, height=2, command = lambda: btnPress(0))
btn0.grid(row = 5, column = 0)
btn00 = tk.Button(keyframe, text="00", width=4, height=2, command = lambda: btnPress(00))
btn00.grid(row = 5, column = 1)
btnperiod = tk.Button(keyframe, text=".", width=4, height=2, command = lambda: btnPress("."))
btnperiod.grid(row = 5, column = 2)
btndiv = tk.Button(keyframe, text="/", width=4, height=2, command = lambda: btnPress("/"))
btndiv.grid(row = 2, column = 3)
btnmulti = tk.Button(keyframe, text="*", width=4, height=2, command = lambda: btnPress("*"))
btnmulti.grid(row = 3, column = 3)
btnminus = tk.Button(keyframe, text="-", width=4, height=2, command = lambda: btnPress("-"))
btnminus.grid(row = 4, column = 3)
btnplus = tk.Button(keyframe, text="+", width=4, height=2, command = lambda: btnPress("+"))
btnplus.grid(row = 5, column = 3)
btncalc = tk.Button(keyframe, text="=", width=4, height=2, command = lambda: btnEqual())
btncalc.grid(row = 5, column = 5)
btnsqrt = tk.Button(keyframe, text="sqrt", width=4, height=2, command = lambda: btnPress("math.sqrt("))
btnsqrt.grid(row = 4, column = 5)
btnperc = tk.Button(keyframe, text="%", width=4, height=2, command = lambda: btnPress("100/"))
btnperc.grid(row = 3, column = 5)
btnclear = tk.Button(keyframe, text="Clear", width=4, height=2, command = lambda: btnClear())
btnclear.grid(row = 2, column = 5)
root.mainloop()
