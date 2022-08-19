import boggle_board_randomizer
from copy import deepcopy

class GameTUI:
    def __init__(self):
        self.BOARD = boggle_board_randomizer.randomize_board()
        self.correct_words_list = []
        self.tempBoard = deepcopy(self.BOARD)
        self.chosen_string = ""
        self.coord_list = []
        self.all_words = convert_file_to_list("boggle_dict.txt")


    def get_input(self,row,col):
            ''' no need to check for input validity since you control it
            only need to check if the cell isn't None so it wasn't chosen before'''
            if self.check_valid_click(row,col):
                self.chosen_string += self.tempBoard[row][col]
                self.coord_list.append((row,col))
                self.tempBoard[row][col] = ""
                return True

    def set_correct_words_list(self,word):
        '''
        update the correct words list
        '''
        self.correct_words_list.append(word)

    def check_valid_choise(self):
        '''
        check if the word the player chooses is in the list
        '''
        return (self.chosen_string in self.all_words) and (self.chosen_string not in self.correct_words_list)

    def check_valid_click(self,row,col):
        '''
        check if the player is click is valid
        '''
        if len(self.coord_list) == 0:
            return True
        #checking the place of the click
        if abs(self.coord_list[-1][0] - row) > 1 or abs(self.coord_list[-1][1] - col) > 1 or self.tempBoard[row][col] == "":
            return False
        return True

    def new_game(self):
        '''
        in this function we set the all the lists to empty and set a new board for a new game
        '''
        self.BOARD = boggle_board_randomizer.randomize_board()
        self.tempBoard = deepcopy(self.BOARD)
        self.correct_words_list = []
        self.coord_list = []
        self.chosen_string = ""

    def end_game(self):
        '''
        in this function we make sure that the game cant continue after the time is up
        '''
        self.correct_words_list = self.all_words

    def check_reset(self):
        '''
        resetting the game board after a check button click
        '''
        self.tempBoard = deepcopy(self.BOARD)
        self.coord_list = []
        self.chosen_string = ""

    def get_board(self):
        '''
        returning the game board
        '''
        return self.tempBoard

    def get_chosen_string(self):
        '''
        return the word the player chose
        '''
        return self.chosen_string


def convert_file_to_list(file):
    '''
    this function opens a file to read an return all the lines in a listS
    '''
    words_list=[]
    with open(file,"r") as f:
        for line in f:
            #adding the file without the last index"\n"
            words_list.append(line[:-1])
    return words_list
