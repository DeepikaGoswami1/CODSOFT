from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog as simpledialog

# Contact list to store dictionaries
contacts = []

# Function to add contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return
    
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", "Contact added!")
    clear_entries()
    view_contacts()

# Function to view contacts
def view_contacts():
    contact_list.delete(0, END)
    for contact in contacts:
        contact_list.insert(END, f"{contact['name']} - {contact['phone']}")

# Function to search contact
def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contact_list.insert(END, f"{contact['name']} - {contact['phone']}")

# Function to update selected contact
def update_contact():
    index = contact_list.curselection()
    if not index:
        messagebox.showwarning("Select Contact", "Please select a contact to update")
        return

    idx = index[0]
    contact = contacts[idx]

    # Get new data
    new_name = simpledialog.askstring("Update", "Enter new name:", initialvalue=contact["name"])
    new_phone = simpledialog.askstring("Update", "Enter new phone:", initialvalue=contact["phone"])
    new_email = simpledialog.askstring("Update", "Enter new email:", initialvalue=contact["email"])
    new_address = simpledialog.askstring("Update", "Enter new address:", initialvalue=contact["address"])

    if new_name and new_phone:
        contacts[idx] = {
            "name": new_name,
            "phone": new_phone,
            "email": new_email,
            "address": new_address
        }
        messagebox.showinfo("Updated", "Contact updated successfully!")
        view_contacts()
    else:
        messagebox.showerror("Error", "Name and Phone cannot be empty!")

# Function to delete selected contact
def delete_contact():
    index = contact_list.curselection()
    if not index:
        messagebox.showwarning("Select Contact", "Please select a contact to delete")
        return

    confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this contact?")
    if confirm:
        contacts.pop(index[0])
        messagebox.showinfo("Deleted", "Contact deleted!")
        view_contacts()

# Function to clear input fields
def clear_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

# GUI Setup
root = Tk()
root.title("Contact Book")
root.geometry("500x600")
root.config(bg="#f0f0f0")

# Input Fields
Label(root, text="Name").pack()
name_entry = Entry(root, width=40)
name_entry.pack()

Label(root, text="Phone").pack()
phone_entry = Entry(root, width=40)
phone_entry.pack()

Label(root, text="Email").pack()
email_entry = Entry(root, width=40)
email_entry.pack()

Label(root, text="Address").pack()
address_entry = Entry(root, width=40)
address_entry.pack()

Button(root, text="Add Contact", command=add_contact, bg="lightgreen").pack(pady=5)

# Search
Label(root, text="Search by Name or Phone").pack()
search_entry = Entry(root, width=30)
search_entry.pack()
Button(root, text="Search", command=search_contact).pack(pady=5)

# Contact List
Label(root, text="Contact List").pack()
contact_list = Listbox(root, width=60, height=10)
contact_list.pack(pady=10)

# Update and Delete Buttons
Button(root, text="Update Selected", command=update_contact, bg="lightblue").pack(pady=5)
Button(root, text="Delete Selected", command=delete_contact, bg="red").pack(pady=5)

# View All Button
Button(root, text="View All Contacts", command=view_contacts).pack(pady=10)

root.mainloop()
   


