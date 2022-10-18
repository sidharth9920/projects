from ast import Delete
from multiprocessing.sharedctypes import Value
from optparse import Values
from tkinter import *
from tkinter import messagebox, ttk

import pymysql
from PIL import Image, ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Students management system")
        self.root.geometry("1350x700+0+0")
        
        title=Label(self.root,text="Students management system",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP,fill=X) 

        #===========All vairables==========#
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.roll_no_var=StringVar()
        self.search_by_var=StringVar()
        self.search_txt_var=StringVar()

        #===========Manage frame==========#
        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        manage_frame.place(x=20,y=100,width=470,height=580)

        m_title=Label(manage_frame,text="Manage Students",font=("times new roman",30,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(manage_frame,text="Roll No :",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(manage_frame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,bg="white",fg="black")
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(manage_frame,text="Name :",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(manage_frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,bg="white",fg="black")
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_email=Label(manage_frame,text="Email :",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_email=Entry(manage_frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,bg="white",fg="black")
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_gender=Label(manage_frame,text="Gender :",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(manage_frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20)

        lbl_contact=Label(manage_frame,text="Contact No :",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_contact=Entry(manage_frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,bg="white",fg="black")
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_dob=Label(manage_frame,text="D.O.B :",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(manage_frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,bg="white",fg="black")
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_address=Label(manage_frame,text="Address :",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_address=Text(manage_frame,width=28,height=4,font=("times new roman",10,"bold"),bd=5,relief=GROOVE,bg="white",fg="black")
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #========Button Frame=============#

        btn_frame=Frame(manage_frame,bd=4,relief=RIDGE,bg="crimson")
        btn_frame.place(x=15,y=525,width=420)

        add_btn=Button(btn_frame,text="ADD",command=self.add_students,width=10).grid(row=0,column=0,padx=15)

        update_btn=Button(btn_frame,text="UPDATE",command=self.update_data,width=10).grid(row=0,column=1,padx=10)

        del_btn=Button(btn_frame,text="DELETE",command=self.delete_data,width=10).grid(row=0,column=2,padx=10)

        clear_btn=Button(btn_frame,text="CLEAR",command=self.clear,width=10).grid(row=0,column=3,padx=10)

        #===========Detail frame==========#

        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        detail_frame.place(x=500,y=100,width=825,height=580)

        search_lbl=Label(detail_frame,text="Search By :",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        search_lbl.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by_var,font=("times new roman",13,"bold"),state="readonly",width=10)
        combo_search['values']=("Roll_no","Name","Contatct")
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(detail_frame,textvariable=self.search_txt_var,width=15,font=("times new roman",15,"bold"),bd=5,relief=GROOVE,bg="white",fg="black")
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        search_btn=Button(detail_frame,text="SEARCH",command=self.search_data,width=10,pady=5).grid(row=0,column=3,padx=10)
        searchall_btn=Button(detail_frame,text="SEARCH ALL",command=self.fetch_data,width=10,pady=5).grid(row=0,column=4,padx=10)

        #===========Table frame==========#
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE,bg="crimson")
        table_frame.place(x=10,y=70,width=800,height=500)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("Roll No","Name","Email","Gender","Contact","D.O.B","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Roll No",text="Roll No.")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Contact",text="Contact")
        self.student_table.heading("D.O.B",text="D.O.B")
        self.student_table.heading("Address",text="Address")
        self.student_table['show']='headings'
        self.student_table.column("Roll No",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Contact",width=100)
        self.student_table.column("D.O.B",width=100)
        self.student_table.column("Address",width=175)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_coursor)
        self.fetch_data()

    def add_students(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="":
            messagebox.showerror("ERROR","All dields are required")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",( self.roll_no_var.get(),self.name_var.get(),self.email_var.get(),
            self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END)
            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been inserted ")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.contact_var.set("")
        self.gender_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_coursor(self,ev):
        coursor_row=self.student_table.focus()
        contents=self.student_table.item(coursor_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.contact_var.set(row[4])
        self.gender_var.set(row[3])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])
    
    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set Name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s where Roll_no=%s",( self.name_var.get(),self.email_var.get(),
        self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END),self.roll_no_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Success","Record has been updated ")
    
    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where Roll_no=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()
        messagebox.showinfo("Success","Record has been deleted ")

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()

        cur.execute("select * from students where "+str(self.search_by_var.get())+" LIKE '%"+str(self.search_txt_var.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()



if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()
