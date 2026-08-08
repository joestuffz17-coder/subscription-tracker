from datetime import datetime, date 

subscriptions = []

try:
    with open("Subscriptions.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")

            if len(parts) == 2:
                name = parts[0]
                expiry_date = parts[1]
                try:
                    expiry = datetime.strptime(expiry_date, "%Y-%m-%d").date()
                except ValueError:
                    continue

                subscriptions.append([name, expiry])
except FileNotFoundError:
    pass

while True:
    print()
    choice = input("1. Add subscription.\n2. View all subscription.\n3. Delete subscription.\n4. Exit\nChoose: ")
    print()

    if choice == "1":
        name = input("Enter subscription name: ")
        la_date = input("Expiry date (MM-DD-YYYY): ")
        print()
        today = date.today()
        expiry = datetime.strptime(la_date, "%m-%d-%Y").date()
        days_left = (expiry - today).days
        print()
        item = [name, expiry]
        subscriptions.append(item)
        print(f"Added {name}! You have {days_left} days left till subscription ends.")

    elif choice == "2": 

        today = date.today()

        for sub in subscriptions:
            days_left = (sub[1] - today).days

            if days_left <= 0:
                status = "Expired!!"
            elif days_left <= 3:
                status = "About to expire..."
            else:
                status = "Not urgent."

            print(f"Subscription: {sub[0]}, expires on {sub[1]} ({days_left} days left!) = {status}" )

    elif choice == "3":
        if len(subscriptions) == 0:
            print("Nothing to delete. Your list is empty.")
        else:
            print("--- Delete Subscription ---")
            for index, sub in enumerate(subscriptions):

                print(f"{index}: {sub[0]}, expires on {sub[1]}")
                print()
            delete = int(input("Which number do you want to delete? "))


            
            if 0 <= delete < len(subscriptions):
                subscriptions.pop(delete)     
                print("Successfully deleted!")    
            else:
                print("Invalid number. Returning to main menu.")

    elif choice == "4":

        file = open("Subscriptions.txt", "w")
        for sub in subscriptions:
            name = sub[0]
            expiry = sub[1]

            file.write(f"{name},{expiry}\n")
        file.close()

        print()
        print("goodbye!")
        break
    else:
        print("Invalid.")

