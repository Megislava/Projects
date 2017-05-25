#import knihovny
import random

#funkce na hraní hry

def game(length):
    #pozice v domecku
    pose = 0
    tah = 0
    #dokud nepadne sest a potom nasadím na 1.policko
    while (pose == 0):
        dice = random.randint(1, 6)
        if (dice == 6):
            pose += 1
    while (pose != length) and (pose < length):
        dice = random.randint(1, 6)
        if (dice + pose) > length:
            continue
        total = 0
        if dice < 6:
            total += dice
        else:
            while (dice == 6):
                total += dice
                dice = random.randint(1, 6)
                if (total + pose) > length:
                    break
        pose += total
        #graficky znázornim
        print (total, end = "")
        print (" Start:", end = "")
        for i in range(length):
            if i == (pose):
                print ("*", end = "")
            else:
                print (".", end = "")
        print (":Finish")
        tah += 1
    return tah
    

def average(count, length):
    num = 0
    for i in range(1, count):
        x = game(length)
        num += x
    return (num/ count)


def statistics(count, maxLength):
    length = 0
    while (length == maxLength):
        y = average(count, length) 
        length += 1
        print (i, y)
        


print(statistics(10, 40))


'''
prumer poctu tahu se zvyšuje v závislosti na délce pole, nepodařilo se mi
vytisknout poslední fci a tak je to jenom podle druhé když jsem nechala
vzrůstat délku pole
'''


