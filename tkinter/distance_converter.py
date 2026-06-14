import tkinter as tk
from tkinter import messagebox


def convert_to_km():
    try:
        miles = float(miles_entry.get())
        km = miles * 1.60934
        km_result_label.config(text=f"{km:.2f} km")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


def convert_to_miles():
    try:
        km = float(km_entry.get())
        miles = km / 1.60934
        miles_result_label.config(text=f"{miles:.2f} miles")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")


root = tk.Tk()
root.title("Distance Converter")
root.geometry("300x200")

frame1 = tk.LabelFrame(root, text="Miles to Kilometers")
frame1.pack(fill="x", padx=15, pady=10)

miles_entry = tk.Entry(frame1, width=10)
miles_entry.pack(side="left", padx=10, pady=10)

miles_label = tk.Label(frame1, text="miles =")
miles_label.pack(side="left", padx=5, pady=10)

km_result_label = tk.Label(frame1, text="0.00 km", font=("Arial", 10, "bold"))
km_result_label.pack(side="left", padx=5, pady=10)

btn1 = tk.Button(frame1, text="Convert", command=convert_to_km)
btn1.pack(side="right", padx=10, pady=10)

frame2 = tk.LabelFrame(root, text="Kilometers to Miles")
frame2.pack(fill="x", padx=15, pady=10)

km_entry = tk.Entry(frame2, width=10)
km_entry.pack(side="left", padx=10, pady=10)

km_label = tk.Label(frame2, text="km =")
km_label.pack(side="left", padx=5, pady=10)

miles_result_label = tk.Label(
    frame2, text="0.00 miles", font=("Arial", 10, "bold")
)
miles_result_label.pack(side="left", padx=5, pady=10)

btn2 = tk.Button(frame2, text="Convert", command=convert_to_miles)
btn2.pack(side="right", padx=10, pady=10)

root.mainloop()