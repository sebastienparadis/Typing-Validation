import tkinter as run
from tkinter import *
import random
import time


""" origin = run.Tk()
origin.title('Speed Typing Test')
origin.geometry("1000x1000")
mycanvas = run.Canvas(origin, height=1000, width=1000, bg='dark grey')
myframe = run.Frame(origin, bg="white")
myframe.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)
sentences = open("sentences.txt", "r").read().split("|")

current_sentence = random.choice(sentences)

game_sentence = run.Label(origin, text=current_sentence)

game_sentence.place(x=475, y=200)

user_answer = run.Text(origin, height=1, width=50)

user_answer.pack()
user_answer.place(x=475, y=350)


button that closes application
exit = run.Button(origin, text="Exit Game", fg="black", bg="black", height=3, width=10, command=origin.destroy)
exit.place(x=450, y=850)
origin.mainloop() """



# Class to do the above functions and more for later efficiency

class test:
    def __init__(self):
        
        # Set basic outline of application
        self.origin = run.Tk()
        self.origin.title('Speed Typing Test')
        
        self.mycanvas = run.Canvas(self.origin, height=1000, width=1000, bg='dark grey')
       
        self.myframe = run.Frame(self.origin, bg='white')
        self.myframe.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)
        
        # Sentences used for games stored in .txt file, each sentence is seperated by \n
        self.sentences = open('sentences.txt', 'r').read.split('\n')
        
        self.current_sentence = random.choice(self.sentences)
        
        self.game_sentence = run.Label(self.myframe, text=self.current_sentence)
        self.game_sentence.place(x=475, y=200)
        
        self.user_answer = run.Text(self.myframe, width=50, font =("Times New Roman", 20))
        self.user_answer.pack()
        self.user_answer.place(x=475, y=350)

        # Timer starts when user presses first character
        # To be written
        self.time_elapsed = 0

        # Button that exits application
        self.exit = run.Button(self.myframe, text="Exit Game", fg="black", bg="black", height=3, width=10, command=self.origin.destroy)
        self.exit.place(x=450, y=850)

        # Button that restarts application                                                                          #create a restart_game function
        self.restart = run.Button(self.myframe, text="Try Again?", fg="black", bg="black", height=3, width=20, command=self.restart_game)
        self.restart.place(x=350, y=600)

        # Speed indicator
        self.speed = run.Label(self.myframe, text="Typing Speed: 0.0 WPM", fg="black", bg="black", height=3, width=20)
        self.speed.place(x=250, y=600)
        
        # make frame responsive and pack
        self.myframe.pack(expand=True)

        self.origin.mainloop()

        # Set the base value of the game_start to False
        # To be used as a boolean for timer function and other
        game_start = False


        def play(self):
            # minutes = 0
            # seconds = 0
            # milliseconds = 0
            while self.game_start == True:
                time.sleep(0.01) 
                self.time_elapsed += 0.01
                # milliseconds+=1
                # if milliseconds == 100
                #     seconds+=1
                #     milliseconds==1000
                # if seconds == 60:
                #     minutes+=1
                #     seconds==0
                #     milliseconds==0
            
            word_length = self.user_answer.split()
            words_in_sentence = len(word_length)
            wpm = word_length 
               

        def restart_game(self):


        def timer(self):    
            


