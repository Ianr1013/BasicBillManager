from tkinter import *

root = Tk()
root.geometry("1000x500")
root.title("Bill Management")
root.resizable(False,False)

def Reset():
    entry_shawarma.delete(0,END)
    entry_lemontea.delete(0,END)
    entry_DBC.delete(0,END)
    entry_coffee.delete(0,END)
    entry_burger.delete(0,END)
    entry_biryani.delete(0,END)
    entry_brownie.delete(0,END)


def Total():
    try: a1 = int(Shawarma.get())
    except: a1 = 0

    try:a2 = int(Burger.get())
    except: a2 = 0

    try:a3 = int(Lemon_tea.get())
    except: a3 = 0

    try:a4 = int(Brownie.get())
    except: a4 = 0

    try: a5 = int(Biryani.get())
    except: a5 = 0

    try: a6 = int(DBC.get())
    except: a6 = 0

    try: a7 = int(Coffee.get())
    except:a7 = 0

    #define the costs of each item per quantity
    c1 = 120*a1
    c2 = 140*a2
    c3 = 15*a3
    c4 = 90*a4
    c5 = 170*a5
    c6 = 150*a6
    c7 = 20*a7

    lbl_total = Label(f2,font=('aria',20,'bold'),text="Total",width=16,fg="lightyellow",bg="black")
    lbl_total.place(x=0,y=50)

    entry_total = Entry(f2,font=('aria',20,'bold'),textvariable=Total_bill,bd=6,width=15,bg="lightgreen")
    entry_total.place(x=20,y=100)

    totalcost = c1+c2+c3+c4+c5+c6+c7
    string_bill = f"Rs.{totalcost}"
    Total_bill.set(string_bill)


Label(text="Bill Management",bg="black",fg="white",font=("Helvetica",33),width="300",height="2").pack()

#menu card
f = Frame(root,bg="lightgreen",highlightbackground="black",highlightthickness=1,width=300,height=370)
f.place(x=10,y=118)
Label(f,text="Menu",font=("Futura",40,"bold"),fg="black",bg="lightgreen").place(x=80,y=0)

Label(f,font=("Lucida Calligraphy",15,'bold'),text="Shawarma.......Rs.120/plate",fg="black",bg="lightgreen").place(x=10,y=80)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Burger.......Rs.140/plate",fg="black",bg="lightgreen").place(x=10,y=110)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Lemon Tea.......Rs.15/cup",fg="black",bg="lightgreen").place(x=10,y=140)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Brownie.......Rs.90/plate",fg="black",bg="lightgreen").place(x=10,y=170)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Biryani.......Rs.170/plate",fg="black",bg="lightgreen").place(x=10,y=200)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="DBC.......Rs.150/plate",fg="black",bg="lightgreen").place(x=10,y=230)
Label(f,font=("Lucida Calligraphy",15,'bold'),text="Coffee.......Rs.20/cup",fg="black",bg="lightgreen").place(x=10,y=260)

#BILL
f2 = Frame(root,bg="lightyellow",highlightbackground="black",highlightthickness=1,width=300,height=370)
f2.place(x=690,y=118)

Bill = Label(f2,text="Bill",font=('calibri',20),bg="lightyellow")
Bill.place(x=120,y=10)


#ENTRIES
f1 = Frame(root,bd=5,height=370,width=300,relief=RAISED)
f1.pack()
Shawarma = StringVar()
Burger = StringVar()
Lemon_tea = StringVar()
Brownie = StringVar()
Biryani = StringVar()
DBC = StringVar()
Coffee = StringVar()
Total_bill = StringVar()

#LABEL

lbl_shawarma = Label(f1,font=("aria",20,'bold'),text="Shawarma",width=12,fg="black")
lbl_burger = Label(f1,font=("aria",20,'bold'),text="Burger",width=12,fg="black")
lbl_Lemon_Tea = Label(f1,font=("aria",20,'bold'),text="Lemon Tea",width=12,fg="black")
lbl_Brownie = Label(f1,font=("aria",20,'bold'),text="Brownie",width=12,fg="black")
lbl_Biryani = Label(f1,font=("aria",20,'bold'),text="Biryani",width=12,fg="black")
lbl_DBC = Label(f1,font=("aria",20,'bold'),text="DBC",width=12,fg="black")
lbl_Coffee = Label(f1,font=("aria",20,'bold'),text="Coffee",width=12,fg="black")

lbl_shawarma.grid(row=1,column=0)
lbl_burger.grid(row=2,column=0)
lbl_Lemon_Tea.grid(row=3,column=0)
lbl_Brownie.grid(row=4,column=0)
lbl_Biryani.grid(row=5,column=0)
lbl_DBC.grid(row=6,column=0)
lbl_Coffee.grid(row=7,column=0)


#entry
entry_shawarma = Entry(f1,font=("aria",20,'bold'),textvariable=Shawarma,bd=6,width=8,bg="lightblue")
entry_burger = Entry(f1,font=("aria",20,'bold'),textvariable=Burger,bd=6,width=8,bg="lightblue")
entry_lemontea = Entry(f1,font=("aria",20,'bold'),textvariable=Lemon_tea,bd=6,width=8,bg="lightblue")
entry_brownie = Entry(f1,font=("aria",20,'bold'),textvariable=Brownie,bd=6,width=8,bg="lightblue")
entry_biryani = Entry(f1,font=("aria",20,'bold'),textvariable=Biryani,bd=6,width=8,bg="lightblue")
entry_DBC = Entry(f1,font=("aria",20,'bold'),textvariable=DBC,bd=6,width=8,bg="lightblue")
entry_coffee = Entry(f1,font=("aria",20,'bold'),textvariable=Coffee,bd=6,width=8,bg="lightblue")

entry_shawarma.grid(row=1,column=1)
entry_burger.grid(row=2,column=1)
entry_lemontea.grid(row=3,column=1)
entry_brownie.grid(row=4,column=1)
entry_biryani.grid(row=5,column=1)
entry_DBC.grid(row=6,column=1)
entry_coffee.grid(row=7,column=1)

#buttons

btn_reset = Button(f1,bd=5,fg="black",bg="lightpink",font=("ariel",16,'bold'),width=10,text="Reset",command=Reset)
btn_reset.grid(row=8,column=0)

btn_total = Button(f1,bd=5,fg="black",bg="lightpink",font=("ariel",16,'bold'),width=10,text="Total",command=Total)
btn_total.grid(row=8,column=1)




root.mainloop()