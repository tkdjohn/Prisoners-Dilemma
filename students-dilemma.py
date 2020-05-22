import random
random.seed()

def Print_Introduction():
    readme = ''
    with open('README.md', 'r') as f:
        for line in f:
            if line[0:5] == '-----':
                break;
            readme += line
    print (readme)

#TODO: populate the scores from the from the README
## possibly change all the Y N stuff to actual words? Or at least C and S for Confess and Stay Silent
scoring_matrix = { ('c', 'c') : ( 0,  0),
                   ('c', 's') : ( 2, -5),
                   ('s', 'c') : (-5,  2),
                   ('s', 's') : (-2, -2)}

def Calc_Result(player_choice, computer_choice, player_bonus, computer_bonus = 0):
    return scoring_matrix[(player_choice + player_bonus, computer_choice + computer_bonus)]

def Get_Computer_Choice():
    #TODO: make the AI smarter - or at least harder to beat
    choice = random.choice(['c','s'])
    if (choice == 'c'):
        description = "confess."
    else:
        description = "stay silent."
    return (choice, description)

def Get_Player_Choice():
    prompt = 'You are seated in a dark room with a bright light shining in your face. A mentor looms over you, looking stern. ' \
        "The mentor's mouth does not move, yet you hear a commanding voice say, 'Your calssmate has already been interrogated. " \
        "Do you (c)onfess or will you stay (s)ilent?' "
    player_choice = input(prompt).lower()

    if player_choice == 'IDKFA':
       return "bonus"

    # The mentors have little patience for stall tactics. If player doesn't respond 
    # appropriately, assume they choose not to confess.
    if player_choice not in ('c', 's'):
        print ("The mentor looks at you even more sternly, shakes their head.")
        print (f"The voice states flatly, 'You had your chance to confess.'")
        player_choice = 's'
    
    return player_choice

def Play():
    # Random number of rounds to help keep players guessing
    rounds_left = random.randint(5, 15)
    
    # Reset for a new round
    scores = [0,0] 
    cheat_already_activated = False
    bonus = 0

    while (rounds_left > 0):
        (computer_choice, computer_choice_description) = Get_Computer_Choice()
        player_choice = Get_Player_Choice()
        
        # Only allow the player to get the cheat bonus once.
        if (player_choice == 'bonus'):
            if (cheat_already_activated):
                print("The voice says, 'The only thing worse than a cheat is a greedy cheat.'")
                (player_choice, computer_choice) = ('s', 'c')
                bonus = 0
            else:
                print("The voice says, 'A wise choice.'")
                (player_choice, computer_choice) = ('c', 's')
                cheat_already_activated = True
                # TODO: get max score from the scoring matrix
                bonus = 2 * rounds_left

        print (f'Your classmate chose to {computer_choice_description}')
        res = list(Calc_Result(player_choice, computer_choice, bonus))
        scores = [a + b for a, b in zip(scores, res)]
        rounds_left -= 1

        print()
        print (f"Player One: {scores[0]}  Computer: {scores[1]}")

####### MAIN Loop ########
Print_Introduction()
play_again = 'a'
while True:
    if play_again == 'a':
        Play()
    elif play_again == 'r':
        Print_Introduction()
    else:
        break;

    print() 
    print()
    play_again = input('Choose (a)gain, (r)ules, or any key to quit? ').lower()
