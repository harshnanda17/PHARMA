from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

        lbltiltle=Label(self.root,text="PHARAMACY MANAGEMENT SYSTEM",bd=15,relief=RIDGE,bg='white',
            fg="darkgreen",font=("times new roman",42,"bold"),padx=2,pady=4)
        lbltiltle.pack(side=TOP,fill=X)

        img1=Image.open("C:\PHARMA\logo.png")
        img1=img1.resize((80,50),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        b1=Button(self.root,image=self.photoimg1,borderwidth=0)
        b1.place(x=70,y=20)

# *************** DATA FRAME ************** # 
        DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        DataFrame.place(x=0,y=120,width=1360,height=400)

        DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
            fg="darkgreen",font=("arial",12,"bold"))

        DataFrameLeft.place(x=0,y=5,width=890,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
            fg="darkgreen",font=("arial",12,"bold"))
        
        DataFrameRight.place(x=900,y=5,width=400,height=350)

################### ButtonsFrame ########################

        ButtonFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
        ButtonFrame.place(x=0,y=520,width=1360,height=65)

# ############### Main Button ############## #


        btnAddDate=Button(ButtonFrame,text=" Medicine Add ",font=("arial",12,"bold"),bg="green",fg="white")
        btnAddDate.grid(row=0,column=0)

        btnAddDate=Button(ButtonFrame,text=" UPDATE ",font=("arial",12,"bold"),width=14,bg="purple",fg="white")
        btnAddDate.grid(row=0,column=1)

        btnAddDate=Button(ButtonFrame,text="DELETE",font=("arial",12,"bold"),width=14,bg="red",fg="white")
        btnAddDate.grid(row=0,column=2)

        btnAddDate=Button(ButtonFrame,text="RESET",font=("arial",12,"bold"),width=14,bg="blue",fg="white")
        btnAddDate.grid(row=0,column=3)

        btnAddDate=Button(ButtonFrame,text="EXIT",font=("arial",12,"bold"),width=14,bg="darkgreen",fg="white")
        btnAddDate.grid(row=0,column=4)

# ############## Search By ############## #

        lblSearch=Label(ButtonFrame,font=("arial",17,"bold"),text="Search By",padx=2,bg="orange",fg="white")
        lblSearch.grid(row=0,column=5,sticky=W)

        serch_combo=ttk.Combobox(ButtonFrame,width=9,font=("arial",17,"bold"),state="readonly")
        serch_combo["values"]=("Ref","Medname","Lot")
        serch_combo.grid(row=0,column=6)
        serch_combo.current(0)

        txtSerch=Entry(ButtonFrame,bd=3,relief=RIDGE,width=8,font=("arial",17,"bold"))
        txtSerch.grid(row=0,column=7)

        searchBtn=Button(ButtonFrame,text="SEARCH",font=("arial",13,"bold"),bg="blue",fg="white")
        searchBtn.grid(row=0,column=8)

        showAll=Button(ButtonFrame,text="SHOW ALL",font=("arial",13,"bold"),bg="darkgreen",fg="white")
        showAll.grid(row=0,column=9)

# ################ Label and Entry ############### #
        
        lblrefno=Label(DataFrameLeft,font=("arial",12,"bold"),text="Reference No",padx=2)
        lblrefno.grid(row=0,column=0,sticky=W)


        ref_combo=ttk.Combobox(DataFrameLeft,width=27,font=("arial",12,"bold"),state="readonly")
        ref_combo["values"]=("Ref","Medname","Lot")
        ref_combo.grid(row=0,column=1)
        ref_combo.current(0)

        lblCmpName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Company Name:",padx=2,pady=6)
        lblCmpName.grid(row=1,column=0,sticky=W)
        txtCmpName=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtCmpName.grid(row=1,column=1)

        lblTypeofMedicine=Label(DataFrameLeft,font=("arial",12,"bold"),text="Type Of Medicine",padx=2,pady=6)
        lblTypeofMedicine.grid(row=2,column=0,sticky=W)

        comTypeofMedicine=ttk.Combobox(DataFrameLeft,state="readonly",font=("arial",12,"bold"),width=27)
        comTypeofMedicine["value"]=("Tablet","Liquid","Capsules","Topical Medicines","Drops","Inhales","Injection")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2,column=1)

