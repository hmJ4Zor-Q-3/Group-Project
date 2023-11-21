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

