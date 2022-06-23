# Election-Analysis

## Project Overview
A Colorado Board of Elections employee provided the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code Version 1.68.1

## Summary
The analysis of the election show that:
- There were 369,711 total votes cast in the election.
- The candidates were: 
  * Charles Casper Stockham
  * Diana DeGette
  * Raymon Anthony Doane 
- The candidate results were:
  * Charles Casper Stockham received 23.0% (85,213) of the total votes cast.
  * Diana DeGette received 73.8% (272,892) of the total votes cast.
  * Raymon Anthony Doane received 3.1% (11,606) of the total votes cast.
- The winner of the election was Diana DeGette who received 73.8% of the vote and 272,892 of the votes.

# Election Audit 
## Overview of Election Audit
The purpose of this election audit is to comply with the additional requests from the election commission to determine the following:
- The voter turnout for each county.
- The percentage of votes from each county out of the total count.
- The county with the highest voter turnout.

## Election-Audit Results:
- Using a Python script written especially for this data set, the following report can be automatically generated from the data provided in our data source:

<img width="191" alt="Election_analysis_terminal" src="https://user-images.githubusercontent.com/104729703/175219863-dc029ae7-c45e-4a65-8236-f56c74edfc63.png">

The output report above illustrates the following:
- Total votes cast in this congressional election: 369,711 votes
- Number of votes and percentage of total votes for each county in the precinct:
  * Jefferson County: 10.5 % of votes (38,855) 
  * Denver County: 82.8% of votes (306,055)
  * Arapahoe County: 6.7% of votes (24,801)
- County with the largest number of votes: Denver County
- Number of votes and percentage of total votes for each candidate:
  * Charles Caper Stockham: 23.0% of votes (85,213)
  * Diana DeGette: 73.8% of votes (272,892)
  * Raymon Anthony Doane: 3.1% of votes (11,606)
- Winner: Diana DeGette
  * Winning Vote Count: 272,829
  * Winning Percentage: 73.8%

## Election Audit Summary
Based on the findings of the above election audit, it is the proposition of our research team that the code written to determine these outcomes in this election could be used to determine the results for any election, provided the election data is stored in a manner similar to that found in the "election_results.csv" excel file used in this project. Provided the data in future elections contains "Ballot ID," "County," and "Candidate" fields, it is estimated that our code could generate the same report for elections with any number of candidates, any number of voters and for precincts containing as many counties as is to be limited by the dataset.

Additional information about voters, candidates, precincts could only deepen our analysis; but given the 3 categories of data that we have, without needing to gather more data, we could also modify our code to determine things like (1) the number of votes from each county that went to each candidate, (2) the percentage of each county that went to each candidate, (3) the declared winner of each county by vote count and vote percentage. These findings could be determined in the following manner:

#1. Initialize a candidate_county list that will hold the name of each candidate concatenated with the name of a county.
candidate_counties = []

#2a. Initialize a dictionary that will hold the candidate_county concatenation as the key and the number of votes cast for that candidate within that county as the values.
candidate_county_votes = {}

#2b. Initialize a variable that will hold the winning number of votes for each candidate in a particular county.
winning_candidate_county_votes = 0

#3. Inside the for loop, after declaring the candidate_name and county_name variables, create a new variable (using an f-string) that concatenates the candidate_name and county_name variables.
candidate_county_name = (f"{candidate_name}_in_{county_name}")

#4a. Write a decision statement with a logical operator to check if the candidate_county variable acquired in Step 3 is in the candidate_county list created in step 1.
if candidate_county_name not in candidate_counties:
   
#4b. If the candidate_county concatenation is not in the list created in Step 1, add it to the list of candidate_county concatenations.
candidate_counties.append(candidate_county_name)
 
#4c. Write a script that initalizes the candidate_county concatenation to zero.
   candidate_county_votes[candidate_county_name] = 0
   
#5. Write a script that adds a vote to the candidate_county's vote_count as you are looping through all the rows.
candidate_county_votes[candidate_county_name] += 1

#6a. Write a repetition statement to get the candidate_county from the candidate_county dictionary that was created in step 2.
for candidate_county in candidate_county_votes:

#6b. Initialize a variable to hold the candidate_county votes as they are retrieved from the candidate_county dictionary.
candidate_county_votecount = candidate_county_votes.get(candidate_county)

#6c. Write a script that calculates the candidate_county votes as a percentage of the candidate_county total votes.
cc_vote_percentage = float(candidate_county_votecount) / float(county_vote) * 100

#6d. Write a print statment that prints the current candidate_county concatenation, the percentage of each county that went to each candidate and the total votes for each candidate in each county.
candidate_county_summary = (
        f"{candidate_county_name}: {cc_vote_percentage:.1f}% ({candidate_county_votecount})\n"
    )
    print(candidate_county_summary)
   

#6e. Write a statement that saves the print statement to the .txt file.
    txt_file.write(candidate_county_summary)
    
6f. Write a decision statement that determines the candidate with the largest vote count for each county and then adds that county and its vote count to the variables created in step 2b.
 if(candidate_county_votecount > winning_candidate_county_votes)
            winning_candidate_county_votes = candidate_county_votes
            winning_candidate_county = candidate_county_name

7. Write a print statement that prints out the candidate with the largest voter turnout for each county.
 winning_candidate_county_summary = (
            f"------------------------\n"
            f"Winner: {winning_candidate_county}\n"
            f"Winning Vote Count: {winning_candidate_county_votes}\n"
            f"Winning Percentage: {cc_vote_percentage}"
            f"------------------------\n"
    )
    txt_file.write(winning_candidate_county_summary)
