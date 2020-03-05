from datetime import datetime as Time
from os import getcwd as CWD
from os import listdir as ListDir
from os import mkdir as CreateDir
from os.path import isdir as IsDir
from random import shuffle as Mix
from os import system as Sys
from os import name as Name

def Clear(): #this function clear the console
    if Name == 'nt': #check if it's a windows system
        _ = Sys('cls')

    else: #is a unix based system
        _ = Sys('clear')

##start non sql implementation

def YearFolder():
    Year = str(CWD()) + "/My " + str(Time.now().year) + " Memories"
    if not IsDir(Year):
        CreateDir(str(str(Time.now().year) + " Memories"))

def CreateMemory(): #this function create a new memory
    Dir = str(CWD() + "/My " + str(Time.now().year) + " Memories" + "/")  # year directory
    Now = Time.now() #memory timestamp
    DateTime = str(Now.hour) + "-" + str(Now.minute) + "-" + str(Now.second) #hours-minutes-seconds
    File = str(Now.date()) + "-" + DateTime #format file name correctly

    with open(Dir + File + ".txt", "w+") as Memory: #file writing of the memory
        print("Write what made you happy just now (check everything is right)")

        while True: #loop for confirmation of the memory
            Text = input() #memory
            print("Are you sure, it's everything correct? <y>")

            if input()[0].lower() == "y": #confirmation check
                break

        Memory.write(Text) #memory writing
        Memory.write("\n" + str(Now.date())) #date writing
        print("Memory inserted in the database")

        ReturnMenu()

def SeeMemories(Random = True, All = False): # function allow to see (all) memories
    Dir = str(CWD() + "/My " + str(Time.now().year) + " Memories")  # year directory

    if len(ListDir(Dir)) == 0:
        Dir = str(CWD() + "/My " + int(Time.now().year - 1) + " Memories")  # year directory fixed

    Memories = [] #list of memories
    Years = [] #list of years directory
    Files = [] #list of files directory

    if All: #check if the user wants to see all the memories
        Years = [str(CWD() + "/" + Year) for Year in ListDir(CWD()) if Year.endswith("Memories")] #every right folder

        for Year in Years: #loop for every file directory
            Files.extend([str(Year + "/" + File) for File in ListDir(Year)]) #files directories are in the same list

    else: #otherwise the use wants to see only the current/past year memories
        Files = [str(Dir + "/" + File) for File in ListDir(Dir)] #all file directories of the year

    for File in Files: #loop for every memory
        with open(File, "r") as FileDir: #opening every memory
            Memories.append(FileDir.read()) #reading memory

    if Random: #shuffle the memory order if the user want to
        Mix(Memories) #mix the memory

    print("Memories:")
    print()

    for Memory in Memories: #loop to print all memories
        print(Memory)
        print()

    ReturnMenu()

def ReturnMenu(): #this function check if return to the menu
    while True:
        Pick = input("Do you want to return to the menu ?<y/n> ")

        if Pick[0].lower() == "y":
            Clear()
            Main()

        elif Pick[0].lower() == "n":
            Clear()
            quit()

        else:
            print("Option not valid")

        Clear()

def Main(): #main function
    Clear()
    YearFolder() #check if the folder of the year exist either create it
    Title = "Positivity.Jar" #program title
    Welcome = "Welcome to Positivity.Jar, a place to store everything that make you happy during the year" #description
    Menu = \
        {
            "Create a new positive memory" : "CreateMemory()",
            "See all the positive memories for this year (random order)" : "SeeMemories()",
            "See all the positive memories for this year (chronological order)" : "SeeMemories(False)",
            "See all the positive memories of all year (random order)" : "SeeMemories(True, True)",
            "See all the positive memories of all year (chronological order)" :  "SeeMemories(False, True)",
            "Quit the program" : "quit()"
        } #menu options
    Answer = - 1

    while not 1 <= Answer <= len(Menu.keys()):  # check if the user input is acceptable
        print(Welcome)
        print()

        for Key in Menu.keys():  # for loop  for every option
            print(str(list(Menu.keys()).index(Key) + 1) + ")", Key)

        print()
        Answer = int(input("type the number matched with the option you want to select: "))  # ask for user input
        Clear()

    eval(list(Menu.values())[Answer - 1]) #transform the string in the corresponding function
    input("Press any key to continue")

##end non sql implementation

if __name__ == "__main__": #launch of the program (directly)
    Main()