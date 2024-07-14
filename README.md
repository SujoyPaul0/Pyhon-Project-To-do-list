# To-do list

### Video Demo : https://youtu.be/el27pQ-UmXw

### Description
The provided code defines a simple to-do list application using Tkinter, a standard GUI library in Python. The application allows users to add, delete, and mark tasks as complete within a graphical interface. The key components and functions of the code are explained below:

## Components and Functions

1. ### main():
   - Sets up the main application window with Tkinter.
   - Creates a `Tk` root window with the title "To-Do List".
   - Creates a `Frame` widget to hold the `listbox` and `scrollbar`.
   - Creates a `Listbox` widget to display the tasks.
   - Adds a `Scrollbar` to the `listbox` for vertical scrolling.
   - Configures the `listbox` to use the `scrollbar`.
   - Creates an `Entry` widget for the user to input new tasks.
   - Creates three buttons:
   - "Add Task" button, which calls `add_task(entry, listbox)` when clicked.
   - "Delete Task" button, which calls `delete_task(listbox)` when clicked.
   - "Complete Task" button, which calls `complete_task(listbox)` when clicked.
   - Starts the Tkinter event loop with `root.mainloop()`, which keeps the application running and responsive to user inputs.

2. ### add_task(entry, listbox):
   - Takes the text from the `entry` widget (where the user types a new task) and adds it to the `listbox` widget (which displays the list of tasks).
   - After adding the task, it clears the `entry` widget.
   - Returns the added task for testing purposes.

3. ### delete_task(listbox):
   - Deletes the currently selected task from the `listbox`.
   - Returns the index of the deleted task for testing purposes. If no task is selected, it returns `None`.

4. ### complete_task(listbox)**:
   - Marks the currently selected task as complete by changing its background color to green and text color to white.
   - Returns the index of the completed task for testing purposes. If no task is selected, it returns `None`.

## Running the Code
- When the script is executed, it creates a window with a listbox, an entry field, and three buttons.
- Users can add tasks by typing in the entry field and clicking the "Add Task" button.
- Users can delete a selected task by selecting it in the listbox and clicking the "Delete Task" button.
- Users can mark a selected task as complete by selecting it in the listbox and clicking the "Complete Task" button.

## test_project.py

### Imports:

- pytest: The testing framework used to run the tests.
- tkinter as tk: The standard GUI library for Python.
- Functions from project: add_task, delete_task, and complete_task functions are imported from the project.py file to be tested.

### setup_tkinter Fixture:

- This fixture function sets up a minimal Tkinter environment that can be reused in multiple tests. It creates a Tkinter root window, an entry widget, and a listbox widget.
- The fixture returns the root, entry, and listbox widgets to be used in the tests.

### test_add_task:

- Uses the setup_tkinter fixture to get a Tkinter environment.
- Inserts the text "Test Task" into the entry widget.
- Calls the add_task function and checks that the returned task is "Test Task".
- Asserts that the listbox contains the new task and that the entry widget is cleared.

### test_delete_task:

- Uses the setup_tkinter fixture to get a Tkinter environment.
- Inserts a task "Test Task" into the listbox and selects it.
- Calls the delete_task function and checks that the returned task index is 0.
- Asserts that the listbox is empty after the deletion.

### test_complete_task:

- Uses the setup_tkinter fixture to get a Tkinter environment.
- Inserts a task "Test Task" into the listbox and selects it.
- Calls the complete_task function and checks that the returned task index is 0.
- Asserts that the task's background color is set to green and the text color to white, indicating it is marked as complete.