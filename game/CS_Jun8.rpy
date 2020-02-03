label junstart_7:
    $ uihide = True
    stop music2 fadeout 2.5
    $ junhearts += 1
    scene HospitalEntrance with fade
    play music "music/breeze.ogg" fadein 5.0
    "I decide to get up a little earlier than normal to go visit Jun in the hospital."
    "I feel a bit poopy from having woken up at a time I'm not used to but I consider it a worthy sacrifice if it means I can brighten his day even just a little."
    show ats 1 c c smile at two
    show yui 1 c smile at eight
    show j 1 c watch at fdis, five
    "Wait, is that... Jun?"
    if day5 == "jun":
        "I see him walking out of the hospital with his parents."
    else:
        "I see him walking out of the hospital with two adult tigers."
        "Are those his parents?"
    show j 1 c shock at fdis
    play music2 "music/BGM/The People Here.ogg" fadein 5.0
    j "\"[povFirstName]-san?\""
    mc 1 u shock "\"Good morning... what are you doing out here?\""
    show j 1 c watch at fdis
    j "\"I got discharged this morning so my parents are taking me home.\""
    if day5 == "jun":
        show j 1 c sigh at fdis
        ats "\"Ah, [povLastName]-kun, it's a pleasure to meet you again! Say, I saw your match at the Prefectural finals and I was really amazed by-\""
        yui "\"Dear, we really don't have time for this right now.\""
        ats "\"O-oh, right, right.\""
        mc 1 u considerate "\"It's good to see you again too, sir.\""
        "Jun's dad is just as intense as the first time I met him."
    else:
        show j 1 c wince at fdis
        ats "\"Oh my, could this be [povName]?!\""
        j "\"D-dad, please don't st-\""
        ats "\"It is. It really is! Oh my God, when my son told me he had a friend with your name, I didn't really think it would be you but it is. I'm your fan, could you sign an autograph for me?!\""
        mc 1 u fsmile "\"U-uhm... I-I'm not a professional player yet you know...\""
        "I'm used to getting {i}some{/i} attention because of my standing in the national junior ranking but I've never had someone so brazenly calling attention to it before."
        "Now there are lots of people looking at us..."
        j "\"Dad...\""
        yui "\"Dear, I understand your enthusiasm but you really shouldn't be so loud in the middle of the street.\""
        "Jun's mother immediately censors her husband."
        ats "\"Oh, I suppose you're right.\""
        yui "\"Also, the first thing you do when meeting one of Jun's friends should be to introduce yourself, not ask for an autograph.\""
        ats "\"R-right...\""
        "Wow, she really controls him quite easily..."
        show j 1 c considerate at fdis
        ats "\"I'm Atsushi Kobayashi, Jun's father. It's a pleasure to meet you.\""
        yui "\"And I'm Yui, Jun's mother. It really is good to finally meet one of Jun's friends. He talks so much about you!\""
        show j 1 c blush at fdis
        j "\"M-mom!\""
        mc 1 u shock "\"H-he does?\""
    show j 1 c considerate at fdis
    j "\"Erm... can we please talk about something less embarrassing?\""
    yui "\"Oh, sweetie, are you embarrassed by us?\""
    show j 1 c sigh at fdis
    j "\"Of course I am.\""
    "B-blunt!"
    ats "\"Tch, you really don't mince words sometimes.\""
    j "\"Why would I?\""
    "Wait... they're smiling? And laughing?"
    "I thought they'd be offended by his response but they... like it?"
    "... What a weird family."
    show j 1 c watch at fdis
    j "\"By the way, [povFirstName]-san, what are you doing here?\""
    mc 1 u talk "\"I wanted to check up on you before I went to school.\""
    show j 1 c smile at fdis
    j "\"Oh. Hehe, thanks for worrying about me but, as you can see, I'm perfectly fine now.\""
    mc 1 u curious "\"And the wound on your head is already healed?\""
    show j 1 c happy at fdis
    j "\"Yep. It was a pretty minor cut so it healed in no time. The doctor also said that there's no sign of concussion so I'm free to go.\""
    mc 1 u smile "\"That's great. I'm glad nothing bad happened.\""
    show j 1 c watch at fdis
    j "\"Mom, Dad, [povFirstName]-san was the one who found me when I collapsed and called for help. He's the reason I got treatment so fast.\""
    yui "\"Oh, is that so? I didn't know that!\""
    ats "\"We're really in your debt. Who knows what would have happened if you hadn't found him. Just a few more minutes and his heart might not have recovered!\""
    mc 1 u shock "\"His heart?!\""
    show j 1 c considerate at fdis
    j "\"Don't mind them. Dad thinks that just because I bled a little, my heart was going to stop beating. I already told him it wasn't nearly enough blood to cause any serious problems but he won't listen.\""
    mc 1 u wince "\"I don't know, it certainly looked like a lot of blood to me at the time.\""
    show j 1 c wry at fdis
    j "\"It wasn't really that bad. If it were, I wouldn't be getting discharged already.\""
    mc 1 u "\"I guess you're right.\""
    yui "\"Well, thank you very much for taking such good care of our son, [povLastName]-kun. We truly are grateful for your help.\""
    mc 1 u happy "\"What? It was nothing. I'm just happy to help him. He's a good friend.\""
    show j 1 c happy at fdis
    j "\"See? I told you, [povFirstName]-san is a really good person.\""
    mc 1 u avoidb "\"N-now, that's not really a big deal...\""
    yui "\"It is to us. Either way, if you'll forgive us, we have to take Jun back home. Just to be careful, we'll keep him at home for a few days to keep an eye on him. He should be back in school in no time though!\""
    show j 1 c sigh at fdis
    j "\"Mom, I already told you that's unnecessary...\""
    ats "\"You can't fault your mother for worrying, Jun.\""
    j "\"I guess not.\""
    j 1 c smile "\"I'll see you later, [povFirstName]-san. Thank you for dropping by to visit me.\""
    mc 1 u happy "\"Of course. See ya!\""
    show j 1 c smile at offscreenleft
    show ats 1 c c smile at offscreenleft
    show yui 1 c smile at offscreenleft
    with moveoledis
    stop music2 fadeout 2.5
    "..."
    "Why do I still have this awful feeling in my chest?"
    stop music fadeout 2.5
    $ date = None
    jump Day13_Jun