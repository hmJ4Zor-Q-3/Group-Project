#
# Name: Reagan Grantham
# Last Revision Date: November 16th 2023
# Description: A program allowing students to control their course registration.
#
import IO
from billing import display_bill
from course import add_course, drop_course, list_courses


def main():
    # Get the registries from disk, or if a predictable issue occurs fall back to the defaults
    try:
        students, courses = IO.read_registries()
    except FileNotFoundError or KeyError as e:
        print('Couldn\'t load course or student registry from the disk, using defaults instead.'
              f'\nIntercepted error of the type: \"{type(e)}\", with the message: {e.__str__()}\n')
        students = IO.get_default_student_registry()
        courses = IO.get_default_course_registry(students)

    while True:
        # get the user to login, or end program
        user_id = input("Enter ID to log in, or 0 to quit: ")
        if user_id == "0":
            break

        if not students.__contains__(user_id):
            print(f"\nNo user was found with the ID: {user_id}\n")
            continue

        student = students[user_id]
        # if the student can be logged in ask them to pick out a menu entry,
        # and then pass control to the relevant function if the provided code's a code from the menu
        if login(student):
            show_menu()
            code = input("What do you want to do? ")
            print()
            while code != "0":

                if code == "1":
                    add_course(student, courses)
                elif code == "2":
                    drop_course(student, courses)
                elif code == "3":
                    list_courses(student, courses)
                elif code == "4":
                    display_bill(student, courses)
                show_menu()
                code = input("What do you want to do? ")
                print()
            print("Session ended.")
            print()
    IO.write_registries(students, courses)


#
# A function to try to log in a student.
#
# Inputs:
#   student_info - The student to log in.
#
# Returns:
#   the success/failure of the login attempt.
#
def login(student_info):
    # ask user for the PIN too check against to the id
    pin = input("Enter PIN: ")
    if student_info.is_pin(pin):
        print("ID and PIN verified")
        return True
    else:
        print("ID or PIN incorrect")
        return False


#
# A function which displays the action menu to the student that's logged in.
#
def show_menu():
    print("\nAction Menu"
          + "\n-----------"
          + "\n1: Add course"
          + "\n2: Drop course"
          + "\n3: List courses"
          + "\n4: Show bill"
          + "\n0: Logout")


main()
