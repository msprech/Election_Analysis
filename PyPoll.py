import csv
import os

#create file object for csv file 
file_to_load = os.path.join("Resources", "election_results.csv")

#file name variable 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#total vote counter variable 
total_votes = 0
#declare a new list for candidates 
candidate_options = []
#declare new dictionary of candidates and votes
candidate_votes = {}
#declare variable holding empty string for winning candidate 
winning_candidate = ""
#declare variable for winning count equal to zero 
winning_count = 0
#declare variable for winning percentage equal to zero 
winning_percentage = 0

#open csv and make file variable 
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    
    for row in file_reader:
        total_votes += 1
        #setting variable for the candidate names
        candidate_name = row[2]
        #if statement to see if candidate is new 
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #setting up the name as the key for the dictionary and tracking votes
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1


    print(total_votes)
    print(candidate_options)
    print(candidate_votes)
   
    #iterate through candidate list 
    for candidate_name in candidate_votes:
        #setting up value and pulling votes
        votes = candidate_votes[candidate_name]
        #calculate vote percentage 
        vote_percentage = float(votes) / float(total_votes) * 100 
        print(f"{candidate_name}: received {vote_percentage: .1f} of the vote.")

        #to do: print out candidate name, vote count, percentage of votes 

        if (votes > winning_count) and (vote_percentage > winning_percentage): 
            winning_count = votes 
            winning_percentage = vote_percentage 
            winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes: ,})\n")

    
    #to do: print out winning candidate, vote, percentage 
    winning_candidate_summary = (
        f" ---------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Votte Count: {winning_count: ,}\n"
        f"Winning Percentage: {winning_percentage: .1f}%\n"
        f"-----------------\n")
print(winning_candidate_summary)



