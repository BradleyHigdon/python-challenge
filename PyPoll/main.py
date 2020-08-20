import os
import csv

election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")


    print("Election Results")
    print("-------------------------")
    #Total votes cast
    #print(sum (total row - 1))


    print("-------------------------")
    #Candidates that recieved votes
    #print

    #Total votes for each candidate
    #print

    print("-------------------------")
    #Winning candidate
    #print(Candidate_Name)

    print("-------------------------")