#import required modules
import csv
import os

#load files and output
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

#create a total vote counter
total_votes = 0

#create a canidate option list and canidate votes dictionary
candidate_options = []
candidate_votes= {}

#create empty string for the winning candidate and a counter 
winning_candidate = ""
winning_count = 0

#read the csv and convert it to a list of dictionaries
with open (file_to_load) as election_data:
    #reader is the csv object
    reader = csv.reader(election_data)

    #read the lead line(header)
    header = next(reader)

    #itterate through the rows of data
    for row in reader:

        #run the load animation
        print(".", end=""),

        #add to the total vote count
        total_votes = total_votes +1

        #extract the candidate name from each row(taking the third option from the row)
        candidate_name = row[2]

        #if the candidate is not in the existsing options, add it to the list
        #there are no options to start, so it adds them as it goes
        if candidate_name not in candidate_options:

            #add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            #and begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        #then add a vote to that candidate;s count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1


#print the results and export the data to our text file
#open the file and write to it
with open(file_to_output, "w") as txt_file:

    #print the final vote count(to terminal)
    election_results = (
        f"\n\nElection Results\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------\n")
    print(election_results, end="")

    #save the final vote count to our text file
    txt_file.write(election_results)

    #determine the wnner by looping through the counts of votes
    for candidate in candidate_votes:

        #gather the vote count and percentages 
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

        #determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate

        #print each candidate's voter count and percentage (to terminal)
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output, end="")
        
        #save each candidat's voter count and percentage to text file
        txt_file.write(voter_output)

    #print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"------------\n"
        f"Winner: {winning_candidate}\n"
        f"---------------------\n")
    print(winning_candidate_summary)

    #save the winning candidat's name to the text file
    txt_file.write(winning_candidate_summary)