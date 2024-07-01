def task():
    tasks=[]
    print("~~~WELCOME TO MY TO-DO-LIST~~~")

    absolute_task=int(input("Enter how many task u want to add : "))

    for i in range(1,absolute_task+1):
       task_name=input(f"Enter task {i} :")
       tasks.append(task_name)

    print(f"My today tasks are\n {tasks} ")

    while True:
        choice=int(input("Enter 1-Add\n2-Update\n3-Delete\n4-view\n5-Exit/terminate/"))
       
        if choice == 1:
            add= input("Enter the task u want to add : ")
            tasks.append(add)
            print(f"Task {add} has been favorably added...")
        
        
        elif choice == 2:
            updated_value=input("Enter the task name u want to update : ")
            if updated_value in tasks:
              up=input("Enter the new task : ")
            ind=tasks.index(updated_value)
            tasks[ind]=up
            print(f"Updated task {up} ")
            
        elif choice == 3:
            del_value = input("which task u want to be delete  : ")
            if del_value in tasks:
                ind = tasks.index(del_value)
                del tasks[ind]
                print(f"Task {del_value}  has been successfully deleted...")

        
        elif choice == 4:
            # for viewing the tasks
            print(f"absolute tasks = {tasks}")  
       
        elif choice == 5:
            print("Exiting to TO-DO-LIST...")
            break   #loop close here---

        else:
            print("Invalid statement")

task()


            
