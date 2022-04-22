import random
from introduction import intro
from menu import menu
from search_item import door, map, desk, pantry, rug, portrait, bookshelf


codenumber1 = random.randint(0, 9)
codenumber2 = random.randint(0, 9)
codenumber3 = random.randint(0, 9)
code = int(str(codenumber1) + str(codenumber2) + str(codenumber3))
items = ["door", "map", "desk", "pantry", "rug", "portrait", "bookshelf"]
number1location = random.randint(1, 2)
number2location = random.randint(3, 4)
number3location = random.randint(5, 6)

intro()
while True:
    choice = menu(items, "What do you want to inspect?")
    if choice == 1:
        map(choice, number1location, codenumber1)
    elif choice == 2:
        desk(choice, number1location, codenumber1)
    elif choice == 3:
        pantry(choice, number2location, codenumber2)
    elif choice == 4:
        rug(choice, number2location, codenumber2)
    elif choice == 5:
        portrait(choice, number3location, codenumber3)
    elif choice == 6:
        bookshelf(choice, number3location, codenumber3)
    else:
        result = door(code)
        if result == 1:
            break
