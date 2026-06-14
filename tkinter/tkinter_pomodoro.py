import tkinter as tk
from tkinter import messagebox

timer = None
time_left = 1500
is_working = True

def countdown():
    global time_left, timer
    canvas.itemconfig(timer_text, text=f"{time_left // 60:02d}:{time_left % 60:02d}")
    if time_left > 0:
        time_left -= 1
        timer = window.after(1000, countdown)
    else:
        switch_mode()

def switch_mode():
    global is_working, time_left
    is_working = not is_working
    time_left = 300 if not is_working else 1500
    lbl.config(text="Break Time!" if not is_working else "Focus Time!", fg="#1E4620")
    messagebox.showinfo("Timer", "Time is up!")
    countdown()

def start():
    btn_start.config(state="disabled")
    countdown()

def reset():
    if timer:
        window.after_cancel(timer)
    global time_left, is_working
    time_left, is_working = 1500, True
    lbl.config(text="Focus Time!", fg="#D90429")
    canvas.itemconfig(timer_text, text="25:00")
    btn_start.config(state="normal")

window = tk.Tk()
window.title("Pomodoro Timer")
window.geometry("350x400")
window.config(bg="#93C572")

lbl = tk.Label(window, text="Focus Time!", font=("Arial", 28, "bold"), bg="#93C572", fg="#D90429")
lbl.pack(pady=20)

canvas = tk.Canvas(window, width=200, height=180, bg="#93C572", highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 60, image=tomato_img)
timer_text = canvas.create_text(100, 150, text="25:00", font=("Arial", 32, "bold"), fill="#1E4620")
canvas.pack()

btn_start = tk.Button(window, text="Start", font=("Arial", 14, "bold"), bg="#1E4620", fg="white", command=start)
btn_start.pack(side="left", padx=50, pady=20)

btn_reset = tk.Button(window, text="Reset", font=("Arial", 14, "bold"), bg="#D90429", fg="white", command=reset)
btn_reset.pack(side="right", padx=50, pady=20)

window.mainloop()