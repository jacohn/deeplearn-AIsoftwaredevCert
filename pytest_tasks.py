import pytest

# Original functions
tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added."

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        return f"Task '{task}' removed."
    else:
        return "Task not found."

def list_tasks():
    return tasks


# Test functions for pytest
@pytest.fixture(autouse=True)
def clear_tasks():
    """Fixture to clear tasks list before each test."""
    global tasks
    tasks = []

def test_add_task():
    # Test adding a task
    result = add_task("Test Task")
    assert result == "Task 'Test Task' added."
    assert "Test Task" in tasks

def test_remove_task_existing():
    # Test removing an existing task
    add_task("Task to Remove")
    result = remove_task("Task to Remove")
    assert result == "Task 'Task to Remove' removed."
    assert "Task to Remove" not in tasks

def test_remove_task_non_existing():
    # Test removing a task that doesn't exist
    result = remove_task("Non-existing Task")
    assert result == "Task not found."

def test_list_tasks_empty():
    # Test listing tasks when no tasks have been added
    result = list_tasks()
    assert result == []

def test_list_tasks_with_items():
    # Test listing tasks with some tasks added
    add_task("First Task")
    add_task("Second Task")
    result = list_tasks()
    assert result == ["First Task", "Second Task"]

def test_add_and_remove_multiple_tasks():
    # Test adding and removing multiple tasks
    add_task("Task 1")
    add_task("Task 2")
    add_task("Task 3")
    assert "Task 2" in tasks
    
    remove_task