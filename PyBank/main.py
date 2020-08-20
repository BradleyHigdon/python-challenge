import os
import csv

budget_data = os.path.join("Pybank", "Resources", "budget_data.csv")

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")


    print("Financial Analysis")
    print("----------------------------")
    #Counting the months
    #print(sum["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])

    #Total profit/loss
    #for row in csv.reader:
    #print(sum[])

    #Average profit/loss
    #print

    #Greatest increase in profits
    #for row in csvreader:
    #if
    #print(Greatest Increase in Profits:)

    #Greatest decrease in profits
    #for row in csvreader:
    #if
    #print(Greatest Decrease in Profits:)
