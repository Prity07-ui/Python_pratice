#Student_result_manager

student = {}

while True:
    print("\n-----Student Result manager-----")
    print("1.Add Student")
    print("2.View Students")
    print("3.Check Result")
    print("4.Exit")

    choice=input("Enter your Choice :")

    #Add student
    if choice=="1":
        name = input("EnterStudent name :")
        marks = int(input("Enter marks:"))
        student[name] = marks
        print(f"{name} Successfully Added!")

    #Veiw Student
    elif choice == "2":
        if not student:
            print("Student not Found !")
        else:
            for name, marks in student.items():
                print(name, ":" , marks)

    #Check Result
    elif choice == "3":
   2     name = input("Enter student name :")
        if name in student:
            marks = student[name]
            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")
        else:
            print("Student not found !")

    #exit
    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid Choise")