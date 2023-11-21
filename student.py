# ----------------------------------------------------------------
#
# Author: Keren Thomas Muthiah
# Date: 4 November, 2023
#
# This module contains the Student defining class.
# -----------------------------------------------------------------

# Class to represent the student info
class Student:
    def __init__(self, s_id, pin, in_state):
        self._s_id = s_id
        self._pin = pin
        self._student_in_state = in_state

    @property
    def s_id(self):
        return self._s_id

    @property
    def student_in_state(self):
        return self._student_in_state

    def is_pin(self, pin):
        return pin == self._pin

    def __str__(self):
        return f'StudentId:{self.s_id} InState:{self.student_in_state}'


#
# Function to print the course information of a given student
#
# Input
#   student - the student to attempt adding
#   course_info - Dictionary of course objects
#
# Returns
#   None
def list_courses(student, course_info):
    print('Courses:')
    total_enrolled = 0

    for course in course_info:
        course_id = course
        course_roster = course_info[course_id].view_roster()
        if student in course_roster:
            print(f'{course_id} (Enrolled)')
            total_enrolled += 1
        else:
            print(course_id)
    print(f'Total courses enrolled: {total_enrolled}')


#
# Function to add the student to a course roster of the selected course
#
# Input
#   student - the student to attempt adding
#   course_info - Dictionary of course objects
#
# Returns
#   None
def add_course(student, course_info):
    course_id = input('Enter course you want to add: ')

    if course_id not in course_info.keys():
        print('Course not found')
    elif student in course_info[course_id].view_roster():
        print('You are already enrolled in that course.')
    elif course_info[course_id].is_full():
        print('Course already full')
    else:
        course_info[course_id].add_student(student)
        print('Course added')


#
# Function to remove the student from the course roster of the selected course
#
# Input
#   student - the student to attempt adding
#   course_info - Dictionary of course objects
#
# Returns
#   None
def drop_course(student, course_info):
    course_id = input('Enter course you want to drop: ')

    if course_id not in course_info.keys():
        print('Course not found')
    elif student not in course_info[course_id].view_roster():
        print('You are not enrolled in that course.')
    else:
        course_info[course_id].remove_student(student)
        print('Course dropped')
