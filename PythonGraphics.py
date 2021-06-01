from tkinter import *
from math import *
def solve():
    if(a.get()!=""and b.get()!="" and c.get()!=""):
        a_=int(a.get()) #float()
        b_=int(b.get())
        c_=int(c.get())
        D=b_*b_-4*a_*c_
        if D>0:
            x1_=round((-1*b_+sqrt(D))/(2*a_),2)
            x2_=round((-1*b_-sqrt(D))/(2*a_),2)
            t=f"X1={x1_}, \nX2={x2_}"
        elif D==0:
            x1_round((-1*b_)/(2*a_),2)
            t=f"X1={x1_}"
        else:
            t="Корней нет"
        answr.configure(text=f"D={D}\n{t}")
        a.configure(bg="lightblue")
        b.configure(bg="lightblue")
        c.configure(bg="lightblue")
    else:
        if a.get()=="":
            a.configure(bg="red")
        if b.get()=="":
            b.configure(bg="red")
        if c.get()=="":
            c.configure(bg="red")

aken=Tk()
aken.title("Квадратные уравнения")
aken.iconbitmap('Calculator.ico')
aken.geometry('600x200')

lbl=Label(aken,text="Решение квадратного уравнения",font="Calibri 26",fg="green",bg="lightblue")
lbl.pack()

answr=Label(aken,text="Решение",height=4,width=60,bg="yellow")
answr.pack(side=BOTTOM)

a=Entry(aken,font="Calibri 26",fg="green",bg="lightblue", width=3)
a.pack(side=LEFT)#,padx=10,pady=10
x2=Label(aken,text="x**2+",font="Calibri 26",fg="green",padx=10)
x2.pack(side=LEFT)
b=Entry(aken,font="Calibri 26",fg="green",bg="lightblue", width=3)
b.pack(side=LEFT)
x=Label(aken,text="x+",font="Calibri 26",fg="green")
x.pack(side=LEFT)
c=Entry(aken,font="Calibri 26",fg="green",bg="lightblue", width=3)
c.pack(side=LEFT)
y=Label(aken,text="=0",font="Calibri 26",fg="green")
y.pack(side=LEFT)

btn=Button(aken,text="Решить",bg="green",font="Calibri 26",command=solve)
btn.pack(side=LEFT) # grid(), place()
#btn.bind("<Button-1>",solve)   =command=solve
aken.mainloop()
