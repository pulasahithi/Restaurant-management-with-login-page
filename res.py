import tkinter as tk
from tkinter import messagebox

# Main restaurant management system
def restaurant_system():
    def calculate_bill():
        total = 0
        if biryani_var.get():
            total += int(biryani_qty.get()) * 200
        if burger_var.get():
            total += int(burger_qty.get()) * 150
        if drink_var.get():
            total += int(drink_qty.get()) * 30
        bill_label.config(text=f"Total Bill: ₹{total}")

    # Clear login window and create the main system
    login_window.destroy()
    system_window = tk.Tk()
    system_window.title("Restaurant Management System")

    # Menu
    tk.Label(system_window, text="Menu", font=("Arial", 16, "bold")).grid(row=0, column=1, pady=10)
    tk.Label(system_window, text="Biryani - ₹200").grid(row=1, column=0, padx=10)
    tk.Label(system_window, text="Burger - ₹100").grid(row=2, column=0, padx=10)
    tk.Label(system_window, text="Drink - ₹50").grid(row=3, column=0, padx=10)

    # Variables for checkboxes and quantities
    biryani_var = tk.BooleanVar()
    burger_var = tk.BooleanVar()
    drink_var = tk.BooleanVar()
    biryani_qty = tk.StringVar(value="0")
    burger_qty = tk.StringVar(value="0")
    drink_qty = tk.StringVar(value="0")

    # Menu Checkboxes and Quantity Inputs
    tk.Checkbutton(system_window, text="Biryani", variable=biryani_var).grid(row=1, column=1)
    tk.Entry(system_window, textvariable=biryani_qty, width=5).grid(row=1, column=2)
    tk.Checkbutton(system_window, text="Burger", variable=burger_var).grid(row=2, column=1)
    tk.Entry(system_window, textvariable=burger_qty, width=5).grid(row=2, column=2)
    tk.Checkbutton(system_window, text="Drink", variable=drink_var).grid(row=3, column=1)
    tk.Entry(system_window, textvariable=drink_qty, width=5).grid(row=3, column=2)

    # Total Bill Section
    bill_label = tk.Label(system_window, text="Total Bill: ₹0", font=("Arial", 14))
    bill_label.grid(row=4, column=1, pady=10)
    tk.Button(system_window, text="Calculate Bill", command=calculate_bill).grid(row=5, column=1)

    system_window.mainloop()

# Login Function
def check_login():
    username = username_entry.get()
    password = password_entry.get()

    # Dummy credentials
    if username == "admin" and password == "password":
        restaurant_system()
    else:
        messagebox.showerror("Error", "Invalid username or password")

# Login Page
login_window = tk.Tk()
login_window.title("Login Page")

tk.Label(login_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
username_entry = tk.Entry(login_window)
username_entry.grid(row=0, column=1, padx=10)

tk.Label(login_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
password_entry = tk.Entry(login_window, show="*")
password_entry.grid(row=1, column=1, padx=10)

tk.Button(login_window, text="Login", command=check_login).grid(row=2, column=0, columnspan=2, pady=10)

login_window.mainloop()
#username:admin
#password:password