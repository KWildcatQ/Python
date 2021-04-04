#1 /usr/bin/python(version)

import os
import csv

csvpath = os.path.join ('..', 'kellenquinn', 'Desktop','python-challenge','PyPoll','Resources','election_data.csv')

data = []
candidate_list = []
candidate_vote_count = []
with open(csvpath) as csvfile:
    #csv delimiter and variable for contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # read the header first row
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        data.append(row)

        # List of Candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

        # Get Vote Count
        candidate_vote_count.append(row[2])

# Total Number of Votes
count=0
for each_vote in data:
    count=count+1

print("Election Results")
print("------------------")
print("Total Votes:", count)
print("Candidates with Total Votes Received and Percentage of Vote:")

# Iterate through all candidates and provide count

for candidate in candidate_list:
    # Candidate Votes
    current_vote_count = candidate_vote_count.count(candidate) 
    vote_number = (current_vote_count/count)
    vote_percentage = (vote_number*100)
    voter_output = f"{candidate}: {vote_percentage:.3f}% ({current_vote_count})\n"
    print(voter_output, end="")

# Get Vote Count
candidate_list.append(row[2])
data.append(row)




