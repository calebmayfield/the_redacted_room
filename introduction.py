def intro():
    print("You wake up and wonder what time it is.")
    print("It's dark and you fumble for you phone.")
    print("")
    print("Dead.")
    print("")
    print("Odd. You never forget to charge your phone.")
    print("")
    print("As you come out of the fog of sleep you realize that you don't know where you are.")
    print("You sit up in bed and try to take in your surroudings.")
    print("")
    print("Across the room you can make out a dresser.")
    print("")
    print("1) - examine the dresser")
    print("2) - check under the bed")

    while True:
        dresserorbed = input()
        if int(dresserorbed) == 1:
            print("You feel your way to the dresser and find what feels like a note.")
            print("It's too dark to read it so you return to the bed.")
            print(
                "By now your eyes have adjusted enough to notice a switch under the bed.")
            print("You twist it and the room is illuminated.")
            break
        elif int(dresserorbed) == 2:
            print("You feel under the bed and find a switch.")
            print("You twist it and the room is illuminated.")
            print("Across the room on the dresser you see a note.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

    print("")
    print("The note reads:")
    print("Congratulations.")
    print("")
    print("After careful consideration you have been selected to potentially join the CIA.")
    print("However. Before we can extend an offer, you must demonstrate your ability to improvise.")
    print("You will notice the key pad on the door.")
    print("Hidden in this room are 3 numbers you must enter in the correct order")
    print("to exit the room.")
    print("")
    print("Failure to complete this task will result in your termination.")
    print("")
    print("Good luck.")
    print("-Agent REDACTED")
    print("")
    print("You examine the room:")
