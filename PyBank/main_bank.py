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

csvpath = os.path.join("budget_data.csv")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    totalmonths = []
    total = 0
    average_change = []
    highest = []
    lowest = []

    for row in csv.reader(csvfile):
        totalmonths = len(list(csvreader))
        total += int(row[1])
        average_change = (total / totalmonths) * 100
        highest = int(max(row[1]))
        lowest = int(min(row[1]))
    
    print('Financial Analysis')
    print('________________________________________________________________')
    print(f"Total Months: {str(totalmonths)}")
    print(f"Total: {str(total)}")
    print(f"Average Change: {str(average_change)}")
    print(f"Greatest Increase in Profits: {str(highest)}")
    print(f"Greatest Decrease in Profits: {str(lowest)}")
    
# # calculate total months, total and average change
# def get_totals(): 
#     totalmonths = len(column[1])
#     total = int(column[2] += 1)
#     average_change = (total / totalmonths) * 100
#     highest = max(column[2])
#     lowest = min(column[2])
    
#     print(f"Total Months: {str(totalmonths)}")
#     print(f"Total: {str(total)}")
#     print(f"Average Change: {str(average_change)}")
#     print(f"Greatest Increase in Profits: {str(highest)}")
#     print(f"Greatest Decrease in Profits: {str(lowest)}")


# # Specify the file to write to
# output_path = os.path.join("totals.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open("totals.txt", 'w') as texy_file:

#     # Initialize text.writer
#     text_file.write(get_totals(column[1])