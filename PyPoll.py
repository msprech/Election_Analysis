#The data we need to retrieve 
#1 the total number of votes cast
#2 a complete list of candidates who received votes
#3 the percentage of votes each candidate won
#4 the total number of votes each candidate won 
#5 the winner of the elction based on popular vote

#assign variable to load file from path 
file_to_load = 'Resources/election_results.csv'


#add dependencies 
import csv
import os 
#assign variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open election results and read file 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

    for row in file_reader:
        print(row)
