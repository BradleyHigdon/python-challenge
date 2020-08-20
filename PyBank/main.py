import os
import csv

budget_data = os.path.join("Pybank", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")