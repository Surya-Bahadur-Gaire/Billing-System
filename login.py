from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image

w=Tk()
w.geometry("350x500")
w.title("LOGIN FORM")
w.resizable(0,0)

j=0
r=0
for i in range(100):
    c=str(222222+r)
    Frame(w,width=20,height=500,bg="#650522"+c).place(x=j,y=0)
    j=j+10
    r=r+1

Frame(w,width=250,height=400,bg="#e72d0c").place(x=50,y=50)

lbl_head=Label(w,text="Enter Valid Username and Password",bg="#e72d0c",fg="#3af60f",font=("Times new roman",11,"italic"))
lbl_head.place(x=60,y=170)

#labeling
lbl_username=Label(w,text="Username:",bg="#e72d0c",fg="white",font=("Times new roman",14,"bold"))
lbl_username.place(x=80,y=200)

username_entry=Entry(w,width=20,bd=3,font=("Times new roman",14))
username_entry.place(x=80,y=230)

lbl_password=Label(w,text="Password:",bg="#e72d0c",fg="white",font=("Times new roman",14,"bold"))
lbl_password.place(x=80,y=260)

password_entry=Entry(w,width=20,bd=3,font=("Times new roman",14))
password_entry.place(x=80,y=290)


#image
image1=Image.open("images/user2.png")
image2=ImageTk.PhotoImage(image1)
lbl_image=Label(image=image2,border=0,justify=CENTER,width=150,height=120,bg="#e72d0c")
lbl_image.place(x=100,y=50)


#command
def loginfunc():
    if username_entry.get()=="admin" and password_entry.get()=="admin123":
        messagebox.showinfo("LOGIN SUCESSFULL","       WELCOME TO SYSTEM        ")
        q=Tk()
        q.mainloop()
    else:
        messagebox.showerror("ACCESS DENIED","     WRONG USERNAME OR PASSWORD   ")


#def forget():

#login button
btn_login=Button(w,text="LOGIN",width=25,bd=3,bg="green",fg="white",command=loginfunc,font=("times new roman",12,"bold"))
btn_login.place(x=60,y=330)
#forget password button
btn_forget=Button(w,text="Forget Password?",width=25,borderwidth=0,bg="#e72d0c",fg="white",font=("times new roman",12,"bold"),activebackground="#e72d0c")
btn_forget.place(x=60,y=365)
#register button
btn_forget=Button(w,text="Register New User",width=25,borderwidth=0,bg="#e72d0c",fg="white",font=("times new roman",12,"bold"),activebackground="#e72d0c")
btn_forget.place(x=60,y=400)









w.mainloop()



    