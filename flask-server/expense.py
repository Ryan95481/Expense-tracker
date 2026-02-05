import argparse, csv
class Expense:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount

def add_expense(description, amount):
    csv_file = '../data/expenses.csv'
    with open(csv_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([description, amount])
    print(f"Added expense: {description} - ${amount}")