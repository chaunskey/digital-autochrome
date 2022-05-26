import random

go = True
print("generating numbers... enter 'stop' to quit")
while go == True:
    print(random.random())
    stop = input()
    if stop == "stop":
        go = False