import os
import csv

# access the data
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# open the csv file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
# create the variables
    months = 0
    totalamount = 0
    totalchanges = []
    previous = 0
    great_increase = 0
    great_decrease = 0
    great_inc_month = 0
    great_dec_month = 0
    total_months = []
# set up the loop
    for row in csvreader:
 # print(row)
        months = months + 1
        totalamount = totalamount + int(row[1])
        change = int(row[1]) - previous
        previous = int(row[1])
        totalchanges.append(change)
        great_increase = max(totalchanges)
        great_decrease = min(totalchanges)
        total_months.append(row[0])
        great_inc_month = totalchanges.index(max(totalchanges))
        great_dec_month = totalchanges.index(min(totalchanges))

# print your statements
print (f"Total Months: {months}")
print (f"Total: ${totalamount}")
totalchanges.pop(0)
print (f"Average Change: ${round(sum(totalchanges)/len(totalchanges), 2)}")
print (f"Greatest Increase in Profits: {total_months[great_inc_month]} (${(str(great_increase))})")
print (f"Greatest Decrease in Profits: {total_months[great_dec_month]} (${(str(great_decrease))})")

# export results in a text file
analysis = os.path.join("Analysis", "Financial_Analysis.txt")
with open(analysis,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("---------------------------")
    file.write("\n")
    file.write(f"Total Months: {months}")
    file.write("\n")
    file.write(f"Total: ${totalamount}")
    file.write("\n")
    file.write(f"Average Change: ${round(sum(totalchanges)/len(totalchanges), 2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[great_inc_month]} (${(str(great_increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[great_dec_month]} (${(str(great_decrease))})")

#this code was prepared by Joseph DeVito for the Northwestern Data Science and Visualization Bootcamp. 