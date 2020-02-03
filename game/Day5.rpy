label Day5:
    window hide
    scene April10 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene LivingRoom with fade
    window show
    $ date = "day5"
    play sound "music/knock.ogg"
    "I hear a knock on the door first thing in the morning as I prepare to leave for school."
    a 1 u "\"Aniki, there's someone at the door.\""
    "My younger brother shouts out groggily from the bathroom."
    mc 1 u talk "\"Coming!\""
    "I make sure to be loud enough so whoever is outside can hear me as well."
    scene HouseEntrance with fade
    play sound "music/slidingdoor.ogg"
    mc 1 u sigh "\"Who is i-\""
    show s 1 u smile at fdis, five with dissolve
    play music2 "music/BGM/Dazzling Sunlight.ogg" fadein 5.0
    s "\"Mornin'.\""
    "Shoichi smiles at me, his tail wagging."
    mc 1 u shock "\"Shoichi? What are you doing here?\""
    show s 1 u at fdis
    s "\"I wanted to go to school with you. You've got a problem with that?\""
    mc 1 u "\"N-no, not at all. I'm just surprised. We stopped walking to school together because you were always so busy.\""
    show s 1 u think at fdis
    s "\"Yeah, I know. But my entire schedule for the next two days ended up being cleaned by happenstance so I decided to use this break to come here.\""
    mc 1 u curious "\"Really? What happened?\""
    show s 1 u at fdis
    s "\"There was a bug problem going on with the volleyball courts so they had to be sealed off and fumigated so it'll be out of order for the day."
    show s 1 u wince at fdis
    s "\"And some of the new student council members took away a bunch of my assignments saying that I needed a break. I didn't agree to it, but they kicked me out of the room nonetheless.\""
    show s 1 u wry at fdis
    s "\"This is probably the freest I've been since we joined high school. To be honest, I'm not quite sure what to do with myself.\""
    mc 1 u fsmile "\"Well, that's pretty unexpected...\""
    show s 1 u sigh at fdis
    s "\"What? If you're dissatisfied with something I can just go to school on my own.\""
    "Shoichi pouts and turns away from me."
    mc 1 u nervous "\"Ah, sorry sorry. I'm super excited, see?\""
    "I wave my arms around in some sort of dance-like sequence. Shoichi starts laughing."
    show s 1 u happy at fdis
    s "\"What the hell are you doing? I was just joking.\""
    mc 1 u avoidb "\"W-Well, how should I have known that?!\""
    "Shit, I can feel my face getting hot."
    show s 1 u smile at fdis
    s "\"Come on, you've known me for years. How can you not have noticed that I was joking?\""
    mc 1 u sigh "\"I'm still sleepy, give me a break...\""
    show s 1 u happy at fdis
    s "\"Hey, if I waited for you to be fully awake, I'd be waiting forever.\""
    mc 1 u annoyed "\"I'm not sleepy all the time, jackass.\""
    show s 1 u smile at fdis
    s "\"Oh, really? When are you not?\""
    mc 1 u avoid "\"...When I'm asleep...\""
    show s 1 u happy at fdis
    s "\"See?\""
    mc 1 u annoyed "\"Oh, shut up.\""
    show s 1 u smile at fdis
    "I slip on a pair of shoes and grab my bag next to the door."
    mc 1 u "\"Aki, I'm heading out! Make sure you lock the doors when you leave!\""
    "I see a little arm waving at me from the door."
    a 1 u "\"A'ight!\""
    stop music2 fadeout 2.5
    play music "music/breeze.ogg"
    play music3 "music/BGM/Snowy Day.ogg" fadein 5.0
    scene Street2
    show s 1 u happy at fdis, five
    with fade
    "Shoichi and I begin our walk to school."
    "Man, it's been so long since the last time we did this. Two years, was it?"
    "It feels nice to have someone to talk to on the way over."
    "It's nostalgic, somehow."
    show s 1 u smile at fdis
    mc 1 u curious "\"By the way, what exactly happened with your council? I remember you telling me last week that your duties were at \"nightmare\" status.\""
    show s 1  think at fdis
    s "\"Ah, my new vice president found out I've been hiding paperwork from them and took it from me to divide amongst the members.\""
    mc 1 u frownj "\"... You've been hoarding work?\""
    show s 1 u wince at fdis, shake1
    s "\"I like my work with the SC. What's wrong with that?\""
    mc 1 u sigh2 "\"Other than the weirdest case of addiction I've ever seen, nothing.\""
    mc 1 u sigh "\"Still, you're doing way too much. I guess next time you blow off hanging out with me, I'll consult your VP about it.\""
    show s 1 u sigh at fdis
    s "\"Jeez, what a tattletale...\""
    "Shoichi's hand brushes on mine as we keep on walking."
    show s 1 u at fdis
    s "\"Ah, sorry.\""
    show s 1 u happy at fdis
    s "\"Oh, did I ever tell you? My mother is remarrying next year. Apparently, she met this-\""
    "His hand brushes mine again."
    show s 1 u avoid at fdis
    s "\"Ah, sorry.\""
    show s 1 u smile at fdis
    s "\"Anyway, she met a guy at a work meeting last year and they have been going out ever since. Isn't it great?\""
    mc 1 u cocky "\"Look at that, you're going to have a new dad.\""
    show s 1 u wince at fdis
    s "\"I'm too old to have a new dad. I'll just think of him as some guy my mom is-\""
    "His hand brushes up against mine for the third time."
    show s 1 u think at fdis
    s "\"Ah, sorry-\""
    mc 1 u frownj "\"What are you being so conscious of me for? That's creepy.\""
    show s 1 u sigh at fdis
    s "\"Geeze, I have at least an inkling of respect for personal space.\""
    mc 1 u sigh "\"No you don't. You don't even know what the definition of it is.\""
    s "\"Do you have that little faith in me?\""
    mc 1 u cocky "\"Faith? In you? Are you kidding?\""
    scene Street1
    show s 1 u sigh at fdis, five
    with fade
    s "\"Alright, I get it. I'm just being a bother aren't I? Maybe I should just g-\""
    mc 1 u sigh "\"I'm not falling for that one again.\""
    show s 1 u think at fdis
    s "\"Booo.\""
    mc 1 u smile "\"You seem to be in good spirits today.\""
    show s 1 u avoid at fdis
    s "\"Well, I {i}am{/i} a little pissed that they wrestled control of the SC from me, but..."
    show s 1 u considerate at fdis
    extend " It does feel good to have a free day, though. I suddenly have so much... time.\""
    mc 1 u suggestive "\"That is the definition of a free day, yes.\""
    show s 1 u sigh at fdis
    s "\"Well aren't you funny? I'm just trying to say that I don't have any idea what to do with myself.\""
    show s 1 u at fdis
    mc 1 u "\"Why don't you hang out with someone?\""
    show s 1 u think at fdis
    s "\"I don't really have any friends outside of you guys, and you're all busy with your own clubs.\""
    show s 1 u at fdis
    mc 1 u "\"Jun isn't.\""
    show s 1 u sigh at fdis
    s "\"Yes he is. Jun-kun is practicing for his piano competition next week.\""
    mc 1 u shock "\"Wait, what?!\""
    s "\"Didn't he tell you that already?\""
    mc 1 u shock "\"N-\""
    "Wait... I think he told me that sometime last week."
    mc 1 u fsmile "\"Ah.\""
    s "\"It seems he's not the only airhead around here, huh.\""
    mc 1 u wince "\"Shut it. Things have been very hectic lately. You can't expect me to remember every little thing.\""
    s "\"Sure, I guess.\""
    show s 1 u at fdis
    mc 1 u "\"Are you going to watch him?\""
    show s 1 u smile at fdis
    s "\"Yeah. I'm planning to make it a surprise. Saya and Urushihara are coming too.\""
    mc 1 u shock "\"W-Wha?!\""
    mc 1 u wince "\"How many people know about it?\""
    show s 1 u sigh at fdis
    s "\"Everyone but you, it seems.\""
    s "\"And after I told him we would all be going. Ah, how disappointed he'll be when he realizes you won't be there.\""
    mc 1 u annoyed "\"Cut it, Pinocchio. You just told me he doesn't know you're going yet.\""
    show s 1 u happy at fdis
    s "\"Oh, I was found out then, huh?\""
    mc 1 u sigh "\"Give me a break...\""
    s "\"Hehe!\""
    "Shoichi chuckles."
    "His tail is unusually lively this morning, going back and forth like a feather duster."
    "Shoichi stretches a little while walking."
    show s 1 u smile at fdis
    s "\"It's so good to be able to enjoy a quiet morning.\""
    mc 1 u smile "\"Maybe you should take that as a sign and cut back on all your responsibilities.\""
    show s 1 u wince at fdis
    s "\"Let's not get too crazy, okay?\""
    mc 1 u sigh "\"Oh, I'm pretty sure between the two of us, {i}I'm{/i} not the crazy one.\""
    show s 1 u sigh at fdis
    s "\"I prefer being called enthusiastic.\""
    mc 1 u sigh "\"And I'd prefer if my friend weren't a giant workaholic. \"You can't always get what you want\" indeed.\""
    show s 1 u scorn at fdis
    s "\"I'm not a workaholic!\""
    "I start counting on my fingers."
    mc 1 u "\"Student Council, Volleyball club, Class President, private tutor, cram school, college prep-\""
    show s 1 u wince at fdis
    s "\"Okay, okay, I got the message. Please stop. {size=-2}I can feel my stomach churn just from thinking about it...{/size}\""
    mc 1 u "\"I'm surprised you haven't had a stress related breakdown already. Or at least an ulcer.\""
    show s 1 u sigh at fdis
    s "\"I'm not stressed..."
    show s 1 u think at fdis
    extend " Well, maybe a little. Still, I like doing what I do.\""
    mc 1 u "\"Wouldn't hurt to delegate some tasks, though. You keep trying to do everything on your own. At least when you're working on the club and the council, you could rely on other people to do some of the more time consuming stuff.\""
    show s 1 u wry at fdis
    s "\"Uhm... I'm not sure if I'm okay with it...\""
    mc 1 u sigh "\"You're a control freak. You know that, right?\""
    show s 1 u judge at fdis
    s "\"H-Hey. Rude!\""
    show s 1 u considerate at fdis
    s "\"Though I suppose you might be right... just a little, though.\""
    scene SGate
    show s 1 u considerate at fdis, five
    with fade
    mc 1 u smile "\"You know I'm right.\""
    show s 1 u sigh at fdis
    s "\"Yeah, yeah. Get off my tail.\""
    "Even if he pretends to be annoyed, I know better. His tail hasn't stopped wagging since we left the house."
    "Girl" "\"Ah, Senpai!\""
    show s 1 u at fdis
    "A girl comes running towards Shoichi."
    "Girl" "\"I'm sorry, we had some trouble with the student council paperwork. We tried calling your phone, but you didn't answer.\""
    show s 1 u shock at fdis
    s "\"Huh?!\""
    "Shoichi pulls his phone from his pocket and, upon trying to use it, it doesn't light up."
    show s 1 u wince at fdis
    s "\"Wha- It didn't charge?!\""
    s "\"Crap, I must have forgotten to put it on the charger when I went to sleep!\""
    show s 1 u at fdis
    s "\"What papers are you having problems with?\""
    "Girl" "\"Eh? Ah, the school festival papers.\""
    show s 1 u wince at fdis
    s "\"Ah, I should have known. Is it the budget forms? Those are always a pain in the ass to deal with.\""
    show s 1 u wry at fdis
    s "\"Sorry, [povFirstName], it seems I won't be able to spend the morning with you after all.\""
    mc 1 u smile "\"Don't worry about it. Go deal with it before you have an aneurysm.\""
    show s 1 u considerate at fdis
    s "\"Thanks.\""
    show s 1 u at offscreenright with moveoridis
    hide s 1 u
    stop music3 fadeout 10.0
    "Shoichi rushes away, the girl following behind him."
    "I watch as his back fades away from my view."
    "..."
    "Guess I'll just wait in class until the bell rings."
    stop music fadeout 5.0
    scene SClass with fade
    play sound "music/schoolbell.ogg"
    "The sound of the bell snaps me out of my daze."
    "I get the feeling that this has been happening a lot lately."
    "Last week I had an excuse for it given the over training. Now though..."
    play music2 "music/BGM/Little by Little I walk.ogg" fadein 5.0
    show j 1 u gentle at fdis, five with moveiridis
    j "\"Hey, [povFirstName]-san, are you headed to practice today?\""
    "Jun approaches me with a big smile, his bag hanging from his shoulder."
    mc 1 u sigh "\"I have to. Practice is daily after all.\""
    show j 1 u think at fdis
    j "\"Hmm... really? Mizoguchi-san said you skip practice a lot, though.\""
    play sound "music/stab.ogg"
    mc 1 u wince "\"Ugh...\"" with hpunch
    "Of course she did."
    mc 1 u "\"By the way, Jun, aren't you going to take part in a competition soon?\""
    show j 1 u fluster at fdis
    j "\"Ah...\""
    "I watch his excitement drain in a second as his whole body sighs."
    mc 1 u shock "\"Ahhh, Jun, hold yourself together!\"" with hpunch
    show j 1 u sigh at fdis
    j "\"Ha ha fuuu. Ha ha fuuu.\""
    "Jun starts taking deep, rhythmical breaths."
    show j 1 u wince at fdis
    "Repeating this a few times seems to have relaxed him a bit."
    mc 1 u shock "\"What's with that reaction? Is there something going on that I should know?\""
    show j 1 u wry at fdis
    j "\"Ah... no, it's not that, it's just... hmm...\""
    show j 1 u wince at fdis
    j "\"I'm a little nervous about it, that's all.\""
    if jun_met == True:
        show j 1 u watch at fdis
        mc 1 u wince "\"Ah, that's true. You did tell me it had been a few years since you last played in front of other people.\""
        show j 1 u wry at fdis
        "Jun nods meekly."
        j "\"Yeah. It's been about seven years since my last competition.\""
        mc 1 u curious "\"Damn, that's a lot of time. Why the big break in your career?\""
        show j 1 u wince at fdis
        j "\"W-Well... I had some... family issues to deal with.\""
        mc 1 u "\"I see. Still, it's a good thing that you decided to get back to it. You really look very happy when you're playing the piano.\""
        mc 1 u happy "\"I really enjoy watching you.\""
        show j 1 u shockb at fdis
        "My words make him pause, as he takes a step back and stares at me with awe."
        show j 1 u gentle at fdis
        j "\"I'm glad you think so!\""
        "There's the Jun I know!"
    else:
        mc 1 u curious "\"Have you never played in a competition before?\""
        show j 1 u watch at fdis
        j "\"I have... it's been a while, though.\""
        mc 1 u curious "\"Why did you stop then? Not your cup of tea?\""
        show j 1 u avoid at fdis
        j "\"Something like that, yeah...\""
        show j 1 u sigh at fdis
        j "\"But I need to have good results in competitions this year, otherwise I won't get a scholarship for the music academy I want to join.\""
        mc 1 u shock "\"Those are a thing?\""
        show j 1 u shock at fdis
        j "\"Wha-? Of course they are. Most musicians study in conservatories and academias before starting their professional careers.\""
        show j 1 u wince at fdis
        j "\"I'm looking to join the Frankfurt University of Music, but they require a mile long list of achievements.\""
        show j 1 u at fdis
        j "\"If I'm starting now, I'll need to get first place in all competitions I take part in until the end of the year to even get them to look at my application...\""
        mc 1 u shock "\"W-wow. Sounds tough.\""
        show j 1 u wry at fdis
        j "\"It is... I've been pulling all-nighters every other day to practice.\""
        show j 1 u wince at fdis
        j "\"Yesterday I was practicing Beethoven's Moonlight Sonata like I always do and I blanked midway. That's never happened to me before!\""
        mc 1 u fsmile "\"Sounds rough...\""
        "...I've never seen someone suffer from performance anxiety before their actual performance."
    show j 1 u watch at fdis
    mc 1 u curious "\"How many songs are you performing next week?\""
    j "\"Two. Saint-Saëns's \"Allegro Apassionato\" and-\""
    show j 1 u shock at fdis
    mc 1 u wince "\"You don't have to tell me the names. {size=-2}I won't know what you're talking about anyway{/size}.\""
    show j 1 u wince at fdis
    j "\"Ah. Sorry, sorry.\""
    if jun_met == True:
        show j 1 u watch at fdis
        mc 1 u curious "\"Are those songs any harder than the one I heard you play?\""
        if tour_jun == False:
            show j 1 u think at fdis
            j "\"Which one? There was Moo-\""
            mc 1 u sigh "\"Please, no names...\""
            show j 1 u wince at fdis
            j "\"A-ah, right.\""
            show j 1 u think at fdis
            j "\"Anyway, I guess it's so-so. The technical difficulty level isn't that high, but...\""
        else:
            show j 1 u think at fdis
            j "\"The one you heard... Ah, that was \"Moonlight Sonata, 3rd Movement\".\""
            "I'll just nod and pretend I know that name."
            j "\"They're easier songs... at least on the technical aspect, but...\""
    else:
        show j 1 u watch at fdis
        mc 1 u curious "\"Are these songs particularly hard? I mean... I haven't seen you play before, so I don't know how-\""
        show j 1 u wry at fdis
        j "\"I get it, I get it."
        show j 1 u think at fdis
        extend " And... well... They're not super difficult. From a technical standpoint, I've played harder songs before, but...\""
    mc 1 u curious "\"What? You need something other than the technique?\""
    show j 1 u wince at fdis
    j "\"W-well... No, not really.\""
    mc 1 u smile "\"Then you're worrying over nothing.\""
    j "\"Ah... I suppose so.\""
    show j 1 u smile at fdis
    j "\"Well, I'm heading over to the music room to practice.\""
    mc 1 u curious "\"They let you use it without a supervisor?\""
    show j 1 u think at fdis
    j "\"Sure. I've been using it every day since I transferred here.\""
    "Hmm... I think I should start dropping by more often."
    show j 1 u happy at fdis
    j "\"See you tomorrow.\""
    mc 1 u smile "\"See ya!\""
    stop music2 fadeout 5.0
    show j 1 u happy at offscreenright with moveoridis
    "Guess I should get going too."
    scene SCorridor with fade
    play sound "music/slidingdoor.ogg"
    "I probably should attend practice more often. I don't want Jun thinking I'm some kind of lazy bu-"
    play sound "music/fall.ogg"
    "Right as I'm leaving my classroom, I bump into someone that was trying to go in and we both fall to the floor."
    mc 1 u wince "\"Ow, what are you-\""
    play music2 "music/BGM/Autumn Day.ogg" fadein 5.0
    show k 1 u wince at fdis, five with dissolve
    "Keisuke is rubbing his backside with a pained expression."
    k "\"At least look where you're-"
    show k 1 u uncomfortable
    extend " Ah!\""
    "As soon as we lock eyes, he trails off.\""
    "I get up and offer him a helping hand."
    play sound "music/tap.ogg"
    mc 1 u smile "\"Sorry about that, I was distracted.\""
    "He dusts himself off with his hands."
    show k 1 u worried at fdis
    k "\"It's fine. I was looking for you anyway.\""
    mc 1 u "\"Couldn't you just wait for me at the courts?\""
    show k 1 u sigh at fdis
    k "\"That's exactly what I came over to tell you. I've talked to Coach. Practice has been canceled today.\""
    mc 1 u shock "\"What? Why?\""
    show k 1 u avoid at fdis
    k "\"Apparently, they were supposed to fumigate the volleyball court today and did a bad job of isolating it. Now the whole building needs to be fumigated.\""
    show k 1 u at fdis
    k "\"Coach said they should be finished by Wednesday.\""
    mc 1 u annoyed "\"You're kidding. We can't have a two day break in practice!\""
    show k 1 u wince at fdis, shake1
    k "\"Don't yell at me, I'm just the messenger.\""
    mc 1 u shock "\"Gah, sorry sorry.\""
    "Oh, come on. The one time I'm actually excited to practice!"
    show k 1 u worried at fdis
    k "\"We'll just have to find something else to do now. I think Mizoguchi-senpai said she's going to try and pick up a few more shifts at the café.\""
    mc 1 u "\"Hmm... And what are you planning to do?\""
    show k 1 u shock at fdis
    play sound "music/disappointment.ogg"
    "Hey, come on, don't look so surprised that I'm showing an interest in you."
    show k 1 u avoid at fdis
    k "\"Practice.\""
    mc 1 u curious "\"Practice? How? Do you have a tennis court at home or something?\""
    k "\"I do, but that's not what I'm going to practice.\""
    mc 1 u sigh "\"Then what {i}are{/i} you going to practice? Don't tell me you're practicing drawing for the manga club.\""
    show k 1 u angryb at fdis
    k "\"N-no!"
    show k 1 u avoidb at fdis
    extend " I never intended to draw. I'm only in the manga club because I enjoy reading it.\""
    show k 1 u annoyed at fdis
    k "\"Anyway, consider the message delivered. I'm going home now. See you tomorrow.\""
    show k 1 u annoyed at fdis, offscreenleft with moveoledis
    "Without letting me get another word in, Kei-kun turns around and walks out."
    "Damn, he can be pretty intense sometimes..."
    "So there's no practice today, huh?"
    "What I should do..."
    menu:
        "Look for Shoichi.":
            "I wonder... maybe Shoichi's finished for the day too? I guess I'll drop by the Student Council room."
            "Well, at least if he's not, I get to have fun watching him freak out over paperwork."
            "Win/win."
            "As I come across the Student Council office, I hear two people talking inside. From their tone, they seem to be in a bad mood."
            "I recognize one of them immediately as Shoichi's. The other is unfamiliar to me."
            play sound "music/knock.ogg"
            "I give a light knock on the door and, immediately, the two are silenced."
            "I hear hurried steps coming over to the door and it is suddenly opened with force."
            show s 1 u frown at fdis, five with dissolve
            s "\"I'm sorry but we're quite bu-"
            show s 1 u shock at fdis
            extend " Oh...\""
            "I-is something wrong here? What's with that look he had on his face?"
            mc 1 u worried "\"Is this a bad time?\""
            show s 1 u wry at fdis
            s "\"No, I'm sorry to have been rude. Is there anything you need?\""
            "I peer over his shoulder and see a cheetah girl absentmindedly fiddling with a stack of papers."
            "Is it just me or is she glaring at me?"
            "Yep. Definitely bad timing."
            "Cheetah Girl" "\"Urata-senpai, we don't have time for chit-chat. If we want to get these papers done by the end of the day, we're going to need you to hurry.\""
            "Her voice echoes from inside the room. She sounds so stuck up..."
            show s 1 u considerate at fdis
            s "\"Yeah, yeah. I know, Kisaragi. Let's just take a break. We've been at it non-stop since morning any way. I need to stretch my legs.\""
            "Cheetah Girl" "\"But-\""
            show s 1 u at fdis
            "She tries to protest but Shoichi just waves his hand in dismissal."
            "The girl groans and plops down on a chair, looking right at me with eyes full of fury."
            "Shoichi steps out of the room, closing the door behind him."
            show s 1 u wry at fdis
            s "\"Sorry, it's been kind of a long day.\""
            mc 1 u worried "\"You've been at it since this morning? Please tell me you haven't been here since we split up at the gate.\""
            show s 1 u considerate at fdis
            "The look on his face tells me everything I need to know."
            show s 1 u wry at fdis
            s "\"Someone made a huge mistake with some paperwork and completely blew the School Festival's budget out of the sky.\""
            mc 1 u worried "\"How bad is it?\""
            show s 1 u considerate at fdis
            s "\"Well... let's just say that a few clubs are going to have their budgets slashed in half for the rest of the year and leave it at that.\""
            mc 1 u shock "\"What the hell kind of mistake did they make?!\""
            show s 1 u wry at fdis
            s "\"Don't worry about it. Plus, I managed to save the budget for the tennis club, so you don't have to worry about your training being compromised.\""
            mc 1 u shock "\"Wha- What about the Volleyball club budget?\""
            show s 1 u think at fdis
            s "\"A reduced budget isn't going to kill us.\""
            mc 1 u shock "\"Bu- Wha- How did this even happen?\""
            show s 1 u sigh at fdis
            s "\"Someone forgot to double-check before submitting and didn't see a couple of... extra zeros.\""
            mc 1 u wince "\"I'm... sorry to hear that. What's he going to do now?\""
            show s 1 u happy at fdis
            s "\"Well... provided the cops don't find his body, he'll just lie quietly in the ditch.\""
            mc 1 u judgef "\"...Okay, usually I find these jokes funny but now I can't tell if you're joking.\""
            s "\"I could tell but I'm not sure if you'd manage to keep it from the police during questioning.\""
            mc 1 u judgef "\"For the love of God, say \"Just kidding.\" or something!\""
            play sound "music/tap.ogg"
            show s 1 u laugh at fdis
            "Shoichi laughs, giving me a few pats on the shoulder."
            s "\"Sorry, I'll stop messing with you. It's just... you're so easy, I can't help it.\""
            mc 1 u sigh "\"Well, gee, I'm glad I'm such a good comedic relief for you.\""
            mc 1 u "\"Anyway, I was hoping we could go home together, when do you think you might be finished?\""
            show s 1 u avoid at fdis
            "His face goes stiff again. He scratches the back of his neck, awkwardly avoiding eye contact."
            s "\"Sorry, [povFirstName], today's just not a good day. I think I'll only get to leave once school closes. Besides, don't you have practice today?\""
            mc 1 u sigh "\"They did a bad job of isolating the volleyball courts and now they had to hurry it up to fumigate ours as well.\""
            show s 1 u shock at fdis
            s "\"Wha- But... we don't {i}have{/i} the money to pay for the tennis court fumigation. It didn't even {i}need{/i} to be fumigated!"
            show s 1 u wince at fdis
            extend " Aww, crap, they're going to take it out of the festival budget aren't they?\""
            mc 1 u think "\"Don't worry, I'm sure the students would riot if they did. Plus, I don't think the company would charge for it, considering it was their fault and all that.\""
            show s 1 u considerate at fdis
            "His expression softens up a bit. He sighs in relief."
            s "\"You're right. I'm just being paranoid.\""
            show s 1 u wry at fdis
            s "\"Sorry, I think you should go home on your own today.\""
            mc 1 u smile "\"I can wait. I don't mind.\""
            show s 1 u shock at fdis
            s "\"What? I just told you it'd take hours. What would you even do? Just sit there and wait for us to be done?\""
            mc 1 u think "\"Pretty much, yeah.\""
            "He stands there in a daze, gaping."
            show s 1 u wince at fdis
            s "\"A-Are you sure?\""
            mc 1 u smile "\"Shoichi, I don't mind waiting for a bit if it means I get to spend some time with you.\""
            mc 1 u happy "\"You did promise me this morning that you'd use this little break of yours to spend more time with me, didn't you?\""
            "He seems shocked to hear my words, mouthing something off without actually making a sound."
            play sound "music/slidingdoor.ogg"
            "He turns his back to me and hastily opens the door to the room again."
            show s 1 u avoidb at fdis
            s "\"Alright. You can wait inside, I have to get back to it already.\""
            mc 1 u sigh "\"Weren't you supposed to be stretching your legs?\""
            show s 1 u avoid at fdis
            s "\"... I don't feel like it.\""
            stop music2 fadeout 5.0
            scene SCRoom
            show s 1 u at fdis, five
            with fade
            play sound "music/chairscoot.ogg"
            "Shoichi drops down onto his chair, pulling up a pile of folders."
            play sound "music/pageflip.ogg"
            "He quietly flips through the sheets of paper, calmly examining each and every one of them."
            "I watch as his eyes attentively scan through every word that's printed on those papers."
            "..."
            "Meanwhile, I can feel the cheetah's murderous glance even without having to look over her way."
            "Almost as if my mere presence here were somehow offensive."
            scene SGateN with fade
            play music "music/night.ogg"
            "After quite a few of some of the most boring hours of my life, a teacher came by to ask us to leave."
            "Sheesh, he really wasn't kidding when he said we'd be sticking around until the school closed for the day..."
            show s 1 u considerate at fdis, five with dissolve
            s "\"Sorry you got held up for so long.\""
            mc 1 u think "\"It's fine. I'm the one who asked to stay anyway.\""
            show s 1 u sigh at fdis
            s "\"And that's exactly why I insisted that you didn't. I still feel bad about it.\""
            show s 1 u happy at fdis
            s "\"How about I treat you to some food as an apology?\""
            mc 1 u wince "\"You have no reason to apologize.\""
            show s 1 u smile at fdis
            s "\"Then as a thank you.\""
            "He's really not taking no for an answer, huh?"
            mc 1 u smile "\"Alright. If you insist on spending your money on me, I have no reason to say no.\""
            show s 1 u laugh at fdis
            "Shoichi laughs and nods, turning around as we start leaving school."
            stop music fadeout 5.0
            $ day5 = "shoichi"
            jump Day5_Shoichi
        "Watch Jun's practice.":
            "I think I'll go look for Jun."
            "He left for the music room not long ago. I'll probably catch him just as he's starting his routine."
            "I can't deny that I'm interested."
            if jun_met == True:
                "The last time I saw him play, I felt almost as if it was calling out to me. I was completely drawn to his music."
            else:
                "I've never seen a live piano performance before so I'm really interested in seeing what it's like."
            "Before I even finish debating it with myself, I realize that I'm already walking towards the Music Room."
            scene SCorridor with fade
            stop music2 fadeout 5.0
            play music3 "music/BGM/Classical/OP. 23 - Prelude in G Minor.ogg" fadein 10.0
            "As I come closer to the Music Room, I start hearing the sound of the piano echoing through the hallway."
            if jun_met == True:
                "Just like last time, the sound of the piano draws me in."
                "It feels like I'm being called. Lured in by a mesmerizing tune."
            else:
                "Once I perk my ears up to listen closely, I start to feel as if the piano were calling out to me."
                "My body begins to move on its own, wanting to get closer and hear this melody not only with my ears, but with my whole self."
            play sound "music/slidingdoor.ogg"
            scene MusicRoom
            show cg2
            with fade
            "I go in as quietly as I can, trying not to disturb Jun as he plays."
            if jun_met == True:
                "I don't want to make a repeat of last time."
            else:
                "Given how jumpy he can be, I don't want to freak him out by surprising him midway."
            "I exercise all of my self-control and stay in the back of the room, watching from a distance."
            "I watch Jun rocking his body back and forth to the melody, gently playing the keys."
            "His hands are moving like a blur. My eyes can barely keep up with his fingers."
            "His brows are furrowed as he continuously hammers the keys."
            if jun_met == True:
                "Just like last time, he has his eyes closed. How can he even play the piano like that?"
            else:
                "Does he... are his eyes closed?"
                "How can he even play like that?"
            "It's terrifying how hard he can concentrate when he wants to."
            "This certainly doesn't seem like the same guy who constantly spaces out even when being talked to."
            "But then again, who am I to complain about that?"
            "Eventually, I notice something that strikes me as odd."
            "Jun is panting a lot, as if he was having difficulty breathing."
            "He slows down, hunching over the piano."
            "Something is definitely wrong, he's gritting his teeth as if he was in pain."
            "His tail starts flicking randomly, almost thrashing."
            "I instinctively move towards him, slowly at first."
            stop music3
            hide cg2
            show j 2 u pain at fdis, five
            with dissolve
            "He's wheezing painfully whilst clutching his chest."
            "I can tell just from the sounds he's making that he's struggling to breathe."
            mc 1 u shock "\"Jun!\""
            "I cover the rest of the distance in a flash, rushing to support him."
            play music2 "music/BGM/Sighs.ogg" fadein 5.0
            j "\"Huh? Who-... Ah, [povFirstName]-san?\""
            "His eyes are completely unfocused. I can tell whenever a new wave of pain shoots up because of how he groans, his eyes squeezing shut."
            mc 1 u frightened "\"What's going on? What should I do? Do you want me to call the school doctor?\""
            "Jun grabs my arm with his other hand, squeezing me hard."
            show j 2 u fsmile at fdis
            j "\"{size=-2}N-no... it's fine. I just need... some rest.{/size}\""
            "He's... smiling?"
            "No, don't look at me like that."
            "Don't smile at me when you're in pain. This is wrong!"
            j "\"Just... shortness of breath.\""
            mc 1 u frightened "\"This doesn't look like shortness of breath. Does your chest hurt?\""
            "The answer should be obvious. And yet, in my panic, without knowing what to do, it's the only thing that rolls out of my tongue."
            "He shakes his head, mouthing out a mute \"No.\""
            show j 2 u gsmile at fdis
            j "\"Just shortness of breath... it's fine.\""
            "His voice is coming out clearer. His tensed up body begins to relax little by little as he takes longer, deeper breaths."
            "Slowly, he lets go of my arm and adjusts himself on his chair."
            "I can see his face twitch every now and then, as if a new wave of pain came every few seconds and he was doing his best to mask it."
            show j 2 u fsmile at fdis
            j "\"What are you doing here, [povFirstName]-san?\""
            mc 1 u frightened "\"That doesn't matter right now. What happened? Are you alright?\""
            show j 2 u gsmile at fdis
            "He tries laughing it off but his voice is weak, he flinches and reaches for his chest again."
            "He catches himself doing it halfway through and stops."
            show j 2 u fsmile at fdis
            j "\"I'm fine. This isn't new for me.\""
            mc 1 u shock "\"Wha- are you saying this happened before? Come on, I'm taking you to the school doct-\""
            show j 2 u gsmile at fdis
            "Jun pushes away my arm and shakes his head in negative."
            j "\"There's no need. It's fine. I'm already seeing a doctor for it.\""
            "This is weird. He usually goes along with everything we do or say. Why is he suddenly being so stubborn."
            mc 1 u annoyed "\"Oh really? Then what happened? What do you have?\""
            "He stutters."
            show j 2 u fsmile at fdis
            j "\"I-It's not a disease or anything. It's just... just weak constitution. That's all.\""
            show j 1 u wince at fdis
            "Almost as if he were trying to prove his point, Jun takes a few more deep breaths, readjusting himself and standing upright."
            mc 1 u angry "\"Weak constitution? You expect me to believe you had a bout of chest pain from weak constitution? Jun, chest pains are serious!\""
            show j 1 u wince at fdis
            j "\"It's... it's chronic. I've had it since I was a kid. It's no problem.\""
            show j 1 u wry at fdis
            j "\"It happens every now and again. I just have to bear it when it does.\""
            show j 1 u considerate at fdis
            j "\"Really, you don't need to worry.\""
            "He's usually so mild... he goes along with anything I say or ask him to do."
            "Why is he being so stubborn all of a sudden? I don't understand!"
            "Unable to come up with anything else to say, I merely relent."
            mc 1 u sigh2 "\"Alright, fine. I'll believe you for now. But at least come with me to the school doctor to get yourself checked out.\""
            "I reach my hand towards his shoulder to help him get up."
            show j 1 u annoyed at fdis
            j "\"No!\""
            play sound "music/slap.ogg"
            "Jun slaps away my hand that was reaching towards him."
            show j 1 u shock at fdis
            "He then gasps."
            show j 1 u wince at fdis
            j "\"Ah, I'm sorry!\""
            "He immediately bows down and apologizes."
            j "\"I-I'll go after I'm finished here. I really need to practice more. I still haven't gotten the songs comfortably down and I only have one week 'till the competition.\""
            mc 1 u worried "\"Have you ever thought about what the stress might be doing to you? Come on, it won't take ten minutes to get you checked out. If there's nothing wrong, the doctor will just sign you out and you'll be able to get back to practice.\""
            stop music2 fadeout 5.0
            j "\"Alright, I'll go.\""
            "Jun reluctantly gets up."
            "I immediately grab his wrist and almost drag him to the Doctors Office before he has time to change his mind."
            scene Doctor
            play music "music/tickingclock.ogg"
            show j 1 u watch at fdis, seven
            show do 1 u bored at fdis, three
            with fade
            do "\"Well, everything seems fine to me.\""
            "Good thing we came here after class. There wasn't anyone waiting for a consult so we were able to get in immediately."
            "The doctor does a few quick tests, checking Jun's heart rate, temperature and the like."
            do "\"No signs of fever or mucus. Your heart seems to be doing fine as well.\""
            do "\"Sit up for me so I can check your breathing...\""
            "The doctor pushes his stethoscope against Jun's bare chest and moves it around for a bit."
            show j 1 u wince at fdis
            j "\"Ah, that's cold!\""
            "Jun almost shoots out of the chair when the stethoscope touches him."
            do "\"Yes, it was already cold last time, it's not going to magically become warm this time.\""
            j "\"S-sorry.\""
            "Our school's Doctor is a very humorous person."
            "Unfortunately, he seems to have picked the one guy who doesn't understand the concept of teasing."
            show j 1 u watch at fdis
            do "\"No abnormal sounds in either of the lungs... take a deep breath.\""
            "Jun does as instructed."
            show j 1 u wry at fdis
            do "\"Yes... Well, everything seems to be the same as always, Kobayashi-kun.\""
            "I sigh, relieved at the good news... but for some reason, when I look over at Jun, he doesn't seem happy."
            j "\"Then I'll get back to practice-\""
            do "\"Not so fast. I said there's nothing out of the ordinary but I can't let you overexert yourself. When was the last time you got some actual rest? I guess you've been playing every time you had free time, haven't you?\""
            show j 1 u wince at fdis
            j "\"But-\""
            do "\"Kobayashi-kun, do remember that I have access to your records.\""
            "He picks up a rather large file from his desk and waves it around for effect."
            j "\"Guh... Alright...\""
            show j 1 u sigh at fdis
            "The Doctor turns to look at me, as if studying me for a while."
            do "\"[povLastName]-kun, since you're already here, would you mind doing me a favor? I have a few files that need to be taken to the staff room, could you do it for me?\""
            mc 1 u shock "\"What? Me?!\""
            do "\"It will only take a second. I'll just have a word with Kobayashi and send him on his way. We'll be done by the time you come back.\""
            mc 1 u wince "\"Okay, okay. I'll do it.\""
            do "\"Thank you.\""
            "He points to a box in the corner of the room."
            "I pick it up and start leaving the office."
            mc 1 u "\"Jun, wait for me, okay?\""
            show j 1 u wry at fdis
            "He nods."
            stop music fadeout 2.5
            scene SCorridor with fade
            $ renpy.pause (0.5)
            scene StaffRoom with fade
            $ renpy.pause (0.5)
            scene SCorridor with fade
            $ renpy.pause (0.5)
            "It takes a little longer to get things done than I imagined it would."
            "Everything was going fine until I got held back by Katsuragi-sensei for another round of lectures."
            "Crazy old hag..."
            play music2 "music/BGM/I Want to Know You - Narration.ogg"
            show j 1 u blank at fdis, five with dissolve
            "I see Jun standing by the Doctor's Office, kicking up some dust at the floor."
            "When I look at his face, I see a look that I've never seen him make before. It's just... nothing. His face is blank."
            "It's weird."
            show j 1 u shock at fdis, shake1
            mc 1 u worried "\"Bad news, I take it?\""
            "He jumps up in surprise when I start talking. I guess he didn't notice me approaching?"
            "He takes a few moments to compose himself. Then, looking down at the floor again, he stammers a few words."
            show j 1 u wince at fdis
            j "\"I'm not allowed to touch my piano for the rest of the day. He called my parents and they told me to go straight home.\""
            show j 1 u annoyed at fdis
            j "\"You couldn't have left me alone, could you?\""
            "W-wait. He's getting angry at me?! I was just trying to take care of him!"
            mc 1 u wince "\"I'm an athlete. I take health issues seriously.\""
            "He keeps glaring at me, except this time I make sure not to back down. If the doctor wanted him to abstain from practicing from the rest of the day, then I'm sure it can't have been \"nothing\"."
            show j 1 u wry at fdis
            "Eventually, Jun backs down. He leans against a wall, crossing his arms and looking down at the floor."
            j "\"I guess you're right. It's not fair that I blame you for it...\""
            mc 1 u worried "\"What are you going to do now?\""
            j "\"What's there for me to do? I have to go home now. My parents won't be home for a couple of hours yet, so I'll just have to wait for them alone with nothing better to do.\""
            mc 1 u curious "\"What do you usually do to pass time?\""
            "He looks me in the eye."
            j "\"Piano.\""
            mc 1 u wince "\"O-oh.\""
            show j 1 u considerate at fdis
            "He leans back against the wall again, nodding with his eyes closed."
            j "\"Guess I'll just go to sleep and wait for time to pass.\""
            mc 1 u curious "\"Don't you have some games you can play?\""
            show j 1 u wry at fdis
            j "\"I've already played all the ones I have. Over and over. There isn't really much left for me to do with my gaming system. It's really old, too.\""
            mc 1 u worried "\"Hmm... Do you actually have to go home? Won't your parents be satisfied if you just leave school and avoid playing a piano?\""
            show j 1 u avoid at fdis
            j "\"No. They want me somewhere where they can keep an eye on me.\""
            mc 1 u avoid "\"Ah... that's too bad. I was hoping we could hang out.\""
            show j 1 u shock at fdis
            j "\"You want to spend the day with... {i}me{/i}?\""
            show j 1 u wince at fdis
            j "\"Wait, why aren't you at practice?\""
            "I hold back a snicker."
            mc 1 u smile "\"It took you this long to notice it? Jeez, you really need to be a little more aware of your surroundings, Jun.\""
            play sound "music/stab.ogg"
            show j 1 u wince at fdis, shake1
            j "\"Guuuh...\""
            "I chuckle. Before I even notice it, I'm petting Jun's head."
            show j 1 u shockb
            j "\"Ah.\""
            "My sudden touch catches him by surprise and he freezes."
            "Honestly, I surprise myself too. I stop moving my hand, though I don't take it off of his head."
            "This feels pleasant, somehow."
            "As if he's this cute little thing I want to protect."
            mc 1 u shock "\"Ah.\""
            "My reaction to move away is delayed by a few seconds."
            "I am left scratching my cheek, looking away in embarrassment."
            mc 1 u avoidb "\"Sorry, I didn't think.\""
            show j 1 u blush at fdis
            "I look at him with the corner of my eye (bless you peripheral vision) and see Jun with his eyes glued to the floor."
            j "\"I-It's fine. I-I don't mind.\""
            "We just stand there in silence."
            "Crap, the mood is too awkward!"
            j "\"U-Uhm... Why didn't you go to practice?\""
            mc 1 u avoidb "\"Ah... They seem to be fumigating our court today, so practice had to be canceled.\""
            j "\"I see...\""
            "I can't think of anything to say."
            "Think, damnit."
            j "\"Uhm...\""
            "I look over to Jun who is standing stiff, fiddling with his fingers."
            show j 1 u sigh at fdis
            j "\"Do you... want to come over to my house?\""
            mc 1 u curious "\"Huh?\""
            show j 1 u wry at fdis
            j "\"You said you wanted to hang out with me, right? Then why not come over to my place?\""
            mc 1 u "\"You'd be okay with that?\""
            show j 1 u happy at fdis
            "He looks down to the floor again."
            j "\"I... I'd like it if you'd come.\""
            "I can't help but feel a little embarrassed myself. Crap, what am I even being so conscious for?"
            mc 1 u happy "\"Alright then, don't mind if I do.\""
            show j 1 u smile at fdis
            j "\"Let's get going, then!\""
            "He starts walking ahead in excitement."
            "This constant mood whiplash is starting to give me neck pain."
            "Well, it doesn't really matter..."
            "At least I can keep him company right now."
            "I don't know why, but I just feel as if I shouldn't let him be alone right now."
            stop music2 fadeout 5.0
            $ day5 = "jun"
            jump Day5_Jun
        "Tag along with Kei-kun.":
            "Well, he's already here anyway. Plus, it wouldn't hurt to get to know him better."
            "Keisuke and I have been friends for a whole year and I didn't even know about his family."
            "I'm honestly afraid of how oblivious I've been."
            play sound "music/running.ogg"
            "Before he can get too far away, I run after him to catch up, giving him a tap on the shoulder."
            show k 1 u worried at fdis, five with dissolve
            k "\"What? Do you need something?\""
            mc 1 u smile "\"I was wondering if you wanted to hang out with me today. You know, since training's been canceled and all.\""
            show k 1 u uncomfortable at fdis
            k "\"Me? You want to hang out with {i}me{/i}? Why?\""
            mc 1 u "\"You're free, you're right in front of me. Why not?\""
            k "\"Why don't you go after Urata or Kobayashi? They'd be more than happy to spend time with you.\""
            mc 1 u smile "\"Shoichi is busy with SC issues and Jun is practicing for his piano competition.\""
            show k 1 u sigh at fdis
            "Kei-kun sighs, scratching his head in exasperation."
            k "\"So I'm your backup plan, huh?\""
            mc 1 u annoyed "\"No, it's not like that! Come on, you're already here and we're already together anyway. Give me one reason we shouldn't hang out.\""
            show k 1 u avoid at fdis
            mc 1 u "\"Well?\""
            show k 1 u angryb at fdis
            k "\"Shut up, I'm trying to think!\""
            mc 1 u sigh "\"You're seriously looking for a reason to say no?\""
            show k 1 u sigh at fdis
            k "\"Look, it's not that I don't want to spend time with you, it's just... I already had plans.\""
            mc 1 u shock "\"Oh... You have a date or something?\""
            show k 1 u angryb at fdis
            "He looks exasperated, quickly waving his hands around in a panic."
            k "\"Not those kinds of plans! I... fine, just don't tell anyone, okay?\""
            "I nod."
            show k 1 u avoid at fdis
            k "\"You know how I said I was going to practice something that isn't tennis? I... I'm going to practice guitar.\""
            show k 1 u serious at fdis
            "Kei-kun gives me a blank look, as if expecting some kind of response."
            mc 1 u curious "\"Okay... and why should that be a secret?\""
            show k 1 u avoid at fdis
            k "\"You don't know my family. You have no idea what kind of lecture I had to hear when I first starting learning it. \"You're the son of a prestigious family, what will the others think when they find out you've been fiddling with such a barbaric instrument?\"\""
            "Kei-kun makes a shrill mock-up voice that is, honestly, very annoying to hear."
            "I seriously hope whoever he's imitating doesn't sound like that in real life."
            mc 1 u smile "\"Why would it be embarrassing? I'm sure if people knew about it, some people might actually approach you to chat.\""
            show k 1 u sigh at fdis
            k "\"Like I said, you don't know my family. My grandmother in particular is a real piece of work. I don't get to do anything I want to do because everything and everyone is \"beneath me\".\""
            show k 1 u wince at fdis
            k "\"Plus... you've got to admit, I'm not the kind of guy you'd imagine playing guitar, right?\""
            "He strikes a guitar holding pose and starts doing an air guitar as if to prove a point."
            mc 1 u "\"Maybe. But up until yesterday, I didn't think of you as a singer either.\""
            show k 1 u avoidb at fdis
            k "\"I-I'm not a singer.\""
            "I have to admit, the idea of watching Kei-kun playing guitar is at least a little interesting."
            "I really want to see that, because, like he said, I just can't picture it in my head."
            mc 1 u smile "\"Can I come watch? If you don't mind, of course.\""
            show k 1 u shock at fdis
            k "\"Wha- I-..."
            show k 1 u sigh at fdis
            extend " Fine.\""
            mc 1 u happy "\"Does that mean I get to visit your house?\""
            k "\"Well, that's where I'm going to practice after all.\""
            show k 1 u at fdis
            k "\"My car is already waiting for me outside, so we should hurry.\""
            mc 1 u shock "\"You're having a chauffeur pick you up?\""
            show k 1 u avoid at fdis
            k "\"Yeah. My house is kinda far so we can't really walk there.\""
            mc 1 u happy "\"Ah, that's right. I sometimes forget you're filthy rich.\""
            show k 1 u angryb at fdis
            k "\"My family is rich, not me.\""
            mc 1 u seductive "\"And yet, I'm pretty sure your guitar is probably worth more than my house.\""
            k "\"Shut up!\""
            show k 1 u avoid at fdis
            k "\"..."
            show k 1 u at fdis
            extend " How much is your house worth?\""
            mc 1 u sigh "\"I said that as a joke. If you tell me your guitar actually is worth more than my house then I'll have to go shoot myself.\""
            show k 1 u avoidb at fdis
            k "\"Don't be over dramatic.\""
            "Despite saying that, the tip of his ears begins tinting red and drooping."
            "Guess I could get used to this."
            stop music2 fadeout 5.0
            $ day5 = "keisuke"
            jump Day5_Keisuke
