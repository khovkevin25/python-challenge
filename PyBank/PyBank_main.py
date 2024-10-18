# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0 # Track the total number of months
total_net = 0 # Track the total sum of profits/losses
months = []
month_changes = []

# Add more variables to track other necessary financial data
greatest_increase = {"month":"","change":-float('inf')}
greatest_decrease = {"month":"","change":float("inf")}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change
    total_months += 1
    total_net += int(first_row[1])
    previous_value = int(first_row[1])

    # Process each row of data
    for row in reader:
        # Track the total
        total_months += 1
        current_value = int(row[1])

        # Track the net change
        total_net += current_value

        # Calculate monthly change in profit/loss and replaces previous value
        monthly_change = current_value - previous_value
        previous_value = current_value

        # Add values to existing predefined lists
        months.append(row[0])
        month_changes.append(monthly_change)

        # Calculate the greatest increase in profits (month and amount)
        if monthly_change > greatest_increase["change"]:
            greatest_increase["month"] = row[0]
            greatest_increase["change"] = monthly_change

        # Calculate the greatest decrease in losses (month and amount)
        if monthly_change < greatest_decrease["change"]:
            greatest_decrease["month"] = row[0]
            greatest_decrease["change"] = monthly_change

# Calculate the average net change across the months
avg_net = sum(month_changes)/len(month_changes)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Count of Months: {total_months}\n"
    f"Total Sum of Changes: ${total_net}\n"
    f"Average Change: ${avg_net:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['change']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['change']})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)