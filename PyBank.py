#Python_Homework
import os
import csv

budget_data = os.path.join("..","Resources", "budget_data.csv") 

#lists to store data
dates = []
profits_losses = []

#start counters at 0
total_months = 0
total = 0


with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        #skip header row
        csv_header = next(csvreader)

        #add dates and total them
        dates.append(row[0])
        total_months += 1

        #add profits/losses and total them
        profits_losses.append(row[1]) 
        total += int(row[1])

        #find average change 
        average_change = sum(profits_losses)/len(profits_losses)

        #find greatest increase
        greatest_increase = max(profits_losses)
        greatest_index = profits_losses.index(greatest_increase)
        greatest_date = dates[greatest_index]

        #find greatest decrease
        greatest_decrease = min(profits_losses)
        least_index = profits_losses.index(greatest_decrease)
        least_date = dates[least_index]


print("Financial Analysis")
print("-----------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total)}")
print(f"Average Change: ${str(round(average_change, 2))}")
print(f"Greatest Increase in Profits: {greatest_date} + (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {least_date} + (${str(greatest_decrease)})")


output_file = os.path.join("pybank.csv")

with open(output_file, 'w') as text:
    print(text)
    lines= text.read()
    print(lines)
    
