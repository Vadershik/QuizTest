import Tasks
import Editor
def ShowStartMenu():
    print("\n\n\t\t\t   --------| MENU |-------")
    print("\t\t\t\t [1] - Test")
    print("\t\t\t\t [2] - Editor")
    print("\t\t\t\t [2] - Exit")
    print("\t\t\t   ------------------------")
def StartMenu():
    choice = int(input("Ваш выбор:"))
    if(choice==1): Tasks.QuestionShow()
    if(choice==2): Editor.Main()
    else: return 0
