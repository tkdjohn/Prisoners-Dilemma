import random
import Constants 
import ComputerPlayer as cp
import HumanPlayer as hp

def Load_Settings():
    with open('README.md', 'r') as settings_file:
        rules = __load_rules_(settings_file)

    return (rules)

def __load_rules_(settings_file):
    rules = ''
    for line in settings_file:
        if line[0:5] == '-----':
            break;
        rules += line
    return rules

def Calc_Score(trigger_p_bonus, trigger_c_bonus):
    if (trigger_p_bonus):
        if Player.Bonus> 0 or Computer.Bonus > 0:
            Computer.Most_Recent_Choice = Constants.Choices.stay_silent
            Player.Set_Bonus(0)
            Computer.Set_Bonus(Computer.Bonus + 1)
        else:
            Computer.Most_Recent_Choice = Constants.Choices.confess
            Player.Set_Bonus(1)

    scores = Constants.Calc_Score(Player.Most_Recent_Choice, Computer.Most_Recent_Choice)
    bonuses = (Player.Bonus, Computer.Bonus)
    round_totals = [a + b for a, b in zip(scores, bonuses)]
    return round_totals[0], round_totals[1]

def Play():
    # Random number of rounds to help keep players guessing
    rounds_left = random.randint(5, 15)
    running_score = [0,0] 

    while (rounds_left > 0):
        trigger_p_bonus, trigger_c_bonus = Player.Choose(), Computer.Choose()
        p_round_score, c_round_score = Calc_Score(trigger_p_bonus, trigger_c_bonus)
        End_Round(p_round_score, c_round_score)
        rounds_left -= 1
    End_Game()

def End_Round(p_round_score, c_round_score):
    Computer.Update_Results(c_round_score, p_round_score, Player.Most_Recent_Choice)
    Player.Update_Results(p_round_score,c_round_score, Computer.Most_Recent_Choice)

def End_Game():
    Player.End_Game() 
    Computer.End_Game()

####### Initialize #######
random.seed()
Rules = Load_Settings()
play_again = 'r'

####### MAIN Loop ########
while True:
    Computer = cp.Computer_Player()
    Player = hp.Human_Player(Rules)

    if play_again == 'r':
        Player.Show_Rules()
    elif play_again == 'p':
        Play()
    else:
        break;

    print() 
    play_again = input('Choose play (p), show rules (r), or press any key to quit> ').lower()

