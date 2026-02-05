import argparse, expense

parser = argparse.ArgumentParser(description= "adds an expense")
parser.add_argument("description", type=str)
parser.add_argument("amount", type=float)
args = parser.parse_args()
(expense.add_expense(args.description, args.amount))
