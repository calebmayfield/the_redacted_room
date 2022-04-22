def door(code):
    print("You walk to the door. The keypad has a 3 character display. You enter a code.")
    while True:
        option1 = int(input("Number one: "))
        break
    while True:
        option2 = int(input("Number two: "))
        break
    while True:
        option3 = int(input("Number three: "))
        break
    selected_code = int(str(option1) + str(option2) + str(option3))
    print("")
    if selected_code == code:
        print("The keypad flashes green and the door opens. Agent REDACTED greets you on the otherside.")
        return (1)
    else:
        print("The keypad flashes red. The code is incorecct.")
        print("")


def map(choice, numberlocation, numbervalue):
    print("")
    print("You examine the map of the USSR. The detail is striking to you.")
    if choice == numberlocation:
        print("Upon closer examination, you notice where Moscow should be, you see the number",
              str(numbervalue) + ".")
        print("")
    else:
        print("All of that time spent learning Russian will be a waste if you cant complete this challenge.")
        print("You don't find any helpful numbers so you move on.")


def desk(choice, numberlocation, numbervalue):
    print("")
    print("You walk over to the desk and notice a pair of sunglass lying on it.")
    if choice == numberlocation:
        print("Inside the frame you see the number," + str(numbervalue) + ".")
        print("")
    else:
        print("You wonder why anyone would leave these behind. However, you don't find any helpful numbers so you move on.")
        print("")


def pantry(choice, numberlocation, numbervalue):
    print("")
    print("You open the pantry and find it mostly empty. You check the few dishes.")
    if choice == numberlocation:
        print("Printed on the bottom of a coffee cup is the number",
              str(numbervalue) + ".")
        print("")
    else:
        print("You wonder when the last time someone cleaned this place was.")
        print("You don't find any helpful numbers and decide to keep looking elsewhere.")


def rug(choice, numberlocation, numbervalue):
    print("")
    print("At the foot of the bed there is a rug that has seen better days.")
    print("You wonder how many applicants had nervously paced it before you.")
    if choice == numberlocation:
        print("The pattern seems distorted.")
        print("You get a closer look and see the number", str(numbervalue) + ".")
        print("")
    else:
        print("You don't find any helpful numbers and start to wonder exactly what the Agent's note meant by terminated...")
        print("")


def portrait(choice, numberlocation, numbervalue):
    print("You walk over to a dusty portrait of President Truman")
    if choice == numberlocation:
        print("Where his American flag pin should be you notice the number", str(
            numbervalue) + ".")
        print("")
    else:
        print("The room feels like no one has been inside it since Truman was the President you think to yourself")
        print("Unfortunately the former President doen't offer any helpful numbers")
        print("")


def bookshelf(choice, numberlocation, numbervalue):
    print("You approach the bookshelf and examine some of the titles.")
    if choice == numberlocation:
        print("One catches your eye. Within the title you see the number",
              str(numbervalue) + ".")
        print("")
    else:
        print("Depending on how long you are here, you may have time to read them all.")
        print("You don't find any helpful numbers.")
        print("")
