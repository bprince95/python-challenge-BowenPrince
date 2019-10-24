


for dates in budget_data_csv:
    total += dates
    print("Total Months :")
    print(total)

for profits_losses in budget_data_csv: 
    net_total += profits_losses
    print("Net total profits/ losses :")
    print(net_total)

for profits_losses in budget_data_csv:
    Average = (net_total / len(profits_losses))
    print("Average of Change : ")
    print(Average)


#total_months = len(dates)
#    net_total = (profits_losses)

with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    


# calucluate total number of months 
# calculate net total amount of profits/ losses over entire period
# average of changes in the profits / losses over entire period 
# the greatest increase in profits (dates and amounts) over the entire period 
# the greatest decrease in profits (dates and amounts ) over the entire period 
# print analysis and export a text file with results#


def month_total(dates):
    month_total = len(dates)

print(month_total)

def average(budget_data_csv):
    profits_losses = int(budget_data_csv[1])
    length = len(profits_losses)
    total = 0.0
    for profits_losses in budget_data_csv[1]:
        total += profits_losses
    return total / length

print(average)