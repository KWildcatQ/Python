import os
import csv

csvpath = os.path.join ('..','kellenquinn', 'Desktop', 'python-challenge', 'PyBank' , 'Resources', 'budget_data.csv')



#! /usr/bin/python(version)

data=[]

with open(csvpath) as csvfile:
    #CSV Delimiter and variable for contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    # Read each row of data after the header
    for row in csvreader:
        data.append(row)

# print(data)
print(data)

# create change list
count=0
agg_sum=0
max_profit=0
min_profit=0

for each_month_profit in data: 
    count=count+1

for each_month_profit in data: # each_month_profit ======> ['Jan-18', '50'], ['Feb-18', '10000']
    # print(each_month_profit[1])
    agg_sum=int(each_month_profit[1]) + agg_sum # agg_sum=0+50 next agg_sum=50+10000

# for loop for max and min profits
for each_month_profit in data:
    if max_profit > int(each_month_profit[1]): # if max is > profit of current row then do nothing
        pass
    else: # Keep Looking for new max
       max_profit=int(each_month_profit[1])

    if min_profit < int(each_month_profit[1]): # Minimum profit
         pass
    else: # Keep looking for new min
        min_profit=int(each_month_profit[1])

changelist=[]
max_increase = 0
max_increase_range = ""
max_decrease = 0
max_decrease_range = ""
for i in range(1, len(data)):
    one_change=int(data[i][1])-int(data[i-1][1])
    changelist.append(one_change)
    # append the different to a separate list (say change_list)
    # Greatest Increase in Profits
    if one_change > max_increase:
        max_increase = one_change
        max_increase_range = data[i][0]
    elif one_change < max_decrease:
        max_decrease = one_change
        max_decrease_range = data[i][0]


# print(count)
# print(len(data))

# Title Financial Analysis
print('Financial Analysis')

# Break 
print('---------------------')

print("Total Months:", count) 

print("Total: $", agg_sum)

# Average Change
Net_monthly_change = sum(changelist) / len(changelist)
# Net Monthly Average
print(f"Average Change: ${Net_monthly_change:.2f}")
print("Greatest Increase in Profits",max_increase_range, max_increase)
print("Greatest Decrease in Profits",max_decrease_range, max_decrease)
print("Max Profit: $", max_profit)
print("Min Profit: $", min_profit)

Output=(f"Financial Analysis\n"
        f"---------------------\n"
        f"Total Months:{count}\n"
        f"Total: $ {agg_sum}\n"
        f"Average Change: ${Net_monthly_change}\n"
        f"Greatest Increase in Profits{max_increase_range, max_increase}\n"
        f"Greatest Decrease in Profits{max_decrease_range, max_decrease}\n"
        f"Max Profit: $ {max_profit}\n"
        f"Min Profit: ${min_profit}\n")

# Export the results to text file
file_to_output = os.path.join('..','kellenquinn', 'Desktop', 'python-challenge', 'PyBank' , 'Resources','PyBank.txt')
with open(file_to_output,"w")as txt_file:
    txt_file.write(Output)

