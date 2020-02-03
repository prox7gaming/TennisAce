label Day14_Jun:
    window hide
    scene May22 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    play music2 "music/BGM/Dazzling Sunlight.ogg" fadein 5.0
    scene SClass with fade
    window show
    $ date = "day14"
    "I reach the door to my classroom, already panting and dripping with sweat."
    "I'd decided to leave the house an hour early so I could visit a store downtown and didn't expect the trains to have all stopped due to an accident just twenty minutes later."
    "In the end, I had to get a cab and then run half of the way here due to the traffic jam it creates."
    play sound "music/slidingdoor.ogg"
    mc 1 u wince "\"D-damn it... I'm finally here...\""
    play sound "music/fabric.ogg"
    "I slump onto my chair with no care as to how I look. All I want right now is to be able to sit somewhere and rest."
    "Goddamnit, why does Saitama have to be so big?"
    show j 1 u shock at fdis, five with dissolve
    j "\"... [povFirstName]-san?\""
    mc 1 u wince "\"Huh? Oh, hey. I didn't see you there when I got in.\""
    j "\"What happened? You're dripping in sweat. And why are you so late?\""
    mc 1 u sigh "\"I had to deal with a traffic jam...\""
    show j 1 u wince at fdis
    j "\"What? But you walk to school.\""
    mc 1 u considerate "\"Unfortunately I picked the worst possible day to run an errand before class.\""
    show j 1 u avoid at fdis
    j "\"Oh... that sounds really bad.\""
    mc 1 u considerate "\"Honestly, it was just some stupidity on my part. It was the kind of thing that totally could have waited until later but I decided to do it now and screwed up.\""
    mc 1 u "\"...\""
    mc 1 u curious "\"By the way... where is everyone else?\""
    "I notice that the class is more or less deserted right now. I only see a few of my classmates hanging around at the time. Not even the teacher is here."
    j "\"Uhm... yeah... do you even know what time it is?\""
    mc 1 u fsmile "\"The... time?\""
    "I hadn't bothered to check the time on my way over because I honestly didn't think it was taking me {i}that{/i} long."
    play sound "music/phonebeep.ogg"
    "Hesitantly, I reach into my bag and pick up my phone for what I'm sure will be a terrible realization..."
    mc 1 u shock "\"What?! It's lunch time already?!\""
    show j 1 u think at fdis
    j "\"How did you even manage to get here without noticing all the people walking through the hallways?\""
    mc 1 u wince "\"Ugh... I was in such a hurry that I didn't even think about it.\""
    show j 1 u considerate at fdis
    j "\"That sounds like a pretty careless thing to do.\""
    "I don't want to be hearing this kind of thing from you of all people."
    mc 1 u wince "\"There's barely any time for me to eat!\""
    show j 1 u watch at fdis
    j "\"I'd suggest you get to it.\""
    mc 1 u wince "\"Ugh... but I just ran to school. If I eat now I'll get sick.\""
    show j 1 u think at fdis
    j "\"Hmm{cps=1}...{/cps}{nw}"
    show j 1 u happy at fdis
    extend " Oh, I have an idea.\""
    show j 1 u smile at offscreenright with move
    "Jun walks away from me without another word."
    "He walks up to each of our classmates still in class, which at this moment is about five or so people, and quietly talks to them for a bit."
    "They all smile and nod something at him. One even gives him a thumbs up."
    "I have no idea what they're talking about though, as even with me straining my ears I still can't make out the words they're saying."
    show j 1 u happy at fdis, five
    j "\"Okay. Let's go!\""
    mc 1 u confused "\"Go? Go where?\""
    show j 1 u smile at fdis
    j "\"Just follow me. And bring your bag.\""
    mc 1 u confused "\"Erm... okay?\""
    stop music2 fadeout 2.5
    scene SRooftop
    show j 1 u happy at fdis, five
    with fade
    play sound "music/metaldoor.ogg"
    play music3 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    "Jun walks me to the roof with an incredibly self-satisfied smile on his face."
    j "\"Tada~\""
    mc 1 u confused "\"... I don't get it.\""
    show j 1 u smile at fdis
    j "\"You like it up here in the roof, right? So I thought bringing you here would be a good idea.\""
    mc 1 u sigh2 "\"Uhm... Jun, as much as I appreciate the gesture, that doesn't solve the problem of t-\""
    play sound "music/schoolbell.ogg"
    show j 1 u think at fdis
    $ renpy.pause(1.0)
    "..."
    mc 1 u sigh "\"That...\""
    show j 1 u happy at fdis
    j "\"Hehe. Way ahead of you.{nw}"
    show j 1 u smile at fdis
    extend " I talked to all of our classmates and explained your circumstances. They all agreed to say nothing to the teacher. Then when you come back to class you can just tell the story again and you won't get an absence.\""
    mc 1 u shock "\"Huh? That's your great idea?!\""
    show j 1 u watch at fdis
    j "\"Yeah. Why? Isn't it pretty clever?\""
    play sound "music/disappointment.ogg"
    "I expected nothing and yet I am {i}still{/i} disappointed."
    mc 1 u sigh "\"We passed by a ton of people on our way here remember? Do you really think all of them are from other classes?\""
    show j 1 u shock at fdis, jumping
    j "\"Ah!\""
    "He gasps dramatically at the realization."
    "Jeez, realize these things sooner..."
    show j 1 u wince at fdis
    j "\"Oh no... the only flaw in an otherwise perfect plan...\""
    "... I'm not even gonna bother coming up with a response to that."
    mc 1 u considerate "\"Well... I guess this is fine.\""
    show j 1 u shock at fdis
    j "\"It is?\""
    mc 1 u smile "\"I can try to hold onto the hope that no one from our class seeing me walk by noticed what happened.\""
    show j 1 u think at fdis
    j "\"Hmm... I guess that's one way to look at it.\""
    show j 1 u happy at fdis
    j "\"Maybe they'll just stay quiet because they don't want to get you in trouble.\""
    mc 1 u worried "\"The people I talk to regularly probably would. I can't say the same for the others though.\""
    show j 1 u pout at fdis
    j "\"You're the one who said to hold onto hope. Stop being so negative.\""
    mc 1 u avoid "\"Er... right, my bad.\""
    show j 1 u watch at fdis
    mc 1 u "\"By the way, it's not that I want to keep poking flaws on your \"otherwise perfect\" plan but... shouldn't {i}you{/i} be in class at least?\""
    show j 1 u happy at fdis
    j "\"Nope. I'm in the infirmary!\""
    "He said it with so much gusto and cheeriness that I almost don't want to ask the question that obviously comes to mind but..."
    mc 1 u sigh "\"Won't your disguise get found out when the teacher asks the school doctor if you were really there?\""
    show j 1 u think at fdis
    stop music3 fadeout 2.5
    j "\"Nah. They don't bother checking anymore. I'm in there way too often for them to check each and every time.\""
    mc 1 u shock "\"Wait, what? You are?\""
    show j 1 u shock at fdis
    $ renpy.pause (1.0)
    show j 1 u wince at fdis
    j "\"Uhm... err... kinda. I mean, it's not {i}that{/i} often. It's just that I have a weak constitution so my parents want me to get checked up often.\""
    "I know I'm kinda dense at times but... this excuse is downright insulting to me."
    "Especially with the stuff I've heard the past few days... there's just no way I can believe this."
    mc 1 u "\"Is that really why?\""
    show j 1 u avoid at fdis
    j "\"...\""
    "Jun looks away, not bothering to say anything."
    "If all he does is avoid my gaze then we can't even have a conversation at all."
    "This isn't even the first time he's done this. He always tries to avoid answering my questions about his health or his past."
    "It's reached a point where even I'm finding it obvious."
    menu:
        "Maybe I'll..."
        "Press him for information":
            play music2 "music/BGM/Sighs.ogg" fadein 5.0
            $ pressjun += 1
            "..."
            "All of this secret keeping is starting to annoy me."
            if pressjun >= 3:
                "No matter how many times I ask, he just gets more or more secretive. Never a concrete answer. Just avoiding the point entirely."
                "I'm tired of this."
                mc 1 u angry "\"Hey, I asked you a question!\""
                show j 1 u wince at fdis, jumping
                j "\"Ah...\""
                mc 1 u sigh2 "\"Come on, Jun, why do you avoid talking to me every time I ask? What's the big deal here? Haven't I opened up to you a lot since we first met? And yet every time I ask you a question you ignore me or change the subject.\""
                show j 1 u avoid at fdis
                j "\"That's not...\""
                mc 1 u angry "\"Yes it is. It's obvious to anyone who looks that you're hiding something. You're not as slick as you think you are!\""
                show j 1 u wry at fdis
                j "\"... I'm sorry.\""
                menu:
                    "Double down":
                        $ pressjun += 1
                        mc 1 u annoyed "\"Don't \"I'm sorry\" me. You're terrible at faking things. It's obvious you're hiding something from me.\""
                        show j 1 u wince at fdis
                        j "\"W-what? N-no.\""
                        mc 1 u judge "\"This isn't the first time, Jun. I tried to let it slide in the past thinking you'd tell me eventually. I also tried just asking and that got me nowhere either.\""
                        mc 1 u judge "\"What's so important that you can't seem to tell me? To tell us? Because we've all already gathered that you have some sort of medical problem and it sure as hell isn't just \"weak constitution\".\""
                        show j 1 u avoid at fdis
                        j "\"...\""
                        mc 1 u sigh "\"You're just gonna give me the silent treatment? What do I have to do to get you to be honest with me? Do I have to get on my knees and beg, is that it? Don't you trust me?\""
                        j "\"It's... it's not about trust...\""
                        mc 1 u judge "\"Whatever you say. Then don't mind me if I try to guess what it is the-\""
                        j "\"N-no. [povFirstName]-san pl-\""
                        if day5 == "jun":
                            mc 1 u judge "The first time I saw you having a problem, you were clutching your chest and having trouble breathing. You told me it was just a panic attack back then.\""
                        mc 1 u sigh2 "\"During the day of your competition, I also saw you having trouble breathing. You told me again back then that it was a panic attack.\""
                        show j 1 u wince at fdis
                        j "\"St-\""
                        mc 1 u sigh "\"I don't know anything about medical stuff but is it something like asthma? Because if that's the case then there's no reason for you to be ashamed and hiding it.\""
                        j "\"I don't-\""
                        mc 1 u judge "\"If it's not that then what is it? Is it a problem with your lungs? Maybe you have anxiety? I've heard there are a lot of problems for people that suffer from th-\""
                        show j 1 u cry at fdis
                        j "\"{size=+4}Stop!{/size}\"" with hpunch
                        "I'm startled by the sudden rising of his voice, stopping me as I'm mid sentence."
                        "Jun's head is hanging low and he's avoiding my gaze entirely."
                        "His small shoulders are quivering, which I initially take as anger on his part."
                        "... Then I notice the tiny droplets falling and my heart sinks."
                        j "\"I'm... I'm not... I'm normal... Just... stop... please.\""
                        "His voice is broken up by choking and tiny little sobs that sounds more like mews."
                        "The sight of him like this disarms me immediately and makes me realize just how much I've fucked up."
                        "I immediately try to think of a way to make things better."
                        "I try to reach out to him and attempt to give him a hug but he backs away from me immediately, shaking his head."
                        j "\"Don't...\""
                        "Being denied like this stings so much for some reason I can't even understand."
                        "My chest hurts so much right now, almost as if someone were squeezing my heart with a tight grip."
                        "My head is swimming in thoughts of self-reproach and self-loathing. So much so that I feel a deafening pounding going on at it."
                        "I can't even begin to think of words to make things better and yet my mind races in an attempt to catch up, looking for some way to salvage this situation."
                        mc 1 u worried "\"J-Jun, I-\""
                        show j 1 u considerate at fdis
                        j "\"I-it's alright...\""
                        "He dries his tears on the cuffs of his jacket, taking deep breaths in an attempt to stabilize himself."
                        j "\"I-I'm fine... so it's alright.\""
                        mc 1 u worried "\"Are you sure?\""
                        j "\"...{nw}"
                        show j 1 u avoid at fdis
                        extend " I... I should probably head back inside.\""
                        mc 1 u shock "\"Wha- You're leaving me?\""
                        show j 1 u considerate at fdis
                        j "\"You were right. I'd probably get caught if I tried to ditch class so it's better if I go back inside...{nw}"
                        show j 1 u wry at fdis
                        extend " Enjoy your lunch, [povFirstName]-san...\""
                        play sound "music/metaldoor.ogg"
                        show j 1 u considerate at fdis, offscreenright with moveoridis
                        "Before I can come up with anything to say, Jun scurries away and back into the building, leaving me staring at door with a slack jaw."
                        "I can feel myself choking whilst trying to think of something."
                        "I am acutely aware that I screwed things up just now..."
                        "I'm gonna have to come up with a way to properly apologize to him later."
                        "I consider going back inside too but I don't think he'd want me following him back, even if he is heading to class."
                        "With a great degree of hesitation, I pull my bag off my back and set it down on the floor, grabbing my lunchbox from inside."
                        "I'm treated to a very sad, lonely lunch where I can do nothing but think of ways to fix this situation later."
                        stop music2 fadeout 2.5
                        jump JunLeaves
                    "Back off":
                        stop music2 fadeout 2.5
                        play music3 "music/BGM/Kokyou no Yuuhi.ogg" fadein 5.0
                        "Just seeing the sad look on his face, I feel as if someone suddenly started squeezing my chest."
                        "I... I let my temper get the better of me for just a second but... I didn't want to have him make such a face to me."
                        "Crap, I'm an idiot for speaking without thinking first."
                        mc 1 u avoid "\"N-no... it's fine. I'm... sorry I yelled at you. I don't know what came over me.\""
                        show j 1 u considerate at fdis
                        j "\"It's okay... I get why you're upset. I'm being kinda unfair, aren't I? Hehe...\""
                        mc 1 u worried "\"No! I... I know everyone has something they would rather not talk about. I'm the one who's being unfair. Even I would hesitate to talk about some things so me asking you to do that is just...\""
                        mc 1 u avoidb "\"I'm sorry...\""
                        show j 1 u wry at fdis
                        j "\"It's fine. You don't have to apologize.\""
                        show j 1 u happy at fdis
                        j "\"See? I'm just fine!\""
                        "..."
                        "Even though he's smiling as if nothing happened, the corners of his mouth are twitching."
                        "This is just wrong. Seeing him trying to play things off like this hurts."
                        show j 1 u cshockb at fdis:
                            ease .2 zoom 1.5 xoffset -50 yoffset 230
                        play sound "music/fabric.ogg"
                        "Before the stunned tiger can react, I've enveloped him in a tight hug."
                        "Not even I know quite well why I just did it. My body decided on its own that I wanted to hug him."
                        j "\"Awawawawawa! W-what are you doing?\""
                        mc 1 u avoidb "\"Please don't do things like that, Jun.\""
                        show j 1 u shockb at fdis
                        j "\"Huh?\""
                        mc 1 u avoid "\"I'm sorry for making you uncomfortable and I get that you don't want me to feel bad about it but... please don't force yourself to smile in front of me. It's always so obvious when you do and it hurts so much to see.\""
                        show j 1 u avoid at fdis
                        j "\"Ah...\""
                        mc 1 u avoid "\"Even if you don't tell me what the things you're hiding are, can you please at least not lie to me about how you're feeling? If you're upset or hurting, I want to have the chance to make you feel better. I don't want you to hide it.\""
                        j "\"...\""
                        play sound "music/fabric.ogg"
                        show j 1 u wry at fdis:
                            ease .2 zoom 1.0 xoffset 0 yoffset 0
                        "The tiger gentle pushes me away from him, looking me in the eyes with a sad smile."
                        mc 1 u worried "\"Jun?\""
                        j "\"I understand...\""
                        show j 1 u avoid at fdis
                        j "\"I don't like making people worry about me... I feel like I'm placing a burden on them that they shouldn't be forced to deal with.\""
                        show j 1 u wry at fdis
                        j "\"I'm sorry for that...\""
                        mc 1 u sigh "\"... Again, I'm the one who's in the wrong here. Why are you apologizing?\""
                        j "\"Hehe... sorry, I just feel like I have to.\""
                        mc 1 u considerate "\"Stupid tiger.\""
                        show j 1 u wince at fdis, shake1
                        play sound "music/stab.ogg"
                        j "\"S-stupid?\""
                        mc 1 u smile "\"It's okay for you to be annoyed at me you know. You don't have to always be so mindful all the time.\""
                        show j 1 u considerate at fdis
                        j "\"I don't like feeling angry or annoyed. It doesn't feel good.\""
                        mc 1 u sigh2 "\"Jeez. And your kind were supposed to be predators?\""
                        show j 1 u wince at fdis
                        j "\"I don't think I'd be a very good predator. \"I'm sorry for hurting you, Mr. Deer. Here, let me go look for something to bandage your wound\".\""
                        mc 1 u happy "\"Oh God, I can totally imagine that happening.\""
                        show j 1 u happy at fdis
                        j "\"Hehehe.\""
                        "Jun's voice carries so softly through the air, even though it's no different than usual, to me it sounds like a soft, gentle melody."
                        "For some reason, I feel the urge to hug him again but being pushed away once is already enough for me."
                        mc 1 u worried "\"Once again... I'm really sorry for pushing you so much. I can't help but want to know but I shouldn't be making you uncomfortable either.\""
                        show j 1 u considerate at fdis
                        j "\"It's alright. For better of worse, this is the kind of thing I'd expect from you after all.\""
                        mc 1 u sigh "\"Oh, so you expect me to be a dick? Good to know.\""
                        show j 1 u happy at fdis
                        j "\"If the shoe fits~\""
                        mc 1 u pout "\"What? You're not supposed to agree with me.\""
                        j "\"Hehehe~\""
                        mc 1 u curious "\"Hey, Jun... Do you mind if I ask a question? Er... not related to that thing.\""
                        show j 1 u watch at fdis
                        j "\"What is it?\""
                        mc 1 u talk "\"I noticed when I got to class that you were alone. Had Saya and Shoichi already left by the time I arrived?\""
                        show j 1 u think at fdis
                        j "\"Oh, that.{nw}"
                        stop music3 fadeout 2.5
            elif pressjun == 2:
                "I click my tongue, feeling a wave of annoyance and anger surging."
                show j 1 u shock at fdis
                "I try to control myself as best as I can but before I notice it, I step closer to him."
                "I'm probably making a really ugly face right now because he looks so intimidated by me all of a sudden."
                "Somehow I manage to make an effort to curb my emotions even just a tiny bit, taking a few seconds to calm down slightly before speaking."
                mc 1 u annoyed "\"Just talk to me already, Jun!\""
                show j 1 u avoid at fdis
                j "\"I... I can't...\""
                mc 1 u sigh "\"Why not?\""
                show j 1 u considerate at fdis
                j "\"... I also can't tell you why.\""
                mc 1 u sigh "\"So it's okay for you to ask me to talk about me but if I do the same to you then I get the silent treatment?\""
                show j 1 u avoid at fdis
                j "\"That's not what I'm saying...\""
                mc 1 u sigh "\"Then what {i}are{/i} you saying?\""
                j "\"I... I can't say.\""
                mc 1 u angry "\"Why not?!\""
                j "\"[povFirstName]-san, please...\""
                "He looks away from me, his whole body shakes slightly. His eyes are beginning to redden and become moist."
                "Somehow, seeing him like that disarms me immediately."
                "I become incredibly aware of how I've just yelled at him and how aggressively I've come off."
                "My mind sets onto damage control mode as I try to figure out what I can do to make things better."
                mc 1 u worried "\"Shi- Jun, I'm sorry. I shouldn't have yelled. I...\""
                show j 1 u considerate at fdis
                j "\"It's... it's fine. Just... please, can we not talk about this? {size=-2}Please?{/size}\""
                "The way his voice breaks when he talks makes my chest break."
                "I awkwardly place a hand behind my neck, crossing my arms and looking away from him."
                "No matter what I do, I can't think of anything to say."
                mc 1 u avoid "\"I'm sorry...\""
                show j 1 u avoid at fdis
                "Those are the only words that come out when I speak."
                "I feel incredibly self conscious all of a sudden."
                "I put him on the spot. I grilled him about something he obviously didn't want to talk about and I was incredibly aggressive in doing so."
                "Even though this isn't the first time something like this has happened, I still didn't bother to respect his boundaries."
                "I let my curiosity get the better of me and that's inexcusable."
                "Jun too must be feeling very awkward because his eyes are glued to the floor, never even glancing my way."
                mc 1 u worried "\"Do you want me to leave?\""
                show j 1 u considerate at fdis
                "Somehow those words seem to get a response from him as he finally lifts his eyes up to look at me."
                j "\"Now that would just be silly wouldn't it? The reason we came up here in the first place was so you could have lunch and relax before going to class.\""
                "Yeah. \"Relax\". I handled that masterfully huh?"
                mc 1 u considerate "\"Boy did I screw that up then.\""
                show j 1 u wry at fdis
                j "\"...\""
                "Without answering, he merely looks at me with sad eyes."
                "I can already tell what they mean even if he doesn't say anything."
                "\"Yeah, you really did\" is what they say. But even then, Jun is just too nice to say those words out loud."
                "Unfortunately for him, his face betrays him every step of the way."
                mc 1 u considerate "\"So, uhm... weather sure is nice huh?\""
                show j 1 u considerate at fdis
                j "\"I guess?\""
                "Ugh, now I'm just making pointless chit-chat."
                "Why is it that at times like this I just seem to freeze up?"
                "Just say something interesting you dumbass!"
                mc 1 u worried "\"Jun, I-\""
                show j 1 u wry at fdis
                j "\"It's alright. I understand why you were upset... You don't have to apologize for it, just... please don't talk about this.\""
                mc 1 u wince "\"G-gotcha.\""
                stop music2 fadeout 2.5
                "He can be surprisingly frank sometimes..."
                "I kinda wish he were this way more often."
                mc 1 u curious "\"Uhm... Can I ask a question? Er... not related to this subject?\""
                show j 1 u avoid at fdis
                j "\"I... I guess. What is it?\""
                mc 1 u worried "\"I noticed when I got to class that you were alone. Had Saya and Shoichi already left by the time I arrived?\""
                show j 1 u think at fdis
                j "\"Oh, that."
                "His whole demeanor changes immediately when I bring up this subject."
                "The shift is so sudden that it gives me mood whiplash."
                j "\"Yeah...{nw}"
            elif pressjun == 1:
                mc 1 u sigh "\"Come on, Jun. I know you're hiding something from me.\""
                show j 1 u wince at fdis
                j "\"That's... that's not true.\""
                mc 1 u sigh "\"Come on, this isn't the first time. You're not exactly good at keeping secrets. You let a lot of minor comments slip all the time. Anyone could piece together the fact that something's up. Do you think I'm stupid or something?\""
                show j 1 u avoid at fdis
                j "\"What? No, of course not!\""
                mc 1 u confused "\"Then what? Can't you just tell me what it is? You really think my opinion of you is gonna change if you do? It's not as if it hasn't already become obvious that you have some sort of medical issue.\""
                j "\"...\""
                mc 1 u avoid "\"Come on, Jun. Please don't give me the silent treatment.\""
                j "\"I... I don't want to talk about this, please...\""
                "..."
                "I sigh, rubbing at the bridge of my nose and attempting to calm myself down."
                "Even though I know there's something being hidden, I can't know how major it is or isn't."
                "Not only that, I get the fact that everyone has things they don't want to speak off but..."
                "Ugh, my curiosity is burning up wanting to know what it is."
                "Not only that, I do feel a little insulted that he feels he can't open up to me about it."
                "But... I also know that demanding he tell me isn't what a friend should do."
                "If he's this uncomfortable with it, asking him further would just make things worse... and yet it's hard to control myself when I want to know this badly."
                mc 1 u sigh2 "\"Alright, fine. I'll leave it be for now. You do realize that at this point you've already all but confirmed that you {i}are{/i} hiding something though, right?\""
                show j 1 u considerate at fdis
                j "\"...\""
                stop music2 fadeout 2.5
                "He merely smiles sadly, not even looking at me properly."
                "I guess I really can't expect him to be forthcoming about it huh?"
                "I should just change the subject and try to avoid upsetting him even more."
                mc 1 u avoid "\"Can I ask a question not related to this subject?\""
                show j 1 u watch at fdis
                j "\"What is it?\""
                mc 1 u talk "\"I noticed when I got to class that you were alone. Had Saya and Shoichi already left by the time I arrived?\""
                show j 1 u think at fdis
                j "\"Oh, that.{nw}"
        "Leave him be":
            stop music2 fadeout 2.5
            "... At this point it's already pretty obvious that he's hiding something... but I don't think I should try to rip that information out of him."
            "I'll just give him some space until he feels comfortable talking about it on his own."
            mc 1 u curious "\"Can I ask a question?\""
            show j 1 u watch at fdis
            j "\"What is it?\""
            mc 1 u talk "\"I noticed when I got to class that you were alone. Had Saya and Shoichi already left by the time I arrived?\""
            show j 1 u think at fdis
            j "\"Oh, that.{nw}"
    play music3 "music/BGM/The People Here.ogg" fadein 5.0
    show j 1 u watch at fdis
    extend " They actually both texted me to tell me they wouldn't show up because they were busy. They said they also texted you before class even started but that you never even read it so they decided to message me instead.\""
    mc 1 u avoid "\"Oh... crap.\""
    show j 1 u think at fdis
    j "\"Yeah. Once I found out why you were late I kinda figured out why you never saw their messages.\""
    mc 1 u wince "\"Hang on a second, I should probably answer them and tell them why I didn't say anything sooner.\""
    show j 1 u happy at fdis
    j "\"That's probably a good idea, yeah.\""
    play sound "music/phonebeep.ogg"
    "I type a quick message to the two of them explaining why I didn't answer sooner and send it so they at least won't worry about me."
    "I know they won't read it until after class but I'd rather do it now so I won't forget later."
    mc 1 u curious "\"Did they say anything about why they didn't show up? There's nothing on the message talking about it.\""
    show j 1 u think at fdis
    j "\"Yeah. They didn't tell me at first either so I had to ask.{nw}"
    show j 1 u watch at fdis
    extend " They said their classes were working on their displays for the festival so they wouldn't be able to.\""
    mc 1 u talk "\"Really? Cause our class was doing no such thing.\""
    show j 1 u considerate at fdis
    j "\"Yeah. I'm actually a little worried because there hasn't been much work put into it at all so far.\""
    mc 1 u sigh2 "\"And the festival's in less than two weeks.\""
    show j 1 u think at fdis
    j "\"I sure hope we'll be able to put things together in time.\""
    mc 1 u sigh "\"Yeah... now that I think about it, the previous two years we only had a handful of people who actively worked on organizing the festival.\""
    mc 1 u avoid "\"Most of them are in class 3-A this year though.\""
    show j 1 u watch at fdis
    j "\"I guess it makes sense. If they're in advanced classes then that means they're usually gonna be more responsible.\""
    show j 1 u think at fdis
    j "\"But that's not really an excuse. Mizoguchi-san's 3-C is also working on it.\""
    mc 1 u sigh "\"... I guess that's true.\""
    "But then again, Saya is one of the people that loves the school festival and always puts a lot of work into preparing it... and I'm sure she'd intimidate anyone who tried to skimp out on work."
    mc 1 u considerate "\"I'm sorry you had to eat all by yourself today.\""
    show j 1 u watch at fdis
    j "\"It's alright. It was just a little boring, that's all.\""
    show j 1 u think at fdis
    j "\"I did talk to some of our classmates for a bit but they all eventually left to do other stuff. The ones who stayed behind were either already with friends or were people I didn't know at all.\""
    mc 1 u talk "\"I don't blame you. I've been with most of these people for three years and I don't know them all. You've only been here for a month and a half.\""
    show j 1 u considerate at fdis
    j "\"I guess so. It's still a little annoying.\""
    mc 1 u smile "\"What? Were you hoping to become one of those well connected, super popular types?\""
    show j 1 u think at fdis
    j "\"Me? Popular? Pfft, as if.\""
    mc 1 u "\"Jeez, you're surprisingly nonchalant in your self-deprecating.\""
    show j 1 u watch at fdis
    j "\"I'm just being honest. We both know I'm not very good with people.\""
    show j 1 u think at fdis
    j "\"Come to think of it, I don't even know why you guys stuck with me.\""
    "I suppose answering with \"Because you're cute\" would just make him embarrassed so I'll refrain from that."
    mc 1 u smile "\"You're pretty fun to hang around with and you actually try to take care of people when they get upset or depressed. Those aren't qualities to be overlooked.\""
    mc 1 u happy "\"In fact, you're one of the gentlest guys I've ever met.\""
    "Even if your hyper, bouncy personality still ends up giving me a headache every now and again."
    show j 1 u watch at fdis
    j "\"Really? I thought being nice and supportive was supposed to be common sense.\""
    mc 1 u considerate "\"Common sense, sadly, isn't as common as you'd think.\""
    show j 1 u wince at fdis
    j "\"That {i}is{/i} pretty sad.\""
    mc 1 u smile "\"Hey, despite what you said, you've been able to make friends with some people outside of just our group. It's not like you're always bound to us.\""
    show j 1 u think at fdis
    j "\"I guess... most of those people already have groups of their own though so I can't go to them when you guys aren't around.\""
    mc 1 u talk "\"What about Che- I mean, Victor? I don't see him hanging out with the same people all the time.\""
    show j 1 u watch at fdis
    j "\"Oh yeah. He's much more of a social butterfly than I am. He's pretty much on good terms with everyone.\""
    show j 1 u think at fdis
    j "\"We talked for a bit but he eventually left to have lunch with a friend from another year. Didn't say who.\""
    mc 1 u confused "\"... Huh. I wasn't expecting that. Usually people from different years don't mingle outside of after class hours.\""
    j "\"Yeah, I noticed that too. It's the one thing I miss about my old school. People used to walk around freely through campus and just talk to each other all they wanted.\""
    mc 1 u smile "\"That sounds pretty interesting. I wish we could do stuff like that at our school too. What was it like there?\""
    show j 1 u wince at fdis
    j "\"Oh... not very pleasant to be honest.\""
    mc 1 u worried "\"Really? Why not?\""
    show j 1 u considerate at fdis
    j "\"I never really managed to adjust there. I studied at that school for five years and I never really made any friends there.\""
    show j 1 u avoid at fdis
    j "\"And since it was at another town, I was away from my family and old friends. I felt really lonely most of the time. The only thing I had to cheer me up back there was the piano.\""
    mc 1 u shock "\"Really? You were there for five years and you never made any friends? I find that a little hard to believe. You fit in so easily over here!\""
    show j 1 u considerate at fdis
    j "\"I think you're not taking into account how big of an influence you were to that, [povFirstName]-san...\""
    mc 1 u avoid "\"Me? What did I do?\""
    show j 1 u wry at fdis
    j "\"You reached out to me. When I just came to this school, you introduced yourself to me, you talked to me, you introduced me to your friends. It was through you that I befriended all of the people in school.\""
    show j 1 u considerate at fdis
    j "\"If you weren't here for me, I'd be just as lonely here as I was back there.\""
    "I'm caught by surprise, unable to think of any words to say in response."
    "I feel like I should say something encouraging... but any words I think of just get caught in my throat, unable to come out."
    j "\"Sorry. I kinda brought down the mood huh?\""
    mc 1 u wince "\"What? No, don't be ridiculous. I'm not feeling down. I just... wish there was something I could say or do to make you feel better.\""
    show j 1 u happy at fdis
    j "\"Hehe. You don't have to worry about that. You've already helped me so much. You have no idea how much I owe you, [povFirstName]-san.\""
    show j 1 u smile at fdis
    j "\"I don't know what your point of view on me is, but I'm being absolutely honest when I say that you're the only reason I've managed to do so well here.\""
    show j 1 u happyb at fdis
    j "\"You're the best thing that's happened to me since I transferred here. It makes me really happy to have come to this school when I think about it.\""
    play sound "music/heartbeat.ogg"
    "My cheek starts growing hot when I hear him shower so much praise onto me. I feel an urge to look away in embarrassment but still I force myself to look him in the eye."
    "Jun has such a wonderful face... I can't help but notice that when he's smiling so happily like this."
    "I want to protect this smile of his... I don't know when I started thinking this way but right now that's the only thing I can think of."
    play sound "music/tap.ogg"
    show j 1 u shockb at fdis
    "Jun is caught by surprise when I place my hand on the top of his head, gently brushing his fur with my fingertips and petting his ears."
    mc 1 u happyb "\"It makes me really happy to hear that. I just hope you don't eventually find yourself so popular that you end up leaving me. Hahaha.\""
    show j 1 u poutb at fdis
    j "\"There's no way something like that would happen!\""
    mc 1 u smile "\"What? You getting popular or you leaving?\""
    show j 1 u blush2 at fdis
    j "\"... Now you're just making fun of me.\""
    mc 1 u happyb "\"Hahaha. Sorry sorry. It's just that you're so cute I can't resist.\""
    j "\"I wish you wouldn't call me that... that makes me sound like I'm either a girl or really small...\""
    mc 1 u think "\"{i}Well{/i}...\""
    show j 1 u poutb at fdis
    j "\"Stop making fun of me!\""
    mc 1 u happy "\"Hahaha. Sorry sorry sorry. I swear I'll stop now!\""
    show j 1 u blush2 at fdis
    j "\"Jeez...\""
    "Even though he's saying all these things, he makes no effort to move away from my hand as I continue to pet his head."
    "In fact, I can even notice his tail swaying contently from side to side as I continue to fawn over him."
    mc 1 u happyb "\"{size=-4}I'm also really glad you transferred here...{/size}\""
    show j 1 u watch at fdis
    j "\"Did you say something?\""
    mc 1 u smile "\"Nope, not at all.\""
    "I stroke his fur one last time and pull my hand back, having already had my fun with him."
    show j 1 u shockb at fdis
    j "\"Ah...\""
    mc 1 u "\"Hm? Is something up?\""
    show j 1 u blush2 at fdis
    j "\"N-no, it's nothing.\""
    "I pick up on what he's thinking almost immediately. A devious smile creeps up my face when I realize what it is."
    mc 1 u suggestive "\"Don't tell me... could it be that you wanted me to continue petting you?\""
    j "\"I-I don't know what you're talking about!\""
    "Jeez, so quick to deny."
    "Too bad you're so damn transparent."
    mc 1 u smile "\"Oh, is that so? Too bad. I might have done if for a bit longer if that was the case.\""
    show j 1 u shock at fdis
    j "\"Ah...\""
    "The look on his eyes is a mixture of both surprise and disappointment. It takes every ounce of self control I have to not burst out laughing at the sight of it."
    "I'm sorry Jun. I know I said I'd stop teasing you but it's just so damn fun."
    "Crap, I better change subjects right now. My sadistic side is starting to show..."
    mc 1 u think "\"Now that I think about it, we initially came up here so I could have lunch didn't we?\""
    show j 1 u think at fdis
    j "\"Oh yeah, that's true.\""
    mc 1 u considerate "\"Would you mind if I got to it?\""
    show j 1 u happy at fdis
    j "\"Not at all. Please do!\""
    mc 1 u happy "\"Thank you. I'm starving!\""
    "..."
    "I'd never say this out loud to you, but..."
    "Even though you haven't been here for long, I really can't imagine my days without you in them anymore, Jun."
    stop music3 fadeout 2.5
    scene SClass with dissolve
    play sound "music/schoolbell.ogg"
    "In a surprising twist of fate, I actually ended up having a pretty productive day in class despite earlier setbacks."
    "By the time the final bell rang for the end of class today, I had managed to catch up on everything I missed earlier."
    "Luckily enough, neither Jun nor I got into any trouble for ditching an entire period."
    "Guess our class has my back after all. It's kinda nice to know."
    show j 1 u watch at fdis, five with dissolve
    "Jun is absent-mindedly packing his books back in his bag, not really bothering to organize them whatsoever."
    mc 1 u smile "\"Hey, Jun, what are you planning on doing today?\""
    show j 1 u think at fdis
    play music2 "music/BGM/On My Way.ogg" fadein 5.0
    j "\"Hmm... I'm not really sure to be honest.\""
    mc 1 u smile "\"Not gonna practice?\""
    show j 1 u wince at fdis
    j "\"Err... I think I'm gonna take a break for today. I've been stressing out over practice too much lately.\""
    mc 1 u happy "\"Not a bad idea at all. It's good to take a break so you don't burn out.\""
    show j 1 u watch at fdis
    mc 1 u smile "\"How about we head somewhere together?\""
    j "\"Like where?\""
    mc 1 u think "\"Hmm... I'm not quite sure. We could see if the others are free and go somewhere all of us.\""
    show j 1 u think at fdis
    j "\"That still doesn't answer the \"where\" part though.\""
    mc 1 u happy "\"We'll worry about that when we get to it.\""
    show j 1 u bored at fdis
    j "\"And I'm the one who gets called an airhead...\""
    mc 1 u wince "\"Wha- hey! You know, you can be surprisingly sharp-tongued sometimes.\""
    show j 1 u happy at fdis
    j "\"Whatever do you mean?\""
    "Yeah yeah, play cute all you want. I'm onto you!"
    show j 1 u watch at fdis
    j "\"But yeah, I'm free if you'd like to set something up.{nw}"
    show j 1 u think at fdis
    extend " Though I'm not exactly sure if the others would be too. They might still be busy working on stuff for the festival.\""
    mc 1 u considerate "\"It's after class. I'm sure they wouldn't have things to do then, right?\""
    show j 1 u watch at fdis
    j "\"You say that but we haven't actually hung out as a group in a while because our free time never matches up.\""
    mc 1 u wince "\"I guess that's true... We did all find time to visit you together in the hospital though.\""
    show j 1 u think at fdis
    j "\"Well... yeah. It's a hospital visit, not a group outing. It goes a little higher on people's priority list.\""
    mc 1 u sigh "\"You're being surprisingly negative here all of a sudden.\""
    show j 1 u watch at fdis
    j "\"I'm just telling you not to get your hopes up.\""
    "... This coming from the person that tends to have unreasonable ideas about activities all the time."
    "Yeah, no, I'm not taking you seriously here. Sorry not sorry."
    play sound "music/message.ogg"
    "Just then, my phone rings inside my pocket."
    "I reach inside to grab it, seeing that Shoichi has replied to my earlier message."
    mc 1 u talk "\"Oh, Shoichi's asking if we're free right now.\""
    show j 1 u think at fdis
    j "\"I guess now that class is over he could finally read your message huh?\""
    mc 1 u considerate "\"Yup. I would never expect him or Saya to be playing with their phones during class. It's just not something they'd do.\""
    show j 1 u wince at fdis
    j "\"How do they not get bored?\""
    mc 1 u smile "\"I'm pretty sure they do. They're just better at controlling themselves than we are.\""
    show j 1 u pout at fdis
    j "\"Boooo.\""
    mc 1 u sigh "\"{size=-2}Who are you even booing?{/size}\""
    play sound "music/message.ogg"
    mc 1 u talk "\"Oh, hang on a sec. Let me see... Yup, he's asking us if we want to hang out.\""
    show j 1 u happy at fdis
    j "\"I've missed hanging out with everyone.\""
    mc 1 u smile "\"Oh come on, it hasn't even been that long.\""
    show j 1 u think at fdis
    j "\"Maybe to you cause you're used to it. I haven't had friends to hang out with for years so I look forward to it every time.\""
    mc 1 u considerate "\"Point taken.\""
    show j 1 u watch at fdis
    j "\"I wonder if anyone else is gonna be coming along.\""
    mc 1 u "\"I'm not sure. Shoichi didn't say anything about that. We'll just have to meet him and see.\""
    show j 1 u think at fdis
    j "\"By the way, where are we meeting him?\""
    mc 1 u smile "\"At the gate. You all done packing your bag?\""
    show j 1 u happy at fdis
    j "\"Yup.\""
    mc 1 u smile "\"Let's not keep him waiting then.\""
    scene SGate
    show j 1 u smile at fdis, five
    with fade
    "We get to the gate to see that there's no one there yet."
    j "\"Guess we're the first ones here.\""
    mc 1 u "\"Maybe Shoichi is still trying to call someone else?\""
    show j 1 u think at fdis
    j "\"Or he just had some things to deal with after class first.\""
    mc 1 u "\"Nah, he'd have told me if that were the case. He's not the kind of guy that leaves people waiting.\""
    show j 1 u watch at fdis
    j "\"Hmm... I guess you're right.\""
    "Just then, we see Shoichi's figure running up to us and cutting through a group of other students."
    show j 1 u watch at fdis, three with move
    show s 1 u smile at fdis, seven
    show sguniform at seven
    with moveiridis
    s "\"Hey there. Did I leave you guys waiting for too long?\""
    show j 1 u smile at fdis
    j "\"No. We just got here too.\""
    show s 1 u considerate at fdis
    s "\"I'm glad to hear. Sorry I didn't show up for lunch today, Jun-kun. I hope Saya at least managed to keep you company.\""
    show j 1 u think at fdis
    j "\"She was busy too so I was by myself today.\""
    show s 1 u wince at fdis
    s "\"O-oh... I'm so sorry about that.\""
    show j 1 u smile at fdis
    j "\"It's not like you have to apologize for that. It's not a big deal.\""
    show s 1 u sigh at fdis
    s "\"Maybe not to you but I don't like canceling on people all of a sudden like that.\""
    show j 1 u think at fdis
    j "\"It's not like us having lunch together is some sort of appointment you've set up.\""
    s "\"Point taken.\""
    show j 1 u watch at fdis
    show s 1 u at fdis
    mc 1 u fsmile "\"Uhm... not to be an ass and interrupt the conversation but... Shoichi, since when did you wear glasses?\""
    show s 1 u think at fdis
    s "\"... Oh, right, I forgot to take these off.\""
    show s 1 u at fdis
    hide sguniform with dissolve
    s "\"Dad ordered these for me when he was in Taiwan. Apparently the family optometrist said I needed reading glasses because I was forcing my eyes too much.\""
    show j 1 u shock at fdis
    j "\"I didn't even notice them until [povFirstName]-san pointed them out.\""
    "That's just cause you don't pay attention."
    show j 1 u watch at fdis
    mc 1 u considerate "\"It stood out to me right away. I've never seen you in glasses before.\""
    show s 1 u think at fdis
    s "\"Hmm... is that so? I didn't think I looked bad in them.\""
    mc 1 u "\"I'm not saying that either. Just that I'm not used to seeing you like that.\""
    show s 1 u smile at fdis
    s "\"Fair enough. They're pretty comfortable to wear though so I forget to take them off sometimes.\""
    j "\"Do you even have to take them off?\""
    show s 1 u think at fdis
    s "\"I mean... they're {i}reading{/i} glasses. There's no point in wearing them when I'm not reading... unless I'm making a fashion statement.\""
    mc 1 u "\"Doesn't that also mean there's no reason {i}not{/i} to wear them?\""
    show s 1 u at fdis
    s "\"Maybe, but at that point I think we're just overthinking things.\""
    show s 1 u think at fdis
    s "\"By the way, I also invited Saya-chan and Urushihara. They shouldn't take much longer.\""
    j "\"Any idea where you want us to go?\""
    show s 1 u smile at fdis
    s "\"I was thinking of going to this place in town that makes oden. I've been craving it for a while.\""
    mc 1 u "\"Don't people usually eat that in winter?\""
    s "\"Sure, but that doesn't mean I can't have it the rest of the year.{nw}"
    show s 1 u happy at fdis
    extend " Besides, the weather's a little chilly today so I thought it'd be perfect.\""
    mc 1 u think "\"I guess that's true.\""
    show j 1 u wince at fdis
    j "\"Uhm... is this place gonna be particularly expensive?\""
    show s 1 u think at fdis
    s "\"Well... it's not the cheapest place around but it's not really expensive either. The prices are pretty normal.\""
    show s 1 u smile at fdis
    s "\"I was already planning on treating you though so you don't have to worry about that.\""
    show j 1 u pout at fdis
    j "\"Of course I'm gonna worry about that. I don't want to have people paying for me all the time.\""
    mc 1 u smile "\"How about you let me handle it then?\""
    show j 1 u wince at fdis
    j "\"... I'm still not sure.\""
    mc 1 u happy "\"Think of it as repayment for bailing me out of class so I could actually eat.\""
    show j 1 u think at fdis
    j "\"... If you're sure about it.\""
    show j 1 u watch at fdis
    show s 1 u sigh at fdis
    s "\"How come you agree to it so readily when it's [povFirstName] offering?\""
    show j 1 u considerate at fdis
    j "\"Sorry... It just doesn't feel that wrong if it's [povFirstName]-san...\""
    show s 1 u annoyed at fdis
    s "\"Hmm...\""
    show j 1 u shock at fdis
    mc 1 u "\"What?\""
    show s 1 u sigh at fdis
    s "\"No, it's nothing.\""
    show j 1 u wince at fdis
    j "\"Shoichi-san, you just made a really scary face just now.\""
    s "\"Just forget it...\""
    mc 1 u confused "\"Jeez, if there's something bothering you then just say it.\""
    s "\"I already said it's nothing.\""
    mc 1 u sigh "\"Y-{fast}"
    show j 1 u watch at fdis, one
    show s 1 u sigh at fdis, four
    with move
    show k 1 u sigh at fdis, eight
    show sa 1 u sigh at fdis, ten
    with moveiridis
    "Just then, the sound of sighing echoes from behind me, making me suddenly jump in surprise."
    j "\"Oh, hey guys. What's with the long face, Keisuke-san.\""
    show k 1 u at fdis
    show sa 1 u at fdis
    "Keisuke takes a good look at us, his eyes immediately snapping to Shoichi's face."
    k "\"You know, I could ask the same about him.\""
    s "\"Please don't.\""
    show k 1 u sigh at fdis
    k "\"Fine fine. Anyway, I'm having trouble dealing with my class and getting them to focus on the preparations for the festival.\""
    show sa 1 u annoyed at fdis
    sa "\"I'm having the same problem myself. We just came from the school building talking about it.\""
    show sa 1 u sigh at fdis
    "The two sigh in tandem."
    show s 1 u at fdis
    show sa 1 u bored at fdis
    s "\"I guess that's the one problem I can't say I'm having.\""
    show k 1 u at fdis
    sa "\"Well duh. Look at what class you're in. All of our responsible classmates are studying with you.\""
    show s 1 u think at fdis
    s "\"Not all of them. There's quite a few that stayed in 3-B and 3-C.\""
    show s 1 u at fdis
    mc 1 u "\"Only the ones that either didn't fulfill the academic requirements or chose not to. Which at this point amounts to two or three people.\""
    show sa 1 u sigh at fdis
    sa "\"You got lucky too, [povFirstName]. You got both Aya-chan and Kyo-chan in the same class as you.\""
    "Jun and I both share a look that basically asks \"Do you want to tell her or should I?\"."
    j "\"Actually, our class hasn't even begun preparations for the festival yet.\""
    show k 1 u uncomfortable at fdis
    show s 1 u smile at fdis
    show sa 1 u shock at fdis
    k "\"Seriously?\""
    s "\"Man, you guys have a lot of courage to be postponing it so much.\""
    show sa 1 u complain at fdis
    sa "\"Or they're just really stupid.\""
    show s 1 u happy at fdis
    show k 1 u sigh at fdis
    show j 1 u avoid at fdis
    s "\"Yeah, I guess that does sound more likely.\""
    show sa 1 u at fdis
    k "\"Talk about irresponsible.\""
    j "\"To be honest, I'm not really comfortable with either but no one seems to be in any hurry to get anything done.\""
    show s 1 u smile at fdis
    show k 1 u at fdis
    show j 1 u watch at fdis
    s "\"Wasn't Ayako-chan testing out recipes for her festival idea back in April already?\""
    mc 1 u talk "\"She was, but after literally no one voted for her suggestion she just pouted and stopped caring.\""
    show s 1 u sigh at fdis
    s "\"Uwah, that's not the sort of behavior you'd expect out of a class leader.\""
    "I shrug."
    mc 1 u considerate "\"I've more or less already accepted the fact that our class' display will be a disaster.\""
    show s 1 u think at fdis
    s "\"You say that but I have serious doubts that you're doing any work to help either.\""
    mc 1 u frownj "\"Hey!\""
    show j 1 u think at fdis
    show k 1 u sigh at fdis
    j "\"He isn't.\""
    show j 1 u happy at fdis
    mc 1 u flustered "\"W-wha- Jun, don't just turn me in like that.\""
    show j 1 u watch at fdis
    k "\"Of course he isn't. If you thought for ever a second that he would be doing work then you're just really naive.\""
    show s 1 u smile at fdis
    show j 1 u watch at fdis
    show k 1 u at fdis
    show sa 1 u laugh at fdis
    mc 1 u pout "\"You guys are all awful.\""
    k "\"Sorry but we're not the ones slacking off. I'm actually working my butt off to try and get my class to do something presentable.\""
    mc 1 u sigh "\"Yeah yeah. Elitist...\""
    show s 1 u sigh at fdis
    show sa 1 u at fdis
    show k 1 u sigh2 at fdis
    k "\"What part of what I just said makes me elitist?\""
    s "\"[povFirstName], you don't get to call someone elitist just because they called you out on being lazy.\""
    mc 1 u avoid "\"Jeez, what is this, an inquisition?\""
    show j 1 u think at fdis
    j "\"If you don't want the heat to fall down onto you then don't try to act like you're innocent in this.\""
    mc 1 u sigh "\"What happened to the meek, mild-mannered Jun that wouldn't just casually give me sass out of nowhere?\""
    show j 1 u watch at fdis
    show s 1 u smile at fdis
    show k 1 u smile at fdis
    show sa 1 u happy at fdis
    sa "\"Don't listen to him, Jun-kun. Keep treating him like that. Maybe then he'll learn!\""
    mc 1 u sigh "\"Devil woman.\""
    show sa 1 u pout at fdis
    sa "\"Better than a lazy bum.\""
    show sa 1 u at fdis
    show j 1 u think at fdis
    show k 1 u at fdis
    j "\"Uhm... maybe we should get going? There's no point hanging around by the school gate.\""
    k "\"Why the hurry? It's not even 4PM. Dinner's not until a couple hours at least.\""
    show j 1 u considerate at fdis
    j "\"I know that but I'd rather be doing something other than hanging around by the gate.\""
    show s 1 u at fdis
    show j 1 u watch at fdis
    s "\"Well, neither of us has club activities today so we don't really need to hang around school until then.\""
    show k 1 u eyesc at fdis
    k "\"Perhaps, but we also don't have any other places to go to.\""
    s "\"That's also a fair point.\""
    show sa 1 u happy at fdis
    sa "\"Ooh, how about we play some card games for an hour or so.\""
    show k 1 u at fdis
    "Everyone" "\"Pass.\""
    show sa 1 u pout2 at fdis, jumping
    sa "\"What? Why not?!\""
    show s 1 u sigh at fdis
    show k 1 u considerate at fdis
    show j 1 u think at fdis
    s "\"You're kidding, right? You always get mad when you start losing.\""
    k "\"Saya-san... you're kinda the definition of sore loser.\""
    j "\"You yelled at me the last time we tried to play I Doubt It.\""
    mc 1 u sigh "\"Forget yelling. You always punch my shoulder when you get upset in a game.\""
    show sa 1 u pout2b at fdis
    "Saya looks down at the floor, her cheeks suddenly slightly tinted red."
    sa "\"W-well... I mean, I get a little annoyed because of all the RNG...\""
    s "\"That's an understatement.\""
    show sa 1 u poutb at fdis
    sa "\"Well, do any of you guys have some sort of brilliant suggestion then?!\""
    show j 1 u watch at fdis
    show s 1 u at fdis
    show k 1 u at fdis
    show sa 1 u at fdis
    s "\"We could just go around town and window shop.\""
    show k 1 u sigh at fdis
    k "\"We do that all the time already. Can't we pick something a little more involved?\""
    show s 1 u smile at fdis
    s "\"Sure. Wanna paint my house?\""
    show k 1 u scorn at fdis
    k "\"I said \"more involved\", not \"slave labor\".\""
    show j 1 u think at fdis
    j "\"Keisuke-san, I don't think you've got a good grasp on the concept of slave labor you're comparing that to painting a house...\""
    show k 1 u avoid at fdis
    show s 1 u seductive at fdis
    k "\"Oh shut up. I was using a hyperbole.\""
    s "\"Sure you were.\""
    mc 1 u talk "\"How about we go bowling? It's been a long time since we last did.\""
    show s 1 u smile at fdis
    show k 1 u at fdis
    show j 1 u wince at fdis
    s "\"That could work.\""
    j "\"I've never played bowling before. Isn't it expensive?\""
    mc 1 u smile "\"Not all that much. But I can just pay for your share.\""
    j "\"Are you sure?\""
    mc 1 u laugh "\"Absolutely. It's more fun with more people anyway.\""
    k "\"This does give us a chance to get some nice competition going too.\""
    mc 1 u smile "\"For sure. We can have fun just trying to outdo one another.\""
    show sa 1 u laugh at fdis
    sa "\"Yeah. You can also egg them on so they get frustrated and lose!\""
    show j 1 u wince at fdis
    show k 1 u uncomfortable at fdis
    show s 1 u at fdis
    k "\"Saya-san, that's kind of a scary thing to say...\""
    j "\"I don't think you should do that...\""
    mc 1 u sigh "\"Devil woman...\""
    show sa 1 u pout at fdis
    sa "\"Stop calling me that!\""
    "Shoichi clears his throat, making an \"ahem\" sound to catch our attention."
    show s 1 u smile at fdis
    show sa 1 u at fdis
    show k 1 u at fdis
    show j 1 u watch at fdis
    s "\"I think bowling sounds like a fun way to kill time before dinner. Is anyone against the idea?\""
    show j 1 u happy at fdis
    show k 1 u smile at fdis
    j "\"I think it sounds really fun!\""
    k "\"Agreed.\""
    show sa 1 u happy at fdis
    sa "\"So long as I get to kick someone's butt in a game, I'm happy.\""
    show j 1 u think at fdis
    j "\"And if you don't, you'll probably kick [povFirstName]-san in real life anyway.\""
    show sa 1 u laugh at fdis
    sa "\"I like the sound of that!\""
    mc 1 u sigh "\"I don't!\""
    stop music2 fadeout 2.5
    scene Bowling
    show j 1 u happy at fdis, one
    show s 1 u smile at fdis, four
    show k 1 u smile at fdis, eight
    show sa 1 u smile at fdis, ten
    with fade
    play music3 "music/BGM/Hanging Out.ogg" fadein 5.0
    "Arriving at the bowling alley, we walk up to the front counter to set up a game as well as rent some shoes."
    "Man, it's been a while since I've been here. The place feels so much cozier now."
    j "\"Waaaaah, it feels so nice in here!\""
    s "\"Say thank you to the air conditioning for giving us such a comfortable environment.\""
    show j 1 u gentle at fdis
    j "\"Thank you, Air Con-san!\""
    show s 1 u sigh at fdis
    s "\"Erm... I didn't mean it literally though.\""
    show k 1 u at fdis
    show s 1 u at fdis
    k "\"If I'd known we'd be coming to a bowling alley I'd have bought bowling shoes for myself.\""
    show j 1 u watch at fdis
    j "\"What's wrong with the rental shoes?\""
    show k 1 u sigh at fdis
    k "\"I don't like the idea of shoving my feet into a used shoe.\""
    show s 1 u seductive at fdis
    s "\"You don't like anything.\""
    show k 1 u at fdis
    k "\"That's not true. I like you... as hard as it is for me to believe.\""
    show s 1 u sigh at fdis
    s "\"Wait, why is it hard to believe? We're friends goddamnit.\""
    show k 2 u gentle at fdis
    k "\"Pfft... don't take it so seriously. I was just joking.\""
    s "\"Somehow I have difficulty believing that...\""
    show j 1 u shock at fdis
    show k 1 u smile at fdis
    show s 1 u at fdis
    j "\"Waaah, there are so many balls in here. And they're so shiny!\""
    show sa 1 u think at fdis
    sa "\"Well... yeah. You do need balls to bowl after all.\""
    show s 1 u happy at fdis
    s "\"Yup. That's why Saya-chan is so good at it!\""
    show sa 1 u doom2 at fdis
    sa "\"Shall I cut {i}your{/i} balls off and use them to bowl instead?\""
    play sound "music/stab.ogg"
    show j 1 u watch at fdis
    show k 1 u sigh at fdis
    show s 1 u wince at fdis, shake1
    s "\"Woah, scaaary...\""
    k "\"You just had to poke the hornet's nest didn't you?\""
    show sa 1 u at fdis
    show k 1 u at fdis
    show j 1 u considerate at fdis
    show s 1 u at fdis
    j "\"I just realized that I didn't even blink to a threat of extreme violence and that worries me a bit...\""
    mc 1 u considerate "\"Yeah, sorry... this means that you're officially one of us.\""
    show j 1 u avoid at fdis
    show k 2 u gentle at fdis
    show s 1 u laugh at fdis
    j "\"I suddenly feel conflicted...\""
    show j 1 u watch at fdis
    show k 1 u smile at fdis
    show s 1 u smile at fdis
    mc 1 u talk "\"How do we decide the playing order?\""
    show sa 1 u laugh at fdis
    sa "\"How about a coin toss?\""
    show s 1 u sigh at fdis
    s "\"We're five people in here you know. Think of how many tosses that would take.\""
    show sa 1 u think at fdis
    sa "\"Hmm... fair enough.\""
    show k 1 u at fdis
    show sa 1 u at fdis
    k "\"We could just use an app to shuffle our names on the phone and get the playing order from that.\""
    show j 1 u shock at fdis
    show s 1 u think at fdis
    j "\"Phones can do that? So cool!\""
    s "\"Oh yeah. The wonders of modern technology.\""
    show s 1 u happy at fdis
    show j 1 u think at fdis
    mc 1 u sigh "\"Don't mock him, Shoichi.\""
    j "\"I was being mocked?\""
    s "\"See? No harm done.\""
    play sound "music/disappointment.ogg"
    "Ugh, this guy..."
    show s 1 u smile at fdis
    show j 1 u watch at fdis
    k "\"Here, just a sec. I'm gonna play the randomizer button now.\""
    show sa 1 u happy at fdis
    sa "\"Alright!\""
    show j 1 u wince at fdis
    show sa 1 u at fdis
    j "\"Shouldn't someone explain the rules to me first?\""
    s "\"No need to worry about that so much. You just throw the ball and score points. The machine will calculate your points automatically so you don't have to think about it too much.\""
    show j 1 u think at fdis
    j "\"Oh... alright.\""
    show j 1 u watch at fdis
    show s 1 u happy at fdis
    mc 1 u sigh "\"You're just saying that because you're too lazy to explain the rules to him aren't you?\""
    s "\"I don't know what you mean.\""
    show s 1 u smile at fdis
    show k 1 u smile at fdis
    k "\"Alright, I've got the playing order. It'll go like this: Saya-san, Urata, Kobayashi-kun, [povFirstName]-san and me.\""
    show k 1 u sigh at fdis
    k "\"... Wait, why am I dead last?\""
    show s 1 u happy at fdis
    s "\"Now here's a playing order I can get behind.\""
    k "\"Rats.\""
    show s 1 u smile at fdis
    show k 1 u at fdis
    s "\"Saya-chan, could you please get us started?\""
    show sa 1 u laugh at fdis
    sa "\"Of course! Time to kick this game into high gear!\""
    show s 1 u think at fdis
    mc 1 u wince "\"Why does hearing her say that fill me with dread?\""
    s "\"Let's just hope \"high gear\" doesn't mean opening a hole on the ceiling with the ball.\""
    show sa 1 u pout at fdis
    sa "\"Hey, that only happened once!\""
    show s 1 u happy at fdis
    show k 1 u sigh at fdis
    show j 1 u shock at fdis
    j "\"Wait, something like that actually happened?!\""
    k "\"Oh yeah, it happened...\""
    show j 1 u watch at fdis
    show s 1 u smile at fdis
    mc 1 u talk "\"Didn't you end up paying for the repairs, Kei-kun?\""
    show k 1 u at fdis
    k "\"I did. The fact that that didn't clue you into my family status scares me to this day.\""
    mc 1 u considerate "\"Hehe... sorry.\""
    show sa 1 u laugh at fdis
    sa "\"Time to get started on this bitch!\""
    show k 1 u uncomfortable at fdis
    k "\"Saya-san, please watch your language. We're in public here...\""
    show k 1 u worried at fdis
    show sa 1 u think at fdis
    sa "\"Yeah yeah, whatever.\""
    show sa 1 u smile at fdis
    "Saya grabs a purple ball from the ball rack, studying for a few seconds. Once she seemed satisfied with it, she smiled happily and walked up to our lane."
    "She lined herself up for a second before swinging the ball and releasing it."
    "The thrown ball rolls rapidly through the clear lane and..."
    play sound "music/disappointment.ogg"
    "Falls into the gutter."
    show k 2 u gentle at fdis
    show s 1 u laugh at fdis
    show j 1 u wince at fdis
    show sa 1 u shock at fdis, jumping
    sa "\"Wha-\""
    s "\"Bahahahahaha. Oh wow, you were talking yourself up so much and you went and threw the first one into the gutter. Oh my God. My sides! Hahahahaha!\""
    "Shoichi immediately explodes into laughter, doubling over himself and tapping his knees repeatedly."
    "Keisuke stands right next to him, his entire body quivering as he attempts to suppress his own laughter."
    "The only one not laughing is Jun, who looks at the entire scene with pity in his eyes."
    show sa 1 u avoidb at fdis
    sa "\"C-cut it out. Stop laughing at me, I still have one more ball!\""
    mc 1 u considerate "\"Well, with the way you were talking it sounded like you'd be doing a strike so it's a little funny.\""
    sa "\"Not you too!\""
    j "\"Mizoguchi-san, good luck...\""
    show sa 1 u sigh at fdis
    sa "\"See, at least Jun-kun has my ba-\""
    show j 1 u considerate at fdis
    j "\"You'll need it.\""
    show sa 1 u poutb at fdis
    sa "\"{size=-4}I hate you all!{/size}\""
    show j 1 u watch at fdis
    show s 1 u smile at fdis
    show k 1 u smile at fdis
    "Saya huffs, grabbing another ball and walking back to the lane with heavy steps."
    show sa 1 u at fdis
    "This time she doesn't meticulously align herself like she did before. She merely swings the ball violently and throws it into the lane."
    play sound "music/bowling.ogg"
    show s 1 u think at fdis
    "And knocks down six pins."
    s "\"Not bad. Over fifty percent at least.\""
    show sa 1 u pout2 at fdis
    sa "\"Nuuuuh. I was aiming for a spare!\""
    show k 1 u at fdis
    k "\"I'd be glad that you didn't just throw it in the gutter again.\""
    show s 1 u smile at fdis
    show j 1 u think at fdis
    "Jun tugs on my sleeve, trying to get my attention."
    j "\"What's a spare?\""
    mc 1 u talk "\"That's a term for when you knock all the pins in your second throw. If you knock them all down on the first one, it's a strike. If you do it on the second one, it's a spare.\""
    show j 1 u at fdis
    show sa 1 u at fdis
    j "\"How many points is it worth?\""
    mc 1 u talk "\"It depends. If you get a strike, then it'll be worth ten points plus the amount of pins you knock down in your next two throws.\""
    mc 1 u talk "\"So if you get a strike in one frame and then knock down six pins on the next, you'll get a total of twenty-two points.\""
    mc 1 u talk "\"It's a similar case with a spare, except you get ten points plus the amount of pins knocked down on the very next throw instead of the next two throws.\""
    show j 1 u wince at fdis
    j "\"Ugh... too many numbers. My head hurts.\""
    k "\"If this is all it takes to trip you up then you're screwed come mid-terms.\""
    show j 1 u sigh at fdis
    j "\"Please don't remind me...\""
    show j 1 u watch at fdis
    s "\"If you'll excuse me, it's my turn now.\""
    show k 1 u smile at fdis
    show s 1 u sigh at fdis
    k "\"Try not to break anything.\""
    s "\"I'm not Saya.\""
    show sa 1 u annoyed at fdis, jumping
    sa "\"I heard that!\""
    show s 1 u smile at fdis
    s "\"Good to know. I guess you can cancel your next visit to the audiologist.\""
    sa "\"...\""
    "Saya stares him down with murderous intent reeking off of her."
    show s 1 u think at fdis
    s "\"Why are you looking at me like that? You hungry or something?\""
    show k 1 u worried at fdis
    k "\"Jesus Christ, man. Don't anger {i}it{/i}.\""
    show s 1 u happy at fdis
    show k 1 u at fdis
    s "\"Okay okay, I'll behave.\""
    "Shoichi chooses a ball, still chuckling."
    show s 1 u smile at fdis
    show sa 1 u at fdis
    "He of course goes for the biggest and bulkiest size they have available."
    "Since he is by far the strongest among us, he can easily just go with the heaviest ball without any issues."
    "Being able to use the heaviest ball also means he has that much more momentum on his throws due to the added weight."
    "Like Saya did before him, he aligns himself for a second and swings his arm to throw the ball."
    play sound "music/bowling.ogg"
    "Unlike Saya however, his first throw makes contact with the pins."
    show s 1 u think at fdis
    s "\"Damn, only four...\""
    show s 1 u at fdis
    mc 1 u smile "\"Knock three more with the next throw and you already have Saya beat.\""
    show sa 1 u pout at fdis
    sa "\"There are nine more frames to play. Don't count your chickens before they hatch!\""
    show j 1 u think at fdis
    j "\"Or your balls before they crash.\""
    show s 1 u happy at fdis
    s "\"I'll already be happy just by avoiding last place.\""
    show j 1 u watch at fdis
    j "\"Really? Why's that?\""
    show k 1 u smile at fdis
    k "\"Urata tends to get last place more often than not.\""
    show j 1 u shock at fdis
    j "\"Really? I never thought there'd be something that Shoichi-san is bad at.\""
    show s 1 u sigh at fdis
    show j 1 u watch at fdis
    s "\"I'm bad at most things actually. You have no idea how much effort it takes me to not suck.\""
    mc 1 u smile "\"I can confirm. Shoichi sucks at most games.\""
    show s 1 u think at fdis
    s "\"I don't spend much time playing games so that's no surprise really.\""
    show s 1 u smile at fdis
    show k 1 u at fdis
    s "\"But now if you don't mind, I have to play my second ball.\""
    play sound "music/bowling.ogg"
    "Shoichi throws the ball once again, this time narrowly avoiding the gutter."
    "Luckily for him, the ball grazes past a single pin that knocks three others when it goes down."
    show s 1 u happy at fdis
    s "\"Woo, lucky!\""
    sa "\"Tch, two more points than me...\""
    show k 1 u smile at fdis
    k "\"We're not off to a bad start here.\""
    show j 1 u wince at fdis
    show s 1 u smile at fdis
    show sa 1 u at fdis
    j "\"Ugh... now's my turn to play.\""
    mc 1 u happy "\"Don't worry about it so much, Jun.\""
    mc 1 u smile "\"Here, let me show you the different ball sizes. I'll walk you throw them from the lightest to the heaviest. Do a couple swings with each before going to the next.\""
    show j 1 u think at fdis
    j "\"Why are we doing this?\""
    show k 1 u at fdis
    k "\"Ideally you want to use the heaviest ball you can comfortably swing. The heavier the ball is the more momentum it carries, so it's best to always stick with the heaviest possible.\""
    mc 1 u talk "\"It's as he said. You basically go up until you can't swing comfortably anymore. If you feel like a certain size would hurt you and would just be difficult to throw, you settle for the one below it.\""
    show j 1 u wince at fdis
    j "\"O-okay... I didn't think there'd be this much prep work involved.\""
    mc 1 u smile "\"It's fine. You only have to do this once to figure out what size is best for you and then you can just stick to it.\""
    show j 1 u watch at fdis
    "I show Jun a few bowling balls so he can familiarize himself with them."
    "I also take the opportunity to give him some pointers on how to properly swing and throw the ball, making sure to correct him when he makes a mistake."
    "It takes us at least five minutes before he's figured out how to do it properly and then a couple more minutes to find the ideal weight for him."
    mc 1 u smile "\"Alright. This one's an 11-pound one. This is what you'll be sticking with.\""
    show j 1 u think at fdis
    j "\"Why are they in pounds?\""
    show j 1 u watch at fdis
    mc 1 u talk "\"The weight markings depend on the manufacturer and country of origin. This venue tends to stick to ones that uses pounds for some reason. You can also find places that use kilos though.\""
    j "\"Hmm... By the way, which balls do you guys use?\""
    mc 1 u smile "\"I use a 15-pound one. Shoichi uses 16-pounds. Saya and Keisuke both use 13.\""
    show j 1 u wince at fdis
    j "\"So I'm the weakest of us all?\""
    show s 1 u happy at fdis
    s "\"Hey, at least you avoided the child sizes. Anything below 10 is usually for children.\""
    j "\"So I'm barely stronger than a child?! How is that supposed to make me feel better?\""
    show s 1 u think at fdis
    s "\"Well, we're talking about children that already have experience bowling. You're a guy that doesn't exercise. You can't expect to start by playing the heavier ones.\""
    show s 1 u at fdis
    k "\"Saya-san and I are athletes and we still use size 13s. I don't know why you're complaining.\""
    j "\"Yeah yeah...\""
    show sa 1 u bored at fdis
    sa "\"Jun-kun, if you don't mind, could you take your turn?\""
    show j 1 u think at fdis
    j "\"Oh, right.\""
    show sa 1 u at fdis
    "Jun hesitantly walks towards the lane with his ball in hand."
    "He tries to line himself up and aim like I taught him."
    "To be honest, I'm totally expecting this first ball to go straight in the gutter since he's never done this before."
    "I just hope he doesn't get too upset if it happens."
    "Jun takes his swing and..."
    play sound "music/tableknock.ogg"
    show j 1 u shockb at fdis
    "... the ball flies into the lane next to us, going right into its gutter."
    j "\"Aaah, my ball!\""
    show k 1 u worried at fdis
    show s 1 u laugh at fdis
    show j 1 u blush2 at fdis
    s "\"Pffft, haha-\""
    play sound "music/slap.ogg"
    show s 1 u wince at fdis, shake1
    "I immediately smack Shoichi upside his head."
    s "\"Ow! What's the big idea?!\""
    mc 1 u annoyed "\"Don't laugh at him. It's his first time. You'll just discourage him from playing.\""
    show s 1 u sigh at fdis
    s "\"Ugh... Sorry...\""
    show j 1 u considerate at fdis
    j "\"It's fine... I really messed up pretty bad huh?\""
    show s 1 u think at fdis
    s "\"I mean, [povFirstName] is right. This is your first time. It's normal to be clumsy at it.\""
    show s 1 u at fdis
    show j 1 u wince at fdis
    j "\"Uhm... I guess I'll try again now...\""
    "I nod at him, trying to give him an encouraging glance and a thumbs up for good measure."
    "From the look on his face, I can already tell it wasn't very effective..."
    "At least it's the thought that counts... right?"
    "Jun grabs another ball, walking every more timidly to the lane."
    "He tries to adjust himself differently from next time."
    "At least he's trying to make adjustments based on the last one."
    "Some people tend to just get frustrated and throw the ball at random."
    "And yes, I am totally staring at Saya as I think of this."
    "The tiger takes a swing and..."
    show j 1 u shock at fdis
    play sound "music/bowling.ogg"
    "Throws a ball cleanly down the middle of the line. It crashes against the pins and knocks them all down in one fell swoop."
    show s 1 u sigh at fdis
    show k 1 u shock at fdis
    mc 1 u shock "\"Woah! Did you seriously just do a spare?\""
    s "\"Seriously? On his second try?\""
    show k 1 u avoid at fdis
    k "\"Why do you look so unhappy about that?\""
    s "\"I don't know what you're talking about...\""
    sa "\"I smell burning. Shoichi, I think it's your pants.\""
    s "\"Har har.\""
    show j 1 u wince at fdis
    j "\"Uhm... so if I remember correctly from what [povFirstName]-san told me, this means I got ten points right?\""
    mc 1 u smile "\"Plus the amount of pins you knock down on your first throw during the next frame, yes.\""
    show j 1 u think at fdis
    j "\"So... that means I'm currently winning?\""
    mc 1 u smile "\"At least as far as the first frame is concerned, yeah.\""
    show j 1 u shock at fdis
    j "\"Yay. I don't suck!\""
    show k 1 u worried at fdis
    show j 1 u watch at fdis
    k "\"That... that had to be beginners luck, right?\""
    s "\"I think so. Either that or the savant has awakened.\""
    k "\"Is there even such a thing as a bowling savant?\""
    s "\"I hope not...\""
    show sa 1 u talk at fdis
    sa "\"Can you two stop grumbling over there?\""
    k "\"Yes ma'am...\""
    show sa 1 u at fdis
    show k 1 u at fdis
    show s 1 u at fdis
    mc 1 u smile "\"I'm next. Let's see if I can at least get enough points to not fall behind on the first frame.\""
    "I inspect the balls available to me, settling on a purple one with a galaxy motif."
    "My fingers fit nicely inside and it doesn't feel uncomfortable to hold."
    "I have to admit, the heft of a bowling ball in my hands is something I hadn't felt in a while. I've totally grown unaccustomed to it."
    "Man, I think it's been over a year since we last played."
    mc 1 u happy "\"Cross your fingers for me, guys!\""
    show s 1 u smile at fdis
    s "\"Yup. Here's hoping they both fly right into the gutter.\""
    mc 1 u annoyed "\"Alright, let me rephrase. Cross your fingers, everyone that isn't Shoichi.\""
    show s 1 u happy at fdis
    s "\"Aww, you're no fun.\""
    show s 1 u smile at fdis
    "I hold the ball in front of my face, trying to take aim and prepare myself to throw it."
    "Since it's been a while I'm sure my aim is going to be a little off."
    "I'll use my first throw to adjust myself so I can have a better idea where to aim."
    "For now, I just swing the ball, curving myself forward to release it straight towards the floor."
    play sound "music/bowling.ogg"
    "It veers slightly to the left as it rolls, threatening to go down the gutter before crashing against a few pins.\""
    mc 1 u smile "\"Hey, five on the first throw. Not bad.\""
    s "\"Booo. It's no fun if you don't mess up!\""
    mc 1 u sigh "\"Stop cheering against me already you traitor.\""
    s "\"How am I a traitor? I don't remember ever taking your side in bowling before.\""
    mc 1 u sigh "\"I see how it is...\""
    "I quickly grab another ball to do my second throw."
    "Since I've knocked down most of the pins on the left side, I'll have to aim for the ones on the right now."
    play sound "music/bowling.ogg"
    "I throw the ball again. This time it knocks three more pins."
    "The falling pins graze against the other two that aren't directly hit by the ball, causing them to sway agressively."
    show j 1 u shock at fdis
    j "\"Ooh-\""
    show j 1 u wince at fdis
    "... But they end up not falling, leaving me with only the three pins I got down initially."
    mc 1 u sigh "\"Rats. I almost got a spare.\""
    show s 1 u happy at fdis
    s "\"Damn, that's just too bad!\""
    mc 1 u sigh "\"Quit looking so amused.\""
    s "\"Amused? Me? I don't know what you mean.\""
    show s 1 u smile at fdis
    j "\"I'm sorry you didn't get those other pins, [povFirstName]-san.\""
    mc 1 u "\"Eh, what can you do. I just didn't get lucky.\""
    show j 1 u watch at fdis
    show k 1 u smile at fdis
    k "\"Well, it's my turn now.\""
    show sa 1 u laugh at fdis
    sa "\"Go, Kei-kun!\""
    show k 1 u calm at fdis
    k "\"Ah, thanks for cheering fo-\""
    show sa 1 u happy at fdis
    sa "\"Please don't knock too many down. I don't want to be last place on the first frame!\""
    show k 1 u sigh at fdis
    show j 1 u gentle at fdis
    k "\"... I take my thanks back.\""
    show j 1 u smile at fdis
    show k 1 u at fdis
    show sa 1 u at fdis
    "Kei-kun spends almost a full minute examining the balls before deciding on which one he wanted."
    "He is by far one of the pickiest people I know when it comes to picking a ball. He checks every minute detail."
    "It tends to get really annoying when he repeats this for many frames in a row..."
    "Once he's found one he's satisfied with, he doesn't dally before taking his first shot."
    show k 1 u smile at fdis
    play sound "music/bowling.ogg"
    "The ball knocks down four pins on its first go."
    k "\"Not too bad.\""
    s "\"Three more and you get more points than Saya.\""
    show sa 1 u annoyed at fdis
    sa "\"Five more and you get more than Shoichi and [povFirstName].\""
    show k 1 u sigh at fdis
    k "\"I knocked pins in the middle. There's no way my ball can hit both sides at the same time.\""
    sa "\"Boo! Just knock them all down already!\""
    show k 1 u worried at fdis
    k "\"I thought you didn't want me to get many points.\""
    s "\"She has no idea what she wants.\""
    sa "\"Zip it, wolf boy!\""
    show s 1 u sigh at fdis
    show sa 1 u at fdis
    s "\"I'm a husky, thank you very much.\""
    show s 1 u at fdis
    show k 1 u at fdis
    "Kei-kun spends another long time picking his next ball."
    "This time it takes even longer than before, almost two full minutes before he finds a \"perfect match\"."
    play sound "music/bowling.ogg"
    "This time he manages to knock down three pins, just enough to overtake Saya."
    show k 1 u worried at fdis
    show sa 1 u complain at fdis
    sa "\"Damn it!\""
    k "\"Tch... I should have gotten one more...\""
    mc 1 u smile "\"Well, you're in the bottom two for now.\""
    show k 1 u sigh2 at fdis
    show sa 1 u at fdis
    k "\"We're still on the first frame. There's still a lot of game to be played before you can start gloating.\""
    mc 1 u talk "\"I'm not even gloating. Jun is ahead of Shoichi and me remember?\""
    show j 1 u think at fdis
    j "\"I don't expect that I'll be for long though.\""
    "... Truth be told, I don't either but that would be a dickish thing to say out loud."
    scene Bowling
    show j 1 u shock at fdis, one
    show s 1 u at fdis, four
    show k 1 u worried at fdis, eight
    show sa 1 u complain at fdis, ten
    with fade
    "After a little over an hour of gaming, we finish the last frame and the scores get tallied up."
    mc 1 u laugh "\"Yes! I win! Fucking finally! I haven't won in so long!\""
    j "\"I'm... I'm second place? Are you kidding? No way!\""
    k "\"A single point ahead of me too... damn it, I was so close...\""
    s "\"Not too bad. At least I wasn't dead last again.\""
    sa "\"I can't believe you beat me by a single point!\""
    show s 1 u happy at fdis
    s "\"Yup. And don't you forget it!\""
    "The final scores were very close together all things considered."
    "I was in first place with 89 points. Jun was second with 84. Keisuke was third with 83. Shoichi fourth with 74 and Saya last with 73."
    "It really felt like a game where even just a few points would make a huge difference."
    "And I won't lie, it feels good to win!"
    "Usually either Saya or Keisuke ended up taking first place so I'm definitely surprised to have won this time."
    mc 1 u curious "\"You were really off your game today, Saya-chan. Did something happen?\""
    sa "\"Not that I know of. I just sucked today...\""
    show s 1 u sigh at fdis
    s "\"Jeez, if you sucked and I barely managed to beat your score then what does that say about me?\""
    show sa 1 u at fdis
    sa "\"That you suck, but that shouldn't be a surprise.\""
    mc 1 u "\"I mean... none of us is crazy good in the first place. And our scores were actually pretty low this time. No one broke 100.\""
    show s 1 u think at fdis
    s "\"Well, we haven't played in a long time for one.\""
    k "\"That's not an excuse though. Kobayashi-kun never played before and he beat most of our scores.\""
    show j 1 u considerate at fdis
    j "\"I'm pretty sure that was just beginners luck.\""
    show k 1 u at fdis
    show s 1 u smile at fdis
    show j 1 u watch at fdis
    s "\"Still, you did pretty well for your first time. You definitely deserve some congratulations on that, Jun-kun.\""
    show j 1 u shockb at fdis
    j "\"T-thank you. I didn't expect something like this to happen...\""
    mc 1 u happy "\"But you did do really well for your first time. Not only that, you even got a full ten point lead over Shoichi and Saya. That's pretty good.\""
    show j 1 u happyb at fdis
    j "\"Hehehe~\""
    show k 1 u smile at fdis
    s "\"I guess the bowling idea was pretty successful after all huh?\""
    k "\"I won't lie, I enjoyed myself. I missed bowling.\""
    show j 1 u watch at fdis
    j "\"Why did you guys go so long without playing?\""
    show k 1 u at fdis
    k "\"We all got busy with our competitions last year and just didn't play again once we were a little more free.\""
    show s 1 u think at fdis
    s "\"I guess it just never crossed our minds.\""
    show sa 1 u bored at fdis
    sa "\"I still can't believe I did that badly...\""
    show s 1 u happy at fdis
    s "\"I still can't believe I beat you!\""
    show sa 1 u pout at fdis
    sa "\"Stop gloating already!\""
    s "\"Never. I will never forget this moment!\""
    sa "\"You didn't even win!\""
    show s 1 u smile at fdis
    s "\"But I got a higher score than you. That's all that matters!\""
    show sa 1 u pout at fdis, shake1
    sa "\"Ugh...\""
    mc 1 u smile "\"You think we can head to the restaurant already?\""
    show s 1 u think at fdis
    show sa 1 u at fdis
    s "\"It's almost 6PM so we could. It'll be a pretty early dinner though.\""
    mc 1 u laugh "\"It doesn't matter. Oden isn't something you want to rush through eating anyway. It's better to take our time.\""
    show j 1 u think at fdis
    j "\"Yeah. We'll probably be there for over an hour easily.\""
    k "\"There's also the time it takes to get there. How far is it?\""
    s "\"We'll have to take the train. It'll be at least twenty minutes to get there.\""
    mc 1 u "\"So it'll already be 6 by the time we arrive. Yeah, I think we should really get going.\""
    show j 1 u wince at fdis
    j "\"[povFirstName]-san... are you sure it's okay for you to be treating me?\""
    mc 1 u smile "\"Of course it is. It's my pleasure, Jun. I'd rather pay and have you with us. It's just not the same without you.\""
    show j 1 u shockb at fdis
    show s 1 u sigh at fdis
    j "\"Ah... I don't know what to say...\""
    s "\"When did the two of you get so chummy with each other?\""
    show j 1 u blush2 at fdis
    mc 1 u talk "\"What do you mean? We're just as friendly with each other as we've always been.\""
    s "\"Really? Cause it definitely feels like you guys got really closer lately.\""
    mc 1 u confused "\"Whatever do you mean? It's the same as always. Isn't that right Jun?\""
    j "\"Y-yeah...\""
    mc 1 u curious "\"What's with that look on your face? Is something wrong?\""
    j "\"N-no. Not at all!\""
    s "\"...\""
    k "\"Don't forget to return the shoes.\""
    show s 1 u at fdis
    show j 1 u shockb at fdis
    j "\"Oh yeah. I almost walked out with their shoes!\""
    mc 1 u considerate "\"Then you wouldn't be able to go to school tomorrow without proper shoes.\""
    stop music3 fadeout 2.5
    scene RamenRestaurant
    show j 1 u sigh at fdis, one
    show s 1 u at fdis, four
    show k 1 u at fdis, eight
    show sa 1 u argue at fdis, ten
    with fade
    play music2 "music/BGM/Lobby Time.ogg" fadein 5.0
    "We finally arrive at the restaurant Shoichi suggested."
    "Having underestimated the afternoon rush, it took us nearly an hour to arrive and we had to go through several crowds of people at the train station."
    "Not to mention being squished inside the train itself like a bunch of sardines in a can."
    "Jun in particularly did not take well to that part."
    "My arm is still numb from how hard he was clutching it."
    sa "\"Ugh... I swear transit gets a little worse every year...\""
    show s 1 u sigh at fdis
    show k 1 u avoid at fdis
    show sa 1 u at fdis
    s "\"Well, Saitama's been growing a lot lately.\""
    k "\"I really miss living in a smaller city...\""
    show j 1 u considerate at fdis
    j "\"I'm just glad we've arrived... I don't think I could keep breathing inside that station.\""
    mc 1 u shock "\"Man, this place is chock full of people. Are there even any open seats?\""
    show s 1 u think at fdis
    s "\"I'll ask the waiter. Hang on a sec.\""
    show s 1 u at fdis, offscreenright
    show j 1 u watch at fdis, two
    show k 1 u at fdis, five
    with move
    "Shoichi approaches a nearby waiter as he finishes serving a desk, talking to him with words we can't hear and gesturing to our group."
    "He and the waiter talk for a little bit before the guy nods."
    "Shoichi looks towards us and flashes a thumbs up before making a gesture with his head that tells us to follow him."
    "It turns out there were still a few open tables a little further on the back of the restaurant."
    "The location of them isn't very visible from the entrance but I can't complain considering it's almost 7PM by the time we got here."
    show j 1 u watch at fdis, one
    show s 1 u smile at fdis, four
    show k 1 u at fdis, eight
    show sa 1 u at ten
    with move
    s "\"There. Problem solved in a jiffy.\""
    show k 1 u sigh at fdis
    k "\"Why was there even a problem? We're still in Spring. Why are so many people in here?\""
    show s 1 u sigh at fdis
    s "\"This place doesn't just serve oden you know. Otherwise they'd be going out of business during three-fourths of the year.\""
    k "\"Yeah, I guess so...\""
    show j 1 u think at fdis
    j "\"Today's pretty chilly too so I'm sure there are other people like us who came by to get something warm.\""
    show s 1 u smile at fdis
    show k 1 u at fdis
    s "\"Oh yeah. That's for sure.\""
    show j 1 u watch at fdis
    j "\"How much does it cost to eat in this place anyway? It looks kinda fancy on the inside.\""
    show s 1 u at fdis
    s "\"Like I said earlier, it's not the cheapest but it's not expensive either. It's just the decor that's really good. The cheapest oden meal on the menu is around ¥2000 though.\""
    show j 1 u wince at fdis
    j "\"Ouch. That's kinda pricy... I think I'll stick to the cheapest option...\""
    mc 1 u "\"Don't be ridiculous. Order whatever you want. I want you to enjoy yourself.\""
    show j 1 u avoid at fdis
    j "\"But... it's so expensive.\""
    mc 1 u considerate "\"Come on, Jun. I actually {i}want{/i} to treat you. Don't cheap out on me here. I want you to eat whatever you want to eat.\""
    j "\"O-okay...\""
    sa "\"You don't have to be so reserved around us, Jun-kun.\""
    show s 1 u at fdis
    s "\"Agreed. You're already with us every day of the week. You don't have to keep acting like a stranger.\""
    show j 1 u considerate at fdis
    j "\"It's not that. I'm just... not too good at accepting things from other people. I feel like I haven't done anything to deserve it.\""
    show j 1 u watch at fdis
    mc 1 u smile "\"You spend time with me, you make me laugh and I enjoy being with you. Pretty sure that's reason enough for me to want you around.\""
    show j 1 u shockb at fdis
    j "\"[povFirstName]-san...\""
    show s 1 u sigh at fdis
    s "\"Get a room you two.\""
    show j 1 u wince at fdis, jumping
    j "\"W-what?\""
    mc 1 u sigh "\"Could you not say weird stuff like that?\""
    s "\"Then don't say sappy stuff like that in public.\""
    mc 1 u sigh2 "\"Yeah yeah.\""
    show j 1 u watch at fdis
    show s 1 u at fdis
    k "\"Have any of you decided on what you're going to order?\""
    s "\"We haven't even checked the menu yet.\""
    mc 1 u sigh "\"Wait, were you reading the menu while we talked? You didn't listen to a single thing we said did you?!\""
    k "\"I tuned out around the time Urata started mocking you two.\""
    show s 1 u sigh at fdis
    s "\"I wasn't {i}mocking{/i} them! ... Not exactly.\""
    mc 1 u talk "\"I think I'll just go for something lighter. Chicken stock and vegetables sounds pretty good.\""
    show s 1 u smile at fdis
    s "\"I want something a little more fulfilling myself. Lots of meat in mine.\""
    show k 1 u sigh at fdis
    k "\"You should be telling that to the waiter, not to us.\""
    show k 1 u at fdis
    show s 1 u at fdis
    s "\"The waiter isn't even here yet.\""
    k "\"Well, call him over.\""
    show s 1 u sigh at fdis
    s "\"Do you have to speak in that kind of tone all the time?\""
    show k 1 u worried at fdis
    k "\"What tone? I'm talking like I always do.\""
    s "\"Exactly.\""
    show k 1 u wince at fdis
    k "\"What? Then what's the problem?\""
    show j 1 u considerate at fdis
    "Damn, it's been a while since they last bickered like that so I didn't think I'd have to deal with it again today."
    "From the corner of my eye, I already see Jun tensing up on the chair next to mine."
    "It seems even he's considering whether he should weigh in and say something..."
    "Just as I prepare myself to speak my mind, Saya-chan clears her throat."
    show sa 1 u think at fdis
    sa "\"What was it you said again? \"Get a room, you two\".\""
    show s 1 u shock at fdis
    show k 1 u shock at fdis
    show sa 1 u smile at fdis
    s "\"Wha-\""
    k "\"Saya-chan, don't say weird things like that either!\""
    show j 1 u happy at fdis
    j "\"I call that instant karma.\""
    show s 1 u sigh at fdis
    show k 1 u avoid at fdis
    s "\"Don't be looking so pleased over that...\""
    show j 1 u think at fdis
    j "\"Me? Pleased? I don't know what you mean.\""
    show j 1 u gentle at fdis
    s "\"It's a good thing you're cute because you are a terrible liar.\""
    show j 1 u smile at fdis
    show s 1 u at fdis
    show k 1 u at fdis
    "Still smiling and looking oh so pleased with himself, Jun beckons over the waiter."
    "He takes our orders very quickly and politely."
    mc 1 u smile "\"I'm kinda surprised. The service here is pretty good.\""
    show sa 1 u bored at fdis
    sa "\"What are you saying? That the service where I work is bad? You wanna pick a fight?!\""
    show k 1 u sigh at fdis
    show j 1 u watch at fdis
    mc 1 u sigh "\"... Where do you even get these outlandish ideas from?\""
    k "\"Mizoguchi-san rolled for Perception. It was a 1.\""
    mc 1 u confused "\"Erm... what?\""
    show k 1 u avoid at fdis
    show sa 1 u at fdis
    k "\"N-no, nothing.\""
    s "\"Probably some kind of game stuff. Maybe Jun-kun can tell us what it is?\""
    show j 1 u think at fdis
    j "\"Sorry, I have no idea.\""
    show s 1 u smile at fdis
    s "\"I guess this means Urushihara's into some pretty obscure stuff huh?\""
    k "\"That sounded so wrong...\""
    show s 1 u happy at fdis
    s "\"And yet oh so right!\""
    show k 1 u sigh at fdis
    k "\"Why do I bother with you?\""
    s "\"Because you {i}looooove{/i} me.\""
    k "\"... Did you hit your head somewhere?\""
    show s 1 u sigh at fdis
    s "\"Sheesh, you don't have to shoot me down so coldly.\""
    mc 1 u talk "\"Get a ro-\""
    show s 1 u doom at fdis
    s "\"Don't you dare!\""
    show j 1 u gentle at fdis
    j "\"I'm pretty sure that one joke really turned against you big time huh?\""
    show s 1 u sigh at fdis
    show j 1 u smile at fdis
    s "\"It's fine. I'm already used to having my big mouth used against me.\""
    show k 1 u at fdis
    k "\"Dumbass.\""
    show s 1 u annoyed at fdis
    s "\"What did you just say, punk?\""
    show k 1 u smile at fdis
    k "\"Who? Me? I have no clue.\""
    s "\"Mhm. That so...\""
    show s 1 u at fdis
    show j 1 u watch at fdis
    mc 1 u smile "\"Petty squabbles aside, I'm actually kinda curious. How are the festival preparations going for you guys?\""
    show k 1 u sigh at fdis
    show s 1 u think at fdis
    k "\"Pretty terrible. My class decided on a theme a while ago but they can't agree on the division of work.\""
    s "\"Ours has been pretty much smooth sailing but I guess the theme is a little more boring than I would like.\""
    show sa 1 u talk at fdis
    sa "\"What did your classes pick? Mine went for an international café. Each booth is supposed to serve food and drinks from different countries.\""
    s "\"That sounds like a logistics nightmare.\""
    show sa 1 u complain at fdis
    sa "\"Exactly.\""
    "Her dry, unamused tone of voice was already enough to tell me how she felt about the whole thing."
    show s 1 u at fdis
    show sa 1 u at fdis
    s "\"My class picked a library theme... We're basically gonna host a library... wooo.\""
    show j 1 u think at fdis
    j "\"Fun fun fun.\""
    show s 1 u sigh at fdis
    show j 1 u happy at fdis
    s "\"Don't you sass me.\""
    show j 1 u watch at fdis
    show k 1 u at fdis
    k "\"My class wanted to do a haunted house of all things.\""
    show s 1 u shock at fdis
    show j 1 u shock at fdis
    mc 1 u shock "\"A haunted house? Why?\""
    show k 1 u avoid at fdis
    k "\"Beats me. It's what they voted for.\""
    show s 1 u think at fdis
    s "\"Man, that's gonna be a bitch to organize.\""
    show k 1 u sigh at fdis
    k "\"Tell me about it. I had to listen to a twenty minute conversation on whether patrons should be chased around by Neddie Luger or Mason...\""
    mc 1 u "\"Our class is gonna serve Sichuan cuisine. That's pretty much it.\""
    show j 1 u think at fdis
    j "\"The girls are gonna be wearing Chinese dresses too.\""
    show k 1 u smile at fdis
    show s 1 u at fdis
    k "\"Oh, that sounds like fun.\""
    show s 1 u sigh at fdis
    s "\"You just say that because you wanna ogle the girls.\""
    k "\"I won't say no to that.\""
    s "\"No shame...\""
    show s 1 u smile at fdis
    show j 1 u watch at fdis
    show sa 1 u think at fdis
    sa "\"I wonder if we'll get any costumes in my class.\""
    s "\"You can just show up in your regular clothes and be the bouncer.\""
    show s 1 u laugh at fdis
    show sa 1 u laugh at fdis
    sa "\"That's a great idea! I'll make sure to throw you out the window first!\""
    s "\"Guess I'm going for a trip!\""
    show j 1 u think at fdis
    show sa 1 u at fdis
    mc 1 u sigh "\"Our classes are on the 3rd floor. You'd be going on a trip to the hospital.\""
    j "\"I've gone on that trip recently. It's not fun.\""
    show j 1 u watch at fdis
    show k 1 u at fdis
    k "\"Oh yeah, how's your head doing Kobayashi-kun?\""
    mc 1 u talk "\"Oh man, I totally forgot to ask that too.\""
    show j 1 u think at fdis
    j "\"It's... okay. It still stings when I touch it so changing clothes is a bit troublesome but otherwise it's fine.\""
    show j 1 u watch at fdis
    show k 1 u smile at fdis
    k "\"Does that mean you now have the okay to get back to practice?\""
    show j 1 u wry at fdis
    show s 1 u avoid at fdis
    show k 1 u at fdis
    j "\"Uhm... Sorta, although I decided to take a break for today. I don't need the stress while dealing with this.\""
    s "\"That's... probably a good idea.\""
    mc 1 u "\"I get why Jun wouldn't be all to happy but why are {i}you{/i} looking like you just swallowed a piece of lime?\""
    show s 1 u sigh at fdis
    s "\"Huh? I am?\""
    show j 1 u considerate at fdis
    j "\"I guess Shoichi-san is just feeling empathetic for me.\""
    show sa 1 u talk at fdis
    sa "\"Doesn't sound like the Shoichi I know.\""
    s "\"Does that mean there's another Shoichi running around that I don't know about? Because I'm the most empathetic one in this group...\""
    show sa 1 u laugh at fdis
    "Saya smirks, showing Shoichi her tongue in a playful gesture."
    show s 1 u at fdis
    show j 1 u smile at fdis
    show sa 1 u smile at fdis
    j "\"Other than that I'm pretty much good to go. The doctors said there wasn't going to be any lasting damage. Not even a scar. I was really lucky with that one.\""
    mc 1 u sigh "\"You gave me a huge scare though.\""
    show j 1 u considerate at fdis
    j "\"Sorry... it wasn't my intention. Thank you for calling the ambulance for me.\""
    mc 1 u smile "\"Of course. Although if it had been Shoichi that found you he could have just carried you to the hospital on foot.\""
    show s 1 u sigh at fdis
    show j 1 u think at fdis
    show k 1 u smile at fdis
    s "\"Don't be ridiculous. There's no way I'd be able to carry anyone that far.\""
    j "\"Hmm... I guess a horseback ride would be pretty nice.\""
    s "\"What the hell kind of idea did you just have in your mind?\""
    show j 1 u happy at fdis
    j "\"Hahaha. I'm just joking.\""
    s "\"Really? Cause I can't tell...\""
    "Seeing everyone just playing around and having fun like this brings a smile to my face."
    "But more importantly, seeing Jun sitting with us after what's happened brings me an overwhelming amount of joy."
    "Just remembering the whole thing is already haunting."
    "I never wish to go through something like that again..."
    stop music2 fadeout 2.5
    scene Street1N
    show j 1 u smile at fdis, five
    with fade
    play music "music/night.ogg"
    "Jun and I walk home together after separating from the others."
    "Despite how boisterous he was during most of the day, the train ride back to our station saw him staying mostly silent."
    "Not that I blame him. He's not fond of tight spaces filled with people."
    "Now that we're walking back home on the more or less deserted streets, he begins to perk up once again."
    show j 1 u happy at fdis
    "Jun walks, almost skipping, a few steps ahead of me, happily humming a melody."
    "He's so full of energy and life even after a full day... I can't help but think back to when we first met and how I used to be annoyed by this."
    "And now... seeing him like this is so precious to me."
    "... I don't know if it's because of his sudden hospitalization a few days ago, but I've been feeling a lot more emotional lately."
    "Thinking these kinds of thoughts isn't like me at all..."
    show j 1 u watch at fdis
    j "\"[povFirstName]-san? Are you okay?\""
    mc 1 u shock "\"Huh? What? Oh, yeah. Yeah, I'm okay.\""
    mc 1 u sigh "\"Wait, why are you even asking me that?\""
    show j 1 u think at fdis
    j "\"You were making this really complicated face. It looked like you were in pain a bit.\""
    mc 1 u wince "\"I... I did?\""
    show j 1 u happy at fdis
    j "\"Yeah. I was worried that something was going on, but if you're okay then I guess that's fine.\""
    mc 1 u avoidb "\"...\""
    show j 1 u watch at fdis
    j "\"[povFirstName]-san?\""
    play sound "music/fabric.ogg"
    show j 1 u shock at fdis:
        ease .2 zoom 1.5 xoffset -50 yoffset 230
    "Taken completely by impulse, I wrap my arms around him."
    play music2 "music/BGM/Recollections.ogg" fadein 5.0
    j "\"Eh?\""
    "Jun makes a small, confused sound when I do so, but he hugs back almost promptly."
    j "\"Is everything okay?\""
    mc 1 u considerate "\"Yeah... everything's fine. Sorry to do this all of a sudden. I'm kinda surprised you barely even reacted to it though. Usually you'd be super confused.\""
    show j 1 u think at fdis
    j "\"... I'm pretty okay if you're the one doing it.\""
    mc 1 u happyb "\"I'll take that as a compliment.\""
    show j 1 u watch at fdis
    j "\"Why this out of the blue though?\""
    "Even though he asks me that, his grip around me doesn't loosen at all."
    "I'm thankful there aren't people walking around at this time of night as this would be a pretty embarrassing thing to be caught doing in public."
    mc 1 u considerate "\"I was just... thinking of some pretty bittersweet things. I guess I needed some reassurance. Sorry.\""
    show j 1 u happyb at fdis
    j "\"It's alright.\""
    show j 1 u smile at fdis
    j "\"[povFirstName]-san, you've helped me a lot since I first met you... but I don't want things to just be one-sided. I want to be able to support you when you need it, too.\""
    mc 1 u happyb "\"Haha... Thank you. That's really nice of you.\""
    show j 1 u happy at fdis
    j "\"Well, I {i}am{/i} the older one here so it's only natural that I should support my juniors.\""
    mc 1 u considerate "\"Now you're just messing with me.\""
    show j 1 u happy at fdis:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    j "\"Yes, I'm messing with you. Punish me if you see it fit.\""
    mc 1 u happy "\"Don't be ridiculous.\""
    show j 1 u smile at fdis
    j "\"... Thank you for spending the day with me. I had a lot of fun.\""
    mc 1 u smile "\"I did too so it's fine. I should be thanking you too.\""
    show j 1 u happy at fdis
    j "\"In that case: you're welcome!\""
    mc 1 u happy "\"Ahaha. You cheeky little thing.\""
    show j 1 u pout at fdis
    j "\"I'm not little. You're the one that's tall.\""
    mc 1 u considerate "\"Yeah yeah. Whatever you say.\""
    j "\"Now you're just brushing me off.\""
    mc 1 u smile "\"That I am.\""
    show j 1 u smile at fdis
    j "\"By the way, you might not have noticed it because you were spacing out while we walked, but my house is right around that corner.\""
    "Jun gestures in that general direction with his head and only then do I notice the shape of his house right nearby."
    mc 1 u talk "\"That it is...\""
    show j 1 u happy at fdis
    j "\"So I guess this is bye-bye for today.\""
    mc 1 u smile "\"Yeah. See ya tomorrow, Jun.\""
    j "\"Yes.\""
    stop music2 fadeout 2.5
    show j 1 u smile at fdis, offscreenright with moveoridis
    "I watch Jun disappear right around the curve, still humming the same melody as before."
    "For some reason, watching him leave makes my heart ache for a bit..."
    "I stand around that corner for a couple of minutes before my body begins moving again and I head back home."
    $ date = None
    jump Day15_Jun
