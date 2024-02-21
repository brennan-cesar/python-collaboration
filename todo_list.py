def addTask():
    hi

def viewTask():
    hi

def markCompleted():
    hi

def delTask():
    hi

def main():
    loop = True
    while loop:
        user = input("What would you like to do? Enter 'A' to add a task, 'C' to mark completed, 'D' to delete, and 'V' to view. To end, type 'end'. >> ")
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
            user = input("What is the name of your task to view? >> ")
            viewTask(user)
        elif user == 'end':
            print("Exiting the program o/")
            loop = False
            return


main()