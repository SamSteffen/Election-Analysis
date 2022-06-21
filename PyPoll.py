#The data we need to retrieve
#1. Total number of votes cast
#2. Complete list of candidates who received votes
#3. Total number of votes received by each candidate.
#4. Percentage of votes receieved by each candidate.
#5. Winner of the election based on popular vote.

#Import dependencies
import csv
import os
import string

#Assign a variable for the .csv file to load and the path (DIRECT)
file_to_load = 'c:/Users/ssteffen/desktop/sam/Vanderbilt Boot Camp/MyRepo/Module 3_Python/Election-Analysis/Resources/election_results.csv'

#Assign a variable for the .csv file to load a file from a path(INDIRECT)
#import os
#file_to_load = os.path.join("C:","Users","ssteffen","desktop","sam","Vanderbilt Boot Camp","MyRepo","Module 3_Python","Election-Analysis", "Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file we want to save
#file_to_save = os.path.join("analysis", "election_analysis.txt")
file_to_save = 'c:/Users/ssteffen/desktop/sam/Vanderbilt Boot Camp/MyRepo/Module 3_Python/Election-Analysis/Analysis/election_analysis.txt'

#ALTERNATIVE:use the open function to open the file as a text file
    #outfile = open(file_to_save, "w")
    #open the election results and read the file
    #close the file
    #outfile.close()

#ALTERNATIVE: election_data = open(file_to_load, 'r')
    #Close the file
    #election_data.close()

#initialize accumulator to 0
total_votes = 0

#declare a new list for candidate names
candidate_options = []

#declare an empty dictionary to collect votes per candidate
candidate_votes = {}

#declare variables for winning_candidate, winning_count, and winning_percentage
winning_candidate = ""
winning_count = int(0)
winning_percentage = float(0)

#access the data
with open(file_to_load) as election_data:

    #create a variable that contains the csv data
    file_reader = csv.reader(election_data)

    #print the header row
    headers = next(file_reader)

    #print each row in the .csv file
    for row in file_reader:

        #increase total_votes by 1 for each row
        total_votes += 1

        #gather all the candidate names from column #3, row index [2]
        candidate_name = row[2]

        #create an if statement to see whether the candidate name is new;
        #   if it's a new name, add the candidate to the candidate list
        if candidate_name not in candidate_options: 
            candidate_options.append(candidate_name)
        
            #begin tracking new candidate's votecounts by initializing to 0
            candidate_votes[candidate_name] = 0

        #increase candidate's votecount by one if their name appears in row[2]
        candidate_votes[candidate_name] += 1

#save the results to our text file    
with open(file_to_save, "w") as txt_file:

#write election results f-string literal message
    election_results = (
    f"\nElection Results\n"
    f"-----------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-----------------------\n")
    #print to output
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)

    #determine percentage of votes for each candidate by looping through the counts
    #iterate through the candidate list
    for candidate_name in candidate_votes:

        #retrieve votecount of a candidate
        votes = candidate_votes[candidate_name]

        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        #print out each candidate's name, vote count and vote percentage to terminal
        #print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')

        #change print command into a variable to print to text file
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
    
        #print results to output 
        print(candidate_results)
        #save report to text file
        txt_file.write(candidate_results)

        #determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
                
            #if true, set winning_count = to votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
                
            #set winning candidate = to candidate's name
            winning_candidate = candidate_name

            #print out winning candidate, winning vote count and winning percentage to terminal
            winning_candidate_summary = (
            f"-----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:1f}%\n"
            f"-----------------------------\n")
    #print to output        
    print(winning_candidate_summary)
    #print to text file
    txt_file.write(winning_candidate_summary)

    #print(total_votes)
    #print(candidate_options)
    #print(candidate_votes)
    #print the candidate name and percentage of votes earned
    #print(f"{candidate_name}: received {vote_percentage:.1f} % of the total votes.")         