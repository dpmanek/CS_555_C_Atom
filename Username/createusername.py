from tkinter import *
from functools import partial


def login(username):
	print("Nickname entered :", username.get())
	return


#window
Window = Tk()  
Window.geometry('500x200')
Window.title('Game Login')
bg = PhotoImage(file='Background.png')


#applying background image
bglabel = Label(Window, image=bg)
bglabel.place(x=0, y=0)


#username entry
usernameLabel = Label(Window, text="Enter Your Nickname: ")
usernameLabel.place(relx=0.3, rely=0.4, anchor='center')
username = StringVar()
usernameEntry = Entry(Window, textvariable=username)
usernameEntry.place(relx=0.6, rely=0.4, anchor='center')


login = partial(login, username)


#login
login = Button(Window, text="Enter", command=login)
login.place(relx=0.5, rely=0.6, anchor='center')  


Window.mainloop()