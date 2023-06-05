import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tkinter"
)

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()

    cursor = db.cursor()
    query = "INSERT INTO student (name, age, grade) VALUES (%s, %s, %s)"
    values = (name, age, grade)
    cursor.execute(query, values)
    db.commit()

    messagebox.showinfo("Success", "Student added successfully")
    clear_entries()
    fetch_students()

def fetch_students():
    cursor = db.cursor()
    query = "SELECT * FROM student"
    cursor.execute(query)
    records = cursor.fetchall()

    for row in student_table.get_children():
        student_table.delete(row)

    for row in records:
        student_table.insert("", END, values=row)

def update_student():
    selected_item = student_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "No student selected")
        return

    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    selected_id = student_table.item(selected_item)['values'][0]

    cursor = db.cursor()
    query = "UPDATE student SET name=%s, age=%s, grade=%s WHERE id=%s"
    values = (name, age, grade, selected_id)
    cursor.execute(query, values)
    db.commit()

    messagebox.showinfo("Success", "Student updated successfully")
    clear_entries()
    fetch_students()

def delete_student():
    selected_item = student_table.selection()
    if not selected_item:
        messagebox.showerror("Error", "No student selected")
        return

    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this student?")
    if confirmation:
        selected_id = student_table.item(selected_item)['values'][0]

        cursor = db.cursor()
        query = "DELETE FROM student WHERE id=%s"
        values = (selected_id,)
        cursor.execute(query, values)
        db.commit()

        messagebox.showinfo("Success", "Student deleted successfully")
        fetch_students()

def clear_entries():
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    grade_entry.delete(0, END)

root = Tk()
root.title("CRUD Application Ntic")

name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

age_label = Label(root, text="Age:")
age_label.grid(row=1, column=0)
age_entry = Entry(root)
age_entry.grid(row=1, column=1)

grade_label = Label(root, text="Grade:")
grade_label.grid(row=2, column=0)
grade_entry = Entry(root)
grade_entry.grid(row=2, column=1)

add_button = Button(root, text="Add", command=add_student)
add_button.grid(row=3, column=0)

update_button = Button(root, text="Update", command=update_student)
update_button.grid(row=3, column=1)

student_table = ttk.Treeview(root, columns=("ID", "Name", "Age", "Grade"), show="headings")
student_table.grid(row=4, column=0, columnspan=2)

student_table.heading("ID", text="ID")
student_table.heading("Name", text="Name")
student_table.heading("Age", text="Age")
student_table.heading("Grade", text="Grade")

delete_button = Button(root, text="Delete", command=delete_student)
delete_button.grid(row=5, column=0, columnspan=2)

fetch_students()

root.mainloop()
