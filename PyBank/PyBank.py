# This is PyBank 
import os  
import csv

budget_data_csv = os.path.join('..','Resources_PyBank', 'budget_data.csv')

print("Financial Analysis")
print("---------------------------------------")

def bank_data (budget_data):
    months = int(budget_data[0])
    profits_losses = int(budget_data[1])

    for months in budget_data_csv[0]:
        totalm = len(months)
    
    for profits_losses in budget_data_csv[1]: 
        net_total = sum(profits_losses)
        
    def average(profits_losses):
        length = len(profits_losses)
        total = 0.0
        for profits_losses in budget_data_csv:
            total += profits_losses
        return (total / length)

    print(f"Total Months: {int(totalm)}")
    print(f"Total: {int(net_total)}")
    print (f"Average Change: {int(average)}")
    print("Greatest increase in profit: ")
    print ("Greatest decrease in profit: ")

with open(budget_data_csv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)


            








    








