from tkinter import *
expression=""
def press(num):       #this function is used for any key press in the calculator...
    global expression
    expression=expression+str(num)
    equation.set(expression)

def equalpress():     #this function is used for "=" 'Equals to" button in the calculator...
    try:
        
        global expression
        total=str(eval(expression))
        equation.set(total)

    except:
        
        equation.set("Syntax Error")   #if any wrong expression is given, this exception will be raised and "Syntax Error" message will be displayed...
        expression=""
def clear():    #this function is used for the "AC" button used in the calculator to clear the text box...
    global expression
    expression=""
    equation.set("")
    
def backspace(self):    #this function is used for the "DEL" button used in the calculator for a backspace...
    self.cancel()
    self.display(len(self.text_box.get())-1)



gui=Tk()
equation=StringVar()
gui.configure(background="grey")   #sets the background color to "grey"...
gui.title("Simple Calculator")     #sets a title to the display screen with name "Simple Calulator"...
expression_feild=Entry(gui,textvariable=equation,fg="white",bg="black",selectborderwidth=7,font=('sans-serif',25,'bold'))
expression_feild.grid(columnspan=4,ipadx=80,ipady=25)
equation.set("")

#the below statements for "numbers" buttons in the calculator...

button1=Button(gui,text="1",fg="black",bg="white",font=('sans-serif', 20, 'bold'),command=lambda:press(1),height=1,width=7)
button1.grid(row=3,column=0)
button2=Button(gui,text="2",fg="black",bg="white",font=('sans-serif', 20, 'bold'),command=lambda:press(2),height=1,width=7)
button2.grid(row=3,column=1)
button3=Button(gui,text="3",fg="black",bg="white",font=('sans-serif', 20, 'bold'),command=lambda:press(3),height=1,width=7)
button3.grid(row=3,column=2)
button4=Button(gui,text="4",fg="black",bg="white",font=('sans-serif', 20, 'bold'),command=lambda:press(4),height=1,width=7)
button4.grid(row=2,column=0)
button5=Button(gui,text="5",fg="black",bg="white",font=('sans-serif', 20, 'bold'),command=lambda:press(5),height=1,width=7)
button5.grid(row=2,column=1)
button6=Button(gui,text="6",fg="black",bg="white",font=('sans-serif', 20, 'bold'),command=lambda:press(6),height=1,width=7)
button6.grid(row=2,column=2)
button7=Button(gui,text="7",fg="black",bg="white",font=('sans-serif', 20, 'bold'),command=lambda:press(7),height=1,width=7)
button7.grid(row=1,column=0)
button8=Button(gui,text="8",fg="black",bg="white",font=('sans-serif', 20, 'bold'),command=lambda:press(8),height=1,width=7)
button8.grid(row=1,column=1)
button9=Button(gui,text="9",fg="black",bg="white",font=('sans-serif', 20, 'bold'),command=lambda:press(9),height=1,width=7)
button9.grid(row=1,column=2)
button0=Button(gui,text="0",fg="black",bg="white",font=('sans-serif', 20, 'bold'),command=lambda:press(0),height=1,width=7)
button0.grid(row=4,column=1)

#this statement is for "." decimal point button in the calculator...
decimal=Button(gui,text=".",fg="black",bg="light blue",font=('sans-serif', 20, 'bold'),command=lambda:press("."),height=1,width=7)
decimal.grid(row=5,column=2)


#this statement is for "+" plus operator button in the calculator...
plus=Button(gui,text="+",fg="black",bg="light blue",font=('sans-serif', 20, 'bold'),command=lambda:press("+"),height=1,width=7)
plus.grid(row=1,column=3)


#this statement is for "-" minus operator button in the calculator...
minus=Button(gui,text="-",fg="black",bg="light blue",font=('sans-serif', 20, 'bold'),command=lambda:press("-"),height=1,width=7)
minus.grid(row=2,column=3)


#this statement is for "X" multiply operator button in the calculator...
mul=Button(gui,text="x",fg="black",bg="light blue",font=('sans-serif', 20, 'bold'),command=lambda:press("*"),height=1,width=7)
mul.grid(row=3,column=3)


#this statement is for "/" division operator button in the calculator...
div=Button(gui,text="/",fg="black",bg="light blue",font=('sans-serif', 20, 'bold'),command=lambda:press("/"),height=1,width=7)
div.grid(row=4,column=3)


#this statement is for "=" 'equals to' operator button in the calculator, but this button was named as "CALCULATE"...
equal=Button(gui,text="CALCULATE",fg="green",bg="white",font=('sans-serif', 20, 'bold'),command=equalpress,height=1,width=7)
equal.grid(row=5,column=0,columnspan=2,ipadx=65)


#this statement is for "AC" CLEAR button in the calculator...
clear=Button(gui,text="AC",fg="black",bg="orange",font=('sans-serif', 20, 'bold'),command=clear,height=1,width=7)
clear.grid(row=4,column=0)


#this statement is for "DEL" BackSpace button in the calculator...
back=Button(gui,text="DEL",fg="orange",bg="white",font=('sans-serif', 20, 'bold'),command=backspace,height=1,width=7)
back.grid(row=4,column=2)


#this statement is for "%" Percentage operator button in the calculator...
percentage=Button(gui,text='%',fg="black",bg="light blue",font=('sans-serif', 20, 'bold'),command=lambda:press("%"),height=1,width=7)
percentage.grid(row=5,column=3)


gui.mainloop()
