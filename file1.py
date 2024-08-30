from tkinter import *
from tkinter import ttk
import tkinter as tk
import pymysql
from tkinter import messagebox

#pymysql, mysql.connector, sqlite3 (ye use hote hai python ko sql se connect krne ke liye)

root=Tk()
root.geometry("1350x700")
root.title("Student Management System")

title_label= Label(root, text="Student Management System", font= ("arial", 20, "bold"), border= 12, relief=GROOVE, bg= "blue", foreground="yellow")
title_label.pack(side=TOP, fill=X)

#---------------functions------------>>

def fetch_data():
    conn= pymysql.connect(host="localhost", user="root", password="admin", database="Project1")
    curr= conn.cursor()
    curr.execute("SELECT* FROM data1")
    rows= curr.fetchall()
    if len(rows)!= 0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END, values=row)
        conn.commit()
    conn.close()

# def add_func():
#     if rollvalue.get() == "" or namevalue.get() == "" or contactvalue== "":
#         messagebox.showerror("Error", "Please fill all the fields")
        
#     else:
#         conn= pymysql.connect(host="localhost", user="root", password="admin", database="Project1")
#         curr= conn.cursor()
#         curr.execute("INSERT INTO data1 VALUES(%s,%s,%s,%s,%s,%s,%s)", (rollvalue.get(), namevalue.get(), emailvalue.get(), gendervalue.get(), contactvalue.get(), dobvalue.get(), addressvalue.get()))
#         conn.commit()
#         conn.close()
#         fetch_data()

def add_func():
    if rollvalue.get() == "" or namevalue.get() == "" or contactvalue.get() == "":
        messagebox.showerror("Error", "Please fill all the fields")
    else:
        try:
            # Establish connection to the MySQL database
            conn = pymysql.connect(host="localhost", user="root", password="admin", database="Project1")
            curr = conn.cursor()
            
            # Execute the SQL INSERT statement
            curr.execute(
                "INSERT INTO data1 (roll_no, name, email, gender, contact, dob, address) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (rollvalue.get(), namevalue.get(), emailvalue.get(), gendervalue.get(), contactvalue.get(), dobvalue.get(), addressvalue.get())
            )
            
            # Commit changes to the database
            conn.commit()
            messagebox.showinfo("Success", "Record added successfully!")

            # Fetch the updated data to refresh the display
            fetch_data()

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error adding data to database: {e}")

        finally:
            # Close the database connection
            conn.close()


def get_cursor(event):
    cursor_row= student_table.focus()
    content= student_table.item(cursor_row)
    row= content['values']
    rollvalue.set(row[0])
    namevalue.set(row[1])
    emailvalue.set(row[2])
    gendervalue.set(row[3])
    contactvalue.set(row[4])
    dobvalue.set(row[5])
    addressvalue.set(row[6])
    
    
def clear_func():
    rollvalue.set("")
    namevalue.set("")
    emailvalue.set("")
    gendervalue.set("")
    contactvalue.set("")
    dobvalue.set("")
    addressvalue.set("")
    
def update_func():
    conn= pymysql.connect(host="localhost", user="root", password="admin", database="Project1")
    curr= conn.cursor()
    curr.execute("UPDATE data1 SET name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s WHERE roll_no=%s",(namevalue.get(), emailvalue.get(), gendervalue.get(), contactvalue.get(), dobvalue.get(), addressvalue.get(), rollvalue.get()))
    conn.commit()
    conn.close()
    fetch_data()    
    clear_func()
    

def delete_func():
    if rollvalue.get() == "":
        messagebox.showerror("Error", "Please select a record to delete")
    else:
        try:
            conn = pymysql.connect(host="localhost", user="root", password="admin", database="Project1")
            curr = conn.cursor()
            curr.execute("DELETE FROM data1 WHERE roll_no=%s", (rollvalue.get(),))
            conn.commit()
            messagebox.showinfo("Success", "Record deleted successfully!")
            fetch_data()
            clear_func()
        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error deleting data from database: {e}")
        finally:
            conn.close()
    
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

detail_frame= LabelFrame(root, text="Enter Details", font= ("arial", 20), border=12, relief=GROOVE, bg="lightgrey")
detail_frame.place(x= 20, y=90, width= 420, height= 570)

data_frame= Frame(root, border=12, bg="lightgrey", relief=GROOVE)
data_frame.place(x= 460, y=90,width=800, height=570)

manage_head= Label(detail_frame, text="Manage Students", font=("arial", 15, "bold"), foreground="black", bg="lightgrey", relief=GROOVE)
manage_head.pack(side=TOP, fill=X, pady=15)

rollno= Label(detail_frame, text="Roll No.", font=("arila", 12, "bold"), foreground="black", bg="lightgrey", anchor="nw")
rollno.place(x=5, y=70)

name_s= Label(detail_frame, text="Name", font=("arila", 12, "bold"), foreground="black", bg="lightgrey", anchor="nw")
name_s.place(x=5, y=110)

email_s= Label(detail_frame, text="Email", font=("arila", 12, "bold"), foreground="black", bg="lightgrey", anchor="nw")
email_s.place(x=5, y=150)

gender_s= Label(detail_frame, text="Gender", font=("arila", 12, "bold"), foreground="black", bg="lightgrey", anchor="nw")
gender_s.place(x=5, y=190)

