# for loop
# for i in range(2):  #range(1,11) to change the range
#     print(f"hello {i}")
# n = int(input("enter the last number: "))
# total = 0
# for i in range(1, n+1):
#     total+=i
# print(f"sum is {total}")
total = 0
num = input("enter the number: ")
for i in range(0, len(num)):
    total += int(num[i])
print(total)

name = input("enter your name: ")
temp =""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]} : {name.count(name[i])}")
        temp += name[i]