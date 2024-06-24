# imports
import tkinter as tk

# variable to store the equation in string format
calculate = ""


# GUI class
class GUI:
    def __init__(self):
        self.root = tk.Tk()

        # geometry
        self.root.geometry("530x500")
        self.root.title("Calculator")

        # result textbox
        self.result = tk.Text(self.root, height=2, width=35, font=('Arial', 20))
        self.result.grid(columnspan=5)

        self.root.bind('<KeyPress>', self.on_key_press)


        # button 1
        self.btn1 = tk.Button(text="1", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation(1))
        self.btn1.grid(row=2, column=0, pady=20)
        # button 2
        self.btn2 = tk.Button(text="2", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation(2))
        self.btn2.grid(row=2, column=1, pady=20)
        # button 3
        self.btn3 = tk.Button(text="3", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation(3))
        self.btn3.grid(row=2, column=2, pady=20)
        # button 4
        self.btn4 = tk.Button(text="4", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation(4))
        self.btn4.grid(row=3, column=0, pady=20)
        # button 5
        self.btn5 = tk.Button(text="5", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation(5))
        self.btn5.grid(row=3, column=1, pady=20)
        # button 6
        self.btn6 = tk.Button(text="6", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation(6))
        self.btn6.grid(row=3, column=2, pady=20)
        # button 7
        self.btn7 = tk.Button(text="7", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation(7))
        self.btn7.grid(row=4, column=0, pady=20)
        # button 8
        self.btn8 = tk.Button(text="8", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation(8))
        self.btn8.grid(row=4, column=1, pady=20)
        # button 9
        self.btn9 = tk.Button(text="9", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation(9))
        self.btn9.grid(row=4, column=2, pady=20)
        # add button
        self.add_btn = tk.Button(text="+", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation("+"))
        self.add_btn.grid(row=2, column=3, pady=20)
        # subtract button
        self.subtract_btn = tk.Button(text="-", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation("-"))
        self.subtract_btn.grid(row=3, column=3, pady=20)
        # multiply button 3
        self.multiply_btn = tk.Button(text="*", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation("*"))
        self.multiply_btn.grid(row=4, column=3, pady=20)
        # divide button
        self.divide_btn = tk.Button(text="/", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation("/"))
        self.divide_btn.grid(row=5, column=3, pady=20)
        # clear button
        self.clear_btn = tk.Button(text="Clear", font=('Arial', 18), width=5, command=self.clear)
        self.clear_btn.grid(row=5, column=0, pady=20)
        # decimal button
        self.decimal_btn = tk.Button(text=".", font=('Arial', 18), width=5, command=lambda: self.add_to_calculation("."))
        self.decimal_btn.grid(row=5, column=1, pady=20)
        # equals button
        self.equals_btn = tk.Button(text="=", font=('Arial', 18), width=5, command=self.evaluate_equation)
        self.equals_btn.grid(row=5, column=2, pady=20)

        self.root.mainloop()

    # adds the number to existing calculation
    def add_to_calculation(self, symbol):
        global calculate
        calculate += str(symbol)
        self.result.delete('1.0', tk.END)
        self.result.insert('1.0', calculate)

    # evaluate the equation in the variable
    def evaluate_equation(self):
        global calculate
        calculate = str(eval(calculate))
        self.result.delete('1.0', tk.END)
        self.result.insert('1.0', calculate)

    # keyboard input
    def on_key_press(self, event):
        self.result.insert('end', (event.char, ))

    # clears the text field
    def clear(self):
        global calculate
        calculate = ""
        self.result.delete('1.0', tk.END)
        print(calculate)


GUI()
