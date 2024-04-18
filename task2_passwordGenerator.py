import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        # Initialize the root window and set its title
        self.root = root
        self.root.title("Password Generator")
        
        # Initialize variables for password length and character types
        self.length_var = tk.IntVar(value="")
        self.use_letters_var = tk.BooleanVar()
        self.use_numbers_var = tk.BooleanVar()
        self.use_symbols_var = tk.BooleanVar()
        self.use_uppercase_var = tk.BooleanVar()
        self.use_lowercase_var = tk.BooleanVar()
        self.security_var = tk.BooleanVar(value=False)
        
        # Create GUI elements
        self.create_widgets()
    
    def create_widgets(self):
        # Create a main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Create a label and entry for password length
        length_label = ttk.Label(main_frame, text="Password Length:")
        length_label.grid(row=0, column=0, sticky="w")
        length_entry = ttk.Entry(main_frame, textvariable=self.length_var)
        length_entry.grid(row=0, column=1, sticky="w", padx=5)
        
        # Create a label frame for character types
        complexity_frame = ttk.LabelFrame(main_frame, text="Include")
        complexity_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)
        
        # Create checkbuttons for character types
        letters_check = ttk.Checkbutton(complexity_frame, text="Letters", variable=self.use_letters_var)
        letters_check.grid(row=0, column=0, sticky="w")
        numbers_check = ttk.Checkbutton(complexity_frame, text="Numbers", variable=self.use_numbers_var)
        numbers_check.grid(row=1, column=0, sticky="w")
        symbols_check = ttk.Checkbutton(complexity_frame, text="Symbols", variable=self.use_symbols_var)
        symbols_check.grid(row=2, column=0, sticky="w")
        uppercase_check = ttk.Checkbutton(complexity_frame, text="Uppercase", variable=self.use_uppercase_var)
        uppercase_check.grid(row=3, column=0, sticky="w")
        lowercase_check = ttk.Checkbutton(complexity_frame, text="Lowercase", variable=self.use_lowercase_var)
        lowercase_check.grid(row=4, column=0, sticky="w")
        
        # Create a checkbutton for security rules
        security_check = ttk.Checkbutton(main_frame, text="Adhere to security rules (avoid ambiguous characters)", variable=self.security_var)
        security_check.grid(row=2, column=0, columnspan=2, sticky="w")
        
        # Create a button to generate password
        generate_button = ttk.Button(main_frame, text="Generate Password", command=self.generate_password)
        generate_button.grid(row=3, column=0, columnspan=2, pady=10)
        
        # Create an entry to display generated password
        self.password_var = tk.StringVar()
        password_entry = ttk.Entry(main_frame, textvariable=self.password_var, state="readonly", width=30)
        password_entry.grid(row=4, column=0, columnspan=2, pady=5)
        
        # Create a button to copy password to clipboard
        copy_button = ttk.Button(main_frame, text="Copy to Clipboard", command=self.copy_password)
        copy_button.grid(row=5, column=0, columnspan=2, pady=5)
    
    def generate_password(self):
        # Retrieve values of variables
        length = self.length_var.get()
        use_letters = self.use_letters_var.get()
        use_numbers = self.use_numbers_var.get()
        use_symbols = self.use_symbols_var.get()
        use_uppercase=self.use_uppercase_var.get()
        use_lowercase=self.use_lowercase_var.get()
        security_rules = self.security_var.get()
        
        # Define character sets
        letters = string.ascii_letters if use_letters else ''
        numbers = string.digits if use_numbers else ''
        symbols = string.punctuation if use_symbols else ''
        uppercase = string.ascii_uppercase if use_uppercase else ''
        lowercase = string.ascii_lowercase if use_lowercase else ''
        
        # Apply security rules to character sets
        if security_rules:
            ambiguous_characters = "il1Lo0O"
            letters = ''.join(filter(lambda x: x not in ambiguous_characters, letters))
            numbers = ''.join(filter(lambda x: x not in ambiguous_characters, numbers))
            symbols = ''.join(filter(lambda x: x not in ambiguous_characters, symbols))
            uppercase = ''.join(filter(lambda x: x not in ambiguous_characters, uppercase))
            lowercase = ''.join(filter(lambda x: x not in ambiguous_characters, lowercase))
        
        # Concatenate all character sets
        all_chars = letters + numbers + symbols + uppercase + lowercase
        
        # Check if any character type is selected
        if not all_chars:
            self.password_var.set("Please select at least one character type.")
            return
        
        # Generate password
        password = ''.join(random.choice(all_chars) for _ in range(length))
        self.password_var.set(password)
    
    def copy_password(self):
        # Copy password to clipboard
        password = self.password_var.get()
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()  # Ensure clipboard is updated

def main():
    # Create the root window and start the application
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
