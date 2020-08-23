import os
import csv

election_data = os.path.join("PyPoll", "Resources", "election_data.csv")

with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Skipping header for further calculations
    csv_header= next(csv_reader)

    print("Election Results")
    print("-------------------------")

    #Creating variables for votes per candidate
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0

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
    

    #Total votes for each candidate
    if (row[2] == "Khan"): Khan_votes += 1
    if (row[2] == "Correy"): Correy_votes += 1
    if (row[2] == "Li"): Li_votes += 1
    if (row[2] == "O'Tooley"): OTooley_votes += 1

    #Percentage of votes for each candidate
    Khan_votes_percentage = ((Khan_votes / total_votes)*100)
    Correy_votes_percentage = ((Correy_votes / total_votes)*100)
    Li_votes_percentage = ((Li_votes / total_votes)*100)
    OTooley_votes_percentage = ((OTooley_votes / total_votes)*100)

    #Print statements for candidates who received votes, percentages of the votes, and vote totals for each candidate
    print("Candidates who received votes",candidate_set)
    print("Khan vote total:",Khan_votes_percentage,"%",Khan_votes)
    print("Correy vote total:",Correy_votes_percentage,"%",Correy_votes)
    print("Li vote total:",Li_votes_percentage,"%",Li_votes)
    print("O'Tooley vote total:",OTooley_votes_percentage,"%",OTooley_votes)
    print("-------------------------")
   
    #Setting conditions for winning candidate
    if ((Khan_votes > Correy_votes),(Khan_votes > Li_votes), (Khan_votes > OTooley_votes)): winner = "Khan"
    if ((Correy_votes > Khan_votes),(Correy_votes > Li_votes), (Correy_votes > OTooley_votes)): winner = "Correy"
    if ((Li_votes > Correy_votes),(Li_votes > Khan_votes), (Li_votes > OTooley_votes)): winner = "Li"
    if ((OTooley_votes > Correy_votes),(OTooley_votes > Li_votes), (OTooley_votes > Khan_votes)): winner = "O'Tooley"

    print(winner)

    print("-------------------------")