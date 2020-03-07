import os
import csv

csvpath = os.path.join("03-Python_homework_assignment_PyPoll_Resources_election_data.csv")

number_of_votes = 0
list_of_candidates = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        number_of_votes = number_of_votes +1
        list_of_candidates.append(row[2])
        
uniquelist = list(set(list_of_candidates))
uniquelist

results= {i: list_of_candidates.count(i) for i in uniquelist}

print (f"""Election Results
----------------------------
Total Votes: {number_of_votes}
----------------------------""")
for candidate in results:
    votes = results.get(candidate)
    percent = float(votes)/float(number_of_votes)*100
    output = f"{candidate}: {percent:.3f}% ({votes})\n"
    print(output, end="")
print ("""------------------------""")
Winner = max(results, key=results.get) 
print(f'Winner: {Winner}') 
print ("""------------------------""")

lines =[]
lines.append("Election Results")
lines.append("----------------------------")
lines.append(f'Total Votes: {number_of_votes}')
lines.append("----------------------------")
for candidate in results:
    votes = results.get(candidate)
    percent = float(votes)/float(number_of_votes)*100
    output = f"{candidate}: {percent:.3f}% ({votes})\n"
    lines.append(output)
lines.append("----------------------------")
lines.append(f'Winner:{Winner}')
lines.append("----------------------------")

with open('PyPoll_results.txt.','w') as file:
    for line in lines:
        file.write('%s\n' % line)