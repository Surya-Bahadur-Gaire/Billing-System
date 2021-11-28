from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random,os
from tkinter import messagebox
import tempfile



class BillApp:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        self.root.configure(bg='black')

#---------------------------------------------------------------------------------------------------------------------
        #making variables
        self.cName=StringVar()
        self.cAddress=StringVar()
        self.cNumber=StringVar()
        self.cEmail=StringVar()
        self.pName=StringVar()
        self.pPrice=IntVar()
        self.pQuantity=IntVar()
        self.srcBill=StringVar()
        #to generate random bill number
        z=random.randint(1000,999999)
        self.srcBill.set(z)
        self.subTotal=StringVar()
        self.govTax=StringVar()
        self.totalAmount=StringVar()

        


        #making product category list
        self.category=["Select Option","Clothing","HomeAppliances","LifeStyles","Mechanics","Gadgets"]

        self.subCatClothing=["Male","Female"]
        self.subCatHomeAppliances=["Major Appliances","Minor appliances","Small Appliances"]
        self.subCatLifeStyles=["Food","Fruits","Vegetables"]
        self.subCatMechanics=["Machines","Tools"]
        self.subCatGadgets=["Smartphones","Watches","Speakers","Computers"]


        #imgae aboove heading
        img=Image.open("images/mart6.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        lbl_img=Label(self.root,image=self.photoimg)
        lbl_img.place(x=0,y=0,width=500,height=130)

        #imgae 2 for above heading
        img2=Image.open("images/mart10.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lbl_img2=Label(self.root,image=self.photoimg2)
        lbl_img2.place(x=500,y=0,width=500,height=130)

        #image 3 for above heading
        img3=Image.open("images/mart8.jpeg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lbl_img3=Label(self.root,image=self.photoimg3)
        lbl_img3.place(x=1000,y=0,width=500,height=130)
        
        #name of the organization
        lbl_title=Label(self.root,text="GAIRE MALL BILLING SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="orange",fg="red")
        lbl_title.place(x=0,y=130,width=1520,height=45)
#----------------------------------------------------------------------------------------------------------------------
        #making main frame 
        main_frame=Frame(self.root,bd=5,relief=GROOVE,bg="green")
        main_frame.place(x=0,y=174,width=1530,height=620)
#--------------------------------------------------------------------------------------------------------------------------
        #making customer frame
        customer_frame=LabelFrame(main_frame,text="CUSTOMERS",font=("times new roman",13,"bold"),bg="white",fg="brown")
        customer_frame.place(x=10,y=5,width=350,height=160)

        #making label for customer frame
        self.lbl_cname=Label(customer_frame,text="Customer Name:",font=("times new roman",11,"bold"),bg="white",fg="blue")
        self.lbl_cname.grid(row=0,column=0,stick=W,padx=5,pady=2)
        #for customer entry field
        self.entryname=ttk.Entry(customer_frame,textvariable=self.cName,font=("times new roman",11,"bold"),width=24)
        self.entryname.grid(row=0,column=1)

         #making label for customer address frame
        self.lbl_caddress=Label(customer_frame,text="Customer Address:",font=("times new roman",11,"bold"),bg="white",fg="blue")
        self.lbl_caddress.grid(row=1,column=0,stick=W,padx=5,pady=2)
        #for customer address entry field
        self.entryaddress=ttk.Entry(customer_frame,textvariable=self.cAddress,font=("times new roman",11,"bold"),width=24)
        self.entryaddress.grid(row=1,column=1)

         #making label for customer number
        self.lbl_cnumber=Label(customer_frame,text="Customer Number:",font=("times new roman",11,"bold"),bg="white",fg="blue")
        self.lbl_cnumber.grid(row=2,column=0,stick=W,padx=5,pady=2)
        #for customer entry field
        self.entrynumber=ttk.Entry(customer_frame,textvariable=self.cNumber,font=("times new roman",11,"bold"),width=24)
        self.entrynumber.grid(row=2,column=1)

         #making label for customer email frame
        self.lbl_cemail=Label(customer_frame,text="Customer Email:",font=("times new roman",11,"bold"),bg="white",fg="blue")
        self.lbl_cemail.grid(row=3,column=0,stick=W,padx=5,pady=2)
        #for customer entry field
        self.entryemail=ttk.Entry(customer_frame,textvariable=self.cEmail,font=("times new roman",11,"bold"),width=24)
        self.entryemail.grid(row=3,column=1)

#--------------------------------------------------------------------------------------------------------------------
        #making product frame
        product_frame=LabelFrame(main_frame,text="PRODUCTS",font=("times new roman",13,"bold"),bg="white",fg="brown")
        product_frame.place(x=370,y=5,width=600,height=160)

        # product category
        self.lbl_pcategory=Label(product_frame,text="Select Category:",font=("times new roman",11,"bold"),bg="white",fg="blue")
        self.lbl_pcategory.grid(row=0,column=0,stick=W,padx=5,pady=2)
        #making combobox for category
        self.cmb_category=ttk.Combobox(product_frame,value=self.category,font=("times new roman",11,"bold"),width=20,state="readonly")
        self.cmb_category.current(0)
        self.cmb_category.grid(row=0,column=1)
        self.cmb_category.bind("<<ComboboxSelected>>",self.categoryfunc)

        # subcategory
        self.lbl_psubcategory=Label(product_frame,text="Sub Category:",font=("times new roman",11,"bold"),bg="white",fg="blue")
        self.lbl_psubcategory.grid(row=1,column=0,stick=W,padx=5,pady=2)
        #making combobox for sub category
        self.cmb_subcategory=ttk.Combobox(product_frame,font=("times new roman",11,"bold"),width=20,state="readonly")
        self.cmb_subcategory.grid(row=1,column=1)

        # product name
        self.lbl_pname=Label(product_frame,text="Product Name:",font=("times new roman",11,"bold"),bg="white",fg="blue")
        self.lbl_pname.grid(row=0,column=2,stick=W,padx=5,pady=2)
        #making textfield for product name
        self.P_name=ttk.Entry(product_frame,textvariable=self.pName,font=("times new roman",11,"bold"),width=20)
        self.P_name.grid(row=0,column=3)

        # product price
        self.lbl_pprice=Label(product_frame,text="Price Per Unit:",font=("times new roman",11,"bold"),bg="white",fg="blue")
        self.lbl_pprice.grid(row=1,column=2,stick=W,padx=5,pady=2)
        #making textfield for product price
        self.p_price=ttk.Entry(product_frame,textvariable=self.pPrice,font=("times new roman",11,"bold"),width=20)
        self.p_price.grid(row=1,column=3)

        # product Quantity
        self.lbl_pquantity=Label(product_frame,text="Quantity:",font=("times new roman",11,"bold"),bg="white",fg="blue")
        self.lbl_pquantity.grid(row=2,column=2,stick=W,padx=5,pady=2)
        #making text for category
        self.P_quantity=ttk.Entry(product_frame,textvariable=self.pQuantity,font=("times new roman",11,"bold"),width=20)
        self.P_quantity.grid(row=2,column=3)
#---------------------------------------------------------------------------------------------------------------------------
        # middleimage frame
        Middleimage_frame=LabelFrame(self.root,bd=10)
        Middleimage_frame.place(x=15,y=350,width=960,height=180)

        #putting image in frame
        
        imgM1=Image.open("images/img1.jpg")
        imgM1=imgM1.resize((480,180),Image.ANTIALIAS)
        self.photoimgM1=ImageTk.PhotoImage(imgM1)
        lbl_imgM1=Label(Middleimage_frame,image=self.photoimgM1)
        lbl_imgM1.place(x=0,y=0,width=500,height=180)

        
        imgM2=Image.open("images/img3.jpg")
        imgM2=imgM2.resize((480,180),Image.ANTIALIAS)
        self.photoimgM2=ImageTk.PhotoImage(imgM2)
        lbl_imgM2=Label(Middleimage_frame,image=self.photoimgM2)
        lbl_imgM2.place(x=480,y=0,width=500,height=180)


#------------------------------------------------------------------------------------------------------------------------
        # right frame bill Area

        bill_frame=LabelFrame(main_frame,text="BILL AREA",font=("times new roman",13,"bold"),bg="white",fg="brown")
        bill_frame.place(x=980,y=45,width=360,height=470)

        #making text field for bill frame
        scroll_bar=Scrollbar(bill_frame,orient=VERTICAL)
        self.textarea=Text(bill_frame,yscrollcommand=scroll_bar.set,bg="white",fg="green",font=("times new roman",11))
        scroll_bar.pack(side=RIGHT,fill=Y)
        scroll_bar.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
#-----------------------------------------------------------------------------------------------------------------------------
       #search button and field
        src_frame=Frame(main_frame,bd=2,bg="white")
        src_frame.place(x=980,y=5,width=360,height=40)

        #search label
        self.lbl_psearch=Label(src_frame,text="Bill Number:",font=("times new roman",11,"bold"),bg="red",fg="white")
        self.lbl_psearch.grid(row=0,column=0,stick=W,padx=1)
        #making text area for search
        self.P_search=ttk.Entry(src_frame,textvariable=self.srcBill,font=("times new roman",11,"bold"),width=20)
        self.P_search.grid(row=0,column=1,stick=W,padx=2)

        #making search button
        self.btnSearch=Button(src_frame,text="SEARCH",command=self.Search_Bill,font=("times new roman",10,"bold"),bg="red",fg="white" ,width=10,cursor="hand2")
        self.btnSearch.grid(row=0,column=2 )



#-----------------------------------------------------------------------------------------------------------------------
        #bill counter frame
        billcounter_frame=LabelFrame(main_frame,text="Bill_COUNTER",font=("times new roman",13,"bold"),bg="white",fg="brown")
        billcounter_frame.place(x=10,y=355,width=960,height=160)

        # subtotal
        self.lbl_subtotal=Label(billcounter_frame,text="Sub Total:",font=("times new roman",14,"bold"),bg="white",fg="blue")
        self.lbl_subtotal.grid(row=0,column=0,stick=W,padx=5,pady=2)
        #making texfield for subtotal
        self.P_subtotal=ttk.Entry(billcounter_frame,textvariable=self.subTotal,font=("times new roman",13,"bold"),width=20)
        self.P_subtotal.grid(row=0,column=1)

        # tax
        self.lbl_tax=Label(billcounter_frame,text="GOV Tax",font=("times new roman",14,"bold"),bg="white",fg="blue")
        self.lbl_tax.grid(row=1,column=0,stick=W,padx=5,pady=2)
        #making texfield for subtotal
        self.P_tax=ttk.Entry(billcounter_frame,textvariable=self.govTax,font=("times new roman",13,"bold"),width=20)
        self.P_tax.grid(row=1,column=1)

        # total amount
        self.lbl_totalamount=Label(billcounter_frame,text="Total Amount:",font=("times new roman",14,"bold"),bg="white",fg="blue")
        self.lbl_totalamount.grid(row=2,column=0,stick=W,padx=5,pady=2)
        #making texfield for subtotal
        self.P_totalamount=ttk.Entry(billcounter_frame,textvariable=self.totalAmount,font=("times new roman",13,"bold"),width=20)
        self.P_totalamount.grid(row=2,column=1)
#-------------------------------------------------------------------------------------------------------------------------
        #button frame
        btn_frame=Frame(billcounter_frame,bd=2,bg="white")
        btn_frame.place(x=320,y=0)
        #making button
        self.btnAdd=Button(btn_frame,height=2,text="ADD TO CART",command=self.AddItem,font=("times new roman",14,"bold"),bg="green",fg="white",width=20,cursor="hand2")
        self.btnAdd.grid(row=0,column=0,padx=5,pady=5)

        self.btnGenBill=Button(btn_frame,height=2,text="GENERATE BILL",command=self.Generate_Bill,font=("times new roman",14,"bold"),bg="green",fg="white" ,width=20,cursor="hand2")
        self.btnGenBill.grid(row=0,column=1 ,padx=5,pady=5)

        self.btnSave=Button(btn_frame,height=2,text="SAVE",command=self.Save_Bill,font=("times new roman",14,"bold"),bg="green",fg="white",width=10,cursor="hand2")
        self.btnSave.grid(row=0,column=2 ,padx=5,pady=5)

        self.btnPrint=Button(btn_frame,height=2,text="PRINT",command=self.Print_Bill,font=("times new roman",14,"bold"),bg="green",fg="white",width=20,cursor="hand2")
        self.btnPrint.grid(row=1,column=0 ,padx=5,pady=5)

        self.btnClear=Button(btn_frame,height=2,text="CLEAR",command=self.clear,font=("times new roman",14,"bold"),bg="green",fg="white",width=20,cursor="hand2")
        self.btnClear.grid(row=1,column=1 ,padx=5,pady=5)

        self.btnExit=Button(btn_frame,height=2,text="EXIT",command=self.root.destroy,font=("times new roman",14,"bold"),bg="green",fg="white" ,width=10,cursor="hand2")
        self.btnExit.grid(row=1,column=2 ,padx=5,pady=5)

        #calling design page
        self.billDesign()

        #for other us making variable
        self.refAmount=[]
     #===============Adding items it the bill======Function declaration======================
    def AddItem(self):
            Tax=1
            self.rate=self.pPrice.get()
            self.qty=self.pQuantity.get()
            self.amount=self.rate*self.qty
            self.refAmount.append(self.amount)

            if self.pName.get()=="":
                    messagebox.showerror("ERROR","PLease Enter the Product Name")
            else:
                    self.textarea.insert(END,f"\n|{self.pName.get()}\t\t\t|{self.pQuantity.get()}\t|{self.pPrice.get()}\t|{self.amount}")
                    self.subTotal.set(str('Rs.%.2f'%(sum(self.refAmount))))
                    self.govTax.set(str('Rs.%.2f'%((((sum(self.refAmount)) - (self.pPrice.get()))*Tax)/100)))
                    self.totalAmount.set(str('Rs.%.2f'%(((sum(self.refAmount)) + ((((sum(self.refAmount)) - (self.pPrice.get()))*Tax/100))))))
    def Generate_Bill(self):
            if self.pName.get()=="":
                    messagebox.showerror("ERROR","PLease Add To Cart product")
            else:
                    text=self.textarea.get(10.0,(10.0+float(len(self.refAmount))))
                    self.billDesign()
                    self.textarea.insert(END,text)
                    self.textarea.insert(END,f"\n-------------------------------------------------------------------")
                    self.textarea.insert(END,f"\n Sub Total Amount:\t\t\t\t{self.subTotal.get()}")
                    self.textarea.insert(END,f"\n Goverment Tax:\t\t\t\t{self.govTax.get()}")
                    self.textarea.insert(END,f"\n Final Total Amount:\t\t\t\t{self.totalAmount.get()}")
                    self.textarea.insert(END,f"\n------------------------------------------------------------------")
                    self.textarea.insert(END,f"\t-----------!!!Thank You For Shopping Here!!!-------------")
    #saving bill funnction
    def Save_Bill(self):
            op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
            if op>0:
                    self.bill_data=self.textarea.get(1.0,END)
                    f1=open('bills/'+str(self.srcBill.get())+".txt","w")
                    f1.write(self.bill_data)
                    op=messagebox.showinfo("Task Sucess",f"The Bill Number:{self.srcBill.get()} is save sucessfully")
                    f1.close()
     #print bill function
    def Print_Bill(self):
             pr=self.textarea.get(1.0,END)
             filename=tempfile.mktemp('.txt')
             open(filename,'w').write(pr)
             os.startfile(filename,"print")
    #search bill function
    def Search_Bill(self):
            found="no"
            for i in os.listdir("bills/"):
                    if i.split('.')[0]==self.srcBill.get():
                        f1=open(f'bills/{i}','r')
                        self.textarea.delete(1.0,END)
                        for d in f1:
                                self.textarea.insert(END,d)
                        f1.close()
                        found="yes"
            if found=="no":
                     messagebox.showerror("Invalid Bill Number","This bill is invalid")
    #making clear function
    def clear(self):
            self.textarea.delete(1.0,END)  
            self.cName.set("")
            self.cAddress.set("")
            self.cNumber.set("")
            self.cEmail.set("")
            self.pName.set("")
            self.pPrice.set(0)
            self.pQuantity.set(0)
            self.srcBill.set("")
        #to generate random bill number
            z=random.randint(1000,999999)
            self.srcBill.set(str())
            self.subTotal.set("")
            self.govTax.set('')
            self.totalAmount.set("")  
            self.amount[0]
            self.billDesign()
        


    #designing the bill
    def billDesign(self):
            self.textarea.delete(1.0,END)
            self.textarea.insert(END,"\tGAIRE MALL BILLING SYSTEM")
            self.textarea.insert(END,"\n------------------------------------------------------------------")
            self.textarea.insert(END,f"\nBill NO:{self.srcBill.get()}")
            self.textarea.insert(END,f"\nCustomer Name:{self.cName.get()}")
            self.textarea.insert(END,f"\nCustomer Address:{self.cAddress.get()}")
            self.textarea.insert(END,f"\nCustomer Contact:{self.cNumber.get()}")
            self.textarea.insert(END,f"\nCustomer Email:{self.cEmail.get()}")
            self.textarea.insert(END,f"\n-------------------------------------------------------------------")
            self.textarea.insert(END,f"\n|Particulars\t\t\t|Qunatity\t|Rate\t|Amount")
            self.textarea.insert(END,"\n-------------------------------------------------------------------\n")
             
             


    def categoryfunc(self,event=""):
            if self.cmb_category.get()=="Clothing":
                    self.cmb_subcategory.config(value=self.subCatClothing)
                    self.cmb_subcategory.current(0)

            if self.cmb_category.get()=="HomeAppliances":
                    self.cmb_subcategory.config(value=self.subCatHomeAppliances)
                    self.cmb_subcategory.current(0)

            if self.cmb_category.get()=="LifeStyles":
                    self.cmb_subcategory.config(value=self.subCatLifeStyles)
                    self.cmb_subcategory.current(0)

            if self.cmb_category.get()=="Mechanics":
                    self.cmb_subcategory.config(value=self.subCatMechanics)
                    self.cmb_subcategory.current(0)

            if self.cmb_category.get()=="Gadgets":
                    self.cmb_subcategory.config(value=self.subCatGadgets)
                    self.cmb_subcategory.current(0)

        






if __name__== '__main__':
    root=Tk()
    obj=BillApp(root)
    root.mainloop()

    
