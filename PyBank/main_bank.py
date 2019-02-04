# Your task is to create a Python script that analyzes the records to calculate each of the following:

# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The average of the changes in "Profit/Losses" over the entire period
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:

#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

#import modules
import os
import csv

#load csv
csvpath = os.path.join("budget_data.csv")

#variables
total_months = 0
total_PL = 0
prev_PL = 0
PL_change = 0
avg_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999]
PL_changes = []

#read file
with open(csvpath, newline='') as PL_data:
    csvreader = csv.DictReader(PL_data, delimiter=',')

    #start loop
    for row in csvreader:

        #totals
        total_months = total_months + 1
        total_PL = total_PL + int(row["Profit/Losses"])
        # print(row)

        #deltas
        PL_change = int(row["Profit/Losses"]) - prev_PL
        # print(PL_change)

        #reset prev_PL
        prev_PL = int(row["Profit/Losses"])
        # print(prev_PL)

        #deteermine greatest increase and deecrease using deltas
        if (PL_change > greatest_increase[1]):
            greatest_increase[1] = PL_change
            greatest_increase[0] = row["Date"]

        if (PL_change < greatest_decrease[1]):
            greatest_decrease[1] = PL_change
            greatest_decrease[0] = row["Date"]

        #add deltas to list
        PL_changes.append(int(row["Profit/Losses"]))

        #calc avg change
        avg_change = str(round(sum(PL_changes) / len(PL_changes)))

    #calc PL avg
    PL_avg = sum(PL_changes) / len(PL_changes)
    
    #print values
    print()
    print()
    print()
    print("Financial Analysis")
    print("__________________________________________________________________")
    print("Total Months: " + str(total_months))
    print("Total PL: " + "$" + str(total_PL))
    print("Average Change: " + "$" + str(avg_change))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")

    #output values to text file
    file = open("totals.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("__________________________________________________________________" + "\n")
    file.write("Total Months: " + str(total_months) + "\n")
    file.write("Total PL: " + "$" + str(total_PL) + "\n")
    file.write("Average Change: " + "$" + str(avg_change) + "\n")
    file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + "\n")
    file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + "\n")
    file.close()