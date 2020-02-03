label Day10_Jun:
    scene Bedroom with squares
    "Right... that's why I had my alarm blaring this early in the morning on a weekend."
    "... I don't really want to get up but I don't think standing Jun up would be a good idea."
    scene black with fade
    "After seeing how excited he was about it when he asked me to come with him... it just wouldn't feel right to ditch."
    "No, it's not even that..."
    show j 1 c happyb at fdis, fiveh with squares
    "I'll admit, after seeing how cute he looked when asking me to go, I just felt like I wasn't allowed to say no."
    "Jesus, the power of cuteness is scary."
    "I guess cute things are still my weak spot..."
    show Bedroom with fade
    "Ah, never mind that. I still need to get up and get myself ready."
    "We agreed to go out at 10 so I probably shouldn't take too long to meet him."
    "Gonna take a quick shower and brush my teeth."
    "... Should I eat something before I go? Hmm..."
    play music "music/crowd01.ogg" fadein 5.0
    scene Station with fade
    "..."
    "Why is it that whenever Jun is involved, I end up waiting for a long time?"
    play sound "music/phonebeep.ogg"
    "It's already 10:12. Jeez, he could at least call me to tell me he's going to be late."
    play sound "music/ringtone.ogg"
    "Oh, speak of the devil."
    play sound "music/phonebeep.ogg"
    mc 1 c curious "\"Yeah?\""
    play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
    j 1 c fluster "\"{size=+4}[povFirstName]-saaaaaaaaan!{/size}\"" with hpunch
    mc 1 c wince "\"Wah!\""
    "I hear a deafeningly loud yell from the other side of the line, nearly dropping my phone as I recoil away from it."
    mc 1 c shock "\"J-Jun? What's going on, why are you shouting?\""
    j 1 c flustert "\"Nuuuu-\""
    "Instead of saying something, Jun is just freaking out on the other side of the line."
    "Oh boy, this is gonna be complicated."
    j 1 c shock "\"Ah!\""
    "From the other end of the line, I hear Jun talking to someone else. I can't make out anything else because it's really noisy where he is."
    "Is he in the middle of the street?"
    "After a couple seconds of radio silence, the noise on the other end of the line disappears."
    "?" "\"Yo!\""
    "A voice that isn't Jun's speaks up from the other end of the line."
    "?!"
    "Could it be that he got mugged?"
    "No, wait... I know this voice."
    "Could it be..."
    mc 1 c shock "\"Class Rep?\""
    "I shoot out a wild guess, but that's who I was reminded of."
    "I hear some giggling from the other end of the line."
    if povFirstName == "Yuuichi":
        ay "\"Bingo, you got it. Nicely done, Yuu-kun.\""
    else:
        ay "\"Bingo, you got it. Nicely done, [povFirstName]-kun.\""
    stop music2 fadeout 2.5
    play music3 "music/BGM/Dazzling Sunlight.ogg" fadein 5.0
    "Waaah, am I relieved that it's someone we know instead of a stranger."
    "Things really could have gotten scary if Jun had been robbed!"
    "... But then again, what sort of thief steals a phone and then says \"Yo\" to the person on the other end of the line?\""
    mc 1 c curious "\"What are you doing with Jun's phone, Class Rep?\""
    ay "\"Oh, I'm taking care of the store today. I just happened to see Jun-kun walking around the front of the store and looking like a lost kitten.\""
    ay "\"Sooooo, I brought him in.\""
    ay "\"You should have seen it, he had these big tears in his eyes and his face was all red. It was quite adorable.\""
    "I hear some commotion on the other end of the line and it goes mute for a few seconds."
    ay "\"Would you look at that, Jun-kun just told me that I wasn't supposed to tell you that, so pretend you didn't hear it from me, okay?\""
    "Once again, I can hear Jun's flustered voice shouting something in the background."
    "... She's totally doing this on purpose just to tease him."
    ay "\"For the time being, could you come pick him up at the store?\""
    "Well... I suppose I am pretty close by so I don't see why not."
    mc 1 c smile "\"Sure, I should be there in about five minutes or so.\""
    ay "\"That's perfect, then. See ya when you get here.\""
    play sound "music/phonebeep.ogg"
    "..."
    "Well, I suppose there's no need to hurry but..."
    "I'd feel bad if I made Class Rep take care of Jun when she's supposed to be working."
    stop music3 fadeout 2.5
    play music2 "music/BGM/The People Here.ogg" fadein 5.0
    scene Sweets
    show ayako at seven
    show j 1 c watch at fdis, three
    with fade
    play sound "music/door.ogg"
    "When I step inside the sweets shop, I see Jun standing next to the counter, leisurely chatting away with Class Rep."
    "As soon as she notices me Class Rep smiles and waves, beckoning me to come closer."
    ay "\"Oh, look who it is.\""
    show j 1 c shock at fdis
    j "\"Ah!\""
    "Jun turns around after Class Rep speaks, noticing me and-"
    show j 1 c flustert at fdis
    j "\"{size=+4}[povFirstName]-saaaaaan!{/size}\""
    show j 1 c flustert at fdis, fiveh with move:
        ease .2 zoom 1.5 xoffset -50 yoffset 80
    play sound "music/fall.ogg"
    "!" with hpunch
    "- nearly tackling me to the ground."
    mc 1 c wince "\"C-Calm down, Jun. What's going on here?\""
    if povFirstName == "Yuuichi":
        ay "\"Just in time. It's good to see you, Yuu-kun. Feels like it was just yesterday when we last spoke.\""
    else:
        ay "\"Just in time. It's good to see you, [povFirstName]-kun. Feels like it was just yesterday when we last spoke.\""
    mc 1 c sigh "\"Uhm... that's because it {i}was{/i} just yesterday. Did you lose your mind, Class Rep?\""
    "She covers her mouth with her hand, giggling."
    ay "\"Of course not. I'm just teasing. Jun-kun here was really anxious to see you as you can plainly see."
    "... I could tell."
    "Jun looks up at me with huge tears forming on his face and sniffles."
    "Normally I'd be taken aback to see someone crying, but..."
    "Come to think of it, I seem to have more memories of seeing Jun crying than I do of any of my other friends."
    "I guess it's a little late for me to be noticing this, but... he's kind of a crybaby isn't he?"
    "Still, something in me compels me to protect and nourish this adorable creature... so I start petting his head."
    mc 1 c considerate "\"Why don't you tell me what happened, Jun?\""
    show j 1 c blush at fdis
    "Jun's face goes red and he immediately buries it on my chest."
    "H-Hey, isn't this a little... I-I mean, what would other people think if they saw us like this?"
    "Class Rep covers her mouth with her hands and starts giggling, the scheming look on her face scaring the crap out of me."
    stop music2 fadeout 2.5
    play music3 "music/BGM/haretahiha kousin.ogg" fadein 5.0
    ay "\"Fufufu, I didn't know you two had that kind of relationship. And you're so lovey-dovey even in public.\""
    mc 1 c shockb "\"I-It's not what it looks like!\"" with hpunch
    "C-Crap, I know she's just trying to get a rise out of me but I'm at risk of getting swallowed up by her pace."
    "First things first, I really need to push Jun away from m-"
    "!" with hpunch
    "When I look down, I see Jun staring up at me, his face red matted by tears."
    "When I see him looking like that, I have to look away to hide the fact that I'm blushing."
    mc 1 c blush "\"A-A-A-Anyway, what's going on here?\""
    show j 1 c avoid at fdis, three with move:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    "Jun steps away from me, drying his eyes on the cuffs of his shirt-"
    "Wait, isn't it a little hot outside to be wearing long sleeved shirts? Ah, doesn't matter, not important now."
    stop music3 fadeout 2.5
    play music2 "music/BGM/The People Here.ogg" fadein 5.0
    j "\"I'm sorry I was late, I... got lost.\""
    "... What?"
    mc 1 c sigh "\"Wait, you're kidding, right?\""
    show j 1 c wince at fdis, fidget
    "Jun fidgets, looking down at the floor."
    j "\"N-No...\""
    mc 1 c sigh2 "\"How did you even manage to get lost?! You've been living here for almost a month!"
    "Hell, we've gone out together tons of times already!\""
    j "\"I-I know, it's just...\""
    mc 1 c "\"Just?\""
    show j 1 c blush at fdis
    "Jun turns his head to the side. I can notice that his cheeks are starting to get red again."
    j "\"Every other time we went out, I always bumped into someone on the way so I was never alone.\""
    j "\"This time when I got close to the station and I saw all those people...\""
    "Ah! Could it be..."
    mc 1 c shock "\"Did you get overwhelmed by the amount of people on the streets and ended up getting disoriented?\""
    "Jun nods meekly."
    "I sigh, slapping myself on the forehead."
    show j 1 c shockb at fdis
    j "\"Wah?\""
    "Jun jumps at the sound of my hand hitting my head."
    mc 1 c wince "\"Ugh, what was I thinking...\""
    "If I had just thought a little bit about it, it would have been obvious something like this was bound to happen."
    "As far as I know, Jun is the type to stay at home. He's already told us many times that he only goes out when he's with us."
    "And I've already seen how he is in the middle of a crowd. How exactly did I expect him to walk through one of the busiest streets in town on a Saturday?"
    "I put both of my hands in front of my face and bow."
    show j 1 c wince at fdis
    mc 1 c considerate "\"I'm sorry, Jun, I should have given our meeting place some more thought!\""
    j "\"N-No, not at all, it's not a problem. Please lift your head!\""
    "I do as I am told and I see Jun blushing again."
    show j 1 c avoid at fdis
    j "\"S-Sorry I ended up getting lost and I made you waste time. I know you don't like being forced to wait around.\""
    "Sheesh, was this idiot really worried about that? Set your priorities straight, moron, you were lost in the middle of a crowd."
    "Honestly, I can't help but smile when I hear this."
    show j 1 c watch at fdis
    if povFirstName == "Yuuichi":
        ay "\"Waah, Yuu-kun is smiling. He must be thinking of something dangerous.\""
    else:
        ay "\"Waah, [povFirstName]-kun is smiling. He must be thinking of something dangerous.\""
    "Class Rep gives me a pointed stare, still grinning, and blabbers out those words."
    mc 1 c sigh "\"I am not thinking anything, please don't say stuff like that even as a joke, Class Rep!\""
    "She laughs."
    ay "\"Oh, you're not thinking anything? So is it safe to say that head of yours is completely empty?\""
    "Guh... t-that's not what I meant either."
    ay "\"Oh, and by the way, I already asked you a few times but you seem to keep forgetting. Could you not call me \"Class Rep\" when we're not at school? I'm not overly fond of those stuffy titles.\""
    "Ah, that's true...\""
    mc 1 c wince "\"T-that's right. I'm sorry, I forgot, Cla... Ayako-san.\""
    "She crosses her arms in front of her chest, putting one of her hands to her cheek. Her eyes stare at me blankly."
    ay "\"Hmm... I'm not a fan of the \"-san\" either but I think this will have to do. Try not to forget it again.\""
    mc 1 c considerate "\"R-Right, I got it, Cla- I mean, Ayako-san!\""
    "She smiles and nods."
    ay "\"Well, since you're both here anyway, can I interest you in some sweets?\""
    mc 1 c considerate "\"Ah, there's no ne-\""
    show j 1 c think at fdis
    j "\"A-Actually!\""
    "Jun suddenly speaks up."
    "Oh, that's right. I got so swept up by Ayako-san's pace that I completely forgot Jun was here."
    "... I'm sorry, Jun. Your presence is so weak at times that I forget you exist."
    j "\"I was actually planning on stopping by later today, but since we're already here...\""
    "Ah, I see. It's true that we're going along with Jun's plan today so I suppose it'd make sense for him to want to come here."
    ay "\"Oh, I'm flattered that you'd planned to stop by our store. What can I get you?\""
    "I pull my wallet out of my pocket, already prepared to pay."
    mc 1 c smile "\"Sure, go ahead and pick whatever you'd like, Jun.\""
    show j 1 c pout at fdis
    "Eh, what is this? Did I do something wrong?"
    "Why is he pouting?"
    j "\"Don't just assume I'm not going to pay for myself!\""
    "Ah."
    mc 1 c considerate "\"Sorry sorry, I'm just so used to you not having the money that I kinda assumed...\""
    show j 1 c annoyed at fdis
    j "\"It's alright, I came prepared. I've been planning to ask you out for a couple weeks already so I've been saving up my allowance...\""
    "Glk?!" with hpunch
    "Ayako-san blinks in surprise a few times and chimes in without missing a beat."
    ay "\"Oh my, so this actually is a date after all?\""
    mc 1 c sigh "\"O-O-O-Of course not, r-right, Jun? There's no way this is a date, right?!\""
    show j 1 c watch at fdis
    "Jun cocks his head to the side, seemingly confused."
    j "\"A date? Why would you think this is a date?\""
    "T-this guy..."
    "Is he completely unaware of how the things he's doing and saying can be taken out of context?"
    mc 1 c sigh "\"You just sa-\""
    "Ayako-san grabs hold of my arm, stopping me mid-sentence. She pulls me close to the counter and whispers in my ear."
    ay "\"{size=-2}Don't explain. If Jun-kun becomes aware of the kind of innuendo his words just now had his head might explode.{/size}\""
    mc 1 c think "\"{size=-2}Ah, good thinking.{/size}\""
    "Phew, bullet dodged."
    j "\"What are you two talking about?\""
    mc 1 c considerate "\"N-Nothing. Hurry up, let's choose your sweets already, okay?!\""
    "Jun's gaze stays focused on me, making me worry that he might not buy our excuse."
    show j 1 c smile at fdis
    j "\"You're right. Let's see...\""
    "Phew, second bullet dodged..."
    mc 1 c "\"Oh, I forgot to ask. Jun, why were you planning to come over to the shop? The two times we came here it was just so you could take a breather from the crowd for a little while.\""
    show j 1 c watch at fdis
    "Jun answers me while absent-mindedly looking at the sweets on display."
    j "\"Oh, ever since you bought those sweets for me last time, I've been coming here almost every day and eating some. I guess I got hooked.\""
    ay "\"It's true. Jun-kun became quite the regular costumer lately.\""
    "... I thought you said you've been saving up."
    show j 1 c happy at fdis
    j "\"By the way, I guess I should thank you again for those sweets. My parents loved them too, my mom wanted to pay you back right away but she had to wait until she got this week's check. Here, she told me to give you your money back-\""
    "Jun handed me a couple of bills but I pushed them away."
    mc 1 c smile "\"It's fine. It was a gift, I don't need you to give me my money back.\""
    show j 1 c watch at fdis
    j "\"But...\""
    "I can already tell that he's going to insist so I quickly come up with a solution."
    mc 1 c smile "\"How about you spend this money on our outing today? Think of it as me treating you, it's something I would do anyway.\""
    show j 1 c think at fdis
    j "\"Hmm...\""
    "Oh come on! I know you're stubborn but you can't possibly disagree with this, can you?"
    show j 1 c happy at fdis
    j "\"Okay, I'll take you up on that!\""
    "Oh, thank God."
    "Ayako-san giggles."
    show j 1 c watch at fdis
    mc 1 c sigh "\"What is it this time? Are you gonna start teasing us again?\""
    "She smiles."
    ay "\"Oh no, I've already had my fill of fun for today, thank you. I was just thinking of how cute you two look together.\""
    "!" with hpunch
    mc 1 c wince "\"You just said you're not going to tease us anymore but how else am I supposed to take that comment?!\""
    "She giggles once more."
    "Honestly, she just opened with that because she knew I'd let my guard down didn't she?"
    "Devious little fox, certainly not helping curb the stereotype of them being cunning and scheming..."
    ay "\"Well, alright, I'll stop with the teasing for now.\""
    "I don't believe it for a second..."
    "Jun finishes picking two sweets that he wants and orders those."
    "Ayako-san immediately goes back to her customer service personality."
    ay "\"Should I pack them up in a cute little box?\""
    show j 1 c happy at fdis
    j "\"No, thanks. I'm gonna eat them here.\""
    "She nods and reaches out for a pair of tongs to take them out of the display."
    mc 1 c smile "\"Are you sure you don't want more? If it's a matter of money, I can pay.\""
    show j 1 c pout at fdis
    "Jun waves his hands trying to dismiss me."
    j "\"N-no no, there's no need. I'm trying to watch what I eat, that's all.\""
    "You know, I'd probably buy that if it weren't for the look on your face."
    show j 1 c watch at fdis
    if povFirstName == "Yuuichi":
        ay "\"Hmm, I remember you coming here yesterday and saying you'd blow your whole allowance if you could but that you wouldn't because you had to save up money to go out with Yuu-kun.\""
    else:
        ay "\"Hmm, I remember you coming here yesterday and saying you'd blow your whole allowance if you could but that you wouldn't because you had to save up money to go out with [povFirstName]-kun.\""
    "As always, Ayako doesn't miss a beat when she has a chance to cut into a conversation."
    show j 1 c cshockb at fdis, shake1
    j "\"Awawawa, Kitsunegawa-san, please don't tell him that!\""
    "And as always, she's an expert at pushing people's buttons."
    mc 1 c sigh "\"You're just telling me this so I'll decide to buy stuff for him and you'll make a bigger sale, aren't you?\""
    ay "\"Fufufu, I could be.\""
    "Jeez, why are all the people around me such weirdos."
    "I can't help but smile when they all act silly like this."
    mc 1 c wry "\"Come on, pick a little more stuff, I'll buy it for you. I insist.\""
    show j 1 c wince at fdis
    j "\"No, I don't want to eat too much. It's almost time for lunch anyway so I can't be filling up on sweets.\""
    mc 1 c judge "\"Hmmm...\""
    "I stare at him with an intense look, trying to see if he cracks under my gaze."
    j "\"W-What?\""
    mc 1 c smile "\"I'm trying to decide whether I believe you or not.\""
    show j 1 c pout at fdis
    "Jun stares back at me with the same intensity."
    "Satisfied, I decide to let it pass."
    "This is probably just an excuse but it's at least one I can live with."
    mc 1 c happy "\"Alright, then. Just those will suffice.\""
    show j 1 c happy at fdis
    "Jun smiles, nodding energetically."
    ay "\"Alright, I've already put them on a paper bag for you. Enjoy.\""
    "Man, she doesn't waste any time does she?"
    "Jun quickly hands her the payment."
    "She gets him his change is less than thirty seconds, dropping a bunch of coins on his palm."
    show j 1 c smile at fdis
    mc 1 c smile "\"Which ones did you pick?\""
    j "\"Bean mochi and matcha cake. Want some?\""
    mc 1 c wince "\"N-no thanks...\""
    "... I hate green tea so I'll stay away from anything that has so much as touched a matcha dessert."
    show j 1 c think at fdis
    j "\"Alright, then. How about we go while I eat?\""
    mc 1 c smile "\"Sure, do you have any place you'd like to go to?\""
    show j 1 c happy at fdis
    j "\"I have a few in mind.\""
    stop music2 fadeout 2.5
    scene Cafe
    show j 1 c smile at fdis, five
    with fade
    play music3 "music/BGM/In That Mood - Narr.ogg" fadein 5.0
    "After walking down the main avenue, window shopping for a bit {i}and{/i} calming Jun down through three crowd-induced panic attacks, he leads us into a big, very expensive looking Cafe."
    "My thoughts immediately go to whether he can pay for anything here."
    mc 1 c wince "\"Uhh... J-Jun? Maybe we should go someplace else...\""
    show j 1 c watch at fdis
    j "\"Huh? Why?\""
    "Seriously, how innocent can a person be?"
    "How does he not realize it?"
    "Oh boy, how do I tell someone that I think they're too poor to be somewhere?"
    show j 1 c think at fdis
    "Before I have time to come up with an answer, Jun expression shifts."
    j "\"Ah, could it be that you're worried about this place being expensive?\""
    "... He's more perceptive than I give him credit for."
    mc 1 c wince "\"W-Well... would you be angry if I said yes?\""
    show j 1 c happy at fdis
    j "\"Oh, don't worry about it. I researched this place beforehand and I already know how much their menu costs.\""
    show j 1 c think at fdis
    j "\"Of course, I won't be able to order anything expensive like a tart or a parfait, but I should be fine with a light snack and a coffee.\""
    "Huh... I have to admit, I didn't expect this level of forethought coming from Jun."
    "His reaction was the complete opposite of what I was expecting."
    "Then again, I think I might infantilize him a little too much."
    "It's easy to forget that he's one year older than me."
    "Actually, I still have a hard time believing that piece of information."
    show j 1 c shockb at fdis
    j "\"Wow, look, they even have a grand piano over here. I didn't see that in the pictures!\""
    "Jun dashes towards a big blue piano they have facing the windows."
    "It's also next to the counter so a waitress immediately notices Jun approaching it."
    "Waitress" "\"Hello, would you like some help to find some seats? We're full right now so you might have to wait a little but it shouldn't be more than five minutes.\""
    "A gazelle goes over to him with a smile on her face, giving Jun a courteous greeting."
    "Just like she said, the place is really packed."
    "Even I feel a little bit anxious being in here."
    "Jun, on the other hand, seems completely fixated on the piano."
    "The waitress notices his interest and turns towards the instrument."
    "Waitress" "\"Oh, you like it? I'll admit, it's a big draw for our customers. We even have a few kids who come over here just to bang on the keys.\""
    "Waitress" "\"It's actually a pretty expensive one, too. It's from-\""
    show j 1 c happy at fdis
    j "\"Steinway & Sons.\""
    "Jun mumbles out, cutting the waitress off and completing her sentence."
    "He seems to snap back into reality right afterwards and looks apologetic about it."
    show j 1 c cshock at fdis, shake1
    j "\"Wawawa, sorry sorry, I didn't mean to interrupt. My mind just kinda filled in the blank before I had time to think about it!\""
    "The gazelle, noticing his nervousness, chuckles softly."
    "Waitress" "\"Oh, don't worry about it. Did you read the brand logo on it before I had time to tell you?\""
    show j 1 c smile at fdis
    j "\"Oh, no. I've played on one of these before.\""
    "The waitress blinks a few times, then her lips part into a radiant smile."
    "Waitress" "\"Could it be that you know how to play the piano?\""
    show j 1 c happy at fdis
    "Jun nods energetically."
    "Waitress" "\"Oh wow, that's wonderful. I love the sound of the piano but I could never play it myself.\""
    "Waitress" "\"We actually offer a free dessert to any customer who plays a full song. Would you be interested?\""
    show j 1 c shockb at fdis
    "Jun's eyes immediately light up."
    j "\"Can I?!\""
    "The waitress smiles, winking at him."
    "Waitress" "\"Of course! Why don't you play a song while you wait for some seats to become vacant? I'll hold one for you if you're not finished before that.\""
    show j 1 c happyb at fdis
    j "\"Okay!\""
    "Huh... This was unexpected."
    "Although I won't complain about being able to watch him perform again. I just love seeing him play."
    "And I suppose it's not a bad deal for the business either. They get someone to play a song at a much cheaper rate than a decent artist would charge."
    "Although I think that with his skills, Jun could ask for a lot more than a single dessert."
    show j 1 c happy at fdis
    "He sits down in front of the piano and closes his eyes, taking deep breaths."
    "I can already see a few heads turning his way. Seems like the customers noticed him."
    stop music fadeout 5.0
    "I just hope he doesn't choke due to nerves."
    "... Then again, he did play at a much bigger venue just a few days ago."
    "No wait, but he did freak out that time."
    "Gaah, I'm just going around in circles with this logic. I'm making myself nervous instead!"
    stop music3 fadeout 2.5
    play music2 "music/BGM/The Meaning of Tears.ogg" fadein 5.0
    "But as soon as his fingers touch the keys, a calm and gentle song starts playing out of the piano."
    "The room that had been boisterous and full of noise up until a second ago becomes completely silent."
    "Jun's piano is the only thing that makes a sound."
    "No. His piano is the only thing {i}allowed{/i} to make a sound."
    "As soon as Jun starts playing, it is as if other sounds were prohibited from sounding."
    "While the melody isn't particularly fast nor does it seem very difficult, it touches the heart."
    "Soon, everyone in this cafe has eyes for no one other than Jun."
    "The piano is his stage, and he shines the brightest whenever he's playing it."
    "This is something I had already noticed before, but Jun turns into a completely different person when he plays."
    "While he's usually bright and cheerful, he can also be meek, shy and insecure."
    "But whenever he plays the piano, he has an honest, gentle smile on his face."
    "As if he were enjoying himself from the bottom of his heart."
    "Jun's smile, which is as beautiful as the melody he weaves, soon infects me. I am left grinning from ear to ear."
    "Before they've even noticed, Jun's music has enthralled all the customers in this cafe better than any words ever could."
    "At this moment alone, Jun is a star."
    "No one dares speak while he's playing. Even the staff seems completely stunned."
    "As the melody starts nearing its inevitable end, the people seem to realize they were completely paused up to now."
    "Little by little, they start to snap out of their daze. But every single one of them has a satisfied smile on their face."
    stop music2 fadeout 5.0
    show j 1 c wry at fdis
    "Once Jun's performance finally reaches an end, he lets out a sigh, opening his eyes and staring at the piano with affection."
    "He strokes the keys as if he were caressing someone very important to him."
    "The waitress from earlier comes back. Her expression is markedly different."
    "While I didn't for a second believe her previous smile was fake, the one she has on her face right now seems so much more genuine."
    "Waitress" "\"That... I don't even know what to say. Wow. That was beautiful. Thank you so much for playing.\""
    play sound "music/clapping.ogg"
    "The gazelle starts clapping and soon enough, all the other diners follow suit."
    show j 1 c shockb at fdis, jumping
    "It seems that only now did Jun notice all the attention his play was gathering."
    play music2 "music/BGM/In That Mood - Narr.ogg" fadein 5.0
    "As soon as he turns around and notices all the people staring at him, his face turns bright red."
    j "\"T-Thank you.\""
    "Damn it. I don't know if I've been enthralled by Jun's song as well, but the expression he has on his face right now is just lovely."
    "Waitress" "\"I actually feel a little bad. I wish I could give you more than just a dessert for that performance...\""
    "She puts a finger to her chin, staring off into space, seemingly lost in thought."
    "Waitress" "\"Oh, I know. Hang on a second.\""
    "The waitress leaves towards another table."
    "Then another one."
    "It seems that she's making rounds on the restaurant."
    mc 1 c curious "\"By the way, Jun, what song was that?\""
    show j 1 c happyb at fdis
    j "\"Oh, hehe, that one was...\""
    "He scratches the back of his head."
    show j 1 c smile at fdis
    j "\"That one was actually an original song I composed...\""
    mc 1 c shock "\"W-Wow! Really? It was insanely beautiful!\""
    show j 1 c happyb at fdis
    j "\"It's a little embarrassing playing one of my songs in public but I just felt like playing that one.\""
    mc 1 c shock "\"I didn't know you could compose too.\""
    show j 1 c pout at fdis
    j "\"What do you mean you didn't know? I told you I planned on becoming a composer. That's why I'm busting my ass to try and get into that school in Germany!\""
    "Ah, now that he mentions it, I think I remember him saying something like that a little while ago."
    "Sheesh, talk about having a bad memory."
    mc 1 c considerate "\"Sorry, I completely forgot about it. Still, I had never heard a song you composed before. It was so beautiful, I really have no words.\""
    show j 1 c happyb at fdis
    "And now he's smiling again."
    "He's so easy to disarm."
    "It's cute."
    j "\"N-Now you're just trying to flatter me, hehehe...\""
    "He's so bad at taking compliments."
    "... But then again, that's one of his charming qualities."
    "Damn, he's really humble to a fault."
    "It's such a breath of fresh air seeing someone at his level being so nice about it."
    "Most people at his level would be cocky jerks."
    show j 1 c smile at fdis
    "Waitress" "\"I'm back!\""
    "The waitress comes back with a glass jar filled with... money?"
    "She's grinning from ear to ear, seemingly very pleased with herself."
    "Waitress" "\"I didn't think it was fair that he'd only get a free dessert after a performance like that, so I asked my manager for permission to ask the customers for donations.\""
    "Waitress" "\"We actually got enough to pay for a full meal for two and then have some money leftover!\""
    show j 1 c shock at fdis
    j "\"W-What?\""
    "... W-Wow, honestly even I'm caught by surprise here."
    "When we turn to look at the diners, we see that many of them are looking up at Jun with big smiles on their faces."
    "Is this the power of music?"
    show j 1 c wince at fdis
    j "\"I-I don't know if I can't accept this. It's not like I wanted to get something out of it, I just did it because I wanted to play.\""
    "The waitress nods."
    "Waitress" "\"But these people decided to chip in because they really loved seeing you perform. Really. Most of the customers were ecstatic to put some money in, they thought you deserved to get something out of that performance!\""
    j "\"E-Even if you say that...\""
    "Waitress" "\"Come on, please! I even chipped in a little myself, I just really loved your playing. I don't think I've ever heard a prettier melody.\""
    "Waah, for someone like Jun who is not used to the attention, having all these people suddenly focusing on him and praising him must be a little overwhelming."
    show j 1 c happyb at fdis
    "Just as I'm afraid that Jun might start freaking out, he takes a deep breath and nods."
    j "\"I-If they're really sure about it, then...\""
    "As soon as Jun reaches for the jar, he glances over at the other people in the cafe."
    "Most of them are smiling and nodding at him, as if telling him \"It's okay to accept it, we want to give you this\"."
    "It's a scene I myself would never believe could happen if I weren't witnessing this."
    "And to be honest, I think no one deserves this as much as Jun does."
    "After a couple more minutes of wait, a table finally clears for us to sit down and eat."
    "During our entire stay at the cafe, we had a bunch of people coming over to our table to speak with Jun."
    "It was quite a weird experience seeing him become so beloved to so many strangers, but all of the people who watched him perform left the establishment with a smile on their face."
    "I never knew music could be this powerful."
    "Honestly, I feel as if I'm spewing lines straight out of a romance manga."
    stop music2 fadeout 3.0
    "Why is it that I always end up thinking this sort of stuff when I'm with him?"
    "It's a bit embarrassing for a guy my age to be romanticizing everyday life so much..."
    scene Station
    show j 1 c watch at fdis, five
    with fade
    play music "music/crowd01.ogg"
    "A little after lunch, we leave the cafe feeling quite pleased with ourselves."
    "The money that was given to Jun was enough to pay for both of our meals, including desserts, and there was still some leftover that the staff insisted Jun take with him."
    "I also insisted on paying my part but Jun absolutely refused."
    "\"This is for all that you've done for me, please accept it!\" he said."
    "Honestly, I kinda didn't want to but it was hard to refuse it."
    "I could tell that Jun really wanted to be able to treat me. And he was pretty happy when I accepted too."
    "Honestly, he's so pure that it's liable to bring me to tears."
    j "\"Is there any other place you'd like to go to, [povFirstName]-san?\""
    mc 1 c wince "\"H-Huh?\""
    "Jun's words snap me out of my daze and bring me back to Earth."
    "Jeez, I'm already spacing out in the middle of the day. That's not good."
    "Did he say something else and I didn't realize it because I wasn't paying attention?\""
    mc 1 c wince "\"I'm sorry, did you say something else?\""
    show j 1 c happy at fdis
    "You don't have to look so amused by my confusion..."
    j "\"Hehe, don't worry. You were looking kinda cute spacing around so I was just having fun watching you.\""
    "Wha-"
    "My cheeks suddenly feel incredibly hot."
    "T-That's a really embarrassing thing to say all of a sudden."
    mc 1 c avoidb "\"I-I-I see. Anyway, n-no, I don't really have any preferences. What about you?\""
    show j 1 c watch at fdis
    j "\"Hmm... let's see...\""
    "Jun starts humming a familiar song."
    "... Does this mean he has no idea and is trying to think of something?"
    "Honestly, didn't you plan this all beforehand? Or are you just winging it by this point?"
    show j 1 c shock at fdis
    j "\"I have no idea!\""
    show j 1 c gentle at fdis
    "You don't have to look so happy just because you figured it out."
    play sound "music/disappointment.ogg"
    "... I know you're sort of an airhead but at least try to think a little bit about stuff beforehand."
    mc 1 c sigh "\"Didn't you tell me you already knew where you wanted to go to today?\""
    show j 1 c watch at fdis
    "Jun looks ahead again."
    "At least the area we're walking through isn't very crowded right now."
    "Jun seems a lot more relaxed than he usually is out in public."
    "Maybe it's some lingering effect from his performance at the cafe?"
    j "\"Well... I know I want to go to the amusement park and I knew I wanted to eat at this cafe. Other than that, I haven't given it much thought.\""
    mc 1 c "\"If you're out of ideas then we could just go to the park now.\""
    "Jun shakes his head in negative."
    j "\"I don't want to go right now, it's still too early.\""
    show j 1 c think at fdis
    j "\"I mean, I know I said I wanted to go to the amusement park, but...\""
    show j 1 c happyb at fdis
    j "\"I think I'm enjoying the company more than I'd be enjoying the park so it doesn't really matter what we do.\""
    play sound "music/heartbeat.ogg"
    "!" with hpunch
    "\"Badoomp\"? Why did my heart just go \"badoomp\"?!"
    "Shit, my face feels so hot right now..."
    "D-Did my heart just skip a beat? Why is my heart skipping a beat?!"
    "Waaaah, what's this, why is my mind getting so hazy all of a sudden?!"
    "Deep breaths, deep breaths. Just take deep breaths!"
    "In, out. In, out."
    "..."
    show j 1 c watch at fdis:
        ease .2 zoom 1.5 xoffset -50 yoffset 80
    j "\"Are you alright, [povFirstName]-san?\""
    "Without me even noticing it, Jun had gotten a lot closer to me."
    "He was walking on the tip of his toes, looking me in the eyes with worry."
    j "\"Do you have a fever or something? Your face is looking really red.\""
    mc 1 c avoidb "\"I-I-I-I-I don't want to hear that sort of thing from you, your face was redder than a tomato back in the cafe!\""
    show j 1 c shock at fdis
    j "\"Eh?\""
    show j 1 c wince at fdis:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    j "\"I-I can't help it. Of course I'd get embarrassed in a situation like that. What do {i}you{/i} have to be embarrassed about?\""
    "... I'm asking myself the same thing."
    mc 1 c avoidb "\"A-Anyway, let's just think of another place to go so we can kill time before we head for the amusement park!\""
    "Change the subject, change the subject!"
    show j 1 c watch at fdis
    j "\"Sounds good. Do you have any suggestions?\""
    "... Jeez, this guy can switch gears so fast it gives me a headache trying to keep track of his mood."
    "Well, at least he's not up in my face anymore..."
    "Wawawawa, my face is getting hot again."
    "Think of something else, think of something else!"
    "Why am {i}I{/i} getting nervous? I've never been the type to get nervous before!"
    mc 1 c wince "\"H-How about we go to...\""
    "... Crap, I'm drawing a blank!"
    "W-what did Jun like other than playing piano? Err- let's see, there's videogames! We could go to a videogame store!"
    "Oh, there's also books. I remember him saying that he liked books!"
    "Wait! That's it!"
    mc 1 c shock "\"Oh, I have an idea!\""
    "Jun looks up at me with expectation."
    "I just remembered a piece of information that gave me the perfect clue as to what we should do next."
    "Hehehe, bless you, memory."
    mc 1 c happy "\"How about we go to a bookstore?\""
    show j 1 c think at fdis
    j "\"A bookstore? Why a bookstore? That's not a very fun place to go to.\""
    "I nod."
    mc 1 c smile "\"Yeah, sure. But I know you like books, right?\""
    j "\"Well, yeah. I do but won't you be bored in there?\""
    "I shake my head in negative."
    mc 1 c smile "\"I might not be the most avid reader but I still enjoy books every now and then if they're really interesting.\""
    mc 1 c happy "\"But that's not the only reason I suggested that.\""
    "Once again, Jun looks at me in confusion."
    mc 1 c smile "\"That money you have leftover from lunch. I'm pretty sure it'd be enough for you to buy a book. And I remember you telling me that this trilogy you really like just had its' last book coming out a couple weeks ago.\""
    show j 1 c shock at fdis
    j "\"Ah, you're right!\""
    show j 1 c gentle at fdis
    j "\"I honestly didn't expect you to remember that. I was so sure you weren't even listening to me when I was talking about the books!\""
    mc 1 c wince "\"W-Why would you think that?\""
    show j 1 c think at fdis
    j "\"Well, I got the feeling you were just looking for random topics of conversation to calm me down when I was freaking out about the competition.\""
    "..."
    "He's {i}much{/i} more perceptive than I give him credit for."
    show j 1 c happy at fdis
    j "\"That really sounds like I great idea, I hadn't even thought of using the money for that. Thank you so much, [povFirstName]-san!\""
    "W-well, I didn't really do much, I just gave him a suggestion."
    "But it feels kinda good having Jun be so happy with me."
    "I have a sudden urge to fawn over Jun like a child."
    "Gah, control yourself, he's older than you and he hates being treated like a kid!"
    "... Even though he acts like one most of the time."
    j "\"Alright, off to the nearest bookstore we go!\""
    mc 1 c happy "\"Aye aye!\""
    "Heh, but still, I can't help but be swallowed up by his carefree pace whenever I'm with him."
    "Hanging out with Jun is so much fun!"
    stop music fadeout 2.5
    scene Bookstore
    show j 1 c smile at fdis, five
    with fade
    play music2 "music/BGM/Summer Day.ogg" fadein 5.0
    "Stepping into the bookstore, I can't help but notice the scent of alcohol tickling my nose."
    "It's not a smell I would usually associate with a place like this but when I look at the counter, I see a clerk wiping it with a cloth."
    "Ah, so that's it..."
    "The air inside is dry and a little dusty. The sun's rays entering through the window illuminate and reveal the particles of dust floating on the air."
    "For some reason, my nose starts to itch a little bit."
    j "\"Haah, they have a pretty good selection over here.\""
    "Jun walked over to a pile of books and started browsing them."
    "While I fully expected him to be interested in the manga section, he actually went for real books."
    "Huh... I know it's kinda mean to think something like this but up until I saw it with my own eyes, I had a hard time believing that Jun actually read real books."
    "I really am a sucky friend, huh..."
    mc 1 c smile "\"What kinds of books are you looking at over there?\""
    play sound "music/pageflip.ogg"
    show j 1 c watch at fdis
    "He was casually flipping the pages of a very big book as if it were nothing."
    j "\"This one is a fantasy book I had been interested in reading for a while but I never knew if it'd be a good fit.\""
    mc 1 c curious "\"Oh, why not?\""
    "Jun puts it back on the shelf and picks up another one."
    show j 1 c think at fdis
    j "\"I hear that the story is very complicated and political, I'm afraid I'd have a hard time following it.\""
    show j 1 c watch at fdis
    j "\"I tend to prefer simpler books. High Fantasy and the likes. When things get too detailed I tend to lose myself in the plot.\""
    mc 1 c smile "\"That's a surprisingly valid point coming from you.\""
    show j 1 c pout at fdis
    "Jun sets the book down and looks up at me in annoyance."
    j "\"Why \"surprisingly\"?\""
    mc 1 c shock "\"?!{nw}\"" with hpunch
    mc 1 c fsmile "\"?!{fast} I-I mean that I honestly didn't expect you to have trouble with those books. I really thought you'd blaze through them no problem!\""
    show j 1 c watch at fdis
    j "\"Ah, is that so?\""
    "S-Safe!"
    "I really have to watch what the hell I say. I don't want to end up angering him by accident."
    "... Though I think the main problem is the skewed opinion I have of him, isn't it..."
    show j 1 c think at fdis
    j "\"Hmm, I don't see the book I'm looking for. Maybe they'll have a copy of it at the back of the store?\""
    show j 1 c wince at fdis
    j "\"It's also a new release of a pretty popular book so they might have run out too... That would suck, I hope it's not the case.\""
    show j 1 c watch at fdis
    "Jun walks to the clerk that was wiping the counter just a little while ago."
    j "\"Excuse me?\""
    "The clerk, a lynx, is wearing a pair of earbuds. He notices Jun approaching and takes them off."
    "Clerk" "\"Yes? How can I help you?\""
    j "\"Do you still have any copies of the book \"The Red Keep\" that was released last week?\""
    "Clerk" "\"Hmm... that's the one written by that foreign guy, what was his name again... Paul White?\""
    "Jun nods."
    "Clerk" "\"Hang on just a second, let me check on the system.\""
    "The lynx starts typing something on his computer."
    "Clerk" "\"It looks like we have one last copy left-\""
    show j 1 c happy at fdis
    j "\"Yay! I'll take it!\""
    "Clerk" "\"But it's at our other store... on the other side of town.\""
    show j 1 c wince at fdis
    j "\"Whaaa, no way. How far is it to the other store?\""
    "Clerk" "\"You'd have to take at least three different trains and a bus.\""
    show j 1 c wince at fdis, shake1
    j "\"N-no way!\""
    "Jun's shoulders immediately sag, his whole mood deflating."
    j "\"Why does this sort of thing always happen to me?\""
    mc 1 c "\"Excuse me, is there any way you could have this book shipped to this store? We live close by so going to the other one would be incredibly inconvenient.\""
    "I decide to intervene to look for a way to have this dealt with."
    "It stands to reason that they'd be willing to sell the book and so could have it shipped right?"
    "The awkward look on the lynx's face tells me otherwise."
    "Clerk" "\"Well...\""
    "He scratched the back of his neck."
    "Clerk" "\"It's true that we could but I honestly wouldn't recommend it. Our store charges a big fee on shipping. It'd be way cheaper for you to just go there yourself.\""
    mc 1 c curious "\"How much is it with the shipping?\""
    "Clerk" "\"Let's see... ¥3625 with shipping.\""
    j "\"Waaah, that's double the price of the book by itself, I don't have that much le-\""
    mc 1 c smile "\"We'll take it, please have it ordered. When can we pick it up?\""
    show j 1 c shock at fdis
    "I immediately pull out my wallet and grab a couple bills inside."
    j "\"[povFirstName]-san?! W-What are you doing?\""
    mc 1 c "\"I'm buying the book for you, of course. What does it look like I'm doing?\""
    show j 1 c wince at fdis
    j "\"B-But I can't have you doing that for me!\""
    "Tch, this guy can be so stubborn at the most annoying moments..."
    "I already know how he is, trying to convince him to let me give this as a gift would be a long and, frankly, annoying process."
    "In this case, how about I go with this..."
    stop music2 fadeout 5.0
    mc 1 c "\"Don't misunderstand, I'm not doing this for you.\""
    show j 1 c shock at fdis
    j "\"E-Eh? Y-You're not?\""
    mc 1 c annoyed "\"I'm going to be spending the rest of the day with you and I know you're gonna be sulking if you don't get this book. Dealing with that would be annoying so this is as much for my own good as anything else.\""
    "There, how about this?!"
    "Jun stands there completely shocked, his mouth open wide."
    "Clerk" "\"Waah, that's kinda cold...\""
    mc 1 c wince "\"T-This is none of your business!\""
    "Jeez, I feel like an asshole for saying something like that."
    "He's probably gonna be mad at me because of it right?"
    "If he at least accepts the book then I'm going to be fine with it."
    show j 1 c blank at fdis
    j "\"... I understand. I'll accept it then.\""
    mc 1 c wince "\"Y-You will?\""
    "You mean that actually worked? Holy shit, I didn't expect it to work!"
    mc 1 c considerate "\"Alright, here's the money then. When can we come back to get it?\""
    "The clerk takes a while to respond as he has to be snapped out of his own daze."
    "He takes the money from my hand and deposits it in his register."
    "He then types a few things on his computer."
    "Clerk" "\"Alright, I've placed the order. They're going to send the book over here. You can come back to get it at the end of the business day or tomorrow morning if you'd like. We're open from 8 to 11 AM on Sundays.\""
    "I nod and thank him for his assistance, turning back around to face Jun."
    "I wonder if he's mad at me for what I said."
    mc 1 c considerate "\"Do you want to buy anything else? I ended up buying the book for you so I suppose you still have some leftover money to spend.\""
    "Jun shakes his head sideways."
    j "\"No thanks, I think I'll use the money at the park.\""
    j "\"Or... is there anything you'd like me to buy for you?\""
    "I make a dismissive gesture with my hand."
    mc 1 c considerate "\"Don't worry about it, I don't usually spend much money so I have quite a bit saved up. If there's anything I want I can buy it for myself no problem.\""
    j "\"I see...\""
    "Jun looks down at the ground."
    mc 1 c wince "\"Well, if there's nothing else you want to check out here then how about we go someplace else?\""
    "Didn't we come here to pass some time in the first place? Why are you acting as if you don't want to check anything now?\""
    "Jun nods."
    scene Station
    show j 1 c blank at fdis, five
    with fade
    play music "music/crowd01.ogg" fadein 5.0
    "We walk around the streets for a few more minutes, browsing the products on the windows and checking out a couple of shops."
    "But Jun remains silent the whole time."
    "He's definitely mad at me for what I said in the bookstore isn't he?"
    mc 1 c wince "\"H-Hey, Jun...-kun? Are you alright?\""
    j "\"Hmm...\""
    "Instead of giving me an actual answer, Jun just makes some random noise."
    mc 1 c wince "\"Y-You're mad at me for what I said in the store aren't you? I-I'm sorry, I guess I really was out of line.\""
    "Now I play the part of repentant friend who is sorry for having been an ass and everything should be okay."
    "Instead of accepting my apology, Jun merely sighs as if this were somehow some sort of annoyance to him."
    j "\"You don't have to do this, [povFirstName]-san...\""
    mc 1 c wince "\"H-Huh? What are you talking about?\""
    j "\"I've been with you almost every day since I met you. By this point I already know you're not the kind of person who'd say something like that. You were just acting like I was annoying you so I'd take the gift.\""
    "..."
    mc 1 c shock "\"That's... how did you even know that?\""
    show j 1 c wince at fdis
    j "\"Oh please, you might be brash and snide at times but you're never plain rude. You're still one of the most kind-hearted people I know.\""
    play sound "music/heartbeat.ogg"
    "!"
    "Shit, I had to look away just now."
    "How can he say something like that without being even a little embarrassed."
    "... My chest feels tight."
    "What is this?"
    show j 1 c watch at fdis
    j "\"You alright, [povFirstName]-san?\""
    mc 1 c considerate "\"A-ah yeah yeah, I'm fine.\""
    "Oh, this won't do. I was so distracted that I ended up making him worry."
    "Still, Jun just feels a little different today..."
    "Or is it because I've never really paid attention before? He's been much more perceptive than usual."
    mc 1 c curious "\"I guess I got caught with that one, huh? Just out of curiosity, why did you accept the book if you knew what I was doing?\""
    show j 1 c wry at fdis
    j "\"Any normal person would assume that I'd get mad after being talked to like that so you had to have thought of that when you did what you did.\""
    show j 1 c considerate at fdis
    j "\"If you were willing to have me get mad at you just for the sake of making me accept a gift then... If you were willing to go that far for it I just felt like I had to accept.\""
    "Like always, I cannot follow his thought process at all."
    "Most of the time he acts like he doesn't put any thought into what he does."
    "Hell, not long ago he admitted to winging our whole meeting after telling me he had already planned the whole thing out."
    "It's really hard to keep up with his pace at times."
    mc 1 c considerate "\"Hehe, I guess this means I've been defeated.\""
    show j 1 c wry at fdis
    j "\"Was I overthinking it?\""
    mc 1 c think "\"No no, not at all. You definitely managed to figure out my whole plan perfectly. I'm honestly surprised with how much you know me.\""
    show j 1 c considerate
    j "\"Well, of course. I'm well aware that I'm just a newcomer at you guys' group. You've all been very kind to include me in most of your meetings and hang-outs but the reality is that I'm not yet part of the group dynamic.\""
    j "\"It's easy for me to get left out of conversations because I just don't know enough about you guys to participate. So whenever that happens, I just make sure to observe you all to try and learn more about you.\""
    mc 1 c shock "\"W-Wow, I didn't know you had given it this much thought.\""
    "Now that I think of it, I guess Jun is kinda similar to Shoichi in a few aspects."
    "The both of them are the type of people who try to always be considerate."
    "I always thought Jun was acting very carefree around us but could it be that he was actually keeping an eye on us and matching our pace?"
    "Ugh... thinking about this sort of stuff is confusing and it makes my head hurt."
    mc 1 c "\"By the way, if you knew what I was doing, why did you get so silent? I've spent the past half hour worrying about you being mad at me.\""
    show j 1 c blush at fdis
    j "\"Hmm, that's...\""
    "Jun looks away. Still, I can tell from the tip of his ears that he's blushing."
    j "\"I've never really had anyone go to such lengths to do something nice for me so I felt a little awkward. I've... actually been thinking of a way that I could reciprocate the gesture since we left the bookstore.\""
    "Just like I thought, Jun really is a good person."
    "He's so adorable when he's like this, I just feel like I can't leave him alone."
    "For some reason, I really have fun fussing over him and taking care of him."
    mc 1 c smile "\"How about we go get some crepes? It'll be my treat!\""
    show j 1 c wince at fdis
    j "\"Ahh, I-I'll pass... {size=-2}I ate too many sweets at the cafe...{/size}\""
    mc 1 c "\"Is that so? You look fine to me.\""
    show j 1 c sigh at fdis
    j "\"It's not like I'm feeling bad or anything. My stomach just feels a little bit bloated...\""
    mc 1 c curious "\"Hmm...\""
    "His shirt does look a bit tighter than usual."
    "Which reminds me..."
    mc 1 c curious "\"Hey, Jun, isn't it a little too hot outside today for you to be wearing a long sleeved shirt?\""
    mc 1 c think "\"Come to think of it, I've only ever seen you wearing long sleeves.\""
    show j 1 c wince at fdis
    j "\"A-Ah, that's... I just feel more comfortable with these. I-I don't really like having my arms uncovered, that's all.\""
    mc 1 c sigh "\"But you're sweating!\""
    show j 1 c shock at fdis
    j "\"A-Am I?\""
    "I reached out and tug at his belly area. Sure enough, his shirt is wet.."
    show j 1 c shockb at fdis, shake1
    j "\"W-Wah! [povFirstName]-san, please don't do this all of a sudden!\""
    mc 1 c sigh "\"What? I just pinched your shirt, I didn't touch you or anything.\""
    show j 1 c wince at fdis
    j "\"I-It's not the touching I mind, you just really surprised me. I thought you were going to lift up my shirt!\""
    "... Why would I do that?"
    mc 1 c sigh "\"You have some crazy ideas sometimes, Jun.\""
    j "\"Uuuhhh...\""
    "Well, it's not like I mind."
    "It's this uniqueness of his that makes it fun to hang out with him anyway."
    mc 1 c think "\"Hmm... I still don't like how much you're sweating. Maybe we should go someplace to have cold drinks? Preferably one that's air-conditioned.\""
    show j 1 c watch at fdis
    j "\"Ah! ... I wouldn't say no to that.\""
    "Bingo. This means that he wanted to do that but didn't want to ask."
    "For someone so random you sure can be easy to read at times."
    stop music fadeout 2.5
    scene IceCream
    show j 1 c watch at fdis, five
    with fade
    play music2 "music/BGM/Hanging Out.ogg" fadein 5.0
    "Luckily enough, there's an ice cream shop nearby."
    "I used to come here sometimes, especially in the Summer."
    "Most of the time, it was when I was hanging out with Shoichi and Saya."
    "Boy, that was a while ago. I didn't even know Kei-kun back then."
    mc 1 c smile "\"Feel free to get whatever you want, it's my treat.\""
    show j 1 c shock at fdis
    j "\"Wha- no, I can't accept that.\""
    mc 1 c happy "\"Come on, pretty please? I'm the one who insisted on coming over so at least let me treat you.\""
    show j 1 c pout at fdis
    j "\"... I feel like you end up treating me a lot.\""
    mc 1 c smile "\"That's because I worry about you. Take this as a sign that you're my friend.\""
    show j 1 c bored at fdis
    j "\"Somehow I don't remember ever seeing you treat anyone else though...\""
    "Jeez, he's still trying to squirm his way out of it."
    mc 1 c smile "\"All of my other friends have more money than I do, why should I treat them?\""
    show j 1 c wince at fdis
    j "\"... I suppose that's true in a sense. But even though you guys have more money than I do, I still want to treat you all... I just don't have the money to.\""
    "I give him a pat on the back."
    mc 1 c smile "\"There there, don't worry so much about it. If you really want to please me then just take my offer and let me treat you okay?\""
    "I even make sure to wink at him as I say this."
    "I'll pile on the encouragement to make him accept it!"
    "... Now that I think of it, I don't think I've ever been this adamant about wanting to take care of someone."
    "Not even my brother."
    "... Aki, I'm so sorry. Big bro promises he'll do something nice for you when he comes home..."
    show j 1 c blush at fdis
    j "\"I-I guess I'll take you up on your offer then. Do you mind if I have a milkshake?\""
    mc 1 c happy "\"Of course not. I told you to have whatever you'd like.\""
    scene IceCream
    show j 1 c happy at fdis, five
    with fade
    "In the end, Jun and I both ordered milkshakes."
    "He got a strawberry shake and I got a vanilla shake."
    "To be honest, the milkshake here isn't as good as I remembered."
    "But Jun..."
    j "\"{cps=60}Waaah, this is amazing! I only ever had milkshakes a couple of times before and they were all from super cheap burger joints, this one is so much better than them! And oh, they actually put some frosting on top of it and they even added sprinkles and-{/cps}\""
    "... I'm honestly having trouble keeping up with him because of how fast he's talking."
    "I guess giving a sugary drink to an already hyperactive person probably wasn't the best idea in the world in hindsight."
    mc 1 c considerate "\"H-Hey, Jun, by the way, do you have any idea what you want to do at the amusement park?\""
    mc 1 c smile "\"I know, how about we go on the roller coaster?! Or the drop tower? I hear they even have a haunted house!\""
    "Not so subtle attempt to change the subject."
    "Let's see if it pays off."
    show j 1 c wince at fdis
    j "\"U-Uh... those are... perfectly acceptable ideas, I guess.\""
    "Aaaand they don't seem to have been well received."
    mc 1 c "\"What's wrong? You don't like them?\""
    j "\"W-Well, it's not that I don't really like them...\""
    show j 1 c wry at fdis
    j "\"Sorry, I'm just not really good at dealing with stuff that makes your heart race... I'm no adrenaline junkie.\""
    mc 1 c sad "\"Aww, but those are the best rides!\""
    show j 1 c considerate at fdis
    j "\"You can still go, I'd just rather not go with...\""
    "Ah, shit, I didn't mean to make him feel bad."
    mc 1 c considerate "\"No no no, don't worry about it, really. I don't really need to go on those. What sort of attractions did you want to visit?\""
    show j 1 c think at fdis
    j "\"Well... I was thinking of going on stuff like the carousel or the bumper cars. You know, tamer stuff.\""
    "... I like to think of those as the {i}boring{/i} stuff but I suppose different people have different tastes."
    mc 1 c considerate "\"Sure, we can go on those no problem!\""
    show j 1 c smile at fdis
    j "\"Thank you, [povFirstName]-san. You're being really nice to me.\""
    mc 1 c smile "\"Well... I'm nice to everyone.\""
    "Jun chuckles, taking another sip from his milkshake."
    j "\"True, but you're usually also snarky or sarcastic with people while you're helping them. I don't recall you ever doing that to me.\""
    "... Huh, that's actually true."
    "If I've ever been snarky to Jun, I don't really remember it."
    "I wonder why that is."
    mc 1 c think "\"I hadn't really thought about that before... Hmm, maybe I should start treating you like that so no one can accuse me of playing favorites!"
    "I say so with a devious smile on my face."
    show j 1 c considerate at fdis
    j "\"N-No there's no need, I prefer it like this!\""
    mc 1 c happy "\"Haha. Alright then, I'll continue to play favorites with you.\""
    show j 1 c happy at fdis
    j "\"Okay!\""
    "Heh, he's so easy to please."
    show j 1 c watch at fdis
    j "\"By the way, what time is it right now? I don't want us to be too late to the amusement park.\""
    mc 1 c curious "\"Hold on, let me check.\""
    play sound "music/phonebeep.ogg"
    mc 1 c smile "\"It's almost 3PM. Are you ready to head out to the park?\""
    show j 1 c gentle at fdis
    "He nods excitedly."
    "Alright, gotta make sure to pay for our tab before we leave."
    stop music2 fadeout 2.5
    scene Amusement with fade
    play music3 "music/BGM/Spring Classroom.ogg" fadein 5.0
    "We were happy to find out that the park was actually holding a flash sale for their tickets and we both managed to get in with half price."
    "Or we would be happy about it, but..."
    show j 1 c flustert at fdis, fiveh with dissolve
    j "\"Uuuu...\""
    "Jun is moping around."
    mc 1 c sigh2 "\"How could you not have known that you need to buy tickets to go on the rides?!\""
    j "\"I thought you only had to pay for the entrance and that was it!\""
    "So in the end, he only saved up enough money to pay for the entrance and none to actually go on any rides."
    "And because I don't tend to walk with much money to begin with, all the extra money I brought was used to buy the milkshakes."
    "So between the two of us, considering how much money we saved on the entrance and the leftover money Jun still had from the cafe, we were able to buy eight tickets."
    "Seven of those were bought by me."
    mc 1 c smile "\"Alright, this means we can go on four rides together. Here, take these three tickets.\""
    "I hand him my extra tickets so we'll both have an equal number."
    show j 1 c wince at fdis
    j "\"N-no, I can't accept it. You're the one who bought t-\""
    mc 1 c scorn "\"What the hell would I use these for if you're not going with me on the rides, dumbass? Just take the damn tickets!\""
    show j 1 c fluster at fdis, jumping, shake1
    j "\"Awawawa, y-yes!\""
    "It seems that Jun responds well to tough love. I'll make sure to remember that."
    mc 1 c sigh "\"Honestly, if you had done some proper research beforehand we could be going on a lot more rides.\""
    show j 1 c wince at fdis
    j "\"W-Why are you criticizing me about it? If it weren't for the flash sale you'd only have been able to buy four tickets anyway...\""
    mc 1 c "\"And you would have been able to buy zero. See how well that would have worked out?!\""
    j "\"Uhh...\""
    "And he's moping around again."
    "Hmm... maybe I should dial back on the tough love back a little bit."
    mc 1 c think "\"Alright, I guess this means we have to pick and choose what rides we go on. If we're excluding the ones you don't like, it doesn't really leave us with many choices.\""
    "And because the carnival game stalls only accept money instead of tickets, we can't go on those."
    show j 1 c considerate at fdis
    j "\"[povFirstName]-san, how about you decide what rides we go on?\""
    mc 1 c curious "\"Huh? Me? Why me?\""
    j "\"Well...\""
    show j 1 c avoid at fdis
    "Jun starts fidgeting in his spot, looking away from for me a while."
    j "\"I feel bad about not bringing extra money and then having you buy tickets for me so I want you to at least choose the ones you'd have the most fun on.\""
    mc 1 c smile "\"Oh, is that so? Does that mean we can go on the rollercoaster?\""
    show j 1 c wince at fdis
    "Jun immediately freezes up at the mention of it."
    j "\"S-Sure, if you want to.\""
    "You're a terrible liar."
    "Hmm, let's see. Jun said he doesn't really like thrill rides so I suppose we should stick to the tamer ones."
    "I don't remember them having all that many in the first place. Guess we don't really have many choices to choose from."
    "I'll just make sure to suggest ones that he can enjoy... and that I can stand being on."
    $ rides = 0
    $ bumper = False
    $ carousel = False
    $ teacups = False
    $ tunnel = False
    $ train = False
    label ride:
        if rides >= 3:
            stop music3 fadeout 2.5
            play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
            show j 1 c shock at fdis
            j "\"Oh!\""
            mc 1 c shock "\"Waah!\"" with hpunch
            "Jun literally yells out as I am thinking of our next ride, completely catching me off-guard and making me yelp."
            show j 1 c wince at fdis
            j "\"Hey, [povFirstName]-san, you shouldn't be so loud in public. It'll make other people think you're weird...\""
            mc 1 c annoyed "\"You're the last person I want to hear that from!\"" with hpunch
            j "\"What's that supposed to mean?\""
            "... How can someone lack so much self awareness?"
            "I sigh, rubbing the bridge of my nose to soothe myself."
            mc 1 c sigh "\"Nothing. It means nothing... Anyway, why did you just suddenly yell out like that?\""
            show j 1 c happy at fdis
            j "\"Oh, right. I had an idea!\""
            mc 1 c "\"An idea? What idea?\""
            "Jun starts rummaging through his pockets and pulls out what looks like a piece of paper, shoving it against my face."
            j "\"Tcharam!\""
            mc 1 c wince "\"T-Tcharam?\""
            "Ignoring the weird sound effect he just tried to make, I grab the piece of paper he's extended to me and hold it a little farther away from my eyes so I can see it better."
            "Wait, this is..."
            mc 1 c curious "\"... A photo?\""
            j "\"Yeah, look how pretty it is! It's actually a photo of the night view from a ferris wheel!\""
            mc 1 c "\"... And this photo is supposed to mean something to me?\""
            show j 1 c smile at fdis
            j "\"Well, it's just that we only have one ticket left each and I suddenly remembered this!\""
            show j 1 c happy at fdis
            j "\"Actually, I had wanted to go on the ferris wheel from the beginning but I guess I was having so much fun that I forgot until now, hehehe.\""
            "A ferris wheel huh? That certainly does sound like it could be fun."
            mc 1 c smile "\"It's almost night too so we could possibly get a similar view from it.\""
            show j 1 c shock at fdis
            j "\"Wait, it is?\""
            mc 1 c sigh "\"You didn't notice the sky getting darker?!\"" with hpunch
            j "\"Huh? It has?\""
            "Jun looks up at the sky."
            scene SkyE with fade
            j 1 c shock "\"Waaah, it's true. The sun's already setting!\""
            mc 1 c smile "\"Yeah. It won't be long before the stars come out. Possibly just twenty minutes or so.\""
            j 1 c happy "\"That's great then, we get to go on the ferris wheel under the moon and stars? That's so cool!\""
            mc 1 c "\"Is it really that cool?\""
            "Jun nods excitedly."
            j 1 c happy "\"Yeah it is. It's awesome!\""
            mc 1 c wince "\"I-If you say so.\""
            "I don't have anything against ferris wheels but I never really found them that interesting to begin with."
            mc 1 c smile "\"Well, if you want to go then I guess this is our next stop then.\""
            "At least now I don't have to keep wracking my brain looking for ideas of rides we can go on that would please him."
            "So, you know, double win."
            j 1 c happy "\"Let's go get in line!\""
            "Without giving me time to react, Jun starts tugging on my arm and dragging me away."
            mc 1 c shock "\"Wha- Hey- Come on- J-Jun, you don't even know where the line is!\""
            stop music2 fadeout 5.0
            j 1 c happy "\"It's alright, we'll certainly find our way!\""
            "N-Not this again!"
            "This wouldn't be the first time I've heard those words and ended up getting lost..."
            jump Ferris
        else:
            menu:
                "Bumper Cars" if bumper == False:
                    $ rides += 1
                    $ bumper = True
                    "Well, I think out of the ones we can choose, this is probably the most exciting one."
                    "I highly doubt anyone could ever classify this as an \"exciting\" ride but at least it's not a boring one."
                    mc 1 c smile "\"Hey, Jun, how about we go on the bumper cars? I remember you mentioning wanting to go on that ride.\""
                    show j 1 c watch at fdis
                    "His ears perk up at my suggestion."
                    j "\"Yeah I did. But are you sure you'd be okay with it?\""
                    mc 1 c happy "\"Why wouldn't I be, you idiot? It's probably the most exciting ride we could go on without freaking you out.\""
                    show j 1 c wince at fdis
                    j "\"Guh, so you really are going to avoid the ones you want because of me...\""
                    "Oh come on, {i}that's{/i} what he took from what I just said?"
                    "He can be so annoying sometimes."
                    mc 1 c "\"Yeah I am, it wouldn't be much fun if I were to go on a ride with you and I had to hold your hand while you freak out would it?\'"
                    j "\"Uuh... I guess you're right.\""
                    mc 1 c sigh "\"You {i}guess{/i} I'm right? Last time you clung to me while freaking out I nearly had to amputate my arm.\""
                    j "\"Now you're just exaggerating.\""
                    mc 1 c "\"There was no blood flow!\""
                    show j 1 c think at fdis
                    j "\"Anyway, should we go?\""
                    "... He just totally ignored what I said didn't he?"
                    scene Bumper with fade
                    "It doesn't take much walking around to reach the line for the bumper cars."
                    mc 1 c shock "\"Wooow, the line looks pretty long right now.\""
                    show j 1 c pout at fdis, fiveh with dissolve
                    j "\"How long do you think it's gonna take?\""
                    mc 1 c "\"A while.\""
                    show j 1 c annoyed at fdis
                    j "\"... You didn't even bother trying to think of it did you?\""
                    mc 1 c think "\"Neither did you so don't try to force this on me!\""
                    show j 1 c happy at fdis
                    "Jun smiles, taking a step to join the waiting line."
                    j "\"Well, nothing we can do but wait, I suppose.\""
                    show j 1 c think at fdis
                    j "\"Is it always like this in amusement parks?\""
                    mc 1 c wince "\"Have you really never gone to an amusement park before? Not ever?\""
                    show j 1 c watch at fdis
                    "Jun shakes his head sideways in negative, putting his arms behind his back and rocking his body back and forth at a slow, steady pace."
                    j "\"My parents always told me they were too busy to take me, even when it was obvious they weren't.\""
                    show j 1 c watch at fdis
                    j "\"When I was a kid, I'd get really upset about it, but...\""
                    show j 1 c considerate at fdis
                    j "\"After I started growing up, I began to notice the look on their face every time they had to refuse me. They weren't doing it because they were busy.\""
                    j "\"They just didn't have the money.\""
                    "Damn, that's heartbreaking..."
                    "I feel a sudden need to buy him something nice."
                    mc 1 c think "\"Well, to answer your question, the bigger parks tend to have bigger lines since they're also a lot more popular.\""
                    mc 1 c curious "\"This isn't the biggest park in the prefecture but it's the closest to where we live.\""
                    show j 1 c watch at fdis
                    j "\"Hoo, that's interesting. I didn't even know there were other parks.\""
                    mc 1 c "\"Really, how come?\""
                    mc 1 c think "\"Even if you were living away until a while back, your family is still from this town aren't they?\""
                    show j 1 c smile at fdis
                    j "\"Yeah, they actually still live in my childhood home. It's just that I had to be transfered to a school on the other side of the country when I was twelve.\""
                    j "\"It was actually a boarding school.\""
                    mc 1 c curious "\"Oh, you mean a music academy like the one you're trying to get into next year?\""
                    show j 1 c wry at fdis
                    j "\"Something like that, yeah.\""
                    "The line moves sixteen people at a time. It's actually going much faster than I thought, changing players every eight minutes."
                    "After the line moves once, we're already in place to join the next round."
                    show j 1 c smile at fdis
                    j "\"Do we get to go on the same car?\""
                    mc 1 c think "\"You can fit two people if you want to but then one of us doesn't get to drive.\""
                    show j 1 c happy at fdis
                    j "\"Oh, I don't mind driving, I think I'll have more fun if I'm just riding along with you, [povFirstName]-kun.\""
                    show j 1 c wince at fdis
                    j "\"I-If you're okay with it, of course!\""
                    "Why he got flustered at the last line is beyond me."
                    mc 1 c smile "\"Sure, I don't mind.\""
                    show j 1 c happy at fdis
                    j "\"Yaay!\""
                    "Jun begins jumping around as if he were commemorating a major victory at a tournament of some sorts."
                    "Honestly, talk about a weird thing to be excited about."
                    mc 1 c wry "\"It really amazes me how excited you can get over going on a simple park ride with me.\""
                    j "\"Oh. It's just that I've never been to an amusement park before, and now I'm getting to go with a friend. {i}And{/i} we're going to play in the ride together!\""
                    j "\"I can't help getting excited!\""
                    "Seeing how genuine and unrestrained his joy is brings a smile to my face."
                    "I want to make him smile and laugh like this a lot more."
                    "I should probably come up with another place to take him after today."
                    "No matter how much money I end up spending, it'll be worth it."
                    show j 1 c smile at fdis
                    j "\"Look, the line's moving. It's our turn now!\""
                    "The gates open and all the people rush to get a car."
                    "Since Jun and I are sharing one, a seventeenth person is allowed on the tracks."
                    "We end up getting a bright red car with yellow accents. It was right in the middle of all the others cars."
                    "I didn't want to get this one but Jun just dragged me to it."
                    "Honestly... I think this makes us easy targets."
                    "We're probably gonna get rammed to death."
                    mc 1 c wince "\"You sure you wanted this one?\""
                    j "\"Yeah, I really like the red color on it! Why do you ask?\""
                    mc 1 c wince "\"... No reason.\""
                    "Alright, [povFirstName]. Buckle up and just try to avoid getting ran off the track."
                    "Of course, something like that is literally impossible but it sure feels like it could happen considering the fact that we're sitting ducks here."
                    play sound "music/buzzer.ogg"
                    stop music3 fadeout 2.5
                    play music2 "music/BGM/Happy Rock.ogg" fadein 5.0
                    "The buzzer rings and with that, our cars come to life, a small energy display lighting up next to the steering wheel to signal that it's now on."
                    show j 1 c shock at fdis
                    j "\"Oooh, it's really bright!\""
                    "Really? The {i}light display{/i} is the thing that you're impressed by?!"
                    play sound "music/punchlocker.ogg"
                    show j 1 c cshock at fdis
                    j "\"Waaaah!\"" with hpunch
                    "Just as I predicted, before we barely even manage to move a few inches, we're already getting bumped by two different cars."
                    j "\"R-Run away! [povFirstName]-san, run away!\""
                    mc 1 c wince "\"I'm trying I'm trying. They're pinching us between them!\""
                    "After getting banged six or seven times, I manage to slip away from the two cars attempting to turn us into a scrap metal sandwich with tiger and dog filling."
                    "Seeing the two cars then bump each other is one of the most satisfying things I've witnessed all week."
                    "And then, when I turned around and hit them both before they could separate, that was the most satisfying thing I've {i}done{/i} all week."
                    show j 1 c gentle at fdis
                    j "\"Ahahaha, [povFirstName]-san, nice one!\""
                    "Jun giggles next to me, completely filled with joy."
                    "It's honestly very rewarding to see him this excited."
                    "I thought he couldn't get more excited than his usual self, but..."
                    "I was wrong. And this is the other level."
                    "In less than a minute, the entire track has already turned into complete and total chaos."
                    "I can barely process everything that's going on at the same time."
                    "Keeping an eye out to try and avoid possible bangers is quickly sapping my concentration."
                    "And then I also have to try and take the offensive."
                    "It doesn't help that Jun is..."
                    show j 1 c cshock at fdis
                    j "\"Watch out for that guy! Oh, look at that other guy coming our w- {size=+2}Did you see that other guy?!{/size}\""
                    "I'm torn between continuing to drive or conking him on the head to try and stop him being a distraction."
                    "I eventually decide that violence is wrong... even if totally justified."
                    "I just try to leave Jun's screaming to the back of my mind and focus on the driving."
                    j "\"{size=+4}Oh my God that guy came so close to hitting us!{/size}\""
                    "... He does not make it easy."
                    "I barely manage to avoid a car that's speeding right at our back."
                    "The satisfaction of watching that guy miss us and hit the wall is priceless."
                    "Still, it bugs me that I've been concentrating so much on dodging that I've barely hit anyone this whole time."
                    "And I'm pretty sure at least half of our time has already passed."
                    j "\"Hit that guy hit that guy hit that guy!\""
                    "And my annoying co-pilot is constantly yelling out instructions that tell me to go for it."
                    menu:
                        "... Should I just go all out?"
                        "Go on the offensive":
                            "Win or loss doesn't matter, I'll take the same approach that I take to tennis."
                            "{size=+4}Always take the offensive!{/size}" with hpunch
                            "I'm already getting bored of just dodging all the time, I want to hit stuff!"
                            j "\"Waaah, [povFirstName]-san, you could have dodged that one!\""
                            "... And even though he was the one calling for it just a while ago, Jun completely changes his tune as soon as we start to get hit."
                            "I just relegate it to the back of my mind since I'm having way too much fun hitting other people."
                            "Hehe, I just pinned a guy against the wall and the other cars started pummeling too."
                            "Oh man, he looks really pissed. This is awesome!"
                            show j 1 c wince at fdis
                            j "\"[povFirstName]-san, t-the other cars. The other cars are hitting us, d-dodge!\""
                            "I guess I might be letting my bloodlust run a little too rampant. In the last two minutes we went from untouchable to the track's biggest target..."
                            "Eh, I don't care. Hitting stuff is too much fun!"
                            "... I probably should never try driving an actual car."
                            play sound "music/punchlocker.ogg"
                            show j 1 c cshock at fdis
                            j "\"Waaah!\"" with hpunch
                            "We get bumped by two cars at the same time, both hitting us on my side."
                            "The shock of the collision makes our car suddenly move to the side and, as a consequence, I hit the door. Hard."
                            "If that weren't enough, Jun also falls to the side, his head hitting my arm, squishing me between a door and a tiger place."
                            mc 1 c wince "\"Ow!\""
                            "I yelp as a sharp pain emanates from my elbow from when it hit the door."
                            show j 1 c shock at fdis
                            j "\"Wawawawa, sorry sorry sorry sorry!\""
                            "Oh great, now I have to calm down a tiger as he freaks out {i}and{/i} try to survive in the track after we've suddenly become the easiest target on the game..."
                            scene Amusement with fade
                            "In the end, despite having quite a few enjoyable minutes just going full sadist and bringing people the pain, our earlier run-in with the physical principle that says \"Objects in movement tend to stay in movement.\" ended up leaving us as sitting ducks."
                            "So, of course, we were completely destroyed by the other cars."
                            "Oddly enough, I still had a blast."
                            "Although, considering how much Jun was complaining about us getting hit, I thought for sure he'd be annoyed when the ride ended."
                            show j 1 c gentle at fdis, fiveh with dissolve
                            j "\"This. Was. {size=+2}Awesome!{/size}\""
                            "Instead, he was like this."
                            j "\"The way you just completely ran that guy into the wall and didn't let him move was amazing!\""
                            j "\"He just went Nyeeeeh~ But then you went Zoooom~ And he just went Splaaat~ against the wall!"
                            "... Is this even Japanese anymore?"
                        "Continue dodging":
                            "Well, this isn't a game with clear winners or losers so it doesn't really matter how many people I hit anyway."
                            "I think I'll just stick with dodging as much as possible."
                            "It's fun to see the annoyed look on people's faces when they miss."
                            show j 1 c judge at fdis
                            j "\"No no no no, attack attack attack!\""
                            "... Although Jun's constant calls for blood make it a little bit harder to show restraint."
                            "Or, in this case, play it smart."
                            "Still, no matter how tempted I am to throw it all to the air, I continue to stick to my guns."
                            "I think we've only got hit once after leaving that car sandwich from the beginning."
                            "Heh, I might be better at this than I thought."
                            "Maybe I should get an actual car, I'm definitely old enough."
                            "... I wonder if my mom would be okay with me driving though?"
                            "No, wait. If I did get a car, she'd force me to drive her everywhere just like she did dad."
                            "Abort plan. I don't need a car after all."
                            scene Amusement with fade
                            "In the end, we spend the full eight minutes just dodging around like crazy."
                            "We actually did pretty good, we didn't even get hit ten times in total."
                            "We also didn't hit many people either but that's a different story altogether."
                            "Considering how much Jun was demanding that we go on the offensive the whole time, I fully expected him to be annoyed by the time we got out, but..."
                            show j 1 c gentle at fdis, fiveh with dissolve
                            j "\"This. Was. {size=+2}Awesome!{/size}\""
                            "He was like this."
                            j "\"The way you just dodged everyone like crazy was incredible.\""
                            j "\"They just came after you like Zoooom~ And then you dodged to the side like Sweeeep~ And then they just hit something else like Paaaaaa~!\""
                            "... Is this even Japanese anymore?"
                    stop music2 fadeout 5.0
                    mc 1 c smile "\"Well, I'm glad you had fun at least. I was afraid you'd be mad at me for not playing how you wanted me to.\""
                    j "\"Nah, I had a blast. Thanks for driving for me, I'm sure I had more fun than I ever could if I were the one driving!\""
                    "Hehehe, he's really excited about the whole thing. I guess coming to the park was really worth it after all."
                    "Although I'm a little bit worried at just how excited he got on that basic ride."
                    "He couldn't get even more electric than this... could he?"
                    "I shudder at the thought."
                    "Anyway, I need to come up with another ride for us to go on."
                    "Let's see..."
                    play music3 "music/BGM/Spring Classroom.ogg" fadein 5.0
                    jump ride
                "Carousel" if carousel == False:
                    $ rides += 1
                    $ carousel = True
                    "Well... it's not my favorite ride in the world but..."
                    "I have to admit that the carousel is a classic."
                    "Plus, considering how much Jun has been eyeing it since we came in, I think it's safe to say that he wants to go there."
                    mc 1 c curious "\"How about the Carousel?\""
                    show j 1 c shockb at fdis
                    "Before I'm even done with my sentence, his face completely lights up, beaming in excitement."
                    j "\"Really?! I've always wanted to go on a carousel!\""
                    "Bingo!"
                    "I knew he was looking a bit too keen to go on it."
                    mc 1 c smile "\"Sure. Anything you want, Jun. We're here for you first of all."
                    show j 1 c happyb at fdis
                    "Jun scratches his cheek, hiding his embarrassment."
                    j "\"Hehe, I guess that's true. Sorry if I ended up dragging you away to someplace you didn't really want to go.\""
                    mc 1 c happy "\"Nah, don't worry about it. It's an amusement park, of course I'm gonna have fun here.\""
                    mc 1 c smile "\"Plus, I have to admit it's been years since I've last been to an amusement park.\""
                    show j 1 c gentle at fdis
                    "Jun laughs, hopping excitedly in place."
                    "That's how pumped up he is."
                    "If I didn't know better, I could confuse him for a bunny."
                    "... Saya would kill me if she heard my speciest remark."
                    stop music3 fadeout 2.5
                    scene Carousel with fade
                    play music2 "music/BGM/Heartwarming.ogg" fadein 5.0
                    "Despite my own belief that the carousel is a boring, lame ride, there's still a huge line to get in."
                    "It's probably one of the biggest lines in the park."
                    "I'm completely stumped."
                    "Sure, I can get how the kids might like it."
                    "It's one of the few rides they're actually allowed to get into."
                    "But what's with all these adults that {i}clearly{/i} aren't accompanying any children?"
                    "... And just for the record, that doesn't apply to me."
                    "I'm with Jun. Certainly he counts as a kid."
                    "... I think."
                    "Either way, the carousel goes around in circles very slowly, with the toys bobbing up and down whilst carnival music plays on the background."
                    "Just watching it spin is nearly putting me to sleep."
                    "The thing is so slow that it's making me drowsy!"
                    "Even as a kid I wasn't much of a fan of a carousels..."
                    "Now that I'm eighteen, I'm even less of a fan..."
                    "But if Jun wants to go on it, then I'll bite back on my dislike of it and I'll go without complaint."
                    "Heh, the things I'll do for this guy."
                    "I don't even understand why I'm as fond of him as I am."
                    "Regardless, by the time we're next in line, a good half an hour has already passed."
                    "{i}At least{/i}."
                    show j 1 c gentle at fdis, fiveh with dissolve
                    j "\"Yay, it's finally our turn!\""
                    "Jun is incredibly giddy now that our turn has finally arrived."
                    "His feet were tapping on the floor the whole time we were waiting and he kept drumming the rails for the waiting line."
                    "Honestly, how can you get so excited about a carousel? I mean... it's a carousel!"
                    "They separate our wave into two different lines, one for people who'd be going alone and another for people who'd be sharing a horse."
                    "I quickly notice that Jun and I are the only pair that isn't constituted of either a parent and child or a boyfriend and girlfriend."
                    "I start to feel a little bit self conscious over it."
                    "Jun, somehow, manages to pick up on my discomfort."
                    show j 1 c watch at fdis
                    j "\"Is everything alright? Does your stomach hurt or anything?\""
                    "... Of course, he can't tell {i}why{/i} I'm uncomfortable."
                    "I'll still give him props for at least figuring out that I'm not 100\%."
                    mc 1 c considerate "\"No, it's fine. I'm just... feeling a bit weird about going on a carousel.\""
                    "I'm not gonna tell him exactly {i}what{/i} is making me feel weird but there's enough truth mixed up in that for me to convince him."
                    show j 1 c think at fdis
                    j "\"Really? Why? There's a bunch of people who look our age going on it.\""
                    show j 1 c watch at fdis
                    "I manage to bite my tongue before I say \"Yeah, but they're all couples\"."
                    "Somehow, I don't think making Jun feel self conscious too is the best way to handle it."
                    "I'll just pretend there's nothing to bother me and I'll allow him to have his fun."
                    "Plus, if he doesn't realize how people might see us if we go together then that just means he's {i}that{/i} innocent and, honestly, that's pretty adorable coming from a guy his age."
                    "... Although I might be the only person that thinks so."
                    "Finally, our group is called to go on the toy."
                    "We quickly reach one of the horses. A pink one (just my luck), and swiftly mount it."
                    "And by swiftly I mean that Jun is so accident prone that it takes him three times to finally mount the damn thing without falling down one of the sides... or the back."
                    "As it turns out, we're the last people to get on our seats and everyone else had to wait for Jun to manage to sit down."
                    hide j 1 c watch with dissolve
                    "In the end, he only manages to stabilize himself by wrapping his arms tightly around my waist and basically hugging me."
                    "His cheek is also pressing against my back so the awkwardness factor is jumping through the roof here."
                    mc 1 c avoidb "\"U-Uhm... a-are you comfortable?\""
                    "I try stuttering something to make him know that I'm not bothered."
                    "Which, to a normal person, would only tell them I'm bothered."
                    "Still, despite how perceptive he's shown himself to be during the day before this, Jun doesn't manage to catch onto it."
                    j 1 c gentle "\"Yeah. You're really soft and fluffy, [povFirstName]-san. And also kinda warm too!\""
                    "!? Shit, I have to put a hand in front of my face to cover up the fact that I'm blushing."
                    "Luckily no one is close enough to us to be able to tell what the hell is going on and, to Jun, it only looks like I'm wiping my face."
                    "It's kinda hot outside today so if he asks me that would be a legitimate excuse at least."
                    "Suddenly, the horses lift up from the ground and just like that, the carousel starts moving."
                    j 1 c shock "\"W-Wow!\""
                    "Jun is left completely in awe."
                    "I can feel his face rubbing against my back every single time he turns it to look another way."
                    "Which, despite the fact that looking left only allows him to look at the other people on the carousel, still happens pretty often."
                    "It almost feels like someone is nuzzling my back and, as soon as that thought crosses my mind, I blush even more."
                    "Must. Think. Happy thoughts!"
                    j 1 c gentle "\"Look, [povFirstName]-san, you can see almost all of the rides from here!\""
                    mc 1 c wince "\"O-Oh? Y-yeah, that's right. The carousel is right in the middle of the park so you can see a lot.\""
                    "I wouldn't go so far as saying \"almost all\" since this {i}is{/i} a pretty big park after all."
                    "But there is some merit to what he said."
                    mc 1 c smile "\"Honestly, I think it would be more interesting if it were nighttime. Then you'd get to see all of the park lights.\""
                    j 1 c gentle "\"Sounds like it would be pretty beautiful!\""
                    "... I have to admit, even though the carousel is to me one of the dullest rides in existence, Jun's cheer and constant excitement manages to make even this fun."
                    "Heh, I guess some people are just naturally fun to hang out with."
                    "... And now I'm suddenly worrying whether he has as much fun being around me as I do with him."
                    "Oooh, don't go there..."
                    "Either way, there isn't much for me to say about the carousel. I can't exactly see Jun's face."
                    "I can however hear him."
                    j 1 c gentle "\"Damn, this is pretty cool. I almost feel like I'm riding a real horse!\""
                    "... Hopefully he means the ones that walk on four legs and are used for racing, {i}not{/i} the ones that can talk and..."
                    "Ugh... no, my mind is taking this someplace horrible."
                    "Honestly, the biggest upside to me is being able to feel the wind on my face."
                    "And... well... I have to admit that it feels pretty comfortable to have Jun hugging my waist..."
                    "God, why is my face so red right now..."
                    "Even though I'm actually having fun, I also can't wait for the ride to end."
                    "Having Jun so close to me is making my heart race like mad. I feel like I could just drop dead from a heart attack at any second."
                    "... Well, maybe I'm exaggerating a little bit but my face feels so damn hot right now..."
                    "In the meantime, even the actual couples that are on the ride with us don't seem to be snuggling up as close to each other as Jun is to me."
                    "Damn, now I feel even more self conscious. I don't even know how that's possible."
                    scene Carousel with fade
                    "Eventually the ride comes to a stop, and I'm all too happy to climb down from it."
                    "Man, this feels really awkward... for me at least."
                    "Jun looks..."
                    show j 1 c gentle at fdis, fiveh with dissolve
                    j "\"This was amazing. Let's do it again, let's do it again!\""
                    "Incredibly excited... Honestly, this is one of those rare moments where I wish he had an off switch."
                    "My mind is swimming in awkwardness that having someone so intense right next to me is making me feel overwhelmed."
                    "If I remember correctly, this is how I felt when I first met him."
                    "Funny how I ended up warming up to him so quickly."
                    "And, honestly, I wouldn't have had it any other way."
                    "But back to the matter at hand..."
                    scene Amusement
                    show j 1 c gentle at fdis, five
                    with fade
                    j "\"[povFirstName]-san, can we ride it again? Please please please!\""
                    "Jun stares up at me whilst clinging to my shirt's cuffs with what can only be described as puppy dog eyes."
                    "Even though he is neither a puppy nor a dog."
                    "Ugh... saying no to this face feels like smothering a dog in his sleep..."
                    "Again, even though he is {i}not{/i} a puppy."
                    mc 1 c wince "\"S-Sorry, Jun. I don't think it'd be all that fun to go again. Plus, we only have so few tickets so we should try to see other rides.\""
                    "I pray to any and all deities that might be out there that this manages to convince him because, honestly, five more minutes on that ride with him clinging that close to me and I swear my head would explode."
                    show j 1 c pout at fdis
                    "Jun lets go of my shirt and looks down at the ground, kicking up some dirt."
                    j "\"Awww, alright.\""
                    "Jesus, why do I feel like I just did something awful like murder his mother?! All I did was say no!"
                    "It's terrifying how much destructive power his face can have at times..."
                    "... I kinda feel like a father doting on his child."
                    "No, that's not a thought I want to be having either. Especially when he's older than me!"
                    "A fact that I constantly forget because, honestly, no one would guess it based on our looks and attitudes."
                    "In fact, I have difficulty believing that Jun is not a junior high student sometimes..."
                    show j 1 c think at fdis
                    j "\"What will we do now, then?\""
                    mc 1 c smile "\"Do I still get to choose?\""
                    show j 1 c happy at fdis
                    j "\"Of course! You're still the one who bought most of the tickets!\""
                    mc 1 c think "\"Alright then. Let's see...\""
                    "Hmm... what else can I choose from..."
                    stop music2 fadeout 2.5
                    play music3 "music/BGM/Spring Classroom.ogg" fadein 5.0
                    jump ride
                "Tea Cups" if teacups == False:
                    $ rides += 1
                    $ teacups = True
                    "Hmm... I think I remember reading something about this park having recently opened a new ride."
                    "It was supposed to be a bunch of spinning tea cups that go really fast."
                    "I also remember reading somewhere that it could cause nausea..."
                    "Sounds like the perfect ride!"
                    mc 1 c smile "\"I have an idea. Follow me!\""
                    show j 1 c think at fdis
                    j "\"You thought of something? What is it?\""
                    mc 1 c happy "\"Tea cups!\""
                    show j 1 c wince at fdis
                    j "\"Tea cups? You mean going to the park's cafe for a cup of tea?\""
                    "I chuckle."
                    mc 1 c smile "\"Sure, something like that. Yeah.\""
                    "Oh, I have to admit, Jun's confused expression is priceless."
                    j "\"But we've used all of our money already!\""
                    "I grin, grabbing his wrist and pulling him by the arm."
                    mc 1 c laugh "\"Just come with me already!\""
                    show j 1 c shock at fdis
                    j "\"Awawawa!\""
                    "The fact that Jun is completely confused about what's going on only makes the whole thing even better!"
                    "Let's see... I seem to remember reading that it was somewhere close to the roller coasters..."
                    "Ah, the roller coasters... How I wish we could ride them..."
                    "Well, nothing I can do if Jun doesn't want to. And I'm not about to make him."
                    "I have no idea how he'd react if I did anyway."
                    stop music3 fadeout 2.5
                    scene Teacups
                    show j 1 c watch at fdis, five
                    with fade
                    play music2 "music/BGM/Punchline - Org.ogg" fadein 5.0
                    "Aha!"
                    "After a little bit of walking, we finally reach our destination."
                    "There's a giant circular platform where multiple booths in the form of tea cups were stationed, each of them on top of their own spinning platform."
                    "So while the giant platform would spin, the tea cups would spin inside of it."
                    "It was supposed to be a fun toy for kids and adults since it mostly plays with speed and centrifugal force."
                    show j 1 c wince at fdis
                    j "\"W-Wait, you mean you want to ride that... that {i}thing{/i}?!\""
                    "Jun's face immediately goes pale when he sees it."
                    "I, of course, smile."
                    mc 1 c happy "\"Sure I do! Doesn't it look like fun?\""
                    "Jun stares at the ride spinning for a few seconds and swallows. Hard."
                    j "\"S-Sure. Looks like a blast...\""
                    "Even I can tell that he's hesitant to go on it."
                    "Don't get me wrong, I like the idea of surprising him with it but if he doesn't want to go then there's no point in making him."
                    mc 1 c "\"You sure you're okay with it? You don't look too happy with the idea.\""
                    "Jun snaps back to reality, looking at me for a few seconds and then looking away."
                    show j 1 c considerate at fdis
                    j "\"N-no, I didn't mean- It's not that I don't want- I didn't really think-\""
                    "I grab hold of him by his shoulders and shake him gently, looking at the tiger dead in the eye."
                    mc 1 c sigh "\"Jun, breathe! Organize your thoughts instead of just stuttering a bunch of half-sentences!\""
                    show j 1 c blush at fdis
                    j "\"R-Right.\""
                    "He steps backwards and away from me."
                    "I guess he doesn't appreciate being grabbed all of a sudden in public?"
                    show j 1 c wince at fdis
                    j "\"A-anyway, it's not that I don't {i}want{/i} to go on it, it's just...\""
                    "Jun looks down at the floor, clutching his chest."
                    j "\"I'm just afraid that I might...\""
                    "He trails off before reaching the end of the sentence, leaving me to wonder what he was even talking about in the first place."
                    "I curve myself down to be able to look him in the eye."
                    mc 1 c curious "\"You're afraid of what? That you'll get nauseous?\""
                    show j 1 c shock at fdis, jumping
                    $ renpy.pause (1.0)
                    show j 1 c considerate at fdis
                    j "\"Y-yeah, that's it. I'm just afraid that I'd throw up hahahaha!\""
                    "Oh, so that's what it was about."
                    "This stupid tiger almost made me think it was something serious for a few seconds there."
                    mc 1 c smile "\"Hehe, you don't have to worry about that. If you get sick we can just stop by the restroom and give you a few minutes to rest.\""
                    j "\"Y-Yes, that's true, we can do that.\""
                    "Jeez, you don't have to look so stiff when you're laughing."
                    "Are you really that afraid you'd get sick?"
                    "It's not like the ride goes all that fast anyway..."
                    mc 1 c smile "\"Well, we should take our place on the waiting line then. It's not very long right now but you can never know!\""
                    show j 1 c wince at fdis
                    j "\"Y-yes, that's true!\""
                    show j 1 c wince at fdis, offscreenleft with moveoledis
                    "Before I'm even given time to turn around, Jun bolts towards the waiting line."
                    "Jeez, now he's suddenly excited to go on the ride?"
                    "Honestly, I can't understand him sometimes..."
                    "Luckily, the line is actually pretty small."
                    "The people that were already on the ride left just as soon as we stepped into the line and then it was our turn."
                    show j 1 c fluster at fdis, fiveh with dissolve
                    "Jun and I enter, going towards a giant blue tea cup."
                    "One of the sides opens like a car door, allowing us easy entrance."
                    mc 1 c wince "\"Wow, it's kinda tight in here.\""
                    "I remember reading that it could have up to four people but I have a hard time imagining even a third person fitting here."
                    "I guess they meant kids when they said four people?"
                    j "\"Is there nowhere for us to hold on to?\""
                    "Jun's face looks to be about two shades paler."
                    "Maybe this wasn't such a good idea after all?"
                    "Just as I'm about to suggest we leave, the ride starts to spin."
                    show j 1 c fluster at fdis, jumping
                    j "\"W-Woah!\""
                    "It didn't start particularly fast but, since Jun had not grabbed onto anything, the sudden movement makes him slide over on his seat, nearly falling out of it."
                    mc 1 c shock "\"Waa, careful!\""
                    "I reach out to grab him before he can fall, pulling the tiger up to me."
                    "Whether it be by instinct or his own will, Jun imediatelly wraps his arms around me, leaning against my chest."
                    j "\"Awawawawawa it's getting faster!\""
                    "I have to admit, watching his reaction was amusing, but..."
                    "I suddenly feel really awkward about having someone clinging so close to me..."
                    "Ah, I have to look away because my cheeks are feeling really hot right now."
                    "Just like Jun said, the toy is gradually gaining speed."
                    "Right now, it's already fast enough that I can feel my back being pressed against the walls of the cup."
                    "If this weren't here right now, I wouldn't be flung off for sure."
                    "Waaa, this thing doesn't look all that fast from the outside but it's a whole different deal when you're actually in it!"
                    "To be honest, I'm starting to feel a little queasy..."
                    "Just as I'm starting to worry that maybe I might get sick from all this spinning, I feel a vice-grip tightening even more around my chest."
                    mc 1 c wince "\"J-J-Jun, c-can't bre-\""
                    stop music fadeout 5.0
                    show j 2 c pain at fdis
                    j "\"Waaaah, [povFirstName]-san, make it stop!\""
                    play sound "music/heartbeat.ogg"
                    "When I look down, I see Jun holding me tightly with tears starting to form around his eyes, his face completely pale and his breathing erratic."
                    stop music3 fadeout 2.5
                    play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
                    "I-Is he crying?!"
                    mc 1 c shock "\"J-Jun, are you alright?!\""
                    "He shakes his head sideways and then buries it on my chest, making it so I can't even see his face anymore."
                    j "\"It hurts, make it stop!\""
                    "H-hurts? You mean his stomach is hurting?"
                    "I start to consider my options here. Would they stop the ride if I asked? I doubt it."
                    "M-maybe there's an emergency button on it. I mean, people get sick on these sometimes so they're bound to have an emergency button, right?"
                    "I try looking around. It's kinda hard to focus my vision because of the spinning but I eventually see a big red square with the letter \"E\" on it."
                    "I don't even consider it, I reach for the emergency but-\""
                    "And before I can even reach it, I hear an alarm ringing and the ride begins to stop on its own."
                    mc 1 c shock "\"W-What?\""
                    "Did the time run out already? I doubt it."
                    "I hear one of the doors opening and, open looking at the side, I can see the reason why it stopped."
                    "A family on another nearby cup pressed the emergency button because the woman was feeling ill. I can see her walking out of the cup with her legs quivering."
                    "W-Wait, this is my chance."
                    mc 1 c wince "\"E-Excuse me!\""
                    "I lift my arm up and made sure that I can be heard by the operator."
                    "The man glances my way, taking his eyes off of the family that's still getting down from the platform."
                    mc 1 c considerate "\"My friend is feeling sick, can we get out?\""
                    "The skunk nods, looking down at his panel and pressing a button. The door to our cup immediately opens."
                    mc 1 c worried "\"Alright, Jun, come on. Let's get out of here.\""
                    "Jun gets up, his head still buried on my chest."
                    stop music2 fadeout 5.0
                    "His breathing is still erratic and I'm left worried that he might throw up on me."
                    "Man, that would suck."
                    scene Amusement
                    show j 1 c cry at fdis, five
                    with fade
                    "We step out of the ride and look for a nearby bench to sit on."
                    "This whole time, Jun was still clinging on to me and I couldn't even see his face."
                    "After a few minutes sitting down, his breathing seems to calm down little by little."
                    mc 1 c wince "\"Hey... Jun? Are you alright?\""
                    "Jun nods without even looking up."
                    mc 1 c worried "\"Come on, let me look at your face, okay?\""
                    "Slowly, he looks up."
                    "The fur around his eyes is matted and his face still looks pale."
                    mc 1 c worried "\"Are you alright? Are you feeling sick? Maybe we should go to the nursing room.\""
                    "Jun desperately shakes his head sideways, as if that's the last thing he wants."
                    mc 1 c worried "\"Come on, you said you were in pain, I can't ignore that! What is it that hurts anyway, your stomach?\""
                    show j 1 c shock at fdis
                    "The tiger immediately freezes, his eyes going wide."
                    show j 1 c blush at fdis
                    "Jeez, that embarrassed to admit he got a stomach ache?"
                    mc 1 c considerate "\"Well, we did eat a lot today. I'm sure having this thing making all the food in your stomach just toss and turn like that was bound to make one of us feel ill sooner or latter. Nothing to be ashamed of!\""
                    "I try to lighten up the mood but he seems to be having none of it."
                    "He's yet to even say a word since we walked out of the ride..."
                    "Slowly, Jun pulls away from me, leaving a small gap between the space that was previously occupied by his body."
                    "He sits upright on his spot at the bench, looking down at the floor."
                    "The whole time I'm wondering when the color will start returning to his face."
                    mc 1 c worried "\"Are you sure you don't want to go to the nursing room?\""
                    show j 1 c wince at fdis
                    "He nods, his eyes still glued to the floor."
                    mc 1 c worried "\"Come on, Jun. If you want me to believe that you're okay, at least say something!\""
                    j "\"... Sorry.\""
                    "I cock my head to the side, confused."
                    mc 1 c curious "\"Sorry? What for?\""
                    "He seems to be a little lethargic because he takes a while to answer me."
                    j "\"... You looked like you really wanted to go on that ride and I... made us get off. Sorry, it was a wasted ticket in the end.\""
                    mc 1 c shock "\"Wha-\""
                    "I want to scream at him. \"Do you really think I'm worried about {i}that{/i}?!\". But I manage to control myself before the words slip out of my mind."
                    "Somehow, I'm still aware that this wouldn't help him in the slightest."
                    "Screaming at someone that's feeling sick is just going to make them feel worse."
                    "I take a few deep breaths to steady myself before speaking again."
                    mc 1 c considerate "\"I don't care about the tickets, I'm just glad that you're okay. Good thing it was nothing serious.\""
                    show j 1 c avoid at fdis
                    j "\"... Yeah.\""
                    mc 1 c "\"Still, you don't look too well. Maybe we should call it quits for today?\""
                    show j 1 c shock at fdis
                    j "\"N-no! Then I'd just feel awful about the whole thing!\""
                    mc 1 c wince "\"B-But, you're obviously not doing well enough for us to-\""
                    "Jun shakes his head vigorously to the sides, as if he's trying as hard as he can to deny me."
                    show j 1 c considerate at fdis
                    j "\"I'll be fine. Just give me a few minutes to rest and I'll be great!\""
                    mc 1 c worried "\"A-Are you sure?\""
                    "Somehow I doubt that."
                    "Still, Jun nods vigorously once more."
                    mc 1 c sigh "\"Alright alright. We'll stay at this bench for a few minutes and then we'll go to another ride.\""
                    "We spend a few minutes sitting side by side, not saying even a word."
                    show j 1 c sigh at fdis
                    "Jun has his eyes closed the whole time, taking deep breaths."
                    "At first I thought that he fell asleep."
                    "Until I noticed his clenched fists quivering on top of his lap, grabbing tightly at the fabric of his shorts."
                    "... I guess he's trying to calm himself down with any way possible, huh..."
                    "After a couple minutes of this silence, Jun sighs, looking up at me with a smile."
                    show j 1 c considerate at fdis
                    j "\"Alright, I think I feel okay now.\""
                    mc 1 worried "\"Are you sure?\""
                    play music3 "music/BGM/Spring Classroom.ogg" fadein 5.0
                    show j 1 c smile at fdis
                    j "\"Yeah. I'm fine now.\""
                    "... I have to admit, he does look normal at least."
                    "Well... if he insists on it, I guess there's no harm in going for other rides."
                    "Let's see... what should I pick this time?"
                    jump ride
                "Tunnel Ride" if tunnel == False:
                    $ rides += 1
                    $ tunnel = True
                    "Wasn't there a water ride in this park?"
                    "I think I remember going with Aki when the two of us were really small."
                    "Yeah, you'd get into a car that would go through a track that was filled with water."
                    "Halfway through it, you'd go inside a tunnel."
                    "It's a pretty popular ride between couples but, really, all sort of people go on this one."
                    "Plus, the cars are comfortable, the tunnel is very cool and the feeling of water droplets splashing on your every now and then is really nice."
                    mc 1 c smile "\"I think I know a ride you might like to go on.\""
                    show j 1 c shockb at fdis
                    j "\"Really? What is it?!\""
                    "His excitement is adorable. Makes me want to fawn all over him."
                    mc 1 c happy "\"There's a water ride here in this park. You basically get inside a car and it goes through a track filled with water. It's pretty cool and relaxing.\""
                    "Jun blinks multiple times, his lips opening up in a smile."
                    j "\"That sounds like it could be fun!\""
                    "Well, for the guy that mentioned a carousel as a fun ride, I'm sure almost anything would be fun."
                    show j 1 c watch at fdis
                    j "\"Do you know where it is?\""
                    mc 1 c smile "\"Not really but we can always check a map.\""
                    show j 1 c pout at fdis
                    j "\"What's the fun in checking a map?\""
                    mc 1 c sigh "\"What's the fun in getting lost?\""
                    play sound "music/stab.ogg"
                    show j 1 c wince at fdis, shake1
                    j "\"Guh...\""
                    "Swiftly, I cut down his free-spirited logic."
                    "This isn't the first time where Jun's approach has lead us to getting lost somewhere and I don't want to have that being repeated again."
                    "I find a map near one of the many rest stops and look for directions to the ride I'm looking for."
                    show j 1 c watch at fdis
                    mc 1 c smile "\"Oh, it's nearby. Come on, it shouldn't take us long to get there.\""
                    show j 1 c happy at fdis
                    j "\"Yay~\""
                    "Even though he wanted to just walk around aimlessly looking for it, he still seems quite pleased that we found the ride."
                    stop music3 fadeout 2.5
                    scene BoatRide
                    show j 1 c smile at fdis, five
                    with fade
                    play music2 "music/BGM/Funin And Sunin.ogg" fadein 5.0
                    "It doesn't take us long to find our way to the line."
                    "The air around the ride is already much cooler due to the huge amount of water nearby."
                    show j 1 c happy at fdis
                    j "\"Waaah, it's so cool around here~\""
                    "I have to say, today wasn't really a super hot day by any means but this area of the park is at such a comfortable temperature!"
                    mc 1 c think "\"I guess this explains why the line is so huge for this one though...\""
                    "If I had to guess, I'd say that there are easily over fifty people in line to go on this ride."
                    show j 1 c wince at fdis
                    j "\"Uuuuh, there's so many people. How long do you think it'll take for us to get in?\""
                    mc 1 c "\"I'm not sure, it looks like it might be a while. The ride isn't exactly fast to begin with.\""
                    "Jun nods, looking downcast."
                    mc 1 c smile "\"Heh, don't worry about it. Even if we stand in line for a while, it's still super comfortable because of the temperature.\""
                    show j 1 c smile at fdis
                    j "\"I guess that's true.\""
                    show j 1 c happy at fdis
                    "Jun begins humming."
                    "While he is not particularly quiet about it, he still makes sure to not bother any of the other people in line."
                    "Seeing him humming is pretty rare, I guess something must have put him on a particularly good mood."
                    "Wait, I think I recognize this tune..."
                    "Isn't this the song he played at the café?"
                    "I strain my ears to try and hear more details and it definitely sounds to me like the song he played today."
                    "The one that he composed."
                    "Huh... that's true. I had some questions I wanted to ask him about the song but I ended up being so absorbed by it at the time that I forgot."
                    "I tap Jun on the shoulder to try and call his attention."
                    show j 1 c watch at fdis
                    j "\"Hmm? What is it, [povFirstName]-san?\""
                    mc 1 c curious "\"This song you're humming. It's the same one you played earlier today, right?\""
                    show j 1 c gentle at fdis
                    j "\"Yup, that's right. I didn't think you'd recognize it, hahaha!\""
                    "Huh... so me knowing the song actually makes him happy? That's... strange?"
                    mc 1 c smile "\"Well, I really liked the song after all. I actually had a few questions I wanted to ask you about it if that's okay with you.\""
                    show j 1 c smile at fdis
                    j "\"Sure. Ask away."
                    mc 1 c curious "\"Well... I was just wondering, I remember you mentioning that you wanted to be a composer but you never really told me why. You just said that you gave up on being a pianist.\""
                    show j 1 c think at fdis
                    j "\"Oh... that.\""
                    show j 1 c watch at fdis
                    j "\"Back when I was a kid, I didn't really have many friends. Videogames were my biggest friends other than the piano, they'd just take me to other worlds were I would be someone different from who I really am...\""
                    show j 1 c considerate at fdis
                    j "\"Hehe, it sounds really cheesy doesn't it...\""
                    mc 1 c smile "\"Not at all! Honestly, it's not much different from people who enjoy to read. Kei-kun is always saying that he likes books that \"take him away\"!\""
                    show j 1 c think at fdis
                    j "\"I guess... In the end, the music was always a big part of why I liked them. The way it could perfectly show you the character's feelings and emotions, the way it would touch the heart.\""
                    show j 1 c happy at fdis
                    j "\"I just decided that, since I couldn't be a pianist, that I wanted to be a composer and work with videogames.\""
                    j "\"I wanted other kids to be able to experience the same things that I did with games and I wanted my songs to be part of it!\""
                    mc 1 c happy "\"Aww, that's really cute actually.\""
                    show j 1 c wince at fdis
                    j "\"R-really? You don't think it's lame or anything like that?\""
                    mc 1 c smile "\"Lame? Why would I think it's lame? People hardly ever have super deep reasons for wanting to do something, we just kinda do them.\""
                    show j 1 c think at fdis
                    j "\"Really? What's your reason for wanting to be a tennis player, then?\""
                    mc 1 c think "\"That's...\""
                    "Ugh... this awkward conversation again."
                    "At this point, I don't mind answering this question, but people always respond the same way when I do..."
                    mc 1 c considerate "\"My dad taught me tennis when I was little. It was his favorite sport and he played competitively when he was in high school, although he stopped when he got into college.\""
                    show j 1 c happy at fdis
                    j "\"That's kinda neat. My dad never really taught me anything that I liked.\""
                    show j 1 c think at fdis
                    "Then, Jun blinks multiple times as if he just realized something."
                    "He cocks his head to the side, confused."
                    stop music2 fadeout 5.0
                    show j 1 c watch at fdis
                    if day5 == "jun":
                        j 1 c wince "\"You said before that your dad wasn't around. Why... uhm... if you don't mind me asking, why did he leave you guys?\""
                        "..."
                    else:
                        j "\"Actually, come to think of it, I've never met your dad before. Is he away on a business trip like Shoichi-san's?\""
                    "... And here comes the awkward part."
                    "I sigh, rubbing the bridge of my nose."
                    mc 1 c considerate "\"No. My dad died when I was a kid... One week after teaching me how to play tennis and one month before Aki was born.\""
                    show j 1 c shock at fdis
                    "Immediately, Jun froze."
                    "I could picture the cogs running in his head, trying to understand what I just told him."
                    "Honestly, I don't blame him. Not many people know about my father in the first place."
                    "Him dying and Aki being born were the reason we moved away from my hometown and into Saitama in the first place."
                    j "\"D-Dead? Y-You mean...\""
                    play music2 "music/BGM/Sighs.ogg" fadein 5.0
                    mc 1 c considerate "\"He died in a car accident when I was six. He had been overworking himself and taking too many shifts to save up money for when Aki was born.\""
                    mc 1 c sad "\"He... was tired and didn't pay enough attention before crossing the street. He got hit by a car and... do I really have to say it?\""
                    "Suddenly, the mood becomes super awkward."
                    "For a few seconds, all that I can hear is the sound of the other people around us chatting excitedly."
                    "Meanwhile, it's as if Jun and I had suddenly been covered by a shroud."
                    "The comfortable cool air suddenly became much colder and uncomfortable."
                    j "\"I-I...\""
                    show j 1 c wince at fdis
                    j "\"I'm sorry, I didn't mean to- I-I shouldn't have-\""
                    "I put a hand on his shoulder, getting him to look at me once again."
                    mc 1 c considerate "\"Listen to me, this stuff is in the past, okay? Sure, it sucks and yeah, I do wish my dad were still here but, really... you don't have to apologize. You couldn't have known and this kind of stuff doesn't really bother me.\""
                    mc 1 c wry "\"And I'm not like Aki anyway. I at least got to meet my dad, he wasn't so lucky... it's why I've always made sure to take good care of him, so he'd have a male role model to look up to.\""
                    "Jun nods, looking down at his feet."
                    "Ugh... now I've done it. I've driven the final nail to the coffin of what was up to now a pleasant conversation."
                    mc 1 c considerate "\"Sorry, maybe I should have just changed the subject?\""
                    "Jun shakes his head sideways, a very conflicted expression on his face."
                    j "\"N-No, of course not. I was just... surprised...\""
                    j "\"I shouldn't have asked. I didn't know it was a sensitive subject...\""
                    "I give him a few taps on the back, trying to get his attention."
                    "Once he looks up, I make sure to give him a big smile."
                    mc 1 c smile "\"It's not a sensitive subject and you didn't do anything wrong. We haven't known each other all that long so it stands to reason that we wouldn't know each other all that well.\""
                    mc 1 c considerate "\"And if we don't ask, we'll never really get to know anything about one another, isn't that right? I'm sure we all had bad experiences in our lives but that doesn't mean we should never talk about it.\""
                    show j 1 c avoid at fdis
                    j "\"I... guess that's true. I'm still sorry to have brought it up...\""
                    "I make an over exaggerated waving gesture with my hand, as if I were driving away imaginary smoke."
                    stop music2 fadeout 5.0
                    mc 1 c considerate "\"Nonsense. I'm the one who's sorry for ruining the mood.\""
                    mc 1 c smile "\"What do you say? Can we just continue to have fun or will we let this little hiccup ruin the rest of the day for us?\""
                    show j 1 c considerate at fdis
                    j "\"I guess so.\""
                    play music2 "music/BGM/Funin And Sunin.ogg" fadein 5.0
                    show j 1 c happy at fdis
                    j "\"Yeah, let's continue to have fun!\""
                    mc 1 c happy "\"That's the spirit!\""
                    "Luckily, just as we finish that conversation, the next car arrives and it is finally our turn to board the ride."
                    show j 1 c shockb at fdis
                    j "\"Oh, cool, there's four seats! Want to share the two on the front with me?\""
                    mc 1 c smile "\"Sure. No reason for each of us to go on a separate row anyway.\""
                    "Jun nods and we board the car."
                    show j 1 c gentle at fdis
                    j "\"Wow, these seats are pretty comfortable.\""
                    mc 1 c think "\"You'd hope so considering it's almost ten minutes sitting down.\""
                    j "\"Hahaha, true enough!\""
                    "Well, good to see he's still keeping his cheer."
                    "I was worried he'd be bummed out by my story."
                    play sound "music/smallsplash.ogg"
                    show j 1 c wince at fdis
                    j "\"Wah, some water just splashed on me!\""
                    mc 1 c considerate "\"Well, this is a water ride after all.\""
                    stop music2 fadeout 2.5
                    scene Amusement
                    show j 1 c smile at fdis, five
                    with fade
                    "Despite how tense the mood had gotten before, we're able to enjoy the ride without further issues."
                    show j 1 c happy at fdis
                    j "\"That was really nice. The cool air inside the tunnel was so relaxing!\""
                    mc 1 c smile "\"Yeah, although I could have done with a little less water splashing on us.\""
                    show j 1 c think at fdis
                    j "\"Well, it {i}was{/i} a water ride.\""
                    mc 1 c sigh "\"Didn't I say that to you a few minutes ago?\""
                    show j 1 c happy at fdis
                    j "\"Hehehe.\""
                    "Well, I'm just glad the mood isn't weird anymore.\""
                    "Let's see... what should we do next?"
                    play music3 "music/BGM/Spring Classroom.ogg" fadein 5.0
                    jump ride
                "Train" if train == False:
                    $ rides += 1
                    $ train = True
                    "Oh, that's true. I remember there being a ride at the edge of the park that takes us via a small train through the nearby woods."
                    "It's supposed to be a way for us to enjoy nature."
                    "Plus, it's relaxing."
                    mc 1 c smile "\"Hey, Jun, how would you like getting to go through the nearby woods?\""
                    show j 1 c wince at fdis
                    j "\"Eh? But what about the park?\""
                    mc 1 c happy "\"You see, it's actually one of the rides of the park. You get into a small \"train\" that takes a bunch of people through the woods.\""
                    mc 1 c smile "\"Of course the tracks are predetermined but it should be relaxing. Plus, you get to sightsee.\""
                    show j 1 c happy at fdis
                    j "\"Oh, that sounds like it could be fun. Have you ever ridden it before?\""
                    "Well, seems like he's interested at least."
                    mc 1 c think "\"Not really, when Aki and I came here we'd always want to stay with the roller coasters.\""
                    mc 1 c smile "\"This park {i}does{/i} have some of the best roller coasters in Japan after all.\""
                    j "\"Oh, that's cool. That means it'll be your first time going too!\""
                    mc 1 c happy "\"Huh, I didn't think you'd be excited about that.\""
                    j "\"Why wouldn't I? That means we'll both get to have fun together. I won't have to worry about whether you're bored doing something you've done a million times before.\""
                    "I guess his logic is infallible, if a little weird."
                    mc 1 c happy "\"Alright then, the ride isn't amazingly popular so we might have to wait a while for them to finish getting enough people for one trip but let's head to it already.\""
                    mc 1 c smile "\"It's at the other edge of the park so there'll be a little bit of walking.\""
                    j "\"Okay!\""
                    stop music3 fadeout 5.0
                    play music2 "music/BGM/Ride the Wind.ogg" fadein 5.0
                    scene Train with fade
                    "As luck would have it, by the time we arrive in line, we find out that we're the last people needed for the train to depart on the next ride."
                    "Seems they were waiting for the past ten minutes for at least two more people to fill up their minimum quota."
                    "We quickly board, taking seats at the end of the train while most other people choose to take the front."
                    "The four rows directly in front of us are completely empty, leaving us complete privacy to talk about whatever we want."
                    show j 1 c shock at fdis, fiveh with dissolve
                    j "\"Wow, I know you said it wasn't a super popular ride but I was expecting more people to show up.\""
                    mc 1 c smile "\"Well, most of the people that come to these are families with kids too young to go on the more adrenaline-inducing rides... or elderly people.\""
                    "In fact, out of the ten people in the train at the moment, there are three people over sixty and a family with their three small kids."
                    show j 1 c think at fdis
                    j "\"Huh... I wish my parents had taken me to these places when I was a kid.\""
                    mc 1 c happy "\"Hey, think of it from the other angle. You get to bring them here when they're old!\""
                    show j 1 c happy at fdis
                    j "\"Hahaha, I guess that's true.\""
                    "The train moves very slowly, taking a leisurely ride next to the park's lake before going into the designated area of the woods."
                    "Even here, you can already see an abundance of trees and general greenery."
                    "There are even some animals from the woods amidst the trees and bushes."
                    show j 1 c shockb at fdis
                    j "\"Oh, look at those birds at the edge of the lake!\""
                    mc 1 c smile "\"There's also some deer drinking water from it too.\""
                    "It's a bit comical looking at the family of deer on our train whilst saying that."
                    "Some people would actually take offense being compared to their feral ancestors."
                    "Well, I myself don't particularly care."
                    show j 1 c happy at fdis
                    j "\"Oh, look, there's a few monkeys on the trees!\""
                    "Still, this guy is being just a little bit too carefree here..."
                    "If the train weren't this empty, I'm sure someone would have told him to be quiet already."
                    "His voice is so loud that it's making my head hurt a little."
                    "Don't say anything don't say anything don't say anything."
                    show j 1 c think at fdis
                    j "\"[povFirstName]-san?\""
                    "Oh shoot, I was spacing out."
                    mc 1 c considerate "\"Hmm, yeah?\""
                    j "\"Are you alright, it looks a little weird...\""
                    mc 1 c curious "\"Huh? What does?\""
                    show j 1 c watch at fdis
                    j "\"Your face!\""
                    play sound "music/stab.ogg"
                    "So direct!!!" with hpunch
                    mc 1 c annoyed "\"I-I'm sorry if my face looks weird, this is the face I was born with!\""
                    show j 1 c considerate at fdis
                    j "\"Ah, no, I don't mean it like that. I just meant that you looked a little tense. Are you uncomfortable?\""
                    mc 1 c sigh "\"How would you even be able to tell? It's not like I have the friendliest-looking face.\""
                    "In fact, I have had a ton of people pointing out just how unfriendly I look."
                    "Shoichi says that this is why I don't have any real friends other than our small group."
                    show j 1 c think at fdis
                    j "\"Hmm? What are you talking about? Whenever I'm with you, you're always smiling.\""
                    "..."
                    "Wait, what?"
                    mc 1 c shock "\"I'm... always smiling?\""
                    show j 1 c watch at fdis
                    j "\"Yeah. You're always smiling whenever I see you. And you're always so kind to me, it makes me feel welcome. Isn't that how you always are?\""
                    "...{nw}"
                    play sound "music/stab.ogg"
                    "...{fast} Whaaaaaaaat?!" with hpunch
                    mc 1 c shock "\"I-I've never been told that before. P-people always tell me I look unapproachable.\""
                    show j 1 c think at fdis
                    j "\"Really? But you're the one that makes me feel the most welcome.\""
                    "!!!"
                    "W-Why am I blushing? Shit, I can't let myself be seen like this."
                    show j 1 c shock at fdis
                    j "\"Waah, [povFirstName]-san, why are you looking away like that? Did I say something wrong? I didn't offend you, did I?!\""
                    "Seriously, how dense can someone be? I'm not mad, I'm blushing, dammit...\""
                    mc 1 c sigh "\"It's fine, I'm just... thinking about it. Yeah, that's it, I'm just thinking it over...\""
                    show j 1 c watch at fdis
                    j "\"Oh, okay then.\""
                    show j 1 c gentle at fdis
                    j "\"Oh, look, a flamingo!"
                    show j 1 c think at fdis
                    extend " {size=-2}Oh, wait, it's just a statue.{/size}\""
                    "... How can he change tracks so fast?"
                    "It's really hard to keep up with him sometimes."
                    "Still, it's fun to watch Jun getting carried away like this."
                    "I have to admit, I really look forward to spending the rest of the year getting to know him better."
                    "In fact, I wish I had met him sooner..."
                    show j 1 c shock at fdis
                    j "\"Is that a boa constrictor on the water?!\""
                    mc 1 c think "\"No, that's an iguana.\""
                    show j 1 c think at fdis
                    j "\"Really? How can you tell?\""
                    mc 1 c sigh "\"... It has legs.\""
                    show j 1 c watch at fdis
                    j "\"Oh.\""
                    mc 1 c sigh2 "\"How do you not notice it {i}walking{/i}?\""
                    "I do wish he paid a little more attention at times though..."
                    show j 1 c gentle at fdis
                    j "\"The breeze is so nice over here!\""
                    "Don't just change the subject like that!"
                    mc 1 c sigh "\"... Yeah, it's a hoot.\""
                    show j 1 c watch at fdis
                    j "\"Your voice sounds a little funny. Did something bother you?\""
                    "You did!" with hpunch
                    "I can't tell whether he's seriously clueless or if he's low-key mocking me."
                    "Both notions are terrifying for different reasons."
                    show j 1 c happy at fdis
                    j "\"I feel like this could be a lot more interesting if real life had theme songs.\""
                    show j 1 c think at fdis
                    j "\"Hmm... I can imagine an upbeat, lighthearted track for this particular ride.\""
                    mc 1 c smile "\"Why don't you try composing one, then?\""
                    j "\"Hmm... I would but I don't really have a computer. Or a composing software. So I end up only using my piano for it.\""
                    show j 1 c considerate at fdis
                    j "\"I think I'd need other instruments for a track like that though, don't you think?\""
                    mc 1 c think "\"Oh yeah, that's true...\""
                    "Jeez, not having a computer is rough..."
                    mc 1 c curious "\"Can't you buy at least a used one? I'm sure you could get a good price.\""
                    j "\"Maybe I could buy one eventually if I got a part-time job, but then I wouldn't have time to practice for my competitions.\""
                    "Oh yeah, there's that..."
                    "Jun's schedule is a lot busier than he makes it look like at times."
                    mc 1 c smile "\"Heh, I tend to forget how much stuff you have to do. You never make it look like you're struggling to do anything.\""
                    show j 1 c watch at fdis
                    j "\"Really? Because I'm struggling all the time.\""
                    "He states that as matter-of-factly as possible."
                    "Honestly, his bluntness blows my mind sometimes."
                    mc 1 c wince "\"R-Really? Most people wouldn't admit that so readily...\""
                    show j 1 c think at fdis
                    j "\"But it's true. I have to study so my grades won't fall too much, I have to practice all the time for my competitions, I mostly take care of the house on my own because my parents rarely get home before dawn...\""
                    show j 1 c watch at fdis
                    j "\"And now I even have to make time to hang out with you guys.\""
                    mc 1 c wince "\"W-Well, you don't {i}have{/i} to make time for us.\""
                    show j 1 c wince at fdis
                    j "\"I've had absolutely no social life at some points in my life. Believe me, I {i}have{/i} to. I'm not the sort of person who deals well with solitude...\""
                    mc 1 c curious "\"Oh, really? Would you mind telling me more about it?\""
                    show j 1 c avoid at fdis, fidget
                    j "\"M-Maybe another time. Either way, I don't really feel the need to hide the fact that I'm struggling to do everything. It's really hard for me...\""
                    show j 1 c annoyed at fdis
                    j "\"{size=-2}Especially the studying part.{/size}\""
                    "Well, he's no brainiac, that's for sure."
                    mc 1 c smile "\"I did offer to help you study. Isn't that the whole reason why we came here? So you could have a good outing before we got started?\""
                    show j 1 c wince at fdis
                    j "\"Guh... don't remind me.\""
                    "... How can just the mention of studying get a person so down like this?"
                    "This tiger really is a mystery to me..."
                    scene Amusement
                    show j 1 c happy at fdis, five
                    with fade
                    j "\"Haaah, that was really fun~\""
                    "The ride lasted a lot longer than I had hoped but I will admit that it was kind of relaxing."
                    "Plus, it's worth it if it means I get to see Jun looking so happy and relaxed like this."
                    mc 1 c smile "\"That certainly was... something different from what I'm used to.\""
                    j "\"Do you want to go again?\""
                    "God no!"
                    mc 1 c considerate "\"... Let's stick to going on rides we haven't tried yet.\""
                    j "\"Okay!\""
                    "So happy-go-lucky..."
                    "Let's see, our next ride should be..."
                    stop music2 fadeout 2.5
                    play music3 "music/BGM/Spring Classroom.ogg" fadein 5.0
                    jump ride

