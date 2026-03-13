students = []

def add_student():
    roll = input("Roll No: ")
    name = input("Name: ")
    students.append({'roll': roll, 'name': name})

def search_student():
    roll = input("Enter Roll No to search: ")
    for s in students:
        if s['roll'] == roll:
            print("Found:", s)
            return
    print("Student not found.")

def list_students():
    for s in students:
        print(s)

def update_student():
    roll = input("Enter Roll No to update: ")
    for s in students:
        if s['roll'] == roll:
            s['name'] = input("New Name: ")
            print("Updated.")
            return
    print("Student not found.")

def delete_student():
    roll = input("Enter Roll No to delete: ")
    for s in students:
        if s['roll'] == roll:
            students.remove(s)
            print("Deleted.")
            return
    print("Student not found.")

while True:
    print("\nMenu:\na) Add\nb) Search\nc) List\nd) Update\ne) Delete\nf) Exit")
    choice = input("Enter choice: ").lower()
    if choice == 'a': add_student()
    elif choice == 'b': search_student()
    elif choice == 'c': list_students()
    elif choice == 'd': update_student()
    elif choice == 'e': delete_student()
    elif choice == 'f': break
    else: print("Invalid choice.")
