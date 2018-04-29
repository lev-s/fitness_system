from tkinter import *

def sign_in():
    root = Tk()
    root.title('Log In')
    root.geometry('700x350+80+80')

    header = Frame(root, width = 500, height = 100, bg = 'sky blue', relief = SUNKEN)
    header.pack(side = TOP)

    instruction = Label(header, font =('arial', 20, 'bold'), text ='Please Sign In',
                        fg = 'Steel Blue', bd = 10, anchor = 'w')
    instruction.grid(row = 0, column =0)

    nameL = Label(root, font =('arial', 10, 'bold'), text = 'Username : ')
    pwordL = Label(root, font =('arial', 10, 'bold'), text = 'Password : ')
    nameL.grid(row = 1, column = 0)
    pwordL.grid(row = 2, column = 0)

    nameEL = Entry(root)
    pwordEL = Entry(root, show = '*')
    nameEL.grid(row = 1, column =1)
    pwordEL.grid(row =2, column =1)

    loginB = Button(root, text ='Sign In', fg='red', bd = 10)
    loginB.grid(columnspan = 1, sticky =E)

    root.mainloop()

sign_in()