# ############## Add Medicine ############### #

        lblMedicineName=Label(DataFrameLeft,font=("arial",12,"bold"),text="Medicine Name",padx=2,pady=6)
        lblMedicineName.grid(row=3,column=0,sticky=W)

        comMedicineName=ttk.Combobox(DataFrameLeft,state="readonly",font=("arial",12,"bold"),width=27)
        comMedicineName["value"]=("nice","novel")
        comMedicineName.current(0)
        comMedicineName.grid(row=3,column=1)



        lblLotNo=Label(DataFrameLeft,font=("arial",12,"bold"),text="Lot No:",padx=2,pady=6)
        lblLotNo.grid(row=4,column=0,sticky=W)
        txtLotNo=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtLotNo.grid(row=4,column=1)

        lblIssueDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblIssueDate.grid(row=5,column=0,sticky=W)
        txtIssueDate=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtIssueDate.grid(row=5,column=1)

        lblExDate=Label(DataFrameLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExDate.grid(row=6,column=0,sticky=W)
        txtExDate=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtExDate.grid(row=6,column=1)

        lblUses=Label(DataFrameLeft,font=("arial",12,"bold"),text="Uses:",padx=2,pady=6)
        lblUses.grid(row=7,column=0,sticky=W)
        txtUses=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtUses.grid(row=7,column=1)

        lblSideEffect=Label(DataFrameLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtSideEffect.grid(row=8,column=1)

        lblPrecWarning=Label(DataFrameLeft,font=("arial",12,"bold"),text="Prec&Warning:",padx=15)
        lblPrecWarning.grid(row=0,column=2,sticky=W)
        txtPrecWarning=Entry(DataFrameLeft,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrecWarning.grid(row=0,column=3)

        lblDosage=Label(DataFrameLeft,font=("arial",12,"bold"),text="Dosage:",padx=15,pady=6)
        lblDosage.grid(row=1,column=2,sticky=W)
        txtDosage=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtDosage.grid(row=1,column=3)

        lblPrice=Label(DataFrameLeft,font=("arial",12,"bold"),text="Tablets Price:",padx=15,pady=6)
        lblPrice.grid(row=2,column=2,sticky=W)
        txtPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtPrice.grid(row=2,column=3)

        lblProductQt=Label(DataFrameLeft,font=("arial",12,"bold"),text="Product QT:",padx=15,pady=6)
        lblProductQt.grid(row=3,column=2,sticky=W)
        txtProductQt=Entry(DataFrameLeft,font=("arial",12,"bold"),bg="white",bd=2,relief=RIDGE,width=29)
        txtProductQt.grid(row=3,column=3)

# #################Image################### #

        lblhome=Label(DataFrameLeft,font=("arial",13,"bold"),text="Stay Home Stay Safe:",padx=2,pady=6,bg="white",fg="red",width=43)
        lblhome.place(x=410,y=140)

        img2=Image.open("C:\PHARMA\med.jpg")
        img2=img2.resize((150,135),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        b1=Button(self.root,image=self.photoimg2,borderwidth=0)
        b1.place(x=760,y=330)

        img3=Image.open("C:\PHARMA\doc.ico")
        img3=img3.resize((150,135),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        b1=Button(self.root,image=self.photoimg3,borderwidth=0)
        b1.place(x=620,y=330)

        img4=Image.open("C:\PHARMA\medi.jpg")
        img4=img4.resize((150,135),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        b1=Button(self.root,image=self.photoimg4,borderwidth=0)
        b1.place(x=475,y=330)

# ############### DataFrameRight ################ #

        DataFrameRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Add Department",
            fg="darkgreen",font=("arial",12,"bold"))
        DataFrameRight.place(x=900,y=5,width=400,height=350)

        img5=Image.open("C:\PHARMA\inject.jpg")
        img5=img5.resize((150,75),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        b1=Button(self.root,image=self.photoimg5,borderwidth=0)
        b1.place(x=950,y=160)

        img6=Image.open("C:\PHARMA\inject.jpg")
        img6=img6.resize((150,75),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        b1=Button(self.root,image=self.photoimg6,borderwidth=0)
        b1.place(x=1090,y=160)

        img7=Image.open("C:\PHARMA\co.jpg")
        img7=img7.resize((100,75),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        b1=Button(self.root,image=self.photoimg7,borderwidth=0)
        b1.place(x=1210,y=160)

        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Reference No:")
        lblrefno.place(x=0,y=80)
        txtrefno=Entry(DataFrameRight,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=24)
        txtrefno.place(x=135,y=80)

        lblrefno=Label(DataFrameRight,font=("arial",12,"bold"),text="Medicine Name:")
        lblrefno.place(x=0,y=110)
        txtrefno=Entry(DataFrameRight,font=("arial",13,"bold"),bg="white",bd=2,relief=RIDGE,width=24)
        txtrefno.place(x=135,y=110)

# ############### Side Frame ################# #

        side_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="white")
        side_frame.place(x=0,y=150,width=270,height=160)

        sc_x=ttk.Scrollbar(side_frame,orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM,fill=X)
        sc_y=ttk.Scrollbar(side_frame,orient=VERTICAL)
        sc_y.pack(side=RIGHT,fill=Y)

        self.medicine_table=ttk.Treeview(side_frame,columns=("ref","madname"),xscrollcommand=sc_x.set,yscrollcommand=sc_y.set)

        sc_x.config(command=self.medicine_table.xview)
        sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref",text="Ref")
        self.medicine_table.heading("madname",text="Medicine Name")

        self.medicine_table["show"]="headings"
        self.medicine_table.pack(fill=BOTH,expand=1)

        self.medicine_table.column("ref",width=100)
        self.medicine_table.column("madname",width=100)

        # ########### Medicine Add Buttons ########### #

        down_frame=Frame(DataFrameRight,bd=4,relief=RIDGE,bg="yellow")
        down_frame.place(x=270,y=150,width=90,height=160)

        btnAddmed=Button(down_frame,text="ADD",font=("arial",10,"bold"),width=9,bg="lime",fg="white",pady=6)
        btnAddmed.grid(row=0,column=0)

        btnUpdatemed=Button(down_frame,text="UPDATE",font=("arial",10,"bold"),width=9,bg="purple",fg="white",pady=6)
        btnUpdatemed.grid(row=1,column=0)

        btnDeletemed=Button(down_frame,text="DELETE",font=("arial",10,"bold"),width=9,bg="red",fg="white",pady=6)
        btnDeletemed.grid(row=2,column=0)

        btnClearmed=Button(down_frame,text="CLEAR",font=("arial",10,"bold"),width=9,bg="orange",fg="white",pady=6)
        btnClearmed.grid(row=3,column=0)

        # ###############Frame Detail################ #

        Framedeatils=Frame(self.root,bd=15,relief=RIDGE)
        Framedeatils.place(x=0,y=580,width=1360,height=120)

        # ############# Main Table & Scrollbar ############## #

        Table_frame=Frame(Framedeatils,bd=15,relief=RIDGE,padx=20)
        Table_frame.place(x=0,y=1,width=1330,height=110)

        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        scroll_y.pack(side=RIGHT,fill=Y) 

        self.pharmacy_table=ttk.Treeview(Table_frame,columns=("reg","companyname","type","tabletname","lotno","issuedate","expdate","uses","sideeffect","warning","dosage","price","productqt")
                ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"]="headings"

        self.pharmacy_table.heading("reg",text="Reference No")
        self.pharmacy_table.heading("companyname",text="Company Name")
        self.pharmacy_table.heading("type",text="Type Of Medicine")
        self.pharmacy_table.heading("tabletname",text="Tablet Name")
        self.pharmacy_table.heading("lotno",text="Lot No")
        self.pharmacy_table.heading("issuedate",text="Issue Date")
        self.pharmacy_table.heading("expdate",text="Exp Date")
        self.pharmacy_table.heading("uses",text="Uses")
        self.pharmacy_table.heading("sideeffect",text="Side Effect")
        self.pharmacy_table.heading("warning",text="Prec&Warning")
        self.pharmacy_table.heading("dosage",text="Dosage")
        self.pharmacy_table.heading("price",text="Price")
        self.pharmacy_table.heading("productqt",text="Product Qts")
        self.pharmacy_table.pack(fill=BOTH,expand=1)
        








if __name__== "__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