label Ferris:
    scene AmusementNight
    show j 1 c wince at fdis, five
    with fade
    play music "music/night.ogg" fadein 5.0
    "Despite how a ferris wheel is giant by nature, Jun still manages to find a way to get us lost in the park."
    j "\"I-I really thought we'd get there if we turned to the left on the intersection...\""
    mc 1 c sigh "\"Are you still on that? It's been almost half an hour, suck it up already!\""
    j "\"Guh...\""
    "In the end, it took us quite a bit of time to find our way into the ferris wheel waiting line."
    "At this point, the sun has already set completely."
    show j 1 c pout at fdis
    j "\"I really wish there were more stars in the sky tonight.\""
    mc 1 c "\"Just be glad it's not raining.\""
    show j 1 c sigh at fdis
    j "\"So I'm not allowed to complain just because {i}maybe{/i} it could have been worse?\""
    mc 1 c happy "\"That's right!\""
    show j 1 c annoyed at fdis
    j "\"Uhh... so unfair.\""
    "He tries to glare at me, but his face is more comical than threatening."
    "I can't help but find it amusing."
    "Sorry, Jun. I'm trying to take you seriously but I just can't."
    mc 1 c smile "\"Good thing we're almost to the other end of the line.\""
    show j 1 c think at fdis
    j "\"Yeah. I was afraid the line was going to be bigger now that it's nighttime.\""
    mc 1 c think "\"Well, it's certainly one of the toys with the most people lining up, that's for sure.\""
    "Although I'm slightly concerned by the fact that almost all the people in line here are couples."
    "... Ferris wheel + night view = romantic?"
    "Ugh... now I'm starting to feel a little awkward about this..."
    mc 1 c considerate "\"H-Hey, Jun. Just how much were you looking forward to going on the ferris wheel? I mean, it or any other ride, isn't it really all just the same to you?\""
    show j 1 c happy at fdis
    j "\"Hmm... Not really, I've been looking forward to going on a ferris wheel since I was a little kid.\""
    play sound "music/stab.ogg"
    "Ugh!"
    "G-Guess I have no choice. I can't back away from this after he said this much."
    "No, wait, why do I even care in the first place?"
    "I'm just a guy going on a ride with his friend who is also a guy."
    "I mean, nothing weird about that. We're both guys, right?"
    "... No, somehow it still doesn't sit right with me."
    "I can't let him notice that I'm feeling a little uncomfortable about it."
    j "\"Oh, hey, it's our turn in the ferris wheel already!\""
    mc 1 c wince "\"O-Oh, right.\""
    "I kept moving along with the line and didn't even notice we were the next ones."
    "We step into the gondola and it shakes lightly upon receiving our weight."
    "Luckily enough, the gondola is quite spacious. Jun and I both sit on opposite ends of it."
    "The walls have big glass windows to allow us to see outside without any risk of falling."
    "Once the door closes, the ferris wheel begins moving again, carrying us up."
    show j 1 c cshock at fdis
    j "\"Whaaa- it's shaking, our gondola is shaking!\""
    "Jun grabs onto the rails of the gondola, looking down at the floor with a pale face."
    mc 1 c smile "\"Don't worry, it's normal for it to shake. Just stay still on your seat and it won't shake as much.\""
    show j 1 c wince at fdis
    j "\"O-Okay...\""
    "He sits upright on his seat, leaning his back against the cushioned wall of the gondola and looking out the window."
    show j 1 c shockb at fdis
    j "\"Wooooooow! The view from up here is amazing!\""
    "I follow his gaze and look outside."
    scene FerrisWheel with fade
    play music2 "music/BGM/The People Here.ogg" fadein 5.0
    mc 1 c shockb "\"Wow, you're right. It's really beautiful.\""
    "As we reach the highest point of the ferris wheel, we are allowed to look down at the ground, seeing all of the park and parts of the town from a distance."
    "With all of the lights on and the night sky above, we see a giant array of colors painting the horizon."
    "Some of the lights stay on all the time, others blink at long intervals, others twinkle rapidly."
    "The show of lights and colors is captivating."
    "If only the sky had more stars then this would be the perfect view."
    show j 1 c happy at fdis, five
    j "\"This is even better than I thought it'd be...\""
    "From the corner of my eye, I see Jun pressing himself up against the window."
    "It's a sight that warms the heart."
    mc 1 c happy "\"I agree. I'm really glad you decided to take the ferris wheel, Jun.\""
    "Because, to be honest, I hadn't even thought about it."
    j "\"Hehehe, thanks. I'm just happy you didn't say no.\""
    mc 1 c wince "\"W-why would I say no?\""
    "Not that I wasn't tempted to. I really thought this could end up being awkward."
    "But after getting here with him, I see now that I was being ridiculous. There's nothing awkward about this."
    show j 1 c considerate at fdis
    j "\"I don't know. We went to all these rides that you don't really find all that fun.\""
    show j 1 c wry at fdis
    j "\"I was fully expecting you to say no at the end and go ride the roller coaster or something of the sorts.\""
    mc 1 c wince "\"I wouldn't just abandon you in the park!\""
    show j 1 c gentle at fdis
    j "\"Hahaha. Guess I was just imagining things.\""
    "The ferris wheel continues to spin very slowly, shifting our view all the same."
    "Every time it moves, we see a new light that we couldn't from another angle."
    "Some lights fade away into the horizon, others become bigger and brighter."
    "It's like watching a painting. One that is always moving and shifting, never really staying the same."
    show j 1 c shock at fdis
    j "\"The people all look really small from the top!\""
    mc 1 c smile "\"Yeah. This ferris wheel is really tall after all.\""
    show j 1 c happy at fdis
    j "\"Don't you think it really puts things into perspective?\""
    mc 1 c curious "\"What do you mean?\""
    show j 1 c think at fdis
    j "\"Like, from up here, everyone looks so small. Can you imagine just how small their problems would be when seen from a distance?\""
    mc 1 c sigh "\"Are you trying to go with a clichéd line like \"Our problems are so small in the grand scheme of things\"?\""
    show j 1 c considerate at fdis
    j "\"Hehe, guess I'm not nearly as mysterious or as philosophical as I think myself to be.\""
    show j 1 c happy at fdis
    "Despite this, he looks so happy right now."
    "No, he looks happy all the time."
    "Even if he says he's always worried about his own problems, he still manages to always look happy and cheerful..."
    mc 1 c worried "\"... How do you do it?\""
    show j 1 c watch at fdis
    j "\"Huh? Do what?\""
    "Jun's attention snaps back to me, making him stare at me in curiosity."
    mc 1 c sigh2 "\"You told me you're constantly struggling with everything around you, right? Like... your problems are always weighing you down in your mind?\""
    "He nods, still looking confused."
    stop music2 fadeout 5.0
    mc 1 c sigh2 "\"And yet, you almost always have a smile on you face. It's hard for me to imagine you struggling with anything because you always look so happy.\""
    show j 1 c wry at fdis
    j "\"Ah.\""
    play music3 "music/BGM/Reminiscing - Piano.ogg" fadein 5.0
    show cg17_pan1 with Dissolve(1.0):
        subpixel True
        xalign 0.0
        linear 0.7
        linear 12.0 xalign 1.0
    "Jun begins scratching his cheek, looking away awkwardly."
    show j 1 c zero
    j "\"Well... it's just that I'm used to it. Compared to... to how things were before, this is really nothing.\""
    show cg17_1
    show cg17_mc1
    show cg17_jun1
    hide cg17_pan1
    with Dissolve(1.0)
    j "\"There was a time when things were really hard for me, but I found out that if I complained about it, all I did was make the people who care about me worry.\""
    j "\"They knew they couldn't do anything to help but they didn't want to see me hurting and struggling. So, in the end, all I did was burden them even further.\""
    show cg17_mc2
    show cg17_jun2
    hide cg17_mc1
    hide cg17_jun1
    with Dissolve(1.0)
    j "\"So I just decided to smile whenever I was feeling particularly sad. If I could at least keep everyone I care about from having to worry about me, then I wouldn't feel like such a burden.\""
    j "\"... I guess after  a while, I just got used to it. I still get sad but I always try to smile.\""
    j "\"Because I don't want anyone to worry about me.\""
    "..."
    show cg17_junclose
    hide cg17_1
    hide cg17_mc2
    hide cg17_jun2
    with Dissolve(1.0)
    "Although he smiled like he always did when he said those words, for the first time I noticed..."
    "Even if he was smiling, his face was strained."
    "His mouth wasn't open as wide as usual, his eyebrows were furrowed, his eyes were creased."
    stop music3 fadeout 5.0
    "I never really stopped to pay attention to it..."
    "Has he been smiling like this for us and I just didn't notice it?"
    "... I don't want to see him make these kinds of expressions."
    show j 1 c considerate at fdis, fiveh
    hide cg17_junclose
    with Dissolve(1.0)
    menu:
        "Hug him and try to encourage him.":
            play music2 "music/BGM/Little by Little I Walk - Piano.ogg" fadein 5.0
            $ day10hug = True
            "I step up from my seat and walk over to Jun."
            show j 1 c watch at fdis
            j "\"[povFirstName]-s-\""
            play sound "music/fabric.ogg"
            show j 1 c shock at fdis
            "And I wrap my arms around him, squeezing the tiger tight."
            show j 1 c shockb at fdis, shake1
            j "\"Awawawawawawawa, [povFirstName]-san, w-what are you doing?\""
            mc 1 c considerate "\"Sorry, Jun... I never really noticed.\""
            show j 1 c wince at fdis
            j "\"T-That's fine, that was the point!\""
            "I shake my head sideways."
            mc 1 c wry "\"If you really didn't want me to know then why did you tell me?\""
            j "\"B-Because you asked...\""
            "I shake my head again, more vigorously this time."
            mc 1 c considerate "\"That's a lie, isn't it?\""
            show j 1 c blush at fdis
            j "\"A-Augh...\""
            "Jun makes a pitiful noise."
            "Even without looking, I just know his cheeks must be red right now."
            show j 1 c wince at fdis
            j "\"... I thought that... it'd be okay to open up to you.\""
            j "\"Hehe, you're always doing so much for me, [povFirstName]-san. You're so kind and gentle to me, even though I'm basically a stranger.\""
            show j 1 c considerate at fdis
            j "\"I'm sure that if I hadn't met you, I wouldn't have been able to summon up the confidence in myself to try my hardest at the competition.\""
            j "\"I also know that if you weren't there, I would never have managed to make friends.\""
            show j 1 c wry at fdis
            j "\"I'd have stayed alone in my shell, keeping everyone at arms length... I got used to it, but it really gets lonely at times.\""
            show j 1 c considerate at fdis
            j "\"I... I was just tired of being alone, but after trying so hard to make everyone think that I'm okay I... I forgot how to rely on people...\""
            j "\"I just thought that... that it'd be okay for me to rely on you a little more. When you asked me about it, I thought you weren't the kind of person who'd judge me for it...\""
            j "\"No, it's not even that... I guess I just wanted to get it off of my chest after so long, hehe...\""
            show cg17_pan2 with Dissolve(1.0):
                subpixel True
                yalign 1.0
                linear 0.7
                linear 9.0 yalign 0.3
            "He tries to laugh it off but his voice gets meeker with every word that comes out of his mouth."
            "He's choking and trying hard not to sob."
            "Jeez, what a crappy friend I am... I never really cared to see if he really was okay."
            "Come to think of it, haven't I been like this for a long time?"
            "I've been pushing everyone away because I've been struggling with my own goals. I've been so absorbed in my own problems that I didn't care to see behind the masks..."
            "Is Shoichi really okay with all of the responsibilities he has to juggle in his life? Is Keisuke really doing well despite how much pressure his family puts on him?"
            "I never really bothered to ask... instead of paying attention to the people around me, I've just been retreating into my own little space, not bothering to really listen..."
            "I really am the worst..."
            hide cg17_pan2
            show cg17_2
            with Dissolve(1.0)
            stop music2 fadeout 5.0
            mc 1 c zero "\"Sorry, Jun... I promise I'll pay more attention from now on, okay? So please rely on me if you need any help.\""
            j "\"Yeah...\""
            "The small tiger I'm cradling in my arms nods meekly, pushing his face against my chest and finally wrapping his own arms around me."
            "We stay like this until the ride is over."
        "Keep your distance to not make him uncomfortable.":
            play music2 "music/BGM/Memories - Slow Piano.ogg" fadein 5.0
            $ day10hug = False
            "I clench my fists really hard, so much so that I can feel my claws threatening to puncture my hand."
            "But it is the only way to keep myself from following up on the impulse that's welling up inside of me."
            "I just want to reach out and hug him. I want to hold him tight and tell him how sorry I am that I never noticed."
            "But that would just trouble him further, wouldn't it?"
            "I think it's best if I keep my impulses in check so as to not bother him any more."
            mc 1 c avoid "\"I'm sorry I never noticed...\""
            show j 1 c considerate at fdis
            "Jun shakes his head sideways, smiling again."
            "The same fake smile he told me about. It just makes me clench my fists even tighter."
            j "\"Don't worry about it. It's just something that I have to deal with by myself.\""
            j "\"Even if I don't ask for it, the people around me are still helping me through it.\""
            show j 1 c wry at fdis
            j "\"You guys all give me encouragement to pursue my dreams, and you also help me study.\""
            show j 1 c considerate at fdis
            j "\"Hehe, you guys really take my mind away from my problems when I need it the most. So I can't really ask for anything else.\""
            j "\"Everyone has problems of their own, don't they? You just have to learn to deal with them.\""
            mc 1 c avoid "\"Yeah, but-\""
            "I choke, unable to say the words that I'd been meaning to say."
            "They wouldn't reach him. As I am right now, my words would be meaningless."
            "\"But I still want you to rely on me\" are the words that I can't say."
            "Rely on me? How can I ask anyone to do that? I haven't even been dealing with my own problems."
            "A false pretense. I myself have only been running away from my problems."
            "I've been taking steps to fix it recently, but the reality of the situation is that I've been so frustrated with my career in tennis that I've been neglecting everything else."
            "My studies, my friends, my family... I've pushed everything away and kept everyone at a distance because I didn't want any reminders to how much I've been struggling."
            "Because hearing them encourage me and not being able to follow up on their expectations hurts..."
            "I have no right to tell him to rely on me and to let me help him when I haven't even been helping myself."
            "If one of my friends were suffering, I wouldn't notice because I never really bothered to look."
            "I'm the worst..."
            stop music2 fadeout 5.0
            show j 1 c smile at fdis
            "Unable to get any words out, I just watch him snap his attention back to the view."
            "Seeing him being so engrossed in something calms by mind."
            "But eventually, the time for us to leave the ride comes..."
    scene Street1N with fade
    show cg17_a at offscreenleft
    show cg17_b at offscreenleft
    show cg17_c at offscreenleft
    "After leaving the park, we make our way home, quietly basking in the moonlight."
    "The streets are fairly empty this time of night, with only a few people passing here and there."
    "It's really surprising how quiet this area of the city becomes at night."
    "A comfortable silence."
    j 1 c watch "\"Hey, [povFirstName]-san?\""
    "I'm snapped back to reality by the voice of the tiger walking next to me."
    show j 1 c watch at fdis, fiveh with dissolve
    mc 1 c considerate "\"Ah, yes?\""
    j "\"You seem a bit out of it. Is everything okay?\""
    mc 1 c worried "\"Of course. I'm just a bit lost in thoughts right now.\""
    j "\"Hmm...\""
    "Jun looks me up and down, examining my expression."
    "... It feels like being examined by a doctor. So invasive..."
    show j 1 c think at fdis
    j "\"Well, I guess that's okay. Even I get lost in thought at times!\""
    "If by \"at times\" you mean \"all the time\" then sure."
    mc 1 c curious "\"... What do you usually think about when you get lost in thought?\""
    show j 1 c watch at fdis
    j "\"Hmm? That's a bit of a weird question isn't it?\""
    mc 1 c considerate "\"Ah, s-sorry. I just got a bit curious.\""
    show j 1 c happy at fdis
    j "\"It's alright."
    show j 1 c think at fdis
    extend " Let's see, what do I usually think about? Hmmm...\""
    j "\"I think about what foods I want to eat when I get home, or what games I wish I was playing at the time, or about a song I want to hear. Oh, I also think about places I want to visit and-\""
    "... He and I are totally different breeds aren't we?"
    "Whenever I get lost in thought, I always think about the things that trouble me..."
    show j 1 c pout at fdis
    j "\"[povFirstName]-san, you were spacing out again!\""
    mc 1 c fsmile "\"A-Ah, s-sorry!\""
    j "\"Don't you know it's rude to people if you don't pay attention to what they're saying?\""
    "You're the last person I want to hear that from!" with hpunch
    "I sigh, suddenly feeling very drained."
    show j 1 c watch at fdis
    j "\"Are you sure you're okay?\""
    mc 1 c sigh "\"Yeah, I just have a lot on my mind at the moment.\""
    "Jun puts his hands behind his head, looking up at the sky."
    show j 1 c think at fdis
    j "\"Yeah... Shoichi-san told me you're having a hard time with tennis recently. That's what you're worried about, right?\""
    "Not really, but... first of all..."
    mc 1 c sigh2 "\"... Why would Shoichi tell you that in the first place?\""
    show j 1 c watch at fdis
    j "\"Hmmm, he said something along the lines of \"If he says something that sounds really mean or condescending, don't mind it. He has a lot going on in his life at the moment so just give him space\".\""
    "... I'm going to kill him. I swear I'm going to kill that dog..."
    "Jeez, all the people around me are being so considerate of my circumstances and I never really noticed."
    "I really am the worst."
    j "\"By the way, [povFirstName]-san, do you mind if I ask another question about you guys?\""
    mc 1 c smile "\"Oh, sure. What is it?\""
    show j 1 c think at fdis
    j "\"Well... A few days ago you told me about how you met Shoichi-san and Mizoguchi-san... What about Urushihara-san though?\""
    mc 1 c "\"Ah, well... I don't really have as much of a past with Kei-kun as I do with the other two. I had played against him a few times back when I was in junior high but we never really talked back then.\""
    mc 1 c think "\"The first time we really interacted was when he joined the same school as I did. We were both members of the same tennis club and ended up getting to know each other.\""
    mc 1 c "\"At first he mostly talked to Saya and made friends with her, then she introduced him to our group.\""
    mc 1 c considerate "\"It's funny when I think about it. I always thought that Keisuke fit right into our group but, in reality, he always felt like an intruder.\""
    mc 1 c smile "\"It wasn't until recently that all this changed.\""
    show j 1 c watch at fdis
    "Jun walked alongside me, watching me intently as I talked."
    "I can't imagine how a conversation like this can even be interesting for him in the first place."
    "Could it be that he's just trying to get me to talk about something he thinks will make me feel better?"
    j "\"What happened that made him feel like part of the group?\""
    mc 1 c smile "\"We talked. Back when class had just started at the beginning of the month, Kei-kun and I had a serious talk about it. I told him it was crazy for him to feel like that and that he was already one of us.\""
    mc 1 c think "\"Well, I did go out of my way after that to include him in everything we did. I didn't want him to feel so excluded.\""
    show j 1 c happy at fdis
    j "\"That's very nice of you. I never really thought that Urushihara-san and I were so similar in that regard.\""
    "Similar?"
    mc 1 c wince "\"... Don't tell me you feel like you don't belong with us too.\""
    show j 1 c smile at fdis
    "Jun smiles, looking up at the sky again."
    j "\"Sometimes I do. You're all so kind to me and always include me, but I sometimes feel like I mess up the group dynamic. I kinda feel like you guys just ask me to tag along to be polite.\""
    show j 1 c considerate at fdis
    j "\"Of course, I know it's just all in my head but I can't help but feel that way at times.\""
    "Jun has been so honest with me about his worries today... I never really imagined he felt all these things until today."
    mc 1 c worried "\"... I don't want you to feel like that. You're definitely a precious friend of ours.\""
    show j 1 c shock at fdis
    j "\"W-what? [povFirstName]-san?\""
    mc 1 c considerate "\"Sorry, I just said something really sappy all of a sudden didn't I?\""
    mc 1 c worried "\"The thing is... it's really scary how easily you fit into our group. It's like you belonged with us all along.\""
    mc 1 c considerate "\"But your easy-going personality always makes us feel really at ease. You're really good at easing the tension at times, and you're fun to hang out with.\""
    mc 1 c smile "\"We wouldn't go out of our way to include someone if we didn't feel like that person worked well with us.\""
    show j 1 c happy at fdis
    j "\"Yeah.\""
    scene HouseFrontN
    show j 1 c smile at fdis, fiveh
    with fade
    "Eventually, we reach the front of my house."
    "I was just following Jun around and I didn't even notice where we were going."
    mc 1 c shock "\"Wait... my house?\""
    show j 1 c happy at fdis
    j "\"Yeah, I wanted to walk you to your house.\""
    mc 1 c sigh "\"But I thought {i}I{/i} was walking {i}you{/i} to {i}your{/i} house.\""
    j "\"Nah, I can go the rest of the way on my own.\""
    mc 1 c wince "\"I'm not sure if I can agree with that...\""
    show j 1 c pout at fdis
    j "\"Oh, come on, I'm fine. Plus, I'm actually the older one here so it makes sense that I'd be the one dropping you off!\""
    "... I still can't agree with that."
    mc 1 c wince "\"But-\""
    j "\"No buts! Now listen to your senior and go home!\""
    "... I just can't picture him as my senior, even if I know that he is."
    mc 1 c wry "\"Alright alright, jeez. No need to get so prickly.\""
    show j 1 c happy at fdis
    j "\"Hehehe.\""
    "He looks like he's really having fun with this."
    show j 1 c smile at fdis
    j "\"I'll see you at school on Monday. See you, [povFirstName]-san. Thanks for spending the day with me.\""
    mc 1 c smile "\"Of course. And I had fun too. See ya, Jun.\""
    "Jun waves at me and walks off, turning on the next intersection and walking out of my sight."
    "I walk into my house."
    stop music fadeout 2.5
    stop music2 fadeout 2.5
    stop music3 fadeout 2.5
    $ day10 = "jun"
    $ date = None
    jump Day11
