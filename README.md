# Colorado Congressional Election Analysis and Results 

## Overview of Election Audit 

I was tasked with conducting an election audit of a congressional precinct in Colorado to find the following information: 

* Total vote count 
* Vote count per county 
* Percentage of total vote per county 
* County with the largest voter turnout 
* Vote count per candidate
* Percentage of total vote per candidate
* Winning candidate, vote count, and percentage of total vote

### Purpose of Analysis

The purpose of the analysis was to not only confirm the results of the election, but also to automate the process using loops and conditionals in python. This process and resulting code patterns could then be applied to other audits, including congressional and senatorial districts, as well as local elections. 

## Election Audit Results 

The following results detailing the outcome of the Colorado Congressional election were printed to the command line. Further analysis breaks down the code used to provide this summary.    

![Printed Election Results](https://github.com/msprech/Election_Analysis/blob/36f350f099e206048d2c62a48247d28041868251/Resources/Terminal%20Election%20Results.png)

* Total Votes Cast: 369, 711

### County Vote Results 

The county vote results were produced by first declaring an empty list, "county_options," and an empty dictionary, "county_votes". I then used a for loop to iterate through each row in the csv file, as well as a conditional statement to add each unique county name to the "county_options" list. Also within the conditional statement, I began tracking each county's vote count using the empty dictionary as shown in the code below. 

```
for row in reader: 
  
  if county_name not in county_options: 
  
    county_options.append(county_name)

    county_votes[county_name] = 0
  
  county_votes[county_name] += 1

```
I then used another for loop to iterate through the "county_votes" dictionary and calculate the total vote count per county and the vote percentage of the total vote per county. Both of these results were printed into the election_results text file using f-string statements.  


```
for county_name in county_votes: 
  
  county_vote_count = county_votes.get(county_name)
  
  county_vote_percentage = float(county_vote_count) / float(total_votes) * 100 
  
  county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
  
  ```
  
The final results per county were as follows. 
  
* Jefferson County: 10.5% of the total vote (38,855) 
* Denver County: 82.8% of the total vote (306,055)
* Arapahoe County: 6.7% of the total vote (11,606)
* Denver County had the largest voter turnout

### Candidate Vote Results 

Votes per candidate were produced using similar code to the county results process. Within the for loop, I set the variable "candidate_name" equal to row[2], or the index of the csv file containing the candidate name. This variable was then used in a conditional statement to iterate through each row of the file, adding unique candidate names to the declared empty list, "candidate_options." By using a dictionary, "candidate_votes," to hold both the candidate name and votes received, I initialized the votes received to 0 and then added a vote to the vote count every time the candidate's name appeared in the file. 

I used the dictionary to calculate the total number of votes per candidate, as well as their vote percentage out of the total number of votes. These results were written to the election_results text file using the following f-string statement. 

```

candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

txt_file.write(candidate_results)

```

The final results per candidate were as follows. 

* Charles Casper Stockhmam: 23.0% of the total vote (85,213)
* Diana DeGette: 73.8% of the total vote (272,892)
* Raymon Anthony Doane: 3.1% of the total vote (11,606)

### Winning Candidate 

While iterating through the "candidate_votes" dictionary, the following conditional statement was used to determine the winning candidate, vote count, and percentage. The "winning_candidate" variable, the "winning_count" variable, and the "winning_percentage" variable were all declared earlier in the code. 

```

if (votes > winning_count) and (vote_percentage > winning_percentage): 
  
  winning_count = votes
  winning_candidate = candidate_name
  winning_percentage = vote_percentage
  
```

The winning candidate and vote statistics were as follows: 

* Winner: Diana DeGette 
* Winning Vote Count: 272,892
* Winning Percentage: 73.8% of the total vote 

## Election Audit Summary 

The use of conditionals and loops in this election audit has made the code versatile and easily applicable to other election audits. The structure of the code focuses on declaring variables, lists, and dictionaries that will allow us to iterate through the csv file and automate necessary calculations. The for loops included iterate through the csv file to create lists of candidates and counties, dictionaries of candidate and candidate vote counts, and county and county vote counts, and conditionals to determine the winning candidate and county with the largest voter turnout. This overall pattern could easily be applied to another election audit with a few modifications. 

Firstly, the code would need to be altered to fit the specific csv file used. This includes changing the path from which to load the file as well as ensuring that any indexes used to reference columns within the file are accurately updated. Similarly, the proper output file and desired data would need to be specified as well. 

Lastly, the code would need to acommodate for different types of election, such as local elections which may need audits focused on city or town votes, rather than on counties. More complex audits with a wider scope of data may also require more conditionals and loops than smaller elections or those with only a few or even a single candidate. However, the structure of the proposed loops and conditionals included above still provide a solid foundation for further analysis.

