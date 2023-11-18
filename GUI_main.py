#
# Name: Chukwuemeka Chidozie
# Last Revision Date: November 18th 2023
# Description: A program allowing students to control their course registration.
# Essentially a GUI rewrite of the deprecated registration.py
#
# High Level Workflow Summary:
# Make a login window and log the student in if credentials match
# Make a registration window and handle updating the student/course registries via interactive input

import IO
import tkinter as tk
from tkinter import messagebox


def create_login_window(students, course_registry):
    # Function to create GUI login window and accept user input
    # Calls login() when the login button is clicked

    # Takes the both the students registry and course registry as args
    # Returns nothing

    window = tk.Tk()
    window.title("Registration Portal")
    window.geometry("400x200")  # Set initial size of the window

    # Configure the grid to expand with the window size
    window.grid_columnconfigure(1, weight=1)
    window.grid_rowconfigure(1, weight=1)

    # Add labels, text entry boxes for ID and PIN
    tk.Label(window, text="Welcome To The Registration Portal\n\nPlease Login").grid(row=0, columnspan=2, pady=10)

    tk.Label(window, text="Student ID:").grid(row=1, column=0, padx=10, sticky='e')
    student_id_entry = tk.Entry(window)
    student_id_entry.grid(row=1, column=1, padx=10, sticky='ew')

    tk.Label(window, text="PIN:").grid(row=2, column=0, padx=10, sticky='e')
    pin_entry = tk.Entry(window, show="*")
    pin_entry.grid(row=2, column=1, padx=10, sticky='ew')

    # Add a login button
    login_button = tk.Button(window, text="Login", command=lambda: login(student_id_entry.get(), pin_entry.get(),
                                                                         window, students, course_registry))
    login_button.grid(row=3, columnspan=2, pady=10)

    window.mainloop()


def login(student_id, pin, window, students, course_registry):
    # Function to log the student in and move them to the main window
    # or show an error pop-up if the login credentials are wrong

    # Takes the inputted Student ID, PIN, Login Window, Students and Course Registry From IO.py
    # Returns nothing, but it destroys the login window and creates the main registration window

    if students.__contains__(student_id) and students[student_id].is_pin(pin):
        messagebox.showinfo("Login Success", "ID and PIN verified")
        window.destroy()  # This will close the login window

        # Call create_main_window with the appropriate arguments
        create_main_window(students[student_id], students, course_registry)
    else:
        messagebox.showerror("Login Failed", "ID or PIN incorrect")


def update_bill_label(student, course_registry, bill_label):
    # Function to update the text in the bill label
    # whenever the user makes changes to their course selection
    # It achieves this by checking the current state of the student and course registries

    # Takes Students and Course Registry and the bill label object
    # Returns nothing, but it modifies the text in the bill label

    bill_text = f"Status: {'In-State' if student.student_in_state else 'Out-Of-State'}\n\n\n"

    total_cost = 0

    for course_id, course in course_registry.items():
        if student in course.view_roster():
            cost = course.hours * (225 if student.student_in_state else 850)
            bill_text += f"{course_id}: ${cost}\n"
            total_cost += cost

    bill_text += f"\n\nTotal Bill: ${total_cost}"
    bill_label.config(text=bill_text)


def create_main_window(student, students, course_registry):
    # Function create the main course registration window and
    # handle events that are triggered by user interaction

    # Includes several sub-objects within the main window and event handlers for them
    # LabelFrames, Checkboxes, Buttons

    # Takes a Student object and both directories
    # Returns nothing but handles the lion share of user interaction via its elements

    window = tk.Tk()
    window.title("Course Registration Portal")

    # Student ID display
    student_id_label = tk.Label(window, text=f"Student ID: {student.s_id}")
    student_id_label.grid(row=0, column=0, sticky="w")

    # Left Section: Course Information
    left_frame = tk.LabelFrame(window, text="Courses")
    left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Dynamically creating course checkboxes
    course_vars = {}
    for course_id, course in course_registry.items():
        course_vars[course_id] = tk.BooleanVar(value=student in course.view_roster())
        cb = tk.Checkbutton(left_frame, text=f"{course_id}", variable=course_vars[course_id],
                            command=lambda cid=course_id: toggle_course(student, cid, course_registry, course_vars[cid],
                                                                        bill_label))
        cb.pack(anchor='w')

    # Right Section: Billing Information
    right_frame = tk.LabelFrame(window, text="Bill Summary")
    right_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    bill_label = tk.Label(right_frame, text="Bill will be shown here")
    bill_label.pack()
    update_bill_label(student, course_registry, bill_label)

    # Save and Exit Button

    # Will update the command arg for the button to also call a function
    # to save the current state of the directories to a file
    save_exit_button = tk.Button(window, text="Save and Exit", command=lambda: [window.destroy()])

    save_exit_button.grid(row=2, column=0, sticky="w")

    # Log-out Button

    # Will update the command arg for the button to also call a function
    # to save the current state of the directories to a file
    logout_button = tk.Button(window, text="Save and Log-Out",
                              command=lambda: [window.destroy(), create_login_window(students, course_registry)])
    logout_button.grid(row=2, column=1, sticky="e")

    window.mainloop()


def toggle_course(student, course_id, course_registry, enrolled_var, bill_label):
    # Function to update the course registry based on the current state of the checkbox
    # and also call the function to dynamically update the bill

    # Takes Student object, Course object, course_registry,
    # a boolean Value that represents enrollment status for that course,
    # and the bill label object

    try:
        if enrolled_var.get():
            course_registry[course_id].add_student(student)
        else:
            course_registry[course_id].remove_student(student)
    except Exception as e:
        messagebox.showerror("Error", str(e))
        enrolled_var.set(not enrolled_var.get())  # Revert checkbox on error
    finally:
        update_bill_label(student, course_registry, bill_label)


# Main script execution
if __name__ == "__main__":
    students = IO.get_student_registry()  # Load student_registry
    course_registry = IO.get_course_registry(students)  # Load courses
    create_login_window(students, course_registry)
