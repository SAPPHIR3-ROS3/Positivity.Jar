from datetime import datetime as Time
from os import getcwd as CWD
from os import listdir as ListDir
from os import mkdir as CreateDir
from os import replace as Move
from os.path import isdir as IsDir
from os.path import realpath as Path
from random import shuffle as Mix
from tkinter import Tk as Tk

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

def YearFolder():
    Year = str(CWD()) + "/" + str(Time.now().year)
    if not IsDir(Year):
        CreateDir(str(Time.now().year + " Memories"))

def CreateMemory(): #this function create a new memory
    Dir = str(CWD() + "/" + Time.now().year + " Memories" + "/")  # year directory
    Now = Time.now() #memory time tamp
    File = Now.date() + "-" + Now.hour + "-" + Now.minute + "-" + Now.second #format file name correctly

    with open(Dir + File + ".txt", "w+") as Memory: #file writing of the memory
        print("Write what made you happy just now (check everything is right)")

        while True: #loop for confirmation of the memory
            Text = input() #memory
            print("Are you sure, it's everything correct? <y>")

            if input()[0].lower() == "y": #confirmation check
                break

        Memory.write(Text) #memory writing
        Memory.write(str(Now.date())) #date writing

def SeeMemories(Random = True, All = False): # function allow to see (all) memories
    Dir = str(CWD() + "/" + Time.now().year + " Memories")  # year directory

    if len(ListDir(Dir)) == 0:
        Dir = str(CWD() + "/" + int(Time.now().year - 1) + " Memories")  # year directory fixed

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
    while not 1 <= Answer <= len(Menu.keys()): #check if the user input is acceptable
        Answer = int(input("type the number matched with the option you want to select: ")) # ask for user input

    eval(list(Menu.values())[Answer - 1]) #trasform the string in the corresponding function

if __name__ == "__main__": #launch of the program (directly)
    Main()