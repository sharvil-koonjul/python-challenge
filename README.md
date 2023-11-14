# python-challenge

In my PyPoll code, I received some suggestions by Esi (in our class) during a study group session to use a list for the names and then using len to get the vote count for each name.

#
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
#


I requested assistance from my sister to find out how I can break the lines as we needed for the analysis. She suggested I use '\n' when writing the lines in the text file.

This is used in both the PyBank and the PyPoll codes.

#
# Write lines in the text file
    writer.write(line + '\n')

