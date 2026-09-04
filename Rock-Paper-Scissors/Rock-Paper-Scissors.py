import random
us=0
cs=0
print('='*15,"WELCOME TO ROCK-PAPER-SCISSOR GAME",'='*15)
print()
print("Lets start the war either you will win or else me")
print()
for i in range(1,6):
    print()
    print('-'*15,f'ROUND{i}','-'*15)
    print()
    user=input("enter your choice (rock/paper/scissor): ")
    option=['rock','paper','scissor']
    comp=random.choice(option)
    print(f'computer choosed {comp}')

    if user==comp:
        print("Match is tie")

    elif user=='rock':
        if comp=='scissor':
            print("you won the match")
            us+=1
        else:
            print("computer won the match")
            cs+=1

    elif user=='paper':
        if comp=='rock':
            print("you won the match")
            us+=1
        else:
            print("computer won the match")
            cs+=1

    elif user=='scissor':
        if comp=='paper':
            print("you won the match")
            us+=1
        else:
            print("computer won the match")
            cs+=1
    print('-'*40)

print(f'User score is {us}',f'Computer score is {cs}',sep='\n')

if us>cs:
    print("User is winner")
elif us<cs:
    print("Computer is winner")
else:
    print("Match tied")
