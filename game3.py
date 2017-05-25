
from random import randint

#trida item pro reprezentaci predmetu
class Item:
    def __init__(self, name, description, value, weight):
        self.name = name
        self.description = description
        self.value = value
        self.weight = weight

#metoda vypíše popis predmetu
    def describe(self):
        print(self.name + ": " + self.description + " (cena: " +\
                str(self.value) + ", vaha: " + str(self.weight) + ")")
        
#to same jako item ale s weapon
class Weapon:
    def __init__(self, name, description, attack, defence):
        self.name = name
        self.description = description
        self.attack = attack
        self.defence = defence

    def describe(self):
        print(self.name + ": " + self.description + " (utok: " +\
                str(self.attack) + ", obrana: " + str(self.defence) + ")")

#trida monster
class Monster:
    def __init__(self, name, attack, defence, vigilance, health):
        self.name = name
        self.attack = attack
        self.defence = defence
        self.sleeping = True
        self.vigilance = vigilance
        self.health = health
#metoda na udání jak tvrdě spí (dvacetistěnka :D)       
    def react_to_noise(self):
        if randint(1, 20) <= self.vigilance:
            self.sleeping = False

#trida player 
class Player:
    def __init__(self, name):
        self.name = name
        self.max_health = randint (150, 200)
        self.health = self.max_health
        self.capacity = randint (150, 200)
        self.weapon = Weapon("dyka", "Stara rezava dyka. Dost tupa.", 5, 2)
        self.bag = {}

# nadledujici metody rest (prida zdravi), dat do batohu(dokud neprekroci kapacitu)
    def rest(self):
        self.health = min(self.health + 50, self.max_health)

    def add_to_bag(self, item):
        if item.weight <= self.capacity:
            self.bag[item.name] = item
            self.capacity -= item.weight
            return True
        else:
            return False

# vzit z batohu (vezme předmet s xy nazvem), vzit zbran (zmena weponu)
    def take_from_bag(self, item_name):
        if item_name in self.bag:
            item = self.bag[item_name]
            del self.bag[item_name]
            self.capacity += item.weight
            return item
        else:
            return None

    def take_weapon(self, weapon):
        old_weapon, self.weapon = self.weapon, weapon
        return old_weapon

# describe (printuje info o hraci), score (soucet cenných predmetu v bagu)
    def describe(self):
        print("Jmeno hrace:", self.name)
        print("Zdravi: " + str(self.health) + "/" + str(self.max_health))
        print("Zbyvajici kapacita batohu:", self.capacity)
        if self.bag:
            print("Obsah batohu:")
            for i in self.bag.values():
                print("-", i.describe())
        else:
            print("Prazdny batoh.")
        print("Zbran:", self.weapon.describe())

    def score(self):
        s = 0
        for i in self.bag.values():
            s += i.value
        return s


def attack_result(attack, defence):
    damage = randint(attack * 4 / 5, attack * 6 / 5)
    return max(damage - defence, 0)

def fight(player, monster):
    print("Souboj s protivnikem:", monster.name, "(" + str(monster.health) + " zdravi)")
    print("Tvoje zdravi: " + str(player.health) + "/" + str(player.max_health))

    players_turn = randint(1,20) > monster.vigilance
    while player.health > 0 and monster.health > 0:
        if players_turn:
            print('Utocis na protivnika.')
            damage = attack_result(player.weapon.attack, monster.defence)
            if damage == 0:
                print("Tvuj utok byl neucinny.")
            else:
                print("Tvuj utok zpusobil", damage, "zraneni.")
                monster.health -= damage
                print("Protivnikovo zdravi:", monster.health)
        else:
            print('Protivnik "' + monster.name + '" na tebe utoci.')
            damage = attack_result(monster.attack, player.weapon.defence)
            if damage == 0:
                print("Tento utok byl neucinny.")
            else:
                print("Tento utok ti zpusobil", damage, "zraneni.")
                player.health -= damage
                print("Tvoje zdravi: " + str(player.health) + "/" + str(player.max_health))
        print("Stiskni enter:", input())
        players_turn = not players_turn
    if player.health > 0:
        print("Protivnik je porazen!")
        return True
    else:
        print("To je tvuj konec.")
        return False

