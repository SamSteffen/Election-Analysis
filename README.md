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

To make our code more universally applicable, the variables themselves could also be modified to more accurately reflect the type of election being conducted as well as the data being collected. For example, if you were looking for the results of a city's mayoral election, you could change the "county" variable in our PyPoll python script to read as "city_districts" so that the code would read as follows:

```python
#1. Initialize a list to collect the items in a list of city_districts.
city_districts = []

#2. Initialize a dictionary that holds the city_districts as keys and
#the number of votes for each city_district as the values.
city_districts_votes = {}

# 3. Initialize a string variable, winning_districts, that will ultimately declare
#the city_district in the dataset with the most number of votes cast.
winning_districts = ""

#4. Initialize a variable, winning_districtvotes, that will hold the number
#of votes for the district with the most votes. Set it equal to zero.
winning_districtvotes = 0
```
```python
        #5. Inside the first for loop, assign variable city_district_name
        #to the respective column in the dataset, as row[x], where column A = row[0],
        #column B = row[1], etc.
        city_district_name = row[x]
```
```python
        #6a. Write a conditional statement to see whether city_district_name
        #is NOT in city_districts list created in step 1.
        if city_district_name not in city_districts:
        
            #6b. If the conditional returns "TRUE", add the city_district_name to
            #city_districts list.
            city_districts.append(city_district_name)
            
            #6c. To begin to count the number of votes returned for a city's district
            #set the number of votes in the city_district_votes dictionary at the 
            #city_district_name index to zero.
            city_district_votes[city_district_name] = 0

        #6d. Increase the count of the value established in 6c by 1.
        city_district_votes[city_district_name] += 1
```
```python
    #7a.Inside the second with statement, establish a for loop that will 
    #iterate through the city_district_votes dictionary by the iterator, district.
    for district in city_district_votes:

        #7b. Get the count of the values of district_votes from the dictionary.
        district_votes = city_district_votes.get(district)

        #7c. Determine the percentage of the total votes that went to the district,
        # using the total_votes variable as the denominator.
        district_percentage = float(district_votes) / float(total_votes) * 100

        #8a. Inside the for-loop, write a summary statement of the results.
        district_results = (
           f"{district}: {district_percentage:.1f}% ({district_votes})\n")

        #8b. Print the summary statement.
        print(district_results, end ="")

        #8c. Save the output to the .txt file.
        txt_file.write(district_results)

    #9. Write an if statment to determine the winning district and get its vote count.
    if (district_votes > winning_districtvotes):
        winning_districtvotes = district_votes
        winning_district = district
    
    #10a. Write a summary for the winning district
    winning_district_summary = (
       f"\n-------------------------\n
       f"\nLargest District Turnout: {winning_district}
       f"\n-------------------------\n)
    
    #10b. Print the winning district summary to the terminal.
    print(winning_district_summary)

    #10c. Save the winning summary to the .txt file.
    txt_file.write(winning_district_summary)
```

The above modification could be further modified to account for any column of data that we wanted to count and find the "winner" of, which is actually a determination of the mode of the data for the column. The following steps could be taken to amend the script to account for the determination of the mode of any column:

```python
#1. Initialize a list to collect the names of strings in column x.
variable_names = []

#2. Initialize a dictionary that holds the items in list_x as the keys
#and the count of the number of times they appear in the dataset as the values.
dict_variable_count = {}

# 3. Initialize a string variable, dataset_mode, that will ultimately declare
#the mode of the dataset, or the variable that appears the most in the dataset.
dataset_mode = ""

#4. Initialize a variable, mode_count, that will hold the number of times
#the mode appears in the dataset. Set it equal to zero.
mode_count = 0
```
```python
        #5. Inside the first for loop, assign a variable to the name of the variable
        # being collected in the list initiated in step 1.
        # Assign it to row[x], where column A = row[0], column B = row[1], etc.
        item_name = row[x]
```
```python
        # 6a. Write a conditional statement to see whether item_name
        # is NOT in the variable_names list created in step 1.
        if item_name not in variable_names: 
    
            #6b. If the conditional returns "TRUE", add the item_name to
            #the variable_names list.
            variable_names.append(item_name)
            
            #6c. To begin to count the number of times items appears in the 
            #variable_names list, set the number of items in the dict_variable_count
            #dictionary at the item_name index to zero. 
            dict_variable_count[item_name] = 0
        
        #6d. Increase the count of the value established in 6c by 1.
        dict_variable_count[item_name] += 1
 ```
 ```python
    #7a. Inside the second with statement, establish a for loop that will
    #iterate through the dict_variable_count dictionary by an iterator, iterator. 
    for iterator in dict_variable_count:
  
        #7b. Get the count of the values of item_count from the dictionary.
        item_count = dict_variable_count(iterator)
       
        #7c. Determine the percentage of the total items within the dataset, 
        # using the total_votes variable as the denominator. 
        item_percentage =  float(item_count) / float(total_votes) * 100

        #8a. Inside the for-loop, write a summary statement of the results.
        count_summary = (
            f"{iterator}:{item_percentage:.1f}% ({item_count}))     
              
        #8b. Print the summary statement.
        print(count_summary, end ="")   
       
        #8c. Save the output to the .txt file.
        txt_file.write(count_summary)

    #9. Write an if statment to determine the mode of the dataset and get its count.
    if (item_count > dataset_mode):
        dataset_mode = item_count
        mode_name = iterator
    
    #10a. Write a summary for the mode
    mode_summary = (
       f"\n-------------------------\n
       f"\nMode: {mode_name}
       f"\n-------------------------\n)
    
    #10b. Print the winning district summary to the terminal.
    print(mode_summary)

    #10c. Save the winning summary to the .txt file.
    txt_file.write(mode_summary)
```

Additional information about voters and candidates (gender, age, race, sexual orientation, cultural heritage, income, political affiliation, geographic location, etc.) as well as precincts could only deepen our analysis. Given the 3 categories of data that we have, without needing to gather more, we could also modify our code to determine additional findings like (1) the number of votes from each county that went to each candidate, (2) the percentage of each county that went to each candidate, (3) the declared winner of each county by vote count and vote percentage. These findings could determined in a number of ways, either by establishing conditional statements at the beginning of our for-loops to populate new lists and dictionaries based on the criteria of a particular county or by creating a list of dictionaries to iterate through each candidate and their vote return within each county.
