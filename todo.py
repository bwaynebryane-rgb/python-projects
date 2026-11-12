print("Welcome To Brian To-Do-List")


task = []


while True:
  print("1. Add Task")
  print("2. View Tasks")
  print("3. Delete Task")
  print("4. Exit")
  choice = input("Enter your task: ")
  
  tasks.append(task)
  print("Task added!")


elif choice == "1":
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task Added!")


elif choice == "2":
    if len(tasks) == 0:
         print("No tasks yet")
    else:
          print("Your tasks yet!")
          for i in range(lens(tasks)):
                print(str(i + 1) + ". " + tasks[i])
            num = int(input("which task number to delete? "))
            if no >= 1 and num <= len(tasks):
                 removed = tasks.pop(num - 1)
              print ("Deleted:", removed)
            else
              print("Invalid number")

elif choice == "4"
    print (" Bye Brian! keepworking hard!")
    break
else:
print("pick 1, 2, 3 or 4 only")


      
 
