import data_store
import transactions
import processing
import savings


def transaction_menu(transaction_list):
    while True:
        print("\n===== TRANSACTION MANAGEMENT =====")
        print("1. Add transaction")
        print("2. View transactions")
        print("3. Update transaction")
        print("4. Delete transaction")
        print("5. Search transactions")
        print("6. Filter transactions")
        print("7. Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            transactions.add_transaction(transaction_list)

        elif choice == "2":
            transactions.view_transactions(transaction_list)

        elif choice == "3":
            transactions.update_transaction(transaction_list)

        elif choice == "4":
            transactions.delete_transaction(transaction_list)

        elif choice == "5":
            transactions.search_transactions(transaction_list)

        elif choice == "6":
            transactions.filter_transactions(transaction_list)

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please try again.")


def savings_menu():
    while True:
        print("\n===== SAVINGS GOALS =====")
        print("1. Add savings goal")
        print("2. View savings goals")
        print("3. Add money to goal")
        print("4. Delete savings goal")
        print("5. Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            savings.add_goal()

        elif choice == "2":
            savings.view_goals()

        elif choice == "3":
            savings.add_money()

        elif choice == "4":
            savings.delete_goal()

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")


def analysis_menu(transaction_list):
    while True:
        print("\n===== FINANCIAL ANALYSIS =====")
        print("1. Calculate total income")
        print("2. Calculate total expenses")
        print("3. Calculate balance")
        print("4. Spending by category")
        print("5. Highest spending category")
        print("6. Monthly summary")
        print("7. Savings analysis")
        print("8. Full report")
        print("9. Back to main menu")

        choice = input("Choose an option: ")

        if choice == "1":
            income = processing.calculate_total_income(transaction_list)
            print("Total income: Rs", income)

        elif choice == "2":
            expenses = processing.calculate_total_expenses(
                transaction_list
            )
            print("Total expenses: Rs", expenses)

        elif choice == "3":
            balance = processing.calculate_balance(transaction_list)
            print("Current balance: Rs", balance)

        elif choice == "4":
            categories = processing.analyze_spending_by_category(
                transaction_list
            )

            print("\n===== SPENDING BY CATEGORY =====")

            if len(categories) == 0:
                print("No expenses found.")

            else:
                for category, amount in categories.items():
                    print(category, ": Rs", amount)

        elif choice == "5":
            highest = processing.find_highest_spending_category(
                transaction_list
            )

            print("\n===== HIGHEST SPENDING CATEGORY =====")

            if highest is None:
                print("No expenses found.")

            else:
                print("Highest spending category:", highest)

        elif choice == "6":
            monthly = processing.generate_monthly_summary(
                transaction_list
            )

            print("\n===== MONTHLY SUMMARY =====")

            if len(monthly) == 0:
                print("No transaction data available.")

            else:
                for month, summary in monthly.items():
                    print("\nMonth:", month)
                    print("Income: Rs", summary["income"])
                    print("Expenses: Rs", summary["expenses"])

        elif choice == "7":
            savings_progress = processing.analyze_savings_progress(
                transaction_list
            )
            print("\n===== SAVINGS ANALYSIS =====")
            print(
                "Savings: Rs",
                savings_progress["savings"]
            )
            print(
                "Savings rate:",
                round(savings_progress["savings_rate"], 2),
                "%"
            )
        elif choice == "8":
            processing.generate_report(transaction_list)

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please try again.")

def main():

    # Load data from the JSON file
    data = data_store.load_data()

    # Get the transaction list
    transaction_list = data["transactions"]

    # Connect savings goals to the loaded data
    savings.goals = data["savings_goals"]

    while True:

        print("\n================================")
        print("   PERSONAL BUDGET TRACKER")
        print("================================")
        print("1. Transaction Management")
        print("2. Savings Goals")
        print("3. Financial Analysis")
        print("4. Save Data")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            transaction_menu(transaction_list)
        elif choice == "2":
            savings_menu()
        elif choice == "3":
            analysis_menu(transaction_list)
        elif choice == "4":
            data_store.save_data(data)
        elif choice == "5":
            data_store.save_data(data)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()