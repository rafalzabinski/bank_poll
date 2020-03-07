
import os
import csv

csvpath = os.path.join('03-Python_homework_assignment_PyBank_Resources_budget_data.csv')

Months = []
Total = []
Revenue_Change = []

with open (csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    next (csvreader,None)
    for row in csvreader:
        Total.append(int(row[1]))
        Months.append(row[0])

for x in range(1, len(Total)):
    Revenue_Change.append((int(Total[x]) - int(Total[x-1])))

greatest_increase = max(Revenue_Change)

greatest_increase_month = str(Months[Revenue_Change.index(max(Revenue_Change))+1])

greatest_decrease = min(Revenue_Change)

greatest_decrease_month = str(Months[Revenue_Change.index(min(Revenue_Change))+1])

Total_sum = sum(Total)

Average = round(sum(Revenue_Change) / len(Revenue_Change),2)

Total_Months = len(Months)

print (f"""Financial Analysis 
------------------------------ 
Total Months:{Total_Months}
Total: ${Total_sum}
Average Change: ${Average}
Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})
Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})""")

lines =[]

lines.append("Financial Analysis")
lines.append("----------------------------")
lines.append(f'Total Months:{Total_Months}')
lines.append(f'Total: ${Total_sum}')
lines.append(f'Average  Change: ${Average}')
lines.append(f'Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
lines.append(f'Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')

with open('PyBank_results.txt.','w') as file:
    for line in lines:
        file.write('%s\n' % line)