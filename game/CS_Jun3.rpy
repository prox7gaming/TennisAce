label junstart_2:
    $ uihide = True
    stop music2 fadeout 2.5
    $ junhearts += 1
    scene SCorridor with fade
    "*sigh*"
    "Half of the day has already gone by and nothing exciting has happened..."
    "Other than our class discussing preparations for the festival, it's mostly just the same boring routine of studying..."
    "Without practice to break it up, it gets tedious very quickly."
    "I was kind of looking forward to lunch with everyone but both Shoichi and Saya had to excuse themselves because of other duties..."
    "As for Jun... he just kinda disappeared before the bell even struck."
    "Hence, I'm now walking around on my own trying to find something to do."
    scene SRooftop with fade
    play sound "music/metaldoor.ogg"
    play music "music/breeze.ogg"
    "Before I'd even decided on where I wanted to go, my feet already began carrying me through a familiar path."
    "Well, I guess the roof is as good a place as any."
    "I might as well take a nap since I've got nothing better to do anyway."
    "Voice 1" "\"I'm telling you, it'd be a great idea!\""
    "Voice 2" "\"Again, I'm gonna have to disagree with you on that.\""
    "Suddenly as I'm walking out to the roof, I hear a set of voices talking very loudly."
    "It's two male voices... for some reason they sound really familiar but I can't quite place them."
    "It seems they didn't hear me coming in because they continue chatting as if nothing's happened."
    "Taken by my curiosity, I press myself against the wall so they can't see me, trying to listen in on their conversation."
    "Voice 1" "\"Come on, pretty please? I really think it'd be really fun if we got together and did it!\""
    "Voice 2" "\"N-no! It's been years since I last did that, I'm way too out of practice. I'm sure it'd just be a bad time for you.\""
    "Voice 1" "\"That's not true! I just really want to do it with you!\""
    "..."
    play music2 "music/BGM/Mischief Maker.ogg"
    "What the hell is going on here?!" with hpunch
    "Do it? What do they mean? Do what?" 
    "T-they couldn't possibly be talking about {i}that{/i}, right? And on a school rooftop of all places!"
    "Voice 2" "\"Look, I already said no, okay... I'd need to spend quite a bit of time preparing if I'm gonna do it with you, otherwise there's no way I could keep up.\""
    "Voice 1" "\"So you're saying you'd do it if you could have more time to practice?!\""
    "W-why does this guy sound so excited?"
    "Voice 2" "\"M-maybe. I'm not making any promises, okay...\""
    "Voice 1" "\"Yay! I can't wait!\""
    "W-what the hell is going on here?!"
    "Unable to stand by anymore, I walk out to interrupt their conversation and-"
    stop music2 fadeout 1.0
    show j 1 u gentle at fdis, three
    show k 1 u sigh at fdis, seven
    with dissolve
    "..."
    mc 1 u shock "\"Eh?\""
    show j 1 u shock at fdis
    show k 1 u shock at fdis
    j "\"[povFirstName]-san?\""
    mc 1 u shock "\"...\""
    mc 1 u dismay "\"{size=+4}Ehhhhhhhhhh?!{/size}\"" with hpunch
    show j 1 u cshock at fdis
    show k 1 u wince at fdis
    "Taken completely by shock, I let out a deafening scream."
    play music2 "music/BGM/Punchline - Org.ogg" fadein 2.5
    k "\"W-what the hell are you doing? Don't just do that all of a sudden.\""
    j "\"M-my ears! Are they bleeding? Am I deaf?!\""
    show k 1 u avoid at fdis
    k "\"I'm pretty sure you're fine. The only thing broken is his mind..\""
    mc 1 u dismay "\"W-w-w-w-what the hell are you two doing? I-I didn't know you two were that close?\""
    show j 1 u watch at fdis
    show k 1 u at fdis
    k "\"That close? What are you talking about?\""
    mc 1 u dismayb "\"D-don't play dumb with me, I heard your entire conversation. You two were talking about d-d-doing it together!\""
    show k 1 u avoid at fdis
    k "\"Doing it toge-\""
    show k 1 u shock at fdis
    $ renpy.pause(1.0)
    show k 1 u angryb at fdis
    k "\"You thought we were talking about {i}that{/i}? What is wrong with you?!\""
    show j 1 u wince at fdis
    j "\"U-uhm... what are you guys talking about?\""
    k "\"This idiot thought we were talking about hooking up!\""
    show j 1 u cshockb at fdis, shake1
    j "\"Huuuuuh?\""
    mc 1 u wince "\"W-well, weren't you? You guys were talking about \"doing it together\" and how it'd be \"really fun if we did it together\"!\""
    k "\"He was asking me to do a duet with him on the violin!\""
    mc 1 u shockb "\"W-what?\""
    show k 1 u annoyed at fdis
    k "\"I told him I hadn't played it in a while and he insisted that he thought it'd be fun if we played together.\""
    show k 1 u avoidb at fdis
    k "\"Seriously, what the hell is wrong with you? Even if we both swung that way, do you really think either of us is the type to just talking about that sort of thing so casually?\""
    mc 1 u shockb "\"I-I-I...\""
    "Oh man, I really messed up..."
    mc 1 u considerate "\"... Oops?\""
    show k 1 u angry at fdis
    k "\"Don't just \"oops\" me, jackass!"
    show k 1 u avoid at fdis
    extend " Just look at poor Kobayashi. I think he completely glitched out...\""
    mc 1 u wince "\"J-Jun, are you alright?\""
    "I wave my hand in front of his eyes, yet he remains completely motionless."
    mc 1 u worried "\"Oh boy...\""
    show k 1 u worried at fdis
    k "\"Jun-san, are you alright?\""
    "Jun merely stood frozen in place."
    mc 1 u avoid "\"I think his brain shorted out...\""
    show k 1 u sigh at fdis
    k "\"You think?\""
    show k 1 u avoid at fdis
    k "\"Time for plan B.\""
    mc 1 u curious "\"Plan B?\""
    "Kei-kun reached behind Jun's ears, gently holding onto his left one and reaching in close."
    mc 1 u shockb "\"What are you-\""
    "Stunned by the sudden motion, I do nothing in response and-"
    show k 1 u angry at fdis
    show j 1 u wince at fdis:
        ease .2 zoom 0.7 xoffset 0 yoffset 0
    k "\"{size=+4}Wake up!{/size}\"" with hpunch
    "Keisuke screams directly into Jun's ear, making the tiger jump back."
    j "\"W-what's going on?\""
    "... It seems Keisuke has just forcibly rebooted Jun's systems..."
    mc 1 u considerate "\"Are you sure there wasn't some sort of gentler approach?\""
    show k 1 u annoyed at fdis
    k "\"Why stick to the uncertain when I knew of something that would work?\""
    mc 1 u worried "\"... Hard to argue with that logic.\""
    show j 1 u pout at fdis:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    show k 1 u at fdis
    j "\"Did you really have to scream that loud into my ear? All I can hear from that side is buzzing...\""
    show k 1 u avoid at fdis
    k "\"Your fault for just freezing up like that.\""
    show j 1 u wince at fdis
    j "\"I needed time to process...\""
    show k 1 u annoyed at fdis
    k "\"What are you, some sort of old model computer? You shouldn't completely freeze up when you're trying to deal with things.\""
    j "\"Ugh...\""
    "I feel kinda bad for the guy. He's rubbing the left side of his head as if his ear is really hurting."
    "I make sure to properly apologize to him... at least in my mind."
    show j 1 u pout at fdis
    j "\"[povFirstName]-san, what the hell kind of weird ideas do you have cooking up in that head of yours?\""
    mc 1 u considerate "\"I don't really have an answer to that... sorry.\""
    show k 1 u sigh at fdis
    k "\"I don't even know what to feel about this...\""
    mc 1 u wince "\"Again, I'm sorry for misunderstanding.\""
    mc 1 u considerate "\"But you two have to admit you were saying some pretty misleading things.\""
    show k 1 u eyesc at fdis
    k "\"I admit to nothing.\""
    mc 1 u shock "\"Wha-\""
    show j 1 u avoid at fdis
    j "\"Same here. We're clearly not the ones at fault.\""
    mc 1 u sigh2 "\"You two could try to work with me at least a little bit here.\""
    show k 1 u at fdis
    show j 1 u watch at fdis
    k "\"Nope. Not gonna happen.\""
    "Ugh... talk about stubborn."
    mc 1 u considerate "\"So... uhm... you two were talking about playing a duet, right?\""
    show k 1 u smile at fdis
    k "\"Trying to change the subject, I see."
    show k 1 u calm at fdis
    extend " I'll pretend I didn't notice that.\""
    mc 1 u sigh "\"Well, thank you for your restraint...\""
    show k 1 u haughty at fdis
    k "\"You're welcome.\""
    show k 1 u avoid at fdis
    k "\"Either way... yeah, Kobayashi wanted me to play violin with him on a duet.\""
    show j 1 u gentle at fdis
    j "\"I thought it'd be fun if we played a classical piece together.\""
    show k 1 u at fdis
    k "\"While I don't entirely reject the notion, I really don't think I'd be the best for that. I haven't played in years...\""
    show k 1 u sigh at fdis
    k "\"Seriously, [povFirstName]-san, why did you have to tell him I played the violin?\""
    mc 1 u considerate "\"Now this is my fault?\""
    show j 1 u happy at fdis
    j "\"Come on, Keisuke-san. I'll give you all the time you need to practice again. Why not give it a spin?\""
    k "\"You really are pushy about this aren't you?\""
    j "\"If it gets me what I want!\""
    show k 1 u avoid at fdis
    k "\"{size=-2}You're even aware of it?{/size}\""
    mc 1 u smile "\"Come on, Kei-kun, why not give it a try?\""
    show k 1 u sigh at fdis
    k "\"Now you're in on it too?\""
    mc 1 u happy "\"Oh, come on. Just look at Jun. How can you say no to this cute little face?\""
    show j 1 u gentle at fdis
    j "\"Pretty please?\""
    show k 1 u avoid at fdis
    k "\"You two are unbelievable...\""
    "Oh, is the corner of his mouth curving up a bit in a smile?"
    show k 1 u sigh at fdis
    k "\"I'll... I'll think about it, okay?\""
    show j 1 u happy at fdis, jumping
    j "\"Yay!\""
    "Jun hops around, waving his arms in the air excitedly."
    "It's a comical sight that also warms the heart."
    "He's so pure and sweet and precious... he really reminds me of a little kid."
    "... Which I'm sure he'd get angry at me if I said out loud."
    show k 1 u avoid at fdis
    k "\"Don't get so happy about it, I only said I'd think about it.\""
    j "\"Maybe, but that's already half the battle!\""
    show k 1 u sigh at fdis
    k "\"You really are an optimist by heart aren't you?\""
    show j 1 u think at fdis
    j "\"Hmm... I wonder about that.\""
    show k 1 u at fdis
    k "\"Either way, if you two will excuse me, I think I've already had enough time to clear my head. I should probably head downstairs.\""
    show j 1 u happy at fdis
    j "\"Okay. See you later!\""
    mc 1 u smile "\"Talk to you later, Kei-kun.\""
    show k 1 u smile at fdis
    k "\"Thanks. See you later too.\""
    show k 1 u smile at offscreenright with moveoridis
    play sound "music/metaldoor.ogg"
    show j 1 u smile at fdis, five with move
    stop music2 fadeout 2.5
    "The sound of the metal door shutting close behind Kei-kun echoes loudly through the roof, leaving Jun and I alone here."
    mc 1 u "\"...\""
    show j 1 u watch at fdis
    j "\"By the way, [povFirstName]-san, what are you doing up here?\""
    mc 1 u sigh "\"That's supposed to be my question. I come up here all the time. You on the other hand do not.\""
    show j 1 u considerate at fdis
    play music3 "music/BGM/Snowy Day.ogg" fadein 5.0
    j "\"Hehehe... I guess that's true...\""
    show j 1 u smile at fdis
    j "\"I just felt like coming upstairs, I guess.\""
    mc 1 u sigh "\"That's... that's it? You didn't have any real reason?\""
    show j 1 u think at fdis
    j "\"Does someone need a reason to go somewhere?\""
    mc 1 u sigh2 "\"Well yeah, of course you do.\""
    show j 1 u happy at fdis
    j "\"Well, I didn't really have any. I just felt like coming here.\""
    "... It's like trying to talk to a brick wall."
    mc 1 u sigh "\"You really didn't have any more compelling reasons to come up here?\""
    show j 1 u think at fdis
    j "\"Not really. I could try making one up if that would make you feel better though.\""
    mc 1 u sigh2 "\"... Are you mocking me? I feel like you're mocking me.\""
    show j 1 u happy at fdis
    j "\"Hehehehe.\""
    "As always, I can't tell what's going on in his head."
    "This tiger remains as much of a mystery to me as he was when we first met."
    show j 1 u think at fdis
    j "\"I can't really say much about it... I just feel like wandering around sometimes.\""
    show j 1 u considerate at fdis
    j "\"There was this one time when I felt like walking around at night, went out into the street and ended up getting lost. Boy, were my parents mad at me back then.\""
    "... This guy really is a danger to himself."
    mc 1 u sigh2 "\"I'm not even gonna try asking for more details about it. I get the feeling the lack of logic would just drive me nuts.\""
    show j 1 u happy at fdis
    j "\"Hehehe.\""
    mc 1 u sigh "\"This isn't funny...\""
    show j 1 u smile at fdis
    j "\"It is for me.\""
    "... This guy."
    mc 1 u "\"Leaving the topic of your wanderlust aside, how's the progress on your rehearsal been going? Have you managed to perfect that song like you wanted to?\""
    show j 1 u think at fdis
    j "\"I wish. It's still nowhere near the level I want it to be when I perform. I guess I'll just have to be patient and keep practicing.\""
    "I have a hard time believing he can get any better than he already is..." 
    "But then again, this guy has a history of subverting expectations... and not always in a good way."
    show j 1 u smile at fdis
    j "\"I know I'll get there eventually, it's just a matter of practice.\""
    show j 1 u considerate at fdis
    j "\"Though I have to admit it's a bit frustrating at times.\""
    mc 1 u curious "\"Frustrating? I never thought you'd feel that practice is frustrating.\""
    show j 1 u wince at fdis
    j "\"Are you kidding me? Practice is nerve-racking.\""
    show j 1 u sigh at fdis
    j "\"It's a constant battle against myself... trying to confront my music with sincerity, trying to overcome the musician I've always been, feeling helpless whenever I don't progress as fast as I can.\""
    show j 1 u considerate at fdis
    j "\"It's one of the worst feelings in the world. There were times when I felt like throwing up from all the pressure...\""
    mc 1 u shock "\"...\""
    "I... I had no idea he could feel like this too."
    "I thought someone like Jun was the type to always be having fun no matter what."
    "I thought he'd always be happy and content as long as he had the piano... I never thought it could make him frustrated like that."
    mc 1 u wince "\"... Don't you worry about the meaning behind those feelings?\""
    show j 1 u think at fdis
    j "\"The meaning behind them? What do you mean?\""
    show j 1 u watch at fdis
    mc 1 u wry "\"I've... felt like that before. To be honest, I feel like that to this day. Whenever I'm practicing, this feeling of anxiousness starts to take hold of me.\""
    mc 1 u considerate "\"I start to feel like I'm not improving. I get desperate, anxious, worried, stressed... sometimes it makes me feel sick to my stomach.\""
    mc 1 u avoid "\"It always makes me wonder... if maybe those feelings mean that I don't really love tennis... that maybe I was wrong in thinking that this is for me.\""
    j "\"..."
    show j 1 u think at fdis
    extend " I think it's the opposite.\""
    mc 1 u shock "The... the opposite?\""
    show j 1 u watch at fdis
    j "\"Yeah. I think it's {i}because{/i} we feel that way that we can know we truly love what we do.\""
    mc 1 u wince "\"I... I don't follow.\""
    show j 1 u happy at fdis
    j "\"I mean... yeah, it sucks when we feel like that. But think about it, would you ever really worry that much about something you don't like?\""
    show j 1 u smile at fdis
    j "\"I believe that the reason we can feel so awful about the things we do is {i}because{/i} we love what we do. We love it so much that we want to devote everything we have to it, and that makes us worry when we feel like we're not making progress.\""
    show j 1 u happyb at fdis
    j "\"Those feelings of helplessness are awful, but, in a way, I feel like they are also wonderful. Because to me they are the proof that I really love the piano more than anything else!\""
    mc 1 u shock "\"...\""
    "Did... did I just hear a speech like that from... from Jun?"
    "Jun of all people?!"
    mc 1 u avoid "\"I... never thought about it this way...\""
    "I never really expect Jun to have something so insightful to say."
    "In a way, he's completely surprised me again."
    "This guy really is a little box full of surprises."
    mc 1 u considerate "\"I... I don't even know what to say here, Jun.\""
    show j 1 u smile at fdis
    j "\"Don't say anything. It's okay to be out of words every now and then.\""
    mc 1 u happy "\"Haha. I really didn't expect this kind of wisdom from you of all people, that's for sure.\""
    show j 1 u at fdis
    $ renpy.pause(0.7)
    show j 1 u blank at fdis
    $ renpy.pause(1.0)
    show j 1 u judge at fdis
    j "\"Why me \"of all people\"?\""
    "Oops..."
    mc 1 u fsmile "\"Oh, hehe... uhm... wow, that really came out wrong, huh?\""
    j "\"What was it {i}supposed{/i} to mean, then?\""
    mc 1 u fsmile "\"Well... err, you know, it's... uhm... Oh man, look at the time, I don't want to be late for class do I?\""
    j "\"[povFirstName], answer me!\""
    mc 1 u fsmile "\"S-sorry, the signal is cutting out. I can't hear you well. I'm... I'm going through a tunnel.\""
    show j 1 u annoyed at fdis
    j "\"{cps=10}[povFirstName]-san...{/cps}\""
    mc 1 u fsmile "\"See ya!\""
    j "\"Get back here!\"" with hpunch
    scene Sky with fade
    "... I ended up getting chased through the school by a tiger... that was the first time in my life that I ever felt like I was being hunted."
    "And for a guy his size, Jun can certainly be pretty fast when he needs to be..."
    stop music fadeout 2.5
    stop music3 fadeout 2.5
    $ date = None
    jump cs_final