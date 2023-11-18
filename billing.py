# ----------------------------------------------------------------
# Author: Chukwuemeka Chidozie
# Date: November 06, 2023
#
# This module calculates and displays billing information
# for students in the class registration system.  Student and
# class records are reviewed and tuition fees are calculated.
# -----------------------------------------------------------------
import datetime


#
# A function which displays the student's bill.
#
# Inputs:
#   student - The student who's bill will be displayed.
#   course_registry - A id keyed dictionary of all courses.
#
# Returns:
#   nothing.
#
def display_bill(student, course_registry):
    # String assignment based on student status
    if not student.student_in_state:
        status = 'Out-of-State Student'
    else:
        status = 'In-State Student'

    # Print first parts of the bill
    print('Tuition Summary')
    print(f'Student: {student.s_id}, {status}')

    # Get the current data/time, convert and print in the right format
    right_now = datetime.datetime.now()
    # Convert to a string with the specified format
    right_now_str = right_now.strftime("%b %d, %Y at %I:%M %p")
    print(right_now_str + '\n')

    # Generate the bill
    s_courses = [course for course, course_obj in course_registry.items() if
                 student in course_obj.view_roster()]  # Grab all relevant courses first
    s_courses.sort()  # Sort the list just in case

    # Constants for cost calculation
    in_state_multiplier = 225
    out_state_multiplier = 850

    # Header for the table
    print(f"{'Course':<10} {'Hours':>6}{' ' * 6}{'Cost':<10}")
    print(f"{'-' * 6}{' ' * 6}{'-' * 5}{' ' * 2}{'-' * 13}")

    # Initialization for totals
    total_hours = 0
    total_cost = 0

    # Calculate and print the line for each course
    for course in s_courses:
        hours = course_registry[course].hours
        cost = hours * (in_state_multiplier if student.student_in_state else out_state_multiplier)
        total_hours += hours
        total_cost += cost
        # Align decimals by ensuring the width before the decimal is consistent
        print(f"{course:<10} {hours:>6}  $  {cost:10.2f}")

    # Print the totals with the same width before the decimal
    print(f"{'-' * 6}{' ' * 6}{'-' * 5}{' ' * 2}{'-' * 13}")
    print(f"{'Total':<10} {total_hours:>6}  $  {total_cost:10.2f}")
