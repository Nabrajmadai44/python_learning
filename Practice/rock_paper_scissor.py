import random
a= "rock","paper","scissors"  
i=1
 
y=0
z=0
while i==True:
    b=input("enter ur answer(rock paper or scissors)\n").strip().lower()
    c=random.choice(a)
    print(f"I choose {c}")
    if b==c:
        print("its a draw\n")
        print("the score is {z}vs{y}")
    elif c=="scissors" and b=="prper" or c=="rock" and b=="scissors" or c=="paper" and b=="rock":
        print("You Loose\n")
        z+=1
        y-=1
        print("the score is {z}vs{y}")
    elif b=="rock" and c=="scissors" or b=="scissors" and c=="paper" or b=="paper" and c=="rock":
        print("You Loose\n")
        y+=1
        z-=1
        print("the score is {z}vs{y}")
    else:
        print("Invalid Input\n")
    if z==10:
        print(f"You Loose,the score is {z}vs{y}")
    elif y==10:
        print("You Win")
    else:
        d=input("wanna continue?reply in y or n for yes or no\t").strip().lower()
        if d== "n"  :
            print("Thank you for playing, your score against the computer was  {z}:{y}")
            break
        else:
            continue
        