#trida room 
class Room:
    def __init__(self, description, ending = None):
        self.description = description
        self.monster = None
        self.weapons = {}
        self.items = {}
        self.directions = {}
        self.ending = ending

#metoda na pridani potovry do mistonsti
    def set_monster(self,monster):
        self.monster = monster

#metoda na pridani zbrane do mistosti + opak
    def add_weapon(self, weapon):
        self.weapons[weapon.name] = weapon

    def remove_weapon(self, weapon):
        if weapon.name in self.weapons:
            del self.weapons[weapon.name]

#pridani cenneho predmetu + opak
    def add_item(self, item):
        self.items[item.name] = item

    def remove_item(self, item):
        if item.name in self.items:
            del self.items[item.name]

#moznosti smeru
    def add_direction(self, name, room):
        self.directions[name] = room

#popis mistnosti (co v ni je)
    def describe(self):
        print(self.description)
        if self.weapons:
            print("V mistnosti se nachazeji nasledujici zbrane:")
            for w in self.weapons.values():
                print("-", w.describe())
        if self.items:
            print("V mistnosti se nachazeji nasledujici cenne predmety:")
            for i in self.items.values():
                print("-", i.describe())
        if self.directions:
            print("Z mistnosti se da odejit nasledujicimi smery:")
            for d in self.directions.keys():
                print("-", d)
        if self.monster != None:
            self.monster.react_to_noise()
            print("V mistnosti je " + self.monster.name + ".",)
            if self.monster.sleeping:
                print("Spi.")
            else:
                print("Je vzhuru!")

    def has_awake_monster(self):
        return self.monster != None and not self.monster.sleeping


def randomize(rooms, monsters, items, weapons):
    # randomize monsters
    assigned = set()
    for m in monsters:
        i = randint(0, len(rooms) - 1)
        while i in assigned:
            i = randint(0, len(rooms) - 1)
        rooms[i].set_monster(m)
        assigned.add(i)
    # randomize weapons
    for w in weapons:
        i = randint(0, len(rooms) - 1)
        rooms[i].add_weapon(w)
    # randomize items
    for it in items:
        i = randint(0, len(rooms) - 1)
        rooms[i].add_item(it)


def play(start):
    #vezme zákl info o hraci a spusti prvni room
    name = input("Zadej sve jmeno: ")
    player = Player(name)
    player.describe()
    print
    room = start
    room.describe()
    while True:
        if room.has_awake_monster():
            print
            result = fight(player, room.monster)
            if result:
                room.set_monster(None)
                print
                room.describe()
            else:
                print("--- neuspesny konec hry ---")
                break
        if room.ending == False:
            print("--- neuspesny konec hry ---")
            break
        if room.ending == True:
            print("--- Konec hry ---")
            print("Finalni skore:", player.score())
            break
        cmd = input("\nZadej prikaz: ")
        args = cmd.split()
        if len(args) == 0:
            continue
        #prikazy pro info o praci, jdi ven z mistosti a vezmi zadany predmet (+ kod k bagu) 
        elif args[0] == "info":
            print
            player.describe()
        elif args[0] == "jdi":
            if len(args) > 1 and args[1] in room.directions:
                room = room.directions[args[1]]
                print
                room.describe()
        elif args[0] == "vezmi":
            if len(args) > 1 and args[1] in room.items:
                item = room.items[args[1]]
                if player.add_to_bag(item):
                    room.remove_item(item)
                    print("\nBeres predmet " + args[1] + ".\n")
                else:
                    print("\nTo uz neuneses.\n")
                room.describe()
            elif len(args) > 1 and args[1] in room.weapons:
                weapon = room.weapons[args[1]]
                old_weapon = player.take_weapon(weapon)
                room.remove_weapon(weapon)
                room.add_weapon(old_weapon)
                print("\nBeres zbran " + args[1] + ".\n")
                room.describe()
        #prikaz pro odpocinek a pro polozeni cenneho predmetu + konec a napoveda
        elif args[0] == "odpocinek":
            if room.monster != None:
                print("\nTady je lepe neodpocivat.")
            else:
                print("\nNa chvili si tu odpocines.")
                player.rest()
        elif args[0] == "poloz":
            if len(args) > 1 and args[1] in player.bag:
                item = player.take_from_bag(args[1])
                room.add_item(item)
                print("\nPokladas predmet " + args[1] + ".\n")
                room.describe()
        elif args[0] == "konec":
            print("--- neuspesny konec hry ---")
            break
        elif args[0] == "napoveda":
            print("\nPovolene prikazy:")
            print("\tinfo")
            print("\tjdi <smer>")
            print("\tvezmi <predmet nebo zbran>")
            print("\todpocinek")
            print("\tpoloz <predmet>")
            print("\tkonec")
            print("\tnapoveda")

