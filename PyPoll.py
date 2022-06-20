#The data we need to retrieve
#1. Total number of votes cast
#2. Complete list of candidates who received votes
#3. Total number of votes received by each candidate.
#4. Percentage of votes receieved by each candidate.
#5. Winner of the election based on popular vote.

#Import dependencies
import csv
import os

#Assign a variable for the .csv file to load and the path (DIRECT)
file_to_load = 'c:/Users/ssteffen/desktop/sam/Vanderbilt Boot Camp/MyRepo/Module 3_Python/Election-Analysis/Resources/election_results.csv'

#Assign a variable for the .csv file to load a file from a path(INDIRECT)
#import os
#file_to_load = os.path.join("C:","Users","ssteffen","desktop","sam","Vanderbilt Boot Camp","MyRepo","Module 3_Python","Election-Analysis", "Resources", "election_results.csv")

#Create a filename variable to a direct or indirect path to the file we want to save
#file_to_save = os.path.join("analysis", "election_analysis.txt")
file_to_save = 'c:/Users/ssteffen/desktop/sam/Vanderbilt Boot Camp/MyRepo/Module 3_Python/Election-Analysis/Analysis/election_analysis.txt'

#use the open function to open the file as a text file
#outfile = open(file_to_save, "w")

#open the election results and read the file
#alternate: election_data = open(file_to_load, 'r')
#Close the file
#election_data.close()

#access the data
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    #create a variable that contains the csv data
    file_reader = csv.reader(election_data)

#print each row in the .csv file
 #   for row in file_reader:
 #       print(row)

#print the header row
    headers = next(file_reader)
    print(headers)

#write some data to the file
#outfile.write("Hello World")

#close the file
#outfile.close()

#REFACTOR code to open and write using a with statement
#with open(file_to_save, "w") as txt_file:
    #write 3 counties to the file
#    txt_file.write("Counties in the Election\n--------------------\nArapahoe \nDenver \nJefferson")
  