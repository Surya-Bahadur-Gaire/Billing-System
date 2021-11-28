from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image,ImageTk  #pip library
import pymysql #pip install mysql in command prompt
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="Yellow")
        #Background image

        self.bg=ImageTk.PhotoImage(file="images/img4.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)


        #left image
        #self.left=ImageTk.PhotoImage(file="images/signup.png")
        #left=Label(self.root,image=self.left).place(x=80,y=100,relwidth=400,relheight=500)

        #register frame
        frame1=Frame(self.root,bg="orange")
        frame1.place(x=480,y=100,width=700,height=500)


        title=Label(frame1,text="REGISTRATION FORM",font=("times new roman",20,"bold"),bg="orange",fg="brown").place(x=50,y=30)

         #row1---------------------------------------------------------------------------------
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="white")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="white")
        self.txt_lname.place(x=370,y=130,width=250)
        #row2----------------------------------------------------------------------------------

        contact=Label(frame1,text="Contact Number",font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="white")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="white")
        self.txt_email.place(x=370,y=200,width=250)

        #row3----------------------------------------------------------------------------------

        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=50,y=240)
        self.cmb_question=ttk.Combobox(frame1,font=("times new roman",13,"bold"),state='readonly',justify=CENTER)
        self.cmb_question['values']=("Select the Question","Favourite Football Player","Favourite NBA Player","Your First Pet")
        self.cmb_question.place(x=50,y=270,width=250)
        self.cmb_question.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="white")
        self.txt_answer.place(x=370,y=270,width=250)

        #row4----------------------------------------------------------------------------------

        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="white")
        self.txt_password.place(x=50,y=350,width=250)

        confirmpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="orange",fg="white").place(x=370,y=310)
        self.txt_confirmpassword=Entry(frame1,font=("times new roman",15),bg="white")
        self.txt_confirmpassword.place(x=370,y=350,width=250)

        #checkbox for terms and condition
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms and Condition",variable=self.var_chk,onvalue=1,offvalue=0,font=("times new roman",12,"bold")).place(x=50,y=400)

        #register button
        btn_register=Button(frame1,text="REGISTER NOW",font=("times new roman",14,"bold"),bg="black",fg="white",command=self.register_data).place(x=50,y=440)
        #sign in button
        lblsign=Label(self.root,text="If you have account already",font=("times new roman",13,"bold"),fg="green").place(x=20,y=100)
        btn_signin=Button(self.root,text="SIGN IN",font=("times new roman",20,"bold"),bg="black",fg="white").place(x=30,y=440,width=200)
    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_question.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_confirmpassword.delete(0,END)
    #Database fetching
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_lname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_question.get()=="Select the Question" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_confirmpassword.get()=="":
            messagebox.showerror("ERROR FOUND","All Fields are required",parent=self.root)

        elif self.txt_password.get()!=self.txt_confirmpassword.get():
            messagebox.showerror("Match Not Found","Password and confirm password should be same",parent=self.root)

        elif self.var_chk.get=="0":

            messagebox.showerror("ERROR FOUND","Please Agree the Terms and Condition",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="Employees")
                cur=con.cursor()
                cur.execute("insert into registration (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                (self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_question.get(),
                                self.txt_answer.get(),
                                self.txt_password.get(),
                                
                                ))
                con.commit()
                con.close()  
                messagebox.showinfo("SUCESS","Data Registered Sucessfully",parent=self.root)
                self.clear()

            except Exception as es:
                    messagebox.showerror("ERROR FOUND",f"Error Due to: {str(es)}",parent=self.root)

            
              #self.txt_lname.get(),
              #self.txt_contact.get(),
              #self.txt_email.get(),
              #self.cmb_question.get(),
              #self.txt_answer.get(),
              #self.txt_password.get(),
              #self.txt_confirmpassword.get()
              


root=Tk()
obj = Register(root)

root.mainloop()