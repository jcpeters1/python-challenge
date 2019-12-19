import os
import csv

#import budget data file
budgetdata = os.path.join('budget_data.csv')

total = 0
change = 0
prev = 0

greatest_incrase = 0
sum_change = 0

#open and read our data file to collect information
with open(budgetdata, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=' ')
    
    #skip header line
    header = next(csvfile)

    for row in csvreader:

        total = total + 1
        if total > 1:
            change = row[1] - prev

            sum_change = sum_change + change

            if change > greatest_increase:
                greatest_increase = change

        prev = int(row[1])

    print(f'{total}')
    print(f'{change}')
    print(f'{sum_change}')
    print(f'{greatest_increase}')
    print(f'{prev}')