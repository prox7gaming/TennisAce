label cs_final:
    window hide
    if may8 == False:
        scene May8 with fade
        $ may8 = True
    elif may9 == False:
        scene May9 with fade
        $ may9 = True
    elif may10 == False:
        scene May10 with fade
        $ may10 = True
    elif may11 == False:
        scene May11 with fade
        $ may11 = True
    elif may12 == False:
        scene May12 with fade
        $ may12 = True
    elif may15 == False:
        scene May15 with fade
        $ may15 = True
    elif may17 == False:
        scene May17 with fade
        $ may17 = True
    elif may18 == False:
        scene May18 with fade
        $ may18 = True
    elif may19 == False:
        scene May19 with fade
        $ may19 = True
    elif end == True:
        scene Empty with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    if end == True:
        jump noroute
    elif may9 == False:
        $ date = "cs2"
    elif may10 == False:
        $ date = "cs3"
    elif may11 == False:
        $ date = "cs4"
    elif may12 == False:
        $ date = "cs5"
    elif may15 == False:
        $ date = "cs6"
    elif may17 == False:
        $ date = "cs7"
    elif may18 == False:
        $ date = "cs8"
    elif may19 == False:
        $ date = "cs9"
    elif may19 == True:
        $ date = "cs10"
        $ end = True
    scene Bedroom with fade
    $ rando = renpy.random.randint(1, 6)
    if rando == 1:
        "Alright... gotta start getting ready for the day..."
    elif rando == 2:
        "Ugh... stupid alarm clock. I wish I could just turn this thing off and sleep in..."
    elif rando == 3:
        "Hmm... I wonder what I should do today after class..."
    elif rando == 4:
        "I really hope today doesn't suck... guess I'll have to make the best of it."
    elif rando == 5:
        "Ugh... so sleepy... I don't want to go out today..."
    elif rando == 6:
        "I wonder what's going to happen today."
    play music2 "music/BGM/Funin and Sunin.ogg" fadein 5.0
    scene Black
    $ uihide = None
    $ renpy.transition(dissolve)
    call screen characterselect_jun
