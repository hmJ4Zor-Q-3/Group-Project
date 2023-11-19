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
