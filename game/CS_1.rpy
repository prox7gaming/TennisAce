label cs_1:
    window hide
    scene May2 with fade
    $ may2 = True
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    $ date = "cs1"
    scene Bedroom with fade
    play sound "music/alarm.ogg"
    "..."
    "... Ugh, is it morning already?"
    "Yeah yeah yeah, I get it, shut up already..."
    "Stupid alarm. Wish I could just smash it into a wall..."
    "But then again, this is super expensive so I'll refrain from that..."
    "Ugh... having a single day of class in the week is so bothersome."
    "Why couldn't they just take the whole week off? It's Golden Week, damn it!"
    "My bed is so comfortable too..."
    "Can I just sleep for five more mi-"
    play sound "music/knock.ogg"
    a 1 c "\"Aniki?\""
    "Aki knocks on my door, calling out to me."
    mc 1 c wince "\"Aki? What are you doing knocking on my door so early?\""
    a 1 c "\"Shoichi-nii asked me to make sure you show up for class today. If you don't get out of the room in five minutes, I'm walking in with a bucket.\""
    "..."
    "You don't have class today, why are you even up at this time, you little brat?!" with hpunch
    "... Maybe I could just l-"
    a 1 c "\"And don't even think of locking the door. I took a copy of the key last week just to make sure.\""
    "Damn it..."
    play sound "music/fabric.ogg"
    "Sighing, I get up from my bed, grabbing my uniform that was lazily thrown over a chair yesterday and walk to the bathroom."
    $ end = False
    play music2 "music/BGM/Funin and Sunin.ogg" fadein 5.0
    scene Black
    $ uihide = None
    $ junhearts = 0
    $ shoichihearts = 0
    $ keisukehearts = 0
    $ renpy.transition(dissolve)
    call screen characterselect_jun
