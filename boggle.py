import tkinter as tki
import game_new
from PIL import Image,ImageTk
class myGame:
    def __init__(self,parent):
        self.parent = parent
        self.parent.geometry('600x600')
        img = ImageTk.PhotoImage(Image.open("BOGGLE-updraft-pre-smush-original.jpg"))
        self.panel = tki.Label(self.parent, image=img)
        self.panel.pack(side="bottom", fill="both", expand="yes")
        self.start_button = tki.Button(self.panel, text="Start",font = ("Coruer",10),command=lambda :self.start_clicked())
        self.start_button.pack()
        self.buttons_list = []
        self.score = 0
        self.remaining = 0
        self.game_frame = tki.Frame(self.parent, width=500, height=100)
        self.label = tki.Label(self.game_frame, text="", font=("Courier", 15))
        self.conform_button = tki.Button(self.game_frame, text="check",command = lambda :self.check_clicked())
        self.score_label = tki.Label(self.game_frame, text=str(self.score), font=("Courier", 15))
        self.board_frame = tki.Frame(self.parent, width=500, height=500)
        self.words_frame = tki.Frame(self.parent,width = 150,height=500)
        self.words_label = tki.Label(self.words_frame,text = "correct words",font=("Courier", 10))
        self.game_TUI = game_new.GameTUI()
        self.label_lst=[]

    def start_clicked(self):
        '''
        in this function start the game and remove the start game button
        '''
        self.start_game()
        self.start_button.forget()

    def check_start_game(self):
        '''
        in this function we check if the game is over and starting the game once again
        '''
        if self.label["text"] == "time's up!":
            self.play_again()
            self.start_clicked()

    def new_game(self):
        '''
        starting new game
        '''
        self.start_game()

    def countdown(self, remaining=None):
        '''
        in this function we start the timer for the game
        '''
        if remaining is not None:
            self.remaining = remaining
        #if the time is over
        if self.remaining <= 0:
            #change the text and give the player an option to start a new game
            self.label.configure(text="time's up!")
            self.game_TUI.end_game()
            self.start_button = tki.Button(self.parent, text="new game", font=("Coruer", 10),
                                           command=lambda: self.check_start_game())
            self.start_button.pack()
        else:
            #if the time is not over
            mins, secs = divmod(self.remaining, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            self.label.configure(text=timeformat)
            self.remaining = self.remaining - 1
            self.parent.after(1000, self.countdown)


    def start_game(self):
        '''
        in this function we start the game
        '''
        #starting the timer!
        self.countdown(10)
        #adding the board
        self.parent.geometry("600x600")
        self.game_frame.place(x=200, y=50)
        self.conform_button.grid(row = 0, column = 0)
        self.score_label.grid(row=0, column=3, padx=(30, 10))
        self.label.grid(row = 0, column = 2, padx = (30,10))
        self.board_frame.place(x=100, y=150)
        self.words_frame.place(x=0,y=0)
        self.words_label.pack()
        #adding the buttons
        lis =  self.game_TUI.get_board()
        for i in range(len(lis)):
            for j in range(len(lis[i])):
                b = tki.Button(self.board_frame, text=str(lis[i][j]), width=15, height=5)
                b["command"] = self.onClick(i, j,b)
                b.grid(row=i, column=j,padx = (5,0),pady = (5,0))
                self.buttons_list.append(b)



    def onClick(self,i, j,button):
        '''
        in this function we update the button if the click is legal
        '''
        def roe():
            check=self.game_TUI.get_input(i,j)
            #changing the color of the button
            if check:
                button["bg"] = "gold"
        return roe

    def check_clicked(self):
        '''
        in this function after the user decides to check his word, we check if the word is correct
        and update the score then reset the board
        '''
        if self.game_TUI.check_valid_choise():
            word = self.game_TUI.get_chosen_string()
            #updating the score
            self.score += len(word) ** 2
            self.score_label["text"] = str(self.score)
            self.game_TUI.set_correct_words_list(word)
            words_label = tki.Label(self.words_frame, text=word, font=("Courier", 10))
            words_label.pack()
            self.label_lst.append(words_label)
            #reseting the board
        self.reset_board()


    def play_again(self):
        '''
        in this function we reset the window to a new game
        '''
        self.score = 0
        self.score_label["text"] = str(self.score)
        self.game_TUI.new_game()
        self.words_label.configure(text="correct words")
        for lab in self.label_lst:
            lab.forget()

    def reset_board(self):
        '''
        resetting the window after the player checks a word
        '''
        self.game_TUI.check_reset()
        #returning the background color to original color
        for b in self.buttons_list:
            b["bg"] = "SystemButtonFace"

if __name__ == '__main__':
    root = tki.Tk()
    game = myGame(root)
    tki.mainloop()

