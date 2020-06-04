from datetime import datetime as Time
from random import shuffle as Mix
from os import system as Sys
from os import name as Name
from random import choices as Picks
from sqlite3 import connect as Connect
from sqlite3 import PARSE_DECLTYPES as TimeStamps
from string import ascii_uppercase as Alphabet
from tkinter import Button as Button
from tkinter import Frame as Frame
from tkinter import Label as Label
from tkinter import Listbox as ListBox
from tkinter import messagebox as MSGBox
from tkinter import PhotoImage as Photo
from tkinter import Scrollbar as Bar
from tkinter import Text as TextBox
from tkinter import Tk as Tk

def Clear(): #this function clear the console
    if Name == 'nt': #check if it's a windows system
        _ = Sys('cls')

    else: #is a unix based system
        _ = Sys('clear')

## Start GUI implementation

def Confirmation(Function , *args , Text = str(), Other = None, **aargs): #this function pops up a message for 2 actions
    Confirm = MSGBox.askquestion('Confirmation', Text) #messagebox yes/no

    if Confirm == 'yes': #positive answer
        Function(*args)

    else: #negative answer
        try:
            Other(**aargs)

        except Exception as Error:
            print(Error)

def Raise(Screen): #this function raise the selected frame to the top
    Screen.tkraise()

