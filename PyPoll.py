#PyPoll Homework
import os
import csv


election_data = os.path.join("..", "Resources", "election_data.csv")

#lists to store data
voter_ID = []
county = []
candidates = []
charles = []
diana = []
raymon = []

total_votes = 0

#open as csv file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    myList = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
    print(myList)

    for row in csvreader:
      
        #add voter ID
        voter_ID.append(row[0])

        #get total votes
        total_votes = len(row[0])
        total_votes += 1
        print(total_votes)

        #add county
        county.append(row[1])

        #add candidate
        candidate.append(row[2])

    #add up total votes per candidate
    for candidate in candidates:
        if candidate == "Charles":
            charles.append(candidates)
            charles_votes = len(charles)

        elif candidate == "Diana":
            diana.append(candidates)
            diana_votes = len(diana)

        else:
            raymon.append(candidates)
            raymon_votes = len(raymon)
    print(charles_votes)
    print(diana_votes)
    print(raymon_votes)

        if charles_votes > diana_votes and raymon_votes:
            candidate_winner = "Charles Casper Stockham"

        elif diana_votes > charles_votes and raymon_votes:
            candidate_winner = "Diana DeGette"
        
        else:
            candidate_winner = "Raymon Anthony Doane"


    #find candidate percents
    charles_percent = round(((charles_votes / total_votes)*100), 2)
    diana_percent = round(((diana_votes / total_votes)*100), 2)
    raymon_percent = round(((raymon_votes / total_votes)*100, 2)


Print("Election Results")
Print("-----------------------------")
Print(f"Total Votes: {str(total_votes)}")
Print("------------------------------")
Print(f"Charles Casper Stockham: {str(charles_percent)}% {str(charles_votes)}")
Print(f"Diana DeGette: {str(diana_percent)}% {str(diana_votes)}")
Print(f"Raymon Anthony Doane: {str(raymon_percent)} % {str(raymon_votes)}")
Print("-------------------------------")
Print("Winner: {candidate_winner}")
Print("-------------------------------")

output_file = os.path.join("pypoll.csv")

with open(output_file, 'w') as text:
    print(text)
    lines= text.read()
    print(lines) 