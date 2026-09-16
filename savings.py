from validation import get_valid_amount, get_valid_name, get_valid_goal_id

# =========== Add Goals ===============

def add_goal(data):
    saving_goals = data["savings_goals"]

    # Get a valid goal name and target using shared validation
    name = get_valid_name("Enter goal name: ", "Goal name cannot be empty.")

    target = get_valid_amount("Enter target amount: ")

    # Create goal dictionary block
    goal = {
        "id": len(saving_goals) + 1,
        "name": name,
        "target": target,
        "saved": 0
    }

    saving_goals.append(goal)
    print()
    
    print("Savings goal added!")


# ============ View Goals ==============
def view_goals(data):
    saving_goals = data["savings_goals"]

    print("\n=== All Savings Goals ===")

    print()

    # Check if there are existing goals in database
    if len(saving_goals) == 0:
        print("No savings goals yet.")
        return

    # Display goals one after the other
    for goal in saving_goals:
        progress = (goal["saved"] / goal["target"]) * 100

        if goal["saved"] >= goal["target"]:
            status = "Completed"
        else:
            status = "Incomplete"

        print(
            "ID:", goal["id"],
            "|", goal["name"],
            "| Target: Rs", goal["target"],
            "| Saved: Rs", goal["saved"],
            "| Progress:", round(progress, 2), "%",
            "|", status
        )

# ========== Update Goal ==============

def update_goal(data):
    saving_goals = data["savings_goals"]

    # Display existing goals
    view_goals(data)

    # Null check
    if len(saving_goals) == 0:
        return

    # Get valid goal ID, name and target using shared validation
    goal_id = get_valid_goal_id(saving_goals, "Which goal do you want to update (Enter Id): ")

    name = get_valid_name("Enter new goal name: ", "Goal name cannot be empty.")

    target = get_valid_amount("Enter new target amount: ")

    # Assignment of new values to goal dictionary block
    saving_goals[goal_id - 1]["name"] = name
    saving_goals[goal_id - 1]["target"] = target

    print("Savings goal updated!")


# ============ Add Money ==============
def add_money(data):
    saving_goals = data["savings_goals"]

    view_goals(data)

    # Null check
    if len(saving_goals) == 0:
        return

    # Get valid goal ID and amount using shared validation
    number = get_valid_goal_id(saving_goals, "Which goal do you want to add money to: ")

    amount = get_valid_amount("How much money do you want to add: ")

    # Update amount on goal dictionary block
    saving_goals[number - 1]["saved"] += amount

    print("Money added!")


# =========== Delete Goal =============
def delete_goal(data):
    saving_goals = data["savings_goals"]

    view_goals(data)

    # Series of checks
    if len(saving_goals) == 0:
        return

    # Get valid goal ID using shared validation
    number = get_valid_goal_id(saving_goals, "Which goal do you want to delete: ")

    # Delete goal from list
    saving_goals.pop(number - 1)

    print("Goal deleted!")
