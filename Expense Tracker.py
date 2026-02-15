import tkinter as tk
from tkinter import messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Daily Expense Tracker")
        self.root.geometry("400x300")

        self.expenses = []

        tk.Label(root, text="Item Name:", font=("Arial", 12)).pack(pady=5)
        self.item_entry = tk.Entry(root, font=("Arial", 12))
        self.item_entry.pack(pady=5)

        tk.Label(root, text="Amount (₹):", font=("Arial", 12)).pack(pady=5)
        self.amount_entry = tk.Entry(root, font=("Arial", 12))
        self.amount_entry.pack(pady=5)

        tk.Button(root, text="Add Expense", command=self.add_expense).pack(pady=5)
        tk.Button(root, text="Show Total", command=self.show_total).pack(pady=5)

        self.expense_list_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
        self.expense_list_label.pack(pady=10)

    def add_expense(self):
        item = self.item_entry.get().strip()
        amount = self.amount_entry.get().strip()

        if not item or not amount:
            messagebox.showerror("Error", "Please enter both item name and amount!")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Amount must be a number!")
            return

        self.expenses.append((item, amount))
        self.update_expense_list()
        self.item_entry.delete(0, tk.END)
        self.amount_entry.delete(0, tk.END)

    def update_expense_list(self):
        text = "Expenses:\n"
        for i, (item, amt) in enumerate(self.expenses, start=1):
            text += f"{i}. {item}: ₹{amt}\n"
        self.expense_list_label.config(text=text)

    def show_total(self):
        total = sum(amount for _, amount in self.expenses)
        messagebox.showinfo("Total Expenses", f"Total: ₹{total}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
