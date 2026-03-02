import argparse, csv, requests

api_url = "https://exercisedb.dev"
class Routine:
    def __init__(self, name, exercises = []):
        self.name = name
        self.exercises = exercises


def add_exercise(routine_name, exercise):
    url = f"{api_url}/api/v1/exercises/{exerciseId}"
    
    

    
    pass
#def add_expense(description, amount):
#    csv_file = '../data/expenses.csv'
#    with open(csv_file, mode='a', newline='') as file:
#        writer = csv.writer(file)
#        writer.writerow([description, amount])
#    print(f"Added expense: {description} - ${amount}")