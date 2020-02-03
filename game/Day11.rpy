label Day11:
    window hide
    scene April27 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene SGate with fade
    window show
    $ date = "day11"
    play music2 "music/BGM/Autumn Day.ogg" fadein 5.0
    "Huh?"
    "The school gate looks awfully empty right now."
    "I arrived for class about ten minutes early but there doesn't seem to be much of anyone here."
    "It's almost like a ghost town."
    ukn "\"[povFirstName]?\""
    show s 1 u at fdis, five with moveiledis
    "I hear someone calling out to me and, surely enough, it's Shoichi."
    mc 1 u curious "\"Shoichi? You're here pretty late. Don't you usually get to school two hours before class?\""
    show s 1 u sigh at fdis
    s "\"I do... that's why I'm arriving right now.\""
    mc 1 u curious "\"What? But it's 8:20.\""
    s "\"... No. It's 6:20.\""
    mc 1 u shock "\"Wait, what?!\""
    play sound "music/phonebeep.ogg"
    "I check the time on my phone and, sure enough, it says 8:22."
    mc 1 u wince "\"But... But... My phone says it's 8:22!\""
    show s 1 u at fdis
    s "\"Let me see that.\""
    "Shoichi picks up my phone and fiddles with the settings."
    show s 1 u think at fdis
    s "\"Ah, I see the problem.\""
    mc 1 u smile "\"You got the times mixed up and came to school late?\""
    show s 1 u sigh at fdis
    s "\"No.\""
    "Shoichi extends his hand, holding my phone to show me the screen."
    show s 1 u think at fdis
    s "\"Your phone seems to think you're in Thailand, so it's showing the local time.\""
    mc 1 u shock "\"What?!\""
    "I snatch my phone from his hand and start checking it."
    mc 1 u shock "\"How did this happen?!\""
    show s 1 u at fdis
    s "\"Your guess is as good as mine. Virus, software glitch, bad GPS app. The list is a mile long.\""
    show s 1 u think at fdis
    s "\"You should really deactivate automatic timezone detection, that sort of thing can just go haywire sometimes. If anything on your phone goes into conflict with it, it just fails.\""
    mc 1 u annoyed "\"Well, gee, thanks for the late warning.\""
    show s 1 u sigh at fdis
    s "\"Hey, this isn't my fault. Don't yell at me.\""
    mc 1 u sigh "\"Ugh, sorry. It's just...\""
    "... Two hours of sleep... lost."
    show s 1 u smile at fdis
    s "\"Well, it's not gonna hurt you to be early for once.\""
    mc 1 u sigh2 "\"... I'm gonna go to the rooftop and get some sleep.\""
    show s 1 u shock at fdis
    s "\"Whoa, hang on!\""
    play sound "music/tap.ogg"
    show s 1 u sigh at fdis:
        ease .2 zoom 1.5 xoffset -30 yoffset 200
    "Just as I try to turn around and walk away, Shoichi quickly grabs me and spins me back to face him."
    s "\"You're already here, you might as well stay up and do something.\""
    mc 1 u think "\"Let me guess, you're gonna tell me to study.\""
    show s 1 u sigh:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    "He scratches the back of his head, thinking his answer over for a few seconds before sighing."
    s "\"Well... I was going to suggest it but...\""
    show s 1 u wry at fdis
    s "\"At this point, my words would only fall on deaf ears wouldn't they.\""
    mc 1 u smile "\"Oh, good. You {i}can{/i} learn!\""
    show s 1 u considerate at fdis
    s "\"Har har, very funny. I don't appreciate the sass, mister.\""
    mc 1 u happy "\"It was done with the best of intentions!\""
    show s 1 u smile at fdis
    s "\"Sure it was.\""
    show s 1 u think at fdis
    s "\"Well, you might as well socialize, then.\""
    mc 1 u sigh "\"... With who?\""
    show s 1 u at fdis
    s "\"Half of your classmates arrive early to school. I also know for a fact that Urushihara usually arrives at this time.\""
    show s 1 u smile at fdis
    s "\"And if you want, I only have to give some papers a look over at the student council room and I'll probably be free in ten or twenty minutes.\""
    mc 1 u think "\"Well... okay. I guess we could have some fun before classes.\""
    show s 1 u happy at fdis
    s "\"You bet.\""
    show s 1 u smile at fdis
    s "\"Either way, I need to get going right now. I'll see you in a few. Do try to stay awake until I come back.\""
    mc 1 u think "\"Pfft, as if I'd fall asleep in twenty minutes.\""
    s "\"Heh, I'll hold to that. Bye!\""
    mc 1 u smile "\"Yeah, see you later, Shoichi.\""
    show s 1 u smile at offscreenright with moveoridis
    "Well... I guess this morning might not suck as hard."
    "I still have no idea what messed with my phone's time."
    "I guess this is why I didn't see mom or Aki when I was getting ready for class. They were probably still asleep."
    "And here I thought I was the last one to leave the house."
    stop music2 fadeout 5.0
    scene SClass with fade
    play sound "music/slidingdoor.ogg"
    "I decide to drop my bag off at my desk before I set out to look for Kei-kun."
    "As I step inside the room, I notice a few people are already in the class."
    "Among then, I recognize someone that I definitely did not expect to see here at this time."
    mc 1 u shock "\"Jun?!\""
    play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    show j 1 u shock at fdis, five with dissolve
    "The tiger snaps back to reality, looking to the side to see me standing by the doorway."
    show j 1 u happy at fdis
    j "\"Oh, [povFirstName]-san, good morning!\""
    show j 1 u shock at fdis
    j "\"Wait, what are you doing here so early?\""
    show j 1 u at fdis
    play sound "music/chairscoot.ogg"
    "I pull up my chair and take a seat."
    "Good thing my desk is right next to his."
    mc 1 u sigh "\"You know that should be my line, right? I can count on my fingers how many times I've seen you {i}not{/i} be late for class.\""
    show j 1 u pout at fdis
    j "\"Oh, come on, now you're exaggerating. I usually arrive at least five minutes before class starts.\""
    mc 1 u sigh2 "\"Alright alright, I'll give you that much. Still, for you to be two hours early... that's surprising.\""
    show j 1 u think at fdis
    j "\"Hmm... maybe just a little.\""
    mc 1 u smile "\"Oh, so even you recognize that it's unusual?\""
    show j 1 u watch at fdis
    j "\"I guess. It's not like I was early because I wanted to.\""
    mc 1 u smile "\"Did your phone's clock go haywire too?\""
    show j 1 u think at fdis
    j "\"Not really..."
    show j 1 u wince at fdis
    extend " I tried studying for a bit last night and... well, I ended up falling asleep.\""
    j "\"Because of that, I woke up earlier than I wanted to.\""
    mc 1 u think "\"You? Studying? That's new.\""
    show j 1 u pout at fdis
    j "\"H-hey, don't act so surprised!\""
    mc 1 u wince "\"Gah, sorry sorry.\""
    show j 1 u watch at fdis
    j "\"Well, anyway, since I was already up, I decided to come to school early.\""
    show j 1 u bored at fdis
    j "\"Me getting here early today was just a coincidence. I don't plan on doing it again.\""
    mc 1 u "\"Well, at least you {i}tried{/i} to study on your own... Though I'm a bit curious as to why. What brought this on?\""
    if day10 == "jun":
        show j 1 u think at fdis
        j "\"I remembered what you said about me needing to study more.\""
        show j 1 u wince at fdis
        j "\"That last mock exam just showed how bad I'm doing right now. I can't flunk on my third year, otherwise it's bye-bye to any chance I'd have of going to Germany.\""
        mc 1 u smile "\"Huh, that's surprisingly responsible of you.\""
        show j 1 u annoyed at fdis
        j "\"Why \"surprisingly\"?\""
        mc 1 u think "\"Oh, uhm... I just meant that I didn't expect you to try studying on your own.\""
        show j 1 u bored at fdis
        j "\"Yeah yeah. Whole lot of good that did me in the end, though. I completely messed up my sleep schedule.\""
        mc 1 u smile "\"Oh, it's not that bad, you'll get used to it.\""
        show j 1 u wince at fidget
        j "\"I'm not sure that I want to get used to it.\""
        "Jun fidgets in his spot, his tail lashing out behind him."
        "I guess talking about studying is just stressful for him?"
        mc 1 u "\"Really? Because you're gonna have to study whether you like it or not.\""
        mc 1 u sigh "\"So in that case, wouldn't it be better if you didn't hate every second of it.\""
        show j 1 u wince at shake1
        j "\"Guh... I guess.\""
        mc 1 u smile "\"There you go, good boy!\""
        show j 1 u annoyed at fdis
        j "\"I'm not a dog!\""
        mc 1 u laugh "\"Hahaha, I'm joking, I'm just joking!\""
        show j 1 u bored at fdis
        j "\"You should really work on your sense of humor.\""
        show j 1 u watch at fdis
        mc 1 u sigh "\"You're one to talk!\""
        show j 1 u happy at fdis
        j "\"What are you talking about? My sense of humor is great!\""
        "... No, it's not."
        "But then again, I guess I should just change the subject here."
        "I don't intend on validating his ridiculous claims, but I also don't want to deal with him pouting."
        show j 1 u watch at fdis
        mc 1 u smile "\"You do remember I promised to help you study, right?\""
        show j 1 u wince at fdis
        j "\"Ugh, I thought we were done with that subject.\""
        mc 1 u sigh2 "\"We're not. How about I help you study this weekend?\""
        j "\"I-If you want to...\""
        j "\"I was kinda looking forward to enjoying this weekend though.\""
        mc 1 u "\"Tough luck.\""
        j "\"Fine, fine. I get it, we'll study.\""
        "Well, it's not gonna be all bad. There are some areas that I need to brush up on anyway."
    else:
        show j 1 u wince at fdis
        j "\"I got some pretty bad grades on that last mock exam.\""
        j "\"At first I didn't really care about it, but...\""
        j "\"I realized that if I got those sorts of grades on our midterms, I could potentially flunk out of my last year.\""
        mc 1 u think "\"Oh. We certainly don't want {i}that{/i}.\""
        j "\"Right. So I decided that I should try studying some more.\""
        show j 1 u watch at fdis
        mc 1 u smile "\"How often do you study right now? Maybe I can try helping you come up with a better routine.\""
        show j 1 u avoid at fdis
        j "\"W-well...\""
        mc 1 u sigh "\"... I swear to God, if you tell me that you don't study I'll smack you upside the head.\""
        show j 1 u cshock at fdis, shake1
        j "\"Awawawa, I swear I study!\""
        mc 1 u "\"How often?\""
        show j 1 u wince at fdis
        j "\"O-once a month?\""
        play sound "music/slap.ogg"
        show j 1 u cshock at fdis, shake1:
            ease .2 zoom 1.5 xoffset 0 yoffset 230
        "I smack his forehead, making sure to put enough power to make it sting."
        "I'm not crazy enough to hit him as hard as I can."
        show j 1 u cshock:
            ease .5 zoom 1.0 xoffset 0 yoffset 0
        j "\"Kyaaaaah! You said you'd only do it if I didn't study at all!\""
        mc 1 u scorn "\"If you only study once a month then you might as well not study at all!\""
        show j 1 u wince at fdis
        j "\"Guuuh... b-but...\""
        mc 1 u "\"Yes?\""
        j "\"Studying is so boring!\""
        play sound "music/slap.ogg"
        show j 1 u cshock at fdis, shake1:
            ease .2 zoom 1.5 xoffset 0 yoffset 230
        j "\"Kyaaaah, my poor forehead!\""
        mc 1 u scorn "\"Take your studies more seriously!\""
        show j 1 u wince at fdis
        j "\"I will, I will. Please stop smacking me!\""
        show j 1 u wince at fdis:
            ease .5 zoom 1.0 xoffset 0 yoffset 0
        "I lean back on my chair, sighing."
        mc 1 u sigh "\"This isn't a joke, Jun. Our school is pretty demanding when it comes to grades. Even a genius would have trouble passing if he only studied this much.\""
        mc 1 u sigh2 "\"And we both know you're not a genius... At least not when it comes to academics.\""
        show j 1 u avoid at fdis
        j "\"S-sorry. I'll try to study more often.\""
        mc 1 u doom "\"You better. Or else I'm going to pull your tail as hard as I can for each subject you get a failing grade on during the midterms.\""
        show j 1 u cshock at fdis, shake1
        j "\"Kyaah, stay away from my tail!\""
        "That seems to have driven the message home, at least."
        show j 1 u wince at fdis
        mc 1 u think "\"Well, I guess that's enough of a lecture for now.\""
        j "\"R-really?\""
        mc 1 u smile "\"Yeah. Don't worry, I'm not gonna smack you anymore.\""
        j "\"You won't pull my tail either?\""
        mc 1 u smile "\"I won't.\""
        show j 1 u sigh at fdis
        j "\"Oh, thank God.\""
    show j 1 u watch at fdis
    j "\"By the way, [povFirstName]-san, what are you going to do to pass time until class starts?\""
    show j 1 u bored at fdis
    j "\"I've been bored out of my mind for the past twenty minutes since I arrived here.\""
    mc 1 u think "\"Well, Kei-kun usually arrives at this time so I was thinking of hanging out with him until class starts.\""
    mc 1 u smile "\"But I can hang around here with you if you'd prefer that.\""
    show j 1 u think at fdis
    j "\"Hmm...\""
    show j 1 u happy at fdis
    j "\"I guess I wouldn't mind going to see Urushihara-san.\""
    mc 1 u think "\"Well, at least you're cheery about it.\""
    show j 1 u watch at fdis
    j "\"Shouldn't I be?\""
    mc 1 u sigh "\"That's not what I- Ah, you know what, never mind. Let's check if Kei-kun's in his class already.\""
    show j 1 u smile at fdis
    j "\"Okay.\""
    stop music2 fadeout 5.0
    scene SCorridor with fade
    "We go downstairs to the junior's classrooms."
    j 1 u watch "\"Do you know which one is Urushihara-san's?\""
    mc 1 u "\"Yeah. He's in class 2-B.\""
    "It should be right around... here!"
    scene SClass2 with fade
    play sound "music/slidingdoor.ogg"
    "A few heads turn as soon as I open the door."
    "Some curious second-years look at us with curiosity, exchanging whispers here and there."
    "Well, I guess it's not unusual to have someone from a completely different year walk into someone else's classroom."
    "Now, where did Kei-kun sit again?"
    play music2 "music/BGM/Spring Classroom.ogg" fadein 5.0
    k 1 u worried "\"[povFirstName]-san and Kobayashi-san?\""
    show k 1 u at fdis, five with dissolve
    "Ah, I see Keisuke sitting in the center of the room, next to a group of students."
    "That's why I didn't see him at first."
    k "\"What are you two doing here?\""
    show k 1 u worried at fdis
    k "\"No, wait, why are you two even at school? Aren't you guys always late?\""
    mc 1 u sigh "\"Excuse you, I'm always on time.\""
    show k 1 u at fdis, three with move
    show j 1 u annoyed at fdis, seven with moveiridis
    j "\"Yeah. And I arrive on time fifty percent of the time!\""
    show k 1 u sigh at fdis
    k "\"So you're saying that you're late about half the time... sounds like a commendable track record.\""
    "I see that he hasn't allowed his early morning routine to affect his sunny disposition."
    mc 1 u think "\"Eh, why we arrived early isn't really important right now.\""
    mc 1 u smile "\"And to answer your previous question: We came here to look for you.\""
    show k 1 u at fdis
    k "\"Oh, is that so?\""
    show j 1 u watch at fdis
    j "\"Oh, yeah. [povFirstName]-san said he was thinking of hanging out with you until classes start.\""
    show j 1 u happy at fdis
    j "\"I just came here to tag along!\""
    show j 1 u smile at fdis
    mc 1 u smile "\"If you're not too busy, that is.\""
    show k 2 u annoyed at fdis
    k "\"Hmm... I guess I've got time. I was going to review yesterday's work before class started but... I don't really have to.\""
    show k 1 u smile at fdis
    k "\"I'm already doing well as is anyway.\""
    show j 1 u watch at fdis
    j "\"Hey, Urushihara-san, how much did you score on the last mock exam?\""
    show k 1 u at fdis
    k "\"Me? Ninety four. Why?\""
    show j 1 u cshock at fdis
    j "\"Waaaah, everyone in this group is a brainiac except for me!\""
    k "\"I wouldn't really go that far. I just study a lot.\""
    show j 1 u wince at fdis
    j "\"Really? How often?\""
    show k 1 u eyesc at fdis
    k "\"At least three hours a day after school.\""
    show j 1 u shock at fdis
    j "\"W-wow. That's a lot.\""
    if day10 == "jun":
        mc 1 u smile "\"You should probably start following his example if you want to salvage those horrible grades of yours.\""
        show j 1 u wince at fdis
        j "\"Guuh...\""
        show k 1 u worried at fdis
        k "\"Are they really that bad?\""
        show j 1 u sigh at fdis
        j "\"No comment.\""
        k "\"I-I see.\""
        show k 1 u wince at fdis
        k "\"H-hey, but those were just mock exams. They don't really mean anything!\""
        "Huh. Looks like Kei-kun got the message if he's trying to comfort Jun."
        show k 1 u at fdis
        show j 1 u wince at fdis
        j "\"No, it's fine, Urushihara-san. I know there's a lot I need to work on.\""
        show j 1 u watch at fdis
        show k 1 u smile at fdis
        k "\"Well, the first step to fixing your problems is realizing they exist. So you're already on the right path, keep it up!\""
        show j 1 u happy at fdis
        j "\"That's true. Thanks, Urushihara-san!\""
        "... What's with that speech that sounds like it was taken right from an alcoholics recovery program?"
    else:
        mc 1 u think "\"Compared to how little you do, it certainly is.\""
        show j 1 u wince at fdis
        j "\"Guuh...\""
        show k 1 u at fdis
        k "\"What about you, Kobayashi-san?\""
        j "\"I-I don't want to say...\""
        show k 1 u worried at fdis
        k "\"Huh?\""
        mc 1 u smile "\"How about we just change the subject?\""
        show k 1 u wince at fdis
        "Kei-kun stares at us both with a confused look on his face."
        show j 1 u sigh at fdis
        j "\"Agreed.\""
    show j 1 u at fdis
    show k 1 u annoyed at fdis
    k "\"Ahem. Well, getting back to the topic that first brought you two here."
    show k 1 u at fdis
    extend " How about we go someplace else, then?\""
    show j 1 u watch at fdis
    show k 1 u avoid at fdis
    k "\"I think my classmates are staring a little too hard at you two. Mostly at [povFirstName]-san. {size=-4}Especially the girls.{/size}\""
    mc 1 u smile "\"Sure. How about we go to the roof?\""
    show k 1 u sigh at fdis
    k "\"Students aren't allowed on the roof.\""
    mc 1 u smile "\"Exactly.\""
    show j 1 u wince at fdis
    show k 1 u worried at fdis
    k "\"I don't like where this is going.\""
    j "\"We're going to get in trouble, aren't we?\""
    play sound "music/slidingdoor.ogg"
    scene SCorridor with fade
    "Just as we walk out of the classroom, a fox spots us leaving and rushes over to us with a big smile on her face."
    show ayako at five
    show j 1 u watch at fdis, eight
    show k 1 u at fdis, two
    with dissolve
    ay "\"Ah, [povFirstName]-kun. Just who I wanted to see.\""
    ay "\"And good morning to you two too.\""
    show j 1 u happy at fdis
    show k 1 u smile at fdis
    j "\"Oh, morning, Kitsunegawa-san.\""
    k "\"Hello, Kitsunegawa-san.\""
    ay "\"My, I really thought I was seeing things when I saw Jun-kun walk into the classroom half an hour ago, but then when you came in too, [povFirstName]-kun... I couldn't believe my eyes.\""
    show j 1 u sigh at fdis
    show k 2 u gentle at fdis
    j "\"We were just a little early today, is all. {size=-4}Why does everyone keep fixating on that?{/size}\""
    mc 1 u smile "\"Pretty much what Jun said. Don't get used to it.\""
    "Class Rep giggles, her voice carrying lightly through the air."
    show k 1 u at fdis
    show j 1 u watch at fdis
    mc 1 u smile "\"Well, doesn't really matter. You said you wanted to see me?\""
    ay "\"Oh, yes. I was working on plans for our class' event at this year's school festival.\""
    show j 1 u think at fdis
    j "\"Already? Isn't the festival in November?\""
    show j 1 u watch at fdis
    mc 1 u "\"It's true that most schools do it in November, but ours hosts it at the end of May.\""
    mc 1 u think "\"Which is still a little over one month away. Why are you already working on it?\""
    ay "\"We can't very well expect to put up a good event if we don't take the time to prepare, can we?\""
    show j 1 u think at fdis
    j "\"But we haven't even voted on what we're going to do yet?\""
    show j 1 u watch at fdis
    show k 1 u worried at fdis
    k "\"You guys haven't? Our class had their vote just last week.\""
    j "\"Really, what did you guys vote for doing?\""
    show k 1 u at fdis
    k "\"An event called \"Dinner Through the Globe\". We're basically going to open a restaurant that serves traditional cousine from all over the world.\""
    ay "\"Oh, that sounds very interesting. To be honest, my idea was also related to food.\""
    mc 1 u smile "\"Oh? You have an idea already?\""
    "She giggles, looking at me as if she were saying \"Well, duh!\"."
    ay "\"Of course I do, silly. This is why I wanted to see you. I hear you're a pretty good cook yourself.\""
    mc 1 u fsmile "\"I-I try. Why, you're not gonna ask me to cook for our event are you?\""
    ay "\"Oh no, no need. If my idea goes through, I'm more than comfortable doing the cooking myself. But I wanted you to taste test for me.\""
    ay "\"Of course, you two are welcome to join too. The more the merrier.\""
    show j 1 u think at fdis
    j "\"Wouldn't the elder Nezumiro be a better taste tester than us? He's a real foodie and all.\""
    ay "\"Uhm, well... Last time I tried having him taste test something he ended up eating all the food I had and left none for the other testers so I'd rather pass on him.\""
    show j 1 u wince at fdis
    j "\"O-oh.\""
    mc 1 u sigh "\"That sounds like Gin alright.\""
    show k 1 u avoid at fdis
    k "\"I don't even know him all that well and I can say that it sounds like him.\""
    show k 1 u at fdis
    ay "\"Yes, well, this was two years ago so forgive me for not knowing this at the time.\""
    show j 1 u watch at fdis
    mc 1 u smile "\"Yeah, no worries. Sure, we were just going to kill time chatting anyway so I have no reason not to join.\""
    show j 1 u bright at fdis
    show k 1 u smile at fdis
    j "\"Me too, I love taste testing!\""
    k "\"Well... I suppose I have nothing better to do. If you'll have me even though I'm from another year entirely then, sure, I'm in.\""
    ay "\"Wonderful! I already have most of it prepared. Come with me to the cooking club room!\""
    scene SCooking with fade
    "To be perfectly honest, I didn't even know our school had a cooking club."
    "It turned out to be on a separate building from the one that houses our classrooms and most of the clubs."
    show ayako at fdis, five with moveiledis
    ay "\"Give me a second to finish preparing and I'll give you guys today's test dishes.\""
    mc 1 u smile "\"Alright.\""
    show ayako at offscreenright with moveoridis
    "She quickly starts fiddling around with multiple pots, plates and other kitchen utensils."
    "The kitchen has so many different smells wafting through the air that I can't even tell what's what."
    show j 1 u watch at fdis, seven
    show k 1 u at fdis, three
    with dissolve
    j "\"I have to say, I didn't even know this school had a cooking club. I'm a bit surprised.\""
    mc 1 u sigh "\"Of course it has a cooking club. Every school has one!\""
    show j 1 u wince at fdis
    j "\"O-oh, is that so?\""
    show k 1 u sigh at fdis
    k "\"[povFirstName]-san, don't even try. I can tell from the look on your face that you had no idea either.\""
    show j 1 u shock at fdis
    j "\"Wha- He didn't know?\""
    mc 1 u shock "\"Busted, huh?\""
    show j 1 u pout at fdis
    j "\"And you actually tried to lecture me on it? [povFirstName]-san, you're mean!\""
    mc 1 u "\"I wouldn't really call that a lecture...\""
    k "\"He was just looking for a chance to show off.\""
    mc 1 u wince "\"K-Keisuke, shut up!\""
    show k 1 u smile at fdis
    k "\"Hey, you brought this on yourself.\""
    show k 1 u smile at fdis, two
    show j 1 u pout at fdis, five
    with move
    show ayako at eight with moveiridis
    ay "\"Oh my, is something going on here? Jun-kun looks pretty upset.\""
    show j 1 u annoyed at fdis
    j "\"No, it's... it's nothing. [povFirstName]-san is just being his usual self.\""
    mc 1 u sigh "\"I'm not sure whether I should be offended by that or not.\""
    k "\"Let's just get back to the matters at hand. Are you finished preparing, Kitsunegawa-san?\""
    ay "\"Oh, yes, I just ne-\""
    play sound "music/ringtone.ogg"
    show j 1 u shock at fdis, jumping
    show k 1 u wince at fdis, jumping
    k "\"Is that...\""
    show j 1 u watch at fdis
    mc 1 u considerate "\"Sorry, my phone's ringing. Excuse me one sec.\""
    show ayako at offscreenright
    show j 1 u watch at fdis, offscreenright
    show k 1 u at fdis, offscreenright
    with moveoridis
    play sound "music/phonebeep.ogg"
    mc 1 u think "\"Hello?\""
    s 1 u think "\"[povFirstName], it's me.\""
    mc 1 u smile "\"Ah, Shoichi. Hey, are you done with your stuff already?\""
    s 1 u happy "\"Yup, I rushed through it as fast as I could. Where are you right now?\""
    mc 1 u "\"Oh, I'm in the cooking club's room.\""
    s 1 u think "\"The cooking club? Why?\""
    mc 1 u smile "\"Class Rep asked us to taste test some things for the idea she's going to pitch for the school festival.\""
    s 1 u happy "\"Oh, that sounds interesting. I'm in.\""
    mc 1 u wince "\"Wait, but I d-\""
    play sound "music/phonebeep.ogg"
    "..."
    "He shut off the phone in the middle of his sentence."
    "He completely cut me off."
    show k 1 u at fdis, two
    show j 1 u watch at fdis, five
    show ayako at eight
    with moveiridis
    ay "\"Is something the matter?\""
    mc 1 u considerate "\"Well... You wouldn't happen to have enough for one more person, would you?\""
    k "\"Urata's coming over?\""
    mc 1 u wry "\"Yeah... he shut the phone off on my face.\""
    show j 1 u think at fdis
    j "\"Doesn't really sound like Shoichi-san.\""
    mc 1 u sigh "\"Shutting the phone off on someone's face? Nah, that's totally like him. He's just clueless.\""
    show j 1 u wince at fdis
    j "\"Oh, I didn't know.\""
    show j 1 u watch at fdis
    ay "\"Well, regardless, I don't mind him joining us. In fact, it should be even better!\""
    show k 1 u sigh at fdis
    k "\"Just promise to not let him get close to the cooking utensils. If he decided to cook something for us, I'm afraid we might not leave this room alive.\""
    ay "\"Oh, don't worry, I'm well aware of his... shortcomings.\""
    show j 1 u wince at fdis
    j "\"I really hope I never actually get to taste one of his concoctions...\""
    show k 1 u worried at fdis
    k "\"I really wish I had never tasted one of them...\""
    mc 1 u sigh "\"Okaaay, that's enough of a depressing conversation for now.\""
    scene SCooking with fade
    "We spend the next five minutes fooling around and waiting for Shoichi to arrive."
    play sound "music/slidingdoor.ogg"
    show s 1 u smile at fdis, two with moveiledis
    s "\"Sorry I took so long.\""
    "He walks in nonchalantly, neatly closing the door behind him."
    stop music2 fadeout 2.5
    show k 1 u at fdis, four
    show j 1 u watch at fdis, six
    show ayako at eight
    with dissolve
    play music3 "music/BGM/Hanging Out.ogg" fadein 5.0
    ay "\"Good morning, Shoichi-kun.\""
    show s 1 u happy at fdis
    s "\"Morning, Ayako-chan."
    show s 1 u smile at fdis
    extend " Oh, Jun-kun? Now that's a surprise, didn't expect to see you here so early.\""
    show j 1 u annoyed at fdis
    j "\"Why does everyone keep saying that?\""
    show k 1 u eyesc at fdis
    k "\"Because it's true.\""
    show j 1 u wince at fdis
    j "\"Guuh...\""
    show j 1 u watch at fdis
    show k 1 u at fdis
    ay "\"Good morning to you too, Shoichi-kun.\""
    "Ayako giggles, somewhat amused by Jun's annoyance."
    k "\"Urata.\""
    show s 1 u at fdis
    s "\"Urushihara.\""
    "They both nod to each other, acknowledging each other's presence."
    show s 1 u smile at fdis
    s "\"So, what are you guys working on here?\""
    mc 1 u smile "\"Like I said, Class Rep wants us to taste-test for her.\""
    "She sighs, leering at me with a grumpy look on her face."
    mc 1 u wince "\"W-what?\""
    ay "\"Honestly, [povFirstName]-kun, how many times do I have to tell you to call me by my name?\""
    mc 1 u wince "\"O-oh...\""
    "I keep forgetting about that."
    ay "\"Honestly, this happens almost every day. Get a grip already.\""
    mc 1 u wince "\"Sorry.\""
    ay "\"Well, no matter. What he said is correct, Shoichi-kun. I want you boys to do some taste testing for me. I already have the dishes prepared, I was just waiting for you to arrive.\""
    show s 1 u happy at fdis
    s "\"That's great. Let me have'em!\""
    show k 1 u smile at fdis
    k "\"At least someone's excited.\""
    show s 1 u smile at fdis
    s "\"Of course I'm excited. It's food. I'm always excited about food.\""
    mc 1 u think "\"And this is why you're the most unpicky eater in our group.\""
    show s 1 u happy at fdis
    s "\"Yup, I'll eat almost anything as long as it's actually edible!\""
    "I guess this means that, on some subconscious level, he's aware that the food he makes isn't edible."
    show s 1 u smile at fdis
    ay "\"Well, I hope you boys will like it, then. Here's the first dish.\""
    show j 1 u shock at fdis
    show s 1 u shock at fdis
    show k 1 u shock at fdis
    "She plops down four plates in front of us, all of them garnished beautifully with a..."
    mc 1 u wince "\"Is this... a walnut?\""
    show j 1 u wince at fdis
    show s 1 u wince at fdis
    show k 1 u worried at fdis
    j "\"It doesn't look like a walnut. It's slimy and gross.\""
    s "\"It certainly looks a little weird, that's for sure.\""
    "Ayako-san laughs, her mouth opening up in a big, happy grin."
    ay "\"Oh, just trust me on this. I made sure to taste everything before serving so I {i}know{/i} it's delicious!\""
    k "\"If... if you say so. {size=-6}Oh God, please don't let this be a repeat of the Urata experience...{/size}\""
    "Good thing Shoichi didn't hear that, otherwise they would start an argument."
    j "\"Well, I... I guess I can give it a try.\""
    mc 1 u wry "\"On three?\""
    "They all nod."
    mc 1 u considerate "\"One, two... three!\""
    "The four of us stab our slimy balls of brown meat, cutting away a piece and quickly popping them in our mouths before we have time to change our minds."
    "It's... it's squishy when you bit into it! What the hell is th-"
    show j 1 u shock at fdis
    show s 1 u shock at fdis
    show k 1 u shock at fdis
    j "\"...!\""
    s "\"...!\""
    k "\"...!\""
    "... This..."
    ay "\"Well?\""
    show j 1 u shockb at fdis
    show k 2 u gentleb at fdis
    show s 1 u flattered at fdis
    mc 1 u shockb "\"This... this is delicious!\""
    j "\"Y-yeah. I didn't expect that! It's a bit tangy and... and spicy. It's not really hot, but it really has a lot of spices to it.\""
    s "\"Damn, I have to admit this is delicious too.\""
    k "\"Yeah... I can't lie, this thing is great.\""
    show j 1 u watch at fdis
    show k 1 u sigh at fdis
    show s 1 u at fdis
    k "\"Which, of course, only scares me more. What {i}is{/i} this, exactly? I realize now that you never actually told us.\""
    "She chuckles."
    ay "\"Oh, yes, that's true.\""
    ay "\"What you boys just ate was boiled pork brain marinated in soy sauce, yuzu juice, sakê and brine!\""
    show j 1 u shock at fdis
    show k 1 u serious at fdis
    show s 1 u blank at fdis
    "..."
    j "\"...\""
    s "\"...\""
    k "\"...\""
    show j 1 u cshock at fdis, shake1
    j "\"{size=+4}I just ate an animal's brain?!{/size}\"" with hpunch
    s "\"Fascinating.\""
    show k 1 u worried at fdis
    k "\"I was afraid it'd be something like that. This definitely felt like some sort of animal organ.\""
    j "\"Puh, puh, puh!\""
    show j 1 u wince at offscreenright with moveoridis
    "Jun kneels next to the trash can, hugging it close to his body and spitting in it repeatedly."
    ay "\"Oh, come on, Jun-kun. You said it yourself that it was delicious!\""
    j 1 u wince "\"It's disgusting! Oh God, I need water. I need to wash it out of my mouth!\""
    ay "\"Does it really matter what it was as long as it was good?\""
    j 1 u wince "\"Of {i}course{/i} it matters. The real question is: What is the matter with you?!\""
    ay "\"Aww, this way you're going to hurt my feelings.\""
    "The big smile on her face tells me that she doesn't mean it."
    show s 1 u sigh at fdis
    s "\"Ayako-chan, while my repulse for this doesn't quite reach the same level as Jun-kun's, I would have appreciated being warned beforehand.\""
    k "\"Same here. I mean, don't get me wrong, rich people eat disgusting stuff like this all the time so I've been forced to try this kind of stuff every now and then.\""
    show k 1 u sigh at fdis
    k "\"But that still doesn't mean I enjoy it.\""
    ay "\"Alright, alright. I'm sorry to not have told you guys beforehand, I was just scared you might not try it if you knew.\""
    mc 1 u sigh2 "\"Ayako-san, with all due respect... What the hell kind of idea are you trying to pitch for our class' event in the school festival?\""
    "She smiles widely, looking incredibly proud of herself."
    ay "\"I want to make a booth called \"Weird foods you'd never know are delicious\"!\""
    mc 1 u avoid "\"I think the only thing that's weird here is your head.\""
    show j 1 u wince at fdis, six with moveiridis
    j "\"Nope, the food is definitely weirder.\""
    mc 1 u "\"You're done spitting stuff out?\""
    j "\"I coughed so much trying to get all the stringy bits out of my mouth that I got an urge to throw up. So I stopped.\""
    show k 1 u worried at fdis
    k "\"You're the one who's going to end up making yourself sick if you abuse your throat that much.\""
    j "\"Message received, I'll stop for now.\""
    "Class Rep's gaze softens a bit when she sees how bummed out Jun is."
    ay "\"I'm sorry, Jun-kun, I really should have told you beforehand. I thought once you tasted it and saw how good it was, you wouldn't mind knowing what it was at first.\""
    show j 1 u sigh at fdis
    j "\"It's... it's fine. I'll get over it, I think.\""
    show j 1 u watch at fdis
    ay "\"I suppose you guys aren't willing to keep testing for me now right?\""
    s "\"Well... I won't lie, it was pretty good. And I don't really mind it all that much. Like I said, I'm not a picky eater.\""
    k "\"Yeah. As long as you tell us what it is beforehand, I'm good. That way I can at least choose whether I want to try it or not.\""
    ay "\"Alright, I'll make sure to warn you guys first... And what about you two?\""
    "She looks over at Jun and me who are standing right next to each other."
    mc 1 u "\"I don't really mind. I liked the food, and I've already had some weird stuff to eat before so it doesn't really gross me out that much.\""
    "She then turns to look at Jun with eyes filled with expectation."
    "We all follow suit, staring at him and waiting to hear his answer."
    show j 1 u wince at fdis
    show k 1 u at fdis
    show s 1 u at fdis
    j "\"Damn it, peer pressure... Fine, I'll eat.\""
    ay "\"Yay, thank you so much!\""
    play sound "music/fabric.ogg"
    show j 1 u cshock at fdis
    "She gets so excited that she immediately pounces Jun, hugging him."
    j "\"Awawawa, bad touch. Bad touch!\""
    "She pulls away from him, still smiling."
    ay "\"Oh, sorry. Got a little carried away there.\""
    show j 1 u sigh at fdis
    j "\"It's fine, just don't do it out of nowhere. You caught me by surprise.\""
    show s 1 u smile at fdis
    s "\"But seriously. \"Bad touch\"? What are you, a fifth grader?\""
    show j 1 u blush at fdis
    j "\"S-shut up. It's what my parents taught me to say when somebody touches you without your permission.\""
    mc 1 u think "\"That's weird. You never did this before and I'm sure we all touched you at one point or another.\""
    show j 1 u wince at fdis
    j "\"None of you literally pounced me out of nowhere. I panicked.\""
    show j 1 u watch at fdis
    ay "\"Sorry. I'll try to control myself.\""
    show j 1 u think at fdis
    j "\"It's fine. As long you tell me beforehand, I don't mind getting hugged.\""
    show j 1 u watch at fdis
    mc 1 u "\"So, what's next?\""
    ay "\"Oh, right!\""
    "As if she had only just remembered that we're supposed to be trying out some food, she dives back behind the counter to pick up another pan."
    "She neatly plates the food and pops it down in front of us."
    mc 1 u fsmile "\"Is this...\""
    show j 1 u wince at fdis
    j "\"A cracker with... meat paste?\""
    show s 1 u wince at fdis
    s "\"It smells ripe, though. Almost... spoiled.\""
    show k 1 u worried at fdis
    k "\"Oh, God. Is this what I think it is?\""
    "Class Rep's eyes light up when she hears Keisuke's words and she leans in, curiously waiting to hear his thoughts."
    "We all follow suit, waiting for him to reveal what kind of foulness has befallen us."
    k "\"This... this is Surströmming pâté, isn't it?\""
    show j 1 u think at fdis
    j "\"Su... Suming?\""
    ay "\"Surströmming. And yes, good job, Kei-kun!\""
    show k 1 u sigh at fdis
    k "\"There's no way I'm eating that.\""
    mc 1 u curious "\"Uhm... care to enlighten us? What's Su... this thing?\""
    show k 1 u avoid at fdis
    k "\"It's basically canned rotten fish.\""
    show j 1 u wince at fdis
    show s 1 u sigh at fdis
    j "\"Ewww!\""
    ay "\"It's not {i}rotten{/i}. It's {i}fermented{/i}!\""
    s "\"It {i}smells{/i} rotten. Dear God, the smell is so putrid and acidic that it's making my eyes water.\""
    ay "\"Really? I thought I'd gotten rid of the odor when I prepared the pâté. I guess huskies have better noses.\""
    "I pick up the cracker and take a whiff of it."
    "!!!"
    "I drop the thing back on the plate, gagging."
    mc 1 u wince "\"Oh God, you're right. This smells awful!\""
    show k 1 u sigh at fdis
    k "\"I guess this is one situation where I can be glad I wasn't born with a particularly good nose.\""
    j "\"Same for me. I don't have a sharp sense of smell, even for a tiger.\""
    s "\"Yeah, well, [povFirstName] doesn't either and even he was able to smell this thing.\""
    show j 1 u think at fdis
    j "\"Yeah, but he's a dog.\""
    mc 1 u sigh "\"That's speciest. It's true... but speciest.\""
    show j 1 u watch at fdis
    ay "\"Come on, guys. Just try it. I mixed it with lots of spices and herbs, not to mention some vegetables that I pureed to mix it in.\""
    "Shoichi picks up the cracker, grimacing as he brings it close to his face."
    show s 1 u wince at fdis
    s "\"It's... ugh, this smells so bad... But alright, I'll... I'll give it a shot.\""
    show j 1 u shock at fdis
    show k 1 u shock at fdis
    "He closes his eyes and pops the whole thing in his mouth, chewing really fast."
    mc 1 u shock "\"W-whoa, are you insane?\""
    "We all stand there, staring at him slack-jawed."
    "Shoichi's face begins to relax. He finished chewing and swallows his food."
    show j 1 u watch at fdis
    show s 1 u think at fdis
    s "\"Well... it's by no means haute cuisine, but...\""
    show k 1 u sigh at fdis
    k "\"What do {i}you{/i} know of haute cuisine?\""
    show s 1 u sigh at fdis
    s "\"Shut up.\""
    "Friendly as usual, I see."
    show s 1 u smile at fdis
    s "\"But... yeah, it's good. It definitely doesn't taste anything like it smells, oddly enough.\""
    show j 1 u wince at fdis
    j "\"Really? Cause I have a hard time imagining it being any good.\""
    ay "\"Aww, that hurts me deeply, Jun-kun!\""
    show j 1 u avoid at fdis
    j "\"S-sorry.\""
    "Class Rep chuckles, waving him off."
    show j 1 u watch at fdis
    ay "\"Oh, don't worry about it. I was just joking.\""
    ay "\"Still, why don't you three give it a try?\""
    show k 1 u wince at fdis
    show s 1 u at fdis
    k "\"... There's still something I'm worried about though.\""
    ay "\"What is it?\""
    k "\"Well... a recently opened can of Surströmming is said to have one of the most putrid smells in the world... and yet this kitchen smells pristine.\""
    show k 1 u sigh at fdis
    k "\"I doubt you'd have been able to get rid of the smell so quickly, so what did you do?\""
    ay "\"Oh, that. The smells was quite strong, that's for sure. But since I was serving it as pâté, I decided to prepare it at home and just garnish it on the plate here.\""
    show k 1 u wince at fdis
    k "\"You prepared it... at your house?\""
    ay "\"Yes, just last night. My parents screamed at me for an hour because of it. The smell is still lingering in the kitchen. {size=-4}My mother threw away the sauce pot that I used to prepare it.{/size}\""
    show s 1 u sigh at fdis
    show j 1 u wince at fdis
    "I can totally imagine how her parents must have reacted. And considering how strong this thing with just a little bit of it smelled... imagining what her house smells like right now is making me wince."
    "In fact, it looks like it's making all four of us wince."
    show s 1 u at fdis
    ay "\"Anyway, go ahead and give it a try!\""
    show k 1 u avoid at fdis
    show j 1 u avoid at fdis
    "Jun, Keisuke and I trade suspicious looks with each other."
    "Keisuke nods to us and reaches out for his plate. As if that had given him encouragement enough, Jun follows suit."
    "I decide to try it too, if only so I wouldn't be the sole refuser."
    "Jun was right. This is peer pressure."
    "We all pop it into our mouths at the same time..."
    "... This... is passable."
    mc 1 u wince "\"I'm not sure I would go so far as to call it {i}good{/i}. It's not something I'd go out of my way to eat again. But it's definitely not {i}bad either{/i}.\""
    show j 1 u think at fdis
    j "\"Yeah, I agree. {size=-4}The taste kind of lingers in the mouth though.{/size}\""
    show k 1 u smile at fdis
    k "\"At least it's not rancid. {size=-4}It's actually quite nice.{/size}\""
    ay "\"See? I knew you'd like it!\""
    "Class Rep looks incredibly pleased that we didn't have anything bad to say about it."
    ay "\"So, are you guys ready for the next dish?\""
    show j 1 u cshock at fdis
    mc 1 u shock "\"Wait... {i}there's more?!{/i}\""
    show k 1 u worried at fdis
    show s 1 u wince at fdis
    ay "\"Of course there's more. I still have eight more dishes for you guys to try. This is supposed to be food for an entire event!\""
    "Oh dear God, we're going to be stuck here eating terrifying food for the next hour aren't we?"
    stop music3 fadeout 5.0
    scene SClass with fade
    play sound "music/schoolbell.ogg"
    "..."
    "I lie half-dead on top of my desk, lazily waiting for the end to arrive and free me from this torment."
    show j 1 u watch at fdis, five with dissolve
    "..."
    "I don't even have to be looking at him to feel Jun's gaze focused on the back of my head."
    j "\"...\""
    mc 1 u sigh "\"...\""
    j "\"...\""
    "I lift my head up from the table and look him square in the eyes."
    mc 1 u wince "\"Yes? Do you need me for something?\""
    show j 1 u smile at fdis
    play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    j "\"Oh, you're still alive. Good!\""
    mc 1 u annoyed "\"... Is this a joke?\""
    show j 1 u happy at fdis
    j "\"Maybe. Who knows.\""
    "I sigh, letting my head fall back to the desk once more."
    show j 1 u watch at fdis
    j "\"You seem pretty out of it.\""
    mc 1 u sigh2 "\"Today was {i}exhausting{/i}!\""
    show j 1 u think at fdis
    j "\"Really? I thought it was pretty normal.\""
    show j 1 u watch at fdis
    mc 1 u sigh "\"Not the classes themselves. The classes were fine. It was just... everything.\""
    show j 1 u think at fdis
    j "\"Ah, yes. The elusive \"everything\". Tiring us out, ruining our days, setting fire to our crops, stealing our wives and killing our children. How dare he.\""
    mc 1 u sigh "\"Don't you snark me.\""
    show j 1 u happy at fdis
    j "\"I'm just trying to cheer you up!\""
    mc 1 u avoid "\"You're doing a piss poor job at it.\""
    show j 1 u think at fdis
    j "\"Maybe you're the one doing a piss poor job at being cheered up.\""
    mc 1 u sigh "\"... Are you going to keep up with these terrible attempts at sassing me until I get up from my desk?\""
    show j 1 u bright at fdis
    j "\"Oh, good. You got the message!\""
    mc 1 u sigh2 "\"Fine, fine."
    play sound "music/fabric.ogg"
    show j 1 u smile at fdis
    mc 1 u "\"There, I got up. Are you happy?\""
    show j 1 u happy at fdis
    j "\"Very!\""
    show j 1 u smile at fdis
    j "\"So, are you heading for practice now?\""
    mc 1 u think "\"I guess... It wouldn't go well with my coach if I skipped practice two days before the start of the prefectural tournament.\""
    show j 1 u shock at fdis
    j "\"Oh, it's this weekend already? Man, time goes fast.\""
    mc 1 u "\"I guess. It runs pretty close to the start of the school year, which is good because schoolwork isn't particularly heavy at this time.\""
    show j 1 u happy at fdis
    j "\"Well, I guess I already know what I'll be doing this weekend!\""
    mc 1 u smile "\"... Planting banana trees at your uncle's farm?\""
    show j 1 u pout at fdis
    j "\"No, you idiot! I'm gonna go cheer you on! {size=-4}And my uncle doesn't own a farm.{/size}\""
    mc 1 u smile "\"Huh... I think this is the first time you've ever called me an idiot.\""
    mc 1 u happy "\"Could I expect you to start baring your fangs at me more often?\""
    show j 1 u sigh at fdis
    j "\"Yeah yeah. I guess I don't feel the need to force myself to be overly polite with you anymore.\""
    show j 1 u watch at fdis
    j "\"I mean, don't get me wrong, I don't like insulting people or being rude to anyone. I'm just saying that if you do or say something stupid, I'm gonna call you out on it.\""
    mc 1 u smile "\"Ah, yes, the true mark of friendship. Kinda-sorta-maybe-somewhat insulting your friends whenever they do something stupid by calling them horrible names such as \"silly\" or \"goof\".\""
    show j 1 u sigh at fdis
    j "\"{i}Now{/i} who's being sassy?\""
    mc 1 u happy "\"Shut up, I deserve this.\""
    show j 1 u watch at fdis
    j "\"By the way, is anyone else going to be cheering you on this weekend? Your family, maybe?\""
    mc 1 u "\"Aki also has his own competition to take part in, and my mom is gonna be busy with work this weekend.\""
    show j 1 u wince at fdis
    j "\"Really? Even on the weekend?\""
    mc 1 u sigh "\"Her work is very demanding. It was the only way to keep both me and Aki cared for.\""
    j "\"I'm really sorry to hear.\""
    show j 1 u watch at fdis
    j "\"What about Shoichi-san, Mizoguchi-san and Urushihara-san?\""
    mc 1 u think "\"Uhm... Shoichi is definitely gonna come to watch. Saya and Keisuke are taking part in the same competition so they kinda have to be there..\""
    show j 1 u think at fdis
    j "\"Oh yeah, that's true.\""
    show j 1 u happy at fdis
    j "\"Well, at least you won't be alone. That's pretty neat, right?\""
    mc 1 u smile "\"It's okay. Nothing special. I'm used to it by this point.\""
    show j 1 u bored at fdis
    j "\"Gee, you could stand to be a little bit more excited.\""
    mc 1 u think "\"... Weeee, my friends are going to come over...\""
    show j 1 u annoyed at fdis
    j "\"...\""
    j "\"Point taken.\""
    mc 1 u happy "\"You know, you don't have to act constantly cheerful all the time.\""
    show j 1 u watch at fdis
    j "\"Who says I'm acting?\""
    mc 1 u wry "\"I dunno. You seem to be trying too hard.\""
    show j 1 u wince at fdis
    j "\"R-really? I was just trying to cheer you up.\""
    mc 1 u smile "\"I'm fine. I don't need to be cheered up... but thank you for the gesture anyway.\""
    show j 1 u happy at fdis
    j "\"Of course!\""
    show j 1 u smile at fdis
    j "\"I'm gonna head to the music room to practice. Do you plan on leaving practice early or can I run into you at the regular time that your club stops practicing?\""
    mc 1 u smile "\"The regular time is fine if you want to walk home with me.\""
    show j 1 u happy at fdis
    j "\"Alright. Then I'll see you later, [povFirstName]-san!\""
    mc 1 u happy "\"See ya.\""
    play sound "music/slidingdoor.ogg"
    show j 1 u smile at offscreenright with moveoridis
    "Jun walks out of the room, leaving me standing by myself, looking down at my bag."
    "Eh... most of everyone's already left the classroom. Other than a few stragglers like myself, there's no one left here."
    "People really leave fast."
    stop music fadeout 5.0
    scene SCourt with fade
    "Huh. The courts are surprisingly empty for a Thursday."
    "Actually, they're {i}too{/i} empty. More than half of our members are absent."
    "Where the hell is everyo-\""
    play sound "music/tap.ogg"
    sa 1 t laugh "\"Hey!\""
    mc 1 t shock "\"Gaah, what the hell?!\"" with hpunch
    play music2 "music/BGM/Dazzling Sunlight.ogg" fadein 5.0
    show sa 1 t at fdis, five with dissolve
    "Saya stands there, looking at me as if I were crazy."
    sa "\"Jesus, calm down. It's just me.\""
    mc 1 t wince "\"Don't... don't just walk up on someone like that.\""
    show sa 1 t pout at fdis
    sa "\"Hey, it's not my fault. I tried calling you but you didn't listen.\""
    mc 1 t sigh "\"O-oh, is that so?\""
    show sa 1 t bored at fdis:
        ease 1.0 zoom 1.5 xoffset 0 yoffset 250
    "She frowns, leaning closer to my face."
    mc 1 t fsmile "\"S-Saya?!\""
    sa "\"You look so... bleh.\""
    mc 1 t annoyed "\"Well, jeez, thank you. You look lovely today.\""
    "She shakes her head in negative."
    show sa 1 t bored at fdis:
        ease 0.5 zoom 1.0 xoffset 0 yoffset 0
    sa "\"No, not like that. Just... your face looks so awful.\""
    mc 1 t sigh "\"Alright, what did I ever do to you that you're suddenly insulting me so much.\""
    show sa 1 t complain at fdis
    "She groans, rubbing the bridge of her nose with frowned brows."
    sa "\"Again, not like that. I just mean that you don't look good. Are you alright?\""
    mc 1 t "\"Yeah, I'm fine. Just feeling a little under the weather.\""
    show sa 1 t bored at fdis
    sa "\"Is it because of the competition this weekend?\""
    "... Perceptive as always."
    mc 1 t sigh "\"No. Like I said, I'm fine.\""
    sa "\"And yet when you say \"I'm fine\", I get so sad that I want to off myself.\""
    show sa 1 t sigh at fdis
    sa "\"Seriously, you're a terrible liar sometimes.\""
    mc 1 t avoid "\"Look, I'm... I'm alright.\""
    show sa 1 t bored at fdis
    sa "\"You're not feeling the pressure?\""
    mc 1 t sigh "\"Pressure? What pressure? I've been the undisputed champion of the prefecturals for the past five years. I think I'll manage.\""
    show sa 1 t at fdis
    sa "\"I know. All the more reason for you to be under pressure?\""
    mc 1 t sigh2 "\"Wha- How is that {i}more{/i} reason?\""
    sa "\"[povFirstName], seriously, stop trying to lie to me. You and I both know that you're not fooling me.\""
    "She puts her hands on her hip, leaning a little to the side as if to emphasize her point."
    show sa 1 t talk at fdis
    sa "\"Being the champion for so long puts you under a lot of stress, because everyone will be expecting you to win again and you're afraid that you might lose.\""
    show sa 1 t think at fdis
    sa "\"Not only that, count the fact that you've been under performing a lot more lately and, boom, recipe for stress.\""
    mc 1 t "\"Well, doesn't it all sound so simple when you say it.\""
    show sa 1 t talk at fdis
    sa "\"That's because it's true.\""
    mc 1 t sigh "\"That's because you're crazy.\""
    "I walk over to where Coach is in an attempt to walk out of this conversation, but Saya seems to follow me around."
    show sa 1 t sigh at fdis
    sa "\"Ugh, you always do this, you know? It wouldn't kill you to open up a bit.\""
    show m 1 u smile at offscreenleft
    mc 1 t annoyed "\"Can I just practice in peace?\""
    show sa 1 t bored at fdis, seven
    show m 1 u smile at three
    with move
    m "\"What's going on here?\""
    "Coach overhears the last part of our conversation after excusing the player he was talking to and turns his attention to us."
    "I swear, his figure is so imposing and exhales an aura of respect... so unlike the actual person."
    mc 1 t sigh "\"Nothing. Saya's decided that I'm under stress, which I'm not, so now she's hounding me until I admit to it.\""
    "He frowns, crossing his arms."
    m "\"You {i}are{/i} under stress.\""
    show sa 1 t laugh at fdis
    sa "\"Hah, told you!\""
    mc 1 t sigh2 "\"What? Not you too!\""
    show sa 1 t at fdis
    "The big crocodile sighs, rubbing his eyes in exasperation."
    m "\"[povFirstName], I've been your coach since your first year here. And I've seen how you used to play back in Junior High. I know for a fact that you're underperforming because of stress.\""
    mc 1 t avoid "\"I'm... I'm fine.\""
    m "\"Sure. Keep saying that enough times and you just might fool someone... probably a toddler, but who's keeping track?\""
    mc 1 t sigh2 "\"Are you two going to gang up on me now or what?\""
    m "\"No one's ganging up on you, but you're stubborn as a mule. You think I can't recognize when someone's slacking off in practice?\""
    "I raise my brow, shooting him a dubious glance."
    mc 1 t annoyed "\"Really? This coming from you? You're notorious for skipping practice.\""
    "Coach smiles."
    m "\"Yes, but see, I'm not a {i}player{/i}.\""
    mc 1 t sigh2 "\"... That's rich.\""
    m "\"Seriously, why did you think I even invited Morisaki and the others over? I thought playing against someone that's already at a world level might give you that spark back.\""
    mc 1 t shock "\"Really? You went through all that trouble just because of me?\""
    "He shrugs, looking completely nonchalant about it."
    m "\"For the most part. I won't lie and pretend it didn't benefit some of our other players as well. But you're definitely the one that benefited the most from it.\""
    mc 1 t curious "\"I am?\""
    m "\"Oh, yes. I think this was the first time I've actually seen you improve since I've become your coach. You can't imagine how frustrated I was getting such a jewel in the rough only to see it refuse to be polished for over two years.\""
    "Jeez, he makes me sound so bad..."
    m "\"Now, I have no doubt that you have the skills to dominate at the next tournament, but I have {i}every{/i} doubt that you'll fail to show them.\""
    mc 1 t sigh "\"H-hey! Do you really have that little faith in me?\""
    m "\"With all honesty? Yes. Trying to put it nicely? Also yes.\""
    mc 1 t annoyed "\"*grumbles*\""
    play sound "music/tap.ogg"
    "He puts a hand on my shoulder, for sure trying to comfort me."
    m "\"Don't take it personally, kid. As long as you can surpass that mental block you've got going on for the past few years, I'm sure you'd be able to do well again.\""
    mc 1 t sigh "\"You speak as if I haven't been doing well. You forget that I was twice the national champion in junior high? Or that I've been 2nd place for the past three years?\""
    m "\"All impressive achievements on their own, sure. At least the two national championships. I'm a little skeptical on the past three years though.\""
    mc 1 t "\"Why?\""
    "He scratches his chin, taking a pause whilst musing over his next words."
    m "\"I believe you could have done so much better. In fact, I believe that if you actually played to your full potential, you could probably be the champion as is.\""
    "I raise an eyebrow at him."
    mc 1 t think "\"Really? Are you perhaps forgetting about Takagi? The {i}other{/i} genius player that's been taking Japan by storm and comfortably beating everyone else.\""
    play sound "music/tap.ogg"
    "Coach snorts, giving me a few more taps on the shoulder."
    m "\"I never said it'd be easy. Just that it'd be feasible. Sure, you could stand to improve more and that would definitely increase your chances, but I still think things would be so much easier if you just... lightened up.\""
    "I roll my eyes, groaning."
    mc 1 t sigh2 "\"\"Lighten up\"? You have any more sage advice that will magically make me get over all these assumed problems you keep insisting I have?\""
    "Coach sighs."
    m "\"You really are one tough nut to crack. You still deny it after everything I've said?\""
    mc 1 t "\"Yes.\""
    show sa 1 t sigh at fdis
    "Both him and Saya, who had stayed out of the conversation so far, sigh."
    sa "\"See? I told you he's stubborn.\""
    mc 1 t annoyed "\"You told him? So you've been talking about me behind my back. That's awful!\""
    show sa 1 t bored at fdis
    sa "\"I talk to coach about {i}everyone{/i} in the club, it's kind of my job as the captain. Don't be such a diva.\""
    mc 1 t annoyed "\"*grumbles*\""
    show sa 1 t at fdis
    "Coach shakes his head sideways."
    if day5 == "shoichi":
        m "\"There isn't much I can do if you keep being this difficult. I can offer you the tools you need to improve yourself but I can do the work for you. And we both know maintaining your mental health is a big part of the game.\""
        m "\"You won't get anywhere if you just turn a blind eye to it.\""
        show m 1 u smile at offscreenleft with moveoledis
        "Coach turns around and walks away, leaving both Saya and I standing around completely dumbfounded."
        show sa 1 t shock at fdis
        sa "\"Wha- W-wait, Coach!\""
        show sa 1 t shock at fdis, five with move
        mc 1 t shock "\"Whoa- Saya, wait!\""
        "I grab her arm before she can run off."
        show sa 1 t at fdis
        sa "\"What is it?\""
        mc 1 t wince "\"Uhm... where is everyone? Barely half of our members came in today.\""
        show sa 1 t think at fdis
        sa "\"Oh.\""
        "Saya looks around, following my gaze."
        show sa 1 t talk at fdis
        sa "\"That's right, I forgot to tell you. The members that aren't taking part in the prefecturals this weekend were excused from club activities for today and tomorrow.\""
        mc 1 t shock "\"What? Why?!\""
        sa "\"It's so the ones taking part have better access to the training equipment and to Coach's help. Even for him, it's hard to keep an eye on literally everyone at the same time.\""
        mc 1 t sigh "\"As if he even bothered to actually do his job.\""
        show sa 1 t at fdis
        sa "\"... I really think you should give the man a chance, you know. I get the feeling he's not as bad as you make him sound.\""
        mc 1 t "\"I'll have to see it to believe it.\""
        "Saya shrugs."
        sa "\"Well, suit yourself. There are still a few things that I'd like to discuss with Coach. And then I have to do a few more rounds around the courts to see if anyone needs help.\""
        show sa 1 t talk at fdis
        sa "\"Talk to you later.\""
        show sa 1 t talk at offscreenleft with moveoledis
        "..."
        "Sighing, I reach into my bag and grab my racket."
        "I don't really feel like practicing right now..."
    else:
        m "\"I don't even know what's the point of us having this conversation right now. You already admitted to needing help a while ago, remember?\""
        mc 1 t shock "\"I... When did I do that?\""
        "He snorts."
        m "\"When you took Keisuke as your training partner.\""
        mc 1 t wince "\"Wait, I... I never told {i}you{/i} that!\""
        m "\"Ah, so you admit that you did tell {i}someone{/i} that!\""
        mc 1 t shock "\"Wait, wh- Wait...\""
        "He lifts an eyebrow, smiling deviously at me."
        mc 1 t wince "\"Did you-\""
        m "\"I just played you, boy. Not like it was particularly hard either.\""
        mc 1 t wince "\"But... but...\""
        play sound "music/tap.ogg"
        m "\"Don't worry about it, kid. As long as you're trying to sort yourself out, I won't say anything. Just come to me if you need my help. That's what I'm here for after all.\""
        "..."
        mc 1 t sigh "\"... Fine.\""
        "He smiles, bellowing out a laugh and giving me an incredibly overacted thumbs up."
        "He really is an eccentric one."
        m "\"Alright. I'll leave you to your practice. Have fun!\""
        show m 1 u smile at left with move
        mc 1 t wince "\"W-wait, you're not gonna tell me what to do?!\""
        "He stops in his tracks and turns around, looking at me in confusion."
        m "\"Tell you what to do? Do I need to?\""
        mc 1 t sigh2 "\"Well, you've been my coach for two years already and you've {i}never{/i} altered my training menu. I've been using the same one for the past two years.\""
        m "\"That's because I don't need to.\""
        mc 1 t wince "\"W-what?\""
        m "\"You didn't notice? Your current training menu is already perfect for the playstyle that you want to pursue, so I never felt any need to change it.\""
        m "\"Of course, if you had decided to change things up then I'd direct you, but for the most part, you've been spot-on in everything.\""
        mc 1 t wince "\"Wait, so... you haven't been avoiding directing me because you're lazy?\""
        "He laughs, scratching his neck."
        m "\"Oh, make no mistake, I {i}am{/i} lazy... but I also take my job seriously. If there was anything I could have suggested, a different exercise or a new approach, then I would have.\""
        m "\"But you've been doing everything right for the most part. Your problem isn't physical, it's mental. And given that I'm not a psychologist or a psychiatrist, I can't do much to help you there.\""
        m "\"Well, of course, if you want my help with something, you need only ask. But until then, as long as you're taking your training seriously and not making any mistakes, I have no reason to step in and correct you.\""
        mc 1 t avoid "\"I... I see...\""
        "I never knew..."
        show m 1 u smile at offscreenleft with moveoledis
        show sa 1 t at fdis, five with move
        "Coach walks away from us and sits back down on one of the benches."
        "Before I'd think he was just lazing around and wouldn't even think twice about it."
        "But now, if I actually pay attention, I can see that he's watching everyone intently."
        "He might not be walking around shouting orders, but he's making sure that everyone is doing what they're told."
        mc 1 t "\"I honestly had no idea he was this dedicated.\""
        show sa 1 t talk at fdis
        sa "\"I kinda suspected it over the years.\""
        mc 1 t sigh "\"Then why didn't you ever say something?\""
        sa "\"Suspecting it and knowing it are two different things. I couldn't tell you that without being sure. That's why I always told you to give him a chance.\""
        mc 1 t avoid "\"Huh... I guess I should have listened.\""
        show sa 1 t smile at fdis
        sa "\"Yup. You should! Anyway, I'm gonna do some more rounds to see if anyone needs help and I'll get back to my own training.\""
        show sa 1 t smile at offscreenleft with moveoledis
        "..."
        "Sighing, I reach into my bag and grab my racket."
        "I don't know how I should feel right now..."
        "I don't like being told that I'm in a slump or that I have a problem or that I'm underperforming or... well, anything else related to it."
        "But I have to stop getting so defensive about it."
        "I already {i}know{/i} that I'm not performing my best. It's the whole reason why I asked Kei-kun to be my practice partner."
        "I really have to stop getting discouraged so easily."
    s 1 v smile "\"Ah, there you are!\""
    show s 1 v smile at fdis, five with moveiridis
    "I hear the sound of hurried steps echoing from behind me and, sure enough, Shoichi is there."
    mc 1 t smile "\"Oh, hey Shoichi. What's up?\""
    show s 1 v think at fdis
    s "\"Could I talk to you for a second? There was something I wanted to ask you this morning but... erm... I kind of forgot given the whole thing with the taste testing.\""
    mc 1 t sigh "\"Ah, yeah. That disaster...\""
    s "\"Disaster? Why disaster? I thought it was fine. Most of the food was good.\""
    mc 1 t sigh2 "\"Good? Maybe. Certainly bad for my heart though.\""
    show s 1 v wry at fdis
    s "\"I don't think it was that bad. Most of it didn't look too bad, only one or two dishes had me scared to try them out.\""
    "Well, duh. You're the master of repulsive cooking."
    mc 1 t avoid "\"I'll... defer to you on that. Anyway, what is it that you wanted?\""
    show s 1 v at fdis
    s "\"So, I just heard the news last night. Dad's latest business trip is ending early. He's coming back home next month.\""
    mc 1 t curious "\"Oh, really? How come? I thought he was supposed to be away for six months.\""
    show s 1 v considerate at fdis
    s "\"Yeah, well, apparently the negotiation he was mediating between his company and whoever it was they were trying to make an agreement with broke down.\""
    mc 1 t wince "\"That kind of sucks. You think he'll be in a bad mood when he comes back?\""
    show s 1 v sigh at fdis
    s "\"I {i}know{/i} he'll be in a bad mood. That's why I kinda wanted your help organizing a welcoming party for him. I mean, he {i}was{/i} away for almost a month.\""
    mc 1 t "\"Doesn't your father hate parties?\""
    show s 1 v think at fdis
    s "\"Nah, just the ones that make too much noise. I think a quiet gathering with his closest friends and some good food could put him in a decent enough mood. Then maybe, just maybe, he might not make my life hell once he's back.\""
    mc 1 t smile "\"Sure. I'll help you. What sort of food do you think of getting for the party? There are a ton of places we could order from.\""
    show s 1 v laugh at fdis
    s "\"Nah, I think homemade food would be best. You know, to give him that \"homely\" feeling! I was thinking that I could cook!\""
    "Oh, God no!"
    mc 1 t fsmile "\"Ehm... er... that's... that's an idea.\""
    show s 1 v annoyed at fdis
    s "\"What? You don't think I can cook?\""
    mc 1 t fsmile "\"No! No no no no no. That's not what I'm saying at all, just that... well, err... maybe it would be best if you organized other stuff. You're the one who knows his friends and what he likes, so maybe you should organize the party and let me do the cooking.\""
    show s 1 v think at fdis
    s "\"Oh... Yeah, I guess that works. In fact, it's probably a better idea. Thanks, [povFirstName]!\""
    "Saved by the gong... or in this case, Shoichi's gullibility."
    "If I had let him make the food for the party, all those guests would leave in caskets..."
    "And I'd very much prefer if my best friend weren't charged with multiple counts of involuntary manslaughter."
    show s 1 v smile at fdis
    s "\"Come to think of it, I'm pretty sure I can find an old copy of dad's address book. I might not know all of his friends by name but I could reach out to the people he knows from that.\""
    mc 1 t sigh "\"An address book? In this day and age? Wouldn't he just use his phone's contact list.\""
    show s 1 v considerate at fdis
    s "\"Dad's terrible with technology, remember?\""
    "Oh, yeah... that's true."
    "He still uses an old feature phone from six years ago."
    mc 1 t smile "\"Okay, if you want homemade food to make him feel more at home, you'll probably prefer to host it at your place, right?\""
    show s 1 v happy at fdis
    s "\"Yeah. I doubt dad would want to go out of the house after arriving from a month-long trip anyway.\""
    mc 1 t happy "\"Got it. Should we have a cake?\""
    show s 1 v laugh at fdis
    s "\"Every party should have a cake.\""
    mc 1 t smile "\"What kind of cake does your dad like?\""
    show s 1 v happy at fdis
    s "\"Ah, that's easy-\""
    hide s 1 v happy with dissolve
    "We spent the next several minutes having fun planning out this little party for Shoichi's dad."
    "In the end, neither of us got much work done in our respective clubs."
    "I even got chewed out by Coach because of it."
    stop music2 fadeout 5.0
    scene SGateE with dissolve
    play music "music/cicadas2.ogg" fadein 5.0
    "Ah, it's hot..."
    "It's way too hot for 5PM on a spring day."
    "I know the weather forecast said we'd have a heat wave this weekend but damn, I didn't expect it to come so soon."
    "I'm so glad I changed out of those sweaty clothes and into something more comfy..."
    "Nor for it to be this strong."
    "No sign of Jun either."
    play sound "music/phonebeep.ogg"
    mc 1 c sigh "\"5:15...\""
    "I've been waiting out here for over ten minutes already."
    "Why is it that when it comes to that tiger, I always sit around waiting for a long time?"
    play music2 "music/BGM/Hanging Out.ogg" fadein 5.0
    k 1 u "\"[povFirstName]-san?\""
    show k 1 u at fdis, five with dissolve
    mc 1 c smile "\"Ah, Kei-kun. I didn't see you there.\""
    show k 1 u sigh at fdis
    k "\"I'll say. I walked all the way over to you and even called you a few times before you answered.\""
    mc 1 c considerate "\"Is that so? Hahaha, sorry. I don't function all that well in heat\""
    show k 1 u wince at fdis
    "Keisuke wrinkles his nose."
    k "\"Doesn't help that you're still covered in sweat. You should really start using the showers after practice.\""
    mc 1 c sigh "\"I'm already having a hard time with the heat as is, don't pile on more stress.\""
    show k 1 u worried at fdis
    k "\"Sorry.\""
    "..."
    show k 1 u at fdis
    mc 1 c "\"By the way, I didn't see you at practice today. I thought you'd gone home early.\""
    show k 1 u wry at fdis
    k "\"Nah. I had some things I needed to take care of first.\""
    mc 1 c curious "\"What happened?\""
    show k 1 u worried at fdis
    k "\"It's... well... ugh. I guess it's okay to tell you.\""
    "Keisuke looks away and down at the floor."
    "This gesture alone is enough to pique my curiosity."
    mc 1 c smile "\"Sure you can. What's up?\""
    if day10 == "keisuke":
        show k 1 u at fdis
        k "\"You remember how we went to the music store the other day to buy my new mic?\""
        mc 1 c "\"Yeah. What about it?\""
        show k 1 u avoid at fdis
        k "\"Well... I thought a lot about what you guys said. About how you liked my voice and all so... I decided to join the Light Music Club.\""
    else:
        show k 1 u at fdis
        k "\"A few days ago, I went to a music store to buy a new mic. When I was there I... erm... I had to play a song to test the mic and all.\""
        show k 1 u wince at fdis
        k "\"Since they didn't have any recording booths free, I... kinda recorded it on the store floor.\""
        mc 1 u smile "\"Oh, wow. Was it awkward?\""
        show k 1 u worried at fdis
        k "\"... A little bit. I kinda zoned out of it all while playing, but I felt really weird once I noticed the crowd that formed.\""
        mc 1 c wince "\"Oh, damn. You attracted a crowd while testing out the mic?\""
        k "\"Yeah... they seemed to think it was an event happening at the store...\""
        show k 1 u avoidb at fdis
        k "\"I got a lot of praise that day. About how I have a good singing voice and... and how I'm good with the guitar.\""
        k "\"So I decided to join the Light Music Club.\""
    mc 1 c "\"Oh. That's neat. But wait, what about the Manga club?\""
    show k 1 u sigh at fdis
    k "\"I quit that a while ago. Right around the time they insisted I cosplay as a popular visual novel character for our club's booth in the festival.\""
    mc 1 c smile "\"Aww, that could have been fun!\""
    show k 1 u avoid at fdis
    k "\"... It was a character from a homo game.\""
    mc 1 c wince "\"Ah.\""
    show k 1 u avoidb at fdis
    k "\"So, yeah... done with that. I planned on just going to the light music club to watch, but they roped me into applying.\""
    show k 1 u smile at fdis
    k "\"Did you know that our light music club actually has a band? As in, the band members are the only people in the club.\""
    mc 1 c wince "\"That's... a bit fishy. Why aren't there more people?\""
    show k 1 u worried at fdis
    k "\"Not many people are willing to pick up an instrument and learn it. And that's the minimal requirement to join.\""
    mc 1 c happy "\"Hmm... I think I'd be interested in learning guitar at some point... Maybe you could teach me?\""
    show k 1 u sigh at fdis
    "Keisuke scoffs, shaking his head in negative."
    k "\"Sorry but I'm in no way qualified to teach someone.\""
    mc 1 c think "\"What? Why not?\""
    show k 1 u at fdis
    k "\"Teaching requires patience. A trait that I definitely don't have.\""
    show k 1 u sigh at fdis
    k "\"I'd probably lose my patience and I'd end up screaming at you for base mistakes.\""
    mc 1 c "\"Huh... you don't really look the type to lose patience that often.\""
    k "\"You're... you're kidding, right? I lose my patience all the time. I always get irritated in the courts and end up not playing well because of it.\""
    "Oh... right. I forgot about that."
    show k 1 u smile at fdis
    k "\"Either way, I ended up spending all my time after class over there. Their band is really interesting. Their vocalist is very talented, she's a senior from Urata's class.\""
    mc 1 c smile "\"Oh, is that so? What kind of music do they make?\""
    k "\"They don't have any originals yet. They're very good players, mind you, but they're not very good composers. I saw the sheets for some of their attempts and... well...\""
    mc 1 c considerate "\"Bad?\""
    show k 1 u sigh at fdis
    k "\"So bad.\""
    show k 1 u calm at fdis
    k "\"But still, the vocalist's voice... I could listen to her sing all day. It was truly amazing.\""
    mc 1 c happy "\"I'm glad you had fun. And what did {i}they{/i} think of your singing and playing?\""
    show k 1 u wince at fdis
    k "\"Oh, yeah, that... uhm...\""
    "Keisuke immediately becomes restless, scratching at the back of his neck and looking away."
    mc 1 c curious "\"... What?\""
    k "\"Well, I... kinda didn't do anything.\""
    mc 1 c shock "\"What?! Why?!\""
    show k 1 u avoidb at fdis
    k "\"I got... erm... shy, I guess.\""
    mc 1 c sigh2 "\"Shy? You got shy?! You went into that club specifically so you could sing and play guitar!\""
    show k 1 u worried at fdis
    k "\"Well, what would you have done?\""
    mc 1 c annoyed "\"Played!\""
    k "\"Oh yeah? Well... you're much braver than I am, then.\""
    mc 1 c sigh2 "\"Oh, come on!\""
    "I hide my eyes behind my hands, taking deep breaths to calm myself."
    mc 1 c sigh2 "\"Keisuke, what's the point of you signing up for the Light Music club if you just go there to watch? What would you say if Jun signed up for the Tennis club just to watch?\""
    show k 1 u at fdis
    k "\"... Did you just call me \"Keisuke\"?\""
    mc 1 c scorn "\"{size=+2}That's what you focused on?!{/size}\""
    show k 1 u wince at fdis
    k "\"Sorry sorry, it's just that I'm not used to you calling me by my full name.\""
    mc 1 c sigh "\"Seriously, if you're going there for the music then you should... you know, play music!\""
    k "\"Eh, I'm still not sure on that. I want to, but...\""
    "I stand, silently waiting for him to continue his sentence, but he continues to stare at me without saying a word."
    mc 1 c "\"... But?\""
    show k 1 u avoidb at fdis
    k "\"I'm... I'm shy.\""
    mc 1 c sigh "\"You routinely play tennis in big tournaments watched by dozens if not hundreds of people and yet you decide to feel shy about singing in front of four, maybe five high school students?\""
    k "\"... I never said it was a rational fear.\""
    mc 1 c sigh2 "\"Well, good, because then you'd be wrong.\""
    show k 1 u sigh at fdis
    k "\"Oh, shut up. I'll do it on my own time.\""
    mc 1 c "\"As long as you actually do it.\""
    show k 1 u avoid at fdis
    k "\"... You're very annoying sometimes, you know that?\""
    "I try to put on the most smug grin that I can muster."
    mc 1 c happy "\"Oh, thank you. I'll take that as compliment.\""
    show k 1 u smile at fdis
    k "\"You're unbelievable.\""
    mc 1 c smile "\"I try.\""
    mc 1 c "\"Oh, by the way, are you going to have someone come pick you up today?\""
    show k 1 u at fdis
    k "\"Yes. Always. Why?\""
    mc 1 c think "\"Oh, it's nothing major. I just wanted to know if you'd like to walk with Jun and I part of the way home. I think Shoichi might even join us if Jun takes too long.\""
    show k 2 u annoyed at fdis
    k "\"Hmm...\""
    "Keisuke's nose twitchs a couple of times (something it always does when he's deep in thought)."
    k "\"I guess I could. They only said that I need to go home by one of my father's cars, they never said I had to be picked up at school.\""
    mc 1 c considerate "\"You really always look for a way to weasel out from under your family's rules, don't you?\""
    show k 1 u smile at fdis
    k "\"Always.\""
    play sound "music/running.ogg"
    "I hear the sound of approaching footsteps at a hurried pace."
    "We both turn around at the same time to see..."
    show k 1 u at fdis, three with move
    show j 1 u sigh at fdis, six with moveiridis
    "A tiger huffing and with his brow covered in beads of sweat."
    j "\"[povFirstName]-san, I'm sorry I took so long, I lost track of time...\""
    show j 1 u watch at fdis
    j "\"Ah, Urushihara-san.\""
    show j 1 u happy at fdis
    j "\"Hi!\""
    show k 1 u wince at fdis
    k "\"Yeah, hi... Are you alright? You look very winded.\""
    show j 1 u sigh at fdis
    j "\"I'm fine. I didn't notice how much time was passing while I practiced and only stopped when a teacher came by to get me. I ran over here because I didn't want to keep [povFirstName]-san waiting any longer.\""
    show k 1 u smile at fdis
    k "\"Well, at least you're dedicated to your craft.\""
    mc 1 c sigh2 "\"True, but I'd still prefer if he kept his eyes on the clock every now and then.\""
    j "\"Sorry sorry sorry!\""
    mc 1 c "\"It's fine. It's just a little hot today, that's all.\""
    show j 1 u happy at fdis
    j "\"Well, I didn't notice it much. The piano room has air conditioning after all.\""
    play sound "music/stab.ogg"
    mc 1 c doom "\"{size=+2}Die!{/size}\"" with hpunch
    show j 1 u wince at fdis
    j "\"W-What? What did I do wrong?\""
    show k 1 u sigh at fdis
    k "\"[povFirstName]-san has been standing out in the heat since practice ended, after hours exercising and sweating. I don't think he'd like to hear you talking about being in an air conditioned room.\""
    j "\"Ah, sorry sorry.\""
    "I sigh."
    "Even if I'm a little annoyed at him... I can't really stay mad at this guy."
    "It worries me that I'm starting to develop a weakness to him."
    "Gah, now that I think of it, I'm the same way with Aki."
    show k 1 u at fdis
    mc 1 c sigh2 "\"It's fine. Don't... don't worry about it.\""
    show j 1 u sigh at fdis
    j "\"Oh, good. I thought I messed up big time there.\""
    mc 1 c sigh2 "\"It'd take a lot more than that to piss me off.\""
    show j 1 u shock at fdis
    j "\"Oh!\""
    show k 1 u sigh at fdis
    k "\"He's lying, of course. He's incredibly petty.\""
    mc 1 c annoyed "\"Hey!\""
    show k 1 u at fdis
    k "\"What? It's true.\""
    show j 1 u watch at fdis
    mc 1 c avoid "\"Since when am I petty?\""
    show k 1 u worried at fdis
    k "\"You once went a full day without talking to me because I accidentally spoiled the ending of a movie that was based on a book that was released forty years ago.\""
    mc 1 c wince "\"That's not being petty!\""
    show j 1 u think at fdis
    j "\"I kinda think it is.\""
    mc 1 c sigh "\"Wha- You too?!\""
    show j 1 u watch at fdis, five
    show k 1 u at fdis, two
    with move
    show s 1 v smile at fdis, eight with moveiridis
    s "\"Who did what?\""
    play sound "music/tap.ogg"
    mc 1 c shock "\"Gah!\"" with hpunch
    "Shoichi shows up out of nowhere, putting a hand on my shoulder and speaking up."
    show s 1 v sigh at fdis
    s "\"Jesus, settle down.\""
    mc 1 c wince "\"Why is everyone deciding to sneak up on me today?!\""
    show k 1 u worried at fdis
    show s 1 v at fdis
    k "\"Everyone? Did I miss something? Because this was the first time I've seen you getting sneaked up on today.\""
    mc 1 c wince "\"Well... there was Saya a little earlier.\""
    show k 1 u sigh at fdis
    k "\"So... two people? That hardly qualifies as \"everyone\", you know.\""
    mc 1 c sigh2 "\"Oh, shut up.\""
    show j 1 u think at fdis
    j "\"[povFirstName]-san is just being over dramatic again.\""
    mc 1 c wince "\"What?! Oh, you guys suck!\""
    show j 1 u watch at fdis
    show s 1 v smile at fdis
    s "\"Actually, I agree with Jun-kun here.\""
    mc 1 c sigh2 "\"Of course you do...\""
    s "\"Well, anyway, what's up? What were you guys talking about? What did I miss?\""
    mc 1 c think "\"Shoichi, get this. They were telling me that {i}I{/i}, this brilliant ray of sunshine standing before your eyes, am petty! Can you believe this?\""
    show s 1 v at fdis
    s "\"First of all, \"brilliant ray of sunshine\"? Dude, get over yourself.\""
    show k 2 u gentle at fdis
    show j 1 u happy at fdis
    mc 1 u shock "\"H-hey! How rude!\""
    j "\"Pffft, hahaha!\""
    show s 1 v smile at fdis
    show k 1 u smile at fdis
    "Oh, great. Now all three of them are cracking up at my expense."
    s "\"And second of all, you {i}are{/i} petty!\""
    mc 1 c shock "\"{size=+2}What?!{/size}\""
    show s 1 v think at fdis
    s "\"Yeah, you get upset and pout for the silliest of reasons.\""
    s "\"I remember this one time, this was a couple years ago when I was sleeping over at your place, when you got mad at me after I won every single round of Sidewalk Fighter II. You then proceeded to make dinner... for everyone but me.\""
    s "\"You told me: \"I'm sorry, you're already too full of yourself to fit anything else in there\". I had to go hungry that night.\""
    show j 1 u shock at fdis
    j "\"Oh, wow. That's awful.\""
    mc 1 c wince "\"But... but... I was a {i}child{/i}!\""
    show j 1 u watch at fdis
    s "\"You were fifteen. You were old enough to know what you were doing.\""
    mc 1 c wince "\"But... but...\""
    show k 1 u at fdis
    k "\"Are you going to do this for the whole walk home, because if so then I'd rather just have my car come pick me up here.\""
    mc 1 c scorn "\"Wha- How rude!\""
    show j 1 u happy at fdis
    j "\"[povFirstName]-san, they're doing this on purpose to annoy you!\""
    mc 1 c wince "\"Wait, what?!\""
    show k 2 u gentle at fdis
    show s 1 v laugh at fdis
    "Keisuke and Shoichi finally break character and begin to laugh hysterically, to the point of having trouble catching their breaths."
    mc 1 c wince "\"You... you... you...\""
    show k 1 u smile at fdis
    k "\"Yes?\""
    mc 1 c sigh "\"When did you- How did you- Why did you... Aaagh!\""
    show s 1 v smile at fdis
    s "\"Is that supposed to be Japanese? I didn't understand a single word!\""
    mc 1 c sigh2 "\"Ugh, screw you guys. I'm leaving.\""
    show s 1 v happy at fdis
    show k 1 u wry at fdis
    s "\"Aww, don't be like that, we're just having some harmless fun!\""
    k "\"At your expense, of course!\""
    stop music fadeout 2.5
    "The two of them continued to harp on me for the entirety of the walk back home."
    stop music2 fadeout 5.0
    scene LivingRoomE with fade
    play music "music/tickingclock.ogg" fadein 5.0
    "I've completely lost track of time at this point."
    "All I know is that I've been sitting in the living room, glued to the TV, since after dinner."
    a 1 c sigh "\"Ah... Aniki?\""
    "The light is flicked on. I reach out with my hands to cover the sudden assault on my vision."
    show a 1 c sigh at fdis, fiveh with moveiridis
    a "\"What are you still doing up?\""
    mc 1 c think "\"What do you mean \"still doing up\"? Has everyone else gone to sleep?\""
    a 1 c "\"Yeah. It's 3AM.\""
    mc 1 c shock "\"Woow, really?\""
    "I look up at the clock on the far wall and, sure enough, it's already that late."
    "I didn't even notice the time passing."
    a 1 c sigh "\"Seriously, what are you doing up?\""
    "Aki yawns, rubbing his eyes. He flops down on the couch, lying the back of his head on my lap and looking directly up at me."
    mc 1 c "\"I've been watching some footage.\""
    a 1 c "\"Footage?\""
    "For the first time since he came downstairs, Aki looks at the TV screen."
    a "\"Is that the kid Keisuke-san told you about? The akita?\""
    "I nod, keeping my eyes glued to the screen."
    a 1 c sigh2 "\"You've been watching videos of him for two weeks. Are you sure you should be obsessing so much about a single player?\""
    mc 1 c sigh "\"I can't help but worry. Something about the way he plays just ticks me off.\""
    a 1 c "\"You mean how he plays so much like you?\""
    mc 1 c think "\"Maybe... I'm not sure.\""
    "I think I've already rewatched this particular match four or five times."
    "I keep looking for something that's not there."
    "For some reason, seeing this guy play just makes me... uneasy."
    a "\"You don't even know if you're gonna go up against him anyway.\""
    mc 1 c sigh "\"I get the feeling that I will...\""
    "If we're talking about skills alone and getting rid of all other factors, I can easily see this guy placing in the Top 4."
    "In fact, the only player other than me in the prefecture that I can imagine beating him is Kei-kun."
    "If we're talking about skills alone, Kei-kun should be better than him, but..."
    "I just have this growing sense of discomfort whenever I watch this guy playing."
    a 1 c "\"... That's weird.\""
    "I look down to see that Aki's staring intently at the TV, also watching the match going on the screen."
    mc 1 c curious "\"What's weird?\""
    a 1 c worried2 "\"Well... it's not just that the guy plays like you. Every single move he makes looks like a carbon-copy of you.\""
    a "\"It's as if he's mimicking you while playing.\""
    mc 1 c think "\"Yeah, I noticed this.\""
    a 1 c "\"This is really creepy. Do you think he's {i}actually{/i} mimicking you?\""
    mc 1 c think "\"I don't know. When I met him, he seemed to already know me.\""
    a "\"So you're saying that it's possible.\""
    mc 1 c "\"... Maybe.\""
    "I'd hope not. It'd be kinda creepy if it were true."
    a "\"He seems to be pretty good. I don't think I could beat him.\""
    mc 1 c smile "\"Well, that'd be a tall order. He's four years older than you.\""
    "He shrugs, looking back up at me."
    a "\"So? You were beating high school players by your first year of junior high. And professional players face people much older than them all the time.\""
    mc 1 c think "\"Professional players have all at least reached full maturity. You still have the body of a kid against someone near adulthood.\""
    a "\"Still doesn't explain how you did it.\""
    mc 1 c wince "\"W-well...\""
    "Honestly, I don't even know all that well."
    "And it's not like I was beating high school players left and right. Maybe once or twice..."
    mc 1 c wry "\"Aki, I think you exaggerate too much when it comes to me.\""
    a 1 c sigh "\"But it's true!\""
    mc 1 c think "\"Maybe, but... uhm... how can I put this...\""
    "... You seem like you think I'm the ultimate player or something?"
    mc 1 c sigh2 "\"... Ugh, never mind.\""
    "This is not the conversation I want to be having with my kid brother at 3AM."
    mc 1 c smile "\"I'm gonna head to bed. You should go back too.\""
    a 1 c "\"Hmm, sure. I'll just grab a glass of water. {size=-2}That's what I came here to do anyway.{/size}\""
    "I shut off the television and Aki props himself up from my lap, letting me get back up."
    a 1 c smile "\"By the way, Aniki, is it okay if some of my friends from the club watch your matches?\""
    mc 1 c "\"I don't mind, but why would they be coming over to my match instead of yours?\""
    a 1 c happy "\"I asked them to record your matches from a lot of angles for me!\""
    mc 1 c think "\"... Why?\""
    a 1 c smile "\"My coach said he wanted us to get videos of players we admire to try and base ourselves on them!\""
    mc 1 c sigh "\"So you want to... try playing more like me?\""
    a 1 c happyb "\"Yeah!\""
    "... Why do I get the feeling that there's a second doppelganger of me about to be born?"
    mc 1 c wince "\"I... Ugh, sure, knock yourselves out.\""
    a "\"Yay, thanks!\""
    "I really have to learn to say no to him..."
    stop music fadeout 2.5
    stop music2 fadeout 2.5
    stop music3 fadeout 2.5
    $ date = None
    jump Day12
