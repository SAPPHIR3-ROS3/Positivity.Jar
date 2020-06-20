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
from tkinter import Canvas as Canvas
from tkinter import messagebox as MSGBox
from tkinter import PhotoImage as Photo
from tkinter import Scrollbar as Bar
from tkinter import Text as TextBox
from tkinter import Tk as Tk

HRel = 0.5  # relative half
Font = lambda Size: ('Courier', Size)

class PositivityJar(Tk):
    def __init__(self, *args, **kwargs):
        self.Database = SQLInterface()
        self.Database.Check(str(Time.now().year))

        Tk.__init__(self, *args, **kwargs)
        self.WIDTH = 400
        self.HEIGHT = 720
        self.SWIDTH = self.winfo_screenwidth()
        self.SHEIGHT = self.winfo_screenheight()
        self.X = int((self.SWIDTH - self.WIDTH) / 2)
        self.Y = int((self.SHEIGHT - self.HEIGHT) / 2)
        self.Sizes = str(self.WIDTH) + 'x' + str(self.HEIGHT)
        self.Pos = '+' + str(self.X) + '+' + str(self.Y)
        self.Title = 'PositivityTestJar'
        self.Icon = Photo(file = 'textures\icon.png')
        self.iconphoto(True, self.Icon)
        self.title(self.Title)
        self.geometry(self.Sizes + self.Pos)

        self.Screens =\
            {
                Menu().Name: Menu(self),
                Input().Name: Input(self),
                View().Name: View(self)
            }

        for Screen in self.Screens.values():
            Screen.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        self.Raise('Menu')

    def Raise(self, Screen = str()): #this function raise the selected frame to the top
        self.Screens[Screen].tkraise()

class Menu(Frame):
    def __init__(self, Parent = None):
        self.Name = 'Menu'
        Frame.__init__(self, Parent)

        MenuTopLabel = Label(self, text='Welcome to\nPositivity.Jar', font= Font(32), bd=10) #welcome label
        MenuTopLabel.place(anchor='n', relx=HRel, rely=0.015, relwidth=1, relheight=0.2) #placing the label

        self.Options =\
            [
                Button
                    (
                        self,
                        text = 'Create new memory',
                        font = Font(14),
                        command = lambda : Parent.Raise('Input') #raising to the top the input frame
                    ),
                Button
                    (
                        self,
                        text='Show all memories of this year\n(random order)',
                        font=Font(14),
                        command = lambda :
                        [
                            Parent.Raise('View'), #raising to the top the view frame
                        ]
                    ),
                Button
                    (
                        self,
                        text='Show all memories of this year\n(chronological order)',
                        font=Font(14),
                        command = lambda :
                        [
                            Parent.Raise('View'), #raising to the top the view frame
                        ]
                    ),
                Button
                    (
                        self,
                        text="See all the memories of all year\n(random order)",
                        font=Font(14),
                        command = lambda :
                        [
                            Parent.Raise('View'), #raising to the top the view frame
                        ]
                    ),
                Button
                    (
                        self,
                        text='See all the memories of all year\n(chronological order)',
                        font=Font(14),
                        command = lambda :
                        [
                            Parent.Raise('View'), #raising to the top the view frame
                        ]
                    )
            ]

        for i in range(len(self.Options)): #loop to place every button
            self.Options[i].place \
                    (
                    anchor='n', #anchored at nord
                    relx=HRel, #centered
                    rely=0.25 + (i * 0.125),#y position
                    relwidth=0.9 #% of window width
                ) #placing the button

