taskDict = {}

def addTask(user): #adds user-input name, and automatically sets it to incomplete
    taskDict[user] = 'incomplete'

def viewTasks():
    for key, value in taskDict.items():
        print(f"Task: {key}. Status: {value}")

def markCompleted(user): #usese .update() function to change task from 'incomplete' to 'complete
    taskDict.update({user: 'complete'})

def delTask(user): #pops (deletes) the selected item from the dict
    taskDict.pop(user)

def save_to_file():
    out_file = open("./output.txt", "w")
    for key, value in taskDict.items():
        out_file.write(f"Task: {key}. Status: {value}\n")

def main():
    loop = True
    while loop:
        user = input("What would you like to do? Enter 'A' to add a task, 'C' to mark completed, 'D' to delete, and 'V' to view. O to output tasks to a file. To end, type 'end'. >> ")
        if user == 'A':
            user = input("What is the name of your task to add? >> ")
            addTask(user)
        elif user == 'C':
            user = input("What is the name of your task to complete? >> ")
            markCompleted(user)
        elif user == 'D':
            user = input("What is the name of your task to delete? >> ")
            delTask(user)
        elif user == 'V':
            viewTasks()
        elif user == 'O':
            save_to_file()
        elif user == 'end':
            print("Exiting the program o/")
            loop = False
            return


main()