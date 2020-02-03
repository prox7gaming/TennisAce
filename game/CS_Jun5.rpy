label junstart_4:
    $ uihide = True
    stop music2 fadeout 2.5
    $ junhearts += 1
    scene MusicRoom with fade
    play music2 "music/BGM/Classical/Fantaisie Impromptu.ogg" fadein 10.0
    "The smell of dust and chalk permeates the air."
    "Today again, I came to this old music room to watch Jun rehearsing."
    "Usually, watching him playing would calm me."
    "Seeing his entranced figure as he gracefully played, his arms dancing across the keys filled with satisfaction."
    "I might even dare call it happiness."
    "Today, like always, I watch as he plays the same old piano."
    "It's the same song that he's been practicing lately... even if I know nothing of music, I could always appreciate it."
    "But unlike the other times I've watched... the air feels tense."
    "I can't quite put my finger on it... with my limited knowledge, nothing he's doing seems to be \"wrong\"."
    "And yet, in a sense, it all feels wrong."
    "Jun moves with a desperation that is unlike him."
    "His body moves jerkily, almost mechanically. Every now and then I see his ears twitching."
    "His tail lashes around, his eyes keep fluttering open whereas he'd normally have them closed the whole time."
    "His expression looks to be anything but peaceful... he looks strained."
    "In more ways than one, I worry."
    "Not knowing what is happening, I merely sit and watch this performance."
    "Calling it grating would probably be a stretch, but at the same time... seeing it makes my heart ache."
    "His mouth curves and his lips quiver... it looks to me like he's gritting his teeth."
    "At this point, I am absolutely convinced that something is wrong."
    "I consider to myself whether I should stop his performance but I also know how he is."
    "He'd probably kick me out if I interrupted him halfway."
    "I grit my own teeth, trying to keep myself sitting down."
    "This is nothing like the last times I'd come to watch."
    "It scares me... from the back of my mind, I keep having bad thoughts."
    "Has he been pushing himself too hard again? Knowing him, that possibility sounds completely believable."
    "Even though I promised I'd stop bothering him about it, I can't help but worry."
    "If he hurts himself because he's been overburdening himself... as an athlete, I've seen the damage that over practicing can cause... not just to your body but to your mind."
    "I just want this to stop."
    "I want this performance to stop."
    "Please, just make him stop."
    stop music2 fadeout 2.5
    show j 1 u wince at fdis, five with dissolve
    "After what seems like an eternity, the last note rings out."
    "Jun sits perfectly still, panting in his seat."
    "I want to reach out to him and say something but my throat merely contracts uselessly."
    "I struggle to find my words."
    show j 1 u considerate at fdis
    j "\"What did you think?\""
    "As he always does, Jun asks me for my feedback on his performance."
    "Usually I'd have nothing but praise to give him... even if I wanted to, I know nothing of music so I couldn't criticize."
    "But today... even as he looked at me and tried to smile, the strain on his face was obvious."
    play music3 "music/BGM/Heartbreaking.ogg" fadein 5.0
    mc 1 u worried "\"Jun... are you... are you alright?\""
    show j 1 u wry at fdis
    j "\"Huh? Of course I am.\""
    "Liar."
    mc 1 u worried "\"... I... I just felt like something was wrong. You didn't play like you usually do... it felt wrong somehow.\""
    "Even as I'm trying to explain my worries, I can't come up with coherent enough words to explain my thoughts."
    "\"It felt wrong\". A fifth grader could probably come up with a better explanation."
    show j 1 u wince at fdis
    j "\"It... was no good?\""
    "Somehow, he looks so pitiful as he mumbles those words."
    "The disappointment is clearly obvious in his eyes."
    "Whether he's disappointed at me or at himself, I don't know."
    "Yet, I still feel guilty."
    "I feel as if I had just yelled at a small, frail little kitten."
    "I know that's an unfair comparison but I can't help but feel that way."
    mc 1 u worried "\"Sorry, I didn't mean to bring you down, it's just...\""
    "The words die in my throat."
    j "\"Just?\""
    "Without missing a beat, he probes me for more information."
    "I compose myself, afraid to say the words I'm thinking."
    "He's already gotten mad at me for it before... I'm afraid of how he might react of I bother him with this subject again."
    "But the rational part of my brain trumps over my fear, reminding me that there are more important things than that."
    mc 1 u avoid "\"I'm worried, Jun... You seemed out of it the entire day. I thought you were just distracted during class but now... even when you were playing, it felt like you were overexerting yourself.\""
    mc 1 u wince "\"It... looked like you were in pain.\""
    show j 1 u shock at fdis
    $ renpy.pause(1.0)
    show j 1 u considerate at fdis
    j "\"I'm fine. You don't have to worry about me.\""
    "I am completely surprised by his reaction."
    "I expected him to get annoyed. I expected him to yell. I expected him to kick me out."
    "Instead, his voice came out meek, almost pleading. As if he desperately wanted me to believe him."
    mc 1 u worried "\"You don't look {i}or{/i} sound fine.\""
    if day5 == "jun":
        mc 1 u worried "\"Are we going to have a repeat of last time?\""
        show j 1 u wry at fdis
        j "\"L-last time?\""
        mc 1 u sigh "\"The day when I had to force you to go to the school doctor because you were having chest pains.\""
        show j 1 u shock at fdis
        j "\"Ah!\""
        show j 1 u considerate at fdis
        j "\"It... it wasn't chest pain. I told you, it was-\""
        mc 1 u sigh2 "\"Shortness of breath? Like I'm gonna believe that.\""
        show j 1 u wry at fdis
        j "\"I'm telling you, I'm fi-\""
        mc 1 u sigh "\"Of course you're not fine!\""
        show j 1 u shock at fdis
        mc 1 u sigh2 "\"And I think I know what you have...\""
        show j 1 u wince at fdis
        j "\"Y-you do?\""
        mc 1 u avoid "\"Yeah...\""
        mc 1 u sigh "\"You're having heart problems because you're overweight, aren't you?\""
        show j 1 u shock at fdis
        $ renpy.pause(1.0)
        show j 1 u annoyed at fdis
        j "\"... [povFirstName]-san, I am not amused.\""
        mc 1 u shock "\"Huh?\""
        j "\"You just called me fat!\""
        mc 1 u wince "\"Wha- but, I mean... it's kinda true?\""
        j "\"[povFirstName]-san... do you want me to kick you?\""
        mc 1 u shock "\"Eh?!\""
        "W-What did I do?"
        mc 1 u worried "\"If it's not that then what's going on with you?\""
        show j 1 u wince at fdis
        j "\"I...\""
    else:
        mc 1 u worried "\"I know you're a bit frail but... I'm starting to worry it's actually something serious.\""
        show j 1 u wry at fdis
        j "\"I-it's not... I'm fine.\""
        mc 1 u sigh2 "\"You don't like fine. You look anything but fine.\""
        show j 1 u considerate at fdis
        j "\"[povFirstName]-san, please... I'm telling you... I'm fine.\""
        "I want to believe... I really want to believe him."
        "But when he looks at me with such a strained smile on his face, how can I?"
        mc 1 u worried "\"Then what's going on? Why do you seem so out of it today.\""
    show j 1 u wince at fdis
    j "\"I..."
    show j 1 u considerate at fdis
    extend " I'm just really tired... I didn't really sleep last and I've also caught a cold...\""
    mc 1 u avoid "\"You don't look like you have a cold.\""
    show j 1 u wry at fdis
    j "\"Just because I'm not coughing doesn't mean I don't have a cold. My head is spinning, I'm running a fever and my throat hurts.\""
    mc 1 u shock "\"Then why didn't you say something earlier? Why did you even come to school at all today?\""
    show j 1 u considerate at fdis
    j "\"I didn't want to make you worry. You know how you are... if you know I'm sick you'd be fussing over me all day.\""
    mc 1 u worried "\"... You're not lying to me are you?\""
    show j 1 u wry at fdis
    j "\"...\""
    "Why won't you answer?"
    "Why are you looking at me like that?"
    mc 1 u wince "\"... Jun?\""
    show j 1 u considerate at fdis
    j "\"... Yes. I promise I'm not lying.\""
    "..."
    mc 1 u worried "\"If that's the case then you really should be resting. You should head to the doctor's office.\""
    j "\"You see, this is exactly why I didn't want to tell you...\""
    mc 1 u sigh2 "\"Are you seriously worried about rehearsing right now? You need to rest. You can't keep pushing your body like that.\""
    show j 1 u sigh at fdis
    j "\"I told you... I'm fine.\""
    mc 1 u annoyed "\"And I told you you're obviously not fine.\""
    mc 1 u sigh "\"Come on, just do what I'm telling you already.\""
    show j 1 u wince at fdis
    j "\"But...\""
    "Why does he always have to be so difficult?"
    "It's like trying to argue with a child.\""
    mc 1 u worried "\"Come on, Jun... please?\""
    j "\"D-don't look at me like that... it's hard to say no.\""
    mc 1 u worried "\"That {i}is{/i} the point.\""
    show j 1 u considerate at fdis
    j "\"J-just a little more? I feel like I need just a little more practice for today.\""
    mc 1 u sigh2 "\"No. You need to rest.\""
    mc 1 u sigh "\"Come on, you should know better than anyone that you won't get anywhere by practicing in this state.\""
    mc 1 u sigh2 "\"You'll just start making mistakes because of your condition and they'll end up sticking to you like a bad habit that is hard to get rid of. You're just hurting your own progress...\""
    show j 1 u wince at fdis
    "Once he hears those words, his shoulder drop and his gaze softens."
    j "\"... Damn it.\""
    "It seems I finally managed to get to him.\""
    j "\"I definitely don't want that to happen...\""
    mc 1 u sigh2 "\"Jeez, you can be so stubborn...\""
    mc 1 u avoid "\"That sort of attitude isn't always cute you know.\""
    show j 1 u considerate at fdis
    j "\"Hehehe...\""
    mc 1 u "\"Are you going to do as I say and head home now?\""
    show j 1 u wry at fdis
    j "\"I guess so..."
    show j 1 u considerate at fdis
    extend " There's no point arguing with you... you're even more stubborn than I am.\""
    mc 1 u smile "\"Damn right I am.\""
    play sound "music/disappointment.ogg"
    j "\"That's not something to be proud of you know...\""
    mc 1 u smile "\"If it gets you to rest then of course it is.\""
    mc 1 u "\"Do you need me to walk you to the doctor's office?\""
    show j 1 u wry at fdis
    j "\"There's no need. I'm just going to go home.\""
    mc 1 u shock "\"Home? But the doctor's office is a better place f-\""
    show j 1 u considerate at fdis
    j "\"It feels too much like a hospital... I can't relax in there.\""
    mc 1 u worried "\"I... I guess that's fair.\""
    mc 1 u "\"Do you need me to walk you home?\""
    show j 1 u wry at fdis
    j "\"Nah, it's alright. I kinda want to be alone with my thoughts.\""
    mc 1 u curious "\"Thoughts? Plural?\""
    show j 1 u annoyed at fdis
    j "\"Something wrong with that?\""
    mc 1 u fsmile "\"N-no no, not at all. Everything's fine. Just dandy. Hehehe...\""
    show j 1 u sigh at fdis
    j "\"If you say so...\""
    show j 1 u considerate at fdis
    j "\"Can I ask you to handle the cleaning of the room for me? Usually I'd take care of it every day after I've finished rehearsing but...\""
    mc 1 u smile "\"Of course. Leave it to me. I'll make sure this place is spotless so you can just relax.\""
    show j 1 u wry at fdis
    j "\"Thanks.\""
    "Jun picks up his bag and stands up, looking me up and down one final time."
    show j 1 u considerate at fdis
    j "\"I guess I'm gonna head home now.\""
    mc 1 u smile "\"I'll see you later. Get well.\""
    show j 1 u wry at fdis
    j "\"I will. Thank you.\""
    play sound "music/slidingdoor.ogg"
    show j 1 u wry at fdis, offscreenright with moveoridis
    "..."
    "I wonder if everything really is okay..."
    stop music fadeout 2.5
    stop music3 fadeout 2.5
    $ date = None
    jump cs_final
