print("Welcome to Python Cli-Todolist!\n\n1. Add todo\n2. View todolist\n3. Delete todo\n")
chooseMode = input("Enter Number: ")
print("")
  
    
def getLines():
    with open("index.txt", 'r') as readFile:
        readFileLength = str(len(readFile.readlines()) + 1)
    return readFileLength
    
def getTodoItem():
    todoItem = input("Enter Todo: ")
    saveTodo(todoItem)
    
def saveTodo(Item):
    setTodoItem = getLines() + ". " + Item + "\n"
    with open("index.txt", 'a') as todoTextFile:
        todoTextFile.write(setTodoItem)
    afterSomeTodo()
    
def afterSomeTodo():
    print("\n\nWhat do you want to next?\n\n1. Add again\n2. View todolist\n3. Delete Todo\n4. Exit\n")
    chooseAfterSomeTodo = input("Enter Number: ")
    print("")
    if(chooseAfterSomeTodo == '1'):
        getTodoItem()
    elif(chooseAfterSomeTodo == '2'):
        showTodoItems()
    elif(chooseAfterSomeTodo == '3'):
        delTodo()
    else:
        return
    
def showTodoItems():
    with open("index.txt", 'r') as todoTextFile:
        while True:
            todoTextLine = todoTextFile.readline()
            if not todoTextLine: break
            print(todoTextLine)
    
def delTodo():
    showTodoItems()
    chooseDelWhat = input("Enter Todo You Want: ")
    
    with open("index.txt", 'r') as readFile:
        readFileLines = readFile.readlines()
    with open("index.txt", 'w') as readFile:
        for line in readFileLines:
            if line.strip("\n") != str(chooseDelWhat):
                readFile.write(line)
    
class init():
    if(chooseMode == "1"):
        getTodoItem()
    elif(chooseMode == "2"):
        showTodoItems()
    elif(chooseMode == "3"):
        delTodo()
    else:
        print("Please try again")
              
init()
    

    
    