filename = "Student.txt"

# Add Student
def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open(filename, "a") as file:
        file.write(f"{roll},{name},{marks}\n")

    print("Student added successfully!\n")

# View Students
def view_student():
    try:
        with open(filename, "r") as file:
            students = file.readlines()

        if not students:
            print("No students found!\n")
            return

        print("\nStudent List")
        print("-" * 50)
        print(f"{'Roll':<15} {'Name':<20} {'Marks':<10}")
        print("-" * 50)

        for s in students:
            s = s.strip()
            if not s:  # Skip empty lines
                continue
            
            # Split and handle cases where name might have spaces
            parts = s.split(",")
            
            # Error handling for corrupted data
            if len(parts) != 3:
                print(f"Corrupted data found: {s}")
                print(f"(Expected 3 fields, got {len(parts)})")
                continue
            
            roll, name, marks = parts
            print(f"{roll:<15} {name:<20} {marks:<10}")

        print()

    except FileNotFoundError:
        print("No data file found!\n")

# Search Student
def search_student():
    roll_search = input("Enter roll number to search: ")

    try:
        with open(filename, "r") as file:
            students = file.readlines()

        for s in students:
            s = s.strip()
            if not s:
                continue
            
            parts = s.split(",")
            if len(parts) != 3:
                continue
            
            roll, name, marks = parts

            if roll == roll_search:
                print(f"\nFound!")
                print(f"Roll: {roll}")
                print(f"Name: {name}")
                print(f"Marks: {marks}\n")
                return

        print("Student not found!\n")

    except FileNotFoundError:
        print("No data file found!\n")


# Delete Student
def delete_student():
    roll_delete = input("Enter roll number to delete: ")

    try:
        with open(filename, "r") as file:
            students = file.readlines()

        new_list = []
        found = False

        for s in students:
            s_stripped = s.strip()
            if not s_stripped:  # Skip empty lines
                continue
            
            parts = s_stripped.split(",")
            if len(parts) != 3:
                continue
            
            roll, name, marks = parts

            if roll != roll_delete:
                new_list.append(f"{roll},{name},{marks}\n")
            else:
                found = True

        with open(filename, "w") as file:
            file.writelines(new_list)

        if found:
            print("Student deleted successfully!\n")
        else:
            print("Student not found!\n")

    except FileNotFoundError:
        print("No data file found!\n")


# Main Menu
def main():
    while True:
        print("STUDENT MANAGEMENT SYSTEM")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Exiting system...")
            break

        else:
            print("Invalid choice!\n")


if __name__ == "__main__":
    main()