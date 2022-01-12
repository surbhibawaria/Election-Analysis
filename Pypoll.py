# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it to the candidate list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Add begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0   
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        
for candidate_name in candidate_votes:     
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print out each candidate's name, vote count, and percentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

    # Determine winning vote count, winning percentage, and candidate.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

# Print the winning candidates' result to the terminal.
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winner Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"---------------------------\n")
print(winning_candidate_summary)
    
# To do: print out the winning candidate, vote count and percentage to terminal.
                      
# Print the candidate vote dictionary.
# print(candidate_votes)
            
    # To do: read and analyze the data here.
    # Print the file object
    #print(election_data)
    # Using the open() function with the "w" mode we will write data to the file.
    #open(file_to_save, "w")
    # Create a filename variable to a direct or indirect path to the file.
    #file_to_save = os.path.join("analysis", "election_analysis.txt")
    # Using the with statement to open the file as a text file.
    #with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
    #txt_file.write("Counties in the Election")
    #txt_file.write("\n-------------------------")
    #txt_file.write("\nArapahoe\nDenver\nJefferson") 


