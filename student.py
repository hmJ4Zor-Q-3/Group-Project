# ----------------------------------------------------------------
# Author:Keren Thomas Muthiah
# Date: 11/04/2023
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

def list_courses(s_id, c_roster):
    # ------------------------------------------------------------
    # This function displays all the courses, indicates which ones
    # in which the student is enrolled, and counts the courses a
    # student has registered for. It has two parameters: s_id is the
    # ID of the student; c_roster is the list of class rosters.
    # This function has no return value.
    # -------------------------------------------------------------
    print('Courses:')
    total_enrolled = 0
    for courseid, student_list in c_roster.items():
        if s_id in student_list:
            print(f'{courseid} (Enrolled)')
            total_enrolled += 1
        else:
            print(courseid)
    print(f'Total courses enrolled: {total_enrolled}')

def add_course(s_id, c_roster, c_max_size):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has three
    # parameters: s_id is the ID of the student to be added; c_roster is the
    # list of class rosters; c_max_size is the list of maximum class sizes.
    # This function asks user to enter the course he/she wants to add.
    # If the course is not offered, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.
    # If the course is full, display error message and stop.
    # If everything is okay, add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------

    course_id = input('Enter course you want to add: ')

    if course_id not in c_roster.keys():
        print('Course not found')
    elif s_id in  c_roster[course_id]:
        print('You are already enrolled in that course.')
    elif c_max_size[course_id] == len(c_roster[course_id]):
        print('Course already full')
    else:
        c_roster[course_id].append(s_id)
        print('Course added')

def drop_course(s_id, c_roster):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has two
    # parameters: s_id is the ID of the student to be dropped;
    # c_roster is the list of class rosters. This function asks
    # the user to enter the course he/she wants to drop.  If the course
    # is not offered, display error message and stop.  If the student
    # is not enrolled in that course, display error message and stop.
    # Remove student ID from the course’s roster and display a message
    # if there is no problem.  This function has no return value.
    # -------------------------------------------------------------
    course_id = input('Enter course you want to drop: ')

    if course_id not in c_roster.keys():
        print('Course not found')
    elif s_id not in c_roster[course_id]:
        print('You are not enrolled in that course.')
    else:
        c_roster[course_id].remove(s_id)
        print('Course dropped')
