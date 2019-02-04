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

# Declare Variables. extratcted names manually as shortcut but if more time could have done this with code.
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#open csv
with open(csvpath,newline="", encoding="utf-8") as elections:

    #read csv
    csvreader = csv.reader(elections,delimiter=",") 

    #skip header
    header = next(csvreader)     

    #loop start
    for row in csvreader: 

        # count votes
        total_votes +=1

        # talley votes by canidate 
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 #lists for library creation
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]

#create a dictionary from lists
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

#capture the summary data
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

#print the summary data in a table format
print(f"Election Results")
print(f"____________________________________")
print(f"Total Votes: {total_votes}")
print(f"____________________________________")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"____________________________________")
print(f"Winner: {key}")
print(f"____________________________________")

#create the output file
output_file = os.path.join("Election_Results_Summary.txt")

#write results to txt file
with open(output_file,"w") as file:
    file.write(f"Election Results" + "\n")
    file.write(f"____________________________________" + "\n")
    file.write(f"Total Votes: {total_votes}" + "\n")
    file.write(f"____________________________________" + "\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})" + "\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})" + "\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})" + "\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})" + "\n")
    file.write(f"____________________________________" + "\n")
    file.write(f"Winner: {key}" + "\n")
    file.write(f"____________________________________" + "\n")