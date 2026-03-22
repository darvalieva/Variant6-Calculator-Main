import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Ошибка")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.geometry("400x500")
root.title("Калькулятор - Вариант 6")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

frame = tk.Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

i = 0
for btn in buttons:
    b = tk.Button(frame, text=btn, font="lucida 15 bold", width=5, height=2)
    b.grid(row=i//4, column=i%4, padx=5, pady=5)
    b.bind("<Button-1>", click)
    i += 1

root.mainloop()