label JunLeaves:
    scene SClass with dissolve
    play music3 "music/BGM/Dog Days.ogg" fadein 5.0
    play sound "music/schoolbell.ogg"
    "The bell's ringing suddenly snaps me back to reality."
    "Crap, I was so worried thinking over other things that I didn't pay any attention to class today."
    "I am so gonna be screwed in the midterms if I keep this up..."
    "Interestingly enough, neither Jun nor I got into any trouble for ditching an entire period."
    "Guess our class has my back after all..."
    show j 1 u watch at fdis, five with dissolve
    "Jun is absent-mindedly packing his books back in his bag, not really bothering to organize them whatsoever."
    mc 1 u smile "\"Hey, Ju-\""
    show j 1 u considerate at fdis
    j "\"Uhm... sorry [povFirstName]-san, I'm kind of in a hurry right now. I'll see you tomorrow, okay?\""
    mc 1 u avoid "\"Oh, oka-\""
    play sound "music/slidingdoor.ogg"
    show j 1 u considerate at offscreenright with moveoridis
    "And he is out the door before I've even managed to finish saying anything."
    "..."
    play sound "music/message.ogg"
    "Just then, my phone buzzes in my pocket."
    "I have half a mind to ignore it, but then Shoichi's voice echoes around in my head saying \"It's rude to ignore someone's message\" and I pick it up anyway."
    "Sure enough, it's Shoichi messaging me back."
    "\"Hey, are you guys free right now?\""
    "... I merely type back a response."
    "\"sorry, not today\""
    play sound "music/message.ogg"
    "He answers me quickly."
    "\"Alright. Tell Jun-kun I said hi.\""
    "..."
    play sound "music/phonebeep.ogg"
    #show ph
    #show shoc
    #show s1 at Position(xpos=506, ypos=162, xanchor=0, yanchor=0)
    #show s2 at Position(xpos=506, ypos=232, xanchor=0, yanchor=0)
    #show as1 at Position(xpos=574, ypos=282, xanchor=0, yanchor=0)
    #show s3 at Position(xpos=506, ypos=332, xanchor=0, yanchor=0)
    #with dissolve
    #$ renpy.pause(1.0)
    #play sound "music/message.ogg"
    #show s4 at Position(xpos=506, ypos=382, xanchor=0, yanchor=0) with dissolve
    #$ renpy.pause(1.0)
    #"..."
    #play sound "music/message.ogg"
    #show as2 at Position(xpos=574, ypos=432, xanchor=0, yanchor=0) with dissolve
    #$ renpy.pause(1.0)
    #play sound "music/message.ogg"
    #show s5 at Position(xpos=506, ypos=482, xanchor=0, yanchor=0) with dissolve
    #"..."
    #hide s5
    #hide as2
    #hide s4
    #hide s3
    #hide as1
    #hide s2
    #hide s1
    #hide shoc
    #hide ph
    #with dissolve
    "I know I shouldn't be blowing him off like this but... I just can't be bothered right now."
    "Sorry, Shoichi... I'll make it up to you later."
    "I finish packing my things and decide to just head home to sulk somewhere where I can't bother anyone else right now."
    $ date = None
    jump Day15_Jun
