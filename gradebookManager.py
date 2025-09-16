while True:
    gradebook = input("Would you like to view grades or the students? Grades/Students: ").capitalize()
    if gradebook == "Grades":
        print("Here are the grades.")
        break
    elif gradebook == "Students":
        print("Here are the students.")
        break
    else:
        print("Please try again, I did not understand that.")

if gradebook == "Grades":
    print()
    print("Test")

if gradebook == "Students":
    print()
    print("Test")