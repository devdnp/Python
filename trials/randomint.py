import random
hit = random.randint(1,100)
# hit = 2
trial = int(input("enter your number: "))
chance = 1
Game_over = False
while not Game_over: #while True
    if trial==hit: #input can be here
        print(f"You got it buddy in {chance} times!! ")
        Game_over = True #break
    else:
        if trial<hit:
            print("Go a little up")
        else:
            print("go a bit slower") #continue
        trial=int(input("try again enter the number: "))
        chance+=1