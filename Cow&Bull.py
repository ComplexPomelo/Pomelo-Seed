import random
print("This Cow & Bull")
o = False
number = []
n = random.randint(0,9)

for i in range(4):
    n = random.randint(0,9)
    number.append(str(n))


while o != True:
    print(number)
    Try = input("How many cows are there:")
    cow = 0
    bull = 0
    
    for b in range(4):
        if number[b] == Try[b]:
            cow = cow + 1

    for i in range(4):
        for c in range(4):
            if number[i] == Try[c] and number[i] != Try[i]:
                bull = bull + 1

    print(number)
    print("There are",cow,"cows, and",bull,"bulls.")

    if cow == 4:
        o = True
print("OK, you got it.")
