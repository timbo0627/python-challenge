import os
import csv

election_csv = os.path.join("", "Resources", "election_data.csv")
out_path = os.path.join("", "analysis", "election_analysis.txt")

with open(election_csv, encoding='UTF-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    counter=0
    unique_candidates = set()
    candidate_votes = {}
    for row in csvreader:
        counter=counter + 1 #count the votes as we iterate over csv rows
        candidate=row[2]
        if candidate in candidate_votes:
             candidate_votes[candidate] += 1
        else:
             candidate_votes[candidate] = 1
        #candidate = row[2]
        #if candidate is not None:
        #    unique_candidates.add(candidate)
        
    #for candidate in unique_candidates:
        #print(candidate)      
    


    total_votes=0
    percent_votes=0
    winner=0    
    #write summary to text file
    with open(out_path, "w") as file:    
        print("\n\n\nElection Results")
        print("----------------------")
        print(f"Total Votes:  {counter}")
        print("----------------------")
        file.write("Election Results" + "\n" + "----------------------")
        file.write("\n" + "Total Votes: " + str(counter) )
        file.write("\n" + "----------------------" + "\n")
        for candidate, votes in candidate_votes.items():
            percentOfVote=(votes/counter) * 100
            if percentOfVote > winner:
                winner=percentOfVote
                winner_candidate=candidate
            total_votes=total_votes+ votes
            percent_votes=(votes/counter*100)
            percent_votes="{:.3f}%".format(percent_votes)
            #print (f"{percent_votes}")
            print(f"{candidate}: {percent_votes} ({votes})")
            file.write(str(candidate) + ": " + str(percent_votes) + " (" + str(votes) + ")\n")
        print("----------------------")
        print(f"Winner: {winner_candidate}")
        print("----------------------")
        file.write("----------------------" + "\n")
        file.write("Winner: " + winner_candidate)
        file.write("\n" + "----------------------" + "\n")