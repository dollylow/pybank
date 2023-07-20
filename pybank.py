#Your task is to create a Python script that analyzes the records to calculate each of the following values:

import os
import csv

Mydatacsv = os.path.join('pybank', 'Resources', 'budget_data.csv')

with open(Mydatacsv, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter = ',')

    header = next(reader) 
    months = 0
    net = 0
    revenue = []
    date = []
    rev_change = []
    profit_change_mthly =[]

    for row in reader:

        date.append(row[0])
        revenue.append(int(row[1]))
        

#The total number of months included in the dataset
    for row in reader:
        months = months +1
        
#The net total amount of "Profit/Losses" over the entire period
        net = sum(revenue)
print("Financial Analysis")
print("-----------------------------------")
print("Total Months:", len(date))
print("Total Revenue: $", sum(revenue))

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))])
        

print("Average Revenue Change: $",round(avg_rev_change))
print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")


#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
output_file=os.path.join("pybank","Financial_analysis.txt")

with open(output_file,"w") as file:
    
# Write methods to print to Financial_Analysis_Summary 
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(date)}")
    file.write("\n")
    file.write(f"Total: ${sum(revenue)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(rev_change)/len(rev_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits:{max_rev_change_date} (${(str(max_rev_change))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits:{min_rev_change_date} (${(str(min_rev_change))})")