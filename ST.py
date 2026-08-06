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
        for index, sub in enumerate(subscriptions):
            print()
            print(f"Subscription: {sub[0]}, expires on {sub[1]}.")
            print()
            print(index, sub)
        delete = input("Which number do you want to delete? ")
                    
    elif choice == "4":
        print()
        print("goodbye!")
        break
    else:
        print("Invalid.")
