import tkinter as tk
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime

window = tk.Tk()
window.title("Invoice Builder")
window.geometry("1000x500")

productList = []
products = ["Refrigerator", "TV", "Waching Machine","Oven","Juicer","Grinder","Water Heater","Vaccum Cleaner"]  # Example product names
quantities = [1, 2, 3, 4, 5]  # Example quantities

def generateInvoice():
    n = name_var.get()
    a = add_var.get()
    p = phone_var.get()
    total = sum(item[3] for item in productList)
    doc = DocxTemplate("JS.docx")
    doc.render({"name": n, "address": a, "phone": p, "itemList": productList, "total": total})
    fileName = n + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
    doc.save(fileName)
    reset()

def addProduct():
    n = pName_var.get()
    q = pQty_var.get()
    p = pricePerUnit_var.get()
    t = q * p
    table.insert("", 0, values=(n, q, p, t))
    productList.append([n, q, p, t])
    clearProductfield()

def clearProductfield():
    pName_var.set("")
    pQty_var.set(quantities[0])
    pricePerUnit_var.set(0.0)

def reset():
    clearProductfield()
    name_var.set("")
    add_var.set("")
    phone_var.set("")
    table.delete(*table.get_children())
    productList.clear()

name_label = ttk.Label(window, text="Full Name")
name_label.grid(row=0, column=0)
name_var = tk.StringVar()
name_entry = ttk.Entry(window, textvariable=name_var)
name_entry.grid(row=1, column=0)

add_label = ttk.Label(window, text="Full Address")
add_label.grid(row=0, column=1)
add_var = tk.StringVar()
add_entry = ttk.Entry(window, textvariable=add_var)
add_entry.grid(row=1, column=1)

phone_label = ttk.Label(window, text="Phone Number")
phone_label.grid(row=0, column=2)
phone_var = tk.StringVar()
phone_entry = ttk.Entry(window, textvariable=phone_var)
phone_entry.grid(row=1, column=2)

pName_label = ttk.Label(window, text="Product Name")
pName_label.grid(row=3, column=0)
pName_var = tk.StringVar()
product_dropdown = ttk.Combobox(window, textvariable=pName_var, values=products)
product_dropdown.grid(row=4, column=0)

pQty_label = ttk.Label(window, text="Quantity")
pQty_label.grid(row=3, column=1)
pQty_var = tk.IntVar(value=quantities[0])
quantity_dropdown = ttk.Combobox(window, textvariable=pQty_var, values=quantities)
quantity_dropdown.grid(row=4, column=1)

pricePerUnit_label = ttk.Label(window, text="Price per unit")
pricePerUnit_label.grid(row=3, column=2)
pricePerUnit_var = tk.DoubleVar()
pricePerUnit_entry = ttk.Entry(window, textvariable=pricePerUnit_var)
pricePerUnit_entry.grid(row=4, column=2)

add_button = ttk.Button(window, text="Add Product", command=addProduct)
add_button.grid(row=5, column=2, columnspan=3)

table = ttk.Treeview(window, columns=("name", "quantity", "price", "total"), show="headings")
table.grid(row=6, column=0, columnspan=3, sticky="ewns", padx=50)
table.heading("name", text="Name", anchor="w")
table.heading("quantity", text="Quantity", anchor="w")
table.heading("price", text="Price", anchor="w")
table.heading("total", text="Total", anchor="w")

new_button = ttk.Button(window, text="New Invoice", command=reset)
new_button.grid(row=7, column=1)

generate_button = ttk.Button(window, text="Generate Invoice", command=generateInvoice)
generate_button.grid(row=7, column=2)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=6)
window.rowconfigure(7, weight=1)
window.rowconfigure(8, weight=1)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.mainloop()