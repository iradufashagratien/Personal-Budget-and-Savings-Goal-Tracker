saving_goals = []


def add_goal():
    name = input("Enter goal name: ").strip()

    if name == "":
        print("Goal name cannot be empty.")
        return

    try:
        target = float(input("Enter target amount: "))

        if target <= 0:
            print("Target amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    goal = {
        "id": len(saving_goals) + 1,
        "name": name,
        "target": target,
        "saved": 0
    }

    saving_goals.append(goal)
    print("Savings goal added!")


def view_goals():
    if len(saving_goals) == 0:
        print("No savings goals yet.")
        return

    for goal in saving_goals:
        print("\nID:", goal["id"])
        print("Goal:", goal["name"])
        print("Target:", goal["target"])
        print("Saved:", goal["saved"])

        progress = (goal["saved"] / goal["target"]) * 100
        print("Progress:", round(progress, 2), "%")

        if goal["saved"] >= goal["target"]:
            print("Status: Completed")
        else:
            print("Status: Incomplete")


def update_goal():
    view_goals()

    if len(saving_goals) == 0:
        return

    try:
        goal_id = int(input("Which goal do you want to update? "))

        if goal_id < 1 or goal_id > len(saving_goals):
            print("Invalid goal ID.")
            return

    except ValueError:
        print("Please enter a valid goal ID.")
        return

    name = input("Enter new goal name: ").strip()

    if name == "":
        print("Goal name cannot be empty.")
        return

    try:
        target = float(input("Enter new target amount: "))

        if target <= 0:
            print("Target amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    saving_goals[goal_id - 1]["name"] = name
    saving_goals[goal_id - 1]["target"] = target

    print("Savings goal updated!")


def add_money():
    view_goals()

    if len(saving_goals) == 0:
        return

    try:
        number = int(input("Which goal do you want to add money to? "))

        if number < 1 or number > len(saving_goals):
            print("Invalid goal ID.")
            return

        amount = float(input("How much money do you want to add? "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    saving_goals[number - 1]["saved"] += amount

    print("Money added!")


def delete_goal():
    view_goals()

    if len(saving_goals) == 0:
        return

    try:
        number = int(input("Which goal do you want to delete? "))

        if number < 1 or number > len(saving_goals):
            print("Invalid goal ID.")
            return

    except ValueError:
        print("Please enter a valid goal ID.")
        return

    saving_goals.pop(number - 1)

    print("Goal deleted!")

