import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


def submit_form():
    name = name_entry.get()
    member_status = "Yes" if is_member.get() else "No"
    notification_type = notification_var.get()
    country = country_box.get()

    if not name:
        messagebox.showwarning("Warning", "Please enter your name!")
        return

    summary = (
        f"Name: {name}\n"
        f"Member: {member_status}\n"
        f"Notifications: {notification_type}\n"
        f"Country: {country}"
    )
    messagebox.showinfo("Submission Successful", summary)


#Initialize the main window
window = tk.Tk()
window.title("Widget Showcase")
window.geometry("400x450")

#Label and Entry Widget
name_label = tk.Label(window, text="Full Name:", font=("Arial", 10, "bold"))
name_label.pack(pady=(20, 2))

name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)

#Checkbutton Widget
is_member = tk.BooleanVar()
member_check = tk.Checkbutton(
    window, text="Subscribe to Newsletter?", variable=is_member
)
member_check.pack(pady=10)

#Radiobutton Widgets
notification_var = tk.StringVar(value="Email")

radio_label = tk.Label(
    window, text="Preferred Contact Method:", font=("Arial", 10, "bold")
)
radio_label.pack(pady=(10, 2))

radio1 = tk.Radiobutton(
    window, text="Email", variable=notification_var, value="Email"
)
radio2 = tk.Radiobutton(
    window, text="SMS", variable=notification_var, value="SMS"
)
radio3 = tk.Radiobutton(
    window, text="None", variable=notification_var, value="None"
)

radio1.pack()
radio2.pack()
radio3.pack()

#Combobox Widget (Dropdown)
dropdown_label = tk.Label(window, text="Country:", font=("Arial", 10, "bold"))
dropdown_label.pack(pady=(15, 2))

countries = ["Greece", "Bulgaria", "France", "Italy", "Other"]
country_box = ttk.Combobox(window, values=countries, state="readonly")
country_box.set("Greece")
country_box.pack(pady=5)

#Button Widget
submit_btn = tk.Button(
    window, text="Submit", command=submit_form, bg="#4CAF50", fg="white", width=15
)
submit_btn.pack(pady=30)

#Start the application loop
window.mainloop()