class Task:
    def __init__(self, name):
        self.name = name
        self.complete = False
        
        
class TodoList:
    def __init__(self):
        self.tasks = {}
        self.key = 1
        
        
    def add_task(self, name):
        task = Task(name)
        self.tasks[self.key] = task
        self.key += 1
        return f"Task {task.name} added succesfully"
        
    def complete_task(self, key):
        if key in self.tasks:
            self.tasks[key].complete = True
            return f"Task with id {key} marked as complete"
        else:
            return f"Task with id {key} not found"
        
        
    def print_tasks(self):
        for key, task in self.tasks.items():
            status = "✓" if task.complete else " "
            print(f"{key} : {task.name} : [{status}]")
            
        
tl = TodoList()


print(tl.add_task("clean room"))
print(tl.add_task("swiffer"))
print(tl.add_task("vacuum"))


print(tl.complete_task(1))

tl.print_tasks()