#!/usr/bin/python3
#this file contains functions that mostly calculate and analyse data
def calculate_total_income(data):
    total_income = 0
  
  # go through every transaction in data to check its type and sum them to total income 
    for transaction in data:
        if transaction["type"] == "income":
            total_income  += transaction["amount"]

    return total_income

def calculate_total_expenses(data):
    total_expenses = 0


    for transaction in data:
        if transaction["type"] == "expenses":
            total_expenses += transaction["amount"]

    return total_expenses

def calculate_balance(data):
    total_income = calculate_total_income(data)
    total_expenses =  calculate_total_expenses(data)

    return  total_income - total_expenses

def analyze_spending_by_category(data):
    #code to group expenses by category

    spending_by_category = {}  # dictionary that will store category name and its amount as value

    for transaction in data:
        if transaction["type"] == "expense":
            category = transaction["category"]
            amount = transaction["amount"]
       
       # Check if category exists and update it 
            if category in spending_by_category:
                spending_by_category[category] += amount
            else:
                spending_by_category[category] = amount

    return spending_by_category

def find_highest_spending_category(data):
    categories =  analyze_spending_by_category(data)
    
    highest_amount = 0
    highest_category = None
    

    for category, amount in categories.items():
        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

    return highest_category

def generate_monthly_summary(data):
    monthly_summary = {}
   
   # this code determines month we want to summarise 
    for transaction in data:
        month = transation["date"][:7]   #this indexing takes first 7 characters from form YYYY-MM-DD to show year and month only 

        if month not in monthly_summary:
            monthly_summary[month] = {
                    "income" : 0,
                    "expenses" : 0
                }
      # We need to decide if transation is income or expense 
        if transaction["type"] == "income":
            monthly_summary[month]["income"] += transaction["amount"]
        else:
            monthly_summary[month]["expenses"] += transaction["amount"]

    return monthly_summary

def analyze_savings_progress(data):
    
    total_income = calculate_total_income(data)
    total_expenses = calculate_total_expenses(data)

    savings = total_income - total_expenses

    if total_income > 0:
        savings_rate = (savings / total_income) * 100
    else: 
        savings_rate = 0

    return {
            "savings": savings,
            "savings_rate": savings_rate
        }

def generate_report(data):
    income = calculate_total_income(data)
    expenses = calculate_total_expenses(data)
    balance = calculate_balance(data)
    categories = analyze_spending_by_category(data)
    highest = find_highest_spending_category(data)
    monthly = generate_monthly_summary(data)
    savings = analyze_savings_progress(data)

    # this generate_report function will call all functions to display report on the screen 
