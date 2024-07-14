import tkinter as tk

def main():
    root = tk.Tk()
    root.title("To-Do List")

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    listbox = tk.Listbox(frame, height=10, width=50)
    listbox.pack(side=tk.LEFT, fill=tk.BOTH)

    scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox.config(yscrollcommand=scrollbar.set)

    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    add_button = tk.Button(root, text="Add Task", width=48, command=lambda: add_task(entry, listbox))
    add_button.pack()

    delete_button = tk.Button(root, text="Delete Task", width=48, command=lambda: delete_task(listbox))
    delete_button.pack()

    complete_button = tk.Button(root, text="Complete Task", width=48, command=lambda: complete_task(listbox))
    complete_button.pack()

    root.mainloop()
    
    
def add_task(entry, listbox):
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    return task  # For testing purposes

def delete_task(listbox):
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
        return task_index  # For testing purposes
    except IndexError:
        return None

def complete_task(listbox):
    try:
        task_index = listbox.curselection()[0]
        listbox.itemconfig(task_index, {'bg': 'green', 'fg': 'white'})
        return task_index  # For testing purposes
    except IndexError:
        return None



if __name__ == "__main__":
    main()
