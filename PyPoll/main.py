import os
import csv

election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Skipping header for further calculations
    csv_header= next(csv_reader)

    print("Election Results")
    print("-------------------------")

    #Creating lists for Voter ID, Candidates, and votes cast
    voterID = []
    county = []
    candidate = []

    #Appending lists
    for row in csv_reader:
        voterID.append(int(row[0]))
        county.append(str(row[1]))
        candidate.append(str(row[2]))

    #Total votes cast
    total_votes = len(voterID)
    print("Total Votes:",total_votes)


    print("-------------------------")
    #Candidates that recieved votes
    candidate_set = set(candidate)
    number_of_unique_values = len(candidate_set)
    print(candidate_set)

    #Total votes for each candidate
    #print

    print("-------------------------")
    #Winning candidate
    #print(Candidate_Name)

    print("-------------------------")