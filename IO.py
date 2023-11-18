#
# Name: Reagan Grantham
# Last Revision Date: November 16th 2023
# Description: A module for serializing and deserializing the course and student registries.
#
from course import Course
from student import Student


#
# A function for loading the student registry.
#
# Returns:
#   A dictionary of all students keyed to their IDs, as loaded from the disk.
#
def get_student_registry():
    # temporarily return the default registry
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
# A function for loading the course registry.
#
# Inputs:
#   student_registry - A id keyed dictionary of all students.
#
# Returns:
#   A dictionary of all courses keyed to their IDs, as loaded from the disk.
#
def get_course_registry(student_registry):
    # temporarily return the default registry
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
