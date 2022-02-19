name = input("enter your name: ").lower()
# total = 0/i = 1/while i<=num:total+=i/i+=1  total = 0/i = 0/while i<len(num):/total+=int(num[i])/i+=1/print(total)
i = 0
done =""
while i < len(name):
    if name[i] not in done:
        done += name[i]
        print(f" {name[i]} : {name.count(name[i])}")
    i+=1