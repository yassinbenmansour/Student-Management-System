from tkinter import *
#import mysql.connector as mysql
#from tkinter import ttk,messagebox

page = Tk()
page.geometry("800x800")

titre = Label(page,text="Gestion stock by Yassine benmansour", font=('Time New Roman',30 , 'bold')).grid(row=0 , column=3)

l1 = Label(page, text="Produit ID")
l2 = Label(page, text="Categorie")
l3 = Label(page, text="Stock")
l4 = Label(page, text="Prix")


l1.grid(row=1 , column=2)
l2.grid(row=2 , column=2)
l3.grid(row=3 , column=2)
l4.grid(row=4 , column=2)





page.mainloop()