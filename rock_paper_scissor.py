import random
def printImg(u):

    rock= '''
        _______
    ---'   ____)
        (_____)
        (_____)
        (_____)
    ---.__(__)
    '''

    paper = '''
            _______
        ---'   ____)___
                _______)
                _______)
                _______)
        ---.__________)
        '''

    scissors = '''
            _____
        ---'   __)______
                ________)
            ____________)
            (____)
        ---.(____)
        '''
    if u=="rock":
        return(rock)
    elif u == "paper":
        return(paper)
    elif u == "scissors":
        return(scissors)
    


user_action = input("Enter a choice (rock, paper, scissors): ")

possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)

print(f"\nYou chose {printImg(user_action)} \n Computer chose {printImg(computer_action)}\n")

if user_action == computer_action:
    print(f"Both players selected {user_action}. It's a tie!")
elif user_action == "rock":
    if computer_action == "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")

#0 = R
#1 = P
#2 = S
#R<P ,R>S
#P<S, P>R
#S<R, S>P


#print(computer)

    




