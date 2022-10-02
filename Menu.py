import Tasks
def ShowStartMenu():
    print("\n\n\t\t\t   --------| MENU |-------")
    print("\t\t\t\t [1] - Start")
    print("\t\t\t\t [2] - Exit")
    print("\t\t\t   ------------------------")
def StartMenu():
    choice = int(input("Your choice:"))
    if(choice==1): Tasks.QuestionShow()
    else: return 0
