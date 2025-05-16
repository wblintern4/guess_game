import random
def guessGame():
    user_score=0
    computer_score=0
    attempt=0
    while attempt<5:
        computer_chosen=random.randint(0,5)
        user_chosen=int(input("enter:"))
        if user_chosen==computer_chosen:
            user_score+=1
        else:
            computer_score+=1
        attempt+=1
        text=f'User Score is {user_score} and Computer Score is {computer_score} And Computer Chosen is {computer_chosen}'
        print(text)
guessGame()