# In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:

# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

# As an example, your analysis should look similar to the one below:
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#import modules
import os
import csv

csvpath = os.path.join("election_data.csv")

with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    totalvotes = []
    candidates = []
    cand_percent = []
    cand_votes = []
    winner = []

    for row in csv.reader(csvfile):
        totalmonths = len(list(csvreader))
        total += int(row[1])
        average_change = (total / totalmonths) * 100
        highest = int(max(row[1]))
        lowest = int(min(row[1]))
    
    print('Elesction Results')
    print('_________________________________________________________________________')
    print(f"Total Months: {str(totalmonths)}")
    print(f"Total: {str(total)}")
    print(f"Average Change: {str(average_change)}")
    print(f"Greatest Increase in Profits: {str(highest)}")
    print(f"Greatest Decrease in Profits: {str(lowest)}")
    
# # Specify the file to write to
# output_path = os.path.join("totals.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open("totals.txt", 'w') as texy_file:

#     # Initialize text.writer
#     text_file.write(get_totals(column[1])