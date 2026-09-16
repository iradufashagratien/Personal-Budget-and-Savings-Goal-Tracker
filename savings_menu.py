import savings


def savings_menu(data):
    while True:
        print("\n===== SAVINGS GOALS =====")
        print("1. Add goal")
        print("2. View goals")
        print("3. Update goal")
        print("4. Add money")
        print("5. Delete goal")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            savings.add_goal(data)

        elif choice == "2":
            savings.view_goals(data)

        elif choice == "3":
            savings.update_goal(data)

        elif choice == "4":
            savings.add_money(data)

        elif choice == "5":
            savings.delete_goal(data)

        elif choice == "6":
            break

        else:
            print("Invalid choice.")