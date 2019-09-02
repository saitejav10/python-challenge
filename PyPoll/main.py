# First we'll import the os module
import os
# Module for reading CSV files
import csv

pypoll = os.path.join('election_data.csv')

candidates = []
votes = []
unique_candidates = []
percentage = []
count_candidates = 0

# Open the CSV File, read the csv file, skip the header row
with open (pypoll, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader=next(csvreader)
    
    # Store the candidates into lists by using the index
    for row in csvreader:
        candidates.append(row[2])

    # Find the total number of votes cast
    total_votes = len(candidates)

# For loop - Set () is used to collect unique candidates from the list
for x in set(candidates): 
    unique_candidates.append(x) # (X) respresents the unique candidates in the list
    candidate_counts = candidates.count(x) #Total count of votes each (unique) candidate received
    votes.append(candidate_counts)  #Store total count of votes each candidate earned into Votes

    #The percentage of votes each candidate won
    total_percent = round((candidate_counts/total_votes) * 100, 1) #Total count of votes each candidate received and divide by total number of votes
    percentage.append(total_percent) #Store percent of votes each candidate won in Percentage

    count_candidates += 1 #Iterate through each unqiue candidate to get the total percent of votes/total count of votes and store them into percentage list

#The winner of the election based on popular vote
winner = unique_candidates[votes.index(max(votes))]

# Print analysis
print("Election Results")
print("-----------------------------------")
print(f'Total Votes: {total_votes}')
print("-----------------------------------")
for i in range(count_candidates):
    print(f'{unique_candidates[i]}: {percentage[i]} ({votes[i]})')
print("-----------------------------------")
print(f'Winner: {winner}')
print("-----------------------------------")


# Set variable for output file
output_file = os.path.join("election_results.txt")

#  Open the output file and print the output into the new text file
with open(output_file, "w", newline="") as textfile:
    print("Election Results" , file=textfile)
    print("-------------------------------------", file=textfile)
    print(f'Total Votes: {total_votes}' , file=textfile)
    print("-------------------------------------", file=textfile)
    for i in range(count_candidates):
        print(f'{unique_candidates[i]}: {percentage[i]} ({votes[i]})', file=textfile)
    print("-------------------------------------", file=textfile)
    print(f'Winner: {winner}', file=textfile)
    print("-------------------------------------", file=textfile)