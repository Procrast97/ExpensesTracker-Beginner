import json

active = True

while active:
    print("Welcome to your Financial Manager.\nPlease fill in the following fields:")
    new_old = input("Making changes to categories or total?(y/n)\n"
                    "(Type 'end' to stop the program OR 'clear' to reset your data):\n").lower()
    if new_old == "n":
        user_busy = True
        while user_busy:
            user_updates = input("What did we do today?\n(Please specify the category name - CHECK SPELLING!)\n").lower().capitalize()
            if user_updates == "End":
                user_busy = False
                continue
            elif len(user_updates.split(" ")) > 1:
                print("Please only enter one category that you would like to update now.")
            elif any(char.isdigit() for char in user_updates) or any(char.isnumeric() for char in user_updates):
                print("Please ensure you only use characters from the English Alphabet.")

            else:
                # curr_cat = ""
                with open("data.json", "r") as file:
                    data = json.load(file)

                found = False
                for cats in data["Categories"]:
                    if cats == user_updates:
                        found = True
                        user_amount = float(input("Total Spent: "))
                        data["Categories"][cats].append(user_amount)
                        data["Total"] -= user_amount
                        data["Total Spent"]["Total"] += user_amount
                        data["Total Spent"][f"{cats}"] = sum(data["Categories"][f"{cats}"])
                        with open("data.json", "w") as file:
                             json.dump(data, file, indent=2)

                        print(f"Data updated successfully. Remaining Total is: {data['Total']}")

                if not found:
                    print("The category you entered is not valid. Please enter a valid category or create it.")

    elif new_old == "y":
        still_busy = True
        while still_busy:
            user_choice = input("Update Total or Categories (Type 'skip' to exit)? (t/c): ").lower()
            if user_choice == "skip":
                still_busy = False
            elif user_choice == "t":
                    total = input("Available Total: ")
                    try:
                        total_spending = float(total)
                        with open("data.json", "r") as file:
                            data = json.load(file)
                        data["Total"] = total_spending
                        with open("data.json", "w") as f:
                            json.dump(data, f)
                    except ValueError:
                        print("Please enter a numerical value like; '100' or '435.53'.")
            elif user_choice == "c":
                    categories = input(
                        'Which categories would you like to use? Please list them below:\n(Example on how to list - '
                        'Food, Groceries, Outings, etc.)\n')
                    with open("data.json", "r") as file:
                        data = json.load(file)
                    cat_list = categories.split(', ')
                    for item in cat_list:
                        item = item.strip().capitalize()
                        data["Categories"][f"{item}"] = []
                        data["Total Spent"][f"{item}"] = sum(data["Categories"][f"{item}"])
                    with open("data.json", "w") as file:
                        json.dump(data, file)

    elif new_old == "clear":
        with open("data.json", "r") as file:
            data = json.load(file)


        data["Categories"] = {}
        data["Total Spent"] = {"Total": 0}
        data["Total"] = 0

        with open("data.json", "w") as file:
            json.dump(data, file, indent=2)

        print("Data Reset Successful.")

    elif new_old == 'end':
        break


















