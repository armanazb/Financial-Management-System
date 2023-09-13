#!/usr/bin/env python
# coding: utf-8

# In[ ]:


expenses = []
investments = []

def add_record():
    print("Choose one of the following options to add to:")
    print("1. Expenses")
    print("2. Investments")

    option = int(input("Enter your choice: "))

    if option == 1:
        category = input("Enter the Category: ")
        try:
            value = float(input("Enter the value of expenses: "))
        except ValueError:
            print("Invalid input for value. Please enter a number.")
            return
        date = input("Enter the date (YYYY-MM-DD): ")
        expense = {"Category": category, "Value": value, "Date": date}
        expenses.append(expense)
        print("Expense successfully added")

    elif option == 2:
        category = input("Enter the Category: ")
        try:
            value = float(input("Enter the value of investment: "))
        except ValueError:
            print("Invalid input for value. Please enter a number.")
            return
        date = input("Enter the date (YYYY-MM-DD): ")
        investment = {"Category": category, "Value": value, "Date": date}
        investments.append(investment)
        print("Investment successfully added")

    else:
        print("Invalid option")

def edit_record():
    print("Which of the following would you like to edit?:")
    print("1. Expenses")
    print("2. Investments")

    option = int(input("Enter your choice: "))

    if option == 1:
        print("Expenses:")
        for i, expense in enumerate(expenses):
            print(f"{i + 1}. Category: {expense['Category']}, Value: {expense['Value']}, Date: {expense['Date']}")
        try:
            choice = int(input("Select which expense to edit by entering its number: ")) - 1
        except ValueError:
            print("Invalid input for expense number. Please enter a valid number.")
            return
        if 0 <= choice < len(expenses):
            category = input("Enter the new Category: ")
            try:
                value = float(input("Enter the new value of expenses: "))
            except ValueError:
                print("Invalid input for value. Please enter a number.")
                return
            date = input("Enter the new date (YYYY-MM-DD): ")
            expenses[choice] = {"Category": category, "Value": value, "Date": date}
            print("Expense successfully edited")
        else:
            print("Invalid choice")

    elif option == 2:
        print("Investments:")
        for i, investment in enumerate(investments):
            print(f"{i + 1}. Category: {investment['Category']}, Value: {investment['Value']}, Date: {investment['Date']}")
        try:
            choice = int(input("Select which investment to edit by entering its number: ")) - 1
        except ValueError:
            print("Invalid input for investment number. Please enter a valid number.")
            return
        if 0 <= choice < len(investments):
            category = input("Enter the new Category: ")
            try:
                value = float(input("Enter the new value of investment: "))
            except ValueError:
                print("Invalid input for value. Please enter a number.")
                return
            date = input("Enter the new date (YYYY-MM-DD): ")
            investments[choice] = {"Category": category, "Value": value, "Date": date}
            print("Investment successfully edited")
        else:
            print("Invalid choice")

    else:
        print("Invalid option")

def delete_record():
    print("From which of the following would you like to delete?:")
    print("1. Expenses")
    print("2. Investments")

    option = int(input("Enter your choice: "))

    if option == 1:
        print("Expenses:")
        for i, expense in enumerate(expenses):
            print(f"{i + 1}. Category: {expense['Category']}, Value: {expense['Value']}, Date: {expense['Date']}")
        try:
            choice = int(input("Select which expense to delete by entering its number: ")) - 1
        except ValueError:
            print("Invalid input for expense number. Please enter a valid number.")
            return
        if 0 <= choice < len(expenses):
            deleted_expense = expenses.pop(choice)
            print("Expense successfully deleted")
        else:
            print("Invalid choice")

    elif option == 2:
        print("Investments:")
        for i, investment in enumerate(investments):
            print(f"{i + 1}. Category: {investment['Category']}, Value: {investment['Value']}, Date: {investment['Date']}")
        try:
            choice = int(input("Select which investment to delete by entering its number: ")) - 1
        except ValueError:
            print("Invalid input for investment number. Please enter a valid number.")
            return
        if 0 <= choice < len(investments):
            deleted_investment = investments.pop(choice)
            print("Investment successfully deleted")
        else:
            print("Invalid choice")

    else:
        print("Invalid option")

def view_summary():
    total_expenses = sum(expense['Value'] for expense in expenses)
    total_investments = sum(investment['Value'] for investment in investments)
    net_worth = total_investments - total_expenses

    print("Total Expenses:", total_expenses)
    print("Total Investments:", total_investments)
    print("Your Net Worth is:", net_worth)

def set_limits():
    print("Which of the following options would you like to set a limit for?:")
    print("1. Expenses")
    print("2. Investments")

    option = int(input("Enter your choice: "))

    if option == 1:
        try:
            expenses_limit = float(input("Enter limit value for expenses: "))
        except ValueError:
            print("Invalid input for expenses limit. Please enter a number.")
            return
        print("Your new expense limit is:", expenses_limit)
        total_expenses = sum(expense['Value'] for expense in expenses)
        if total_expenses > expenses_limit:
            print("Your total expenses exceed the limit")

    elif option == 2:
        try:
            investments_limit = float(input("Enter limit value for investments: "))
        except ValueError:
            print("Invalid input for investments limit. Please enter a number.")
            return
        print("Your new investment limit is:", investments_limit)
        total_investments = sum(investment['Value'] for investment in investments)
        if total_investments > investments_limit:
            print("Your total investments exceed the limit")

    else:
        print("Invalid option")

def calculate_interest():
    try:
        years = int(input("Enter the amount of years being considered: "))
    except ValueError:
        print("Invalid input for years. Please enter a valid number.")
        return
    total_investments = sum(investment['Value'] for investment in investments)
    interest = total_investments * (1 + (4.5) * years)
    print("Your interest value is:", interest)

def user_interface():
    print("Welcome to the Financial Management System")

    while True:
        print("Please select one of the following options:")
        print("1. Add Record")
        print("2. Edit Record")
        print("3. Delete Record")
        print("4. View Summary")
        print("5. Set Limit")
        print("6. Calculate Interest")
        print("7. Exit")

        option = int(input("Enter your choice: "))

        if option == 1:
            add_record()
        elif option == 2:
            edit_record()
        elif option == 3:
            delete_record()
        elif option == 4:
            view_summary()
        elif option == 5:
            set_limits()
        elif option == 6:
            calculate_interest()
        elif option == 7:
            print("Thank you for using the Financial Management System!")
            break
        else:
            print("Invalid option")

user_interface()


# 
# 
