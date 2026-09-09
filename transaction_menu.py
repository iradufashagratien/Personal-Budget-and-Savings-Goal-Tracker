from data_store import load_data, save_data
from transactions import (
    add_transaction,
    view_transactions,
    update_transaction,
    delete_transaction,
    search_transactions,
    filter_transactions
)


def transaction_menu(transactions):
    data = load_data()
    transactions = data["transactions"]

    while True:
        print("\n========== TRANSACTION MANAGER ==========")
        print()
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Search Transactions")
        print("6. Filter Transactions")
        print("7. Save and Exit")
        print()
        print("=============================================")
        print()    
        choice = input("Choose an option: ")

        if choice == "1":
            add_transaction(transactions)
        elif choice == "2":
            view_transactions(transactions)
        elif choice == "3":
            update_transaction(transactions)
        elif choice == "4":
            delete_transaction(transactions)
        elif choice == "5":
            search_transactions(transactions)
        elif choice == "6":
            filter_transactions(transactions)
        elif choice == "7":
            save_data(data)
            print()
            print("Goodbye! See you next time.")
            break
        else:
            print("Invalid option. Please choose 1-7.")


if __name__ == "__main__":
    transaction_menu()