from random import choice, shuffle
def Trust():
    print("\n\n\t\t\t\t   ВЕРНО")
    print("\t\t\t   Продолжить?(y/n)")
    choice = input("> ")
    if choice=="y":
        QuestionShow()
    else:
        return 0
def Failed():
    print("\n\n\t\t\t\t   НЕ ВЕРНО")
    print("\t\t\t     Повторить?(y/n)")
    choice = input("> ")
    if choice=="y":
        QuestionShow()
    else:
        return 0
def QuestionShow():
    variables = {}
    num=1
    with open('questions.txt', 'r') as file:
        questions=[]
        for x in file.readlines():
            questions.append(x)
        question=choice(questions).split("\"")
        question=[x for x in question if x not in (" ","\n","",None)]
        answer=question[len(question)-1]
        print(f"\n\n\t\t\t   --- {question[0]} ---")
        question.remove(question[0])
        question.remove(question[len(question)-1])
        shuffle(question)
        for j in range(0,len(question)):
            print(f"\t\t\t    [{num}] - {question[j]}")
            variables[num] = question[j]
            num+=1
        print('\t\t\t   '+'-'*(len(question[1])+6))
        Question(answer, variables)
def Question(Answer, variables):
    choice = int(input("> "))
    if variables[choice]==Answer:
        Trust()
    else:
        Failed()
