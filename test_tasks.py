import unittest

# The original code for reference
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


# Unit tests for the task management functions
class TestTaskFunctions(unittest.TestCase):
    
    def setUp(self):
        # Clear the tasks list before each test to ensure tests are independent
        global tasks
        tasks = []

    def test_add_task(self):
        # Test adding a task
        result = add_task("Test Task")
        self.assertEqual(result, "Task 'Test Task' added.")
        self.assertIn("Test Task", tasks)

    def test_remove_task_existing(self):
        # Test removing an existing task
        add_task("Task to Remove")
        result = remove_task("Task to Remove")
        self.assertEqual(result, "Task 'Task to Remove' removed.")
        self.assertNotIn("Task to Remove", tasks)

    def test_remove_task_non_existing(self):
        # Test removing a task that doesn't exist
        result = remove_task("Non-existing Task")
        self.assertEqual(result, "Task not found.")
        
    def test_list_tasks_empty(self):
        # Test listing tasks when no tasks have been added
        result = list_tasks()
        self.assertEqual(result, [])
        
    def test_list_tasks_with_items(self):
        # Test listing tasks with some tasks added
        add_task("First Task")
        add_task("Second Task")
        result = list_tasks()
        self.assertEqual(result, ["First Task", "Second Task"])
        
    def test_add_and_remove_multiple_tasks(self):
        # Test adding and removing multiple tasks
        add_task("Task 1")
        add_task("Task 2")
        add_task("Task 3")
        self.assertIn("Task 2", tasks)
        
        remove_task("Task 2")
        self.assertNotIn("Task 2", tasks)
        self.assertEqual(list_tasks(), ["Task 1", "Task 3"])

if __name__ == '__main__':
    unittest.main()