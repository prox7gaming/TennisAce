label Day16_Shoichi:
    window hide
    scene May26 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    play music2 "music/BGM/Spring Classroom.ogg" fadein 5.0
    scene SClass with fade
    window show
    $ date = "day16"
    "The teacher has already left the class by the time the bell announced the start of our lunch time."
    "Class today hasn't been nearly as confusing as the past few days."
    "For once, we were actually studying the subject matter that was in our curriculum instead of something completely unrelated."
    "Bless Shima-sensei's enthusiasm but the dude needs to start sticking to the guidelines."
    show j 1 u think at fdis, five with dissolve
    j "\"Hmm... Class felt a little different today for some reason.\""
    mc 1 u "\"The teacher probably got a talking to for straying from the curriculum. It happens every now and again.\""
    show j 1 u shock at fdis
    j "\"This has happened before?\""
    mc 1 u smile "\"Around once every couple months, yeah. Shima-sensei is notorious for it.\""
    show j 1 u watch at fdis
    j "\"I'm surprised they haven't fired him if he does it that often.\""
    mc 1 u talk "\"He's a good teacher and he's well liked by the students.\""
    j "\"And that's enough to get him off the hook?\""
    mc 1 u smile "\"Pretty much.\""
    show j 1 u think at fdis
    j "\"Huh...\""
    show j 1 u watch at fdis, two with move
    play sound "music/slidingdoor.ogg"
    show s 1 u smile at fdis, eight with moveiridis
    s "\"Good morning.\""
    show j 1 u happy at fdis
    j "\"Ah, Shoichi-san. Good morning!\""
    mc 1 u considerate "\"Uhm... hey.\""
    show s 1 u at fdis
    s "\"Hey.\""
    show j 1 u watch at fdis
    "..."
    "Oh man, I feel really awkward right now."
    "After the kiss we shared yesterday, Shoichi had to rush back home due to his father's strict curfew..."
    "And now we're kinda... dating? Ugh, I don't know how I'm supposed to act around him."
    mc 1 u wince "\"Uhm... did you manage to get home in time for your curfew yesterday?\""
    show s 1 u think at fdis
    s "\"Er... I was a couple minutes late. I was able to excuse myself by making up a lie about having to talk to the faculty about plans for the festival.\""
    mc 1 u worried "\"And he bought that?\""
    show s 1 u at fdis
    s "\"He's got no reason not to. I'm the student council president after all.\""
    j "\"I still think a 6PM curfew is kinda ridiculous for someone our age.\""
    show s 1 u considerate at fdis
    s "\"Most of what dad does is ridiculous. He's pretty strict when it comes to rules and regulations.\""
    show s 1 u wry at fdis
    s "\"So, [povFirstName]... how was your day after you went home yesterday? You didn't answer my text.\""
    mc 1 u avoidb "\"Sorry. I was feeling a little awkward...\""
    j "\"Why were you feeling awkward?\""
    mc 1 u shockb "\"O-oh, uhm, that's...\""
    "Right, I forgot this isn't something we should be talking about openly!"
    mc 1 u avoidb "\"Uhm, err... I mean...\""
    show s 1 u think at fdis
    s "\"I asked him to do something for me, but he had to refuse and I guess felt awkward because of it.\""
    show j 1 u think at fdis
    j "\"Oh. I guess [povFirstName]-san really does feel awkward about saying no to people.\""
    show s 1 u happy at fdis
    s "\"That's definitely true.\""
    "Damn... Shoichi's not usually this good at lying."
    mc 1 u considerate "\"Y-yeah. I just like to please people I guess.\""
    show s 1 u smile at fdis
    s "\"Actually, [povFirstName], I came here to ask you to eat your lunch with me in the student council room. I kinda need your help with something while we eat. Would that be okay?\""
    mc 1 u shock "\"O-oh, s-sure.\""
    show j 1 u watch at fdis
    j "\"Ah. I guess it'll just be me and Mizoguchi-san today, huh?\""
    show s 1 u considerate at fdis
    s "\"Yeah. Sorry, Jun-kun. I really need to borrow this guy.\""
    show j 1 u happy at fdis
    j "\"No problem. Have a nice lunch!\""
    show s 1 u smile at fdis
    s "\"You too.\""
    mc 1 u considerate "\"See you back in class later, Jun.\""
    show j 1 u smile at fdis
    j "\"See ya.\""
    scene SCorridor
    show s 1 u at fdis, two
    show sa 1 u smile at fdis, seven
    play sound "music/slidingdoor.ogg"
    with fade
    "We run into Saya just as we are leaving the classroom."
    show sa 1 u laugh at fdis
    sa "\"Osu!{nw}"
    show sa 1 u talk at fdis
    extend " Wait, where are you two going?\""
    show s 1 u smile at fdis
    show sa 1 u at fdis
    s "\"Oh, uhm... I need [povFirstName]'s help with something.\""
    sa "\"Really? With what?\""
    show s 1 u think at fdis
    s "\"Err... something student council related.\""
    show sa 1 u bored at fdis
    "Saya looks between the two of us and raises an eyebrow."
    sa "\"And you asked [povFirstName] of all people for that? Are you {i}that{/i} strapped for choices?\""
    mc 1 u annoyed "\"Hey!\""
    show sa 1 u at fdis
    show s 1 u considerate at fdis
    s "\"N-no. I just preferred working with someone I'm already familiar with if I had to bring someone from outside to help.\""
    sa "\"Wouldn't Kei-kun be a better choice for that? Or, arrogance aside, me?\""
    s "\"W-well, yeah. But you two are already busy with your own clubs and things.\""
    mc 1 u annoyed "\"H-hey. Don't just agree with her that I'm a bad choice so easily.\""
    show s 1 u wince at fdis
    s "\"Ah, n-no, that's not what I meant. It's just...\""
    show sa 1 u considerate at fdis
    "Saya shakes her head and smiles."
    sa "\"You can barely even finish a sentence today. You really do need help. Enjoy your lunch. And I hope you'll be able to finish whatever it is you need help with.\""
    show s 1 u wry at fdis
    show sa 1 u smile at fdis
    s "\"Thanks, Saya-chan.\""
    mc 1 u considerate "\"See ya.\""
    stop music2 fadeout 2.5
    play music "music/breeze.ogg"
    play music3 "music/BGM/The People Here.ogg" fadein 5.0
    scene SRooftop
    show s 1 u sigh at fdis, five
    with fade
    play sound "music/metaldoor.ogg"
    s "\"Oh man, I'm really not good at this whole lying thing.\""
    mc 1 u sigh2 "\"Yeah, I'll say. Nice job bringing yesterday up in front of Jun.\""
    show s 1 u wince at fdis
    s "\"Sorry, I forgot. I'm not used to having to hide things...\""
    mc 1 u avoidb "\"...\""
    "I still feel a little awkward being around him after yesterday."
    "I'm not quite sure how to act..."
    show s 1 u think at fdis
    s "\"So... I was just hoping we could eat together alone since we're... you know. Man, it's so weird to suddenly start dating after being friends for so long.\""
    mc 1 u shock "\"Really? You're feeling that way too?\""
    show s 1 u considerate at fdis
    s "\"Of course. We were best friends for twelve years and now all of a sudden we're dating? Of course I don't know how to act.\""
    show s 1 u wry at fdis
    s "\"Should I act all boyfriend-like and start spoon-feeding you or holding your hand or calling you by a pet name?\""
    mc 1 u flustered "\"We've only agreed to start dating yesterday. I don't even know if I should be calling you my boyfriend yet. Besides... \"boyfriend\"... that's something that'll take me a while to get used to...\""
    show s 1 u considerate at fdis
    s "\"Ah, yeah, I understand.\""
    show s 1 u smile at fdis
    s "\"How about we just have a seat and eat together for now?\""
    mc 1 u considerate "\"Y-yeah. That's a good idea.\""
    play sound "music/fabric.ogg"
    "At least I'm glad to hear I'm not the only one feeling awkward here."
    "I don't even know how to proceed with this whole thing..."
    mc 1 u talk "\"I see you have a convenience store lunch today again.\""
    show s 1 u sigh at fdis
    s "\"Yeah. Hitoka's really sticking to her guns on this. She said she won't start packing me lunches again until I agree to take her out with my friends.\""
    mc 1 u avoidb "\"Uhm... wouldn't that be a little awkward since she's... and you and I are... you know.\""
    s "\"Gee, that was so cryptic, I don't know if I can crack that code.\""
    mc 1 u avoidb "\"Come on, this is already embarrassing enough. Don't make me say the actual words...\""
    show s 1 u avoid at fdis
    s "\"... Yeah. I'm a bit worried about that. I'm scared of how she'd react if she found out about us...\""
    mc 1 u "\"If?\""
    show s 1 u sigh at fdis
    s "\"I mean... you're not even sure if you really want to date me yet. I'm not going to get ahead of myself and come out to my family.\""
    show s 1 u smile at fdis
    s "\"Here, have a bite!\""
    "Shoichi interrupts our conversation by grabbing a piece of egg with his chopsticks and putting it in front of my face."
    mc 1 u flustered "\"We're actually doing that?\""
    show s 1 u happy at fdis
    s "\"I want to give it a try!\""
    mc 1 u avoidb "\"Fine...\""
    "I tentatively eat the egg in front of me, feeling my face getting flushed."
    s "\"Hehe. This is kinda fun.\""
    mc 1 u flustered "\"... This is really embarrassing.\""
    show s 1 u at fdis
    s "\"Oh. Should I stop?\""
    mc 1 u wince "\"Please. I don't think I'm ready for this kind of thing...\""
    show s 1 u wry at fdis
    s "\"Alright, I'll stop."
    show s 1 u think at fdis
    extend " Hmm... what kind of thing should we do now that we're dating though?\""
    mc 1 u wince "\"Do we need to do anything different?\""
    show s 1 u at fdis
    s "\"I mean... otherwise it doesn't really feel like anything's changed.\""
    mc 1 u avoidb "\"I guess...\""
    show s 1 u happy at fdis
    s "\"Maybe I should hold your hand then?\""
    play sound "music/fabric.ogg"
    "Shoichi reaches out and grabs my right hand, squeezing it tightly."
    show s 1 u flattered at fdis
    s "\"How about this?\""
    mc 1 u avoidb "\"Uhm... Shoichi, I... can't eat like this.\""
    show s 1 u shock at fdis
    s "\"Oh. That's true.\""
    show s 1 u sigh at fdis
    "He pulls his hand away, sighing."
    s "\"Man, I really suck at this kind of thing.\""
    show s 1 u at fdis
    s "\"You've dated a lot before. What did you used to do with your girlfriends?\""
    mc 1 u avoidb "\"Uhm... that's...\""
    "Honestly... I tended to spend as little time as possible with them just because I wasn't really that interested."
    "... And when we were together, we tended to just..."
    mc 1 u sigh2 "\"N-no. We're not ready for that kind of thing...\""
    show s 1 u wince at fdis
    s "\"Huh? What do you mean?\""
    mc 1 u avoidb "\"I'll tell you later.\""
    s "\"O-okay.\""
    show s 1 u sigh at fdis
    s "\"It really doesn't feel like anything changed though...\""
    mc 1 u talk "\"I... don't think anything has to change.\""
    show s 1 u shock at fdis
    $ renpy.pause(1.0)
    show s 1 u blush at fdis
    s "\"Are... are you saying you don't want to date me anymore?\""
    mc 1 u shock "\"W-what? N-no! That's not what I meant!\""
    show s 1 u sigh at fdis
    s "\"O-oh. I... I think my heart stopped for a second there.\""
    mc 1 u wince "\"Sorry, I might have been a little ambiguous for a second there.\""
    mc 1 u talk "\"It's just that... we're best friends. Even if we're dating, that's not really gonna change. We'll just... be doing more things we didn't do before.\""
    mc 1 u worried "\"But I think we should just do things as they come naturally. There's no point forcing ourselves to change just because we have to. That would just make both of us uncomfortable.\""
    show s 1 u wince at fdis
    s "\"... I guess that's true.\""
    show s 1 u considerate at fdis
    s "\"I've just... been dreaming of this for a long time. I guess I got a little ahead of myself.\""
    mc 1 u smile "\"That's alright. It's a big change what we're doing... we need to give ourselves time to get used to it.\""
    mc 1 u sigh "\"I myself still need to wrap my head around the whole idea... I'm not only dating my best friend of twelve years. I'm dating a {i}guy{/i}... it still feels strange...\""
    show s 1 u smile at fdis
    s "\"I'll bet. Don't worry, I'll give you as much time as possible to adjust.\""
    show s 1 u wry at fdis
    s "\"Should I refrain from kissing you until you're used to it? Gotta admit that after doing it yesterday, I'm already craving for more.\""
    mc 1 u wince "\"M-maybe not completely.\""
    show s 1 u happy at fdis
    s "\"You mean I can kiss you now?\""
    mc 1 u avoidb "\"... Just eat your lunch.\""
    show s 1 u sad at fdis
    s "\"Aww.\""
    mc 1 u sigh2 "\"... Maybe once we're done eating. {size=-2}Stop looking at me like that.{/size}\""
    show s 1 u happy at fdis
    s "\"Yay!\""
    show s 1 u smile at fdis
    "We continue munching on our food quietly."
    "I don't know why but the mood is different from when we used to eat together before."
    "It's a lot more awkward than I thought... but at the same time, I feel really satisfied just sitting next to him."
    "Man, I really need to figure out my own feelings don't I?"
    show s 1 u think at fdis
    s "\"Hmm... you know... I kinda want to call you by a pet name.\""
    mc 1 u wince "\"A... pet name?\""
    if povFirstName == "Yuuichi":
        s "\"Yeah. I already slip up and call you \'Yuu\' every now and again. Maybe I should just start calling you that all the time.\""
    else:
        s "\"Yeah. I kinda want to call you something different since we're dating now and all.\""
    show s 1 u flattered at fdis
    s "\"It might be a bit corny but... I've always dreamed of calling a partner of mine by a name no one else was allowed to use.\""
    mc 1 u avoidb "\"I don't know...\""
    show s 1 u smile at fdis
    s "\"It's up to you. I won't do it unless you let me.\""
    show s 1 u think at fdis
    s "\"Although it would probably have to be something inconspicuous since we can't just give away that we're dating. Maybe we should stick to shortening your name?\""
    "I..."
    $ povPetName = renpy.input("What should I have him call me? Default: Yuu", length=15) or "Yuu"
    if povPetName == povFirstName:
        mc 1 u considerate "\"Sorry, Shoichi. I don't think I'm comfortable with that kind of thing just yet.\""
        show s 1 u sad at fdis
        s "\"Aww. Alright.\""
        jump Day16_Shoichi_Named
    if povPetName == "Love":
        "No, wait... if he called me that in public everyone would realize what's going on wouldn't they?"
        mc 1 u considerate "\"I... think we'd better just stick with my name like we always have.\""
        show s 1 u sad at fdis
        s "\"Aww. Alright.\""
        $ povPetName = povFirstName
        jump Day16_Shoichi_Named
    if povPetName == "Sweetie":
        "No, wait... if he called me that in public everyone would realize what's going on wouldn't they?"
        mc 1 u considerate "\"I... think we'd better just stick with my name like we always have.\""
        show s 1 u sad at fdis
        s "\"Aww. Alright.\""
        $ povPetName = povFirstName
        jump Day16_Shoichi_Named
    if povPetName == "Honey":
        "No, wait... if he called me that in public everyone would realize what's going on wouldn't they?"
        mc 1 u considerate "\"I... think we'd better just stick with my name like we always have.\""
        show s 1 u sad at fdis
        s "\"Aww. Alright.\""
        $ povPetName = povFirstName
        jump Day16_Shoichi_Named
    if povPetName == "Hun":
        "No, wait... if he called me that in public everyone would realize what's going on wouldn't they?"
        mc 1 u considerate "\"I... think we'd better just stick with my name like we always have.\""
        show s 1 u sad at fdis
        s "\"Aww. Alright.\""
        $ povPetName = povFirstName
        jump Day16_Shoichi_Named
    if povPetName == "Dear":
        "No, wait... if he called me that in public everyone would realize what's going on wouldn't they?"
        mc 1 u considerate "\"I... think we'd better just stick with my name like we always have.\""
        show s 1 u sad at fdis
        s "\"Aww. Alright.\""
        $ povPetName = povFirstName
        jump Day16_Shoichi_Named
    mc 1 u avoidb "\"How about... [povPetName]?\""
    if povPetName == "Yuu":
        show s 1 u happy at fdis
        s "\"Hehe. So I'm finally allowed to call you that, huh? I've always wanted to call you that way.\""
        mc 1 u wince "\"Why?\""
        show s 1 u smile at fdis
        s "\"It just feels more special if I call you Yuu instead of [povFirstName].\""
        mc 1 u worried "\"You have very weird thoughts.\""
        show s 1 u happy at fdis
        s "\"I guess.\""
    else:
        show s 1 u think at fdis
        s "\"[povPetName], huh?"
        show s 1 u happy at fdis
        extend " I like it!\""
        mc 1 u avoidb "\"Feels kinda embarrassing though but... I guess it's good.\""
        show s 1 u smile at fdis
        s "\"Now I'll be the only one who gets to call you something different. That's one way to feel special.\""
        mc 1 u sigh2 "\"You're pretty easy to please, huh?\""
        show s 1 u happy at fdis
        s "\"Pretty much.\""