items = [ # jmeno, popis, hodnota, vaha
    Item("zlato", "Volne polozeny kus zlata.", 100, 10),
    Item("prsten1", "Prsten s diamantem.", 50, 1),
    Item("prsten2", "Prsten bez diamantu.", 5, 1),
    Item("prsten3", "Zlaty prsten.", 20, 1),
    Item("prsten4", "Zelezny prsten.", 1, 1),
    Item("vaza", "Cenna anticka vaza.", 75, 20),
    Item("miska", "Zlata miska osazena drahokamy.", 120, 5),
    Item("truhla", "Mosazna truhla plna zlatych minci.", 300, 150),
    Item("mince", "Zlata mince.", 10, 2),
    Item("diamant", "Diamant velky jako krepelci vejce.", 200, 5),
    Item("smaragd", "Bezny smaragd.", 25, 5),
    Item("vec", "Nejaka vec. Zrejme cenna.", 120, 40),
    Item("predmet", "Zahadny predmet. Vypada draze.", 230, 82),
    ]

superitem = Item("maska", "Faraonova maska. Velmi cenna.", 500, 50)

weapons = [ # jmeno, popis, utok, obrana
    Weapon("sekera", "Obrovska oborucni sekera. Uneses ji?", 15, 1),
    Weapon("kopi", "Dvoumetrove kopi.", 6, 8),
    Weapon("mec", "Uplne normalni mec.", 8, 6),
    Weapon("r_mec", "Rezavy mec.", 6, 4),
    Weapon("palice", "Velka dubova palice.", 12, 2),
    Weapon("kus", "Samostril. Ucinny, ale obtizne se natahuje.", 20, 0),
    Weapon("sv_mec", "Svetelny mec. Kde se tady vzal?", 30, 15),
    ]

monsters = [ # popis, utok, obrana, ostrazitost, zdravi
    Monster("mumie", 6, 0, 7, 55),
    Monster("mumie", 7, 0, 7, 50),
    Monster("odolna mumie", 6, 1, 7, 100),
    Monster("slaba mumie", 4, 0, 5, 50),
    Monster("slaba mumie", 4, 0, 5, 50),
    Monster("ostrazita mumie", 7, 0, 20, 50),
    Monster("pavouk", 5, 1, 10, 30),
    Monster("velky pavouk", 8, 2, 10, 50),
    Monster("velky zly pavouk", 10, 1, 15, 55),
    Monster("velky zly jedovaty pavouk", 12, 3, 10, 40),
    Monster("kobra", 20, 3, 18, 60),
    Monster("netopyr", 4, 4, 12, 40),
    Monster("stir", 14, 4, 11, 35),
    Monster("pisecny golem", 6, 6, 2, 200),
    ]

pharaoh = Monster("faraon", 25, 5, 10, 100)

exit = Room("Hura! Jsi venku z pyramidy a jsi nazivu.", True)
start = Room("Jsi ve vchodu do pyramidy.")
tomb = Room("Jsi ve slavne faraonove kobce.\n" +
        "Stena na zapade vypada, ze se da odsunout.")
tomb.set_monster(pharaoh)
tomb.add_item(superitem)

