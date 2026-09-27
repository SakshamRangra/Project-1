
students_list = []
def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks1 = float(input("Enter marks for Subject 1: "))
    marks2 = float(input("Enter marks for Subject 2: "))
    marks3 = float(input("Enter marks for Subject 3: "))
    total = marks1 + marks2 + marks3
    avg = total / 3
    if avg >= 90:
        grade = "A+"
    elif avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "F"  
    student_data = [name, roll_no, marks1, marks2, marks3, total, avg, grade]
    students_list.append(student_data)
    print("Student added successfully!")
def display_all():
    if len(students_list) == 0:
        print("No student records found.")
    else:
        print("\n--- ALL STUDENT RECORDS ---")
        for s in students_list:
            print("Name:", s[0])
            print("Roll No:", s[1])
            print("Marks:", s[2], s[3], s[4])
            print("Total:", s[5])
            print("Average:", s[6])
            print("Grade:", s[7])
            print("-----------------------")
def search_student():
    search_roll = input("Enter roll number to search: ")
    found = False
    for s in students_list:
        if s[1] == search_roll:
            print("\nStudent Found:")
            print("Name:", s[0])
            print("Roll No:", s[1])
            print("Total Marks:", s[5])
            print("Grade:", s[7])
            found = True
            break      
    if found == False:
        print("Student record not found.")
def save_to_file():
    file = open("student_data.txt", "a")
    for s in students_list:
        line = s[0] + "," + s[1] + "," + str(s[5]) + "," + s[7] + "\n"
        file.write(line)
    file.close()
    print("Data saved to student_data.txt file.")
while True:
    print("\n***** MENU *****")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Save Records")
    print("5. Exit")
    choice = int(input("Enter choice (1-5): "))
    if choice == 1:
        add_student()
    elif choice == 2:
        display_all()
    elif choice == 3:
        search_student()
    elif choice == 4:
        save_to_file()
    elif choice == 5:
        print("Exiting project...")
        break
    else:
        print("Invalid choice, try again.")