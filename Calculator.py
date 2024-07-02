import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.cal = tk.Tk()
        self.cal.title("Calculator") # Set title of the window
        self.cal.geometry("300x400") # Set dimensions of the window
        self.cal.protocol("WM_DELETE_WINDOW", self.close) # Confirm before exiting
        
        # Create a menu bar
        self.menubar = tk.Menu(self.cal)
        self.filename = tk.Menu(self.menubar, tearoff=0)
        self.filename.add_command(label="1.0")                    # Add version changes
        self.menubar.add_cascade(menu=self.filename, label='Ver')
        self.cal.config(menu=self.menubar)
        
        # Create a textbox for input and output
        self.textbox = tk.Entry(self.cal, font=('Arial', 20), borderwidth=5, relief="sunken")
        self.textbox.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        self.result_shown = False
        
        # Define buttons
        buttons = [
            '1', '2', '3', '+',
            '4', '5', '6', '-',
            '7', '8', '9', '*',
            '0', '(', ')', '/',
            '**', 'C', 'DEL', '='
        ]
        
        row_val = 1
        col_val = 0
        
        # Create buttons and place them in the grid
        for button in buttons:
            if button == '=':
                tk.Button(self.cal, text=button, width=10, height=2, command=self.calculate).grid(row=row_val, column=col_val, columnspan=2, padx=5, pady=5, sticky="nsew")
                col_val += 2
            elif button == 'C':
                tk.Button(self.cal, text=button, width=5, height=2, command=self.clear).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
                col_val += 1
            elif button == 'DEL':
                tk.Button(self.cal, text=button, width=5, height=2, command=self.backspace).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
                col_val += 1
            else:
                tk.Button(self.cal, text=button, width=5, height=2, command=lambda b=button: self.add_calculation(b)).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
                col_val += 1
            
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        # Configure rows and columns to have equal size
        for i in range(5):
            self.cal.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.cal.grid_columnconfigure(i, weight=1)

        # Bind keys to the calculator functions
        self.bind_keys()
        
        self.cal.mainloop()
    
    def add_calculation(self, symbol):
        # Add the symbol to the textbox
        if self.result_shown:
            self.textbox.delete(0, tk.END)
            self.result_shown = False
        current = self.textbox.get()
        self.textbox.delete(0, tk.END)
        self.textbox.insert(0, current + symbol)
    
    def calculate(self):
        # Evaluate the expression in the textbox
        try:
            result = eval(self.textbox.get())
            self.textbox.delete(0, tk.END)
            self.textbox.insert(0, str(result))
            self.result_shown = True
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")
            self.textbox.delete(0, tk.END)
    
    def clear(self):
        # Clear the textbox
        self.textbox.delete(0, tk.END)
    
    def backspace(self):
        # Remove the last character from the textbox
        current = self.textbox.get()
        if current:
            self.textbox.delete(0, tk.END)
            self.textbox.insert(0, current[:-1])
    
    def close(self):
        # Confirm before closing the application
        if messagebox.askyesno(title="Exit", message="Do you want to exit?"):
            self.cal.destroy()
    
    def bind_keys(self):
        # Bind keys to the calculator functions
        self.cal.bind('<Return>', lambda event: self.calculate())
        self.cal.bind('<Delete>', lambda event: self.clear())
        self.cal.bind('<BackSpace>', lambda event: self.backspace())
        
        for key in '1234567890()+-*/':
            self.cal.bind(key, lambda event, k=key: self.add_calculation(k))
        
        self.cal.bind('<Shift-Key-8>', lambda event: self.add_calculation('*'))  # For '*' on keyboard
        
        # Keybinding for '**'
        self.cal.bind('<Shift-Key-6>', lambda event: self.add_calculation('**'))  # For '**' on keyboard

Calculator()
