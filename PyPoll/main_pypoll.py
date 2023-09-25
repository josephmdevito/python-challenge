# import operating system module + csv module
import os
import csv

# access the data
csvpath = os.path.join(".", "Resources_PyPoll", "election_data.csv")
# create your variables: total amount of votes, votes per candidate
total_votes = []
doane_votes = 0
degette_votes = 0
stockham_votes = 0
# open the csv file + encode fopr Windows
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # set up the loop, count the total number of votes
    for row in csvreader:
        total_votes.append(row[0])
        #count the number of votes for each candidate
        if row[2] == "Raymon Anthony Doane":
            doane_votes +=1
        elif row[2] == "Diana DeGette":
            degette_votes +=1
        elif row[2] == "Charles Casper Stockham":
            stockham_votes +=1
# calculate the percent vote for each candidate
total_votes_var = len(total_votes)
doane_percent = (doane_votes/total_votes_var) * 100
degette_percent = (degette_votes/total_votes_var) * 100
stockham_percent = (stockham_votes/total_votes_var) * 100

# find winner ... make dictionary of lists?
candidates = ["Raymon Anthony Doane", "Diana DeGette", "Charles Casper Stockham"]
candidate_votes = [doane_votes, degette_votes, stockham_votes]
dictionary_votes = dict(zip(candidates, candidate_votes))
winner = max(dictionary_votes, key=dictionary_votes.get)

# print the analysis 
print("Election Results")
print("-------------------------------------------")
print(f"Total Votes: {len(total_votes)}" )
print("-------------------------------------------")
# print vote percents + round to nearest 3 decimals per project example
# print number of votes for each candidate
print(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
print(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
print(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
print("-------------------------------------------")
# print winner name
print(f"Winner: {winner}")
print("-------------------------------------------")

# export the results in a text file
analysis_PyPoll = os.path.join("Analysis_PyPoll", "Election_Analysis.txt")
with open(analysis_PyPoll,"w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("-------------------------------------------")
    file.write("\n")
    file.write(f"Total Votes: {len(total_votes)}" )
    file.write("\n")
    file.write("-------------------------------------------")
    file.write("\n")
    file.write(f"Charles Casper Stockham: {stockham_percent:.3f}% ({stockham_votes})")
    file.write("\n")
    file.write(f"Diana DeGette: {degette_percent:.3f}% ({degette_votes})")
    file.write("\n")
    file.write(f"Raymon Anthony Doane: {doane_percent:.3f}% ({doane_votes})")
    file.write("\n")
    file.write("-------------------------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------------------------------")

# This code was prepared by Joseph DeVito for the Northwestern Data Science & Visualization Bootcamp. 