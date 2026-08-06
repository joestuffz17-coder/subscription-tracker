subscriptions = []


while True:
    print()
    choice = input("1. Add subscription.\n2. View all subscription.\n3. Exit.\n\nChoose: ")
    print()
    if choice == "1":
        name = input("Enter subscription name: ")
        date = input("Expiry date: ")
        print()
        item = [name, date]
        subscriptions.append(item)
        print(item[0])
        print(item[1])
    elif choice == "2":
        for sub in subscriptions:
            print(f"Subscription: {sub[0]}, expires on {sub[1]}.")
    elif choice == "3":
        print()
        print("goodbye!")
        break
    else:
        print("Invalid.")
