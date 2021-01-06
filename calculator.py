from tkinter import *
root = Tk()
# root.geometry("400x500")
root.title("Chirantan GUI Calculator")
en = Entry(root,width = 40,relief = SUNKEN)
en.grid(columnspan = 3,column = 0 , row = 0) # By default row and column are zero but it will be easy to track things.
def calc(number):
    calcnum = en.get()
    en.delete(0,END)
    en.insert(0,str(calcnum) + str(number))

def clear():
    en.delete(0,END)

def calcplus ():
    num = en.get()
    global firstnum
    global func
    func = "Add"
    firstnum = int(num)
    en.delete(0,END)
def calcsub():
    num = en.get()
    global firstnum
    global func
    func = "Sub"
    firstnum = int(num)
    en.delete(0,END)
def calcmul():
    num = en.get()
    global firstnum
    global func
    func = "Mul"
    firstnum = int(num)
    en.delete(0, END)
def calcdiv():
    num = en.get()
    global firstnum
    global func
    func = "Div"
    firstnum = int(num)
    en.delete(0, END)
def equal ():
    num2 = en.get()
    secondnum = int(num2)
    en.delete(0, END)
    if func == "Add" : 
        en.insert(0,firstnum + secondnum) 
    if func == "Sub" :
        en.insert(0,firstnum - secondnum)   
    if func == "Mul" :
        en.insert(0, firstnum * secondnum)
    if func == "Div" : 
        en.insert(0, firstnum / secondnum)

b7 = Button(root,text="7",padx=20,pady=18,bg = "#ff8989",relief = RAISED,font = "comicsans 11 bold",command = lambda : calc(7))
b8 = Button(root,text="8",padx=20,pady=18,bg = "#ff8989",relief = RAISED,font = "comicsans 11 bold",command = lambda : calc(8))
b9 = Button(root,text="9",padx=20,pady=18,bg = "#ff8989",relief = RAISED,font = "comicsans 11 bold",command = lambda : calc(9))
b7.grid(row = 1 ,column = 0)
b8.grid(row = 1,column = 1)
b9.grid(row=1, column=2)

b4 = Button(root, text="4",padx=20,pady=18,bg = "#ffb154",relief = RAISED,font = "comicsans 11 bold", command = lambda : calc(4))
b5 = Button(root, text="5",padx=20,pady=18,bg = "#ffb154",relief = RAISED,font = "comicsans 11 bold", command = lambda : calc(5))
b6 = Button(root, text="6",padx=20,pady=18,bg = "#ffb154",relief = RAISED,font = "comicsans 11 bold", command = lambda : calc(6))
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b1 = Button(root, text="1",padx=20, pady=18,bg = "#5dc7c7",relief = RAISED,font = "comicsans 11 bold",command = lambda : calc(1))
b2 = Button(root, text="2",padx=20, pady=18,bg = "#5dc7c7",relief = RAISED,font = "comicsans 11 bold",command = lambda : calc(2))
b3 = Button(root, text="3",padx=20, pady=18,bg = "#5dc7c7",relief = RAISED,font = "comicsans 11 bold",command = lambda : calc(3))
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)
b3.grid(row=3, column=2)

b0 = Button(root,text = "0",padx = 35,pady = 20,bg = "#35d4a0",relief = RAISED,font = "comicsans 11 bold",command = lambda : calc(0))
b0.grid(row=4, column=1)

bplus = Button(root, text="+", padx=35, pady=20, bg="#35d4a0",relief = RAISED,font = "comicsans 11 bold",command=calcplus)
bplus.grid(row=4, column=0)

bsub = Button(root,text = "-",padx = 35,pady = 20,bg = "#35d4a0",relief = RAISED,font = "comicsans 11 bold",command = calcsub)
bsub.grid(row = 5,column = 0)

bmul = Button(root,text = "x",padx = 35,pady = 20,bg = "#35d4a0",relief = RAISED,font = "comicsans 11 bold",command = calcmul)
bmul.grid(row = 5,column = 1)

bdiv = Button(root,text = "/",padx = 35,pady = 20,bg = "#35d4a0",relief = RAISED,font = "comicsans 11 bold",command = calcdiv)
bdiv.grid(row = 5,column = 2)

bclear = Button(root, text="C", padx=55, pady=20, bg="#ac84d8", relief = RAISED,font = "comicsans 11 bold",command=clear)
bclear.grid(row = 6,column = 1,columnspan = 3)

bequal = Button(root,text = "=",padx = 35,pady = 20,bg = "#35d4a0",relief = RAISED,font = "comicsans 11 bold",command = equal)
bequal.grid(row=4, column=2)


root.mainloop()

