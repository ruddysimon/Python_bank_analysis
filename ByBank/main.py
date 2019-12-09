import os
import csv

# CSV FILE
csv_file = os.path.join("Resources","budget_data.csv")

# LIST TO STORE DATA
total_month = []
net_total = []
average_change_total= []
average_change = []
great_pdecrease = []
great_pincrease = []


# OPEN AND READ THE CSV FILE
with open(csv_file, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
   

    # SKIP THE ROW IF THERE IS NO HEADER
    csv_header = next(csv_reader)
    # print(f"CSV HEADER : {csv_header}")

    # LOOPING THROUGH THE ROWS IN ORDER TO FIND THE TOTAL NET AND TOTAL MONTHS
    for row in csv_reader:
        net_total.append(float(row[1]))
        total_month.append(row[0])

       
    # PRINT THE TOTAL MONTHS AND TOTAL REVENUE
    print("Financial Analysis")
    print("_________________________")
    print("Total Months :", len(total_month))
    print("Total Revenue : $", sum(net_total))
   




#TOTAL DIFFERENCE OF AVERAGE
    for i in range(1,len(net_total)):
        average_change.append(net_total[i] - net_total[i-1])
        average_change_total = sum(average_change)/len(average_change)


    # PRINT THE AVERAGE CHANGE      
    print("Average Change : $" , float(average_change_total))
    

# FIND GREATEST INCREASE AND DECREASE CHANGE
great_pdecrease = min(average_change)
great_pincrease = max(average_change)

# FIND GREATEST INCREASE AND DECREASE DATES 
max_increase_date = str(total_month[average_change.index(max(average_change))])
min_decrease_date = str(total_month[average_change.index(min(average_change))])

# PRINT THE MAXIMUM INCREASE DATE AND MINIMUM INCREASE DATE
print("Greatest Increase In Profits :",max_increase_date,"($" , great_pincrease,")")
print("Greatest Decrease In Profits :",min_decrease_date,"($" , great_pdecrease,")")

# PRINT AS TEXT FILE
text_export = os.path.join("Data_financial.csv")

with open(text_export,"w",newline="") as text_file:
    csv_writer = csv.writer(text_file)


    csv_writer.writerow(["Financial Analysis"])
    csv_writer.writerow(["_________________________"])
    csv_writer.writerow(["Total Months :", len(total_month)])
    csv_writer.writerow(["Total Revenue : $", sum(net_total)])
    csv_writer.writerow(["Average Change : $" , float(average_change_total)])
    csv_writer.writerow(["Greatest Increase In Profits :",max_increase_date,"($" , great_pincrease,")"])
    csv_writer.writerow(["Greatest Decrease In Profits :",min_decrease_date,"($" , great_pdecrease,")"])














