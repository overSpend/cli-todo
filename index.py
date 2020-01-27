print("Welcome to Python Cli-Todolist!\n")
print("1. Add todo\n2. View todolist")
chooseMode = input("숫자를 입력해주세요: ")
print("")
  
def getLines():
    readFile = open("index.txt", 'r')
    readFileLength = str(len(readFile.readlines()) + 1)
    readFile.close()
    return readFileLength
    
def saveTodo(Item):
    setTodoItem = getLines() + ": " + Item + "\n"
    todoTextFile = open("index.txt", 'a')
    todoTextFile.write(setTodoItem)
    todoTextFile.close()
    afterAddTodo()
    
def getTodoItem():
    todoItem = input("Enter Todo: ")
    saveTodo(todoItem)
    
def afterAddTodo():
    print("\nAdd Success!!\n\nWhat do you want to next?\n")
    print("1. Add again\n2. View todolist\n3. Exit")
    chooseAfterAddTodo = input("숫자를 입력해주세요: ")
    print("")
    if(chooseAfterAddTodo == "1"):
        getTodoItem()
    elif(chooseAfterAddTodo == "2"):
        showTodoItems()
    else:
        return
    
def showTodoItems():
    todoTextFile = open("index.txt", "r")
    while True:
        todoTextLine = todoTextFile.readline()
        if not todoTextLine: break
        print(todoTextLine)
    todoTextFile.close()

class init():
    if(chooseMode == "1"):
        getTodoItem()
    elif(chooseMode == "2"):
        showTodoItems()
    else:
        getNumber()
              
init()
    

    
    