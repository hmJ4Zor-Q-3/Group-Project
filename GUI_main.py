#
# Name: Chukwuemeka Chidozie
# Last Revision Date: November 19th 2023
# Description: A program allowing students to control their course registration.
# Essentially a GUI rewrite of the deprecated registration.py
#
# High Level Workflow Summary:
# Make a login window and log the student in if credentials match
# Make a registration window and handle updating the student/course registries via interactive input

import IO
import tkinter as tk
from tkinter import Toplevel
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


def auto_close_popup(title, message, window, duration=1000):
    # Function to create a temporary window to act as a pop-up
    # Makes a temporary window with pre-defined content

    # Takes a title, message content, a window reference and a duration
    # Returns nothing

    # Create a temporary top-level window
    popup = Toplevel(window)
    popup.title(title)
    popup_width, popup_height = 250, 100  # Pre-populated dimensions
    popup.geometry(f"{popup_width}x{popup_height}")

    # Calculate position x, y
    # Using the dimensions of the parent window and divide by two,
    # So that the pop-up will always be centered to the parent window
    x = (window.winfo_x() + window.winfo_width() // 2) - popup_width // 2
    y = (window.winfo_y() + window.winfo_height() // 2) - popup_height // 2
    popup.geometry(f"+{x}+{y}")

    # Add a message
    message_label = tk.Label(popup, text=message)
    message_label.pack(expand=True)

    # Automatically close the window after 'duration' milliseconds
    popup.after(duration, popup.destroy)


def login(student_id, pin, window, students, course_registry):
    # Function to log the student in and move them to the main window
    # or show an error pop-up if the login credentials are wrong

    # Takes the inputted Student ID, PIN, Login Window, Students and Course Registry From IO.py
    # Returns nothing, but it destroys the login window and creates the main registration window

    if students.__contains__(student_id) and students[student_id].is_pin(pin):
        auto_close_popup("Login Success", "ID and PIN verified", window, 1000)

        window.destroy()  # This will close the login window
        # This also causes a silent error - I'm assuming it's because the
        # auto_close_popup is still referencing an object that no longer exists (the login window)
        # not sure how to fix, but the program still works as intended

        # Call create_main_window with the appropriate arguments
        create_main_window(students[student_id], students, course_registry)

    else:
        auto_close_popup("Login Failed", "ID or PIN incorrect", window, 1500)


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
    # Function to create the main course registration window
    # Handles events triggered by user interaction

    # Includes several sub-objects within the main window and event handlers for them
    # LabelFrames, Checkboxes, Buttons

    # Takes a Student object and both directories
    # Returns nothing but handles the lion share of user interaction via its elements

    window = tk.Tk()
    window.title("Course Registration Portal")

    # Configure the grid to be resizable
    window.grid_rowconfigure(1, weight=1)  # Make row 1 expandable
    window.grid_columnconfigure(0, weight=1)  # Make column 0 expandable
    window.grid_columnconfigure(1, weight=1)  # Make column 1 expandable

    # Student ID display
    student_id_label = tk.Label(window, text=f"Student ID: {student.s_id}")
    student_id_label.grid(row=0, column=0, sticky="w")

    # Left Section: Course Information
    left_frame = tk.LabelFrame(window, text="Courses")
    left_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    left_frame.grid_rowconfigure(0, weight=1)  # Configure internal grid of left_frame
    left_frame.grid_columnconfigure(0, weight=1)

    course_vars = {}  # Store references to enrollment status
    course_checkboxes = {}  # Store references to the checkboxes
    for course_id, course in course_registry.items():
        course_vars[course_id] = tk.BooleanVar(value=student in course.view_roster())
        current_size = len(course.view_roster())
        cb = tk.Checkbutton(left_frame, text=f"{course_id}  |  Seats: {current_size}/{course.max_size}",
                            variable=course_vars[course_id],
                            command=lambda cid=course_id: toggle_course(student, cid, course_registry, course_vars[cid],
                                                                        bill_label, course_checkboxes[cid]))
        cb.pack(anchor='center', expand=True)
        course_checkboxes[course_id] = cb

    # Right Section: Billing Information
    right_frame = tk.LabelFrame(window, text="Bill Summary")
    right_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
    right_frame.grid_rowconfigure(0, weight=1)  # Configure internal grid of right_frame
    right_frame.grid_columnconfigure(0, weight=1)
    bill_label = tk.Label(right_frame, text="Bill will be shown here")
    bill_label.pack(expand=True)
    update_bill_label(student, course_registry, bill_label)

    # Save and Exit Button
    save_exit_button = tk.Button(window, text="Save and Exit",
                                 command=lambda: [IO.write_registries(students, course_registry), window.destroy()])
    save_exit_button.grid(row=2, column=0, padx=12, pady=12, sticky="w")

    # Log-out Button
    logout_button = tk.Button(window, text="Save and Log-Out",
                              command=lambda: [IO.write_registries(students, course_registry),
                                               window.destroy(), create_login_window(students, course_registry)])
    logout_button.grid(row=2, column=1, padx=12, pady=12, sticky="e")

    window.mainloop()


def toggle_course(student, course_id, course_registry, enrolled_var, bill_label, checkbox):
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
        # Update the checkbox text
        current_size = len(course_registry[course_id].view_roster())
        checkbox.config(text=f"{course_id}  |  Seats: {current_size}/{course_registry[course_id].max_size}")


# Main script execution
if __name__ == "__main__":
    # Get the registries from disk, or if a predictable issue occurs fall back to the defaults
    try:
        students, course_registry = IO.read_registries()
    except FileNotFoundError or KeyError as e:
        print('Couldn\'t load course or student registry from the disk, using defaults instead.'
              f'\nIntercepted error of the type: \"{type(e)}\", with the message: {e.__str__()}\n')
        students = IO.get_default_student_registry()
        course_registry = IO.get_default_course_registry(students)

    create_login_window(students, course_registry)
