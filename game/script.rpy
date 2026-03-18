
default steal = 0
default question = 0
default trust = 0

init python:
    achievement.register("First Theft")
    achievement.register("Independent")

default player_name = "Player"
define P = Character("[player_name]")
define skip = Character("TIMESKIP", color="#ff00ff")
define B = Character("Brother", color="#0000ff")
define Officer = Character("Officer", color="#008000")
define Teacher = Character("Teacher", color="#606010")
define Person = Character("Person", color="#901022")
define Boss = Character("Nathan")
define S = Character("Shane", color="#109090")
define shrug = Character("???")


define N = Character("Narrator", color="#808080")

label start:


    N "Welcome to Fools Gold. This is a visual novel about trust, stealing and friendship. I hope you like it!"

    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()
    
    if not player_name:
        $ player_name = "Player"

    N "I really really hope you will enjoy this. Now let's stop the yapping and get started"

    jump Intro

label Intro:

    N "You live in Great Britain, in the 1980's your name is [player_name] and you are a 22 years old"
    N "You and your brother have been interested in valuable goods and history since you knew your minds"
    N "Also you both been really good at stealing aswell. Your brother more than you, but you learnt from him"
    N "It's been over 10 years since you last seen your brother since that incident"

    jump Incindent

label Incindent:

    skip "ACT 0 - THE INCIDENT 10 YEARS BEFORE"

    P "Catch me *panting*"

    B "I got you bro"

    N "Your brother pulled you up the window inside"

    B "Y'know, next time I will just let you fall. You need to get stronger to pull yourself up"

    P "Yeah Yeah blah blah blah Your my brother so you will always help me *sticks tongue out*"

    B "Just shhhh we don't want to get caught"

    N "You both walk up to glass case that has a map"
    
    P "Oh my god is that it?"

    B "It definietly is"

    P "I've never seen a map of the world this big and old"

    B "Yeah its authentic"

    N "You both heard shouting"

    Officer "PUT YOUR HANDS UP"

    N "The Officer pulls around the corner and see you two already with their hands up"

    N "Later back at school"

    Teacher "Cole this was your last strike. Pack up your bags you are expelled"

    P "No, you can't just expel him"

    Teacher "Say your goodbyes and be happy that I didn't expel you too"

    N "You go up to your brother"

    B "[player_name] everything will be fine okay?"

    N "You hug your brother"

    B "I will come back. I promise"

    N "Your brother leaves through the window."

    jump ACT1

label ACT1:

    skip "ACT 1 - TRUST 10 YEARS LATER"

    N "You're currently on the street, listening to music and walking to your job in a bar"
    N "You get in 15 minutes late"

    Boss "Welcome [player_name] the late, great and definietly fired"

    P "You know you were right at great, but I can live with the others aswell"

    N "You get some glasses and change into your outfit"
    N "There's a girl who wants a drink"

    P "What's up what is your order sweetheart"

    P "Wait wait let me guess. Gin and Tonic"
    Person "Damn, yeah that's what I wanted"
    P "Y'know your not a regular here"
    Person "Yeah This is not my neighborhood"
    P "Well y'know gin and tonic is one of the most ordered drinks here"
    P "and surprisingly more by men then women"
    Person "You know at other bars I don't get statistics"
    P "At other bars you don't get G&T like this"

    N "You hand her the drink. She just puts the credit card on the counter before you could finish your monologue"

    P "Usual girls probably open cause it's daddy's money"
    N "You noticed the necklace around her neck so you go out"

    N "She's trying to find where she wants to go on her phone"
    P "Want some help around? I live nearby"
    Person "Yeah I would appreciate it"

    menu:
        "You have the chance to steal her necklace but will you?"
        "Steal her necklace":
            jump steal
        
        "Don't steal her necklace":
            jump no_steal
        
label steal:
    $ steal += 1
    $ achievement.grant("First Theft")
    $ achievement.sync()
    show screen achievement_popup("First Theft")
    N "You stole her necklace"
    N "+1 Necklace"

    jump home

label no_steal:
    N "You were respectful and didn't steal her necklace"

    jump home

