import json

def load_tasks():
  try:
    with open("tasks.json", "r") as file:
      return json.load(file)
  except FileNotFoundError:
    return []

def save_tasks(tasks):
  with open("tasks.json", "w") as file:
    json.dump(tasks, file)

def add_task(tasks):
  task = input("Enter your task: ")
  tasks.append(task)
  save_tasks(tasks)
  print("Task added successfully!")

def list_tasks(tasks):
  if not tasks:
    print("No tasks found.")
  else:
    for i, task in enumerate(tasks):
      print(f"{i+1}. {task}")

def mark_task_complete(tasks):
  task_number = int(input("Enter the number of the task to mark as complete: "))
  if 0 < task_number <= len(tasks):
    tasks[task_number - 1] = f"[DONE] {tasks[task_number - 1]}"
    save_tasks(tasks)
    print("Task marked as complete!")
  else:
    print("Invalid task number.")

def delete_task(tasks):
  task_number = int(input("Enter the number of the task to delete: "))
  if 0 < task_number <= len(tasks):
    del tasks[task_number - 1]
    save_tasks(tasks)
    print("Task deleted successfully!")
  else:
    print("Invalid task number.")

def main():
  tasks = load_tasks()
  while True:
    print("\nCodSoft To-Do List Application\n")
    print("1. Create a task")
    print("2. List all the tasks")
    print("3. Mark a task as done")
    print("4. Delete the task")
    print("5. Exit\n")
    choice = input("Enter your choice: ")

    if choice == "1":
      add_task(tasks)
    elif choice == "2":
      list_tasks(tasks)
    elif choice == "3":
      mark_task_complete(tasks)
    elif choice == "4":
      delete_task(tasks)
    elif choice == "5":
      break
    else:
      print("Invalid choice.")

if __name__ == "__main__":
  main()
