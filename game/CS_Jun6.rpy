label junstart_5:
    $ uihide = True
    stop music2 fadeout 2.5
    $ junhearts += 1
    scene SCorridor with fade
    "I've been thinking over a lot of stuff since I last saw Jun."
    "I've been wondering what I could do to help him feel better."
    "It's plain to see that the stress has been taking a toll on him... so I've thought of ways that I could potentially try to help without also being intrusive and annoying."
    "In the end, all I could come up with was a silly little \"care package\"."
    "I've bought all of Jun's favorite sweets as well as some vitamin pills and some tasty food."
    "I want to make sure he's eating... even if it's junk food, it's still better than nothing."
    "Hehe, I can't wait to see his face when I give this to him."
    play sound "music/slidingdoor.ogg"
    scene MusicRoom with fade
    mc 1 u happy "\"Heya, pardon me for the intru-\""
    mc 1 u curious "\"Huh?\""
    "At first, I don't see anything."
    "The tiger I expected to find sitting in front of the piano isn't there."
    "For a second, I imagine that he might have taken my advice to heart and decided to take a break to rest today."
    "Feeling satisfied with that, I ready myself to step outside and close the door."
    "Then, for some reason, a chill runs over my spine."
    "Call it instinct or premonition, but something in me tells me to investigate further."
    play sound "music/footsteps wood.ogg"
    "I step inside the room and begin to walk over to the piano."
    mc 1 u curious "\"Ju-\""
    mc 1 u shock "\"!\""
    "Lumped over in the floor is the tiny figure of a tiger dressed in his school uniform."
    "He is fallen over behind the piano, hidden from view from anyone who doesn't bother to take more than a cursory glance into the room."
    mc 1 u shock "\"Jun!\""
    "Without I second thought, I run towards him."
    mc 1 u shock "\"Jun. Jun, are you alr-\""
    "That's when I notice it."
    "A small puddle of blood forming around his head."
    "I look up and see a few drops of blood running down the edge of the piano."
    mc 1 u shock "\"No way...\""
    "I desperately open my bag, rummaging through for a piece of cloth or anything I can use to put pressure on it."
    "Come on come on come on."
    "A clean shirt!"
    mc 1 u wince "\"Come on, Jun, answer me.\""
    "I try to remember the basics of first aid that I learned a few years ago in school but it's no use, my mind is racing too fast to properly think."
    mc 1 u shock "\"{size=+4}Help! Someone... anyone... please... HELP!{/size}\""
    scene Black with fade
    play music "music/ambulance.ogg" fadein 1.0
    "..."
    "Jun was taken to the hospital a few minutes afterwards."
    "I don't know if anything I did past calling for help was useful at all."
    "I wasn't allowed to ride with him in the ambulance for some reason... instead, the school doctor went with them."
    "As I stood there in front of the school gate, the cuff of my shirt soaked in blood, watching that ambulance riding away... I felt so small."
    "{cps=10}... Useless.{/cps}"
    stop music fadeout 2.5
    $ date = None
    jump cs_final
