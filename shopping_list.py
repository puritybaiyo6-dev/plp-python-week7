
shopping_list = []

while True:
    print("\n--- Shopping List Manager ---")
    print("add / remove / show / done")

    choice = input("Choose an action: ").strip().lower()

    if choice == "add":
        item = input("Enter item to add: ").strip()

        if item:
            shopping_list.append(item)
            print(item, "added to your list.")
        else:
            print("Please enter an item.")

    elif choice == "remove":
        item = input("Enter item to remove: ").strip()

        if item in shopping_list:
            shopping_list.remove(item)
            print(item, "removed from your list.")
        else:
            print("That item is not on your list.")

    elif choice == "show":
        if shopping_list:
            print("Your shopping list:")
            for item in shopping_list:
                print("-", item)
        else:
            print("Your shopping list is empty.")

    elif choice == "done":
        print("Goodbye! Happy shopping.")
        break

    else:
        print("Invalid choice. Please choose add, remove, show, or done.")
