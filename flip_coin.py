import random
heads1=0
tails1=0
tails2=0
heads2=0
mixed=0
both_heads=0
both_tails=0
counter=(int)(input("How many flips would you like to do: "))
while counter > 0:
    counter -=1
    coin1=random.randint(0,1)
    coin2=random.randint(0,1)
    if coin1 == 0:
        heads1+=1
    else:
        tails1+=1
        
    if coin2 == 0:
        heads2+=1
    else:
        tails2+=1
    if coin1 == 0 and coin2 == 0:
        both_heads+=1
    elif coin1 == 1 and coin2 == 1:
        both_tails+=1
    elif coin1 != coin2:
        mixed+=1
    
print("here are your stats; ")
print("your first coin hit heads: ",heads1)
print("your first coin hit tails: ",tails1)
print("your second coin hit heads: ", heads2)
print("your second coin hit tails: ", tails2)
print("you landed two tails: ", both_tails)
print("you landed two heads: ", both_heads)
print("you landed mix coins: ", mixed)
