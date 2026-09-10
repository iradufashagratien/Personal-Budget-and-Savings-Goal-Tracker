import transaction_menu
import savings_menu
import processing_menu
from data_store import load_data, save_data


def main():
    # Load existing data when the program starts
    data = load_data()

    while True:
        print("\n===== PERSONAL BUDGET & SAVINGS TRACKER =====")
        print("1. Income & Expenses")
        print("2. Savings Goals")
        print("3. Financial Analysis")
        print("4. Exit")
        print()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            transaction_menu.transaction_menu(data["transactions"])

        elif choice == "2":
            savings_menu.savings_menu()

        elif choice == "3":
            processing_menu.processing_menu(data["transactions"])

        elif choice == "4":
            save_data(data)
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()