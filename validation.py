def get_valid_amount(prompt="Enter amount in MUR: "):
    while True:
        try:
            amount = float(input(prompt))

            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")


def get_valid_type():
    while True:
        transaction_type = input(
            "Enter type (income/expense): "
        ).lower()

        if transaction_type == "income":
            return transaction_type

        if transaction_type == "expense":
            return transaction_type

        print("Please enter either income or expense.")


def get_valid_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        if len(date) == 10 and date[4] == "-" and date[7] == "-":
            return date

        print("Please use YYYY-MM-DD format.")


def get_valid_name(prompt, empty_message="Name cannot be empty."):
    while True:
        name = input(prompt).strip()

        if name == "":
            print(empty_message)
        else:
            return name


def get_valid_goal_id(saving_goals, prompt):
    while True:
        try:
            goal_id = int(input(prompt))

            if goal_id < 1 or goal_id > len(saving_goals):
                print("Invalid goal ID.")
            else:
                return goal_id

        except ValueError:
            print("Please enter a valid goal ID.")