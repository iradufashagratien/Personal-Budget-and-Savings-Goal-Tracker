
#Importing the validation functions from the validation.py file to be used in this file for validating user inputs related to transactions.
from validation import get_valid_amount, get_valid_type, get_valid_date

#Check whether the first transaction's index is zero and find the next available transaction ID

def get_next_id(transactions):
    if len(transactions) == 0:
        return 1

    highest_id = 0

    for transaction in transactions:
        if transaction["id"] > highest_id:
            highest_id = transaction["id"]

    return highest_id + 1

#Add new transaction to the list 

def add_transaction(transactions):
    print("\n=== Add Transaction ===")

    print()
    
    transaction_type = get_valid_type()

    description = input("Enter the description: ")

    while description == "":
        print("Description cannot be empty.")
        description = input("Enter the description: ")

    amount = get_valid_amount()

    category = input("Enter category [Food, Entertainment, Work, Gifts, ...]: ")

    while category == "":
        print("Category cannot be empty.")
        category = input("Enter category [Food, Entertainment, Work, Gifts, ...]: ")

    date = get_valid_date()

    transaction = {
        "id": get_next_id(transactions),
        "type": transaction_type,
        "description": description,
        "amount": amount,
        "category": category,
        "date": date
    }

    transactions.append(transaction)

    print("Transaction added successfully!.")

#Viewing all transactions 
def view_transactions(transactions):
    print("\n=== All Transactions ===")

    print()

    if len(transactions) == 0:
        print("No transactions found!.")
        return

    for transaction in transactions:
        print(
            "ID:", transaction["id"],
            "|", transaction["type"],
            "|", transaction["description"],
            "| Rs", transaction["amount"],
            "|", transaction["category"],
            "|", transaction["date"]
        )

#Updating existing transaction
def update_transaction(transactions):
    print("\n=== Update Transaction ===")

    print()

    if len(transactions) == 0:
        print("No transactions to update.")
        return

    view_transactions(transactions)

    try:
        transaction_id = int(input("Enter the transaction ID to update: "))
    except ValueError:
        print("Invalid ID.")
        return

    for transaction in transactions:
        if transaction["id"] == transaction_id:

            print("Leave description or category empty to keep the old value.")

            description = input("New description: ")

            if description != "":
                transaction["description"] = description

            category = input("New category [Food, Entertainment, Work, Gifts, ...]: ")

            if category != "":
                transaction["category"] = category

            print("Enter the new amount and date below.")

            transaction["amount"] = get_valid_amount("New amount: ")
            transaction["date"] = get_valid_date()

            print("Transaction updated successfully!.")
            return

    print("Transaction not found. Please enter the valid transaction ID")

def delete_transaction(transactions):
    print("\n=== Delete Transaction ===")

    print()

    if len(transactions) == 0:
        print("No transactions to delete.")
        return

    view_transactions(transactions)

    print()

    try:
        transaction_id = int(input("Enter transaction ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    for transaction in transactions:
        if transaction["id"] == transaction_id:

            confirm = input(
                "Are you sure you want to delete it? (yes/no): "
            ).lower()

            if confirm == "yes":
                transactions.remove(transaction)
                print("Transaction deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Transaction not found. Please enter the valid transaction ID to delete")

    print()

def search_transactions(transactions):
    print("\n=== Search The Transactions ===") 

    print()

    keyword = input("Enter description to search: ").lower()

    found = False

    for transaction in transactions:
        if keyword in transaction["description"].lower():
            print(
                "ID:", transaction["id"],
                "|", transaction["description"],
                "| Rs", transaction["amount"],
                "|", transaction["type"]
            )
            found = True

    if not found:
        print("No matching transaction found!. Please review the keyword")

#Filter transactions and display data accordingly

def filter_transactions(transactions):
    print("\n=== Filter Transactions ===")

    print()

    if len(transactions) == 0:
        print("No transactions found.")
        return

    print("1. Filter by type")
    print("2. Filter by category")

    choice = input("Choose option: ")

    found = False

    if choice == "1":

        transaction_type = input(
            "Enter type (income/expense): "
        ).lower()

        for transaction in transactions:
            if transaction["type"].lower() == transaction_type:
                print(
                    "ID:", transaction["id"],
                    "|", transaction["type"],
                    "|", transaction["description"],
                    "| Rs", transaction["amount"],
                    "|", transaction["category"],
                    "|", transaction["date"]
                )
                found = True

    elif choice == "2":

        category = input("Enter category [Food, Entertainment, Work, Gifts, ...]: ").lower()

        for transaction in transactions:
            if transaction["category"].lower() == category:
                print(
                    "ID:", transaction["id"],
                    "|", transaction["type"],
                    "|", transaction["description"],
                    "| Rs", transaction["amount"],
                    "|", transaction["category"],
                    "|", transaction["date"]
                )
                found = True

    else:
        print("Invalid choice.")
        return

    if not found:
        print("No matching transactions found.")

#End of the transactions part        