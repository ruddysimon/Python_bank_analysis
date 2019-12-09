import os
import csv

# CSV FILE
csv_file = os.path.join("Resources","budget_data.csv")
dict_data = []
print('')
# OPEN AND READ THE CSV FILE
with open(csv_file, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # SKIP THE ROW IF THERE IS NO HEADER
    csv_header = next(csv_reader)
    # print(f"CSV HEADER : {csv_header}")

    # CREATE A DICTIONARY FOR LOOPING THROUGH THE ROWS IN ORDER TO FIND THE TOTAL NET AND TOTAL MONTHS
    for row in csv_reader:
        dict_data_this ={}
        dict_data_this['month'] = row[0]
        dict_data_this['profit'] = int(row[1])
        dict_data.append(dict_data_this)

 
profit_list = [k['profit'] for k in dict_data]
profit_list_change = [x1 - x2 for (x1, x2) in zip(profit_list[1:], profit_list[:-1])] 
gratest_increase_id = profit_list_change.index(max(profit_list_change)) + 1
gratest_decrease_id = profit_list_change.index(min(profit_list_change)) + 1

# PRINT THE FINAL VALUES
print("Financial Analysis")
print("_________________________")
print("Total Months:{}".format( len(dict_data) ) )
print("Total Revenue: ${}".format( sum( profit_list ) ) )
print("Average Revenue: ${}".format( sum( profit_list_change ) / (len(dict_data) - 1) ) )
print("Greatest Increase in Profits: {} (${})".format( dict_data[gratest_increase_id]['month'] , profit_list_change[gratest_increase_id - 1] ) )
print("Greatest Decrease in Profits: {} (${})".format( dict_data[gratest_decrease_id]['month'] , profit_list_change[gratest_decrease_id - 1] ) )