class Input(Frame):
    def __init__(self, Parent = None, Env = None):
        self.Name = 'Input'

        Frame.__init__(self, Parent)

        self.InputLabel = Label(self, text='Memory:', font= Font(24)) #top label of input frame
        self.InputLabel.place(anchor='n', relx=HRel, relwidth=1, relheight=0.1) #placing the top label

        self.WarningLabel = Label \
            (
                self,
                text='attention:\ninserted memories can no longer be modified',
                font= Font(10),
                fg='#ff0000'
            ) #smaller red label
        self.WarningLabel.place(anchor='n', relx=HRel, rely=0.09, relwidth=1, relheight=0.04) #placing the label

        self.MemoryInput = TextBox(self, font = Font(10)) #text box for memory insertion
        self.MemoryInput.place(anchor='n', relx=HRel, rely=0.15, relwidth=0.98, relheight=0.7) #placing the textbox

        self.Submit = Button \
            (
                self,
                text='Create Memory',
                font = Font(20),
            ) #submition button to insert new memory
        self.Submit.place(anchor='n', relx=HRel, rely=0.8635, relwidth=0.9) #placing the button

        self.BackMenu = Button \
            (
                self,
                text='Back to menu',
                font=Font(10),
                command = lambda: Parent.Raise('Menu')
            ) #return at menu button and clean the text box
        self.BackMenu.place(anchor = 'n', relx = HRel, rely = 0.945, relwidth = 0.9) #placing the button

class View(Frame):
    def __init__(self, Parent = None, Env = None, Filter = -1):
        self.Name = 'View'

        Frame.__init__(self, Parent)

        self.TopViewFrame = Frame(self)  # frame for top label and search bar
        self.TopViewFrame.place(relx=0, rely=0, relwidth=1, relheight=0.2)  # placing the frame top

        self.MemoriesFrame = MemoriesList(self)
        self.MemoriesFrame.place \
            (
                relx = 0,
                rely = 0.2,
                relwidth = 1,
                relheight = 0.745
            ) #placing the frame under the top frame

        self.BottomViewFrame = Frame(self) #frame for back to menu
        self.BottomViewFrame.place(relx=0, rely=0.945, relwidth=1, relheight=0.1)  # placing the frame at the bottom

        #############################################################################################################Top

        self.MemoriesLabel = Label \
            (
                self.TopViewFrame,
                text='Your Memories:',
                font=('Courier', 32),
            ) #top label in top frame
        self.MemoriesLabel.place(anchor='n', relx=HRel, relwidth=1, relheight=0.7) #placing the label

        self.SearchBar = TextBox(self.TopViewFrame, font=('Courier', 16)) #searchbar to search keywords in memories text
        self.SearchBar.place(anchor='n', relx=HRel, rely=0.7, relwidth=0.99, relheight=0.2) #placing the search bar TODO

        self.SearchButton = Button \
            (
                self.TopViewFrame,
                text='Search',
                font=('Courier', 14),
            )  # button to research
        self.SearchButton.place(anchor='n', relx=0.86, rely=0.7225, relwidth=0.25, relheight=0.17) #placing the button

        #########################################################################################################Top end
        ##########################################################################################################Bottom

        BackView = Button \
            (
                self.BottomViewFrame,
                text = 'Back to menu',
                font = ('Courier', 10),
                command = lambda: Parent.Raise('Menu')
            )  # return at menu button
        BackView.place(anchor='n', relx=HRel, rely=0.05, relwidth=0.9)  # placing the button

class MemoriesList(Frame):
    def __init__(self, Parent = None, ListName = 'Memories', Items = []):
        self.Parent = Parent
        self.Name = ListName
        Frame.__init__(self, Parent)
        self.SBar = Bar(self, orient = 'vertical')
        self.Memories = Canvas(self, yscrollcommand = self.SBar.set)
        self.SBar.config(command = self.Memories.yview)
        self.SBar.pack(side = 'right', fill = 'y')
        self.Memories.pack(side='left', fill = 'both')
        self.Items = self.Convert(Items)

    def Convert(self, Items):
        # MemoOpts = \
        #     [
        #         [True, False], #random order, last year only
        #         [False, False], #chronological order, last year only
        #         [True, True], #random order, all years
        #         [False, True] #chronological order, all years
        #     ] #parameters for a specific query of the database

        ItemList = []

        for Item in Items:
            ItemList.append(MemoryItem(Text = Item[0], Date = Items[1]))
            pass

        return ItemList

    pass

