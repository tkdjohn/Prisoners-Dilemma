import random

class Computer_Player:
    '''Represents the computer player.'''
  
    Runing_Score = 0
    
    def Choose(self, available_choices):
        return self.__choose_method_(available_choices)

    def Update_Results(self, choices, round_scores):
        self.__opponent_previous_choice_ = choices[self.Opponent_Player_Number]
        self.Runing_Score += round_scores[self.Player_Number]
        
    def __init__(self, player_number, opponent_player_number):
        random.seed()
        self.__choose_method_ = self.__Tit_for_That_
        #self.__choose_method_ = self.__Random_
        self.Player_Number = player_number
        self.Opponent_Player_Number = opponent_player_number

    __opponent_previous_choice_ = None

    def __Random_(self, available_choices):
        return random.choice(available_choices)
    
    def __Tit_for_That_(self, available_choices):
        if self.__opponent_previous_choice_ is None:
            self.__opponent_previous_choice_ = available_choices[0]
        return self.__opponent_previous_choice_
