from enum import Enum, unique

@unique
class Choices(Enum):
    confess = 'c'
    stay_silent = 's'
    
    @classmethod
    def list(cls):
        return list(cls)

    @classmethod
    def names_list(cls):
        return list(map(lambda c: c.name, cls))

    @classmethod
    def values_list(cls):
        return list(map(lambda c: c.value, cls))
    
    def __str__(self):    
        return str(self.name).replace('_', " ")

    def next(self):
        cls = self.__class__
        members = list(cls)
        index = members.index(self) + 1
        if index >= len(members):
            index = 0
        return members[index]

    def prev(self):
        cls = self.__class__
        members = list(cls)
        index = members.index(self) - 1
        if index < 0:
            index = len(members) - 1
        return members[index]

#TODO: populate the scoring matrix from the from the README using regular expresions! 
SCORING_MATRIX = { 
    (Choices.confess, Choices.confess)          : ( 2,  2),
    (Choices.confess, Choices.stay_silent)      : (-3,  3),
    (Choices.stay_silent, Choices.confess)      : ( 3, -3),
    (Choices.stay_silent, Choices.stay_silent)  : (-1, -1) }

def Calc_Score(p_choice, c_choice):
    return SCORING_MATRIX[(p_choice, c_choice)]
    