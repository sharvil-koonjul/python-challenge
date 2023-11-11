import os
import csv

# Path to CSV doc for budget data
pybank_csv = r'PyBank\Resources\budget_data.csv'

# Open the file to read
with open(pybank_csv,'r') as csv_file:
    csvreader = csv.reader(csv_file,delimiter=",")

    # Identify the header row and move on to the next row
    header_row = next(csvreader)
    
    # Setting count values and default reference values
    month_count = 0
    total_profit_losses = 0
    previous_value = 0
    sum_of_differences = 0
    count_of_differences = 0
    max_difference = float(0)
    min_difference = float(0)


    for row in csvreader:
        if row:
            # Getting the row count which will be used for the total months
            month_count += 1

            # Getting the total for Profit/Losses in the second column
            profit_losses = int(row[1])
            total_profit_losses += profit_losses
            
            # Taking each row for the month below and subtracting the row above in each loop
            if previous_value != 0:
                difference = profit_losses - previous_value
                
                # Get the sum of all of the differences calculated
                sum_of_differences += difference

                # Get the count for all of the differences calculated
                count_of_differences += 1

                # Identifying the greatest decrease using 0 as a starting part then going to the lowest number
                if difference < min_difference:
                    min_difference = difference
                    # Identifying the corresponding month value  
                    min_difference_month = row[0]

                # Identifying the greatest increase using 0 as a starting part then going to the highest number
                if difference > max_difference:
                    max_difference = difference
                    # Identifying the corresponding month value
                    max_difference_month = row[0]
                        
            previous_value = profit_losses
    if count_of_differences > 0:
        # Getting the average difference or "Average Change" then rounding to two decimal points
        average_difference = round(sum_of_differences / count_of_differences,2)        
            
# Creating the path for new text file we are creating
text_file = r'PyBank\analysis\analysis.txt'

# Generating a lines list for printing and writing
lines = [
    "Financial Analysis",
    "----------------------------",
    f"Total months: {month_count}",
    f"Total: ${total_profit_losses}",
    f"Average Change: ${average_difference}",
    f"Greatest Increase in Profits: {max_difference_month} (${max_difference})",
    f"Greatest Decrease in Profits: {min_difference_month} (${min_difference})"
]

# Opening new text file for writing
with open(text_file,'w', newline='') as writer:
        # Creating a loop for each line
        for line in lines:
            # Print each line in terminal
            print(line)
            # Write each line in the text file
            writer.write(line + '\n')

