#import modules
import os
import csv

# name variables
voter_id = []
county = []
candidate = []
unique_cand = []

#open "election_data.csv" and read
csvpath1 = os.path.join("/Users/Ali/Desktop/DataBootCamp/WASHSTL201806DATA4-Class-Repository-DATA/Week 3 - Python/Homework/PyPoll/Resources/election_data.csv")

with open(csvpath1, "r", newline='') as csvfile1:
    csvreader1 = csv.reader(csvfile1, delimiter=",")
    next(csvreader1, None)

#add  voter id and name of canidate
    for row in csvreader1:
        voter_id.append(row[0])
        candidate.append(row[2])

#new path to find winner later
'''
csvpath2 = os.path.join("/Users/Ali/Desktop/DataBootCamp/WASHSTL201806DATA4-Class-Repository-DATA/Week 3 - Python/Homework/PyPoll/Resources/election_data.csv")
with open(csvpath2, "r", newline='') as csvfile2:
    csvreader2 = csv.reader(csvfile2, delimiter=",")
    next(csvreader2, None)
    for row in csvreader2:
        voter_id.append(row[0])
        candidate.append(row[2])
'''

totalVotes = len(set(voter_id))
unique_cand = set(candidate)

#print("Candidate Count: " + str(len(set(candidate))))    

candidateVotes = dict()

for name in unique_cand:
    candidateVotes[name] = 0

poll = zip(voter_id, candidate)

for voter_id, candidate in poll:
    if candidate in candidateVotes:
        candidateVotes[candidate] += 1

#print (candidateVotes)

sortByvotes = sorted(candidateVotes.values(), reverse=True)

#print ("Winner Vote Count: " + str(sortByvotes[0]))

# find the winner
'''
for key, value in candidateVotes.items():
    if (value == sortedValues[0]) :
        Winner = key
        break
'''
Winner =  list(candidateVotes.keys())[list(candidateVotes.values()).index(sortByvotes[0])]

#print results

print("Election Results")
print("_____________________________")
print("Total Votes: " + str(totalVotes))
print("_____________________________")
for key, value in candidateVotes.items():
    print(key + ": " + str(round(((value/totalVotes)*100),2)) + "%  (" + str(value) + ")")
print("_____________________________")
print ("Winner : " + Winner)
print("_____________________________")

