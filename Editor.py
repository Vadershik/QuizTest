def AddQuestion():
    res=[]
    print("Введите вопрос:")
    res.append(input("> "))
    print("Введите кол-во вариантов ответов:")
    for i in range(int(input("> "))):
        res.append(input())
    with open("questions.txt", "a") as file:
        file.write(f'"{res[0]}" "'+"\" \"".join(res[1:])+'" ')
        for i,j in enumerate(res[1:]):
            print(f'[{i}] - {j}')
        print("Введите правильный вариант")
        file.write('"'+res[int(input())+1]+"\"\n")
    #Пока только так
def RemoveQuestion():
    linetodelete=0

    #Part with changing what line he want delete
    print(ListQuestions())
    print("Какую линию вы хотите удалить?")
    linetodelete=int(input("> "))
    lines=[]
    with open("questions.txt", "r") as file:
        lines = file.readlines()
    with open("questions.txt", "w") as file:
        linetodelete=lines[linetodelete]
        Status=False
        for line in lines:
            if Status is True or line!=linetodelete:
                file.write(line)
            else:
                Status=True
                
def ListQuestions():
    out=""
    with open("questions.txt", "r") as file:
        for i,j in enumerate(file.readlines()):
            j=j.split("\"")
            out+=f'[{i}] - {j[1]}'+"\n"
    return out


#Точка входа
def Main():
    while True:
        print("\n\n\t\t\t   -----|What are you want?|-----")
        print("\t\t\t\t [1] - Add Question")
        print("\t\t\t\t [2] - Remove Question")
        print("\t\t\t\t [3] - List Questions")
        print("\t\t\t\t [0] - Exit")
        print("\t\t\t   ------------------------------")
        change=int(input("> "))
        if change==1:
            AddQuestion()
        if change==2:
            RemoveQuestion()
        if change==3:
            print(ListQuestions())
        if change==0:
            break
