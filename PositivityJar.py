from datetime import datetime as Time
from os import getcwd as CWD
from os import listdir as ListDir
from os import mkdir as CreateDir
#from os import replace as Move
from os.path import isdir as IsDir
#from os.path import realpath as Path
from random import shuffle as Mix
from random import choices as Picks
from sqlite3 import connect as Connect
from sqlite3 import PARSE_DECLTYPES as TimeStamps
from string import ascii_uppercase as Alphabet
from tkinter import Tk as Tk

#start non sql implementation

def YearFolder():
    Year = str(CWD()) + "/" + str(Time.now().year) + " Memories"
    if not IsDir(Year):
        CreateDir(str(str(Time.now().year) + " Memories"))

def CreateMemory(): #this function create a new memory
    Dir = str(CWD() + "/" + str(Time.now().year) + " Memories" + "/")  # year directory
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

def SeeMemories(Random = True, All = False): # function allow to see (all) memories
    Dir = str(CWD() + "/" + str(Time.now().year) + " Memories")  # year directory

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

    for Memory in Memories: #loop to print all memories
        print(Memory)
        print()

#end non sql implementation

#start sql implementation

Connector = Connect(":memory:", detect_types = TimeStamps)
SQLShell = Connector.cursor()
SQLTables = "SELECT name FROM sqlite_master WHERE type = 'table'"

def YearTable(): #this function declares a table of the current year inside  the database if non-existent
    with Connector: #database as  context manager
        Table = str(Time.now().year) + "Memories" #table name
        DataBase = [str(Tab[0]) for Tab in SQLShell(SQLTables).fetchall()] #getting names of al tables
        if not Table in DataBase: #if the table is in the list
            SQLShell.execute\
                (
                    """
                    CREATE TABLE """ + Table +
                    """
                    (
                        MemoryID text PRIMARY KEY,
                        Memory text,
                        Timestamp timestamp,
                        Date date
                    )
                    """
                ) #SQL command to create the table

def InsertMemory(): #this function create a new memory inside the table of the current year
    Now = Time.now() #timestamps
    Today = Now.date() #date
    MemoryID = Now + str("".join(Picks(Alphabet, k = 6)))

    print("Write what made you happy just now (check everything is right)")

    while True:  # loop for confirmation of the memory
        Text = input()  # memory
        print("Are you sure, it's everything correct? <y>")

        if input()[0].lower() == "y":  # confirmation check
            break

    try:
        with Connector: #database as context manger
            SQLQuery = "INSERT INTO " + str(Now.year) + "Memories " + "VALUES(:MemID, :Text, :Now, :Date)"
            Values = {"MemID" : MemoryID, "Text" : Text, "Now" : Now, "Date" : Today} #values safely inserted
            SQLShell.execute(SQLQuery, Values) #execute the sql query correctly

    except Exception as Error:
        print(Error)

def ShowMemories(Random = True, All = False):
    YearsQuery = SQLTables + " AND name LIKE %Memories" #SQLQuery to find the name of all tables of memories
    Memories = [] #list of all selected memories
    Years = [str(Tab[0]) for Tab in SQLShell.execute().fetchall(YearsQuery)] #list of names of the tables of memories

    with Connector:
        if All:
            for Year in Years:
                MemoryQuery = "SELECT Memory, Date FROM " + Year #query for memories of the current year
                YearMemories = SQLShell.execute(MemoryQuery).fetchall() #getting all memories from the current year
                YearMemories = [[Data[0], Data[1]] for Data in YearMemories] #formatting properly the data
                Memories.extend(YearMemories) #proper extension of the list of all memories
        else:
            MemoryQuery = "SELECT Memory, Date FROM " + Years[-1] #query for memories of the last registered year
            YearMemories = SQLShell.execute(MemoryQuery).fetchall() #getting all memories from the selected year
            Memories = [[Data[0], Data[1]] for Data in YearMemories] #formatting properly the data

    if Random:  #shuffle the memory order if the user want to
        Mix(Memories)  #mix the memories

    for Memory in Memories:#loop to print all memories
        print(Memory[0])
        print(Memory[1])
        print()

#end sql implementation

def Main(): #main function
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
    Answer = - 1

    print(Welcome)

    for Key in Menu.keys(): #for loop  for every option
        print(str(list(Menu.keys()).index(Key) + 1) + ")", Key)

    while not 1 <= Answer <= len(Menu.keys()): #check if the user input is acceptable
        Answer = int(input("type the number matched with the option you want to select: ")) # ask for user input

    eval(list(Menu.values())[Answer - 1]) #trasform the string in the corresponding function
    input("Press any key to continue")

if __name__ == "__main__": #launch of the program (directly)
    Main()