contact_s= Label(detail_frame, text="Contact", font=("arila", 12, "bold"), foreground="black", bg="lightgrey", anchor="nw")
contact_s.place(x=5, y=230)

dob_s= Label(detail_frame, text="D.O.B", font=("arila", 12, "bold"), foreground="black", bg="lightgrey", anchor="nw")
dob_s.place(x=5, y=270)

addr_s= Label(detail_frame, text="Address", font=("arila", 12, "bold"), foreground="black", bg="lightgrey", anchor="nw")
addr_s.place(x=5, y=310)

#entries for details frame

rollvalue= StringVar()
namevalue= StringVar()
emailvalue= StringVar()
gendervalue= StringVar()
contactvalue= StringVar()
dobvalue= StringVar()
addressvalue= StringVar()

searcvinvalue= StringVar()

#final entry

rollentry= Entry(detail_frame, textvariable= rollvalue, border=2, relief=GROOVE)
nameentry= Entry(detail_frame, textvariable= namevalue, border=2, relief=GROOVE)
emailentry= Entry(detail_frame, textvariable=emailvalue, border=2, relief=GROOVE)
genderentry= Entry(detail_frame, textvariable=gendervalue, border=2, relief=GROOVE)
contactentry= Entry(detail_frame, textvariable=contactvalue, border=2, relief=GROOVE)
dobentry= Entry(detail_frame, textvariable=dobvalue, border=2, relief=GROOVE)
addressentry= Entry(detail_frame, textvariable=addressvalue, border=2, relief=GROOVE)





rollentry.place(x=100, y=70)
nameentry.place(x=100, y=110, width=180, height=25)
emailentry.place(x=100, y=150, width=180)
genderentry.place(x=100, y=190)
contactentry.place(x=100, y=230)
dobentry.place(x=100, y=270)
addressentry.place(x=100, y=310, height=50, width=180)

audc= Frame(detail_frame, relief=GROOVE, bg="lightgrey")
audc.place(x=6, y= 450, height=50, width=380)

audc_button= Button(audc, text="Add", foreground="black", bg="darkgrey", anchor="w", command=add_func)
audc_button.pack(side=LEFT, padx= 20)

audc_button2= Button(audc, text="Update", foreground="black", bg="darkgrey", command=update_func)
audc_button2.pack(side=LEFT, padx= 30)

audc_button3= Button(audc, text="Delete", foreground="black", bg="darkgrey", command= delete_func)
audc_button3.pack(side=LEFT, padx= 20)

audc_button4= Button(audc, text="Clear", foreground="black", bg="darkgrey", command= clear_func)
audc_button4.pack(side=LEFT, padx= 40)

data_frame_frame= Frame(data_frame, border=3, bg="lightgrey")
data_frame_frame.pack()

# iss frame ke liye things

searchby= Label(data_frame_frame, text="Search By", font=("arial", 10, "bold"))
searchby.grid(row=0, column=0, padx=20,pady=10)

searchinentry= Entry(data_frame_frame, textvariable=searcvinvalue, border=2, relief=GROOVE)
searchin= ttk.Combobox(data_frame_frame, font= ("arial", 10), state= "readonly", textvariable=searcvinvalue)
searchin['values']= ("Roll No.", "Name", "Email","Gender", "Contact", "D.O.B", "Address")
searchin.grid(row=0, column= 1, padx= 20, pady=10)

search_button= Button(data_frame_frame, text="Search", font= ("arial", 10, "bold"), width=15)
search_button.grid(row=0, column=2, padx=20, pady=10)

searchall_button= Button(data_frame_frame, text="Search All", font= ("arial", 10, "bold"), width=15)
searchall_button.grid(row=0, column=3, padx=20, pady=10)

entry_frame= Frame(data_frame, border=3, relief=GROOVE)
entry_frame.pack(fill=tk.BOTH, expand=True)

y_scroll= Scrollbar(entry_frame, orient= VERTICAL)
x_scroll= Scrollbar(entry_frame, orient= HORIZONTAL)

student_table= ttk.Treeview(entry_frame, columns=("Roll No.","Name","Email","Gender","Contact","D.O.B","Address"), yscrollcommand= y_scroll.set, xscrollcommand= x_scroll.set)

y_scroll.config(command= student_table.yview)
x_scroll.config(command= student_table.xview)

y_scroll.pack(side= RIGHT, fill=Y)
x_scroll.pack(side= BOTTOM, fill=X)

student_table.heading("Roll No.", text="Roll No.")
student_table.heading("Name", text="Name")
student_table.heading("Email", text="Email")
student_table.heading("Gender", text="Gender")
student_table.heading("Contact", text="Contact")
student_table.heading("D.O.B", text="D.O.B")
student_table.heading("Address", text="Address")

student_table['show']= "headings"

student_table.column("Roll No.", width=100)
student_table.column("Name", width=100)
student_table.column("Email", width=100)
student_table.column("Gender", width=100)
student_table.column("Contact", width=100)
student_table.column("D.O.B", width=100)
student_table.column("Address", width=100)


student_table.pack(fill= BOTH, expand= True)

fetch_data()

student_table.bind("<ButtonRelease-1>", get_cursor)

root.mainloop()