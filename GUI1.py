from tkinter import *
window = Tk()
window.title('Password storeroom')
window.geometry('700x500')
headlinelbl = Label(window, text='ENTER INFORMATION TO STORE IT', fg='pink', bg='purple', font=('bold', 20))
headlinelbl.place(x=50, y=20)
usernamelbl = Label(window, text='Username', fg='black', font=(30))
usernamelbl.place(x=50, y=100)
passwordlbl = Label(window, text='Password', fg='black', font=(30))
passwordlbl.place(x=50, y=150)
password2lbl = Label(window, text='Confirm Password', fg='black', font=(30))
password2lbl.place(x=50, y=200)
emaillbl = Label(window, text='E-Mail', fg='black', font=(30))
emaillbl.place(x=50, y=250)
usernamefld = Entry(window, text='enter username here', bd=2)
usernamefld.place(x=300, y=100)
passwordfld = Entry(window, text='enter password here', bd=2)
passwordfld.place(x=300, y=150)
password2fld = Entry(window, text='enter password again', bd=2)
password2fld.place(x=300, y=200)
emailfld = Entry(window, text='enter e-mail here', bd=2)
emailfld.place(x=300, y=250)
savebtn=Button(window, text='   SAVE    ', fg='white', bg='blue', font=('bold', 10))
savebtn.place(x=370, y=320)
window.mainloop()
