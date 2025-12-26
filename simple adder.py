import tkinter as tk
root = tk.Tk()

def add_numbers():
	num1 = float(entry1.get())
	num2 = float(entry2.get())
	result_lable.config(text=f"sum:{int(num1 + num2)}")
root.title("simple adder")

def clear_fields():
	entry1.delete(0, tk.END)
	entry2.delete(0, tk.END)
	result_lable.config(text="Result will be displayed here")


entry1 = tk.Entry(root, font=("Arial",14))
entry1.pack(pady=14)
entry2 = tk.Entry(root, font=("Arial",14))
entry2.pack(pady=14)

button = tk.Button(root,text="Add Numbers",command=add_numbers)
button.pack()
button = tk.Button(root,text="Clear",command=clear_fields)
button.pack()


result_lable = tk.Label(root, text="Result will be displayed here.")
result_lable.pack()

root.mainloop()

