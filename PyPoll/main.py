import os
import csv

# Path to source data file
election_file = r'PyPoll\Resources\election_data.csv'

# Lists
names_list = []
name_1_list = []
name_2_list = []
name_3_list = []

# Reading the CSV
with open(election_file,'r') as csv_file:
    csvreader = csv.reader(csv_file,delimiter=",")
    
    # Identifying the header row
    header_row = next(csvreader)
    # Setting a counter for the total vote count
    total_vote_count = 0
        
    for row in csvreader:
        if row:
            # Summing up the vote counts
            total_vote_count += 1
            # Looking up names
            name = row[2]
            name_exists = False
            
            # Check if the names are repeated. If not, add to names list
            for names in names_list:
                if names == name:
                    name_exists = True
                            
            if name_exists == False:
                names_list.append(name)

        # Creating a names list for each name and then using len to get the vote count for each name
        if row[2] == names_list[0]:
            name_1_list.append(names_list[0])
            name_1_votes = len(name_1_list)
        elif row[2] == names_list[1]:
            name_2_list.append(names_list[0])
            name_2_votes = len(name_2_list)
        else:
            name_3_list.append(names_list[0])
            name_3_votes = len(name_3_list)

# Calculating the percentage for the votes and rounding to 3 decimals
name_1_percentage = round((name_1_votes / total_vote_count)*100,3)
name_2_percentage = round((name_2_votes / total_vote_count)*100,3)
name_3_percentage = round((name_3_votes / total_vote_count)*100,3)

# Finding the winner and storing in a conditional variable
if (name_1_votes > name_2_votes) and (name_1_votes > name_3_votes):
    winner = f"Winner: {names_list[0]}"
elif (name_2_votes > name_1_votes) and (name_2_votes > name_3_votes):
    winner = f"Winner: {names_list[1]}"
else: 
    winner = f"Winner: {names_list[2]}"

# Path to output text file
text_file = os.path.join("PyPoll/analysis/Election_Results.txt")

# Generating a lines list for printing and writing
lines = [
            "Election Results",
            "-------------------------",
            f"Total votes: {total_vote_count}",
            "-------------------------",
            f"{names_list[0]}: {name_1_percentage}% ({name_1_votes})",
            f"{names_list[1]}: {name_2_percentage}% ({name_2_votes})",
            f"{names_list[2]}: {name_3_percentage}% ({name_3_votes})",
            "-------------------------",
            f"{winner}",
            "-------------------------"
        ]

# Opening new text file for writing
with open(text_file,'w',newline='') as writer:
    # Creating a loop for each line
    for line in lines:
        # Print lines in terminal
        print(line)
        # Write lines in the text file
        writer.write(line + '\n')
