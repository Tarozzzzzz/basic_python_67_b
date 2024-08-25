"""
#
# Part: Python while Loop
#
"""
print("Python while Loop")
i = 1
while i < 5:
    print("i = ", i)
    i +=1 # i = i + i
    print(" ")
    
    i = 1
    while i < 5:
        print("i = ", i)
        if i == 3:
            break # break = หยุด
        i += 1 # i = i + 1
        print(" ")
        
        
        # i = 1
        # while i < 5:
        # print("i = ", i)
        # if i == 3:
        # continue # continue = ไปต่อ
        # i+=1 # i = i + 1
        # else:
        # # print(" ")
        
        i = 1
        while i < 5:
            print("i =", i)
        else:
            print("Game over!")
        print("End while Loop\n")
        
        
        
"""
#
# Part: Python for Loop
#
"""
print("Python for Loop")
fruits = ["apple", "banana", "coconut"]
for fruit in fruits:
    print("fruit : ", fruit)
    
fruits = ["apple", "banana", "coconut"]
for fruit in fruits:
    print("fruit : ", fruit)
    if fruit == "banana":
        break

fruits = ["apple", "banana", "coconut"]
for fruit in fruits:
    if fruit == "banana":
        break
    print("fruit : ", fruit)
    
fruits = ["apple", "banana", "coconut"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print("fruit : ", fruit)

    for x in range(len(fruits)):
        print("Number: ", x)
        
    for x in range(5):
        print("Number: ", x)
    else:
        print("Game Over!\n")
        
    adjs = ["red", "blue", "green"]
    fruits = ["apple", "banana", "coconut"]
    for adj in adjs:
        for fruit in fruits:
            print("Fruit : " + " " + adj + " " + fruit)
            # print("Fruit : "," ",adj," ", fruit)
            
    print("END for Loop\n")