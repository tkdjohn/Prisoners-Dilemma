import random
random.seed()

PLAYER = 0
COMPUTER = 1

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

#TODO: populate the scoring matrix from the from the README
scoring_matrix = { ('c', 'c') : ( 0,  0),
                   ('c', 's') : ( 2, -5),
                   ('s', 'c') : (-5,  2),
                   ('s', 's') : (-2, -2) }

def Calc_Score(choice, bonus):
    scores = scoring_matrix[(choice[PLAYER], choice[COMPUTER])]
    return [a + b for a, b in zip(scores, bonus)]

def Get_Computer_Choice():
    #TODO: make the AI smarter - or at least harder to beat
    choice = random.choice(['c','s'])
    return choice

def Get_Player_Choice():
    prompt = 'You are seated in a dark room with a bright light shining in your face. A mentor looms over you, looking stern. ' \
        "The mentor's mouth does not move, yet you hear a commanding voice say, 'Your calssmate has already been interrogated. " \
        "Do you (c)onfess or will you stay (s)ilent?' "
    choice = input(prompt).lower()

    if choice == 'idkfa':
       return "bonus"

    # The mentors have little patience for stall tactics. If player doesn't respond 
    # appropriately, assume they choose not to confess.
    if choice not in ('c', 's'):
        print ("The mentor looks at you even more sternly and shakes their head.")
        print (f"The voice states flatly, 'You had your chance.'")
        choice = 's'
    
    return choice

def Report_Round(choice, score):
        print (f'You chose to {Get_Choice_Description(choice[0])}.')
        print (f'Your classmate chose to {Get_Choice_Description(choice[1])}.')
        print (f'=========== Scores ===========')
        print (f'          You: {score[PLAYER]}') 
        print (f'Your Opponent: {score[COMPUTER]}') 
        print ()

def Handle_Choices( bonus, bonus_activated,):
    choice = [Get_Player_Choice(),  Get_Computer_Choice()]

    if (choice[PLAYER] == 'bonus'):
        if (bonus_activated):
            print("The voice says, 'The only thing worse than a cheat is a greedy cheat.'")
            choice[PLAYER] = 's'
            choice[COMPUTER] = 'c'
            bonus[PLAYER] = 0
            bonus[COMPUTER] += 1
        else:
            bonus_activated = True
            print("The voice says, 'A wise choice.'")
            choice[PLAYER] = 'c'
            bonus[PLAYER] = 2
    return (choice, bonus, bonus_activated)

def Play():
    # Random number of rounds to help keep players guessing
    rounds_left = random.randint(5, 15)
    
    # Reset for a new round
    running_score = [0,0] 
    bonus_activated = False
    bonus = [0,0]

    while (rounds_left > 0):
        (choice, bonus, bonus_activated) = Handle_Choices(bonus, bonus_activated)

        score = Calc_Score(choice, bonus)

        # Shortcut to add the values in scores to running scores.
        running_score = [a + b for a, b in zip(running_score, score)]
        Report_Round(choice, running_score)
        rounds_left -= 1
    return running_score

def Report_Game(scores):
    win_lose = "You failed to outwit the computer!"
    if (scores[PLAYER] > scores[COMPUTER]):
        win_lose = "Congratulations, you win!"
    print (f'======= GAME OVER =======')
    print (f'          You: {scores[PLAYER]}') 
    print (f'Your Opponent: {scores[COMPUTER]}') 
    print (win_lose)

####### MAIN Loop ########
Print_Introduction()
play_again = 'a'
while True:
    if play_again == 'a':
        Report_Game(Play())
    elif play_again == 'r':
        Print_Introduction()
    else:
        break;

    print() 
    print()
    play_again = input('Choose (a)gain, (r)ules, or any key to quit? ').lower()
