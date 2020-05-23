import random
import ComputerPlayer as cp
import HumanPlayer as hp
SECRET_BONUS_WORD = 'idkfa'
H_PLR_NUM = 0
C_PLR_NUM = 1

random.seed()

#TODO: populate the scoring matrix from the from the README
# and do this with regular expresions! 
Scoring_Matrix = { ('c', 'c') : ( 0,  0),
                   ('c', 's') : ( 2, -5),
                   ('s', 'c') : (-5,  2),
                   ('s', 's') : (-2, -2) }

Computer = cp.Computer_Player(C_PLR_NUM, H_PLR_NUM)
Player1 = hp.Human_Player()

def Print_Introduction():
    readme = ''
    with open('README.md', 'r') as f:
        for line in f:
            if line[0:5] == '-----':
                break;
            readme += line
    print (readme)

def Get_Choice_Description(choice):
    if (choice == 'c'):
        return "confess"
    elif (choice == 'b'):
        return "get a bonus"
    else:
        return "stay silent"

def Calc_Score(choice, bonus):
    # Use 0 an 1 instead of H_PLR_NUM and C_PLR_NUM here because 
    # this function should return the scores in the same order
    # as the choices, without need to know which is which.
    scores = Scoring_Matrix[(choice[0], choice[1])]
    return [a + b for a, b in zip(scores, bonus)]

def Get_Player_Choice():
    prompt = 'You are seated in a dark room with a bright light shining in your face. A mentor looms over you, looking stern. ' \
        "The mentor's mouth does not move, yet you hear a commanding voice say, 'Your calssmate has already been interrogated. " \
        "Do you (c)onfess or will you stay (s)ilent?' "
    choice = input(prompt).lower()

    if choice == SECRET_BONUS_WORD:
       return "bonus"

    # The mentors have little patience for stall tactics. If player doesn't respond 
    # appropriately, assume they choose not to confess.
    if choice not in ('c', 's'):
        print ("The mentor looks at you even more sternly and shakes their head.")
        print (f"The voice states flatly, 'Not choosing is still choosing. You had your chance.'")
        choice = 's'
    
    return choice

def Report_Round(choice, score):
    Computer.Update_Results(choice, score)
    #TODO: move to Player.Update_Results
    print (f'You chose to {Get_Choice_Description(choice[0])}.')
    print (f'Your classmate chose to {Get_Choice_Description(choice[1])}.')
    print (f'=========== Scores ===========')
    print (f'          You: {score[H_PLR_NUM]}') 
    print (f'Your Opponent: {score[C_PLR_NUM]}') 
    print ()

def Get_Choices(bonus):
    # Assign individual choices based on the index set in the constants. This way
    # we don't have to keep track of which index is the player and which is the computer.
    choice = ['', '']
    choice[H_PLR_NUM] = Get_Player_Choice()
    #TODO: s and c here should be pulled from config data
    choice[C_PLR_NUM] = Computer.Choose(['s','c'])

    if (choice[H_PLR_NUM] == 'bonus'):
        if bonus[H_PLR_NUM] > 0 or bonus[C_PLR_NUM] > 0:
            print("The voice says, 'The only thing worse than a cheat is a greedy cheat.'")
            choice[H_PLR_NUM] = 's'
            choice[C_PLR_NUM] = 'c'
            bonus[H_PLR_NUM] = 0
            bonus[C_PLR_NUM] += 1
        else:
            print("The voice says, 'A full written confession, a wise choice.'")
            choice[H_PLR_NUM] = 'c'
            bonus[H_PLR_NUM] = 2

    return (choice, bonus)

def Play():
    # Random number of rounds to help keep players guessing
    rounds_left = random.randint(5, 15)
    running_score = [0,0] 
    bonuses = [0,0]

    while (rounds_left > 0):
        (choices, bonuses) = Get_Choices(bonuses)
        round_score = Calc_Score(choices, bonuses)

        # Shortcut to add the values in scores to running scores.
        running_score = [a + b for a, b in zip(running_score, round_score)]
        Report_Round(choices, running_score)
        rounds_left -= 1

    return running_score

def Report_Game(scores):
    win_lose = "You failed to outwit the computer!"
    if (scores[H_PLR_NUM] > scores[C_PLR_NUM]):
        win_lose = "Congratulations, you win!"
    print (f'======= GAME OVER =======')
    print (f'          You: {scores[H_PLR_NUM]}') 
    print (f'Your Opponent: {scores[C_PLR_NUM]}') 
    print (win_lose)

####### MAIN Loop ########
Print_Introduction()
play_again = 'a'
while True:
    if play_again == 'a':
        results = Play()
        Report_Game(results)
    elif play_again == 'r':
        Print_Introduction()
    else:
        break;

    print() 
    print()
    play_again = input('Choose (a)gain, (r)ules, or any key to quit? ').lower()
