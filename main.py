# main.py

import sympy
import time
from tkinter import *

root = Tk()
root.title("解决数学一元、二元方程")
root.geometry("500x300")

resultThing = StringVar()

def solveIt():
    result.delete('1.0', END)
    word = theX.get()
    mathExpression = theMath.get("1.0",END)
    try:
        x,y = sympy.symbols(word)
    except:
        x = sympy.symbols(word)
    try:
        mathResult = sympy.solve([eval(mathExpression)], [x, y])
    except:
        mathResult = sympy.solve([eval(mathExpression)], [x])
    print(mathResult)
    resultThing.set(str(mathResult).strip("{").strip("}"))
    time.sleep(0.5)
    result.insert('insert', resultThing.get())

wordTitle = Label(root, text="请在下方输入你的未知数(不同未知数用英文空格隔开，请使用x和y)", font=("微软雅黑", '10'))
theX = Entry(root, show=None)
mathTitle = Label(root, text="请在下方输入你的方程\n等号右边为零，只需输入左边部分，请善用括号\n\
多个方程用逗号隔开，按照编程表达式编写，系数与字母之间的乘号不可省略\n\
程序已知bug:可能会出现增根，结果仅供参考\n↓示例↓", font=("微软雅黑", '10'))
example = Label(root, text="x/(x+1)+1-(2*x+1)/x\nx+y-9, x-y-5", font=("微软雅黑", '10'), bg="green")
theMath = Text(root, width=50, height=3)
buttom = Button(root, text="解方程", width=12, height=1, command=solveIt)
result = Text(root, width=60, height=1)

wordTitle.pack()
theX.pack()
mathTitle.pack()
example.pack()
theMath.pack()
buttom.pack()
result.pack()

root.mainloop()
