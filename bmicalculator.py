import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        age = int(age_entry.get())
        gender = gender_var.get()
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        bmi = weight / (height * height)
        result_label.config(text="Your BMI: {:.2f}".format(bmi))

        if gender == "Male":
            if bmi < 18.5:
                interpretation_label.config(text="Interpretation: you are Underweight")
            elif 18.5 <= bmi < 24.9:
                interpretation_label.config(text="Interpretation: you are Normal weight")
            elif 25 <= bmi < 30:
                interpretation_label.config(text="Interpretation: you are Overweight")
            else:
                interpretation_label.config(text="Interpretation: you are Obese")
        else:
            if bmi < 18.5:
                interpretation_label.config(text="Interpretation: you are Underweight")
            elif 18.5 <= bmi < 24.9:
                interpretation_label.config(text="Interpretation: you are Normal weight")
            elif 25 <= bmi < 30:
                interpretation_label.config(text="Interpretation: you are Overweight")
            else:
                interpretation_label.config(text="Interpretation: you are Obese")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values for age, weight, and height.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create labels and entries for age, gender, weight, and height
age_label = tk.Label(root, text="Age:")
age_label.grid(row=0, column=0, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.grid(row=0, column=1, padx=10, pady=5)

gender_label = tk.Label(root, text="Gender:")
gender_label.grid(row=1, column=0, padx=10, pady=5)
gender_var = tk.StringVar(root)
gender_var.set("select")
gender_menu = tk.OptionMenu(root, gender_var, "Male", "Female")
gender_menu.grid(row=1, column=1, padx=10, pady=5)

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=2, column=0, padx=10, pady=5)
weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1, padx=10, pady=5)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=3, column=0, padx=10, pady=5)
height_entry = tk.Entry(root)
height_entry.grid(row=3, column=1, padx=10, pady=5)

# Create button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create labels to display BMI result and interpretation
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2)

interpretation_label = tk.Label(root, text="")
interpretation_label.grid(row=6, column=0, columnspan=2)

# Start the Tkinter event loop
root.mainloop()
