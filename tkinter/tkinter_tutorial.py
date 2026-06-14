import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 25))
my_label.pack()

my_label.config(text="New Text")

#Button
def button_clicked():
    print("I got clicked!")
    print(input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#Entry

input = tkinter.Entry(width=10)
input.pack()


window.mainloop()
