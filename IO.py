#
# Name: Reagan Grantham
# Last Revision Date: November 16th 2023
# Description: A module for serializing and deserializing the course and student registries.
#
import json

from course import Course
from student import Student

VALUES_KEY = 'values'
ID_KEY = 'id'
PIN_KEY = 'pin'
IN_STATE_KEY = 'in_state'

HOURS_KEY = "hours"
MAX_SIZE_KEY = 'max_size'
ROSTER_KEY = 'roster'


#
# A function for loading the student and course registries.
#
# Returns:
#   A dictionary of all students keyed to their IDs, as loaded from the disk,
#   and also a dictionary of all courses keyed to their IDs, as loaded from the disk.
#
def read_registries():
    student_registry \
        = {str(obj[ID_KEY]): Student(str(obj[ID_KEY]), str(obj[PIN_KEY]), bool(obj[IN_STATE_KEY]))
           for obj in json.loads(open('students.json', 'r').read())[VALUES_KEY]}
    course_registry \
        = {str(obj[ID_KEY]): Course(str(obj[ID_KEY]), obj[HOURS_KEY], int(obj[MAX_SIZE_KEY]),
                                    [student_registry[str(s)] for s in obj[ROSTER_KEY]])
           for obj in json.loads(open('courses.json', 'r').read())[VALUES_KEY]}
    return student_registry, course_registry


#
# A function for recoding the student and course registries.
#
# Inputs:
#   student_registry - A id keyed dictionary of all students.
#   course_registry - A id keyed dictionary of all courses.
#
def write_registries(student_registry, course_registry):
    student_list = list()
    for student in student_registry.values():
        student_list.append({ID_KEY: student.s_id,
                             PIN_KEY: student._pin,
                             IN_STATE_KEY: student.student_in_state})

    course_list = list()
    for course in course_registry.values():
        course_list.append({ID_KEY: course.c_id,
                            HOURS_KEY: course.hours,
                            MAX_SIZE_KEY: course.max_size,
                            ROSTER_KEY: [s.s_id for s in course.view_roster()]})

    s = open('students.json', 'w')
    s.write(json.dumps({VALUES_KEY: student_list}))
    s.close()
    c = open('courses.json', 'w')
    c.write(json.dumps({VALUES_KEY: course_list}))
    c.close()


#
# A function for creating in the default student registry.
#
# Returns:
#   A dictionary of all students keyed to their IDs, as defined by the instructor's original specification.
#
def get_default_student_registry():
    student_list = [('1001', '111'), ('1002', '222'),
                    ('1003', '333'), ('1004', '444'),
                    ('1005', '555'), ('1006', '666')]

    student_in_state = {'1001': True,
                        '1002': False,
                        '1003': True,
                        '1004': False,
                        '1005': False,
                        '1006': True}
    return {p[0]: Student(p[0], p[1], student_in_state[p[0]]) for p in student_list}


#
# A function for creating in the default course registry.
#
# Returns:
#   A dictionary of all courses keyed to their IDs, as defined by the instructor's original specification.
#
def get_default_course_registry(student_registry):
    # Slightly modified the function here
    course_hours = {'CSC101': 3, 'CSC102': 4, 'CSC103': 5,
                    'CSC104': 3, 'CSC105': 2}

    course_roster = {'CSC101': ['1004', '1003'],
                     'CSC102': ['1001'],
                     'CSC103': ['1002'],
                     'CSC104': [],
                     'CSC105': ['1005', '1002']}

    course_max_size = {'CSC101': 3, 'CSC102': 2, 'CSC103': 1,
                       'CSC104': 3, 'CSC105': 4}
    return {k: Course(k, course_hours[k], course_max_size[k], [student_registry[s] for s in course_roster[k]])
            for k in course_hours.keys()}
