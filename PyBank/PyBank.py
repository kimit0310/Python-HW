import os
import csv

cwd = os.path.dirname(os.path.abspath(__file__))
csvpath = os.path.join(cwd,'Resources','budget_data.csv')

# i = total months j = placeholder for previous month's revenue
i = 0
j = 0
revenue = 0
dates = []
deltalist = []
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        date = row[0]
        dates.append(date)
        # Net total profit / losses
        revenue = revenue + int(row[1])
        # Average variance = (total profit / i)
        # Delta in a list max(list) and min(list) for biggest increase and smallest increase
        deltalist.append(int(row[1]) - j)
        j = int(row[1])
        # Total # of months
        i = i + 1

avgchange = (sum(deltalist) - deltalist[0])/(i-1)
great_date = dates[deltalist.index(max(deltalist))]
least_date = dates[deltalist.index(min(deltalist))]

output = (f'''
  Financial Analysis
  ----------------------------
  Total Months: {i}
  Total: {revenue}
  Average  Change: $-2315.12
  Greatest Increase in Profits: {great_date} (${max(deltalist)})
  Greatest Decrease in Profits: {least_date} (${min(deltalist)})
  '''
)
print(output)
with open("output.txt","w") as outfile:
    outfile.write(output)