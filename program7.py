lst = []

def add():
    n = int(input("Enter number of elements you want to add: "))
    for i in range(n):
        element = int(input(f"Enter element {i+1}: "))
        lst.append(element)

def remove_element():
    print("Current list:", lst)
    index = int(input("Enter index of element you want to remove: "))
    lst.pop(index)

def display():
    print("Elements of list:", lst)

def remove_last():
    if lst:
        lst.pop()
    else:
        print("List is empty!")

while True:
    choice = int(input(
        "\n1. Add Element"
        "\n2. Remove Element by Index"
        "\n3. Display Elements"
        "\n4. Remove Last Element"
        "\n0. Exit\n"
    ))

    match choice:
        case 1:
            add()
        case 2:
            remove_element()
        case 3:
            display()
        case 4:
            remove_last()
        case 0:
            print("Exiting program...")
            break
        case _:
            print("Invalid choice!")
