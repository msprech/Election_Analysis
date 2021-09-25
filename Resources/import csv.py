import csv 
import os 

file_to_load = os.path.join ("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0

candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}

winning_candidate = ""
winning_count = 0 
winning_percentage = 0 
highest_turnout_county = ""
highest_turnout_votes = 0 

with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader: 
        total_votes = total_votes + 1
        highest_turnout_votes = highest_turnout_votes + 1


        candidate_name = row[2]
        county_name = row[1]

        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 

        candidate_votes[candidate_name] += 1

        if county_name not in county_options: 
            county_options.append(county_name)
            county_votes[county_name] = 0 

        county_votes[county_name] += 1
    
    for county_name in county_votes:
        county_vote_count = county_votes.get(county_name)
        county_vote_percentage = float(county_vote_count) / float(total_votes) * 100
        print(county_vote_percentage)

  
