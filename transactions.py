from validation import get_valid_amount
from validation import get_valid_type
from validation import get_valid_date

#Check whether the transactions and find the next available transaction ID

def get_next_id(transactions):
    if len(transactions) == 0:
        return 1

    highest_id = 0

    for transaction in transactions:
        if transaction["id"] > highest_id:
            highest_id = transaction["id"]

    return highest_id + 1

#Add new transac to the list 

def add_transaction(transactions):
    print("\n=== Add Transaction ===")

    transaction_type = get_valid_type()

    description = input("Enter the description: ")

    while description == "":
        print("Description cannot be empty.")
        description = input("Enter the description: ")

    amount = get_valid_amount()

    category = input("Enter category: ")

    while category == "":
        print("Category cannot be empty.")
        category = input("Enter category: ")

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

            print("Leave the description empty to keep the old value.")

            description = input(
                "New description: "
            )

            if description != "":
                transaction["description"] = description

            amount = input("New amount: ")

            if amount != "":
                try:
                    amount = float(amount)

                    if amount > 0:
                        transaction["amount"] = amount
                    else:
                        print("Amount must be greater than 0.")
                        return

                except ValueError:
                    print("Invalid amount.")
                    return

            category = input("New category: ")

            if category != "":
                transaction["category"] = category

            date = input("New date (YYYY-MM-DD): ")

            if date != "":
                transaction["date"] = date

            print("Transaction updated successfully!.")
            return

    print("Transaction not found. Please enter the valid transaction ID")


def delete_transaction(transactions):
    print("\n=== Delete Transaction ===")

    if len(transactions) == 0:
        print("No transactions to delete.")
        return

    view_transactions(transactions)

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


def search_transactions(transactions):
    print("\n=== Search The Transactions ")

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
        print("No matching transactions found. Please review the keyword")

#Filter transactions and display data accordingly

def filter_transactions(transactions):
    print("\n=== Filter Transactions ===")

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

        category = input("Enter category: ").lower()

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