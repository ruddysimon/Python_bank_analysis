import os
import csv

# CSV FILE LOCATION 
csv_file = os.path.join("Resources", "election_data.csv")

# LIST TO STORE DATA
Total_votes = 0
candidates = {}

# OPEN AND READ THE CSV_FILE
with open(csv_file, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # SKIP THE HEADER
    csv_header = next(csv_reader)

    # TOTAL VOTES 
    for row in csv_reader:
        Total_votes += 1

        # IF/ELSE STATEMENT 
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

        
    # PRINT THE VALUES
    print("Election Results")
    print("_____________________")
    print("Total_votes :" , str(Total_votes))
    print("________________________")


    # CANDIDATES NAMES AND TOTAL VOTES FOR EACH ONE   
    #candidates_names = []
    #candidates_votes = []

    #for key,value in candidates.items():
        #candidates_names.append(key)
        #candidates_votes.append(value)


    # CANDIDATES PERCENTAGE
    candidates_percentage = {}  
    
    for key,value in candidates.items():
        candidates_percentage[key] = round((value / Total_votes) * 100 ,1)
        


# FIND THE WINNER
winner_count = 0
winner = ""

for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

for key, value in candidates.items():

    print(key + ": " + str(candidates_percentage[key]) + "% (" + str(value) + ")")
print("_____________________________________")
print("Winner: " + winner)
print("_____________________________________")
        
# PRINT AS A TEXT FILE
export_file = os.path.join("Final_Data.txt")

with open(export_file,"w", newline = "") as txt_file:
    csv_writer = csv.writer(txt_file)


    csv_writer.writerow(["Election Results"])
    csv_writer.writerow(["_____________________"])
    csv_writer.writerow(["Total_votes :" , str(Total_votes)])
    csv_writer.writerow(["________________________"])
    for key, value in candidates.items():
    
        csv_writer.writerow([key + ": " + str(candidates_percentage[key]) + "% (" + str(value) + ")"])
    csv_writer.writerow(["____________________________________"])
    csv_writer.writerow(["Winner: " + winner])
    csv_writer.writerow(["____________________________________"])

