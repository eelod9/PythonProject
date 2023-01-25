import art
import random
from game_data import data

#print(art.logo)
#print(data[0]['name'])
def compareAB(A,B, response):
    #Assuming no two artist have the same followers
    if(A>B):
        if(response =='A'): #winner
            return True
        else:
            return False
    elif(A<B):
        if(response =='B'): #winner
            return True
        else:
            return False
        

print(art.logo)
win = True
score = 0
while(win):
    A,B = random.sample(data,2)
    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.  {A['follower_count']}")
    


    print(art.vs)
    print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}.  {B['follower_count']} ")
    response = input("Who has more followers? Type 'A' or 'B':")
    A_followers = A['follower_count']
    B_followers = B['follower_count']
    win = compareAB(A_followers, B_followers, response)
    if(win):
        score +=1
        print(f"Correct! Current Score: {score}")
    else:
        print(f"Wrong! Final Score: {score}")
    
    print(chr(27) + "[2J") #clear screen
        
    



