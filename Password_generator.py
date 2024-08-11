import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, user_word=""):
    # Ensure the user-provided word fits within the specified length
    if len(user_word) > length:
        return None

    # Calculate remaining length needed after including the user's word
    remaining_length = length - len(user_word)

    # Define the characters to include in the password: digits and special characters
    characters = string.digits + string.punctuation

    # Generate the remaining part of the password
    random_part = ''.join(random.choice(characters) for _ in range(remaining_length))

    # Combine the user's word with the random part
    password = user_word + random_part

    return password

def generate_password_gui():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Invalid Input", "Password length must be at least 1.")
            return
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")
        return

    user_word = word_entry.get()
    password = generate_password(length, user_word)

    if password:
        password_var.set(password)
    else:
        messagebox.showerror("Invalid Input", "The provided word is longer than the desired password length.")

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Set up the GUI window
window = tk.Tk()
window.title("Password Generator")

# Create input fields and labels
tk.Label(window, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(window)
length_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(window, text="Word to Include:").grid(row=1, column=0, padx=10, pady=10)
word_entry = tk.Entry(window)
word_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a button to generate the password
generate_button = tk.Button(window, text="Generate Password", command=generate_password_gui)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Display the generated password
password_var = tk.StringVar()
password_label = tk.Label(window, textvariable=password_var, font=("Arial", 12, "bold"))
password_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Create a button to copy the password to the clipboard
copy_button = tk.Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI loop
window.mainloop()
