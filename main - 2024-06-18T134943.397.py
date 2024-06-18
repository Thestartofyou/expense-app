import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt

class FinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        
        self.income_data = []
        self.expense_data = []
        
        self.setup_ui()
        
    def setup_ui(self):
        # Income section
        income_frame = ttk.LabelFrame(self.root, text="Income")
        income_frame.grid(row=0, column=0, padx=10, pady=10)
        
        ttk.Label(income_frame, text="Amount:").grid(row=0, column=0)
        self.income_amount = tk.DoubleVar()
        ttk.Entry(income_frame, textvariable=self.income_amount).grid(row=0, column=1)
        
        ttk.Button(income_frame, text="Add Income", command=self.add_income).grid(row=1, columnspan=2, pady=5)
        
        # Expense section
        expense_frame = ttk.LabelFrame(self.root, text="Expenses")
        expense_frame.grid(row=1, column=0, padx=10, pady=10)
        
        ttk.Label(expense_frame, text="Amount:").grid(row=0, column=0)
        self.expense_amount = tk.DoubleVar()
        ttk.Entry(expense_frame, textvariable=self.expense_amount).grid(row=0, column=1)
        
        ttk.Label(expense_frame, text="Category:").grid(row=1, column=0)
        self.expense_category = tk.StringVar()
        ttk.Entry(expense_frame, textvariable=self.expense_category).grid(row=1, column=1)
        
        ttk.Button(expense_frame, text="Add Expense", command=self.add_expense).grid(row=2, columnspan=2, pady=5)
        
        # Summary section
        summary_frame = ttk.LabelFrame(self.root, text="Summary")
        summary_frame.grid(row=2, column=0, padx=10, pady=10)
        
        self.summary_text = tk.StringVar()
        ttk.Label(summary_frame, textvariable=self.summary_text).grid(row=0, column=0)
        
        ttk.Button(summary_frame, text="Show Summary", command=self.show_summary).grid(row=1, columnspan=2, pady=5)
        
        # Visualization section
        ttk.Button(self.root, text="Show Visualizations", command=self.show_visualizations).grid(row=3, column=0, pady=10)
        
    def add_income(self):
        amount = self.income_amount.get()
        self.income_data.append(amount)
        self.income_amount.set(0)
        
    def add_expense(self):
        amount = self.expense_amount.get()
        category = self.expense_category.get()
        self.expense_data.append((amount, category))
        self.expense_amount.set(0)
        self.expense_category.set("")
        
    def show_summary(self):
        total_income = sum(self.income_data)
        total_expense = sum([amount for amount, category in self.expense_data])
        balance = total_income - total_expense
        self.summary_text.set(f"Total Income: ${total_income}\nTotal Expenses: ${total_expense}\nBalance: ${balance}")
        
    def show_visualizations(self):
        df = pd.DataFrame(self.expense_data, columns=["Amount", "Category"])
        category_sum = df.groupby("Category").sum()
        
        plt.figure(figsize=(10, 5))
        
        plt.subplot(1, 2, 1)
        plt.bar(category_sum.index, category_sum["Amount"])
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        
        plt.subplot(1, 2, 2)
        plt.pie([sum(self.income_data), sum([amount for amount, category in self.expense_data])],
                labels=["Income", "Expenses"], autopct='%1.1f%%')
        plt.title("Income vs Expenses")
        
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceTracker(root)
    root.mainloop()
