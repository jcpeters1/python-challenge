import os
import csv

#import budget data file
budgetdata = os.path.join('budget_data.csv')

total = 0
change = 0
prev = 0
sum_profitloss = 0

greatest_increase = 0
decrease = ()
greatest_decrease = 0
increase = ()

sum_change = 0

#open and read our data file to collect information
with open(budgetdata, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header line
    header = next(csvfile)

    for row in csvreader:

        total = total + 1
        sum_profitloss = sum_profitloss + int(row[1])

        if total > 1:
            change = int(row[1]) - prev
            sum_change = sum_change + change
            
            if change > greatest_increase:
                greatest_increase = change
                increase = row[0]

            if change < greatest_decrease:
                greatest_decrease = change
                decrease = row[0]

        prev = int(row[1])

    print()
    print("Financial Analysis")
    print("--------------------------")
    print(f'Total Months = {total}')
    print(f'Total: ${sum_profitloss}')
    print(f'Average Change: ${round(sum_change / (total - 1),2)}')
    print(f'Greatest Increase in Profits: {increase} ({greatest_increase})')
    print(f'Greatest Decrease in Profits: {decrease} ({greatest_decrease})')

file = open("budget_analysis.txt", "w")

file.write("Financial Analysis\n")
file.write("--------------------------\n")
file.write(f'Total Months = {total}\n')
file.write(f'Total: ${sum_profitloss}\n')
file.write(f'Average Change: ${round(sum_change / (total - 1),2)}\n')
file.write(f'Greatest Increase in Profits: {increase} ({greatest_increase})\n')
file.write(f'Greatest Decrease in Profits: {decrease} ({greatest_decrease})\n')