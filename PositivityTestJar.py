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

HRel = 0.5  # relative half
Font = lambda Size: ('Courier', Size)

class PositivityJar(Tk):
    def __init__(self, *args, **kwargs):
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
        self.Icon = Photo(file='textures\icon.png')
        self.iconphoto(True, self.Icon)
        self.title(self.Title)
        self.geometry(self.Sizes + self.Pos)

        self.Screens = {}
        pass

    @staticmethod
    def Raise(Screen):  # this function raise the selected frame to the top
        Screen.tkraise()

class Menu(Frame):
    def __init__(self, Parent):
        Frame.__init__(self, Parent)

        MenuTopLabel = Label(self, text='Welcome to\nPositivity.Jar', font=('Courier', 32), bd=10) #welcome label
        MenuTopLabel.place(anchor='n', relx=HRel, rely=0.015, relwidth=1, relheight=0.2) #placing the label

        self.Menu =\
            [
                Button
                    (
                        self,
                        text='Create new memory',
                        font=Font(14),
                    ),
                Button
                    (
                        self,
                        text='Show all memories of this year\n(random order)',
                        font=Font(14),
                    ),
                Button
                    (
                        self,
                        text='Show all memories of this year\n(chronological order)',
                        font=Font(14),
                    ),
                Button
                    (
                        self,
                        text="See all the memories of all year\n(random order)",
                        font=Font(14),
                    ),
                Button
                    (
                        self,
                        text='See all the memories of all year\n(chronological order)',
                        font=Font(14),
                    )
            ]

        for i in range(len(Menu)): #loop to place every button
            self.Menu[i].place \
                    (
                    anchor='n', #anchored at nord
                    relx=HRel, #centered
                    rely=0.25 + (i * 0.125),#y position
                    relwidth=0.9 #% of window width
                ) #placing the button

class Input(Frame):
    def __init__(self, Parent = None):
        self.Name = 'Input'
        Frame.__init__(self, Parent)

        self.InputLabel = Label(self, text='Memory:', font=('Courier', 24)) #top label of input frame
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
            ) #return at menu button and clean the text box
        self.BackMenu.place(anchor = 'n', relx = HRel, rely = 0.945, relwidth = 0.9) #placing the button

class View(Frame):
    def __init__(self, Parent = None, FrameName = str()):
        self.Name = FrameName
        Frame.__init__(self, Parent)

        TopViewFrame = Frame(self)  # frame for top label and search bar
        TopViewFrame.place(relx=0, rely=0, relwidth=1, relheight=0.2)  # placing the frame top

        #TODO insert the middle Memorieslist frame here
        #.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.745) #placing the frame under the top frame

        BottomViewFrame = Frame(self)  # frame for back to menu
        BottomViewFrame.place(relx=0, rely=0.945, relwidth=1, relheight=0.1)  # placing the frame at the bottom

        #############################################################################################################Top

        MemoriesLabel = Label \
            (
                TopViewFrame,
                text='Your Memories:',
                font=('Courier', 32),
            ) #top label in top frame
        MemoriesLabel.place(anchor='n', relx=HRel, relwidth=1, relheight=0.7) #placing the label

        SearchBar = TextBox(TopViewFrame, font=('Courier', 16)) #search bar to search keywords in memories text
        SearchBar.place(anchor='n', relx=HRel, rely=0.7, relwidth=0.99, relheight=0.2) #placing the search bar TODO

        SearchButton = Button \
            (
                TopViewFrame,
                text='Search',
                font=('Courier', 14),
            )  # button to research
        SearchButton.place(anchor='n', relx=0.86, rely=0.7225, relwidth=0.25, relheight=0.17) #placing the button

        #########################################################################################################Top end
        #####################################################################################################MemorieList
        #TODO add something here (probably)
        #################################################################################################MemorieList end
        ##########################################################################################################Bottom
        BackView = Button \
            (
                BottomViewFrame,
                text='Back to menu',
                font=('Courier', 10),
            )  # return at menu button
        BackView.place(anchor='n', relx=HRel, rely=0.05, relwidth=0.9)  # placing the button

class MemoriesList(Frame):
    def __init__(self, Parent = None, ListName = 'Memories'):
        self.Name = ListName
        Frame.__init__(self, Parent)
    pass


if __name__ == '__main__' : PositivityJar().mainloop() #one line main(???)