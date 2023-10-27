#
# Name: Reagan Grantham
# Date: October 26th 2023
# Description: A program allowing students to control their course registration.
#
from student import add_course, drop_course, list_courses
from billing import display_bill


def main():
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444'),
                    ('1005', '555'), ('1006', '666')]

    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False,
                        '1005': False,
                        '1006': True}

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5,
                    'CSC104': 3, 'CSC105': 2}

    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': [],
                     'CSC105': ['1005', '1002']}

    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1,
                       'CSC104': 3, 'CSC105': 4}

    while True:
        user_id = input("Enter ID to log in, or 0 to quit")
        if user_id == "0":
            break

        if login(user_id, student_list):
            show_menu()
            code = input("What do you want to do? ")
            print()
            if code == "0":
                print("Session ended.")
            elif code == "1":
                add_course(id, course_roster, course_max_size)
            elif code == "2":
                drop_course(id, course_roster)
            elif code == "3":
                list_courses(id, course_roster)
            elif code == "4":
                display_bill(id, student_in_state, course_roster, course_hours)
            print()
            # use a loop to allow a student to choose to add courses,
            # to drop courses,
            # or list courses that the student has registered for,
            # or if they would want to display a bill


#
# A function to try to log in a student.
#
# Inputs:
#   id - id of student trying to log in.
#   s_list - list of all known students.
#
# Returns:
#   the success/failure of the login attempt.
#
def login(id, s_list):
    pin = input("Enter PIN: ")
    if s_list.__contains__((id, pin)):
        print("ID and PIN verified")
        return True
    else:
        print("ID or PIN incorrect")
        return False


#
# A function which displays the action menu to the student that's logged in
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
