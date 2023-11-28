from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(height=770, width=550, bg='#d3f3f5')
window.title("Contact Book")
# window.resizable(width=False, height=False)
contact_list = []
Name = StringVar()
Number = StringVar()
frame = Frame(window)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20,
                 borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def Selected():
    print("hello", len(select.curselection()))
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


def AddContact():
    if Name.get() != "" and Number.get() != "":
        contact_list.append([Name.get(), Number.get()])
        print(contact_list)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")

    else:
        messagebox.showerror("Error", "Please fill the information")


def EntryReset():
    Name.set('')
    Number.set('')


def UpdateDetail():
    if Name.get() and Number.get():
        contact_list[Selected()] = [Name.get(), Number.get()]

        messagebox.showinfo("Confirmation", "Successfully Update Contact")
        EntryReset()
        Select_set()

    elif not (Name.get()) and not (Number.get()) and not (len(select.curselection()) == 0):
        messagebox.showerror("Error", "Please fill the information")

    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and \n press Load button")
        else:
            message1 = """To Load the all information of \n
                          selected row press Load button\n.
                        """
            messagebox.showerror("Error", message1)


def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'You Want to Delete Contact\n Which you selected')
        if result == True:
            del contact_list[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')


def VIEW():
    NAME, PHONE = contact_list[Selected()]
    Name.set(NAME)
    Number.set(PHONE)


def Select_set():
    contact_list.sort()
    select.delete(0, END)
    for name, phone in contact_list:
        select.insert(END, name)


Select_set()

Label(window, text='Name', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=20)
Entry(window, textvariable=Name, width=30).place(x=200, y=30)
Label(window, text='Contact No.', font=("Times new roman", 20, "bold"), bg='SlateGray3').place(x=30, y=70)
Entry(window, textvariable=Number, width=30).place(x=200, y=80)

Button(window, text=" ADD", font='Helvetica 18 bold', bg='#e8c1c7', command=AddContact, padx=20).place(x=50, y=140)
Button(window, text="UPDATE", font='Helvetica 18 bold', bg='#e8c1c7', command=UpdateDetail, padx=20).place(x=50, y=200)
Button(window, text="DELETE", font='Helvetica 18 bold', bg='#e8c1c7', command=Delete_Entry, padx=20).place(x=50, y=260)
Button(window, text="SEARCH", font='Helvetica 18 bold', bg='#e8c1c7', command=VIEW).place(x=50, y=325)
Button(window, text="RESET", font='Helvetica 18 bold', bg='#e8c1c7', command=EntryReset).place(x=50, y=390)
# Button(window, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=EXIT).place(x=250, y=470)

window.mainloop()
