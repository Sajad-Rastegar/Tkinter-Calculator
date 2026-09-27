import tkinter as tk


win = tk.Tk()
win.title("Calculator")


def get_numbers():
    try:
        x = float(entry_number1.get())
        y = float(entry_number2.get())
        return x, y

    except ValueError:
        result.set("Enter valid numbers")
        return None


def add():
    numbers = get_numbers()

    if numbers:
        x, y = numbers
        result.set(x + y)


def subtract():
    numbers = get_numbers()

    if numbers:
        x, y = numbers
        result.set(x - y)


def multiply():
    numbers = get_numbers()

    if numbers:
        x, y = numbers
        result.set(x * y)


def divide():
    numbers = get_numbers()

    if numbers:
        x, y = numbers

        if y == 0:
            result.set("Cannot divide by zero")
        else:
            result.set(x / y)


result = tk.StringVar()


tk.Label(win, text="Number 1").grid(
    column=0, row=0, padx=5, pady=5
)

tk.Label(win, text="Number 2").grid(
    column=0, row=1, padx=5, pady=5
)


entry_number1 = tk.Entry(win)
entry_number1.grid(
    column=1, row=0, padx=5, pady=5
)

entry_number2 = tk.Entry(win)
entry_number2.grid(
    column=1, row=1, padx=5, pady=5
)


tk.Button(win, text="+", command=add).grid(
    column=2, row=0, padx=5, pady=5
)

tk.Button(win, text="-", command=subtract).grid(
    column=2, row=1, padx=5, pady=5
)

tk.Button(win, text="*", command=multiply).grid(
    column=3, row=0, padx=5, pady=5
)

tk.Button(win, text="/", command=divide).grid(
    column=3, row=1, padx=5, pady=5
)


tk.Label(win, textvariable=result).grid(
    column=1, row=2, columnspan=2, padx=5, pady=10
)


tk.Button(
    win,
    text="Exit",
    command=win.destroy
).grid(
    column=0, row=2, padx=5, pady=5
)


win.mainloop()