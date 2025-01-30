# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load =  r"C:\Users\aidan\OneDrive\Desktop\Module_3\Starter_Code\PyBank\Resources\budget_data.csv"
  # Input file path
file_to_output = r"C:\Users\aidan\OneDrive\Desktop\Module_3\Starter_Code\PyBank\Analysis\budget_analysis.txt"  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
total_profit_losses = 0
previous_profit_loss = None
changes = []
dates = []
# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list


    # Track the total and net change


    # Process each row of data
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Track total months and total profit/losses
        total_months += 1
        total_profit_losses += profit_loss
        
        # Compute monthly changes in profit/loss
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
        
        previous_profit_loss = profit_loss



# Calculate the average net change across the months
average_change = sum(changes) / len(changes) if changes else 0
greatest_increase = max(changes) if changes else 0
greatest_decrease = min(changes) if changes else 0

greatest_increase_date = dates[changes.index(greatest_increase)] if changes else "N/A"
greatest_decrease_date = dates[changes.index(greatest_decrease)] if changes else "N/A"


# Print the output
analysis = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n"
)

print(analysis)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(analysis)
