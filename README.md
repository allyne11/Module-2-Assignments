Data Analysis Project - Financial & Election Analysis
Project Overview
This project consists of two separate data analysis tasks:

Financial Analysis - Analyzing company financial records using budget_data.csv.
Election Analysis - Modernizing vote-counting using election_data.csv.
Each task involves writing a Python script to process the respective datasets and generate meaningful insights.

Part 1: Financial Analysis
Objective
You are tasked with creating a Python script to analyze the financial records of a company. You will be given a dataset named budget_data.csv, which contains:

Date: The month and year of the financial record.
Profit/Losses: The profit or loss recorded for that month.
The script should compute:
✅ The total number of months in the dataset.
✅ The net total amount of "Profit/Losses" over the entire period.
✅ The changes in "Profit/Losses" and the average of those changes.
✅ The greatest increase in profits (date and amount).
✅ The greatest decrease in profits (date and amount).

Dataset Example - budget_data.csv
Date	Profit/Losses
Jan-2010	867884
Feb-2010	984655
Mar-2010	322013
...	...
Expected Output
yaml
Copy
Edit
Financial Analysis
----------------------------
Total Months: 86
Total: $38382578
Average Change: $-2315.12
Greatest Increase in Profits: Feb-2012 ($1926159)
Greatest Decrease in Profits: Sep-2013 ($-2196167)
The results will be displayed in the terminal and saved in financial_analysis.txt.

Part 2: Election Analysis
Objective
You are tasked with helping a small, rural town modernize its vote-counting process. The dataset election_data.csv contains:

Voter ID: Unique ID for each voter.
County: The county where the voter resides.
Candidate: The candidate the voter selected.
The script should compute:
✅ The total number of votes cast.
✅ A complete list of candidates who received votes.
✅ The percentage of votes each candidate won.
✅ The total number of votes each candidate won.
✅ The winner of the election based on the popular vote.

Dataset Example - election_data.csv
Voter ID	County	Candidate
12864552	Jefferson	Charles Casper Stockham
17425657	Denver	Diana DeGette
14211541	Jefferson	Charles Casper Stockham
...	...	...
Expected Output
markdown
Copy
Edit
Election Results
-------------------------
Total Votes: 3521001
-------------------------
Charles Casper Stockham: 23.0% (812347)
Diana DeGette: 73.8% (2592384)
Raymon Anthony Doane: 3.1% (107270)
-------------------------
Winner: Diana DeGette
-------------------------
The results will be displayed in the terminal and saved in election_results.txt.
