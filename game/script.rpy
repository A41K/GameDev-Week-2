
default hunger = 100
default thirst = 100
default energy = 100

label start:
    menu:
        "choose what you do..."

        "eat some food...":
            $ hunger = min(hunger + 5, 100)
            $ thirst -= 10
            $ energy -= 10

        "drink some water...":
            $ hunger -= 10
            $ thirst = min(thirst + 5, 100)
            $ energy -= 10

        "sleep...":
            $ hunger -= 10
            $ thirst -= 10
            $ energy = min(energy + 5, 100)

    if hunger <= 0:
        "you've died of starvation... you forgot to eat!"
        return
    elif thirst <= 0:
        "you've dehydrated... you forgot to drink!"
        return
    elif energy <= 0:
        "you're too exhausted to breathe... you forgot to take a breath!"
        return

    jump start