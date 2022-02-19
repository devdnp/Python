# name, age = input("enter your comma separated name and age: ").split(",")
name = input("enter your name: ").lower()
age = int(input("enter your age: "))
if name[0] == "a" and age >= 10: #age>=10 and (name[0]='a' or name[0]='A')
    print("Go ahead!!")
else:
    print("You're not eligible buddy")