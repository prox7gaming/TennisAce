label day2:
    window hide
    scene April4 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene SClass with fade
    window show
    $ date = "day2"
    play music "music/crowd01.ogg" fadein 10.0
    "The classroom is excessively noisy first thing in the morning."
    "Hmm... it's already been a few minutes since the bell rang and our teacher hasn't shown up yet."
    "I wonder if something's come up..."
    play sound "music/slidingdoor.ogg"
    stop music fadeout 5.0
    show shima 1 u smile at five with moveiridis
    shima "\"Good morning, students. I'm sorry for the delay. Now if everyone could please return to their seats.\""
    "Ah, speak of the devil."
    shima "\"And before I forget, there's someone you all need to meet.\""
    "The stag looks out the still open door at someone that I can't see."
    shima "\"Come here. Introduce yourself.\""
    play music2 "music/BGM/Spring Classroom.ogg"
    if jun_met == True:
        if tour_jun == False:
            "Could it be that transfer student I met yesterday? That's awfully coincidental."
            show shima 1 u at three with move
            show j 1 u avoid at fdis, seven with moveiridis
            "A tiger walks into the room, slowly making his way to the front of the class."
            "His eyes are focusing everywhere {i}but{/i} on the other people in the room."
            show j 1 u fluster at fdis
            "Uwaah, it looks like he's totally panicking."
            j "\"I-I'm Jun Kobayashi. It's a pleasure to meet you all.\""
            "He makes a robotic bow and starts walking towards a free chair."
            shima "\"W-wait. Kobayashi, you have to write your name on the board so others can know how to spell the kanji!\""
            show j 1 u flusterb at fdis
            j "\"Ah, y-yes, just one second!\""
            "Several people laugh at his nervousness."
            "I myself think it's a bit endearing."
            "He walks back to the board, writing down his name in big, shaky letters."
            j "\"I-It's a pleasure to meet you all.\""
            "He bows once again."
            "He looks to be on the edge of a panic attack..."
            shima "\"Very well. Kobayashi, you need an empty seat. Let's see... ah, there's one next to [povLastName]. Why don't you go there?\""
            show j 1 u shockb at fdis
            j "\"Ah!\""
            "As soon as his eyes focus on me, the tiger freezes."
            shima "\"Is something the matter, Kobayashi?\""
            show j 1 u flusterb at fdis
            "He notices everyone's eyes are still on him."
            j "\"N-no, sir!\""
            play sound "music/chairscoot.ogg"
            show j 1 u watch at fdis
            "He sits down next to me, consistently shooting me curious glances the whole time."
            "Very obvious ones too."
            "Maybe I should talk to him?"
            "That would be the nice thing to do. After all, he doesn't know anyone here and I've already talked to him before."
            "And he's pleasant enough so there's no real reason not to."
            "I lean over to him, whispering."
            show j 1 u shock at fdis
            mc 1 u smile "\"I forgot to introduce myself yesterday. I'm [povName]. Nice to meet you.\""
            show j 1 u gentle at fdis
            "His face opens up into a very bright smile."
            "The boy nods enthusiastically."
            j "\"I'm Jun Kobay-{nw}"
            show j 1 u think at fdis
            extend " Wait, you already know that...\""
            show j 1 u happy at fdis
            j "\"Well, anyway, it's a pleasure to meet you!{nw}"
            show j 1 u wince at fdis
            extend " Wait, you already know that too...\""
            "Heh, he really is an amusing guy after all."
            "This just might give us a breath of fresh air for this year..."
        else:
            "That's right. Kob... Jun-kun was transferring to my class today, wasn't he?"
            show shima 1 u at three with move
            show j 1 u avoid at fdis, seven with moveiridis
            "The tiger walks into the room, slowly making his way to the front of the class."
            "His eyes are focusing everywhere {i}but{/i} on the other people in the room."
            show j 1 u fluster at fdis
            "Uwaah, it looks like he's totally panicking."
            j "\"I-I'm Jun Kobayashi. It's a pleasure to meet you all.\""
            "He makes a robotic bow and starts walking towards a free chair."
            shima "\"W-wait. Kobayashi, you have to write your name on the board so others can know how to spell the kanji!\""
            show j 1 u flusterb at fdis
            j "\"Ah, y-yes, just one second.!\""
            "Several people laugh at his nervousness."
            "I myself think it's a bit endearing."
            "He walks back to the board, writing down his name in big, shaky letters."
            j "\"I-It's a pleasure to meet you all.\""
            "He bows once again."
            "He looks to be on the edge of a panic attack..."
            shima "\"Very well. Kobayashi, you need an empty seat. Let's see... ah, there's one next to [povLastName]. Why don't you go there?\""
            show j 1 u gentle at fdis
            j "\"Ah, yes. [povFirstName]-san, hi!\""
            "He waves enthusiastically at me."
            "Waah, everyone's eyes are focused on me. Can't he be a little more careful?"
            j "\"Good morning, [povFirstName]-san!\""
            show j 1 u smile at fdis
            "And just like that, people are already whispering about it."
            hide j 1 u smile
            hide shima 1 u smile
            show ayako at five
            with dissolve
            "Ayako leans forwards, tapping me on the back to get my attention."
            ay "\"You know him, [povFirstName]-kun?\""
            mc 1 u think "\"I met him yesterday after I met with Katsuragi-sensei. I gave him a tour of the school.\""
            ay "\"Oh my, that's pretty nice of you. I would have done it if I knew he was still around.\""
            show ayako at three with move
            show kyoko at seven with moveiridis
            ky "\"Ayako, what's he saying?\""
            hide ayako
            hide kyoko
            with dissolve
            "And just like that, a \"telephone line\" has already been formed to discuss how I came to meet Jun-kun."
            play sound "music/disappointment.ogg"
            "Wait a second, why am I the one getting all the attention here? {i}He's{/i} the transfer student."
            show j 1 u watch at fdis, five with dissolve
            j "\"You're really popular, aren't you?\""
            mc 1 u think "\"Not really. They're just incredibly curious people.\""
            show j 1 u smile at fdis
            j "\"I wish I had that many friends.\""
            mc 1 u think "\"I wouldn't really call them friends. More like friendly acquaintances.\""
            show j 1 u watch at fdis
            j "\"Isn't that the same thing?\""
            "I shrug."
    else:
        "His words suddenly catch my attention, making my ears stand upright."
        "A new student? In our class?"
        "Seeing senior transfer students isn't all that common."
        "I wonder what reason that guy had to transfer."
        "And why did he only show up on the {i}second{/i} day of class?"
        show shima 1 u at three with move
        show j 1 u avoid at fdis, seven with moveiridis
        "A tiger walks into the room, slowly making his way to the front of the class."
        "His eyes are focusing everywhere {i}but{/i} on the other people in the room."
        show j 1 u fluster at fdis
        "Uwaah, it looks like he's totally panicking."
        j "\"I-I'm Jun Kobayashi. It's a pleasure to meet you all.\""
        "He makes a robotic bow and starts walking towards a free chair."
        shima "\"W-wait. Kobayashi, you have to write your name on the board so others can know how to spell the kanji!\""
        show j 1 u flusterb at fdis
        j "\"Ah, y-yes, just one second.!\""
        "Several people laugh at his nervousness."
        "I myself think it's a bit endearing."
        "He walks back to the board, writing down his name in big, shaky letters."
        j "\"I-It's a pleasure to meet you all.\""
        "He bows once again."
        "He looks to be on the edge of a panic attack..."
        shima "\"Very well. Kobayashi, you need an empty seat. Let's see... ah, there's one next to [povLastName]. Why don't you go there?\""
        show j 1 u fluster at fdis
        j "\"H-Hello. It seems I'll be sitting next to you this year.\""
        "He attempts to flash me a smile... or at least I {i}think{/i} it's a smile. It's hard to tell."
        "He looks so completely stiff, almost like a machine."
        "I'll try to at least put him at ease."
        show j 1 u shock at fdis
        "I offer him my hand."
        mc 1 u smile "\"My name is [povFirstName]. [povName]. It's a pleasure.\""
        show j 1 u happy at fdis
        "The look on his face this time is much more genuine."
        "He grabs my hand and shakes it enthusiastically."
        j "\"It's a pleasure on my part as well. I'm Ju...{nw}"
        show j 1 u think at fdis
        extend " no, wait, you already know that.\""
        "He's an interesting guy, I'll give him that at least."
    stop music2 fadeout 4.0
    if jun_met == True:
        if tour_jun == True:
            scene SClass with fade
            play sound "music/schoolbell.ogg"
            play music "music/crowd01.ogg"
            "Augh... I expected to be bored by the classes, but dear God, did they have to be {i}that{/i} boring?"
            "Most of the students are already getting packed and heading home."
            "Club activities haven't started yet, so most of the students have nothing to do after class."
            "Only competitive clubs like mine or Shoichi's have been given permission to start early."
            "... I think I'm going to laze around on top of my desk for a while longer."
            "Some others students seem to be doing the same and are sticking around in class to talk to their friends."
            "Must be nice... my friends are all super enthusiastic about their respective clubs so I'm sure they must all be headed there already."
            play music2 "music/BGM/Autumn Day.ogg" fadein 5.0
            show j 1 u watch at fdis, five with moveiridis
            "I hear the sound of someone clearing their throat and, when I look up from my desk, I see a tiger standing there, looking down at me."
            j "\"Excuse me, [povFirstName]-san... Would you mind showing me to the Staff Room? I don't know how to get there.\""
            mc 1 u "\"Why me? Shouldn't you ask one of our teachers?\""
            show j 1 u blush at fdis
            j "\"W-Well... the thing is... he already left...\""
            "I look at the teacher's desk and confirm that his words are actually true."
            "Isn't the teacher supposed to stick around for a few minutes in case their students have any questions?"
            play sound "music/disappointment.ogg"
            "What's up with this school and all their lazy teachers?"
            j "\"Y-You're the only person in here that I know so I... uhm... I kinda figured it'd be better if I asked you first.\""
            mc 1 u fsmile "\"W-well, I would but... I-I have the tennis club to get to. Remember how I told you I was on the tennis club?\""
            "Yes, the perfect excuse!"
            show j 1 u watch at fdis
            j "\"Then how come you've been sitting around for the past five minutes without going anywhere?\""
            play sound "music/stab.ogg"
            "Guh..." with hpunch
            "He's got me there..."
            mc 1 u fsmile "\"Well, either way, I really should get going to the tennis club.\""
            show j 1 u bright at fdis
            j "\"Oh, I know! How about you take me to your practice session so I can watch? You promised me you would yesterday!\""
            mc 1 u sigh "\"... Don't you have to go to the Staff Room?\""
            show j 1 u happy at fdis
            j "\"I only needed to get my class itinerary. I can do that whenever!\""
            "Boy, you really need to get your priorities straight..."
            "Well... I guess Saya wouldn't mind. She likes to show the club off to any interested spectators."
            "And Coach is a weirdo so I doubt he'd mind... if he's even present at all."
            "... Have I agreed to this already?"
            mc 1 u think "\"I... guess I can. Though I can't promise I'll be allowed to bring you in. We can still try.\""
            "It's not like our practices are secret after all."
            show j 1 u happy at fidget
            "Kobayashi looks incredibly pleased at the news. I swear he's radiating satisfaction."
            "Heh, what a weird kid."
            stop music2 fadeout 5.0
        else:
            scene SClass with fade
            play sound "music/schoolbell.ogg"
            play music "music/crowd01.ogg"
            "Augh... I expected to be bored by the classes, but dear God, did they have to be {i}that{/i} boring?"
            "Most of the students are already getting packed and heading home."
            "Club activities haven't started yet, so most of the students have nothing to do after class."
            "Only competitive clubs like mine or Shoichi's have been given permission to start early."
            "... I think I'm going to laze around on top of my desk for a while longer."
            "Some others students seem to be doing the same and are sticking around in class to talk to their friends."
            "Must be nice... my friends are all super enthusiastic about their respective clubs so I'm sure they must all be headed there already."
            play music2 "music/BGM/Autumn Day.ogg" fadein 5.0
            show j 1 u watch at fdis, five with moveiridis
            "I hear the sound of someone clearing their throat and, when I look up from my desk, I see a tiger standing there, looking down at me."
            j "\"Excuse me, [povFirstName]-san... Would you mind showing me to the Staff Room? I don't know how to get there.\""
            mc 1 u "\"Why me? Shouldn't you ask one of our teachers?\""
            show j 1 u blush at fdis
            j "\"W-Well... the thing is... he already left...\""
            "I look at the teacher's desk and confirm that his words are actually true."
            "Isn't the teacher supposed to stick around for a few minutes in case their students have any questions?"
            play sound "music/disappointment.ogg"
            "What's up with this school and all their lazy teachers?"
            j "\"Y-You're the only person in here that I know so I... uhm... I kinda figured it'd be better if I asked you first.\""
            mc 1 u fsmile "\"W-well, I would but... I-I have the tennis club to get to. Remember how I told you I was on the tennis club?\""
            "Yes, the perfect excuse!"
            show j 1 u watch at fdis
            j "\"Then how come you've been sitting around for the past five minutes without going anywhere?\""
            play sound "music/stab.ogg"
            "Guh..." with hpunch
            "He's got me there..."
            j "\"That's true though, you are in the tennis club..."
            show j 1 u bright at fdis
            extend " Oh, I know! How about you take me to your practice session so I can watch? You promised me you would yesterday!\""
            mc 1 u sigh "\"... Don't you have to go to the Staff Room?\""
            show j 1 u happy at fdis
            j "\"I only needed to get my class itinerary. I can do that whenever!\""
            "Boy, you really need to get your priorities straight..."
            "Well... I guess Saya wouldn't mind. She likes to show the club off to any interested spectators."
            "And Coach is a weirdo so I doubt he'd mind... if he's even present at all."
            "And I did promise him after all."
            mc 1 u think"\"Well, sure. I guess I can. I can't make any promises that it'll be exciting but I don't see why I couldn't.\""
            "It's not like our practices are secret after all."
            show j 1 u happy at fidget
            "Kobayashi looks incredibly pleased at the news. I swear he's radiating satisfaction."
            "Heh, what a weird kid."
            stop music2 fadeout 5.0
    else:
        scene SClass with fade
        play sound "music/schoolbell.ogg"
        play music "music/crowd01.ogg"
        "Augh... I expected to be bored by the classes, but dear God, did they have to be {i}that{/i} boring?"
        "Most of the students are already getting packed and heading home."
        "Club activities haven't started yet, so most of the students have nothing to do after class."
        "Only competitive clubs like mine or Shoichi's have been given permission to start early."
        "... I think I'm going to laze around on top of my desk for a while longer."
        "Some others students seem to be doing the same and are sticking around in class to talk to their friends."
        "Must be nice... my friends are all super enthusiastic about their respective clubs so I'm sure they must all be headed there already."
        play music2 "music/BGM/Autumn Day.ogg" fadein 5.0
        show j 1 u watch at fdis, five with moveiridis
        "I hear the sound of someone clearing their throat and, when I look up from my desk, I see a tiger standing there, looking down at me."
        j "\"Excuse me, Senpai... Would you mind showing me to the Staff Room? I don't know how to get there.\""
        mc 1 u "\"Why me? Shouldn't you ask one of our teachers?\""
        show j 1 u blush at fdis
        j "\"W-Well... the thing is... he already left...\""
        "I look at the teacher's desk and confirm that his words are actually true."
        "Isn't the teacher supposed to stick around for a few minutes in case their students have any questions?"
        play sound "music/disappointment.ogg"
        "What's up with this school and all their lazy teachers?"
        show j 1 u wince at fdis
        j "\"I-I know we don't really know each other, but since you sit right next to me and you don't look like you're doing anything right now I... I thought I'd ask.\""
        mc 1 u fsmile "\"W-well, I would but... I actually am part of a club. I'm just... err... killing time before I get to it.\""
        j "\"O-oh, I'm sorry. I didn't know.\""
        mc 1 u nervous "\"It's fine. There's no way you could have known anyway. Most clubs haven't begun operating yet. Only the sports clubs were given a pass.\""
        show j 1 u watch at fdis
        j "\"You play a sport?\""
        mc 1 u smile "\"Yeah. I'm in the tennis club.\""
        show j 1 u bright at fdis
        "Immediately upon hearing this, his eyes begin to sparkle as he flashes me a blinding smile."
        j "\"You play tennis? That's amazing. I think tennis is a totally awesome sport! {size=-4}Though I've never really watch it.{/size}\""
        show j 1 u smile at fdis
        j "\"If it's not asking too much, could I come watch?\""
        "T-that's fast. He switched gears way too fast!"
        mc 1 u nervous "\"D-didn't you need to go to the Staff room?\""
        show j 1 u happy at fdis
        j "\"I only needed to get my class itinerary. I can do that whenever!\""
        "... This kid seriously needs to get his priorities in check."
        show j 1 u watch at fdis
        "Can I even take him there? I suppose I could show him a few places on the way..."
        "... I've already unconsciously agreed to do this haven't I?"
        mc 1 u "\"Alright. I can't promise you'll be allowed in but I suppose we can try.\""
        mc 1 u smile "\"I guess I could point out a few places on the way to help you get situated.\""
        show j 1 u gentle at fdis
        j "\"Yay!\""
        "Heh, I guess this isn't so bad."
        stop music2 fadeout 5.0

    play music3 "music/BGM/On My Way.ogg" fadein 5.0
    scene SLockers with fade
    if jun_met == False:
        "Once we arrive, I have Kobayashi wait outside the building while I get dressed."
        "I need to get Saya's permission before I can allow him to come inside."
    else:
        if tour_jun == False:
            "Once we arrive, I have Kobayashi-kun wait outside the building while I get dressed."
            "I need to get Saya's permission before I can allow him to come inside."
        else:
            "Once we arrive, I have Jun-kun wait outside the building while I get dressed."
            "I need to get Saya's permission before I can allow him to come inside."
    scene SCourt
    play music "music/tennisambiance.ogg" fadein 5.0
    show sa 1 t talk at fdis, five
    with fade
    sa "\"A visitor? That's kinda rare for {i}you{/i} to be asking me this?\""
    mc 1 t "\"Is that a no?\""
    show sa 1 t smile at fdis
    sa "\"Of course not. I'm fine with it if you want to bring someone to watch. Having someone watch you with interest is always a great way to get yourself pumped up!\""
    "That's exactly the kind of answer I'd expect coming from her."
    mc 1 t smile "\"I'm sure he's not going to be lacking on the interest front, at least.\""
    "She nods, smiling."
    show sa 1 t talk at fdis
    sa "\"So, tell me. What's your real reason from bringing him along? You wouldn't just invite your other classmates.\""
    mc 1 t avoid "\"You saw through me, huh? To be honest, I felt a bit bad for him since he doesn't know anyone else in the school.\""
    mc 1 t smile "\"So I just thought. \"Ah, why not?\" and brought him along.\""
    show sa 1 t laugh at fdis
    sa "\"That's pretty kind of you, [povFirstName].\""
    show sa 1 t think at fdis
    sa "\"Hmm... but we don't have any practice matches scheduled for today. Don't you think he'd be bored of watching us practice our shots?\""
    show sa 1 t shock at fdis, three with move
    show m 1 u smile at seven with moveiridis
    m "\"That shouldn't be a problem, Saya-tan.\""
    "Suddenly, a huge mountain of scales towers behind Saya."
    sa "\"WAAH?! C-Coach!?"
    show sa 1 t pout at fdis
    extend " Don't just sneak behind me.\""
    m "\"Ahahaha. Sorry sorry. I couldn't keep myself from overhearing what you guys were talking about!\""
    "I'm going to call bullshit on that."
    m "\"There's been a change of plans. We're going to have a few matches today!\""
    show sa 1 t shock at fdis
    sa "\"Wait, wait. What about our training menu for the day?\""
    m "\"Don't worry so much about that.\""
    show sa 1 t doom at fdis
    "Saya glares at him, a look that on more than one occassion left me visualizing the very image of death itself."
    "And it has no effect on the crocodile."
    sa "\"You left me alone for a whole month without even helping me make a balanced training regime and now you're going to mess it up?\""
    m "\"If you keep fretting over everything when you're this young, you're going to get wrinkly before you're thirty. Bahahaha!\""
    show sa 1 t annoyed at fdis, shake1
    sa "\"Grrrrr...\""
    "I'm half expecting her to jump on his throat any second now."
    "Meanwhile, he merely laughs it off as if it were a big joke."
    play sound "music/disappointment.ogg"
    "You're almost hitting forty. Could you please start acting your own age..."
    mc 1 t serious "\"Who do you propose we play against? I'm okay with anyone other than Kei-kun.\""
    m "\"Keisuke would cry if he heard you saying that...\""
    "Yeah, I've been getting that a lot lately."
    show sa 1 t at fdis
    m "\"Well, not to worry. I've already made arrangements to get us some new players to practice with.\""
    mc 1 t curious "\"Did you invite players from another club?\""
    "Coach scratches his chin with a cheeky smile on his face."
    m "\"Well, let's go with that. Wait here while I go call them over.\""
    show m 1 u smile at offscreenright
    show sa 1 t shock at fdis, five
    with move
    sa "\"Ah, could it be...\""
    mc 1 t curious "\"Hmm? You know what's going on here, Saya-chan?\""
    show sa 1 t think at fdis
    sa "\"I remember him telling me that he was coming over to visit today but I didn't think that meant...\""
    "Who's {i}he{/i}?"
    mc 1 t sigh "\"Can't you just drop the pronoun game and tell me who you're talking about?\""
    show kaito at offscreenright
    mo "\"Why don't you take a guess?\""
    "The sound of a familiar voice immediately catches my attention."
    play sound "music/tap.ogg"
    show sa 1 t shock at fdis, one with move
    show kaito at five
    show kenma at nine
    with moveiridis
    "Before I can even react, I feel a tap on my back and two figures come into view."
    sa "\"Kaito-kun!\""
    show sa 1 t laugh at fdis
    "Saya rushes over to the tiger, locking him in a tight hug."
    mc 1 t shock "\"Morisaki-senpai?\""
    "The tiger's grin widens."
    mo "\"Hey there, Saya-chan. [povFirstName]-kun, I see you've grown taller!\""
    "This goofy looking tiger was our club's captain back when I was a freshman."
    "We were all surprised when he decided to go to a college in America at the same time as he debuted as a pro."
    "From what I researched, the college he went to has a big sports program that scouts players from all over the world."
    "They definitely are one of the best environments a tennis player could hope for."
    "During his time as an active player in the junior ranks, Morisaki-senpai was ranked #3 in the country."
    "The lynx right next to him though... I don't know him."
    mo "\"Oh, and by the way, this guy here is a friend of mine from college! He's from a bit before my time but he's an excellent player! Hehehe.\""
    "The lynx smiles and offers me his hand."
    ke "\"Kenma Sasaki. Pleasure to meet you.\""
    mc 1 t nervous "\"Y-yeah. It's a pleasure to meet you too.\""
    "This guy is really intimidating!"
    show sa 1 t at fdis
    m "\"Oe, Morisaki!\""
    show sa 1 t at fdis, one
    show kaito at four
    show kenma at seven
    show m 1 u smile at ten
    with move
    "The crocodile walks back to the courts grinding his teeth."
    m "\"Jeez, don't wander around without permission. I went to the van to pick you guys up and there wasn't anyone there.\""
    "Morisaki-senpai scratched the back of his head, laughing nervously."
    mo "\"Ah, sorry sorry. The girls said that it was too hot inside and left, so Kenma and I decided to leave too.\""
    ke "\"I told you we should have stayed put. Idiot.\""
    mo "\"H-hey, Kenma, back me up a little here!\""
    "Coach sighs."
    m "\"Jeez, you always were a troublemaker.\""
    mo "\"Hehehe, thank you, Amanuma-san.\""
    m "\"That wasn't a compliment!\""
    "Oh, yeah, I remember this little dynamic fairly well."
    "Morisaki-senpai's carefree attitude would always cause Coach a ton of problems..."
    mo "\"But come on, it's just so nostalgic being back here. How could you expect me to not have a look around?!\""
    m "\"Alright, fine. I'll let this one slide. But you ruined my dramatic entrance...\""
    m "\"And by the way, where did the girls go?\""
    mo "\"Oh, that's right!\""
    "The tiger immediately lifts a finger up in the air as if he just had a grand epiphany."
    mo "\"I have no idea! Hahaha!\""
    play sound "music/punch.ogg"
    "Coach conks him on the head."
    m "\"Then what was that dramatic pause for?!\""
    ke "\"Say so from the beginning. Idiot.\""
    mo "\"{cps=+30}Why are you two ganging up on me?! And Kenma, you knew from the very beginning too!{/cps}\""
    "Waah... they're more of a wacky trio than Shoichi, Kei-kun and I..."
    "Although I guess this is the kind of thing I'd expect from Morisaki-senpai..."
    "Coach sighs again, taking in a deep breath of air to recompose himself."
    m "\"Ahem... where was I? Oh, right.\""
    m "\"I've decided to reach out to some of our more successful alumni. Our school has always had a pretty strong tennis program after all so many of our former students became pros.\""
    m "\"Since they are all pretty new to the professional scene, I figured they could spare us some of their time. Aren't I brilliant? Bahaha.\""
    ke "\"Actually, we were coming to Saitama anyway for the Tozansha Challenger tournament. We merely rescheduled our stay to come five days in advance due to the promise of free lodging and food.\""
    play sound "music/disappointment.ogg"
    "In other words, they took pity on us?"
    m "\"What do you think, huh? Pretty neat, isn't it. Isn't it?!\""
    mc 1 t smile "\"Well, I do have to admit that I didn't expect this. And all this time I thought you were just lazing around at home.\""
    "Coach's shoulders sag."
    m "\"You could try having some more faith in me, you know.\""
    mc 1 t avoid "\"When can we start the matches?\""
    m "\"Don't just ignore m- Ah, forget it.\""
    "He clears his throat one more time, crossing his arms to appear more serious than he really is."
    m "\"The matches can start once everyone is ready. I've also arranged for two female players to come over to practice with you and Kushina, Saya-tan.\""
    m "\"You guys will be playing consecutive one-set matches.\""
    m "\"You better be prepared, because we'll be practicing all the way through the schools closing times. You'll probably be playing twenty sets a day.\""
    mc 1 t shock "\"Twenty sets? That's impossible. With the average duration of a set, there's no way we could cram that much in just a few hours.\""
    "Coach smiles. His toothy grin sends shivers down my spine."
    m "\"Oh, don't worry. Your sets won't last long at all.\""
    mc 1 t nervous "\"W-what's that supposed to m-\""
    play sound "music/slap.ogg"
    "Morisaki-senpai gives me a slap on the back, nearly knocking me down face first into the ground."
    mo "\"Come on, [povFirstName]-kun. It will be fun!\""
    mc 1 t sigh2 "\"C-can't breathe...\""
    "Oh God, I'm going to cough my lungs out."
    scene SCourt with fade
    stop music3 fadeout 5.0
    "It takes us a few minutes to track the female players down but eventually all the preparations are made."
    "I took the opportunity to go outside and give Kobayashi the all-clear to come in."
    "Although some curious onlookers tried to stop their own practice to watch, Coach made sure to get them all back on track."
    "Even then, people keep shooting glances at us every now and then."
    show kaito at five with dissolve
    mo "\"[povFirstName]-kun, why don't you serve first? Show me how much you've matured the past two years!\""
    mc 1 t fsmile "\"Y-yes, captain!\""
    "In the end, Morisaki-senpai insisted on having me be his first opponent."
    "On another court, Kei-kun is about ready to start his match against the lynx, Sasaki-san."
    show diagram with dissolve
    "I take a couple deep breaths, mentally preparing myself for this."
    "I have to admit. I'm excited at the idea of playing against Morisaki-senpai again after so many years."
    "I can't wait to see how much he's changed since going pro!"
    play music2 "music/BGM/Synapse.ogg"
    show mm1p1i1 with dissolve
    "Once the ball is in play, focus only on it and on my opponent..."
    play sound "music/tennishit.ogg"
    show mm1p1i2 with dissolve
    "I toss the ball high in the air and bring down my racket to meet it, putting as much power into it as I can."
    "The feeling of the ball leaving the racket was great. This might just be one of my best serves in a while."
    "While I fully expected to get an ace of of it, Morisaki-senpai quickly reaches the ball before it can leave the court."
    play sound "music/tennishit.ogg"
    show mm1p1i3 with dissolve
    "He doesn't waste time being timid and immediately goes on the offensive, sending a powerful return to attack my serve."
    "The ball bounces right on the backline, forcing me to move back a few steps."
    play sound "music/tennishit.ogg"
    show mm1p1i4 with dissolve
    "The resulting motion leaves my posture out of whack, making my shot slow."
    "Before I notice it, Morisaki-senpai dashes towards the net... no, that's not quite right."
    "He was already on the net even before I hit the ball back."
    "How did he get there so fast?"
    play sound "music/tennishit.ogg"
    show mm1p1i5 with dissolve
    "He volleys the ball with force."
    show mm1p1i6 with dissolve
    "I'm not even halfway through the court when the ball hits the ground and rolls away."
    mo "\"15-0.\""
    hide mm1p1i6
    hide mm1p1i5
    hide mm1p1i4
    hide mm1p1i3
    hide mm1p1i2
    hide mm1p1i1
    with dissolve
    mo "\"Hoo, that was a pretty WILD serve!\""
    play sound "music/disappointment.ogg"
    "Did you really have to say the \"wild\" part in English..."
    "..."
    "Even though I hit the ball with everything I had, he easily returned it to the worst possible spot..."
    "Not only that, he reached the net before I even noticed he had moved."
    "His movement is completely different from three years ago..."
    "And the quality of his shots has improved a considerable amount."
    "This might just have been luck, but..."
    mo "\"Yo, [povFirstName], you there?\""
    mc 1 t shock "\"Ah, yes, sorry!\""
    "Crap, I was spacing out and didn't hear him call me."
    show mm1p2i1 with dissolve
    "Play resumes on my court."
    play sound "music/tennishit.ogg"
    show mm1p2i2 with dissolve
    "This time I go for a slice that quickly escapes to the sides of the court."
    play sound "music/tennishit.ogg"
    show mm1p2i3 with dissolve
    "As if anticipating it, Morisaki-senpai does a quick sideways jump and meets the ball right in the center of his racket."
    "His return paints the line on the opposite side of the court."
    "How am I supposed to use my serve advantage when he's already countering my serve?"
    play sound "music/tennishit.ogg"
    show mm1p2i4 with dissolve
    "I make a mad dash for the ball, barely managing to tap it."
    "When did his shots become so heavy?"
    "I'm having a hard time just getting the ball to go over the net."
    "If it keeps going like this, I'm bound to end up making a mistake."
    "Wait, he's already at the net again?! When did he-"
    play sound "music/tennishit.ogg"
    show mm1p2i5 with dissolve
    "Senpai taps the ball back lightly. A drop volley."
    play sound "music/tennishit.ogg"
    show mm1p2i6 with dissolve
    "In the end, I never had a chance to reach the ball before it bounced twice."
    hide mm1p2i6
    hide mm1p2i5
    hide mm1p2i4
    hide mm1p2i3
    hide mm1p2i2
    hide mm1p2i1
    with dissolve
    mo "\"30-0.\""
    "I can't accept it."
    "I can't do anything against him on my serve game? That's ridiculous."
    show mm1p3i2 with dissolve
    play sound "music/tennishit.ogg"
    show mm1p3i2 with dissolve
    "I try putting as much topspin as I can on my next serve."
    "As soon as the ball rises, it should spin out of control, making it shoot up higher than normal."
    "If he can't adapt his swing, he'll miss the perfect point of impact."
    "And even if he sees it coming, he'll have to move further back, giving me an opportunity to attack."
    "At least that's what should happen."
    play sound "music/tennishit.ogg"
    show mm1p3i3 with dissolve
    "As if he realizes what I'm doing, Senpai immediately dashes to the point where the ball bounces on the court, hitting it right as it rises from the ground, before it has the chance to properly bounce."
    "A rising shot is such a difficult shot to make."
    "Even Kei-kun, the most skillful player on the club, can't hit those properly."
    "Yet, this guy... Senpai hits it easily, sending the ball back to me."
    "Still, this wasn't a perfect return by any means. This ball lacks power when compared to his regular groundstrokes."
    "The ball hits the ground a little short of the baseline."
    "I can reach it!"
    play sound "music/tennishit.ogg"
    show mm1p3i4 with dissolve
    "I try hitting a straight shot with as much power as I can."
    "What I lack in control I can make up with pure firepower."
    "Even if I can't put it in a difficult position, as long as I can stop him from coming to the net, I have a chance."
    "Senpai has always been weak in his baseline game, even more so than the regular Serve and Volley player."
    "As long as I can keep him anchored to the baseline, I should have a chance."
    "Senpai reaches my ball easily and has ample time to prepare."
    play sound "music/tennishit.ogg"
    show mm1p3i5 with dissolve
    "He hits it with a full swing, sending it to the other side of the court."
    "The ball is going unbelievably fast. I can barely keep up with it."
    "Somehow, I manage to reach it."
    "The very tip of my racket makes contact..."
    "And the racket is blown out of my grip."
    play sound "music/racketdrop.ogg"
    show mm1p3i6 with dissolve
    mc 1 t shock "\"Wah?!\""
    "So much power!"
    hide mm1p3i6
    hide mm1p3i5
    hide mm1p3i4
    hide mm1p3i3
    hide mm1p3i2
    hide mm1p3i1
    with dissolve
    "Senpai has always had a decent bit of upper body strength, but nothing like this."
    "This is seriously bad. I can't even think of ways to deal with it."
    "Volley, power, speed, control, technique."
    "He far outclasses me in every single one of those."
    "And I haven't even seen him in his serve game..."
    "I can't accept being beaten like this!"
    mo "\"Hey, [povLastName]-kun, are you ready yet? It's time to resume play.\""
    "Crap! I'm spacing out again..."
    "Keep it together. Feeling defeated right at the beginning of the game doesn't help."
    "Just take deep breaths. That's it, calm down..."
    "He's gotten me so worked up this quickly..."
    show mm1p4i1 with dissolve
    "I prepare another serve."
    "Slice, topspin, flat. He's received every single one of my best serves without any trouble."
    "Since there isn't anything that stands out as the best option, I'll just go with my personal best."
    play sound "music/tennishit.ogg"
    show mm1p4i2 with dissolve
    "FLAT!!"
    "I hit the ball with everything I have."
    "This is without a doubt the fastest serve I can pull off."
    "The ball must be going at at least 190km/h."
    "There's no way he can reach it easily."
    play sound "music/tennishit.ogg"
    show mm1p4i3 with dissolve
    "Senpai manages to send the ball back."
    "But I can tell from his stance that that shot can't possibly have as much power as the last one. He didn't have time to make a good swing."
    "Against this weakened shot that is going towards my forehand, I immediately prepare to counter it."
    play sound "music/tennishit.ogg"
    show mm1p4i4 with dissolve
    "I concentrate every ounce of my strength on sending the ball right on top of the line, on the side of the court opposite to where Senpai is right now."
    "By all means, this should be the best option."
    "He shouldn't reach."
    "And yet, the little voice in the back of my head tells me to prepare."
    "Not only is he going to reach it, but he's going to send a strong ball right back at me."
    "Left or right?!"
    "Whatever, it doesn't matter."
    mc 1 t angry "\"Bring it!\"" with hpunch
    "I catch myself screaming from the top of my lungs."
    "Before I even realized it, I got this worked up."
    "I don't care if I look lame, I just don't want to lose."
    "No matter what happens, I absolutely don't want to lose!"
    play sound "music/tennishit.ogg"
    show mm1p4i5 with dissolve
    "Somehow, he managed to reach my best shot with absolute ease."
    "If it's going to be like this, then I have to make sure he can't go towards the net."
    "If he reaches the net, it's game over. That's what my instincts are telling me right now."
    "I have to exert myself to reach the ball."
    play sound "music/tennishit.ogg"
    show mm1p4i6 with dissolve
    "I jump towards it, nearly losing my footing as I do so, but I manage to hit the ball back with some semblance of power."
    "As long as I make it strong enough, he shouldn't have an opportunity to dash towards the net."
    "Senpai reaches it."
    "I immediately start running towards the center of the court, so as to reach the ball regardless of his shooting it left or right."
    play sound "music/tennishit.ogg"
    show mm1p4i7 with dissolve
    "!?"
    "He tapped it!"
    "Crap, a drop shot!"
    "A perfect shot to take advantage of my momentary loss of focus, his stance didn't give away what he was going to do until the ball left the racket."
    "For a fraction of a second, I'm rooted to this spot."
    "Damn it, legs, MOVE!"
    "I direct all of my energy to my legs and make a mad run for it."
    "I jump towards the ball, hitting the ground with my chest."
    "Shit, this hurts like hell."
    play sound "music/tennishit.ogg"
    show mm1p4i8 with dissolve
    "Still, I manage to miraculously tap the ball right before it hits the ground."
    "The ball goes up just enough to go over the net..."
    "I relax for only just a second."
    "Then, a towering orange figure eclipses my vision."
    "He knew all along I'd reach it, and so he made his way to the net."
    play sound "music/tennishit.ogg"
    show mm1p4i9
    show mm1p4i10
    with dissolve
    "I'm left defenseless as he hits the ball right over my head to take the point."
    mo "\"There you go. Game won by me, 1-0!\""
    hide mm1p4i10
    hide mm1p4i9
    hide mm1p4i8
    hide mm1p4i7
    hide mm1p4i6
    hide mm1p4i5
    hide mm1p4i4
    hide mm1p4i3
    hide mm1p4i2
    hide mm1p4i1
    hide diagram
    with dissolve
    "He flashes me a goofy smile."
    "I feel anger surging inside, most of it is directed at me."
    "It takes every ounce of self-restraint I have not to lash out."
    "Somehow, I am dimly aware that I am baring my fangs."
    "Senpai's notices the look on my face. Of course he does, how wouldn't he?"
    "He shifts around in his spot and glares back at me with such intensity that I feel like I'm being shot dead."
    "He has a very smug smile on his face, as if he's enjoying seeing me like this."
    "It's enough to make me freeze on the spot."
    mo "\"Oh, I like the look on your face, [povFirstName]-kun!\""
    mo "\"Okay, then. I'll play seriously now. Let's see if you can entertain me for a little bit.\""
    stop music2 fadeout 5.0
    scene SCourt
    show kaito at five
    with fade
    "I'm completely dominated during his serve games."
    "I can't even properly return the balls at first and he scores many aces off of it."
    "Near the end of the match I realize that I didn't even get a single point during the whole thing."
    mo "\"Yay, 6-0. I win!\""
    mo "\"Better luck next time, [povLastName]-kun. Bahahahaha.\""
    show kaito at offscreenright with moveoridis
    "Senpai walks away, laughing."
    "I clench my fists in frustration, my claws threaten to puncture the palms of my hands."
    "It didn't take him ten minutes to completely dispose of me as if I were garbage."
    "This is so frustrating!"
    play sound "music/tap.ogg"
    show k 1 t annoyed at fdis, five with moveiledis
    k "\"[povLastName]-san.\""
    "Keisuke taps me on the shoulder."
    show k 1 t avoid at fdis
    k "\"Looks like you didn't fare any better than I did.\""
    mc 1 t "\"Yeah... did you even manage to score a single point?\""
    show k 1 t sigh at fdis
    k "\"No. Not once.\""
    mc 1 t wince "\"Ha... it's so frustrating.\""
    "Kei-kun nods."
    show k 1 t nervous at fdis
    k "\"I wonder what their rank is in the World League.\""
    k "\"If I find out that they're in the seven hundreds or something like that, I'll lose it.\""
    mc 1 t fsmile "\"Heh, I know what you mean. But don't worry. Last I checked, Morisaki-senpai was #421.\""
    show k 1 t sigh at fdis
    k "\"Well, that makes me feel a little better, at least.\""
    show k 1 t smile at fdis
    k "\"Let's try to win at least one set by the end of the game.\""
    mc 1 t smile "\"Right!\""
    play sound "music/clap.ogg"
    "Kei-kun lifts his hand up high and we share a high five."
    show k 1 t smile at fdis, offscreenleft with moveoledis
    hide k 1 t smile
    "Alright, I'm feeling pumped again!"
    "?!"
    show j 1 u wince at fdis, one, fidget with dissolve
    if jun_met == False:
        "Kobayashi is fidgeting uncomfortably at a nearby corner."
    else:
        if tour_jun == False:
            "Kobayashi-kun is fidgeting uncomfortably at a nearby corner."
        else:
            "Jun-kun is fidgeting uncomfortably at a nearby corner."
    "That's true, he's been watching me this whole time."
    "Did I... did I scare him?"
    "Ugh, I really need to get a grip..."
    "It won't do me any good if I'm so angry that I can't think straight."
    show kenma at offscreenright
    play sound "music/tap.ogg"
    ke "\"So, are you ready?\""
    show j 1 u wince at offscreenleft
    show kenma at five
    with move
    "I turn around to see Sasaki-san standing behind me, holding his racket in hand."
    "His clothes barely have any sweat on them. It's as if the set just now barely even winded him."
    "Which, considering how short it was, it probably didn't."
    play sound "music/disappointment.ogg"
    "We didn't even need to take breaks during the whole thing..."
    "The lynx smiles. And by that I mean that the corners of his mouth {i}barely{/i} curve a little bit upwards."
    ke "\"I saw a bit of your match. You're an interesting player.\""
    ke "\"I didn't think a high schooler was capable of making Morisaki play seriously. This might be a decent learning experience.\""
    "With no other words, he began walking towards one of the empty courts."
    "Took me a few seconds to react and follow behind him."
    "Once we both took our positions, Sasaki-san grabbed a couple balls and waved at me."
    ke "\"I'll take service if you don't mind.\""
    ke "\"Since you already started with the serve last match, I'm sure you'll be okay with it, right?\""
    "... This guy is a little pushy, isn't he?"
    "But I guess I'll let this one pass. After the last match, I think I prefer having him take the first serve."
    "I'm afraid of thinking about the psychological damage that getting broken on the first game would cause..."
    "It might be better to serve second so as to lower my expectations on the match."
    "Or maybe I'm being too timid?"
    "No, this is fine. I should take the chance to see how he plays."
    show diagram
    show kem1p1i1
    with dissolve
    "Kenma-san picks up a ball in his pocket and starts bouncing it on the court."
    "After a few bounces, he gripped the ball tightly in his hand and focused on me."
    play music2 "music/BGM/Auto Pilot.ogg" fadein 5.0
    "Something about the way he looked at me made me uncomfortable."
    "It was like he was analyzing me, just looking for a weakness."
    "He makes me feel uneasy."
    play sound "music/tennishit.ogg"
    show kem1p1i2 with dissolve
    "He tossed the ball high into the air and slammed his racket against it."
    "I-It's fast. Really fast!"
    "Not on the same level as Morisaki-senpai but... it might just be faster than mine."
    play sound "music/tennishit.ogg"
    show kem1p1i3 with dissolve
    "I reached the ball with a little difficulty and hit it back at him."
    play sound "music/tennishit.ogg"
    show kem1p1i4 with dissolve
    "Unfortunately, my return was shallow and the lynx wasted no time in attacking it."
    show kem1p1i5 with dissolve
    ke "\"15-0!\""
    hide kem1p1i5
    hide kem1p1i4
    hide kem1p1i3
    hide kem1p1i2
    hide kem1p1i1
    hide diagram
    with dissolve
    ke "\"You'll have to do better than that if you want to take a point from me.\""
    "He said that with a smile on his face."
    "Ugh... this guy pisses me off."
    stop music2 fadeout 5.0
    scene SCourt with fade
    "By the end of the twentieth set I couldn't even keep myself standing."
    "It took us over three hours to get it all done, with only a few minimal breaks here and there."
    "And even then, when you consider how many sets it was, it should have definitely taken much longer."
    "That's how overwhelmed we were."
    "As soon as the last point was scored, I dropped to the floor, unable to keep myself standing."
    "Even scoring a single point was hard. The best I could do was to get two games against Morisaki-senpai..."
    "The girls, on the other hand, did a lot better than us."
    "Saya even managed to take a set from one of her opponents."
    show j 1 u at five with dissolve
    if jun_met == True:
        "Kobayashi stood over me, looking at me with worry."
    else:
        if tour_jun == False:
            "Kobayashi-kun stood over me, looking at me with worry."
        else:
            "Jun-kun stood over me, looking at me with worry."
    j "\"Are you alright? Maybe I should go get the nurse...\""
    mc 1 t sigh2 "\"I-I... I'm fine.\""
    "The only thing broken right now is my pride."
    "I force myself to stand up again, heaving heavily from exertion."
    mc 1 t considerate "\"Hah... it's been a while since I've been thoroughly beaten like that. It's incredibly frustrating but it also feels... refreshing, somehow.\""
    "I can't even remember when I last felt so completely useless."
    "Suddenly there was a wall ahead of me whose limits I couldn't even see."
    "Instead of feeling discouraged, I felt a sudden burst of excitement."
    show j 1 u happy at fdis
    j "\"Well, I guess you had fun then, all things considered. Kinda made me wish I could play tennis too.\""
    mc 1 t smile "\"Well, I'm glad you enjoyed watching us.\""
    "I'm still awed by the distance Morisaki-senpai managed to put between us in these two years..."
    "Just how did he manage to get so much better?"
    show j 1 u at fdis, three with move
    show kaito at seven with moveiridis
    mo "\"How are you feeling, [povLastName]-kun?\""
    mc 1 t sigh "\"Mostly frustrated. But, well... these kinds of things are good too.{w} Once in a while.\""
    mc 1 t smile "\"You've changed a lot, you know.\""
    mo "\"Hahaha. I guess I did change a little. Things are a lot tougher in America than I thought they'd be.\""
    mo "\"I was pretty confident in myself when I first got there, but I was quickly mowed down by them.\""
    mo "\"To be honest, there are currently twelve guys in our tennis program and I'm the weakest of them all.\""
    "That's a depressing thought..."
    mo "\"Still. I'm the one that's surprised. I was pretty disappointed when we played our first set, you know.\""
    mc 1 t sigh "\"Ah... sorry. I guess I didn't quite live up to your expectations.\""
    "Senpai gasped and started frantically waving his arms in denial."
    mo "\"No, no. That's not what I meant.\""
    mo "\"Well. It's true that I was expecting you to be much better, but...\""
    mo "\"To be honest, it's scary how much you've improved over the day. You got used to my speed in a flash.\""
    mo "\"By the end of the last set, I was actually struggling to score.\""
    "Really? It didn't feel like he was struggling at all."
    mc 1 t smile "\"Well, I guess we'll have to see how things go over the week.\""
    "Morisaki-senpai was surprised, as if he finally realized he hadn't said a word about it yet."
    mo "\"I'm glad we agreed to Mikado-san's idea. It's been so long since I've been to Japan, I'm still a bit jet lagged from the trip.\""
    mo "\"Can you imagine how tough it'd be if I played in the tournament feeling like this?\""
    mc 1 t curious "\"How do you think you'll fare in the competition?\""
    mo "\"Hmm... I'm not too sure. The prize is pretty big and it's worth quite a lot of points so I'm sure it's attracted quite a lot of higher-ranked folks.\""
    mo "\"And I still need to take part in the qualifiers after all!\""
    show kenma at offscreenright
    ke "\"Kaito, hurry up already. The van is already here to pick us up!\""
    "Sasaki-san shouts from the entrance."
    mo "\"Ah. Sorry to cut this short, [povFirstName]. I'll see you tomorrow.\""
    mc 1 t gentle "\"See ya.\""
    show kaito at offscreenright
    show j 1 u at fdis, five
    with move
    "I wave the two goodbye as they leave our building."
    show j 1 u watch at fdis
    j "\"You guys look like you get along pretty well.\""
    "I nod."
    mc 1 t smile "\"Morisaki-senpai used to be the club's captain when I first joined this school.\""
    show j 1 u happy at fdis
    j "\"Ah, that explains it!\""
    if jun_met == True:
        show j 1 u watch at fdis
        mc 1 t curious "\"By the way, Kobayashi...\""
        j "\"Just Jun is okay. Feels a bit pointless to be so formal since we're going to be seeing each other every day.\""
        mc 1 t think "\"Well... okay.\""
        "If I can have an excuse to drop all this stiff deference then I have no reason not to."
        mc 1 t smile "\"Was it fun? Feel like it was worth coming?\""
    else:
        if tour_jun == False:
            show j 1 u watch at fdis
            mc 1 t curious "\"By the way, Kobayashi..."
            j "\"Just Jun is okay. Feels a bit pointless to be so formal since we're going to be seeing each other every day.\""
            mc 1 t think "\"Well... okay.\""
            "If I can have an excuse to drop all this stiff deference then I have no reason not to."
            mc 1 t smile "\"Was it fun? Feel like it was worth coming?\""
        else:
            show j 1 u watch at fdis
            mc 1 t curious "\"By the way, Jun-kun..."
            j "\"Just Jun is okay. Feels a bit pointless to be so formal since we're going to be seeing each other every day.\""
            mc 1 t think "\"Well... okay.\""
            "If I can have an excuse to drop all this stiff deference then I have no reason not to."
            mc 1 t smile "\"Was it fun? Feel like it was worth coming?\""
    show j 1 u happy at fdis
    j "\"Yeah. It looked like a lot of fun!\""
    show j 1 u think at fdis
    j "\"The white hare felt like he was an amazing player, even though half the time I had no idea what he was doing.\""
    mc 1 t smile "\"His name is Keisuke. You're right about him being an awesome player. Not very physically imposing but he's very skillful and fast.\""
    mc 1 t wince "\"That's why I hate playing against him. He just makes me run all over the place and it's a chore.\""
    stop music fadeout 5.0
    scene SLockers
    show j 1 u smile at fdis, five
    with fade
    "Jun follows me all the way to the locker room."
    "I put my bag on the bench next to my locker and sit next to it, picking up a towel from inside it."
    mc 1 t sigh "\"Crap. My legs are hurting so much that going home might be a problem...\""
    show j 1 u blush at fdis
    "I start taking off my clothes. Upon seeing this, Jun-kun makes a weird noise and turns his back to me."
    j "\"A-anyway, [povFirstName]-san. It was really fun watching you play. I think I might come cheer for you in the next tournament.\""
    mc 1 t smile "\"Really? Thanks. That'd be appreciated.\""
    "I finish toweling myself off and I spray myself with a strong deodorant."
    "Since I don't feel like showering at school, I'll at least make sure I don't stink of sweat."
    mc 1 u "\"You can turn back around now.\""
    show j 1 u smile at fdis
    "Jun-kun glances over my way before turning around slowly."
    j "\"Sure, I'll come. {size=-6}You could also come to my piano competition if you want.{/size=-4}\""
    "If I didn't have good hearing, I probably would have missed that last part."
    mc 1 u "\"A piano competition? Those are a thing?\""
    "Jun-kun nods, a little more confidently."
    show j 1 u gentle at fdis
    j "\"Yes. They're a pretty big thing in Japan. You can gain scholarships for big name schools if you do well on those.\""
    j "\"Actually, I used to participate a lot when I was a kid, but... Anyway, I'd like it if you could come.\""
    mc 1 u smile "\"Sure. If I don't have a game scheduled for the day of your competition, I'll go.\""
    "I'm at least a little bit interested, after all."
    j "\"Well, I've got to get going anyway. Thank you very much for bringing me over. See you tomorrow!\""
    mc 1 u smile "\"See ya!\""
    show j 1 u smile at offscreenright with moveoridis
    "I lean against one of the lockers, letting my body get some rest."
    "My whole body is sore... It's been a while since I've worked this hard."
    show k 1 t angry at fdis, five with moveiledis
    "From the corner of my eye, I see Kei-kun entering the locker room and heading towards his locker."
    play sound "music/punchlocker.ogg"
    k "\"Damn it!\"" with hpunch
    "He punches his locker with full force, leaving a dent on the metal."
    "Keisuke turns towards me, his face is completely warped in anger."
    show k 1 t angryb at fdis
    k "\"That damn lynx! That guy is so cocky.\""
    mc 1 u shock "\"What happened? He seemed pretty nice to me.\""
    k "\"He came up to me after the last match and said: \"If that's how far you can go, then you should forget about placing in a national competition\". Who the hell does he think he is?\""
    play sound "music/punchlocker.ogg"
    k "\"Damn it!\"" with hpunch
    mc 1 u sigh "\"Did he really say that? {size=-6}Also, spare the poor locker, it didn't do anything.{/size}\""
    "That's a horrible thing to say, no matter how true it might be."
    k "\"Yeah, he did...\""
    show k 1 t angry at fdis
    k "\"I know I'm not good enough. I know that!\""
    show k 1 t avoidb at fdis
    k "\"... He didn't have to say it.\""
    show k 1 t angry at fdis
    play sound "music/tap.ogg"
    "I grab Keisuke's arm before he punches the locker a third time."
    mc 1 u "\"Alright, stop right there. I get that you're angry but you really need to calm down. Punching things won't solve anything.\""
    "What would you do if you severely injured your hand? You idiot!"
    mc 1 u "\"Sit.\""
    show k 1 t avoid at fdis
    mc 1 u angry "\"Sit!\""
    show k 1 t shock at fdis
    k "\"Y-yes!\""
    "Good. He's not resisting as much anymore."
    "I kneel down in front of him, gently inspecting his hand in search of any injuries."
    show k 1 t avoid at fdis
    k "\"It's fine. Just leave it be.\""
    "Kei-kun tries to push my hands away but I make sure to hold onto him firmly."
    "That's when I see a big cut between his ring finger and his pinky."
    "Without hesitation, I press into it as hard as I can."
    play music2 "music/BGM/Punchline.ogg" fadein 5.0
    show k 1 t wince at fdis, shake1
    k "\"OW! What's the big idea?\""
    mc 1 u angry "\"This-\""
    show k 1 t wince at shake1
    "I press the injury one more time, making him squirm."
    mc 1 u annoyed "\"This is not fine. I'll pick up the first aid kit and treat your wound. You sit there and don't you dare move.\""
    show k 1 t avoid at fdis
    "Even though he seemed annoyed at my orders, he made no effort to get up."
    "At least he's obedient."
    "Looking at his locker, I can see two dents on it."
    "Looks like one of his punches was right at the edge of the locker. Of course he ended up cutting himself."
    stop music2 fadeout 5.0
    scene SLockers
    show k 1 t avoid at fdis, five
    with fade
    play music3 "music/BGM/Let it Happen.ogg" fadein 5.0
    "It takes a bit of work, but I make sure his wound is cleaned and disinfected properly."
    mc 1 u smile "\"There. The cut is big but I don't think it'll need bandaging. It'll probably be sore for a while so be careful.\""
    show k 1 t worried at fdis
    k "\"Thank you. I...\""
    mc 1 u "\"Yes?\""
    show k 1 t avoidb at fdis
    k "\"I'm... I'm sorry I yelled at you. I shouldn't have lost my temper. All you were doing was try to help me.\""
    mc 1 u smile "\"Don't worry about it. It was interesting though. That was the first time I've ever seen you angry.\""
    show k 1 t avoid at fdis
    k "\"Yeah. Not my finest moment right there, I'll admit..."
    show k 1 t wry at fdis
    extend " Still, thank you for taking such good care of me.\""
    mc 1 u "\"I'd be lying if I said I didn't understand how you feel. Don't think I'm not frustrated about the whole thing either.\""
    mc 1 u smile "\"Heh, maybe we should have a strategy meeting to think up ways to beat them.\""
    show k 1 t uncomfortable at fdis
    k "\"That's...\""
    show k 1 t shock at fdis
    "Kei-kun freezes mid-sentence."
    show k 2 t cocky at fdis
    k "\"Actually, that's a great idea. You've adapted to them the fastest, perhaps you can give me some insight into what I can do!\""
    mc 1 u fsmile "\"H-huh? I was just jo-\""
    k "\"All right, it's settled then. I'll buy you some ice cream.\""
    "..."
    "What? What, if anything, does that have to do with finding ways to beat them?"
    mc 1 u sigh "\"Uhmm... Kei-kun, I don't think-\""
    show k 1 t avoidb at fdis
    k "\"Oh, shut up... I want to thank you for today...\""
    "Ah, so that's what this is about."
    "You could stand to be a little more honest."
    "Kei-kun takes off his shirt to get changed, though he quickly freezes when his shirt gets close to his nose."
    show k 1 t wince at fdis
    k "\"Ugh... there's no way I can get away without a shower. Let's go, [povFirstName]-san.\""
    mc 1 u "\"Nah. I'm already set.\""
    "I point to the bottle of deodorant spray on the bench."
    show k 1 t avoid at fdis
    k "\"Really? You think that's acceptable?\""
    mc 1 u fsmile "\"Well... yeah. It's been enough so far.\""
    show k 1 t sigh at fdis
    k "\"Do you have any idea how much we sweat today? I'm not going out with a guy that smells like a pile of rancid clothes.\""
    mc 1 u sigh "\"Can't you be a little less fussy?\""
    show k 1 t serious at fdis
    k "\"I'm already taking you out. The least you can do is shower.\""
    "You never even asked me if I {i}wanted{/i} to be taken out!"
    mc 1 u sigh "\"Fine, fine. Get off my tail.\""
    "I fish for a towel in my bag and start undressing. Kei-kun does the same behind me."
    "Ugh... I still hate being undressed in front of other people..."
    "I wrap myself in my towel before taking off my underwear and quickly make my way to the shower."
    stop music3 fadeout 6.0
    scene Showers with fade
    "I manage to get myself into a shower booth before Kei-kun even has time to get into the showers."
    "Still, he manages to take the one right next to mine."
    play music "music/shower.ogg"
    "Brr... they only have cold water in here..."
    "Ah, wait..."
    mc 1 n fsmile "\"Kei-kun... I didn't plan on showering here, you know. I don't have shampoo or soap.\""
    k 1 t "\"I'll slide you some of mine under the booth.\""
    mc 1 n "\"Oh, thanks.\""
    "..."
    mc 1 n "\"You know, you surprised me this time.\""
    k 1 t avoid "\"How so?\""
    mc 1 n smile "\"You're always going out with us but you've never actually invited any of us to go out with you before.\""
    mc 1 n smile "\"Hell, you're in my house all the time and I have no idea what yours looks like.\""
    k 1 t avoid "\"My house isn't exactly the kind of place I'd like to take guests... but I can see your point. I'm sorry for never inviting any of you anywhere before.\""
    mc 1 n happy "\"It's fine. I'm not asking you to invite me over, it's just... When you get used to someone never asking you out, you get surprised when they do.\""
    k 1 t calm "\"I guess I can kind of get what you're saying. Still, you helped me out. I'd feel bad if I didn't return the favor.\""
    mc 1 n smile "\"Heh, suit yourself.\""
    "I have no reason to say no anyway."
    "Who says no to free ice cream after all?"
    stop music fadeout 6.0
    scene IceCream
    show k 1 c smile at fdis, five
    with fade
    play music2 "music/BGM/In That Mood.ogg" fadein 6.0
    "Kei-kun takes me to a shop a few blocks away from school."
    "Funny, I've passed by this street a few times and I've never noticed this place before."
    "It looks so chic too."
    mc 1 c shock "\"Wow, I never knew this place existed.\""
    show k 1 c calm at fdis
    k "\"Yeah. It's pretty great. I only found out about it last summer.\""
    "Ooh, it's one of those self-service parlors that sell ice cream by weight."
    "I like places like those. They're always the best bang for your buck!"
    show k 1 c smile at fdis
    "While I'm standing around in a daze, Kei-kun quickly serves himself."
    "The clerk writes it down on a card and hands it over to him."
    show k 1 c at fdis
    k "\"Quit standing around and get your serving. I'm gonna be sitting in that booth over there!\""
    "Oh, right!"
    "I make my way to the freezer and see the various flavor stickers. They all look really tasty!"
    "Hmm... I wonder if there's any price difference between flavors. Let's see, where's the menu..."
    "..."
    "HUH?!"
    "{i}¥1800 per 100 grams?{/i} That's insane. A kilo of this would be more than my monthly allowance!"
    "I do a complete 180 and sit in front of Kei-kun without taking anything."
    k "\"... Why didn't you get anything?\""
    mc 1 c fsmile "\"You know what? I don't really feel like eating ice cream.\""
    show k 1 c annoyed at fdis
    k "\"The only reason I brought you here was so I could treat you. Just get something.\""
    "How can someone be so oblivious?!"
    "And more importantly, how can he be okay with treating someone to something so expensive?"
    mc 1 c avoid "\"It's just... I'm not comfortable spending this much money on just ice cream...\""
    show k 1 c shock at fdis
    k "\"This much...\""
    "Kei-kun's gaze flicks towards the menu for a second."
    show k 1 c avoid at fdis
    k "\"Oh.\""
    "He sits there in silence for a few seconds, analyzing what he is going to say."
    show k 1 c at fdis
    k "\"You don't know?\""
    mc 1 c curious "\"Know what?\""
    show k 1 c shock at fdis
    "His eyes widen in complete shock."
    "What is this thing that I'm supposed to know?!"
    k "\"My name. Urushihara. Doesn't it ring any bells for you?\""
    mc 1 c talk "\"No. Should it?\""
    "He gapes, looking even more surprised than he already did. Slowly, he leans over on his chair and whispers to me."
    show k 1 c at fdis
    k "\"Haven't you heard of the Urushihara Corporation? The biggest tech conglomerate in the world? You know, designers of the most popular computer operating system and phones.\""
    show k 1 c sigh at fdis
    k "\"If I'm not mistaken, your phone was manufactured by us too.\""
    "Us? Huh? Wait... Urushihara Corporation... Wait... He's {i}that{/i} Urushihara?!"
    mc 1 c shock "\"Y-you're kidding!\""
    show k 2 c sigh at fdis
    k "\"I guess it finally makes sense why you always treated me just like an average joe...\""
    show k 1 c sad at fdis
    k "\"So I guess you're going to start treating me differently now that you know...\""
    "My mind is completely blank for a few seconds. I'm... just... wow."
    "I finally snap out of the near-trance I was in, having to clear my throat a few times to get my voice to work."
    mc 1 c avoid "\"N-no. I don't care if your family is rich. I was just... shocked.\""
    mc 1 c shock "\"Wait. Is that why you never invite anyone over?\""
    "Kei-kun shifts on his seat."
    show k 1 c uncomfortable at fdis
    k "\"Yeah... I gave up on having friends over a few years ago. Most people only seemed to be interested in befriending me so they could enjoy the \"perks\" that come with being my friend.\""
    show k 1 c sad at fdis
    k "\"To be honest, I had completely given up on having friends who really care about me for who I am instead of what I have...\""
    show k 1 c avoidb at fdis
    k "\"You, Saya-san and Urata are the only people who've ever actually shown an interest in getting to know me for me...\""
    mc 1 c avoid "\"I... oh God, it's a horrible thing to say but I can understand. People can be very shallow.\""
    mc 1 c fsmile "\"Once I became a little famous, a bunch of kids my age started approaching me just because they thought they'd raise their {i}status{/i} if they were seen with me.\""
    mc 1 c shock "\"N-not that I think my situation is even remotely comparable to yours of course!\""
    show k 1 c shock at fdis
    "Kei-kun looks completely stunned by my words."
    show k 2 c gentle at fdis
    k "\"Hahahaha... Oh, man... I didn't expect this.\""
    show k 2 c gentleb at fdis
    k "\"Funny. I brought you here to thank you for making me feel better and, instead, you ended up consoling me again.\""
    show k 1 c wry at fdis
    k "\"Thank you, [povFirstName]-san...\""
    "Well, I'll be damned. I never knew this side of Kei-kun..."
    show k 2 c gentle at fdis
    k "\"Well, now you know why I didn't mind bringing you over."
    show k 1 c smile at fdis
    extend " So please, go get yourself some ice cream. After you were so nice to me today, I want to treat you no matter what.\""
    "Keisuke basically kicks me out of the booth, laughing."
    mc 1 c shock "\"Alright alright, I'm going. Stop kicking my shin!\""
    scene IceCream
    show k 1 c calm at fdis, five
    show cg3
    with fade
    "We spend a good deal of time talking and having fun."
    "I've already eaten most of my ice cream, the little bit left on the bottom has already turned into a soupy mess (that I will definitely not waste because this is one very expensive soupy mess)."
    k "\"Thanks for coming with me today, [povFirstName]-san. It's good to talk to someone without worrying whether they're interested in me because of me or because of my family.\""
    mc 1 c think "\"I'm a bit curious now. Do Saya-chan and Shoichi know about your family? I know for a fact that they're not the type of people to care about that kinda thing.\""
    mc 1 c "\"Plus, Shoichi's dad also makes quite a bit of money so it's not like he needs any. Not as much as your family, though.\""
    show k 1 c avoid at fdis
    "At the mention of Shoichi's name, Keisuke's demeanor immediately changes."
    "Actually, this just might be an opportunity to prod him about it."
    mc 1 c curious "\"Hey, Kei-kun. I actually have a question.\""
    show k 1 c at fdis
    k "\"Yes?\""
    mc 1 c "\"Why do you and Shoichi bicker so much? You guys don't look like you dislike each other, but...\""
    show k 1 c sigh at fdis
    "Just as I expected, his entire face scrunches up at the mention of Shoichi."
    k "\"It's not... I don't {i}dislike{/i} him. It's... it's complicated.\""
    "Huh. That actually answered... nothing at all."
    mc 1 c sigh "\"Oookay... Why?\""
    "Keisuke sighs."
    k "\"I'm not really sure. He's a nice guy and I do like him... but he always ends up doing or saying something that pisses me off.\""
    show k 1 c at fdis
    k "\"But like I said, I do like him.\""
    mc 1 c sigh "\"Soo... you're like two friends who bicker.{w} A lot.\""
    show k 1 c smile at fdis
    k "\"Something like that. I do think of him as a friend, yes.\""
    mc 1 c avoid "\"Good to know.\""
    "I ready myself to get up and discard the plastic cup, but Keisuke holds my arm."
    show k 1 c serious at fdis
    k "\"Wait. It's my turn to ask a question.\""
    mc 1 c shock "\"Oh, sure. Shoot.\""
    k "\"Why does it matter to you whether we get along or not?\""
    "That's... hard to explain."
    mc 1 c smile "\"Well... Shoichi is my best friend. I've known him since we were little kids. The two of us are always spending time together.\""
    mc 1 c "\"And I also like you a lot. You're pretty dependable and easy to get along with. But even though you're definitely part of our group, it always feels like you're keeping your distance.\""
    mc 1 c avoid "\"I guess I worry that you're just avoiding us to be away from Shoichi.\""
    show k 2 c sigh at fdis
    "Keisuke lets go of my hand."
    "His fingers start tapping at the table in front of him."
    k "\"Well... That is not untrue. Whenever I'm with you guys, I always worry that I'm going to ruin your fun...\""
    show k 1 c avoid at fdis
    k "\"I mean. The few times we all went out together during spring break, I could tell how annoyed you and Saya-san were when he and I argued.\""
    k "\"I guess... I guess I was afraid I was being a burden.\""
    "Wow. I didn't expect him to be so honest with me."
    mc 1 c smile "\"Don't be. I won't lie, you two do get on my nerves every so often. But even so, it's nice having you around.\""
    mc 1 c happy "\"You're a good guy. We aren't going to forget that just because you and Shoichi are fighting.\""
    show k 1 c shock at fdis
    "My words seem to strike him deeply as his eyes open wide."
    show k 2 c gentleb at fdis
    k "\"Thank you, [povFirstName]-san, that... That actually means a lot to me.\""
    scene Street1N with fade
    "Kei-kun urged me to wait outside while he paid."
    "It's gotten pretty dark while we were inside."
    "It's actually a little cold."
    show k 1 c smile at five with moveiridis
    k "\"There. I've already paid.\""
    k "\"Wow, some of the stores are closing up already. What time is it?\""
    play sound "music/phonebeep.ogg"
    "He fishes his phone out of his pocket."
    show k 1 c at fdis
    k "\"Almost 9PM. We were in there for a while, huh.\""
    mc 1 c smile "\"Time flies when you're having fun.\""
    show k 1 c calm at fdis
    k "\"Couldn't have said it better myself.\""
    show k 1 c at fdis
    mc 1 c curious "\"By the way, how are you getting home?\""
    show k 1 c smile at fdis
    k "\"I'm going to call my driver to pick me up. Want a ride?\""
    mc 1 c smile "\"Nah. You know I live nearby. I can just walk.\""
    show k 1 c calm at fdis
    k "\"Fair enough."
    show k 1 c smile at fdis
    extend " Thank you again for coming here with me. You have no idea how happy you've made me today.\""
    mc 1 c smile "\"It was fun for me so there's no problem there.\""
    show k 2 c gentle at fdis
    k "\"I can actually believe you when you say that.\""
    show k 1 c smile at fdis
    k "\"Anyway, you should probably get going now. I'm going to call the car to come pick me up.\""
    mc 1 c "\"It's fine. I'll wait with you until the car gets here.\""
    show k 2 c gentle at fdis
    k "\"Don't be stupid, it's super late already. Just go home. Your family is probably waiting for you.\""
    mc 1 c "\"But will you be alright waiting here alone?\""
    show k 1 c smile at fdis
    k "\"I'll be waiting inside the store until they arrive. I do have a bit of common sense, you know. I'm not gonna wait outside in the dark streets.\""
    mc 1 c smile "\"Alright, fair enough. Have a good night.\""
    show k 1 c wry at fdis
    k "\"You too, [povFirstName]-san. Be safe and see you tomorrow.\""
    mc 1 c happy "\"See ya!\""
    stop music fadeout 2.5
    stop music2 fadeout 2.5
    $ date = None
    jump Day3
