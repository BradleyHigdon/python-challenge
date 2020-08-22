import os
import csv

budget_data = os.path.join("Pybank", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Skipping header for further calculations
    csv_header= next(csv_reader)

    print("Financial Analysis")
    print("----------------------------")
    #Counting the months
    months = []
    profit = []
    difference = []
    #Part of Method 2
    #total_months = 0
    for row in csv_reader:
        months.append(str(row[0]))
        profit.append(int(row[1]))

        
        #Method #2
        #total_months = total_months + 1
        #total_months += 1 
    
    total_months = len(months)
    print("Total Months:",total_months)
    print("Total:","$",sum(profit))
    

    
    for i in range(len(profit)-1):
        difference.append(profit[i+1] - profit[i])

    average_difference = (sum(difference)/len(profit))
    print("Average Change","$",average_difference)

    #maximum_increase = (max(increase)/len(profit))
    #print(maximum_difference)

    #Greatest increase in profits
    #for row in csvreader:
    #if
    #print(Greatest Increase in Profits:)

    #Greatest decrease in profits
    #for row in csvreader:
    #if
    #print(Greatest Decrease in Profits:)
