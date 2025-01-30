# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = r"C:\Users\aidan\OneDrive\Desktop\Module_3\Starter_Code\PyPoll\Resources\election_data.csv"
file_to_output = "election_analysis.txt"  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidates = {}
winner = ""
max_votes = 0
# Define lists and dictionaries to track candidate names and vote counts


# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load, mode="r", newline="") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    
    for row in reader:
        total_votes += 1
        candidate = row[2]  # Candidate's name is in the third column

        # Tally votes for each candidate
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

results = []
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")

    if votes > max_votes:
        max_votes = votes
        winner = candidate

results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")


for line in results:
    print(line)


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    for line in results:
        file.write(line + "\n")

print(f"\nElection results have been saved to {file_to_output}.")