# ----------------------------------------------------------------
# Author: Chukwuemeka Chidozie
# Date: November 06, 2023
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
import datetime
from student import Student, Course

def display_bill(student_info, course_info):
    # ------------------------------------------------------------
    # This function displays the student's bill. It takes four
    # parameters: s_id, the student id; s_in_state, the list of
    # in-state students; c_rosters, the rosters of students in
    # each course; c_hours, the number of hours in each course.
    # The function has no return value.
    # ------------------------------------------------------------

    # String assignment based on student status
    if not student_info.student_in_state:
        status = 'Out-of-State Student'
    else:
        status = 'In-State Student'

    # Print first parts of the bill
    print('Tuition Summary')
    print(f'Student: {student_info.s_id}, {status}')

    # Get the current data/time, convert and print in the right format
    right_now = datetime.datetime.now()
    # Convert to a string with the specified format
    right_now_str = right_now.strftime("%b %d, %Y at %I:%M %p")
    print(right_now_str + '\n')

    # Generate the bill
    s_courses = [course for course, course_obj in course_info.items() if student_info.s_id in course_obj.course_roster]  # Grab all relevant courses first
    s_courses.sort()  # Sort the list just in case

    # Constants for cost calculation
    in_state_multiplier = 225
    out_state_multiplier = 850

    # Header for the table
    print(f"{'Course':<10} {'Hours':>6}{' '*6}{'Cost':<10}")
    print(f"{'-'*6}{' '*6}{'-'*5}{' '*2}{'-'*13}")

    # Initialization for totals
    total_hours = 0
    total_cost = 0

    # Calculate and print the line for each course
    for course in s_courses:
        hours = course_info[course].course_hours
        cost = hours * (in_state_multiplier if student_info.student_in_state else out_state_multiplier)
        total_hours += hours
        total_cost += cost
        # Align decimals by ensuring the width before the decimal is consistent
        print(f"{course:<10} {hours:>6}  $  {cost:10.2f}")

    # Print the totals with the same width before the decimal
    print(f"{'-'*6}{' '*6}{'-'*5}{' '*2}{'-'*13}")
    print(f"{'Total':<10} {total_hours:>6}  $  {total_cost:10.2f}")