label home:
    Person "Ah, thank you"
    P "My pleasure miss"

    N "You go back inside. A few hours later your shift ends so you pack up and go home"
    N "You get to your houses door, but you notice it's already unlocked"

    N "You see a silhouette of a person with the necklace you stole around his neck"
    
    menu:
        "What will you do?"

        "You again?":
            jump again
        
        "Who are you?":
            jump whoareyou
        
        "You just stand there frozen":
            jump shock
        
label again:
    P "Ashley if its you aga..."

    N "A deep voice cuts through my monologue"

    shrug "My name is not Ashley."
    shrug "By the way, do people just like walk in your place unannounced?"

    P "Well yeah... sometimes"
    
    jump whoareyou

label shock:
    N "You stand there shocked"

    shrug "don't just stand there shocked. I dont bite"

    jump whoareyou

label whoareyou:
    P "Who are you??"

    N "He sees your shaking"

    shrug "Just calm down okay? I know a lot about you"

    P "You know that just makes me more scared"

    shrug "I was close friends with my your brother"

    P "I need a name yknow"

    S "Okay okay. My name is Shane"

    P "Doesn't ring a bell sadly"

    P "Where is the necklace by the way"

    S "First drawer on the left"

    P "You know this chick was kinda hot and ...."

    S "Im not here for a story time"
    S "Im here for business"

    S "We can find the Chest of britain"

    P "The chest that's been lost for over 30 years?"
    P "doubt it. We already tried"

    S "I know, but we have a solid hint for us that can maybe lead to it"

    P "Well i have jackshit with a *maybe* I need something 100%% or im 0%%"

    S "You know you can't be certain with something that's been lost for over 400 years"
 
    menu:
        "So will you join me?"

        "How can I trust you":
            jump trusting
        
        "Go f yourself":
            jump end1
        
        "yes":
            jump yes
    
label end1:
    $ achievement.grant("Independent")
    $ achievement.sync()
    show screen achievement_popup("Independent")
    $ question += 1

    P "Go f yourself. I'm happy like this Now get out"

    N "Shane just clicks his tongue then sighs"

    S "Sour decision I guess"

    N "Shane Leaves and your life continues as normal."

    N "END - INDEPENDENT"
    return

label trusting:
    $ trust += 1
    S "You already know you can't trust anybody in this business"

    P "Yeah yeah I know"

    P "Still I want to know if I can trust you"

    S "Your choice"

    P "Fine I'll trust you, but if you try anything I will make you suffer"

    N "He just snickers"

    S "Okay tuff guy"

    jump plan

label yes:
    P "Yes. Count me in"

    S "Well I thought you would put up a fight, but I guess not"

    P "You know how much I hate my life right now"

    P "I make 15$/hr"

    S "you know that's not bad"

    N "You roll your eyes"

    jump plan

label plan:
    S "Now cause you agreed"
    S "2 days from now there's an auction happening where the Cross of Monaco is being sold"
    S "It's the key to th..."

    P "Yeah I know Y'know I've been studying this for atleast 10 years now"

    S "Okay history boy. Then I'll just lay the plan out"
    S "You have to cut the power and while that happens I'll get the cross Okay?"

    P "Cutting the power??? That's all Im doing??"

    S "Yeah. You're just a rookie in this"
    P "Finee fine. I need planning right?"
    S "Definietly. Get floor plans, guards, time cards anything useful for us"

    P "Aye Aye cap"

    S "Just get to work okay?"
    S "I'll text you before and if you need anything text me"

    P "Okay got it"

    N "You studied everything you could find about this auction from the building to the people and even the story of the chest and even Shane"

    skip "2 DAYS LATER"

    N "You needed box cutters, a tux and a hamster????"

    jump auction

label auction:
    S "I got you your stuff, but why did you need a hamster?"

    P "It's for you cause you look lonely"

    S "FOR ME????"

    P "Yeah hope you will take good care of it"

    S "jesus christ *he mutter*"

    N "We drive to the auction place"

    S "Got everything ready?"

    P "Yes"