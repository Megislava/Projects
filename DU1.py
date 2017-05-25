'''1. fce expession vypisuje hodnotu zadaného výrazu tj. 1. je 8, 2. je 6 atd (8, 6, 6, 8, 12, 18,...)
a vypisuje je od nuly do zadaného čísla'''

def expression(x):
    y = 0
    while y <= x:
        exp = y ** 2 - 5 * y + 12
        print (exp)
        y += 1
        

expression(6)

        
'''2. Fce triangle vypisuje n řádků hvězdiček zarovnaných napravo, první hvězdička má n mezer
i-tý řádek má i hvězdiček'''

def triangle (n):
    for i in range(n):
        for u in range((n - i) - 1):
            print (" ", end = "")
        for z in range(i + 1):
            print ("*", end = "")
        print ("")

triangle(4)
    

'''3. Import z turtlovské knihovny všechno, fce polygon kde v argumentu je n značka pro vrcholy
n-úhelníku a size značka pro velikost hrany n-úhelníku v pixelech'''

from turtle import *

def polygon(n, size):
    for i in range(n):
        forward(size)
        left(360/n)

polygon (9, 100)


'''4. Popis prográmku: Fce arrow kde v argumentu se udává
opakování a výška trojuhelníku/počet hvězdiček v posledním řádku'''

def arrow(high, repetitions):
    for i in range (repetitions):
        for i in range(high):
            for u in range((high - i) - 1):
                print (" ", end = "")
            for z in range(i + 1):
                print ("*", end = "")
                if z != (i + 1) - 1:
                    print (".", end = "")
            print ("")

arrow(4, 2)


'''5. Fce print_alpha na začátku dostane písmeno a v turtlovské grafice ho vykreslí'''


def print_alpha(ch):
    if ch == "A":
        #posunutí písmene do adekvátní dálky
        up()
        goto(-200, 0)
        down()
        #otočení a napsání A
        left(60)
        forward(100)
        right(60)
        forward(20)
        goto(-115, 0)
        up()
        goto(-180, 35)
        down()
        forward(60)
    
    elif ch == "B":
        up()
        goto(-100, 0)
        down()
        left(90)
        forward(90)
        right(270)
        circle(45/2, -180)
        right(180)
        circle(45/2, -180)

    elif ch == "C":
        up()
        goto(-40, 0)
        down()
        circle(50, -180)
    
    elif ch == "D":
        up()
        goto(50, 0)
        down()
        circle(50, 180)
        goto(50, 0)

    elif ch == "E":
        home()
        
        left(90)
        forward(90)
        right(90)
        forward(60)
        
        up()
        home()
        down()
        
        forward(60)
        
        up()
        goto(0, 45)
        down()
        
        forward(60)
    
    elif ch == "F":
        up()
        goto(75, 0)
        down()
        
        left(90)
        forward(90)
        right(90)
        forward(60)
        up()
        goto(75, 50)
        down()
        forward(60)
    else:
        print("""Zadej písmeno z množiny {"A", "B", "C", "D", "E", "F"}""")
    
print_alpha("A")

   
