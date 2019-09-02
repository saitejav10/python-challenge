# First import the os module
import os
# Module for reading CSV files
import csv

budget_data = os.path.join("budget_data.csv")

months = []
revenue = []
profits = []

# Open the CSV File, read the csv file, skip the header row
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    
    # Store the months and revenue into lists by using the index
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))

    # Calculate the total number of months
    total_months = len(months)

    # Calculate the net total amount of "Profit/Losses" over the entire period
    total_revenue = sum(revenue)

    # Two parameters with iterating lists (iterates from index 1 to the length of the revenue column)
    for i in range(1, len(revenue)):
        revenue_change = ((int(revenue[i]) - int(revenue[i-1]))) #Find the revenue change between the months
        profits.append(revenue_change) # Store the revenue change into profits list

    # Find the average of the changes in "Profit/Losses" by using the information stored in profits list
    average_revenue_change = sum(profits) / len(profits)
    
    # Find the greatest increase in profits (date and amount)
    greatest_increase = max(profits)
    greatest_date = (months[profits.index(greatest_increase)+1])
    
    # Find the greatest decrease in losses (date and amount)
    greatest_decrease = min(profits)
    loss_date = (months[profits.index(greatest_decrease)+1])
    
# Print analysis 
print("Financial Analysis")
print("----------------------")
print(f'Total months: {total_months}')
print(f'Total: ${total_revenue}')
print(f'Average Change: ${round(average_revenue_change,2)}')
print(f'Greatest Increase in Profits: {greatest_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {loss_date} (${greatest_decrease})')

# Set variable for output file
output_file = os.path.join("budget_data.txt")

#  Open the output file and print the output into the new text file
with open(output_file, "w", newline="") as textfile:
    print("Financial Analysis", file=textfile)
    print("----------------------", file=textfile)
    print(f'Total months: {total_months}', file=textfile)
    print(f'Total: ${total_revenue}', file=textfile)
    print(f'Average Change: ${round(average_revenue_change,2)}', file=textfile)
    print(f'Greatest Increase in Profits: {greatest_date} (${greatest_increase})', file=textfile)
    print(f'Greatest Decrease in Profits: {loss_date} (${greatest_decrease})', file=textfile)