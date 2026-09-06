goals = []


def add_goal():
    name = input("Enter goal name: ")
    target = float(input("Enter target amount: "))

    goal = {
        "id": len(goals) + 1,
        "name": name,
        "target": target,
        "saved": 0
    }

    goals.append(goal)
    print("Savings goal added!")


def view_goals():
    if len(goals) == 0:
        print("No savings goals yet.")
        return

    for goal in goals:
        print("\nID:", goal["id"])
        print("Goal:", goal["name"])
        print("Target:", goal["target"])
        print("Saved:", goal["saved"])

        progress = (goal["saved"] / goal["target"]) * 100
        print("Progress:", round(progress, 2), "%")



def add_money():
    view_goals()

    if len(goals) == 0:
        return

    number = int(input("Which goal do you want to add money to? ")) - 1
    amount = float(input("How much money do you want to add? "))

    goals[number]["saved"] += amount

    print("Money added!")


def delete_goal():
    view_goals()

    if len(goals) == 0:
        return

    number = int(input("Which goal do you want to delete? ")) - 1

    goals.pop(number)

    print("Goal deleted!")


if __name__ == "__main__":

    while True:
        print("\n===== SAVINGS GOALS =====")
        print("1. Add goal")
        print("2. View goals")
        print("3. Add money")
        print("4. Delete goal")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_goal()

        elif choice == "2":
            view_goals()

        elif choice == "3":
            add_money()

        elif choice == "4":
            delete_goal()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")