class MemoryItem(Frame):
    def __init__(self, Parent = None, Text = str(), Date = str()):
        Frame.__init__(self, Parent, bg = '#c4c4c4')

        self.RawMemory = Text #setting raw text of the memory
        self.MemoryComplete = Text + ' ' * (252 - len(Text)) #memory text 255 chars long
        self.Memory = ''

        for i in range(6): #loop for formatting properly
            self.Memory += self.MemoryComplete[42 * i : 42 * (i + 1)] + '\n' #string divided in 6 lines

        self.Memory = self.Memory[: -1] #removing last new line
        self.Date = Date #setting the date

        self.MemoryLabel = Label(self, text = self.Memory, font = Font(11), bd = 4 , bg = '#04c4c4')
        # self.MemoryLabel.place(anchor='n', relx=HRel, rely = 0, relwidth = 1)
        self.MemoryLabel.pack()
        self.DateLabel = Label(self, text = Date, font = Font(8), bd = 4, bg = '#c4c4c4')
        # self.DateLabel.place(anchor='n', relx=HRel, rely = 0.8, relwidth= 1)
        self.DateLabel.pack()

        pass

class SQLInterface:
    def __init__(self):
        self.Connector = Connect("Memories.db", detect_types = TimeStamps)
        self.Shell = self.Connector.cursor()
        self.SQLTables = "SELECT name FROM sqlite_master WHERE type = 'table'"


    def Check(self, Year = str()):
        with self.Connector: #connector as text manager
            Table = 'My' + Year + 'Memories' #table name
            DB = self.Shell.execute(self.SQLTables).fetchall() #execute the query fetching all the results
            Tables = [str(Tab[0]) for Tab in DB] #getting names of al tables
            if not Table in Tables: #if the table is in the list
                SQLQueryTable = """
                    CREATE TABLE """ + Table + """
                    (
                        MemoryID text PRIMARY KEY,
                        Memory text,
                        Timestamp timestamp,
                        Date date
                    )
                    """
                self.SQLShell.execute(SQLQueryTable) #SQL command to create the table

    def Insert(self, Text = str()):
        Now = Time.now()  # timestamps
        Today = Now.date()  # date
        MemoryID = str(Now) + str("".join(Picks(Alphabet, k=6)))
        Table = "My" + str(Now.year) + "Memories"

        try:
            if not Text == '':
                with self.Connector:  # database as context manger
                    SQLQuery = "INSERT INTO " + Table + " VALUES(:MemID, :Text, :Now, :Date)"
                    Values = {"MemID": MemoryID, "Text": Text, "Now": Now, "Date": Today} #values safely inserted
                    self.Shell.execute(SQLQuery, Values) #execute the sql query correctly
                    print('Memory inserted in the database')

        except Exception as Error:
            print(Error)

    def Show(self, Random = True, All = False):
        YearsQuery = self.SQLTables + " AND name LIKE '%Memories'" #SQLQuery to find the name of all tables of memories
        Years = [str(Tab[0]) for Tab in self.Shell.execute(YearsQuery).fetchall()] #list of names of the memory tables
        Memories = []

        with self.Connector:
            if All:
                for Year in Years:
                    MemoryQuery = "SELECT Memory, Date FROM " + Year  #query for memories of a selected year
                    YearMemories = self.Shell.execute(MemoryQuery).fetchall() #getting memories from the selected year
                    YearMemories = [[Data[0], Data[1]] for Data in YearMemories]  #formatting properly the data
                    Memories.extend(YearMemories)  #proper extension of the list of all memories

            else:
                MemoryQuery = "SELECT Memory, Date FROM " + Years[-1]  #query for memories of the last registered year
                YearMemories = self.Shell.execute(MemoryQuery).fetchall()  #getting all memories from the selected year
                Memories = [[Data[0], str(Data[1])] for Data in YearMemories]  #formatting properly the data

                if len(Memories) == 0:
                    MemoryQuery = "SELECT Memory, Date FROM " + Years[-2] #query for memories of the previous year
                    YearMemories = self.Shell.execute(MemoryQuery).fetchall() #getting memories from the selected year
                    Memories = [[Data[0], Data[1]] for Data in YearMemories] #formatting properly the data

        if Random: #shuffle the memory order if the user want to
            Mix(Memories) #mix the memories

        pass

if __name__ == '__main__' :  #PositivityJar().mainloop() #one line main(???)
    test = Tk()
    test.geometry('400x400+100+100')
    test.title('test')
    mem = 'a' * 252
    d = '12-12-2024'
    memtest = MemoryItem(test, mem, d)
    memtest.pack()
    
    test.mainloop()
