import json

#Defining the file name for the JSON data storage using constant variable. This variable is used to specify the path and name of the JSON file where the budget and savings goal data will be stored

FILE_NAME = "data/budget_data.json"

#Brings data from JSON file to Python to be used (Read JSON file)

def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
#An error handling method in case the JSON file is not found or does not exist.
    except FileNotFoundError:
        print("Data file not found. Starting with empty data.")

        return {
            "transactions": [],
            "savings_goals": []
        }
  #An error handling method in case the JSON file is written incorrectly or damaged anyhow.
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
