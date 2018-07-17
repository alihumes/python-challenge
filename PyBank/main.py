#name dependecies
import os
import csv

#name variables
months = []
revenue = []
revenue_change = []

#open "budget_data.csv"
file_path = os.path.join("/Users/Ali/Desktop/DataBootCamp/WASHSTL201806DATA4-Class-Repository-DATA/Week 3 - Python/Homework/PyBank/Resources/budget_data.csv")
with open(file_path,'r') as csvfile:
    csvdata = csv.reader(csvfile, delimiter=",")
    next(csvdata, None)

    for row in csvdata:
        months.append(row[0])
        revenue.append(int(row[1]))

    unique_months = set(months)    
    total_revenue = sum(revenue)

    # Calculate Change in Revenue 

    for i in range(0,len(revenue) -1): 
        revenue_change.append(int(revenue[i+1]) - int(revenue[i]))

    avg_rev_change = sum(revenue_change)/len(revenue_change)
    
    # Maximum and minumum revenue
    max_revenue = max(revenue)
    min_revenue = min(revenue)
    
    # associate dates with maximum and minimm revenue
    max_revenue_date = months[revenue.index(max_revenue)]
    min_revenue_date = months[revenue.index(min_revenue)]
    print("Financial Analysis")
    print("---------------------------")
    print("Total Months: " + str(len(unique_months)))
    print("Total Revenue: $" + str(total_revenue)) 
    print("Average Revenue Change: $" + str(avg_rev_change))
    print("Greatest Increase in Revenue: " + max_revenue_date + " ($" + str(max_revenue)+ ")")
    print("Greatest Decrease in Revenue: " + min_revenue_date + " ($" + str(min_revenue)+ ")")

# export to "txt"
output_path = os.path.join("/Users/Ali/Desktop/python-challenge/python-challenge/PyBank/", "Results.txt")

with open(output_path, "w", newline='') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write("Total Months: " + str(len(unique_months)) + "\n")
    txtfile.write("Total Revenue: $" + str(total_revenue) + "\n")
    txtfile.write("Average Revenue Change: $" + str(avg_rev_change)+"\n")
    txtfile.write("Greatest Increase in Revenue: " + max_revenue_date + " ($" + str(max_revenue) + ")" + "\n")
    txtfile.write("Greatest Decrease in Revenue: " + min_revenue_date + " ($" + str(min_revenue) + ")")
