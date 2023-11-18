#
# Name: Reagan Grantham. Extracted and modified from Keren Thomas Muthiah's Student module.
# Last Revision Date: November 16th 2023
# Description: This module contains the Course defining class, and the utilities for listing out courses,
# and adding students to courses.
#

# Class to represent the course info
class Course(object):
    def __init__(self, c_id, hours, max_size, roster):
        self._c_id = c_id
        self._hours = hours
        self._max_size = max_size
        # clone contents instead of caching list reference to protected from blind outside mutations.
        self._roster = [r for r in roster]

    @property
    def c_id(self):
        return self._c_id

    @property
    def hours(self):
        return self._hours

    @property
    def max_size(self):
        return self._max_size

    def view_roster(self):
        return [r for r in self._roster]

    def add_student(self, student):
        if self.is_full():
            # TODO, pick better error to raise
            raise IndexError("Can't add a student to a course that's full")
        self._roster.append(student)

    def remove_student(self, student):
        self._roster.remove(student)

    def is_full(self):
        return len(self.view_roster()) >= self._max_size

    def __str__(self):
        return (f'CourseId:{self.c_id} Hours:{self.hours} Size:{self.max_size} '
                f'Roster:{self.view_roster}')


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
