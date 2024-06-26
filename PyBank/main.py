import os
import csv

budget_csv = os.path.join("", "Resources", "budget_data.csv")
out_path = os.path.join("", "analysis", "budget_analysis.txt")
counter=0
pandl=0

#def find_highest_lowest(budget_csv):
    # Initialize variables to hold highest and lowest values and their dates
highest_value = float('-inf')
highest_date = None
lowest_value = float('inf')
lowest_date = None


#open and read CSV
with open(budget_csv, encoding='UTF-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    first=0
    smallest_change=0
    prevchange=0
    for row in csvreader:
        date = row[0]  
        value = float(row[1])
        monthchange=round(value - prevchange)
        #print(f"{date} {value} {monthchange} {highest_value}")
        if first == 0: #find first value to figure out total change
            first=row[1] #add first value as first value
        if monthchange > highest_value: #find highest value and date of that value while iterating through CSV
            highest_value = monthchange
            highest_date = date
        if monthchange < lowest_value: #find highest value and date of that value while iterating through CSV
            lowest_value = monthchange
            lowest_date = date    
        counter = counter + 1 # count number of rows
        pandl += float(row[1]) # Profit and loss is each value in second column summed (including negative values)
        prevchange=value
        #print(f"{row[0]}:  Total change: {monthchange} Highest value on {highest_date} is {highest_value}  Lowest value on {lowest_date} is {lowest_value}")
    curr = "{:,}".format(pandl) #display pandl as currency
    avgchange = round((float(row[1]) - float(first)) / float(counter), 2) #latest value minus first value divided by total count for average change
    
    #print all of this out
    print (f"Total Months: {counter}.") 
    print (f"Total: ${curr}.") 
    print (f"Average change: ${avgchange}.") 
    print (f"Greatest Increase in profits: {highest_date} (${highest_value})")
    print (f"Greatest Decrease in profits: {lowest_date} (${lowest_value})")

    #write summary to text file
    with open(out_path, "w") as file:
        file.write("Financial Analysis" + "\n" + "------------------------" + "\n")
        file.write("Total Months: " + str(counter) + "\n")
        file.write("Total: $" + str(curr) + "\n")
        file.write("Average change: $" + str(avgchange) + "\n") 
        file.write("Greatest Increase in profits: " + str(highest_date) + " $" + str(highest_value) + "\n")
        file.write("Greatest Decrease in profits: " + str(lowest_date) + " $" + str(lowest_value))