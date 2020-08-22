import os
import csv

budget_data = os.path.join("Pybank", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    #Skipping header for further calculations
    csv_header= next(csv_reader)

    print("Financial Analysis")
    print("----------------------------")
    #Creating lists for months, profit, and difference
    months = []
    profit = []
    difference = []

    #Appending months and profit
    for row in csv_reader:
        months.append(str(row[0]))
        profit.append(int(row[1]))
    
    #Calculating total months
    total_months = len(months)

    #Printing total months and sum of profit
    print("Total Months:",total_months)
    print("Total:","$",sum(profit))
    

    #Creating loop to find differences between months in profit
    for i in range(len(profit)-1):
        difference.append(profit[i+1] - profit[i])

    #Calculating and printing average difference in profit between months
    average_difference = (sum(difference)/len(profit))
    print("Average Change","$",average_difference)

    
    #Declaring and printing the greatest increase and decrease in profits
    maximum_difference = (max(difference))
    print("Greatest Increase in Profits:",maximum_difference)

    minimum_difference = (min(difference))
    print("Greatest Decrease in Profits:",minimum_difference)

    