trap = Room("Vchazis do mistnosti, kdyz tu slysis, jak pod tebou cvaklo propadlo.")
snakes = Room("Padas do mistnosti plne hadu. Tim to pro tebe konci.", False)
rooms = [
    Room("Jsi v pyramide, chodby vedou na vychod a na jih."),
    Room("Jsi uprostred chodby, ktera vede zapadovychodnim smerem."),
    Room("Jsi v rohove mistnosti pyramidy. Chodby vedou na zapad a na jih."),
    Room("Jsi uprostred severojizni chodby. Stena na vychode vypada podezrele."),
    Room("Jsi uprostred severojizni chodby. Stena na zapade vypada uplne obycejne."),
    Room("Jsi v podlouhle mistnosti, ze ktere vede jedina chodba na sever.\n" +
        "Ve vzdalenem rohu mistnosti jsou schody nahoru."),
    Room("Jsi v pyramide, chodby vedou na sever, na jih a na vychod."),
    Room("Jsi v klikate chodbe, ze ktere se da pokracovat na sever a na vychod."),
    Room("Jsi v klikate chodbe, ze ktere se da pokracovat na sever a na zapad.\n" +
        "U steny chodby jsou schody nahoru."),
    Room("Jsi v obrovske mistnosti, severni stena je pokryta hieroglyfy.\n" +
        "Na jihu jsou dvoje dvere, v rohu mistnosti jsou schody nahoru."),
    Room("Jsi v druhem patre pyramidy, na severu jsou pootevrene dvere.\n" +
        "Chodba pokracuje na jih."),
    Room("Jsi v druhem patre pyramidy, na severu jsou pootevrene dvere.\n" +
        "Chodba pokracuje na jih."),
    Room("Jsi v rohove mistnosti v druhem patre pyramidy.\n" +
        "Chodby vedou na sever a na vychod. V rohu mistnosti jsou schody dolu."),
    Room("Jsi v rohove mistnosti v druhem patre pyramidy.\n" +
        "Chodby vedou na sever a na zapad. V rohu mistnosti jsou schody dolu."),
    Room("Jsi v nejvyssim patre pyramidy. Jedina chodba vede na jih.\n" +
        "Uprostred mistnosti jsou schody dolu."),
    Room("Jsi v nejvyssim patre pyramidy. Po prichodu za tebou zapadly dvere.\n" +
        "Uprostred mistnosti je skluzavka dolu. Je to zrejme jedina cesta ven."),
    ]

start.add_direction("ven", exit)
start.add_direction("dovnitr", rooms[6])
trap.add_direction("dolu", snakes)
tomb.add_direction("zapad", rooms[3])
rooms[0].add_direction("vychod", rooms[1])
rooms[0].add_direction("jih", rooms[3])
rooms[1].add_direction("vychod", rooms[2])
rooms[1].add_direction("zapad", rooms[0])
rooms[2].add_direction("zapad", rooms[1])
rooms[2].add_direction("jih", rooms[4])
rooms[3].add_direction("sever", rooms[0])
rooms[3].add_direction("jih", rooms[5])
rooms[4].add_direction("sever", rooms[2])
rooms[4].add_direction("jih", rooms[6])
rooms[5].add_direction("sever", rooms[3])
rooms[5].add_direction("nahoru", rooms[12])
rooms[6].add_direction("sever", rooms[4])
rooms[6].add_direction("jih", rooms[8])
rooms[6].add_direction("vychod", start)
rooms[7].add_direction("sever", trap)
rooms[7].add_direction("vychod", rooms[8])
rooms[8].add_direction("sever", rooms[6])
rooms[8].add_direction("zapad", rooms[7])
rooms[8].add_direction("nahoru", rooms[13])
rooms[9].add_direction("jihovychod", rooms[10])
rooms[9].add_direction("jihozapad", rooms[11])
rooms[9].add_direction("nahoru", rooms[14])
rooms[10].add_direction("sever", rooms[9])
rooms[10].add_direction("jih", rooms[12])
rooms[11].add_direction("sever", rooms[9])
rooms[11].add_direction("jih", rooms[13])
rooms[12].add_direction("sever", rooms[10])
rooms[12].add_direction("vychod", rooms[13])
rooms[12].add_direction("dolu", rooms[5])
rooms[13].add_direction("sever", rooms[11])
rooms[13].add_direction("zapad", rooms[12])
rooms[13].add_direction("dolu", rooms[8])
rooms[14].add_direction("jih", rooms[15])
rooms[14].add_direction("dolu", rooms[9])
rooms[15].add_direction("dolu", tomb)

randomize(rooms, monsters, items, weapons)
play(start)
