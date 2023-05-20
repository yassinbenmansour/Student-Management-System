import tkinter as tk
from tkinter import ttk
import mysql.connector as mysql


db = mysql.connect(host='localhost', user='root', password='', database='ntic_stock')
c = db.cursor()

def add_item():
    # Functionality to add an item
    pass

def edit_item():
    # Functionality to edit an item
    pass

def delete_item():
    # Functionality to delete an item
    pass

def show_items():
    # Functionality to display items
    pass

page = tk.Tk()
page.geometry("800x800")

titre = tk.Label(page, text="Gestion stock by Yassine benmansour", font=('Time New Roman', 30, 'bold'))
titre.grid(row=0, column=3)

l1 = tk.Label(page, text="Produit ID")
l2 = tk.Label(page, text="Categorie")
l3 = tk.Label(page, text="Stock")
l4 = tk.Label(page, text="Prix")

l1.grid(row=1, column=2)
l2.grid(row=2, column=2)
l3.grid(row=3, column=2)
l4.grid(row=4, column=2)

e1 = tk.Entry(page)
e1.grid(row=1, column=3)
e2 = tk.Entry(page)
e2.grid(row=2, column=3)
e3 = tk.Entry(page)
e3.grid(row=3, column=3)
e4 = tk.Entry(page)
e4.grid(row=4, column=3)

col = ("Produit ID", "Categorie", "Stock", "Prix")
listbox = ttk.Treeview(page, columns=col, show='headings')
for x in col:
    listbox.heading(x, text=x)
listbox.grid(row=1, column=0, columnspan=2)
listbox.place(x=9, y=180)

tk.Button(page, text="Ajouter", command='', height=2, width=10).place(x=0, y=450)
tk.Button(page, text="Editer", command='', height=2, width=10).place(x=120, y=450)
tk.Button(page, text="Supprimer", command='', height=2, width=10).place(x=240, y=450)
tk.Button(page, text="Afficher", command='', height=2, width=10).place(x=350, y=450)

page.mainloop()
