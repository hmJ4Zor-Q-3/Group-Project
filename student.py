# ----------------------------------------------------------------
#
# Author: Keren Thomas Muthiah
# Date: 4 November, 2023
#
# This module supports changes in the registered courses
# for students in the class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

# Class to represent the student info
class Student:
    def __init__(self, s_id, pin, in_state):
        self.s_id = s_id
        self.pin = pin
        self.student_in_state = in_state

    def __str__(self):
        return f'StudentId:{self.s_id} InState:{self.student_in_state}'


#
# Function to create a dictionary of student objects
# The key is the student id and value is student object
#
# Inputs:
#  student_list - list of the students
#  student_in_state - dictionary of the student in state status
#
# Returns:
#  Dictionary of the student objects
#
def create_student_dict(student_list, student_in_state):
    student_info = {}

    for student in student_list:
        student_id, pin = student[0], student[1]
        student_obj = Student(student_id, pin, student_in_state[student_id])
        student_info[student_id] = student_obj

    return student_info


# Class to represent the course info
class Course:
    def __init__(self, course_id, course_hours, course_max_size, course_roster):
        self.course_id = course_id
        self.course_hours = course_hours
        self.course_max_size = course_max_size
        self.course_roster = course_roster

    def __str__(self):
        return f'CourseId:{self.course_id} Hours:{self.course_hours} Size:{self.course_max_size} Roster:{self.course_roster}'


#
# Function to create a dictionary of course objects
# The key is the course id and value is course object
#
# Inputs:
#  course_hours - Dictionary of course id and hours
#  course_roster - Dictionary of course id and course roster list
#  course_max_size - Dictionary of course id and max size
#
# Returns:
#  Dictionary of the course objects
#
def create_course_dict(course_hours, course_roster, course_max_size):
    course_info = {}

    for course in course_hours:
        course_id = course
        hours = course_hours[course]
        roster = course_roster[course]
        max_size = course_max_size[course]
        course_obj = Course(course_id, hours, max_size, roster)
        course_info[course_id] = course_obj

    return course_info


#
# Function to print the course information of a given student
#
# Input
#   s_id - the student id
#   course_info - Dictionary of course objects
#
# Returns
#   None
def list_courses(s_id, course_info):

    print('Courses:')
    total_enrolled = 0

    for course in course_info:
        course_id = course
        course_roster = course_info[course_id].course_roster
        if s_id in course_roster:
            print(f'{course_id} (Enrolled)')
            total_enrolled += 1
        else:
            print(course_id)
    print(f'Total courses enrolled: {total_enrolled}')


#
# Function to add the student to a course roster of the selected course
#
# Input
#   s_id - the student id
#   course_info - Dictionary of course objects
#
# Returns
#   None
def add_course(s_id, course_info):

    course_id = input('Enter course you want to add: ')

    if course_id not in course_info.keys():
        print('Course not found')
    elif s_id in  course_info[course_id].course_roster:
        print('You are already enrolled in that course.')
    elif course_info[course_id].course_max_size == len(course_info[course_id].course_roster):
        print('Course already full')
    else:
        course_info[course_id].course_roster.append(s_id)
        print('Course added')


#
# Function to remove the student from the course roster of the selected course
#
# Input
#   s_id - the student id
#   course_info - Dictionary of course objects
#
# Returns
#   None
def drop_course(s_id, course_info):

    course_id = input('Enter course you want to drop: ')

    if course_id not in course_info.keys():
        print('Course not found')
    elif s_id not in course_info[course_id].course_roster:
        print('You are not enrolled in that course.')
    else:
        course_info[course_id].course_roster.remove(s_id)
        print('Course dropped')