def TKinterSetup():
    Root = Tk() #ambient
    HRel = 0.5 #relative max size halved
    WIDTH = 400  #window width
    HEIGHT = 720 #window height
    SWIDTH = Root.winfo_screenwidth() #screen width
    SHEIGHT = Root.winfo_screenheight() #screen height
    X = (SWIDTH - WIDTH) / 2
    Y = (SHEIGHT - HEIGHT) / 2
    Dim = str(str(WIDTH) + 'x' + str(HEIGHT)) #string of sizes
    Pos = str('+' + str(int(X)) + '+' + str(int(Y)))
    Title = 'Positivity.Jar'
    Icon = Photo(file='textures\icon.png') #program icon
    Root.iconphoto(True, Icon) #setting the icon
    Root.title(Title) #setting the title
    Root.geometry(Dim + Pos) #setting dimensions

    ################################################################################################################menu

    MenuFrame = Frame(Root) #menu window area
    MenuFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)  #placing the menu frame in the window

    MenuTopLabel = Label(MenuFrame, text = 'Welcome to\nPositivity.Jar', font = ('Courier', 32), bd = 10) #welcome label
    MenuTopLabel.place(anchor = 'n', relx = HRel, rely = 0.015, relwidth = 1, relheight = 0.2) #placing the label



    def ButtonSelection(Selection = int()):
        nonlocal Sel
        Sel = Selection

    Menu =\
        [
            Button
            (
                MenuFrame,
                text = 'Create new memory',
                font = ('Courier', 20),
                command = lambda : Raise(InputFrame) #raising a top level the input frame
            ),
            Button
            (
                MenuFrame,
                text = 'Show all memories of this year\n(random order)',
                font = ('Courier', 14),
                command = lambda : [Raise(ViewFrame), ButtonSelection(0)]
            ),
            Button
            (
                MenuFrame,
                text = 'Show all memories of this year\n(chronological order)',
                font=('Courier', 14),
                command = lambda : [Raise(ViewFrame), ButtonSelection(1)]
            ),
            Button
            (
                MenuFrame,
                text = "See all the memories of all year\n(random order)",
                font=('Courier', 14),
                command = lambda : [Raise(ViewFrame), ButtonSelection(2)]
            ),
            Button
            (
                MenuFrame,
                text = "See all the memories of all year\n(chronological order)",
                font = ('Courier', 14),
                command = lambda: [Raise(ViewFrame), ButtonSelection(3)]
            )
        ] #list of buttons of the menu

    for i in range(len(Menu)): #loop to place every button
        Menu[i].place\
            (
                anchor = 'n', #anchored at nord
                relx = HRel, #centered
                rely = 0.25 + (i * 0.125), #y position
                relwidth = 0.9 #% of window width
            )# placing the button

    ###############################################################################################################input

    InputFrame = Frame(Root) # memory insertion frame
    InputFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1) #placing the input frame

    InputLabel = Label(InputFrame, text = 'Memory:', font = ('Courier', 24)) #top label of input frame
    InputLabel.place(anchor = 'n', relx = HRel, relwidth = 1, relheight = 0.1) #placing the top label

    WarningLabel = Label\
        (
            InputFrame,
            text = 'attention:\ninserted memories can no longer be modified',
            font = ('Courier', 10),
            fg = '#ff0000'
        ) #smaller red label
    WarningLabel.place(anchor = 'n', relx = HRel, rely = 0.09, relwidth = 1, relheight = 0.04) #placing the label

    MemoryInput = TextBox(InputFrame, font = ('Courier', 16)) #text box for memory insertion
    MemoryInput.place(anchor = 'n', relx = HRel, rely = 0.15, relwidth = 0.98, relheight = 0.7) #placing the textbox


    Submit = Button\
        (
            InputFrame,
            text = 'Create Memory',
            font = ('Courier', 20),
            command = lambda : Confirmation(InsertMemory, MemoryInput.get(1.0))
        ) #sbmition button to insert new memory
    Submit.place(anchor = 'n', relx = HRel, rely = 0.8635, relwidth = 0.9) #placing the button

    BackInput = Button\
        (
            InputFrame,
            text = 'Back to menu',
            font = ('Courier', 10),
            command = lambda : [MemoryInput.delete(1.0, 'end'), Raise(MenuFrame)]
        ) #return at menu button and clean the text box
    BackInput.place(anchor = 'n', relx = HRel, rely = 0.945, relwidth = 0.9) #placing the button

    ###########################################################################################################memmories

    MemoOpts =\
        [
            [True, False], #random order, last year only
            [False, False], #chronological order, last year only
            [True, True], #random order, all years
            [False, False] ##chronological order, all years
        ] #parameters for a specific query of the database

    MemoriesDB = lambda x: ShowMemories(MemoOpts[x][0], MemoOpts[x][1])  # memories of the db based on user options
    Sel = int()
    Memories = MemoriesDB(Sel)

    ViewFrame = Frame(Root) #memory view root frame
    ViewFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)  #placing the frame in the window

    TopViewFrame = Frame(ViewFrame) #frame for top label and search bar
    TopViewFrame.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.2) #placing the frame top

    ListFrame = Frame(ViewFrame) #canvas for memories in database
    ListFrame.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.745) #placing the frame under the top frame

    BottomViewFrame = Frame(ViewFrame) #frame for back to menu
    BottomViewFrame.place(relx = 0, rely = 0.945, relwidth = 1, relheight = 0.1) #placing the frame at the bottom

    MemoriesLabel = Label\
        (
            TopViewFrame,
            text = 'Your Memories:',
            font = ('Courier', 32),
        ) #top label in top frame
    MemoriesLabel.place(anchor = 'n', relx = HRel, relwidth = 1, relheight = 0.7) #placing the label

    SearchBar = TextBox(TopViewFrame, font = ('Courier', 16)) #search bar to search keywords in memories text
    SearchBar.place(anchor = 'n', relx = HRel, rely = 0.7, relwidth = 0.99, relheight = 0.2) #placing the searchbar TODO

    SearchButton = Button\
        (
            TopViewFrame,
            text = 'Search',
            font = ('Courier', 14),
            command = lambda : None
        ) #botton to research
    SearchButton.place(anchor = 'n', relx = 0.86, rely = 0.7225, relwidth = 0.25, relheight = 0.17) #placingthe button

    SBar = Bar(ListFrame, orient = 'vertical')
    ListMemoryBox = ListBox\
        (
            ListFrame,
            selectmode = 'browse',
            bg = '#5f00f1',
            activestyle = 'none',
            font = ('Courier', 14),
        )
    # ListMemoryBox.config()
    ListMemoryBox.place(anchor = 'n', relx = HRel, rely = 0, relwidth = 0.99, relheight = 1)
    BackView = Button\
        (
            BottomViewFrame,
            text = 'Back to menu',
            font = ('Courier', 10),
            command = lambda: Raise(MenuFrame)
        )  #return at menu button
    BackView.place(anchor = 'n', relx = HRel, rely = 0.05, relwidth = 0.9)  #placing the button

    Raise(MenuFrame) #raising the menu as first viewed frame
    return Root

