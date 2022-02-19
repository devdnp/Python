import random
hit = random.randint(1,100)
trial =int(input("enter the number: "))
chance = 1
over = False
while True:
    if trial == hit:
        print(f"you got it!! In {chance} times.")
        break
    else :
        if trial<hit:
            print("go a bit up buddy")
        else:
            print("go a little slower")
        trial=int(input("Try again buddy, enter the number: "))
        chance+=1