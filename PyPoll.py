# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")
my_list = list()
# def unique(list1):
 
#     # initialize a null list
#     unique_list = []
     
#     # traverse for all elements
#     for x in list1:
#         # check if exists in unique_list or not
#         if x not in unique_list:
#             unique_list.append(x)
  
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
    for row in file_reader:
        my_list.append(row[2])
        
 
print(unique(my_list))


# 1. total num of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candadates won
# 5. The winner of the election based on popular vote


import datetime as dt
now = dt.datetime.now()
print(now)