#
# Name: Reagan Grantham
# Last Revision Date: November 7th 2023
# Description: A program allowing students to control their course registration.
#
from student import Student, Course, add_course, drop_course, list_courses,  create_student_dict, create_course_dict
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

    # Create a dictionary of student objects.
    # The dictionary has key = s_id, value = student_obj

    student_info = create_student_dict(student_list, student_in_state)

    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5,
                    'CSC104': 3, 'CSC105': 2}

    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': [],
                     'CSC105': ['1005', '1002']}

    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1,
                       'CSC104': 3, 'CSC105': 4}

    # Create a dictionary of course objects.
    # The dictionary has key = course_id, value = course obj

    course_info = create_course_dict(course_hours, course_roster, course_max_size)

    while True:
        # get the user to login, or end program
        user_id = input("Enter ID to log in, or 0 to quit: ")
        if user_id == "0":
            break

        # if the student can be logged in ask them to pick out a menu entry,
        # and then pass control to the relevant function if the provided code's a code from the menu
        if login(user_id, student_info[user_id]):
            show_menu()
            code = input("What do you want to do? ")
            print()
            while code != "0":


                if code == "1":
                    add_course(user_id, course_info)
                elif code == "2":
                    drop_course(user_id, course_info)
                elif code == "3":
                    list_courses(user_id, course_info)
                elif code == "4":
                    display_bill(student_info[user_id], course_info)
                show_menu()
                code = input("What do you want to do? ")
                print()
            print("Session ended.")
            print()


#
# A function to try to log in a student.
#
# Inputs:
#   s_id - id of student trying to log in.
#   student_info - The object of the student
#
# Returns:
#   the success/failure of the login attempt.
#
def login(s_id, student_info):
    # ask user for the PIN too check against to the id
    pin = input("Enter PIN: ")
    if student_info.pin == pin:
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
