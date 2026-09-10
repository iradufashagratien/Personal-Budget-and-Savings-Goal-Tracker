import json

FILE_NAME = "data/budget_data.json"

#Brings data from JSON file to Python to be used 
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Data file not found. Starting with empty data.")

        return {
            "transactions": [],
            "savings_goals": []
        }

    except json.JSONDecodeError:
        print("Data file is damaged. Starting with empty data.")

        return {
            "transactions": [],
            "savings_goals": []
        }

#Writing data to JSON file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
    print()
    print("Data saved successfully.")
