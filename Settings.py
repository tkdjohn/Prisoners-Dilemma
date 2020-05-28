from enum import Enum, unique
import re

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

#set default scoring matrix
__scoring_matrix_ = { 
    (Choices.confess, Choices.confess)          : ( 2,  2),
    (Choices.confess, Choices.stay_silent)      : (-3,  3),
    (Choices.stay_silent, Choices.confess)      : ( 3, -3),
    (Choices.stay_silent, Choices.stay_silent)  : (-1, -1) 
}

Rules = 'The rules have not been loaded!!'

def Get_Score(p_choice, c_choice):
    return __scoring_matrix_[(p_choice, c_choice)]

def Load():
    global Rules
    with open('README.md', 'r') as settings_file:
        Rules = __load_rules_(settings_file)
    __parse_rules(Rules)

def __parse_rules(rules):
    global __scoring_matrix_
    # get the defaults 
    both_confess_points = __scoring_matrix_[Choices.confess, Choices.confess][0]
    one_confess_points, one_stay_silent_points = __scoring_matrix_[Choices.confess, Choices.stay_silent]
    both_stay_silent_points = __scoring_matrix_[Choices.stay_silent, Choices.stay_silent][0]

    x = re.compile('(both|one) (confess(e?s?)|stay(s?) silent) \((-?\d*) points\)')
    y = x.findall(Rules)
    for z in y:
        both_confess_points =  z[4] if z[0:2] == ('both', 'confess')  else both_confess_points
        one_confess_points =  z[4] if z[0:2] == ('one', 'confesses')  else one_confess_points
        one_stay_silent_points = z[4] if z[0:2] == ('one', 'stays silent')  else one_stay_silent_points
        both_stay_silent_points = z[4] if z[0:2] == ('both', 'stay silent')  else both_stay_silent_points
    __scoring_matrix_ = { 
        (Choices.confess, Choices.confess)          : (both_confess_points, both_confess_points),
        (Choices.confess, Choices.stay_silent)      : (one_confess_points,  one_stay_silent_points),
        (Choices.stay_silent, Choices.confess)      : (one_stay_silent_points,  one_confess_points),
        (Choices.stay_silent, Choices.stay_silent)  : (both_stay_silent_points, both_stay_silent_points) 
    }
    print(__scoring_matrix_)


def __load_rules_(settings_file):
    rules = ''
    for line in settings_file:
        if line[0:5] == '-----':
            break;
        rules += line
    return rules