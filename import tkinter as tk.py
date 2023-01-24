import tkinter as tk

def calculate_liquidation():
    salary = float(salary_entry.get())
    seniority = int(seniority_entry.get())
    liquidation = int(salary * seniority)
    liquidation_label.config(text=f"La liquidación es: {liquidation}")

root = tk.Tk()
root.title("Cálculo de liquidación laboral")

salary_label = tk.Label(root, text="Ingrese el salario:")
seniority_label = tk.Label(root, text="Ingrese la antigüedad:")
liquidation_label = tk.Label(root)

salary_entry = tk.Entry(root)
seniority_entry = tk.Entry(root)
calculate_button = tk.Button(root, text="Calcular", command=calculate_liquidation)

salary_label.grid(row=0, column=0)
seniority_label.grid(row=1, column=0)
liquidation_label.grid(row=2, column=1)

salary_entry.grid(row=0, column=1)
seniority_entry.grid(row=1, column=1)
calculate_button.grid(row=3, column=1)

root.mainloop()