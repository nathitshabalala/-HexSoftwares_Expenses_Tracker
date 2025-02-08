import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime



EXPENSES_FILE = "expenses.csv"

#Function to add an Expense
def add_expense(date, category, amount, description):
    #Adding an expense to the CSV file
    with open(EXPENSES_FILE,"a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense has been succefully added! \n")


#Function for viewing expenses
def view_expenses():
    #Displaying all the expenses
    try:
        print("##################### All Expenses #######################")

        reader = pd.read_csv(EXPENSES_FILE, names=["Date", "Category", "Amount", "Description"])
        print(reader)
        print("##########################################################")
    except FileNotFoundError:
        print("Could not find any expenses. Please add some expenses first \n")
       
        

#Function for filtering by category
def filter_expenses(category):
    #Filter and display expenses by category
    try:
        reader = pd.read_csv(EXPENSES_FILE, names=["Date", "Category", "Amount", "Description"])
        filtered_reader = reader[reader["Category"] == category]
        print("##################### " + category + " ##############################")
        print(filtered_reader)
        print("##########################################################")
    except FileNotFoundError:
        print("Could not find any expenses. Please add some expenses first \n")



#Function for calculating the total spending
def total_spending():
    #Calculating the total spending
    try:
        reader = pd.read_csv(EXPENSES_FILE, names=["Date", "Category", "Amount", "Description"])
        print("##################### Total Spending ##############################")
        print(f"Total spent: R{reader['Amount'].sum():.2f}")
        print("#################################################################")

    except FileNotFoundError:
        print("Could not find any expenses. Please add some expenses first \n")


#Visualize expenses
def graph_expenses():
    # Create a chart for expenses by category

    try:
        reader = pd.read_csv(EXPENSES_FILE, names=["Date", "Category", "Amount", "Description"])
        category_totals = reader.groupby("Category")["Amount"].sum()
        category_totals.plot(kind="pie", autopct= "%1.1f%%", startangle = 90)
        plt.title("Expenses By Category")
        plt.ylabel("")
        plt.show()
    except FileNotFoundError:
        print("Could not find any expenses. Please add some expenses first \n")


#Creating a simple user interface
def main():
    while True:
        print("\n")
        print("Personal Expenses Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter Expenses By Category")
        print("4. Total Expenses")
        print("5. View expenses graph")
        print("6. Exit \n")

        selection = input("Please select the desired choice: ")
        print("\n")

        if selection == "1":
            #Displaying the options to the user
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category of expense: ")
            amount = float(input("Enter the amount: "))
            description = input("Enter the description of the expense: ")
            
            #After the user has entered the inputs add the expenses
            add_expense(date, category, amount, description)

        elif selection == "2":
            #Viewing the expenses
            view_expenses()
        elif selection == "3":
            #Filtering the expenses by category
            category = input("Enter category to filter: ")
            print("\n")
            filter_expenses(category)
        elif selection == "4":
            #Viewing the total expenses
            total_spending()
        
        elif selection == "5":
            #Displaying the graph
            graph_expenses()
        elif selection == "6":
            #Exit the program
            print("Exiting..... \n")
            break
        else:
            print("Invalid option choosen. Please try again. \n")


if __name__== "__main__":
    main()
        