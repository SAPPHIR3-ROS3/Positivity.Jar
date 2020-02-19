from datetime import datetime as Time
from os import getcwd as CWD
from os import mkdir as CreateDir
from os import replace as Move
from os.path import isdir as IsDir
from os.path import realpath as Path
from tkinter import Tk as Tk

def YearFolder():
    Year = str(CWD()) + "/" + str(Time.now().year)
    if not IsDir(Year):
        CreateDir(str(Time.now().year + " Memories"))

def Setup(): #this function make sure that the script is in the right directory
    DirName = "PositivityJar" #name of the directory of the program
    if not str(Path(__file__)).endswith(DirName + "/" + __file__): #check if the file is in the directory
        try:
            Move(Path(__file__), Path(__file__)[: - len(__file__)] + DirName + "/" + __file__) #try to create the folder

        except Exception as Error: #if the folder is not created
            print(Error) #print the exception error
            print("Try opening the program in another directory with a lower access level") #solution

    else:
        return None

def CreateMemory(): #this function create a new memory
    Dir = str(CWD() + "/" + Time.now() + "/")
    Now = Time.now()
    File = Now.date() + "-" + Now.hour + "-" + Now.minute + "-" + Now.second

    with open(Dir + File + ".txt", "w+") as Memory:
        print("Write what made you happy just now (check everything is right)")


def SeeMemories(Random = True, All = False): # function allow to see (all) memories
    pass

def Main(): #main function
    Setup() #setup the environment
    YearFolder() #check if the folder of the year exist either create it
    Title = "Positivity.Jar" #program title
    Welcome = "Welcome to Positivity.Jar, a place to store everything that make you happy during the year" #description
    Menu = \
        {
            "Create a new positive memory" : "CreateMemory()",
            "See all the positive memories for this year (random order)" : "SeeMemories()",
            "See all the positive memories for this year (chronological order)" : "SeeMemories(False)",
            "See all the positive memories of all year (random order)" : "SeeMemories(True, True)",
            "See all the positive memories of all year (chronological order)" :  "SeeMemories(False, True)"
        } #menu options

    print(Welcome)

    for Key in Menu.keys(): #for loop  for every option
        print(str(list(Menu.keys()).index(Key) + 1) + ")", Key)

    Answer = - 1
    while not 1 <= Answer <= len(Menu.keys()):
        Answer = int(input("type the number matched with the option you want to select: "))

    eval(list(Menu.values())[Answer - 1])

if __name__ == "__main__":
    Main()