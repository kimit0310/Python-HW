import os
import csv
import sys

cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd,'Resources','election_data.csv')

# i = row count
i = 0
candidates = []
votecount = {}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])
            votecount[row[2]] = 0
        votecount[row[2]] = votecount[row[2]] + 1
        #counter place at end of for
        i = i + 1


# percent (votecount[index] / i) * 100
# total = i
# key with max value = max(votecount, key=votecount.get)
# ([*votecount][0])
print(f'''
Election Results
-------------------------
Total Votes: {i}
-------------------------'''
)
for x in range(len(candidates)):
    print(f"{[*votecount][x]}: {(votecount[[*votecount][x]])/ i * 100}% ({votecount.get([*votecount][x])})")
print(f'''-------------------------
Winner: {max(votecount, key=votecount.get)}
-------------------------
'''
)

sys.stdout = open("output.txt","w")
print(f'''
Election Results
-------------------------
Total Votes: {i}
-------------------------'''
)
for x in range(len(candidates)):
    print(f"{[*votecount][x]}: {(votecount[[*votecount][x]])/ i * 100}% ({votecount.get([*votecount][x])})")
print(f'''-------------------------
Winner: {max(votecount, key=votecount.get)}
-------------------------
'''
)
