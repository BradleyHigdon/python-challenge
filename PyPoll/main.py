import os
import csv

election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")