# name = input("type your name")
# print("hello " + name )
#input will be always taken in string
# age = input("what is your age")
# print("i don't care you are " + age)
# number_one = int(input("first")) #input("first") srting
# number_two = int(input("second")) #input("second") string
# total = number_one + number_two
# print("total is " + total) error
# print("total is " + str(total))
name, age = input("enter your name and age ").split() #split(",") fir splitting inputs now , can be used
print(name)
print(age)