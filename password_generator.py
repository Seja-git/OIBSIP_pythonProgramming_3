import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip  

# --------- Functions ---------
def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError

        characters = ""
        if letters_var.get():
            characters += string.ascii_letters
        if numbers_var.get():
            characters += string.digits
        if symbols_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Password length must be a positive number.")

def copy_to_clipboard():
    pwd = password_var.get()
    if pwd:
        pyperclip.copy(pwd)
        messagebox.showinfo("Copied", "✅ Password copied to clipboard!")

# --------- GUI ---------
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("500x350")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", font=("Arial", 11))
style.configure("TLabel", font=("Arial", 11))

# Main Frame
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Title
ttk.Label(main_frame, text="Secure Password Generator", font=("Arial", 18, "bold")).pack(pady=10)

# Length
length_frame = ttk.Frame(main_frame)
length_frame.pack(pady=5, fill="x")
ttk.Label(length_frame, text="Password Length:").pack(side="left")
length_var = tk.StringVar(value="12")
ttk.Entry(length_frame, textvariable=length_var, width=5).pack(side="left", padx=5)

# Character types
options_frame = ttk.LabelFrame(main_frame, text="Include Characters", padding=10)
options_frame.pack(pady=10, fill="x")

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=False)

ttk.Checkbutton(options_frame, text="Letters (A-Z, a-z)", variable=letters_var).pack(anchor="w", pady=2)
ttk.Checkbutton(options_frame, text="Numbers (0-9)", variable=numbers_var).pack(anchor="w", pady=2)
ttk.Checkbutton(options_frame, text="Symbols (!, @, #...)", variable=symbols_var).pack(anchor="w", pady=2)

# Generate button
generate_btn = tk.Button(main_frame, text="Generate Password", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", command=generate_password)
generate_btn.pack(pady=10, fill="x")

# Output + Copy button
output_frame = ttk.Frame(main_frame)
output_frame.pack(pady=10, fill="x")

password_var = tk.StringVar()
password_entry = ttk.Entry(output_frame, textvariable=password_var, font=("Consolas", 14),
                           state="readonly", width=32, justify="center")
password_entry.pack(side="left", padx=5)

copy_button = tk.Button(output_frame, text="📋 Copy", font=("Arial", 11, "bold"),
                        bg="#2196F3", fg="white", command=copy_to_clipboard)
copy_button.pack(side="left", padx=5)

root.mainloop()
