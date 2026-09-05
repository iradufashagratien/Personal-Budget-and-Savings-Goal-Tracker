def get_next_goal_id(goals):
    if len(goals) == 0:
        return 1

    highest_id = 0

    for goal in goals:
        if goal["id"] > highest_id:
            highest_id = goal["id"]

    return highest_id + 1


def create_goal(goals):
    print("\n--- Create Savings Goal ---")

    name = input("Enter goal name: ")

    while name == "":
        print("Goal name cannot be empty.")
        name = input("Enter goal name: ")

    try:
        target = float(input("Enter target amount: "))

        if target <= 0:
            print("Target must be greater than 0.")
            return

    except ValueError:
        print("Invalid amount.")
        return

    goal = {
        "id": get_next_goal_id(goals),
        "name": name,
        "target": target,
        "saved": 0
    }

    goals.append(goal)

    print("Savings goal created successfully.")


def view_goals(goals):
    print("\n--- Savings Goals ---")

    if len(goals) == 0:
        print("No savings goals found.")
        return

    for goal in goals:
        percentage = (goal["saved"] / goal["target"]) * 100

        if percentage > 100:
            percentage = 100

        print(
            "ID:", goal["id"],
            "|", goal["name"],
            "| Saved: Rs", goal["saved"],
            "| Target: Rs", goal["target"],
            "| Progress:", round(percentage, 1), "%"
        )


def add_savings(goals):
    print("\n--- Add Savings ---")

    if len(goals) == 0:
        print("No savings goals found.")
        return

    view_goals(goals)

    try:
        goal_id = int(input("Enter goal ID: "))
        amount = float(input("Enter amount to add: "))
    except ValueError:
        print("Invalid input.")
        return

    if amount <= 0:
        print("Amount must be greater than 0.")
        return

    for goal in goals:
        if goal["id"] == goal_id:
            goal["saved"] += amount

            print("Savings added successfully.")
            return

    print("Goal not found.")


def update_goal(goals):
    print("\n--- Update Savings Goal ---")

    view_goals(goals)

    try:
        goal_id = int(input("Enter goal ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for goal in goals:
        if goal["id"] == goal_id:

            name = input("New goal name: ")

            if name != "":
                goal["name"] = name

            target = input("New target amount: ")

            if target != "":
                try:
                    target = float(target)

                    if target > 0:
                        goal["target"] = target
                    else:
                        print("Target must be greater than 0.")
                        return

                except ValueError:
                    print("Invalid amount.")
                    return

            print("Goal updated successfully.")
            return

    print("Goal not found.")


def delete_goal(goals):
    print("\n--- Delete Savings Goal ---")

    view_goals(goals)

    try:
        goal_id = int(input("Enter goal ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    for goal in goals:
        if goal["id"] == goal_id:

            confirm = input(
                "Are you sure? (yes/no): "
            ).lower()

            if confirm == "yes":
                goals.remove(goal)
                print("Goal deleted successfully.")
            else:
                print("Deletion cancelled.")

            return

    print("Goal not found.")