label Day16_Shoichi_Named:
    show s 1 u smile at fdis
    s "\"And by the way..."
    show s 1 u happy at fdis
    extend " I love you, [povPetName].\""
    play sound "music/heartbeat.ogg"
    "!"
    mc 1 u avoidb "\"Don't just say that out of nowhere. It's embarrassing!\""
    s "\"Hehe. It just feels so good to finally be allowed to say it.\""
    mc 1 u sigh2 "\"You're so weird.\""
    show s 1 u smile at fdis
    s "\"By the way, I've already finished my lunch. Do I get a kiss now?\""
    mc 1 u flustered "\"Y-you won't let this go, will you?\""
    show s 1 u happy at fdis
    s "\"Not unless you actually say no.\""
    "My face feels so hot right now..."
    mc 1 u sigh2 "\"... I'm gonna finish my food first.\""
    show s 1 u smile at fdis
    s "\"Sure!\""
    "... It's going to take me some time to get used to all this."
    stop music3 fadeout 2.5
    scene SGate with fade
    play music2 "music/BGM/Groundwork.ogg" fadein 5.0
    "I'm walking towards practice for the day."
    "I've made some progress in improving my stamina and backhand lately."
    "Since those are some of my weakest areas, it's good to be able to work on them."
    show k 1 t at fdis, three
    show sa 1 t think at fdis, seven
    with dissolve
    "I see Kei-kun and Saya talking to each other in front of the building while a mass of students does a variety of exercises on the side."
    show k 1 t smile at fdis
    show sa 1 t at fdis
    k "\"Ah, good afternoon, [povFirstName]-san.\""
    mc 1 u smile "\"Hey there. What are you guys talking about?\""
    show k 1 t at fdis
    sa "\"We were discussing the possibility of renting a few courts for the students that will take part in the Kanto Regional tournament in July. It's not good to be missing practice for a whole month.\""
    mc 1 u "\"That sounds like a good idea. What do you guys need?\""
    k "\"Right now? Budget. Even if it's just until the festival is over, renting courts for five hours a day and five days a week would be pretty costly.\""
    show sa 1 t talk at fdis
    sa "\"We'd have to submit a request to the student council and they would then have to submit it to the school.\""
    mc 1 u sigh "\"Oh, great. Bureaucracy.\""
    show k 1 t smile at fdis
    show sa 1 t at fdis
    k "\"We do have Urata who can intercede on our behalf if we ask nicely.\""
    mc 1 u sigh "\"Just try not to ask too many favors of him. He's already got a lot of stuff to do as it is.\""
    show k 1 t at fdis
    k "\"I know that. It's just this one thing.\""
    show sa 1 t talk at fdis
    sa "\"By the way, did you guys manage to get that thing done?\""
    mc 1 u confused "\"What thing?\""
    show sa 1 t bored at fdis
    sa "\"Erm... the thing he pulled you away during lunch to do?\""
    mc 1 u shock "\"O-oh. Y-yeah, that! Sure, we managed to get it done.\""
    show sa 1 t at fdis
    k "\"You guys were working on something during lunch time? What was it?\""
    mc 1 u considerate "\"I-It's just student council stuff. Really boring. Just forget about it.\""
    show k 1 t sigh at fdis
    k "\"You do know I plan to run for the student council next year, right? Knowing about it could even be helpful for me.\""
    mc 1 u fsmile "\"T-that's a bit...\""
    play sound "music/tap.ogg"
    show k 1 t at fdis, two
    show sa 1 t smile at fdis, five
    with move
    show s 1 u smile at fdis, eight with moveiridis
    s "\"Hey, guys.\""
    mc 1 u shock "\"Waah!\""
    "Shoichi suddenly walks up behind me, putting a hand on my shoulder and making me jump."
    show k 1 t at fdis
    show sa 1 t at fdis
    k "\"Urata, have you been asking for [povFirstName]-san's help on council related issues?\""
    show s 1 u think at fdis
    s "\"Uhh... just this morning. Why?\""
    show k 1 t sigh at fdis
    k "\"You know, I actually {i}want{/i} to be in the student council. Why couldn't you call me?\""
    show sa 1 t talk at fdis
    sa "\"That's what I asked him this morning.\""
    show s 1 u considerate at fdis
    show k 1 t at fdis
    s "\"Come on, don't make a big deal out of this. I just had a pick of people that could all help me and I decided I preferred [povPetName] with me.\""
    if povPetName == povFirstName:
        jump Pet
    else:
        show sa 1 t confused at fdis
        sa "\"[povPetName]?\""
        "Saya looks right at me with a raised eyebrow."
        "I immediately look away, suddenly feeling very exposed."
        show s 1 u think at fdis
        s "\"Err... I just thought I'd switch things up a bit. No big deal.\""
    label Pet:
    show s 1 u smile at fdis
    show sa 1 t at fdis
    s "\"Now, if you guys don't mind I'm going to steal [povFirstName] for the day.\""
    mc 1 u shock "\"W-what? But I have practice.\""
    show s 1 u happy at fdis
    s "\"Come on, I just need your help with something. Pretty please?\""
    k "\"Twice in a single day? Give him a rest. He was just telling us not to ask too many favors of you and here you are doing it again in the same day.\""
    show s 1 u at fdis
    s "\"Asking me favors?\""
    mc 1 u avoid "\"They want your help to secure more budget for the tennis club so we can rent courts for the players that'll participate in the Regional tournament to practice.\""
    show s 1 u think at fdis
    s "\"Oh... Sure, why not? Submit an application and I'll have a look. See if I can fast-track the process.\""
    mc 1 u shock "\"That easy?\""
    show s 1 u happy at fdis
    s "\"Of course. It's your club after all and it'll directly benefit you. Why shouldn't I?\""
    "..."
    "This feels weird..."
    "Am I getting preferential treatment?"
    show k 1 t worried at fdis
    k "\"This isn't just for [povFirstName]-san's sake you know.\""
    show sa 1 t confused at fdis
    sa "\"Hmm...\""
    "Saya looks between the two of us with a raised eyebrow."
    "For some reason, it kinda creeps me out."
    mc 1 u fsmile "\"I... uhm... as long as it helps the club then it's fine, right?\""
    show k 1 t at fdis
    k "\"I suppose so...\""
    show s 1 u smile at fdis
    s "\"Anyway, I really need to steal him away now. Need him to help me choose some new... err, drapes for the house. Dad wants to do some renewal.\""
    sa "\"... And he's doing that by buying new drapes?\""
    show s 1 u happy at fdis
    s "\"Sure. Why not?\""
    "Learn to lie better!" with hpunch
    mc 1 u fsmile "\"I... I guess I should go with him then. Wouldn't want his father to... dislike his new drapes.\""
    sa "\"Sure. You do that.\""
    k "\"Alright. I'll get started on that application right after we end for the day. I'll see about having it ready for you in the morning, Urata.\""
    s "\"Great. I'll be waiting!\""
    stop music2 fadeout 2.5
    scene Park
    show s 1 u happy at fdis, five
    with fade
    play music3 "music/BGM/Snowy Day.ogg" fadein 5.0
    "Shoichi takes me to a nearby park."
    "He's all smiles the entire way there. Even as we walk in silence."
    "I can't help but feel a little annoyed the entire way there."
    show s 1 u smile at fdis
    s "\"What's wrong? You don't look so chipper right now.\""
    mc 1 u sigh2 "\"... You're way too obvious?\""
    show s 1 u at fdis
    s "\"I am? But I'm not even touching you right now.\""
    mc 1 u sigh "\"I'm not talking about now. Look at the horrible excuse you gave them. I'm sure Saya already thinks there's something up.\""
    show s 1 u think at fdis
    s "\"... With her, I wouldn't really doubt it.\""
    mc 1 u confused "\"What's that supposed to mean?\""
    show s 1 u considerate at fdis
    s "\"Oh... It's just that Saya-chan is really perceptive. A lot more than you think.\""
    mc 1 u confused "\"How so?\""
    show s 1 u wince at fdis
    s "\"... Okay, uhm... please don't get mad?\""
    mc 1 u sigh2 "\"... I'm not going to like this am I?\""
    show s 1 u considerate at fdis
    s "\"She's... kinda known about my feelings for you for a while now.\""
    mc 1 u shock "\"W-what?!\""
    show s 1 u wince at fdis
    s "\"I don't really know how she figured it out. She just walked up to me one day and asked me point blank about it. She later agreed to keep it a secret because she didn't want our friendship at risk...\""
    show s 1 u considerate at fdis
    s "\"She did say I needed to learn to be a little less obvious though.\""
    mc 1 u sigh2 "\"... Why am I not surprised?\""
    s "\"Sorry...\""
    show s 1 u smile at fdis
    s "\"Is that it though? If so, I'll try to be a little more careful."
    show s 1 u happy at fdis
    extend " I'm just so happy right now. I can't help it.\""
    "His tail wagging at the speed of a helicopter blade certainly makes that abundantly clear."
    show s 1 u smile at fdis
    s "\"Are we good then?\""
    mc 1 u avoid "\"...\""
    show s 1 u at fdis
    "When I don't answer, the look on his face shifts."
    s "\"[povPetName]? Is... there something else?\""
    mc 1 u avoidb "\"Just... You got me pulled out of practice without even asking me if I was okay with that. I was actually looking forward to it today you know...\""
    show s 1 u shock at fdis
    s "\"O-oh..."
    show s 1 u wince at fdis
    extend " I'm sorry. I didn't think you'd... I thought you'd be happy about that.\""
    show s 1 u considerate at fdis
    s "\"I just really want to spend even more time with you now that we're dating. I guess I wasn't thinking.\""
    mc 1 u avoidb "\"I don't think that's a bad thing. Just ask me beforehand okay?\""
    show s 1 u smile at fdis
    s "\"Roger!\""
    show s 1 u considerate at fdis
    s "\"And, uhm... sorry. I'm still pretty new to this whole dating thing. I don't really know how I'm supposed to act.\""
    mc 1 u smile "\"It's alright. We'll figure this out together.\""
    "Man, I feel weird for saying that."
    "Every time I think it out, I have a small pause in my brain where it just goes \"Shoichi and I dating? What are you, crazy?\""
    "I'm gonna have to learn to get rid of that one, huh?"
    show s 1 u smile at fdis
    mc 1 u think "\"Soooo, was there anything you had in mind that you wanted to do?\""
    show s 1 u happy at fdis
    s "\"Not at all. I just wanted to spend some time with you. I don't really mind what we're doing.\""
    mc 1 u smile "\"You really are easy to please.\""
    s "\"I am. As long as I'm with you I'm already happy.\""
    mc 1 u fsmile "\"M-man, you really have some pretty sappy lines now that we're dating.\""
    show s 1 u smile at fdis
    s "\"I've always wanted to say them but since we weren't dating before, I thought you'd be creeped out."
    "... That was probably a good call."
    show s 1 u happy at fdis
    s "\"Oh, I know! How about we go out for ice cream?"
    show s 1 u smile at fdis
    extend " That's a thing that couples do, right?\""
    mc 1 u "\"It's also a thing we already did even before we started dating.\""
    show s 1 u think at fdis
    s "\"Hmm... I guess that's true.\""
    show s 1 u at fdis
    mc 1 u considerate "\"Honestly, do you even remember what I told you this morning? You don't need to keep racking your brain trying to think of \"couple's activities\".\""
    show s 1 u sad at fdis
    s "\"I knoooow that. I just wanted us to do something fun together.\""
    mc 1 u "\"What's wrong with just having fun by doing the things we usually do?\""
    show s 1 u considerate at fdis
    s "\"I guess there's nothing wrong. I'm just being a bit greedy.\""
    mc 1 u smile "\"Heh. That you are.\""
    show s 1 u happy at fdis
    s "\"Hey... can you come with me for a second?\""
    "Shoichi grabs my hand and drags me to a few nearby trees."
    mc 1 u curious "\"Uhm... what are you doing?\""
    show s 1 u smile at fdis
    s "\"I just thought this patch of trees would be semi-private so I wanted to come here for a bit.\""
    show s 1 u flattered at fdis:
        ease .5 zoom 1.5 xoffset -30 yoffset 200
    play sound "music/chu.ogg"
    mc 1 u confused "\"Why-\""
    show s 1 u flattered at fdis:
        ease .5 zoom 1.0 xoffset 0 yoffset 0
    "Before my brain can even process what happened, I feel something press up against my lips and quickly pull back."
    mc 1 u dismayb "\"W-wha-\""
    s "\"Hehe. Sorry, I just really wanted to kiss you.\""
    mc 1 u flustered "\"W-warn me before you do things like that!\""
    s "\"Okay!\""
    "Ugh... the excitement has turned him into a happy-go-lucky idiot..."
    show s 1 u at fdis
    s "\"You don't seem too happy.\""
    mc 1 u sigh2 "\"You're kissing me in public. I'm embarrassed.\""
    show s 1 u think at fdis
    s "\"There's no one around though. We should be fine.\""
    mc 1 u sigh "\"You're too relaxed.\""
    "... There's no way I can tell him that I actually liked it."
    "He's already being dumb and careless as it is. He doesn't need another nudge."
    show s 1 u smile at fdis
    s "\"Really? Cause from my point of view, you're the one who's too tense.\""
    mc 1 u sigh2 "\"Whatever you say.\""
    show s 1 u happy at fdis
    s "\"Now let's go for that ice cream!\""
    "..."
    "It's really going to take me a while to get used to this..."
    $ date = None
    stop music fadeout 2.5
    stop music3 fadeout 2.5
    jump Day17_Shoichi
