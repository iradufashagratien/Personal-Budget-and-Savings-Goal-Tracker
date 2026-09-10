import savings


def savings_menu():
    while True:
        print("\n===== SAVINGS GOALS =====")
        print()
        print("1. Add goal")
        print("2. View goals")
        print("3. Update goal")
        print("4. Add money")
        print("5. Delete goal")
        print("6. Exit")
        print("\n==========================")
        print()

        choice = input("Choose an option: ")

        if choice == "1":
            savings.add_goal()

        elif choice == "2":
            savings.view_goals()

        elif choice == "3":
            savings.update_goal()

        elif choice == "4":
            savings.add_money()

        elif choice == "5":
            savings.delete_goal()

        elif choice == "6":
            break

        else:
            print()
            print("Invalid choice.")

