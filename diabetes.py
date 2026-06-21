import tkinter as tk
from tkinter import messagebox
import csv
import math

cols = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", 
        "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]

def calculate():
    # Check if empty
    for i in range(8):
        if entries[i].get().strip() == "":
            messagebox.showerror("Error", "You missed a field!")
            return
    
    if k_input.get().strip() == "":
        messagebox.showerror("Error", "Enter K value!")
        return

    # Convert patient inputs and check ranges
    try:
        user_data = []
        for i in range(8):
            val = float(entries[i].get())
            
            if val < dataset_mins[i] or val > dataset_maxs[i]:
                messagebox.showerror("Error", cols[i] + " must be between " + str(dataset_mins[i]) + " and " + str(dataset_maxs[i]))
                return
            user_data.append(val)
    except:
        messagebox.showerror("Error", "Patient data fields must be numbers!")
        return

    try:
        k = int(k_input.get())
        if k < 1 or k > len(data):
            messagebox.showerror("Error", "K must be between 1 and " + str(len(data)) + "!")
            return
    except:
        messagebox.showerror("Error", "K must be a valid whole number!")
        return

    # Normalize the input
    norm_user = []
    for i in range(8):
        n_val = (user_data[i] - dataset_mins[i]) / (dataset_maxs[i] - dataset_mins[i])
        norm_user.append(n_val)

    # Find distance to every row
    distances = []
    for row in normalized_data:
        d_sum = 0
        for i in range(8):
            d_sum += (norm_user[i] - row[i])**2
        dist = math.sqrt(d_sum)
        
        distances.append([dist, row[8]])

    # Sort and find k closest
    distances.sort() 
    closest_k = distances[:k]
    
    diabetic_count = 0
    for item in closest_k:
        if item[1] == 1.0: # 1 means diabetic
            diabetic_count += 1
            
    prob = (diabetic_count / k) * 100
    messagebox.showinfo("Result", "Probability is: " + str(prob) + "%\n" + str(diabetic_count) + " out of " + str(k) + " neighbors are diabetic.")


# Read the file
data = []
f = open("C:\\Users\olcay\Downloads\diabetes.csv", "r")
lines = f.readlines()
f.close()

# Skip header and split by comma
for l in lines[1:]:
    parts = l.strip().split(",")
    temp = []
    for p in parts:
        temp.append(float(p))
    data.append(temp)

# Get mins and maxs
dataset_mins = []
dataset_maxs = []
for i in range(8):
    column_vals = []
    for row in data:
        column_vals.append(row[i])
    dataset_mins.append(min(column_vals))
    dataset_maxs.append(max(column_vals))

# Preprocess the data
normalized_data = []
for row in data:
    new_row = []
    for i in range(8):
        norm_v = (row[i] - dataset_mins[i]) / (dataset_maxs[i] - dataset_mins[i])
        new_row.append(norm_v)
    new_row.append(row[8]) # Add outcome
    normalized_data.append(new_row)

# Save the file
f2 = open("diabetes_preprocessed.csv", "w")
f2.write("Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DPF,Age,Outcome\n")
for r in normalized_data:
    line = ""
    for val in r:
        line += str(val) + ","
    f2.write(line[:-1] + "\n") # remove last comma
f2.close()

# GUI Part
root = tk.Tk()
root.title("Diabetes Probability Calc")

entries = []
for i in range(8):
    # Show min and max in labels for the user 
    label_text = cols[i] + " (" + str(dataset_mins[i]) + "-" + str(dataset_maxs[i]) + ")"
    tk.Label(root, text=label_text).grid(row=i, column=0, padx=10, pady=5, sticky="w")
    e = tk.Entry(root)
    e.grid(row=i, column=1, padx=10, pady=5)
    entries.append(e)

# K input field
tk.Label(root, text="K value (1-" + str(len(data)) + "):").grid(row=8, column=0, padx=10, pady=5, sticky="w")
k_input = tk.Entry(root)
k_input.insert(0, "5")
k_input.grid(row=8, column=1, padx=10, pady=5)

tk.Button(root, text="Calculate Probability", command=calculate).grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()