my_list = []

while True:
    print("\n--- LIST OPERATIONS MENU ---")
    print("1. Create list")
    print("2. Display list")
    print("3. Add element")
    print("4. Insert element at position")
    print("5. Delete element")
    print("6. Search element")
    print("7. Sort list")
    print("8. Reverse list")
    print("9. Length of list")
    print("10. Exit")

    choice = int(input("Enter your choice (1-10): "))

    if choice == 1:
        n = int(input("Enter number of elements: "))
        my_list = []
        for i in range(n):
            element = input("Enter element: ")
            my_list.append(element)
        print("List created successfully.")

    elif choice == 2:
        print("List elements:", my_list)

    elif choice == 3:
        element = input("Enter element to add: ")
        my_list.append(element)
        print("Element added.")

    elif choice == 4:
        element = input("Enter element to insert: ")
        position = int(input("Enter position: "))
        my_list.insert(position, element)
        print("Element inserted.")

    elif choice == 5:
        element = input("Enter element to delete: ")
        if element in my_list:
            my_list.remove(element)
            print("Element deleted.")
        else:
            print("Element not found.")

    elif choice == 6:
        element = input("Enter element to search: ")
        if element in my_list:
            print("Element found at index", my_list.index(element))
        else:
            print("Element not found.")

    elif choice == 7:
        my_list.sort()
        print("List sorted.")

    elif choice == 8:
        my_list.reverse()
        print("List reversed.")

    elif choice == 9:
        print("Length of list:", len(my_list))

    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
