import random

class Computer:
    '''Represents the computer player.'''
  
    def Choose(self, available_choices):
        return self.__choice_method_(self), available_choices

    def Update_Results(self, choices, round_scores):
        self.__opponent_previous_choice_ = choices[self.Opponent_Player_Number]
        self.Runing_Score = round_scores(self.Player_Number)
        
    def __init__(self, player_number, opponent_player_number):
        random.seed()
        self.__choice_method_ = self.__Random_(self)
        self.Player_Number = player_number
        self.Opponent_Player_Number = opponent_player_number

    def __Random_(self, available_choices):
        return random.choice(available_choices)
    
    def __Tit_for_That_(self, available_choices):
        return self.__opponent_previous_choice_