## Start SQl implementation

Connector = Connect("Memories.db", detect_types = TimeStamps)
SQLShell = Connector.cursor()
SQLTables = "SELECT name FROM sqlite_master WHERE type = 'table'"

def YearTable(): #this function declares a table of the current year inside  the database if non-existent
    with Connector: #database as  context manager
        Table = "My" + str(Time.now().year) + "Memories" #table name
        DB = SQLShell.execute(SQLTables).fetchall()
        DataBase = [str(Tab[0]) for Tab in DB] #getting names of al tables
        if not Table in DataBase: #if the table is in the list
            SQLQueryTable = """
                    CREATE TABLE """ + Table + """
                    (
                        MemoryID text PRIMARY KEY,
                        Memory text,
                        Timestamp timestamp,
                        Date date
                    )
                    """
            SQLShell.execute(SQLQueryTable) #SQL command to create the table

def InsertMemory(Text = str()): #this function create a new memory inside the table of the current year
    Now = Time.now() #timestamps
    Today = Now.date() #date
    MemoryID = str(Now) + str("".join(Picks(Alphabet, k = 6)))
    TableName = "My" + str(Now.year) + "Memories"

    try:
        if not Text == '':
            with Connector: #database as context manger
                SQLQuery = "INSERT INTO " + TableName + " VALUES(:MemID, :Text, :Now, :Date)"
                Values = {"MemID" : MemoryID, "Text" : Text, "Now" : Now, "Date" : Today} #values safely inserted
                SQLShell.execute(SQLQuery, Values) #execute the sql query correctly
                print("Memory inserted in the database")

    except Exception as Error:
        print(Error)

    ReturnMenuSQL()

def ShowMemories(Random = True, All = False): #this function show the memories selected
    YearsQuery = SQLTables + " AND name LIKE '%Memories'" #SQLQuery to find the name of all tables of memories
    Memories = [] #list of all selected memories
    Years = [str(Tab[0]) for Tab in SQLShell.execute(YearsQuery).fetchall()] #list of names of the tables of memories

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

            if len(Memories) == 0:
                MemoryQuery = "SELECT Memory, Date FROM " + Years[-2]  #query for memories of the previous year
                YearMemories = SQLShell.execute(MemoryQuery).fetchall()  # getting all memories from the selected year
                Memories = [[Data[0], Data[1]] for Data in YearMemories]  # formatting properly the data

    if Random:  #shuffle the memory order if the user want to
        Mix(Memories)  #mix the memories

    # for i in Memories:
    #     print(i)

    return Memories

def ReturnMenuSQL(): #this function check if return to the menu (SQL)
    while True:
        Pick = input("Do you want to return to the menu ?<y/n> ")

        if Pick[0].lower() == "y":
            Clear()
            MainSQL()

        elif Pick[0].lower() == "n":
            Clear()
            quit()

        else:
            print("Option not valid")

        Clear()

def MainSQL():
    Clear()
    YearTable()
    Title = "Positivity.Jar" #program title
    Welcome = "Welcome to Positivity.Jar, a place to store everything that make you happy during the year" #description
    Menu = \
        {
            "Create a new positive memory": "InsertMemory()",
            "See all the positive memories for this year (random order)": "ShowMemories()",
            "See all the positive memories for this year (chronological order)": "ShowMemories(False)",
            "See all the positive memories of all year (random order)": "ShowMemories(True, True)",
            "See all the positive memories of all year (chronological order)": "ShowMemories(False, True)",
            "Quit the program": "quit()"
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


    eval(list(Menu.values())[Answer - 1])  # transform the string in the corresponding function
    input("Press any key to continue")

##end sql implementation

if __name__ == "__main__": #launch of the program (directly)
    ROOT = TKinterSetup()
    ROOT.mainloop()