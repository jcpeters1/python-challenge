import os
import csv

#import budget data file
electiondata = os.path.join('election_data.csv')

canidates = {}
total = 0

#open and read our data file to collect information
with open(electiondata, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header line
    header = next(csvfile)

    for row in csvreader:

        canidate = row[2]
        total = total + 1

        if canidate in canidates:
            canidates[canidate] = canidates[canidate] + 1

        else:
            canidates[canidate] = 1

print("Election Results")
print("----------------------------")            
print(f'Total Votes: {total}')
print("----------------------------")
for canidate, num in canidates.items():
    print(f'{canidate}: {round((num / total) * 100,3)}% ({num})')
print("----------------------------")
print(f'Winner: {list(canidates.keys())[0]}')
print("----------------------------")

file = open("election_winner.txt", "w")

file.write("Election Results\n")
file.write("----------------------------\n")            
file.write(f'Total Votes: {total}\n')
file.write("----------------------------\n")
for canidate, num in canidates.items():
    file.write(f'{canidate}: {round((num / total) * 100,3)}% ({num})\n')
file.write("----------------------------\n")
file.write(f'Winner: {list(canidates.keys())[0]}\n')
file.write("----------------------------\n")
