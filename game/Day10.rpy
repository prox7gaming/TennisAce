label Day10:
    window hide
    scene April22 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene Bedroom with fade
    window show
    $ date = "day10"
    play sound "music/alarm.ogg"
    "..."
    "My mind is violently snapped back into wakefulness by the sudden blaring noise of the alarm."
    "What the... who even set up the alarm?"
    "Shit, where is it so I can turn this damn thing off?"
    "Ah, there... 9:30?! Why the hell am I waking up at 9:30 on a weekend?!"
    "It's not as if I have anything to..."
    "Wait..."
    "Did I promise to go out with someone today?"
    "..."
    "Ah!" with hpunch
    "As my mind slowly dispels its foggy state, I seem to remember a little bit more."
    "That's right, I had scheduled to go out today..."
    label notdone:
    menu:
        "It was with..."
        "Shoichi":
            scene black
            show s 1 c smile at five
            with fade
            "Shit!" with hpunch
            "That's right, Shoichi asked me to go out with him today!"
            scene SRooftop with squares
            play music "music/breeze.ogg"
            "I was sitting on the rooftop like I do sometimes. Cloud gazing helps keep my stress at an acceptable level."
            play sound "music/metaldoor.ogg"
            s 1 u wry "\"Oh, I knew you'd be here.\""
            show s 1 u wry at fdis, five with moveiridis
            "Shoichi showed up, looking down at me with a mix of annoyance and amusement."
            "I get the feeling that we've done this a lot over the years."
            s "\"What was it this time? Too much homework? Incoming tests are leaving you stressed?\""
            mc 1 u think "\"Hmm... not sure.\""
            "It wasn't uncommon for me to feel on edge from time to time. Be it home life, school work or everything that was going on with my tennis career."
            "There was always something to tick me off and make me feel stressed."
            "Being lazy was my major outlet."
            "Shoichi sits down on the ground next to me. I can see him staring at my face in curiosity for a few seconds. Then, he turns his eyes towards the sky, watching the clouds."
            "He curves his body forward, hugging his knees as he looks up."
            "We sit in silence for a few minutes, merely watching the clouds as they fly by."
            "It might be silly, but it really does help me to relax."
            s "\"You know...\""
            "Shoichi starts to talk."
            mc 1 u sigh "\"Spare me the lecture!\""
            "Before he even has time to finish his sentence, I already cut him off."
            show s 1 u sigh at fdis
            s "\"Rude! You don't even know what I was going to say.\""
            mc 1 u happy "\"It's you. Of course you were going to give me a lecture about missing class and how that will reflect poorly on my college admittance exams.\""
            mc 1 u think "\"Then I'd have to remind you that I don't even plan on taking those. Yada yada yada. It's the same argument we have every time. Pick a new topic already.\""
            "I give a fleeting glance in his direction."
            "Seeing that look of annoyance on his face feels refreshing somehow."
            show s 1 u happy at fdis
            s "\"Haha, I guess you really do know me well.\""
            mc 1 u think "\"It's been over ten years. It's expected that I would by this point.\""
            s "\"Haha, I guess that's true.\""
            "Shoichi starts rocking his body sideways as he hums a familiar melody."
            "For some reason, I can't seem to recall where I've heard this before. Still, it's a very pleasant tune."
            s "\"Hm hm hmhm~\""
            "Shoichi continues humming happily, not realizing that I've begun watching him."
            "Seeing him look so happy also does wonders for my mood."
            "More so than any clouds in the sky could."
            show s 1 u at fdis
            s "\"Hm?\""
            "Shoichi finally seems to notice that my attention has turned to him."
            show s 1 u smile at fdis
            s "\"What is it?\""
            play sound "music/heartbeat.ogg"
            "!"
            "My heart seems to skip a beat for a second there."
            show s 1 u smile at fdis, offscreenright with move
            "I have to look away to hide the fact that I'm suddenly blushing."
            "Why am I blushing?!"
            mc 1 u avoidb "\"No, it's nothing.\""
            "I hear Shoichi chuckling, but I still don't turn to look at him."
            s 1 u happy "\"Is that so, huh?\""
            "Shoichi starts humming again."
            s 1 u smile "\"Hey, [povFirstName]?\""
            mc 1 u curious "\"Hm?\""
            "He starts humming very quickly, suddenly calling out to me."
            show s 1 u smile at fdis, five with move
            "Reflexively, I turn to look at him."
            mc 1 u curious "\"What is it?\""
            "Shoichi leans forward against his knees, resting his chin on them as his eyes look sideways at me."
            show s 1 u happy at fdis
            s "\"Do you remember this song?\""
            mc 1 u fsmile "\"Huh?\""
            "What kind of question is this?"
            mc 1 u think "\"You mean... the one you were humming?\""
            show s 1 u smile at fdis
            s "\"Yeah.\""
            "Shoichi nods."
            mc 1 u think "\"Hmm...\""
            "Where was it that I heard that song before?"
            menu:
                "Hmm... It sounds really familiar..."
                "\"I remember it.\"":
                    show s 1 u happy at fdis
                    s "\"Really?!\""
                    mc 1 u think "\"It's the song that was playing at the Moon Festival we went to as kids. When was that again...\""
                    mc 1 u curious "\"Six years ago?\""
                    show s 1 u shock at fdis
                    s "\"Ha...\""
                    "Shoichi stares at me in complete bewilderment for a few seconds."
                    "Doubt starts creeping in. Could it be that... I was wrong?"
                    "Then, he suddenly nods energetically, looking incredibly pleased with himself."
                    show s 1 u happy at fdis
                    s "\"You do remember! I'm glad!\""
                    show s 1 u laugh at fdis
                    "Shoichi starts laughing."
                    "He seems so innocent and unguarded. I can't help but start laughing myself."
                    "We keep laughing like two idiots for a few seconds, just enjoying the moment."
                    show s 1 u happy at fdis
                    s "\"That's right. The song suddenly popped back in my mind this morning, I don't know why.\""
                "\"I don't remember.\"":
                    show s 1 u wry at fdis
                    s "\"Is that so?\""
                    "Shoichi looks up at the sky."
                    show s 1 u considerate at fdis
                    s "\"Well, that's fine. I didn't really expect you to remember.\""
                    mc 1 u curious "\"Hey, Shoichi, what's with all this mystery all of a sudden?\""
                    show s 1 u shock at fdis
                    "He seems to snap back to reality."
                    show s 1 u considerate at fdis
                    s "\"Huh? Ah, sorry. It's just that I seemed to remember it at random this morning.\""
                    show s 1 u think at fdis
                    s "\"Honestly, it's a bit strange if I say so myself. There's really no reason for me to be remembering this, but...\""
                    show s 1 u happy at fdis
                    s "\"That's the song that was playing when we went to the Moon Festival. The last one we went to together, the one from six years ago.\""
                    "Ah..."
                    mc 1 u shock "\"... I remember it.\""
                    show s 1 u smile at fdis
                    s "\"Oh, so {i}now{/i} you remember?\""
                    mc 1 u sigh "\"Wha- give me a break! Did you really expect me to remember a song that we heard once six years ago?!\""
                    show s 1 u laugh at fdis
                    s "\"Ahahaha, of course not. I'm just having some fun at your expense!\""
                    mc 1 u think "\"Jeez, we were still kids back then.\""
                    show s 1 u happy at fdis
                    s "\"That's true. I don't remember much from that time. And yet, somehow, I can suddenly recall it vividly. Isn't that strange?\""
                    mc 1 u sigh2 "\"You're the one who's strange.\""
                    show s 1 u laugh at fdis
                    s "\"Oh my poor heart. How mean of you!\""
                    "Shoichi starts laughing."
                    "He seems so innocent and unguarded. I can't help but start laughing myself."
                    "We keep laughing like two idiots for a few seconds, just enjoying the moment."
                    show s 1 u happy at fdis
                    s "\"The song suddenly popped back in my mind this morning, I don't know why.\""
            show s 1 u smile at fdis
            s "\"It just reminded me of how long it's been since we last went to a festival.\""
            mc 1 u think "\"Well, we always seem to be very busy around the time of the festival so it's no surprise.\""
            show s 1 u wry at fdis
            "Shoichi nods."
            s "\"That's also true. It's kinda sad when I think about it.\""
            mc 1 u think "\"It doesn't help that the festival only happens during one of the busiest seasons of the year.\""
            "Our city's Moon Festival happens mid-June, just when one of the major tennis tournaments is going on."
            "It's also right in the middle of the Interhigh Qualifiers, so Shoichi has been very busy with his team in later years."
            "In the end, we haven't managed to attend together once in the last six years."
            "It feels a bit sad when you think about it."
            mc 1 u sigh "\"Damn it, now that you mention it, I really want to try going to a festival again. It's really been a while.\""
            show s 1 u considerate at fdis
            s "\"Last time I attended was on our first year, but you weren't doing too hot back then and didn't want to go with me.\""
            mc 1 u sigh "\"Ugh... don't remind me.\""
            "That was back during the peak of my slump. I was sitting around and feeling pity for myself most of the time."
            "Ugh... it's embarrassing to even think about it."
            show s 1 u smile at fdis
            s "\"Hey, how about we go together this year?\""
            mc 1 u sigh "\"Uhm... you forgot the part where we're both probably going to be super busy by then?\""
            show s 1 u at fdis
            s "\"Well, do you know for a fact that you won't have at least one free day during the festival?\""
            mc 1 u wince "\"W-Well...\""
            "Our city's festival starts on Friday, going all the way to Sunday."
            "So it might be possible for us to meet up then, but..."
            mc 1 u wince "\"I might have the time. But we don't know if you will. We can't make arrangements like this without knowing.\""
            show s 1 u think at fdis
            s "\"That's true...\""
            play music2 "music/BGM/Summer Day.ogg" fadein 8.0
            show s 1 u wince at fdis, shake1
            s "\"Nuuu, but I want to go to a festival!\""
            "Shoichi starts throwing a temper tantrum."
            "As comical as the image of an 18 year old that's almost two meters tall flailing around in a tantrum is, it's also a little bit weird."
            mc 1 u sigh "\"What are you, a kid?\""
            show s 1 u sigh at fdis, jumping
            s "\"That's cruel!\""
            "His switch suddenly goes off."
            "Jeez, when we're both alone together he becomes so easy-going that it's like hanging out with a completely different person."
            mc 1 u sigh "\"Just accept reality already. The chances of us two going out to a festival together are stupidly small this year.\""
            show s 1 u think at fdis
            s "\"Uhm...\""
            s "\"Well...\""
            mc 1 u sigh "\"What is it? Just spit it out already.\""
            show s 1 u smile at fdis
            s "\"Now that I think about it, that's not entirely true. We could go to a festival if we wanted to.\""
            mc 1 u fsmile "\"What? I don't know of any festival's in town save for the Moon Festival.\""
            show s 1 u happy at fdis
            s "\"Hehe, then you're in for a treat. Will you be free on Saturday?\""
            mc 1 u "\"... I should be. Why?\""
            s "\"Oh, no reason in particular.\""
            show s 1 u smile at fdis
            s "\"Except that you'll be going out with me of course! There's one festival going on in town this Saturday and I am absolutely going to take you there!\""
            mc 1 u shock "\"What festival is this?\""
            show s 1 u happy at fdis
            s "\"That, my friend, will be a surprise!\""
            "I groan, already anticipating the worst..."
            stop music fadeout 2.5
            stop music2 fadeout 2.5
            jump Day10_Shoichi
        "Jun":
            scene Black
            show j 1 c gentle at five
            with fade
            "Oh, that's right. Jun had talked to me a couple days ago..."
            "Uh... when was this exactly... Thursday?"
            "Ah, I think I remember..."
            scene SCorridor with squares
            play sound "music/schoolbell.ogg"
            "... Man, I can't believe I missed all of today's history class."
            "Shima-sensei is going to kill me..."
            "Then again, it's not my fault that I was asked to help out at the Staff Room."
            "Honestly, what kind of teacher pulls a student out of his class to ask for help?"
            "\"We both know you're not going to pay attention anyway so you might as well be useful and help me out\" is what she said."
            "Ugh, it makes my blood boil when I think about it."
            play sound "music/slidingdoor.ogg"
            "Just as I reach for the door, it slides open and I nearly collide with someone."
            play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
            show j 1 u shock at fdis, five with dissolve
            j "\"Ah.\""
            "Jun stands in my path, looking up at me with surprise."
            show j 1 u smile at fdis
            j "\"Ah, [povFirstName]-san, I was going to head out to look for you!\""
            play sound "music/slidingdoor.ogg"
            "I step aside to give Jun some room."
            "He walks out of the room and closes the door neatly behind him, all while still facing me."
            mc 1 u curious "\"What for exactly? There's still one more class before lunch break.\""
            show j 1 u watch at fdis
            j "\"Our English teacher didn't show up today. Something about a cold...\""
            "Man, our teachers really have been getting lazier and lazier by the day."
            show j 1 u think at fdis
            j "\"... or pneumonia. I don't really remember.\""
            "... I take it back."
            show j 1 u watch at fdis
            mc 1 u "\"So we're going to have a free period today? And what about Shima-sensei, shouldn't he still be in the classroom?\""
            "Jun looked up for a few seconds, as if he was trying to remember something."
            show j 1 u think at fdis
            j "\"Hmm... I don't really know all that well because I honestly wasn't paying attention. Shima-sensei left early. Something about a family emergency... I think.\""
            "... And yet {i}I'm{/i} the one who gets pulled out of class?"
            show j 1 u considerate at fdis
            j "\"Either way, he left us a bit of homework to do during our free period. I don't really know how to do it so I'm just gonna skip. I was hoping we could spend some time together having fun!\""
            "... This guy."
            mc 1 u sigh "\"Sorry, nope, no can do. We're marching back into that room and doing the homework.\""
            show j 1 u cshock at fdis
            j "\"Whaaaat? Why? You almost never do your homework and you're always skipping classes, why can't I?!\""
            play sound "music/slidingdoor.ogg"
            "I turn Jun around and open the door, pushing the small tiger inside. He digs his feet into the ground, trying to use them as a break of sorts."
            "Jeez, he can be stubborn as a mule when he wants to."
            mc 1 u sigh "\"Do as I say, don't do as I do. I'm a terrible example anyway so don't try to imitate me.\""
            show j 1 u wince at fdis
            j "\"B-But-\""
            scene SClass
            show j 1 u wince at fdis, five
            with fade
            "I manage to drag Jun inside without much issue."
            "Noticing that resistance is futile, he sits down at his desk without much protest."
            show j 1 u pout at fdis
            j "\"Booo, I wanted to have fun.\""
            mc 1 u sigh2 "\"Then finish your homework. We can have fun afterwards.\""
            show j 1 u annoyed at fdis
            j "\"You're not even doing yours, why do I have to do mine?!\""
            "It's true that I just sat down and grabbed my videogame. I guess it might be a bit hypocritical for me to tell him to work when I myself am not..."
            "But then again, I feel like a parent trying to force their kid to do well in class. I might be a terrible example and I might hate doing it myself, but I still expect him to do it without complaint."
            "I guess I might be just a tiny bit twisted."
            mc 1 u "\"I don't need to do it, I'm still keeping an eighty four point grade while skipping classes and never doing homework. How about you?\""
            play sound "music/stab.ogg"
            show j 1 u wince at fdis, shake1
            j "\"G-Guh...\""
            "Bingo, my jab hits him right where it hurts."
            mc 1 u sigh "\"How many points did you get at last week's mock exam?\""
            j "\"... I don't want to say.\""
            "I look up from my game and glare at him."
            show j 1 u fluster at fdis, shake1
            j "\"H-Hiiiiii! F-Forty eight, I got forty eight points!\""
            "It honestly worked better than expected."
            "I set my gaming console down for a second, sighing dramatically to try and drive home just how disappointed I am to hear it."
            show j 1 u wince at fdis
            mc 1 u sigh "\"Forty eight? That's all? You do know you need at least seventy points to be able to pass, right? Are you looking to flunk your way out of one of the most expensive schools in Saitama?\""
            "Jun's shoulders sag and he looks down at his feet."
            j "\"N-No...\""
            "Jeez, he acts so downcast that it looks like I just killed his puppy."
            "There's a limit to how upset you can be about a simple bad grade..."
            show j 1 u at fdis
            j "\"What about you, [povFirstName]-san? How many points did you get on your test?\""
            "I pick my video game back up and start playing again."
            mc 1 u think "\"I didn't really study for it so my scores were pretty bad, I'm gonna have to put at least some effort into it to make sure I don't fail my midterms.\""
            show j 1 u judge at fdis
            j "\"T-They can't have been all that bad if you're lecturing me about it. What was it, seventy five?\""
            mc 1 u "\"Eighty six.\""
            show j 1 u wince at fdis, shake1
            $ renpy.pause (1.0)
            show j 1 u pout at fdis
            "I hear a pitiful choking sound."
            mc 1 u "\"You alright there?\""
            j "\"...\""
            "Oh-oh, he's gone silent."
            mc 1 u think "\"Uhhh... is something wrong?\""
            j "\"N-no... it's just that I've realized something...\""
            mc 1 u curious "\"Oh? What is it?\""
            j "\"...{w=2}"
            play sound "music/stab.ogg"
            show j 1 u fluster at fdis, shake1
            stop music2 fadeout 2.5
            play music3 "music/BGM/Mischief Maker.ogg" fadein 5.0
            extend " {size=+2}I'm stupid!{/size}\""
            mc 1 u shock "\"Wah!\""
            "Jun's sudden shrieking caught me by surprise and caused me to cry out."
            "A few heads turn our way, most of them looking curious at the sudden commotion in the back of the classroom."
            "To be honest, most people aren't doing their work either so they don't seem too upset at being interrupted."
            "Lucky for me."
            mc 1 u wince "\"What do you mean you're stupid? You're not stupid!\""
            "Jun buries his face on his arms and starts huffing."
            j "\"Yes I am. I studied all week and all I got was a forty eight. You didn't even pay attention in class and you got eighty six!\""
            mc 1 u shock "\"You studied all week and only got that grade? How?!\""
            play sound "music/stab.ogg"
            show j 1 u flustert at fdis, shake1
            j "\"Guh...\""
            "I run my mouth before I have time to think of what I'm saying."
            "Note to self: what I just said wasn't helpful. Please don't do it again."
            mc 1 u fsmile "\"I-I mean, Gee, Jun, I guess we'll just have to try harder for next time!\""
            show j 1 u annoyed at fdis
            j "\"Nice save, genius.\""
            "Guess I couldn't convince him with that one huh..."
            mc 1 u considerate "\"H-How about I help you study then? We're already going to have our first tests next month, I can help you boost your grade.\""
            stop music3 fadeout 2.5
            play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
            show j 1 u shock at fdis
            j "\"Really?!\""
            "I hesitantly nod, already regretting the situation I just got myself in."
            mc 1 u considerate "\"S-Sure. I used to help Shoichi study all the time when we were kids, I'm used to it.\""
            j "\"You did?\""
            "I nod."
            show j 1 u think at fdis
            j "\"But isn't Shoichi-san taking advanced classes? Doesn't that mean he's smarter than you?\""
            show j 1 u watch at fdis
            j "\"I mean, you always struck me as kinda dumb.\""
            play sound "music/stab.ogg"
            "Oof!" with hpunch
            "T-This guy..."
            "The fact that he can say these things without a single trace of malice or forethought just makes his words all the more devastating..."
            mc 1 u wince "\"Y-Yeah, I used to be a model student back when I was a kid, but I eventually got sick of studying all the time and started slacking off.\""
            mc 1 u "\"Shoichi, on the other hand, struggled to ever get more than sixty-points on a test. He barely passed the admission exams back in Junior High.\""
            show j 1 u think at fdis
            j "\"I dunno, that sounds a little hard to believe.\""
            mc 1 u considerate "\"H-Hey, I know that he's an honor student {i}now{/i}, but I swear that wasn't always the case.\""
            j "\"Hmm...\""
            show j 1 u watch at fdis
            j "\"If that's true then how does he get such good grades nowadays?\""
            mc 1 u avoid "\"Well, that's... Err... I'm not sure if he'd want me to tell you this.\""
            j "\"How come?\""
            "Oh boy, I just dug myself a pretty deep hole here."
            "I look away for a second, scratching the back of my neck."
            mc 1 u sigh "\"Shoichi and I were very different people when we were kids. Honestly, it's a bit hard to believe how much we've changed from when we were little.\""
            show j 1 u think at fdis
            j "\"Oh... I guess I can sorta get that... I mean, you went with me to my piano competition, right? I used to be much different back when I still competed.\""
            j "\"Hell, I even had a rival... {size=-4}Though I had no idea we were rivals.{/size}\""
            "..."
            "I guess... there's no harm telling him?"
            "I sigh, setting my gaming console down once more and leaning back on my chair."
            show j 1 u watch at fdis
            mc 1 u avoid "\"Alright, but if Shoichi ever finds out I told you about this, I'm toast. Are we understood?\""
            stop music2 fadeout 2.5
            play music3 "music/BGM/Mischief Maker.ogg" fadein 5.0
            show j 1 u happy at fdis
            j "\"Okay. I'll make sure to tell him you told me.\""
            mc 1 u shock "\"W-Wha-\""
            show j 1 u gentle at fdis
            "Jun giggles, winking at me."
            stop music3 fadeout 2.5
            play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
            j "\"Relax, I'm just joking. My lips are sealed!\""
            "This guy!" with hpunch
            mc 1 u annoyed "\"Don't do that again!\""
            "No matter how scary Saya or Keisuke are when they're angry, Shoichi is a million times worse."
            stop music2 fadeout 5.0
            "Ugh... it feels like it's been years since I last got him furious with me and still the memory is enough to make me shiver."
            mc 1 u sigh "\"Alright, where do I start...\""
            show j 1 u watch at fdis
            "Jun readjusts himself on his chair, looking at me with sudden interest."
            play music2 "music/BGM/Reminiscing - Piano.ogg" fadein 5.0
            mc 1 u "\"Despite what many people think, Shoichi was never a gifted student or athlete. It's actually the contrary, he's a very slow learner.\""
            mc 1 u think "\"If a regular person would take ten hours to learn something, Shoichi could easily take double that time to learn the same thing.\""
            mc 1 u "\"Ever since we were little, he was always grouchy and angry that other people didn't seem to need to put as much effort into things.\""
            mc 1 u wince "\"Because of that, he developed a very warped view of the world. He thought that, since he always had to work harder than everybody else, that other people were always slacking off.\""
            "... Man, even though this happened ten years ago, it really doesn't feel like it's been that long."
            mc 1 u sigh "\"He used to be very snippy, prideful and arrogant...\""
            mc 1 u sigh "\"And because he always felt like the other kids didn't work as hard as he did, he felt out of place.\""
            mc 1 u think "\"He ended up never having any friends. I'm pretty sure I was the first person to ever take an interest on him since... well, forever.\""
            show j 1 u think at fdis
            j "\"... I'm having trouble imagining Shoichi-san as anything other than a nice, caring person.\""
            show j 1 u watch at fdis
            "I'll admit that the concept of Shoichi being that different from how he is now is pretty alien to me."
            mc 1 u smile "\"Heh, tell me about it. He's nothing like the brat he used to be.\""
            mc 1 u considerate "\"Shoichi and I ended up being drawn to each other because we had similar opinions when it came to the concept of effort, but we were complete polar opposites.\""
            mc 1 u smile "\"I was a cheerful, happy kid that liked to excel at everything and worked very hard to do so.\""
            mc 1 u considerate "\"Shoichi was a sulky, inconsiderate brat who felt he was superior to everyone because he put in more work, even if that was just barely enough to let him keep up with others.\""
            "Hmm... when I say it like this, it kinda looks like I'm talking smack about him."
            "But man, I haven't thought about those days in a really long time."
            "I take a few seconds to organize my thoughts and notice Jun staring at me in anticipation."
            j "\"And? What happened that made you two change so much?\""
            "... I was so focused on remembering all this stuff that I kinda forgot I was supposed to be telling a story."
            mc 1 u wince "\"Err... a bunch of stuff happened over the years.\""
            mc 1 u wry "\"In Shoichi's case, I helped him come up with different ways to study and to practice that worked better for him.\""
            mc 1 u "\"Make no mistake, he still works ten times harder than anyone else I know, he just doesn't let it show.\""
            "In fact, he's the type of person who'd keep working until he passed out. Then when he woke up, he'd try to get back to work."
            mc 1 u considerate "\"He's the type that worries about other people before worrying about himself. He even goes as far as pretending to be okay when he's hurting just so no one will worry about it.\""
            mc 1 u wry "\"It's stupid and it makes me want to yell at him sometimes, but that's just the kind of person he is.\""
            show j 1 u wince at fdis
            "I shrug. I've already mostly accepted that this is just the kind of person he is."
            "Either way, he wouldn't do all these things if he didn't enjoy it so there's no point telling him to stop."
            "Jun, on the other hand, shifts uncomfortably on his seat."
            "I guess he's not as accepting of the idea as I am."
            mc 1 u happy "\"Shoichi ended up mellowing out over the years, mostly because Saya and I stuck by him all the time.\""
            mc 1 u avoid "\"Talking about our time as kids is kinda taboo for him nowadays, not even the two of us are allowed to speak of it.\""
            "Jun cocks his head to the side."
            "I can practically visualize the question mark popping up over his head."
            j "\"Why is that?\""
            mc 1 u wry "\"Well... Shoichi doesn't like the kind of person he used to be and he gets down whenever he's reminded of it.\""
            mc 1 u considerate "\"It's one of the reasons he always tries so hard to help everyone.\""
            mc 1 u think "\"He feels that as long as he's there for someone else, he can stop that person from ending up like he did as a child.\""
            mc 1 u smile "\"Essentially, he tries to be to others what Saya and I were for him.\""
            j "\"Oh...\""
            "An awkward silence hangs over us for a few seconds."
            j "\"I guess I really shouldn't have asked. I don't think I'll be able to act normal around Shoichi-san after hearing this. I'll be too worried about whether he's hiding something or not.\""
            mc 1 u considerate "\"I told you I probably shouldn't tell you this. You insisted.\""
            stop music2 fadeout 5.0
            "Although I probably didn't need to tell him the part about Shoichi hurting and not telling others."
            "That was too much information."
            show j 1 u considerate at fdis
            j "\"C-can we change the subject to something a little more... pleasant?\""
            mc 1 u wry "\"Sure. What do you want to talk about?\""
            show j 1 u think at fdis
            j "\"Well... after hearing this story about Shoichi-san, I kinda feel inspired. I want to try harder at something. All I need is to figure out what!\""
            mc 1 u think "\"... {w=2}How about you try harder at your studies?\""
            play sound "music/stab.ogg"
            show j 1 u wince at fdis, shake1
            play music2 "music/BGM/Little By Little I Walk.ogg" fadein 5.0
            j "\"Guh... I-I guess that's an option.\""
            mc 1 u annoyed "\"It's not {i}an{/i} option. It's the only option you have if you want to avoid flunking out of school and having to repeat your third year someplace else.\""
            show j 1 u avoid at fdis
            j "\"I-I definitely don't want that...\""
            mc 1 u smile "\"Then it's settled, I'm gonna help you study. Prepare yourself, you'll barely have time for anything else.\""
            show j 1 u wince at fdis
            j "\"N-no, that's too much, I don't think I could handle it!\""
            "I'll admit, tormenting Jun can be a little fun at times."
            mc 1 u happy "\"Nope, I'm not having any of it. I'm gonna turn you into an honor student just like I did with Shoichi.\""
            j "\"P-Please don't.\""
            "I laugh. Jun's expression is just too lovely when he's nervous like this."
            "Wait, isn't this the sort of thought a sadist would have?"
            "... Note to self: don't think things like this."
            show j 1 u wry at fdis
            j "\"Can we at least have some fun before you start tutoring me?\""
            mc 1 u "\"What do you mean?\""
            show j 1 u wince at fdis
            j "\"Well, if you're not gonna give me any time to enjoy myself, I figured I should at least go out one last time before we start doing this.\""
            "... I think he took me a little too serious there."
            "Eh, I'll roll with it."
            mc 1 u smile "\"Alright. What do you have in mind?\""
            show j 1 u think at fdis
            "It feels like I can almost see his brain processing and trying to come up with something."
            "It's kinda cute."
            show j 1 u gentle at fdis
            j "\"How about we go out this Saturday? I always wanted to go to the amusement park but my parents were always too busy to take me!\""
            mc 1 u fsmile "\"A-An amusement park?\""
            "... Isn't that sort of thing reserved for kids and couples?"
            show j 1 u smile at fdis
            j "\"Yeah. Is that a problem?\""
            "Jun stares at me with twinkling eyes filled with expectations."
            "... Crap, I can't say no to this adorable creature!"
            mc 1 u considerate "\"N-No, not at all. I'm gonna run this by the others and see if they're gonna be free on Saturday.\""
            show j 1 u wince at fdis
            j "\"O-Oh.\""
            "Jun's expression suddenly shifts."
            "For a split second, I could have sworn he looked disappointed."
            mc 1 u wry "\"Okaaay, now's my turn to ask. Is something wrong?\""
            j "\"N-No, it's just that...\""
            show j 1 u blush at fdis
            "He fidgets on his seat, looking down at the floor."
            "His cheeks start blushing lightly."
            j "\"I was hoping it'd be just the two of us.\""
            "?!" with hpunch
            "S-Shit, I think I just choked on my own saliva."
            show j 1 u wince at fdis, jumping
            j "\"O-Of course I don't mean l-like a date, t-that would be weird!\""
            "Noticing my reaction, Jun immediately interjects."
            "Crap, he's seeing me get nervous and he's getting nervous too."
            "Calm down, [povFirstName], you don't want to deal with Jun when he's freaking out!"
            mc 1 u wince "\"W-Why do you want it to be just the two of us?\""
            show j 1 u blush at fdis
            j "\"W-Well...\""
            "Jun blushes even more. Unable to sustain my gaze any longer, he turns his head away, looking to the side."
            j "\"I-It's kinda childish for a guy my age to want to go to an amusement park, right? I... I didn't want the others to know.\""
            mc 1 u shock "\"O-Oh!\""
            "... That explanation kinda makes sense."
            "Well, except for..."
            mc 1 u sigh "\"... If the idea of them knowing embarrasses you so much then why are you okay with asking me?\""
            "Jun turns to face me again, looking me right in the eye."
            "Even though his cheeks are burning red, he still manages to mumble out some words."
            j "\"B-Because I just feel like I can tell you this sort of stuff. I feel like you're the only person who wouldn't judge me for it. I guess I just really trust you, [povFirstName]-san.\""
            "!" with hpunch
            "Crap, I had to look away just now."
            "Those words... that expression... I couldn't help but blush just now."
            "I cover my mouth with my hand in an attempt to hide my blushing."
            "Still, I have my face turned away from Jun and I only look at him from the corner of my eyes."
            "I take a few seconds to compose myself. Have to make sure my voice doesn't break when I try to speak."
            mc 1 u considerate "\"I-If you really want to, then I don't mind taking you. T-This can be our secret.\""
            "C-Crap, these words are really embarrassing no matter how I think about it."
            "I'm not supposed to be saying this sort of thing to a friend."
            "No, scratch that. I'm not supposed to be saying this sort of thing to a {i}guy{/i}!"
            "Then, from the corner of my eyes, I see an image with enough destructive power to completely disarm me."
            show j 1 u happyb at fdis
            j "\"Thank you, [povFirstName]-san, you're really the best!\""
            "!"
            "W-What is this adorable creature?!" with hpunch
            stop music2
            jump Day10_Jun
        "Keisuke":
            scene black
            show k 1 c smile at five
            with fade
            "Agh, that's true. I agreed to go out with Kei-kun today."
            "But... ugh... my bed is so nice and warm, I don't want to get up..."
            "Maybe he'll let me skip this time?"
            "... Yeah, right. Even I know that would be a scummy thing to do."
            "Come to think of it, I don't even know where we're going."
            "Yeah, Kei-kun didn't really give me much information when he asked me to hang out with him..."
            scene SGateE with squares
            play music2 "music/BGM/Dog Days.ogg"
            "I remember I was already done with my club activities for the day and was about to head home."
            k 1 t "\"Senpai, wait!\""
            show k 1 t at fdis, five with moveiledis
            "I saw Keisuke running my way, still wearing his practice clothes and with his tennis bag hanging from his shoulders."
            mc 1 c "\"You need me for something, Kei-kun? Also, please don't call me \"senpai\".\""
            show k 1 t calm at fdis
            k "\"Sorry sorry, Coach insists I do when we're in practice and I haven't switched back to normal mode yet.\""
            show k 1 t smile at fdis
            k "\"I actually wanted to talk to you if that's okay.\""
            "I could see beads of sweat running their way down his forehead and onto his eyebrows."
            "Kei-kun had to wipe his face every few seconds due to just how much sweat there was."
            mc 1 c "\"Sure, I don't mind, but wouldn't you rather shower first? I'm actually surprised, don't you always shower after practice?\""
            show k 1 t sigh at fdis
            k "\"Yes, I do. But since you left practice before me, I didn't have a chance to ask you to wait around for me. If I had showered before running to find you, you'd have gone home already.\""
            "True, I don't usually wait around after practice and I don't like getting naked in public so I prefer just walking to my house and showering there."
            mc 1 c "\"Alright, I don't mind waiting around for you. You can go shower.\""
            show k 1 t avoid at fdis
            k "\"Oh, good. Feeling all this sweat running down my fur was starting to drive me crazy.\""
            show k 1 t at fdis, offscreenright with moveoledis
            hide k 1 t
            "And just like that, Kei-kun turned around and dashed back to the gym."
            "Somehow, it looked like he was running with a much bigger sense of urgency now that he was heading to the showers."
            "Never stand between a man and his shower."
            stop music2 fadeout 2.5
            scene IceCream with fade
            play music3 "music/BGM/In That Mood.ogg" fadein 5.0
            "Kei-kun insists that we come over to the expensive ice cream shop he likes so much."
            "Of course I object to it, given that this place is absurdly expensive and I can't pay for it."
            ".... Which only makes Kei-kun decide that he will treat me."
            mc 1 c sigh2 "\"I already told you, I don't need you to buy me ice cream.\""
            "Even though I've been going against it, Kei-kun still makes a point of coming over to the shop anyway."
            "And since it's not in my nature to simply walk away from someone in the middle of a conversation, I stupidly follow."
            show k 1 c worried at fdis, five with dissolve
            k "\"And I already told you I don't mind treating you. Come on, why do you even care, you know money is not an issue for me.\""
            mc 1 c avoid "\"You know I don't like people buying things for me. I don't want to take advantage.\""
            show k 1 c smile at fdis
            k "\"Yes, I know. And that's exactly why I want to treat you.\""
            mc 1 c wince "\"Wha- That doesn't even make sense!\""
            show k 1 c at fdis
            k "\"Really? It's quite simple.\""
            show k 1 c eyesc at fdis
            k "\"The fact that you don't expect nor want me to pay for things for you only makes it so I want to do so, because I know you're always hanging out with me for me, not my money.\""
            show k 1 c smile at fdis
            k "\"I suppose you could just say that I like honest people like you.\""
            "Jesus, I'm not used to seeing Kei-kun smile this much."
            mc 1 c avoid "\"Isn't that a contradiction?\""
            show k 1 c eyesc at fdis
            "He shrugs, walking over to the counter and placing an order."
            "Seems like today he's not just going to get some scoops."
            show k 1 c at fdis
            k "\"So what if it's a contradiction? It's just how I feel about it. People are weird like that.\""
            show k 1 c smile at fdis
            k "\"Ah yes, I'd like a strawberry yogurt sundae.\""
            "The lady behind the counter smiles and nods, getting right to it."
            k "\"Come on, get something. I insist.\""
            "Admitting defeat, I sigh, walking over to the counter to pick up a cup and scoop myself some ice cream."
            "Some ridiculously expensive ice cream."
            "If this were me treating someone, I'd be weeping every time they picked up another scoop..."
            k "\"Don't you want to try the sundae? It's really good too.\""
            mc 1 c think "\"Is it cheaper?\""
            show k 1 c at fdis
            k "\"No.\""
            mc 1 c "\"Then no.\""
            "... Is this how Jun feels when he goes out with us?"
            "I suddenly start reviewing all the times we hung out as a group, trying to think of how I could have made Jun uncomfortable."
            "I make a mental note to myself to try and go to places that don't require us to spend money in the future..."
            show k 1 c worried at fdis
            k "\"Jeez, I'm treating you anyway. You might as well just pick whatever you want.\""
            mc 1 c smile "\"Yes, and I want this.\""
            "I place the ice cream cup on top of a scale to be weighed."
            "I made sure to pick the minimum necessary not to have Kei-kun on my case about being stingy while at the same time not getting too much."
            "And yet the total still makes me want to weep."
            "Rich people venues are scary..."
            show cg3 with dissolve
            "After picking up our orders, we walk over to a nearby booth and take our seats, sitting directly across from each other."
            "Kei-kun wastes no time plunging his spoon in the soft, creamy ice cream."
            "Damn, I have to admit, that sundae does look good..."
            "No, I cannot be taken in by temptation!"
            mc 1 c curious "\"What was it that you wanted to talk to me about anyway?\""
            show k 1 c wince at fdis
            k "\"Hmm? Oh waighf.\""
            "Keisuke snaps back to reality, speaking up with his mouth still full of food."
            "His voice comes out funny."
            "For a boy raised in a rich household, he sure doesn't make much of a deal about table manners."
            show k 1 c at fdis
            k "\"I wanted to ask you to go out with me this Saturday.\""
            mc 1 c sigh "\"Go out with you? And you had to take me out for ice cream to do that? Couldn't you have just asked me at the school gate and saved yourself the trouble?\""
            show k 1 c calm at fdis
            "Keisuke shrugs."
            k "\"I wanted to bribe you with ice cream to increase my chances.\""
            "Bribe? You basically badgered me until I accepted the damn ice cream..."
            mc 1 c smile "\"... If you say so. Anyway, I suppose I have Saturday free... Yeah sure, why not? We rarely ever do anything with just the two of us. Might be an opportunity to know each other better.\""
            if day5 == "keisuke":
                show k 1 c smile at fdis
                k "\"You say that but you're also the only one of my friends to have ever visited my house.\""
                k "\"Pretty safe to say you already know me better than anyone else in our age group.\""
                "... That's sad."
                mc 1 c sigh "\"You know, a guy like you could have a ton of friends easily. Why do you only go out with us? We're clearly a bunch of weirdos.\""
                show k 1 c calm at fdis
                k "\"I could shoot that question right back at you.\""
                mc 1 c avoid "\"... Touché.\""
                "He chuckles and takes another spoonful of ice cream."
                "At least he seems to be enjoying himself."
            else:
                show k 1 c avoid at fdis
                k "\"I hadn't really thought about that. I just know that I have a few boring errands to run and I thought having someone else around when I do them might make the day a little more tolerable.\""
                mc 1 c sigh "\"... \"Boring errands\"? Is this why you wanted to \"bribe\" me with expensive ice cream?\""
                show k 1 c smile at fdis
                "He smirks, playing around with the empty spoon on his mouth."
                k "\"Saw right through it didn't you?\""
                "I'll give it to him, he's a little more devious than I thought."
                mc 1 c "\"What sort of errands are those anyway?\""
                "He shrugs."
                k "\"It's boring stuff, there's no point to me telling you anyway.\""
                show k 1 c at fdis
                k "\"Although I did decide to take the chance to do some shopping for myself so at least there's that.\""
                "Nodding, I decide to change the subject."
                "There's no way I'm gonna get anything else pertaining to these errands out of him so I might as well just try to have a normal conversation."
            mc 1 c "\"By the way, how are you feeling about practice lately?\""
            mc 1 c smile "\"Especially now that we've been paired up as training partners.\""
            if day5 == "shoichi":
                show k 1 c sigh at fdis
                k "\"You mean how Coach just decided out of the blue that you had to partner up and play with me every day and you've whined and pouted about it ever since?\""
                k "\"I feel peachy.\""
            else:
                show k 1 c smile at fdis
                k "\"I still don't get why you decided to partner up with me out of the blue but... it's what I've been wanting since I first joined the club so I'm not gonna complain.\""
            show k 1 c at fdis
            k "\"But to answer your question as plainly as I possibly can:"
            show k 1 c sigh at fdis
            extend " I hate it!\""
            "Kei-kun sets his spoon down, pushing his now empty sundae cup away and sighing."
            show k 1 c at fdis
            k "\"Don't get me wrong, it's all I've wanted from our tennis club but... God, I just hate losing.\""
            show k 1 c avoid at fdis
            k "\"And the way you do short work of me every time... I thought I had figured out a way to deal with you at first and it seemed like it was working, but...\""
            if day5 == "shoichi":
                show k 1 c sigh at fdis
                k "\"Ugh... why did Coach have to interrupt that first match of ours? Stupid water pipe bursting...\""
                "He grumbles unhappily, quietly sulking in his seat."
            else:
                show k 1 c sigh at fdis
                k "\"Ugh... why did I have to injure my wrist there of all times? If that match hadn't been interrupted, I'm sure I would have won...\""
                show k 1 c avoid at fdis
                "He grumbles unhappily, quietly sulking in his seat."
                "Well, not that he's wrong anyway. I don't think I would have managed to win that one."
                "But the extra time I had to compose myself was enough for me to get my head back in its place and turn the match around when we resumed."
                "Kei-kun didn't get a single game after we restarted."
            show k 1 c worried at fdis
            k "\"Seriously, how can we play so many matches like that and I cannot manage to come out of it with a single set? Seriously, that's demoralizing...\""
            mc 1 c smile "\"Well, this is what you asked me for since you first joined the club. Now you have it. Suck it up.\""
            show k 1 c sigh at fdis
            k "\"Yeah yeah, no need to tell me twice. I just needed to get it out of my system.\""
            "He sighs, putting his elbow on the table and leaning his chin on his hand, absentmindedly looking out the window."
            show k 1 c at fdis
            mc 1 c "\"By the way, Kei-kun, I don't think I've ever asked... Why do you even play tennis in the first place?\""
            mc 1 c think "\"I mean, don't get me wrong, you're definitely one of the hardest workers in the club and you're certainly a good player, but... You just don't have the body for it. You have to know you're going to have a hard time going pro, right?\""
            show k 1 c sigh at fdis
            k "\"I like tennis. Shouldn't that be reason enough?\""
            mc 1 c think "\"... To attempt to go pro on one of the hardest, most competitive sports in the world. All of this against your family's wishes? Sure, that's reason enough.\""
            show k 1 c avoid at fdis
            k "\"Yeah yeah, my reasons are more complicated than that but I don't feel like talking about them right now.\""
            show k 1 c wry at fdis
            k "\"Sorry, [povFirstName]-san, I mean no offense by that.\""
            mc 1 c smile "\"Ah... Don't worry about it. Sorry to have asked such an awkward question in the first place.\""
            show k 1 c at fdis
            "Kei-kun shrugs and turns his gaze to the window once more, staring at the scenery outside."
            mc 1 c "\"... You really like to look out the window, huh?\""
            "Without looking at me, Keisuke fires back an answer."
            k "\"I like looking at the cars passing by. For some reason it relaxes me. Does that make me weird?\""
            mc 1 c think "\"I think it makes you just as weird as people who enjoy watching clouds. Or stars.\""
            show k 1 c calm at fdis
            k "\"So you're saying that it does make me weird. Noted.\""
            "If it weren't for the smirk on his face, I'd have a hard time telling whether he's joking or not."
            "His sense of humor is a bit... puzzling at times."
            show k 1 c smile at fdis
            k "\"Well, I guess I've already said my piece. I think I'll head home now.\""
            mc 1 c smile "\"Alright. I'll wait with you until your car comes pick you up.\""
            k "\"I appreciate it.\""
            hide cg3 with dissolve
            "Kei-kun pays our tab and we exit the shop."
            stop music3 fadeout 5.0
            jump Day10_Keisuke
            scene
