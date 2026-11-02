namn = input("Vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")

import random as rand
tal = rand.randint(1,10)
for i in range(3):
    while i < 3:
        gissning = int(input("Gissa ett tal mellan 1 och 10: "))
        if gissning == tal:
            print("Helt rätt!!")
            break
        elif gissning != tal:
            print("Det var fel")
        break
    if i == 2:
        print("Slut på försök")
        break



        
