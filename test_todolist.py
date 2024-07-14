import pytest
import tkinter as tk
from project import add_task, delete_task, complete_task

@pytest.fixture
def setup_tkinter():
    root = tk.Tk()
    entry = tk.Entry(root)
    listbox = tk.Listbox(root)
    return root, entry, listbox

def test_add_task(setup_tkinter):
    root, entry, listbox = setup_tkinter
    entry.insert(0, "Test Task")
    task = add_task(entry, listbox)
    assert task == "Test Task"
    assert listbox.get(0) == "Test Task"
    assert entry.get() == ""

def test_delete_task(setup_tkinter):
    root, entry, listbox = setup_tkinter
    listbox.insert(tk.END, "Test Task")
    listbox.select_set(0)
    task_index = delete_task(listbox)
    assert task_index == 0
    assert listbox.size() == 0

def test_complete_task(setup_tkinter):
    root, entry, listbox = setup_tkinter
    listbox.insert(tk.END, "Test Task")
    listbox.select_set(0)
    task_index = complete_task(listbox)
    assert task_index == 0
    assert listbox.itemcget(0, "bg") == "green"
    assert listbox.itemcget(0, "fg") == "white"
