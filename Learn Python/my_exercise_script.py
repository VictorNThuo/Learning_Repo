import tkinter as tk
from tkinter import messagebox

class BudgetApp:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_income(self, amount, description):
        self.balance += amount
        self.transactions.append(f"Income: +{amount} ({description})")

    def add_expense(self, amount, description):
        self.balance -= amount
        self.transactions.append(f"Expense: -{amount} ({description})")

    def view_balance(self):
        return f"Current Balance: {self.balance}"

    def view_transactions(self):
        return "\n".join(self.transactions)

class BudgetAppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget App")

        self.budget_app = BudgetApp()

        self.amount_label = tk.Label(root, text="Amount:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.description_label = tk.Label(root, text="Description:")
        self.description_label.pack()

        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        self.add_income_button = tk.Button(root, text="Add Income", command=self.add_income)
        self.add_income_button.pack()

        self.add_expense_button = tk.Button(root, text="Add Expense", command=self.add_expense)
        self.add_expense_button.pack()

        self.view_balance_button = tk.Button(root, text="View Balance", command=self.view_balance)
        self.view_balance_button.pack()

        self.view_transactions_button = tk.Button(root, text="View Transactions", command=self.view_transactions)
        self.view_transactions_button.pack()

    def add_income(self):
        amount = float(self.amount_entry.get())
        description = self.description_entry.get()
        self.budget_app.add_income(amount, description)
        messagebox.showinfo("Success", f"Income added: +{amount}")

    def add_expense(self):
        amount = float(self.amount_entry.get())
        description = self.description_entry.get()
        self.budget_app.add_expense(amount, description)
        messagebox.showinfo("Success", f"Expense added: -{amount}")

    def view_balance(self):
        balance = self.budget_app.view_balance()
        messagebox.showinfo("Balance", balance)

    def view_transactions(self):
        transactions = self.budget_app.view_transactions()
        if transactions:
            messagebox.showinfo("Transactions", transactions)
        else:
            messagebox.showinfo("Transactions", "No transactions yet")

def main():
    root = tk.Tk()
    app_gui = BudgetAppGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
