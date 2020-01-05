
# Import the Path from pathlib
from pathlib import Path
# Import  csv liberary 
import csv


csvpath = Path('/Users/mostafajoma/Desktop/Python-hw/budget_data.csv')

months = []
net_revenue= []
dates = []

with open(csvpath, 'r') as budget:
    csvreader = csv.reader(budget, delimiter =',')
    
    csv_header = next(csvreader)
    

   
    for rows in csvreader:
        months.append(rows[0])
        net_revenue.append(int(rows[1]))
        dates.append(str(rows[0]))


    monthly_revenue_change = []

    for j in range(1,len(net_revenue)):
        monthly_revenue_change.append((int(net_revenue[j])- int(net_revenue[j-1])))

        average = sum(monthly_revenue_change) / len(monthly_revenue_change)

    total_number_months = len(months)
    max_rev_change = max(monthly_revenue_change)
    min_rev_change = min(monthly_revenue_change)
    
    greatest_index = monthly_revenue_change.index(max(monthly_revenue_change))+1
    worst_index = monthly_revenue_change.index(min(monthly_revenue_change))+1

    greatest_date = dates[greatest_index]
    worst_date = dates[worst_index]

print(f"Financial Analysis")
print(f"-----------------------------------------------------------")
print(f"Total Months: {total_number_months}")
print(f"Total: ${sum(net_revenue)}")
print(f"Average Change ${round(average,2)}")
print(f"Greatest Increase in Profits: {(greatest_date)} ${str(max_rev_change)}")
print(f"Greatest Decrease in profits: {(worst_date)} ${str(min_rev_change)}")

with open('Financial_analysis.txt', 'w') as text:
    text.write(f"Financial Analysis")
    text.write(f"-----------------------------------------------------------")
    text.write(f"Total Months: {total_number_months}")
    text.write(f"Total: ${sum(net_revenue)}")
    text.write(f"Average Change ${round(average,2)}")
    text.write(f"Greatest Increase in Profits: {(greatest_date)} ${str(max_rev_change)}")
    text.write(f"Greatest Decrease in profits: {(worst_date)} ${str(min_rev_change)}")

