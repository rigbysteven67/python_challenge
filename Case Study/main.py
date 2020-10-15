#%% -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:36:26 2020

@author: Steven
"""

import os
import csv

#set path
csv_path = os.path.join(r'C:\Users\Steven\gwu-arl-data-pt-09-2020-u-c\02-Homework\03-Python\02-Case-Assignment\Instructions\PyBank\Resources', 'budget_data.csv')
csv_path_output = os.path.join(r'C:\Users\Steven\Homework\python_challenge\Case Study\Analysis', 'budget_analysis.txt')
 
#open file and read it                       
with open(csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    
#skip header row
    next(csv_reader)
    
    
    count = 0
    total = 0 
    all_changes = []
#count number of months
    for row in csv_reader:
        count = count + 1
#total profit/loss
        total = total + int(row[1])  
#avg of monthly profit/loss 
        if count == 1:
            profit_loss = int(row[1])
            change = int(row[1]) - profit_loss
            #all_changes.append(change)
            profit_loss = int(row[1])
        if count >= 2:
            change = int(row[1]) - profit_loss
            all_changes.append(change)
            profit_loss = int(row[1])
            
#compute average           
    avg = int(sum(all_changes)/len(all_changes))


#max profit/loss
    max_change = all_changes[0]
    for item in all_changes:
        if max_change < item:
            max_change = item
#find position of max profit/loss
    max_pos = all_changes.index(max_change)
#min profit/loss
    min_change = all_changes[0]
    for item in all_changes:
        if min_change > item:
            min_change = item
#find position of min profit/loss
    min_pos = all_changes.index(min_change)
        
#start file at beginning
    csv_file.seek(0)
    next(csv_reader)

#find month of max profit/loss
    max_col = max_pos + 3
    x = 1
    for rows in csv_reader:
        x = x + 1
        if x == max_col:
            max_month = rows[0]

#start file at beginning
    csv_file.seek(0)
    next(csv_reader)

#find month of max profit/loss
    min_col = min_pos + 3
    x = 1
    for rows in csv_reader:
        x = x + 1
        if x == min_col:
            min_month = rows[0]
            

#find month of min and profit/loss  
output = (f'Budget Analysis\n'
    f'-------------------\n'
    f'Total Months: {count}\n'
    f'Total Profit/Loss: ${total}\n'
    f'Average Change: {avg}\n'
    f'Greatest Increase in Profits: {max_month} (${max_change})\n'
    f'Greates Decrease in Profits: {min_month} (${min_change})\n') 

print(output)  
        
#create and write text file

with open(csv_path_output, "w") as txt_file:
    txt_file.write(output)
