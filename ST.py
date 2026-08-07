subscriptions = []


while True:
    print()
    choice = input("1. Add subscription.\n2. View all subscription.\n3. Delete subscription.\n4. Exit\nChoose: ")
    print()
    if choice == "1":
        name = input("Enter subscription name: ")
        date = input("Expiry date: ")
        print()
        item = [name, date]
        subscriptions.append(item)
    elif choice == "2":
        for sub in subscriptions:
            print(f"Subscription: {sub[0]}, expires on {sub[1]}.")
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
        print()
        print("goodbye!")
        break
    else:
        print("Invalid.")

