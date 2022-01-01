import tkinter as run
from tkinter import *
import random
import time
import threading
from tkinter import font


# Testing
# origin = run.Tk()
# origin.title('Speed Typing Test')
# origin.geometry("1000x1000")
# # mycanvas = run.Canvas(origin, height=1000, width=1000, bg='dark grey')

# myframe = run.Frame(origin, bg='white')
# myframe.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)
        
#     # Sentences used for games stored in .txt file, each sentence is seperated by \n
# sentences = ["The kangaroo is a marsupial from the family Macropodidae (macropods, meaning \"large foot\"). In common use the term is used to describe the largest species from this family, the red kangaroo", "Second Sentence", "Third Sentence"]
# current = random.choice(sentences)
        
# game_sentence = run.Label(origin, text=current)
# game_sentence.place(x=475, y=200)

# user_answer = run.Text(origin, height=1, width=50)
# user_answer.pack()
# user_answer.place(x=475, y=350)
      
# exit = run.Button(origin, text="Exit Game", fg="black", bg="black", height=3, width=10, command=origin.destroy)
# exit.place(x=450, y=850)

# origin.mainloop() 


# Class to do the above functions and more for later efficiency

class game:

    def __init__(self):
        # Set basic outline of application
        self.origin = run.Tk()
        self.origin.title('Speed Typing Test')
        self.origin.geometry("1000x1000")

        #self.mycanvas = run.Canvas(self.origin, height=1000, width=1000, bg='dark grey')
        
        self.myframe = run.Frame(self.origin, bg='white')
        self.myframe.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)
        
        self.bigtitle = run.Label(self.myframe, bg="white", fg='black', text="Speed Typing Game", font=('Lucida Sans Typewriter', 75), anchor="center")
        self.bigtitle.place(x=165, y= 140)

        self.greybox = run.Frame(self.myframe, bg='light grey')
        self.greybox.place(relwidth=0.95, relheight=0.35, relx=0.025, rely=0.575)

        self.sentences = [
                          "Unless someone like you cares a whole awful lot.", 
                          "How far that little candle throws its beams!",
                          "So shines a good deed in a naughty world.",
                          "Practice sentence typing and try to get faster.",
                          "The professional football player who was good at math.",
                          "The politician who was a teacher's pet.",
                          "Korea consists of a peninsula and islands in East Asia.",
                          "Mount Kilimanjaro is a dormant volcano in Tanzania.",
                          "In Python, Strings are arrays of bytes representing Unicode characters.",
                          "Darwin has been described as one of the most influential figures in history.",
                          "Ancient Rome began as an Italic settlement, traditionally dated to 753 BC."
                          ]
        self.random = random.choice(self.sentences)
        
        self.game_sentence = run.Label(self.origin, text=self.random, bg="white", fg="black", font=('Times New Roman', 30))
        self.game_sentence.place(x=500, y=375, anchor="center")
        
        self.user_answer = run.Entry(self.myframe, bg="light grey", fg="white", width=60, font=('Times New Roman', 25))
        self.user_answer.place(x=475, y=475, anchor="center")
        self.user_answer.bind("<KeyPress>", self.play)


        # Button that restarts application                                                                          #create a restart_game function
        self.restart = run.Button(self.myframe, text="Try Again", fg="black", bg="black", height=3, width=17, font=('Times New Roman', 20), command=self.restart_game)
        self.restart.place(x=360, y=675)

        # Speed indicator
        self.speed = run.Label(self.myframe, text="Typing Speed:\n0.0 cps", fg="white", bg="black", height=5, width=25, font=('Times New Roman', 20))
        self.speed.place(x=80, y=650)
        
        # exit application
        self.exit = run.Button(self.myframe, text="Exit", fg="black", bg="black", height=3, width=5, font=('Times New Roman', 15), command=self.origin.destroy)
        self.exit.place(x=35, y=35)

        # Timer starts when user presses first character
        self.time_elapsed = 0
        self.gametime = run.Label(self.myframe, text=f"Time: {self.time_elapsed} seconds", fg="white", bg="black", height=5, width=25, font=('Times New Roman', 20))
        self.gametime.place(x=585, y=650)
        self.game_started = False

        # Set the base value of the game_start to False
        # To be used as a boolean for timer function and other
    

        #graphics

        self.origin.mainloop()


    def play(self, event):
        accuracy = 0
        # start the timer usung threading,
        # threading allows for the timer to work simultaneously with the code
        if self.game_started == False:  
                self.game_started = True
                simul = threading.Thread(target=self.timer)
                simul.start()


        if self.game_sentence.cget('text').startswith(self.user_answer.get()):
            # if the user input the proper character, print it out in the same colour
            self.user_answer.config(fg="black")

        else: 
            # indicate to the user that they input the wrong character
            self.user_answer.config(fg="red")  
                                                                # code not properly running at regular index
                                                                # move index back one to properly read the input
        if self.user_answer.get() == self.game_sentence.cget('text')[:-1]:
            self.user_answer.config(fg="green")
            sentence = self.game_sentence.cget('text')
            # The user is now done the game
            # set the game running boolean to False so that the timer ceases
            self.game_started = False

    def exit_game(self):
        # Button that exits application
        pass


    def restart_game(self): #treated as c++ deconstructor, set values to intial value 
        self.game_sentence.config(text=random.choice(self.sentences))
        self.game_started = False
        self.speed.config(text="Typing Speed\n0.0 cps")
        self.user_answer.delete(0, END)
        self.time_elapsed = 0
        self.gametime.config(text=f"Time: {self.time_elapsed}")


    def timer(self):    
        while self.game_started == True:
            time.sleep(0.1) 
            self.time_elapsed += 0.1         
            char_length = float(len(self.user_answer.get()))
            #user_answer = self.user_answer
            cpm = char_length/(self.time_elapsed*60)
            self.speed.config(text=f"Typing Speed:\n{round(cpm*60, 3)} cps")
            self.gametime.config(text=f"Time:\n{round(self.time_elapsed, 3)} sec")


game()