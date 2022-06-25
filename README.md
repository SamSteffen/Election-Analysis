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
Based on the findings of the above election audit, it is the proposition of our research team that the code written to determine these outcomes in this election could be used to determine the results for any election, provided the election data is stored in a manner similar to that found in the "election_results.csv" excel file used in this project, with "Ballot ID," "County," and "Candidate" data provided in columns A, B, and C, respectively. It is estimated that our code could generate the same report for elections with any number of candidates, any number of voters and for precincts containing as many counties as is to be limited by the dataset.

Additional information about voters, candidates, precincts could only deepen our analysis; given the 3 categories of data that we have, without needing to gather more data, we could also modify our code to determine additional findings like (1) the number of votes from each county that went to each candidate, (2) the percentage of each county that went to each candidate, (3) the declared winner of each county by vote count and vote percentage. These findings could be determined as follows:

https://www.w3schools.com/python/python_dictionaries_nested.asp

- Investigation into additional Python coding shows that a nested dictionary could be added to the 'PyPoll_Challenge' script that contains:
    * Dictionary (A) that holds the names of the counties as the keys and the names of candidates as values
    * Dictionary (B) that holds each county-candidate value in dictionary A as the key and the total count of the number of votes received by that candidate in that county as the value.
Made explicit, the nested dictionary described above would give us something resembling the following:

for County_Candidate: {
    Jefferson County: Charles Casper Stockham: votes for candidate in county
    Jefferson County: Diana DeGette: votes for candidate in county
    Jefferson County: Raymon Anthony Doane: votes for candidate in county
    Denver County: Charles Casper Stockham: votes for candidate in county
    Denver County: Diana DeGette: votes for candidate in county
    Denver County: Raymon Anthony Doane: votes for candidate in county
    Arapahoe County: Charles Casper Stockham: votes for candidate in county
    Arapahoe County: Diana DeGette: votes for candidate in county
    Arapahoe County: Raymon Anthony Doane: votes for candidate in county
    }
    
    child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
    
    
```
