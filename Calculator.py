
import tkinter as tk


window = tk.Tk()
window.title("Calculator")
window.geometry("350x500")
window.resizable(False, False)
window.configure(bg="#1e1e1e")


expression = ""

calc_label = tk.Label(
    window,
    font=("Arial", 18),
    bg="#1e1e1e",
    fg="#4683B7",
    text="Calculus",
)
calc_label.pack(pady=10)


display = tk.Entry(
    window,
    font=("Arial", 24),
    bg="#1D2951",
    fg="white",
    insertbackground="white",
    justify="right",
    bd=0
)
display.pack(
    fill="x",
    padx=15,
    pady=20,
    ipady=20
)


def validate_input(event):
    if event.char.isdigit() or event.keysym in (
        "BackSpace", "Delete", "Left", "Right"
    ):
        return None
    return "break"


def sync_expression(event):
    global expression
    expression = display.get()


display.bind("<Key>", validate_input)
display.bind("<KeyRelease>", sync_expression)


def button_click(value):
    global expression

    expression += str(value)

    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def clear():
    global expression

    expression = ""
    display.delete(0, tk.END)


def backspace():
    global expression

    expression = expression[:-1]

    display.delete(0, tk.END)
    display.insert(tk.END, expression)


def calculate():
    global expression
    try:
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(tk.END, str(result))
        expression = str(result)

    except:
        display.delete(0, tk.END)
        display.insert(tk.END, "ERROR")
        expression = ""


buttons = [
    ["1", "6", "7", "+"],
    ["2", "5", "8", "-"],
    ["3", "4", "9", "*"],
    [".", "0", "=", "/"]
]


button_frame = tk.Frame(
    window,
    bg="#1D2951"
)
button_frame.pack(
    expand=True,
    fill="both",
    padx=10,
    pady=5
)



backspace_button = tk.Button(
    button_frame,
    text="⌫",
    font=("Arial", 15, "bold"),
    bg="#4683B7",
    fg="white",
    bd=0,
    command=backspace
)

backspace_button.grid(
    row=0,
    column=0,
    columnspan=2,
    sticky="nsew",
    padx=4,
    pady=4
)


clear_button = tk.Button(
    button_frame,
    text="C",
    font=("Arial", 15, "bold"),
    bg="#4683B7",
    fg="white",
    bd=0,
    command=clear
)

clear_button.grid(
    row=0,
    column=2,
    columnspan=2,
    sticky="nsew",
    padx=4,
    pady=4
)


for row_index, row in enumerate(buttons, start=1):

    for col_index, value in enumerate(row):

        if value == "=":
            command = calculate
            color = "#4683B7"

        elif value in ["+", "-", "*", "/"]:
            command = lambda v=value: button_click(v)
            color = "#4683B7"

        else:
            command = lambda v=value: button_click(v)
            color = "#1D2951"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 18, "bold"),
            bg=color,
            fg="white",
            bd=0,
            command=command
        )

        button.grid(
            row=row_index,
            column=col_index,
            sticky="nsew",
            padx=4,
            pady=4
        )


for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)


window.mainloop()
