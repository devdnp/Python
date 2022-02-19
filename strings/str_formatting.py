# name = "vipul"
# age = 25
# print("hello {} your age is {}".format(name, age)) #python 3 arithmetic operations allowed in format
# print(f"hello {name} your age is {age}") #python 3.6 same operations allowed

#one = int(input("first number"))
#two = int(input("second number"))
#three = int(input("third number"))
# avg = (one + two + three)/3
# print("avg is " + str(avg))

# one, two, three = input("enter one, two and three").split(",")
# avg = (one + two + three)/3
# print(f"avg is:  {(int(one) + int(two) + int(three))/3}")

#string indexing : position(index number)
# language = "Python"
# print(language[3])  print(language[start argument:stop argument-1:step]) chhalaang is step+/- frwrd/revrs
# print("language"[0:5]) #--> slicing/ selecting sub sequence
# print(language[-1])
name = input("enter your name: ")
print(f"reverse of your name is: {name[::-1]}")