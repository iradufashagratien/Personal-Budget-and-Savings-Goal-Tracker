import processing

def processing_menu(data):
    while True:
        print("\n===== FINANCIAL ANALYSIS =====")
        print()
        print("1. Total income")
        print("2. Total expenses")
        print("3. Current balance")
        print("4. Spending by category")
        print("5. Highest spending category")
        print("6. Monthly summary")
        print("7. Savings progress")
        print("8. Full financial report")
        print("9. Back to main menu")
        print("\n===============================")
        print()

        choice = input("Choose an option: ")

        if choice == "1":
            total_income = processing.calculate_total_income(data)
            print("\nTotal income: Rs", total_income)

        elif choice == "2":
            total_expenses = processing.calculate_total_expenses(data)
            print("\nTotal expenses: Rs", total_expenses)

        elif choice == "3":
            balance = processing.calculate_balance(data)
            print("\nCurrent balance: Rs", balance)

        elif choice == "4":
            categories = processing.analyze_spending_by_category(data)

            print("\nSpending by category:")

            if len(categories) == 0:
                print("No expenses found.")
            else:
                for category, amount in categories.items():
                    print(category, ": Rs", amount)

        elif choice == "5":
            highest = processing.find_highest_spending_category(data)

            if highest is None:
                print("\nNo expenses found.")
            else:
                print("\nHighest spending category:", highest)

        elif choice == "6":
            monthly = processing.generate_monthly_summary(data)

            print("\nMonthly summary:")

            if len(monthly) == 0:
                print("No transactions found.")
            else:
                for month, summary in monthly.items():
                    print(
                        month,
                        "| Income: Rs", summary["income"],
                        "| Expenses: Rs", summary["expenses"]
                    )

        elif choice == "7":
            savings = processing.analyze_savings_progress(data)

            print("\nSavings progress:")
            print("Savings: Rs", savings["savings"])
            print(
                "Savings rate:",
                round(savings["savings_rate"], 2),
                "%"
            )

        elif choice == "8":
            processing.generate_report(data)

        elif choice == "9":
            break

        else:
            print("Invalid choice. Please try again.")