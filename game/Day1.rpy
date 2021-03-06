﻿label Day1:
    stop music fadeout 2.0
    scene Black
    $ povFirstName = renpy.input("What is your first name? Default: Yuuichi", length=15) or "Yuuichi"
    $ povLastName = renpy.input("What is your last name? Default: Michimiya", length=30) or "Michimiya"
    $ povName = povFirstName +" "+povLastName
    if persistent.prologue_played == True:
        "Skip to character selection? The game will tailor choices made in the prologue based on which character you chose last in character selection (by getting all the hearts)."
        menu:
            "Yes":
                $ may2 = False
                $ may8 = False
                $ may9 = False
                $ may10 = False
                $ may11 = False
                $ may12 = False
                $ may15 = False
                $ may17 = False
                $ may18 = False
                $ may19 = False
                $ end = False
                if persistent.picked_character == "Jun":
                    $ reflexes = "True"
                    $ mori_match = "Win"
                    $ jun_met = True
                    $ tour_jun = True
                    $ moresweets = True
                    $ day5 = "jun"
                    $ day10 = "jun"
                    $ day10hug = True
                    $ yuuyawin = True
                elif persistent.picked_character == "Shoichi":
                    $ reflexes = "True"
                    $ mori_match = "Win"
                    $ jun_met = False
                    $ tour_jun = False
                    $ moresweets = False
                    $ day5 = "shoichi"
                    $ day10 = "shoichi"
                    $ day10hug = False
                    $ yuuyawin = True
                elif persistent.picked_character == "Keisuke":
                    $ reflexes = "True"
                    $ mori_match = "Win"
                    $ jun_met = True
                    $ tour_jun = False
                    $ moresweets = False
                    $ day5 = "keisuke"
                    $ day10 = "keisuke"
                    $ day10hug = False
                    $ yuuyawin = True
                jump cs_1
            "No":
                window hide
    scene April3 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene Sky with fade
    window show
    $ date = "day1"
    play music "music/breeze.ogg" fadein 10
    "A cool breeze passes by, softly ruffling my fur. I bask in the mild weather of April, enjoying the feel of the sun against my skin."
    "I can faintly hear the sound of the wind against the trees below and the chirping of birds above."
    "I'm content to just laze around and watch the clouds in the sky. It has always been a good way to kill time when I had nothing better to do."
    "Lately, though, it has developed into a habit."
    "As I lay on the ground counting clouds, I feel myself drifting away into sleep."
    "Just keeping my eyelids open seems like an impossible fight at this point."
    "I'm tempted to just reach into my bag and grab my gaming console, but the thought of playing while fighting my urge to sleep is too troublesome."
    play sound "music/schoolbell.ogg"
    "I am snapped out of my sleep induced daze by the sound of the school bell."
    "Is it already this late?"
    "Slowly, I hear voices. At first there are only a few, but they keep increasing little by little."
    "Students are probably leaving the auditorium now and are heading towards their classrooms."
    "Others are likely carrying around pamphlets and trying to recruit new students for their clubs."
    "I don't even have to look to know what's happening. It's the same scene every year, after all."
    "Just the thought of being pushed around by all those people who keep trying to go to a million different places gives me a headache."
    "I suppose I should head into class myself..."
    "Then I remember that {i}that{/i} teacher is going to be in charge of our homeroom this year."
    "I think I'll just stay here and catch some sleep. Seems like the more comfortable approach."
    play sound "music/metaldoor.ogg" fadein 1.0
    "As I begin to feel the sweet calling of dreamland, a sudden noise snaps my mind back to reality."
    "Did some student decide to wander onto the roof?"
    "Students aren't allowed up on the roof so no one is supposed to come here..."
    "As for me... I just come here for the peace and quiet. It's a great napping spot after all."
    play sound "music/footsteps concrete.ogg"
    "The sound of approaching steps echoes, I move my ears a bit to be able to hear it better."
    "Is it... is it coming towards me?!"
    "Crap, have I been caught?!"
    sw "\"I had a feeling you would be here...\""
    "My ears twitch to the sound of a familiar voice. My body relaxes almost instantly."
    "Thank God... it's not trouble."
    show s 1 u wry at fdis, five with moveiridis
    "I slowly open my eyes, holding a hand up to block the sunlight from assaulting my vision."
    "Standing atop me is a tall guy my own age with a kind, wry smile across his face."
    "His bright green gaze looks directly at my eyes, nearly as bright as the morning sky above it."
    "He looked like he didn't know whether he wanted to commend or chastize me."
    "So in the end, he merely stood at that same spot, looking down at me with indecision."
    "Finally, he sighed, scratching his chin and continuing to watch me with that smile."
    s "\"You do know morning assembly is already over, right?\""
    scene SRooftop
    show s 1 u smile at fdis, five
    with fade
    stop music fadeout 3.0
    play music2 "music/BGM/Windswept.ogg" fadein 6
    play sound "music/fabric.ogg"
    "He sits down next to me with a huff, turning around to look at my face with a smile."
    s "\"I don't know how you manage to keep evading the teachers every single year, but they were royally pissed this time. I think your luck just might have run out.\""
    "I'm somewhat taken aback by this nonchalant attitude."
    "Shouldn't you be a little more pissed?"
    "I really thought he had come over to drag me to the Staff Room."
    "He puts both his arms behind his head and lies down on the ground next to me."
    "I can feel the heat radiating from his body. Our arms slightly graze one another."
    "Ah, I'm still feeling a little drowsy. Guess I might sleep for a few more minutes."
    show s 1 u at fdis
    s "\"By the way, my sister was looking for you this morning. Did you speak to her?\""
    "His voice breaks the pleasant silence from before. I don't really feel like speaking so I just nod along."
    "His tail shifts around next to him, whipping me in the legs."
    show s 1 u displeased at fdis
    "I turn my head slightly so that he's in my sight."
    "He looks somewhat annoyed by my lack of words."
    "Eh... what a pain."
    mc 1 u sigh "\"She asked me to show her around school. I said that she should probably ask you instead. She wasn't amused.\""
    show s 1 u smile at fdis
    "Shoichi holds back a laugh."
    mc 1 u sigh "\"She also asked me if she looked cute in her new uniform. I told her it was \"so so\". She was {i}not{/i} happy about that.\""
    show s 1 u laugh at fdis
    "This time, he's unable to hold back and laughs softly, his shoulders moving up and down at a pleasant rhythm."
    mc 1 u happy "\"She tried to hit me with her bag. Lucky for me, I'm a fast runner.\""
    "Shoichi doubles over, clutching his stomach as he continues on his fit of laughter."
    mc 1 u judge "\"It's not funny. Your sister is the devil.\""
    s "\"Sorry, sorry. I know I shouldn't laugh.\""
    show s 1 u sigh at fdis
    "He takes a few deep breaths, trying to stabilize himself."
    "Little by little, his shoulders stop quivering."
    s "\"Okay...{nw}"
    show s 1 u laugh at fdis
    extend " I think I'm okay now.\""
    "Really? Because you still look like you're about to burst into fits of laughter at any minute now."
    show s 1 u smile at fdis
    s "\"Sorry she was such a pain, she actually spent most of the summer sending me photos of her in different clothes, asking me what would look good for her first day of class.\""
    show s 1 u sigh at fdis
    s "\"At first I thought she was joking, but when the semester was close to starting and she hadn't stopped, I sent her a message reminding her of the uniform.\""
    mc 1 u "\"And?\""
    show s 1 u at fdis
    s "\"She got mad at me because I \"didn't tell her sooner\".\""
    "Really? A high school student has to be reminded of the existence of the school uniform? Talk about a blunder."
    show s 1 u smile at fdis
    s "\"Oh, and it looks like she still has a major crush on you!\""
    mc 1 u wince "\"Ugh... don't remind me.\""
    "When we were kids, Hitoka had a serious older brother complex. Always following us around and saying that she wanted to marry her \"big bro\" when she grew up."
    "In fact, I remember teasing Shoichi about it all the time..."
    play sound "music/disappointment.ogg"
    "{size=+4}Why did she have to fall for me?{/size}" with hpunch
    "... If I let him know how much it annoys me, he'll tease me mercilessly for the rest of the day."
    "Time for a tactical retreat. Change of subject!"
    mc 1 u wince "\"... Is your dad still out of town?\""
    "... That was the first thing that came to mind."
    "Oh God, I suck at this."
    show s 1 u seductive at fdis
    "His eyes say \"Really? That's the best you can do?\", but he still lets it slide."
    show s 1 u smile at fdis
    s "\"Yeah. Business trip to Taiwan. He'll stay there for most of the semester.\""
    mc 1 u "\"Why don't you stay with your mom in the meantime? I'm sure she'd be thrilled about it. Hitoka too.\""
    show s 1 u wince at fdis
    "At that moment, the look on his face is enough to tell me that I said something I shouldn't have."
    s "\"That's... an idea... but I don't really feel comfortable there. I feel like an outsider. Their house has stopped being my home a long time ago.\""
    show s 1 u at fdis
    s "\"Plus, someone has to watch over our house, so it's better if I stay there.\""
    show s 1 u laugh at fdis
    s "\"It's not all bad, though. At least I can enjoy not having someone breathing down my neck about the chores that need to be done.\""
    "And yet, I'm sure you will do them all regardless."
    "Come to think of it... I don't really remember much of his current house. I didn't really visit much since his parents got divorced."
    "Maybe I should go there sometime to keep him company?"
    "I know he still has a hard time dealing with the divorce, even if he likes to pretend that everything is fine."
    mc 1 u smile "\"Maybe I could come over? I'll even bring one of my gaming consoles.\""
    show s 1 u smile at fdis
    s "\"Oh, that actually sounds like a great idea. Bring the Mega Neptune, then. It has the best fighting games!\""
    mc 1 u judge "\"Fighting games? Again? Are those the only ones you can play?\""
    show s 1 u laugh at fdis
    s "\"No, but they're the only ones I can actually beat you in.\""
    "How can he say something so sad with such a smile on his face?"
    show s 1 u smile at fdis
    mc 1 u smile "\"Fair enough. I'll see if I can get some free time this week. I can go over and spend the night. We could pull a gaming all-nighter.\""
    s "\"Deal! Well, except the part about the all-nighter. I don't think it'd be a good idea to lose sleep.\""
    "Boo, such a goody two shoes!"
    "It feels so natural to see him smiling all the time... it's weird to think that he isn't always like this."
    "Whenever he's dealing with the few people that aren't part of his group of friends, he always has such a serious look on his face."
    "Honestly, it feels like two completely different people."
    play sound "music/fabric.ogg"
    "He starts leaning back to lie on the floor as well, but just as his back is about to touch the floor, he shoots up."
    show s 1 u shock at fdis
    stop music fadeout 5.0
    s "\"Shoot, I almost forgot!"
    show s 1 u at fdis
    stop music2 fadeout 2.5
    play music "music/breeze.ogg" fadein 5.0
    extend " Saya-chan asked me to bring you over after she's done instructing the new club members.\""
    "Guh... I was hoping she wouldn't have gone that far."
    mc 1 u fsmile "\"N-nah, she's mistaken. I've taken a day off since there isn't anything important we need to do today.\""
    show s 1 u sigh at fdis
    s "\"Is that so? Shouldn't the vice captain be there to be introduced to the new members?\""
    "Shoichi shoots me such a suspicious look that I'm afraid he won't buy it."
    s "\"Eh, I guess I'll just give you the benefit of the doubt on this one.\""
    "... Luckily, he merely shrugs it off."
    "I just managed to make up a convincing lie on the spot. Good going, me!"
    s "\"The tennis club has things so easy. We had to jump through all sorts of hoops to get permission to use the courts during the break.\""
    show s 1 u scorn at fdis
    s "\"Meanwhile, you guys had free access to them every day. It's so unfair.\""
    mc 1 u cocky "\"If you want better treatment, maybe you guys should start winning more.\""
    "I had planned on getting up and bolting long before I finished my sentence, but I seem to have overlooked one fatal flaw in my plan..."
    "My body is still feeling sluggish from sleep, taking too long to move. In that time, Shoichi-"
    stop music fadeout 3.0
    play music2 "music/BGM/Punchline - Org.ogg" fadein 6.0
    play sound "music/tap.ogg"
    show s 1 u doom at fdis:
        ease .2 zoom 1.5 xoffset -30 yoffset 200 #moves right 100px, bottom 50px. set to 0 when you return later.
    "Unable to get up on time, I'm grabbed in a choke hold by Shoichi, who immediately starts grinding his fist at my head."
    s "\"Hoho, was it my imagination? I could have sworn I heard a little brat trash talking my precious volleyball club. It couldn't have been you, right?\""
    "While this might seem like a bad situation for an average person, I'm already so used to this kind of treatment that it doesn't even faze me."
    "In fact, even if Shoichi is a little annoyed at my comment, this is nothing more than rough play for him."
    "If he really wanted to hurt me, I'd have no chance. That guy is freakishly strong!"
    "While he definitely has his arm wrapped around my neck, the \"noose\" is loose enough that I can get out whenever I want."
    "Still, I decide to humor him and play the part."
    mc 1 u laugh "\"Gaaah, Shoichi-san, I'm sorry I'm sorry. Please forgive me. Let me go!\""
    show s 1 u doom at shake1, fdis
    s "\"Glk...\""
    "Shoichi's body rumbles as he makes a choking noise."
    show s 1 u laugh at fdis
    stop music2 fadeout 2.5
    play music3 "music/BGM/Dazzling Sunlight.ogg" fadein 5.0
    s "\"Bahahaha!\""
    "Unable to hold it in, Shoichi begins to laugh with me still in his grip. Feeling his body vibrating like that is a strange, albeit familiar sensation."
    "But even though he can barely restrain his laughter, he continues to play his part."
    s "\"If you think forgiveness is going to come that easily, then you're sorely mistaken. It would take you at least one hundred years to achieve penance.\""
    mc 1 u laugh "\"Ahahaha, wait, Shoichi, you're tickling me. And what's with that number? Be more realistic!\""
    "Playing around like this is so nostalgic. It makes me miss the days of our childhood together."
    "... Well, not that those days ever really left. After all, we {i}are{/i} rolling around on the rooftop in plain daylight."
    show s 1 u laugh at fdis:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    "Shoichi gently pushes me away from him, giving me a tap on the shoulder."
    s "\"Away with you, now, heathen. I am done with your punishment.\""
    mc 1 u judge "\"Heathen? When did this become an inquisition?\""
    show s 1 u smile at fdis
    s "\"I don't know. I just always wanted to say a line like that.\""
    "He's acting so silly right now that I can't help but laugh."
    "Whenever we get together, we end up fooling around like little kids."
    "It's why we stopped studying together. We could never get things done."
    show s 1 u at fdis
    s "\"This is our last year, you know. You should try enjoying high school life a little more.\""
    "Whoa. The change of subject came so fast that I can feel some whiplash."
    mc 1 u judge "\"I am enjoying it. And also, what's with the sudden change of subject?\""
    show s 1 u sigh at fdis
    s "\"No you're not. You barely speak to anyone in school other than Saya, Urushihara and me.{nw}"
    show s 1 u at fdis
    extend " And \"that\" came from me being worried about you. You should be happy.\""
    mc 1 u sigh "\"Alright... {i}Mom{/i}. And for your information, I have plenty of friends.\""
    show s 1 u sigh at fdis
    s "\"Casual acquaintances aren't the same thing as friends, and I know that all of your classmates fall into that category.\""
    mc 1 u annoyed "\"That's not true. You're just overstating the requirements to friendship.\""
    s "\"Is that so?\""
    "I shrug. Nothing I can say to change his mind, so I won't really bother to."
    show s 1 u at fdis
    s "\"By the way, what time is it now? I can't hear the students downstairs anymore.\""
    "... Huh, that's true. It's gotten pretty quiet."
    mc 1 u shock "\"I can't either..."
    extend mc 1 u judge " Wait, why are you asking me that? Just check your phone.\""
    s "\"I left it in my bag.\""
    mc 1 u sigh "\"Pfft, you're so unprepared.\""
    play sound "music/phonebeep.ogg"
    "I pull my phone out of my pocket and look at the time."
    "Woah, it's already past 11AM!"
    mc 1 u shock "\"11:35?!\""
    show s 1 u shock at fdis
    "Shoichi almost shoots up."
    s "\"Shit, I'm late. I'm supposed to be helping with the new team members.\""
    mc 1 u nervoussmile "\Sorry I held you up here for so long.\""
    "Shoichi gets up quickly, dusting his clothes off."
    show s 1 u wince at fdis
    s "\"Is there any dirt on my back?\""
    mc 1 u sigh "\"No, it's fine. They clean the rooftop every day, you know.\""
    show s 1 u sigh at fdis
    s "\"Doesn't change the fact we were lying around on the floor.\""
    mc 1 u sigh "\"If this was going to be such a problem then why did you do it in the first place?\""
    s "\"It didn't feel like a problem at the time. I'll chalk it up to a lack of foresight.\""
    show s 1 u smile at fdis
    s "\"Now come on, I'm sure you have better things to do than fall asleep on a school rooftop. Even if you end up skipping practice.\""
    stop music3 fadeout 4.0
    play music2 "music/BGM/The People Here.ogg" fadein 8.0
    hide s 1 u smile
    show cg1
    with dissolve
    s 1 u smile "\"Here, let me help you.\""
    "Shoichi leans down towards me, offering me a hand."
    "Seeing the blue sky shining brightly behind him and the gentle breeze ruffling his fur... for some reason I can feel myself blushing."
    "Without really knowing why, I decide to look away and attempt to hide, like a kid that got caught doing something bad."
    mc 1 u avoidb "\"I-I don't need help, I'm not a baby!\""
    s 1 u happy "\"I'm not saying you are. But what's wrong with me trying to do something nice for a friend? I just want to help you.\""
    "Damn smooth talker..."
    "Despite my protests, I still grab hold of his hand, with him pulling up to my feet with ease."
    $ renpy.music.set_volume(0.3, 0.0, channel="sound")
    play sound "music/tap.ogg"
    "He actually pulls me with too much force, and we end up bumping chests."
    "My face lands square on his shoulder."
    "It never ceases to amaze me how deceptively strong he is."
    "I mean... he already looks strong. But he's still much stronger than he looks."
    "If that makes any sense."
    $ renpy.music.set_volume(1.0, 0.0, channel="sound")
    mc 1 u annoyed "\"Ow! Jeez, you're way too strong. Try to reign it in a little, you're gonna end up throwing me off the building!\""
    s 1 u laugh "\"Hehe, sorry. You have so much fluff that you look much stockier than you really are.\""
    mc 1 u annoyed "\"What's {i}that{/i} supposed to mean?\""
    s 1 u happy "\"It's a compliment. I'm saying you're lighter than you look.\""
    hide cg1
    show s 1 u smile at fdis, five
    with dissolve
    play sound "music/gust.ogg"
    show s 1 u wince at fdis
    "Just as I'm pulling away from him, a particularly strong gust of wind blows against us, rustling my fur violently."
    s "\"Waah. It's so windy up here, how do you manage to stay here for so long.\""
    mc 1 u sigh "\"It's not usually this windy up here, you know.\""
    "Plus, you're making for a pretty good wind shield right now with how big you are."
    "Although I decide against mentioning that part."
    show s 1 u shock at fdis
    stop music2 fadeout 3.0
    play music "music/breeze.ogg" fadein 6.0
    play sound "music/phonevibrating.ogg"
    "My pocket starts vibrating with force."
    "I already have an idea who might be calling, so I choose to ignore it."
    show s 1 u at fdis
    "Shoichi, though, has completely stopped. His eyes are glued to my pants pocket."
    s "\"Aren't you going to get that?\""
    mc 1 u "\"Nope!\""
    show s 1 u sigh at fdis
    s "\"It's in bad taste to ignore a call, you know.\""
    mc 1 u sigh "\"Spare me the lecture. I have a pretty good idea of who it is and this will be a conversation I'd rather avoid.\""
    show s 1 u annoyed at fdis
    play sound "music/fabric.ogg"
    stop music fadeout 2.5
    play music2 "music/BGM/Punchline - Org.ogg" fadein 5.0
    "Shoichi gives me a bemused \"Hmm.\" and, in one fast movement, shoves a hand down my pocket, pickpocketing my phone."
    mc 1 u shock "\"Hey, give that back!\""
    play sound "music/phonebeep.ogg"
    show s 1 u laugh at fdis
    s "\"Hello, could this be [povFirstName]'s secret girlfri-"
    show s 1 u at fdis
    extend " Saya-chan?\""
    "Oh-oh. Here's the development I didn't want to see occurring."
    show s 1 u shock at fdis
    $ renpy.pause(1.0)
    show s 1 u judge at fdis
    $ renpy.pause(1.0)
    show s 1 u frown at fdis
    "..."
    "The changes to his expression are already enough to tell me that I'm busted."
    "And screwed."
    "I attempt to stealthily walk away from the situation."
    show s 1 u scorn at fdis
    s "\"You have a match? You told me you were taking the day off!\""
    "Crap..."
    mc 1 u avoid "\"I am! {size=-4}Without consent...{/size}\""
    show s 1 u sigh at fdis
    "Shoichi starts rubbing his forehead."
    s "\"Yeah, Saya-chan. Sure. I'll bring him.\""
    "Noooo..."
    show s 1 u annoyed at fdis
    play sound "music/phonebeep.ogg"
    "Shoichi hangs up the phone and looks at me with a grumpy expression."
    s "\"I don't appreciate being lied to.\""
    mc 1 u annoyed "\"I don't {i}have{/i} to tell you every detail off my every waking moment, do I?\""
    show s 1 u scorn at fdis
    s "\"Well, no... But you have to go to practice.\""
    mc 1 u annoyed "\"Why?\""
    s "\"It's your responsibility.\""
    mc 1 u avoid "\"Again. Why?\""
    show s 1 u frown at fdis
    s "\"Because you're the vice-captain for crying out loud. And this is not up for debate.\""
    show s 1 u frown at fdis:
        ease .2 zoom 1.5 xoffset -30 yoffset 200 #moves right 100px, bottom 50px. set to 0 when you return later.
    play sound "music/tap.ogg"
    "Shoichi grabs me by my shirt collar and starts dragging me."
    mc 1 u shock "\"Waah, I'll go I'll go, you don't have to drag me. S-Shoichi. Shoichi?!\""
    stop music2
    $ renpy.music.set_volume(1.0, 0.0, channel="music")
    $ renpy.music.set_volume(1.0, 0.0, channel="music2")
    play music "music/tennisambiance.ogg" fadein 5.0
    scene SCourt
    show s 1 u sigh at fdis, five
    with fade
    show sa 1 t at offscreenleft
    s "\"Saya-chan, we're here!\""
    show s 1 u sigh at seven with move
    show s 1 u sigh at fdis, seven
    show sa 1 t annoyed at fdis, three with moveiledis
    "Saya stomps her way over to us, nearly knocking down some students that were unlucky enough to be in her path."
    "If this were some kind of manga, I'm one hundred percent sure she'd have smoke coming out of ears."
    $ renpy.music.set_volume(0.7, 2.5, channel="music")
    play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
    show s 1 u wry at fdis
    show sa 1 t angry at fdis
    sa "\"You. Asshole!\"" with hpunch
    mc 1 u wince "\"Gah!\""
    "I am grabbed by the collar of my shirt and dragged to the courts."
    "What's with people always grabbing me by my shirt. I have arms. Grab those. They don't cost money and there is no risk of ripping them!"
    sa "\"There's no way you're running away again!\""
    mc 1 u nervous "\"W-wait. S-Saya-chan. I promise I'm not gonna try to escape. Please stop pulling on my shirt!\""
    "Saya Mizoguchi, one of my dear childhood friends, is the current captain of our school's tennis club."
    "Unfortunately for me, she is incredibly brash and hot-headed..."
    "Even though she looks so innocent and tries to act cute, she's a monster whenever she gets angry."
    "And considering how easy she is to anger, one could say that she lives in a state of constant rage."
    "Standing at 176cm, she's also one of the tallest girls in school, which I find slightly unsettling."
    show s 1 u wry at fdis, nine
    show sa 1 t annoyed at fdis, five
    with move
    show k 1 t sigh at two with moveiledis
    stop music2 fadeout 4.0
    $ renpy.music.set_volume(1.0, 8.0, channel="music")
    kw "\"Mizoguchi-san, I'd like to remind you that our new members are watching this little display here.\""
    show s 1 u at fdis
    "Saya turns around to look at the source of that voice, her nostrils flared and her brows furrowed."
    "Not to mention that huge vein that's pulsing on her forehead."
    "The one addressing her is Keisuke Urushihara, one of our juniors."
    "Despite his age, he's by far the most responsible member of the team and is constantly counseling Saya and I."
    "Sometimes it feels like {i}he's{/i} the one pulling the strings here instead of us seniors."
    show k 1 t at offscreenleft
    show s 1 u at seven
    show sa 1 t annoyed at fdis, three
    with move
    show s 1 u at fdis, seven
    "Not thirty seconds after popping up to speak his mind, Kei-kun has already left to busy himself with something else."
    $ renpy.music.set_volume(0.7, 3.0, channel="music")
    play music2 "music/BGM/On My Way.ogg" fadein 6.0
    "Somehow, it seems that his interference, however brief, was enough to bring her back to her senses."
    show sa 1 t sigh at fdis
    "Saya clears her throat and straightens her clothes, turning around to look at Shoichi."
    "She still maintains a death grip on my shirt collar though."
    sa "\"Right. Anyway, thanks for the help Sho-chan!\""
    show s 1 u laugh at fdis
    s "\"Pfft, don't mention it. Call me anytime this unruly child gives you any more problems!\""
    "He seems to be enjoying himself far more than he should."
    "Bastard, I'll get him back for this."
    "Gym #3, the one that houses the tennis courts, is actually separated in half by a giant locker room. On one side, we have the tennis courts. On the other, we have the volleyball courts."
    "So in the end, it was incredibly convenient for him as he was already bound to come this way anyway."
    s "\"Now if you'll excuse me, I have some captaincy duties to fulfill!\""
    show s 1 u smile at offscreenright
    show sa 1 t annoyed at fdis, five
    with move
    hide s 1 u smile
    "He waves us goodbye, heading towards the locker rooms, supposedly for his own practice."
    "... Meanwhile, I can feel Saya leering at my back."
    "A creeping sense of dread begins to settle."
    mc 1 u fsmile "\"W-Well, Saya-chan. I guess I'll just...\""
    show sa 1 t doom at fdis
    sa "\"Freeze!\""
    play sound "music/stab.ogg"
    "Her voice is so filled of authority that I'm cut down before I even have a chance to speak."
    "Before long, I completely toss away the foolish notion that I ever had a chance to escape."
    show sa 1 t sigh at fdis
    sa "\"Why are you being so troublesome? You know about our club's tradition. We had to delay practice because of you!\""
    "I look away from her, trying to ignore the slight pang of guilt I feel in my chest."
    "She's, of course, talking about our club's special yearly match featuring a junior and a senior player elected by members of those years to represent them in a special one-set match."
    "No one really knows why they initially made it, but nowadays it's accepted as a way to show off our best players to those that are just joining the club."
    "This is why this match takes place at the first day of class."
    mc 1 u wince "\"Do I really have to? I already took part of it last year. Isn't there some kind of attendance limit to allow more people to participate?\""
    "Even as I'm trying to find a way out of it, I already know the best I can do is buy some time."
    "It's true though that I was chosen to represent the juniors last year, defeating the senior's representative by 6-3, the first time in over ten years that the juniors had won."
    "Heh, I was pretty happy about it last year too."
    show sa 1 t bored at fdis
    sa "\"Look, normally I'd give you a pass, but all of the seniors voted for you this year. It'd be unfair to them if I picked someone else.\""
    "Usually we host one match per gender category, so we'd have the girls and the boys playing in separate categories."
    "But still, the guys are still allowed to vote on who they want to see representing the girls and vice versa. It's a pretty neat system."
    mc 1 u fsmile "\"Come on, it can't have been literally everyone. I know for a fact that {i}I{/i} didn't vote for myself.\""
    show sa 1 t sigh at fdis
    sa "\"Don't try to be cute, you didn't even vote at all. You were absent that day.\""
    "Rats."
    show sa 1 t pout at fdis
    sa "\"And yes, you got every single one of the votes. One hundred percent. Is it even that big of a surprise? You're a famous player in all of Japan, of course our guys would want to watch you play.\""
    sa "\"Doesn't help that you have been slacking off in practice for the past year.\""
    "I attempted to act frustrated by sighing as loudly as I can."
    "The hope was that she'd see it and decide to take pity on me."
    "It isn't very effective..."
    show sa 1 t doom2 at fdis
    sa "\"Should I take that sigh as a sign that you've resigned yourself to your fate? Yes? Great, then it's show time!\""
    stop music2 fadeout 2.5
    play music3 "music/BGM/Punchline.ogg" fadein 5.0
    play sound "music/tap.ogg"
    "Saya grabs me by my wrist and starts dragging me to one of the courts."
    "Just as I'm about to truly surrender to my inescapable fate..."
    play sound "music/tap.ogg"
    show sa 1 t doom2 at fdis, seven with move
    show k 2 t sigh at three with move
    show k 2 t sigh at fdis, three
    "I feel a hand touching my shoulder. As I turn around, I'm greeted to the sight of Kei-kun's face."
    k "\"Hey hey, how about we take a little breather here, okay?\""
    show k 1 t sigh at fdis
    k "\"Mizoguchi-san, [povLastName]-san hasn't even changed out of his uniform yet, how is he supposed to play like this? Can't we at least give him some time to get changed?\""
    show k 1 t at fdis
    "K-K-Keisuke, you're the best!"
    show sa 1 t annoyed at fdis
    "Saya stares at him, the bulging vein on her forehead makes another appearance as her brows twitch with frustration."
    "Just when it seems that she might not budge..."
    stop music3 fadeout 5.0
    $ renpy.music.set_volume(1.0, 10.0, channel="music")
    show sa 1 t sigh at fdis
    sa "\"Ugh, fine. But be quick about it, I don't want to have to delay this any longer than I have to.\""
    mc 1 u nervoussmile "\"T-Thank you, I'll be right back!\""
    "I flash Kei-kun a thumbs up as a thank you."
    "Now I just have to plot my esc-"
    show sa 1 t doom2 at fdis
    sa "\"And don't even think of trying to run away, otherwise I'll hunt you down and I'll make a fur coat out of your skin.\""
    "... On second thought."
    stop music fadeout 3.0
    scene SLockers with fade
    "I dash towards the male locker room, trying to get this done as fast as I can."
    "Every second I take makes Saya even more mad and I can't risk that."
    "Just then..."
    show cg19 with Dissolve(1.0)
    "I see Shoichi standing right next to his locker, his eyes just as glued on me as mine are on him."
    "For a second, what is happening doesn't really click for any of us."
    "After all, it's not every day that someone runs into a locker room and nearly crashes into the lockers."
    "Shoichi's hands are still frozen on the waistband of his... underwear?"
    "Whatever it is that he is wearing. His hands are still clutching it as if he had just pulled it up a mere fraction of a second before I walked in."
    "And the entire backside of it is completely bare, especially with him standing frozen like that, giving me a perfect view of his-"
    hide cg19
    show s 1 jo shock at fdis, five
    with Dissolve(1.0)
    play music2 "music/BGM/Punchline - Org.ogg" fadein 5.0
    mc 1 u shock "\"Ah! S-s-s-Sorry.\""
    show s 1 jo shock at fdis, offscreenleft with move
    "I turn around as fast as possible, trying to erase the image of my half-naked childhood friend from my mind."
    "Being so self-conscious around half-naked people... I'm a failure as a Japanese person..."
    s 1 jo sigh "\"Is this really necessary? I'm not packing anything you haven't seen tons of times before.\""
    mc 1 u wince "\"S-s-s-shut up!\""
    "Ugh, I'm not usually this much of a nervous wreck around naked people, but having no time to prepare myself mentally has made me completely shocked to this sudden exposure."
    "And it had to be Shoichi of all people?!"
    "I can hear him softly chuckling from behind me. Probably having a lot of fun at my breakdown."
    "I mean... Seeing someone in their underwear inside of a locker room is no big deal... and it's true that I've seen him wearing less before (no comment on that one)."
    "But... ugh... I was a kid back then. I didn't really understand how embarrassing nudity is."
    "In the end, I can't decide if I should make conversation, move towards my locker or start undressing myself."
    "I just stand frozen with my back turned away from him."
    s 1 jo sigh "\"Your eyes aren't going to fall off if you look at me, you know.\""
    mc 1 u sigh "\"Have you gotten dressed yet?\""
    s 1 jo smile "\"Nope. And I'm not going to until you turn around and look at me.\""
    mc 1 u shock "\"Wha- Why would you do that?!\""
    s 1 jo laugh "\"Cause you're freaking out and it's hilarious!\""
    "Gh... I'm gonna kill him."
    show s 1 jo smile at five with moveiledis
    show s 1 jo smile at fdis, five
    mc 1 u wince "\"T-there, I'm looking... I can see more of you than I'd like to... {size=-2}Oh God, did you have to be wearing a jockstrap, I can see your ass...{/size}\""
    show s 1 jo laugh at fdis
    s "\"Oh, this? It looks pretty snazzy doesn't it?\""
    mc 1 u sigh "\"It looks like something you'd buy at a sex shop. Since when have you worn this kind of skimpy underwear?\""
    show s 1 jo smile at fdis
    s "\"I'll have you know that I bought this at an athletic gear store. And it's actually pretty damn comfortable. It's great to practice in. One of my teammates recommended it to me a few weeks back and I gave it a try.\""
    show s 1 jo laugh at fdis
    s "\"Don't I look great in it?\""
    mc 1 u sigh2 "\"Whatever you want to believe...\""
    show s 1 jo seductive at fdis
    s "\"You know, for someone that's complaining so much about me being half-naked, you sure seem to be interested in my crotch. Your eyes haven't left that area since you turned around.\""
    mc 1 u avoidb "\"S-shut up, I'm looking at the only area of your body that's still clothed!\""
    s "\"Mhm, sure you are. Keep telling yourself that.\""
    "Shoichi turns back to his locker room, picking up a change of clothes."
    play sound "music/fabric.ogg"
    stop music fadeout 2.5
    play music2 "music/BGM/Dazzling Sunlight.ogg" fadein 5.0
    show s 1 v smile at fdis
    s "\"There, I'm dressed. You can stop freaking out now.\""
    mc 1 u sigh "\"T-thank you...\""
    "God, my cheeks are so hot right now."
    show s 1 v seductive at fdis
    s "\"Good thing your house has a bath. I think you'd have a meltdown if you had to shower at school.\""
    mc 1 u sigh "\"I don't doubt that.\""
    show s 1 v smile at fdis
    "I place my tennis bag on a bench and pull out my practice clothes. For a second, I move to undress myself."
    "I see Shoichi with the corner of my eye and freeze."
    "He looks at me in confusion for a few seconds. Then, realization dawns on him and he sighs."
    show s 1 v sigh at fdis
    s "\"You want me to turn my back, don't you?\""
    "I just nod."
    "Shoichi sighs again and turns away from me."
    play sound "music/fabric.ogg"
    s "\"How do you even deal with this when you're staying at a hotel for a tournament?\""
    mc 1 u annoyed "\"I don't use the hotel's bath. I look for a bathhouse with private rooms.\""
    s "\"That's kinda sad.\""
    play sound "music/fabric.ogg"
    mc 1 u annoyed "\"Beats getting naked in front of a bunch of strangers. Alright, you can turn around now.\""
    show s 1 v wry at fdis
    "Shoichi turns over again as I'm adjusting my shirt."
    mc 1 u wince "\"Good thing Kei-kun swooped in to help me. If I had left it up to Saya, she'd have forced me to play in plain school clothes.\""
    show s 1 v displeased at fdis
    "His expression turns sour when I mention Keisuke."
    s "\"Hooray for that.\""
    mc 1 u sigh "\"Still mad over last time?\""
    show s 1 v annoyed at fdis
    s "\"That was my ball and he {i}knew{/i} it.\""
    "For some reason that completely eludes me, these two are always finding some stupid reason to fight over."
    "I swear, it's like placing a burning candle next to gasoline. The slightest thing makes it catch fire."
    mc 1 u annoyed "\"And for the last time: let it go. It's been almost two weeks already.\""
    show s 1 v avoid at fdis
    "Shoichi pouts. God, he's too childish when it comes to Kei-kun."
    s "\"I'll let go when he apologizes.\""
    mc 1 u sigh2 "\"We both know that's never going to happen. Just drop it.\""
    show s 1 v scorn at fdis
    s "\"Why do I have to be the one to accept defeat?\""
    mc 1 u annoyed "\"Because when neither of you is winning, you're both just making me miserable!\""
    show s 1 v sigh at fdis
    s "\"Fine fine, I'll talk to him. You don't have to be rude.\""
    s "\"Well, anyway, I have to get to practice. Talk to you later?\""
    mc 1 u "\"Sure. See ya.\""
    show s 1 v at offscreenright with moveoridis
    "I check my bag to make sure I have everything in order."
    "Once I sure that nothing's missing, I grab my racket and head outside."
    stop music2 fadeout 5.0
    scene SCourt with fade
    play music "music/tennisambiance.ogg" fadein 10.0
    "As I start looking for Saya, I catch Kei-kun stretching alone at a court."
    mc 1 t sigh "\"Oh, you've got to be kidding me...\""
    play sound "music/punch.ogg"
    "Pain suddenly shoots from my shin, making me jump forward, yelping."
    mc 1 t shock "\"Son of a-\""
    show sa 1 t bored at fdis, five with moveiledis
    "I reflexively reach down to my foot, rubbing down the spot that just got brutally assaulted by this monster woman."
    "Saya merely leers down at me with an annoyed look on her face."
    sa "\"What took you so long? Did you get lost inside the locker room? Sheesh.\""
    mc 1 t sigh "\"I ran into Shoichi while I was changing... Also, {size=+6}OW!{/size}\""
    show sa 1 t sigh at fdis
    "At least she's no longer breathing fire from her mouth. She seems to have mostly calmed down."
    "She's only {i}just{/i} annoyed."
    show sa 1 t complain at fdis
    sa "\"By the way, I'm sorry I didn't tell you this before, but Kei is the one you'll be playing against.\""
    show sa 1 t pout2 at fdis
    sa "\"You were kind of a flight risk at the time...\""
    show sa 1 t laugh at fdis
    sa "\"Just like you, he got all the votes in his year. This is the first time our club has ever gotten two players with 100\% of the votes. I'm really excited for this!\""
    "She looks like she might start hopping in place from excess glee."
    mc 1 t sigh2 "\"I've only played against him once and that was a while ago... but I still can't see myself losing to him. Sorry if that sounds cocky.\""
    show sa 1 t at fdis
    sa "\"To be honest, I also think you'll win. But then again, this is tennis. Never put it past your opponent to win by an upset.\""
    show sa 1 t happy at fdis
    sa "\"You should be happy, this will be a great chance for you to practice. You'll probably play against him during the prefecturals anyway.\""
    mc 1 t avoid "\"Yeah, great. Practice I didn't even want to get. Such an amazing opportunity indeed.\""
    "I grumble unhappily in place, still thinking of the throbbing pain in my shin."
    show sa 1 t argue at fdis
    "Goddammit, even if she was just playing around, she kicked way too hard!"
    "She shakes her head sideways, making an exaggerated shrug."
    sa "\"I find your lack of enthusiasm disturbing.\""
    mc 1 t sigh "\"Really? You're quoting {i}Galaxy Warz{/i} in regular conversation now?\""
    "I know she's a film nerd but there's a limit to everything..."
    show sa 1 t happy at fdis
    sa "\"Hey, if it fits the situation then why shouldn't I?\""
    show sa 1 t happy at fdis, offscreenleft with move
    "With a big smile on her face, Saya shrugs one last time before walking away towards the umpire chair, leaving me to watch in dismay as Kei-kun finishes his preparations."
    "Wait, the umpire chair? She's the one that'll be overseeing the match today?"
    "Oh, this is just great. Is our coach absent today again? I swear, that man takes every opportunity he has to slack off."
    "And on the first day of class? Really?"
    "Deciding to think nothing more of it, I proceed to do the most basic warm up, making sure to finish it in less than five minutes."
    "It's not my usual warm up routine, but then again, I don't even care about this match in the first place."
    "I wish I was home..."
    "As I make my way to the court, I can hear some of my club mates whispering here and there, most of them sounding really excited for some reason."
    "I guess Saya wasn't kidding when she said that people had been looking forward to this match..."
    "Damn it, why do I have such a stupid grin on my face? I'm letting the excited mood permeating the gym affect me."
    show k 1 t at five with moveiledis
    show k 1 t at five, fdis
    "I see that Kei-kun is waiting for me, having already finished his warm up routine."
    "Even though he was running around and doing stretches up until now, his clothes still look to be in pristine condition."
    show k 1 t smile at fdis
    $ renpy.music.set_volume(0.5, 4.0, channel="music")
    play music2 "music/BGM/In That Mood.ogg" fadein 8.0
    "As he sees me coming over, he flashes a smile."
    k "\"How are you feeling right now? You seemed a little out of it earlier. Did Saya-san give you too much trouble?\""
    "Even though he was referring to us by our last names while other club members were around, now that we're out of earshot of other people, he's back to calling us by our first names."
    "Which is great, because I hate the excessive deference people treat me with just because I happen to be a bit older."
    "Age is just a number after all."
    mc 1 t smile "\"Sorry, I was still half asleep earlier today. Saya gave me one hell of a kick to the shin though so that's jolted me awake.\""
    show k 1 t calm at fdis
    "He seems almost... amused by hearing it."
    "He's been exposed to Saya for too long, he's not even batting an eye to random acts of violence."
    "This one has already been corrupted by us..."
    k "\"As long as you're not limping it should be fine. I'd be wary of angering her again though.\""
    mc 1 t sigh "\"I'll say. Feels like I've had a few years knocked off of my life expectancy.\""
    "Saya is one scary girl when she's angry."
    show k 2 t gentle at fdis
    "He laughs at my remark, his normally deep voice carrying softly through the air."
    "He's pretty subdued most of the time, but I guess there's a certain air of refinement to him."
    "Like... almost as if he wasn't just some average high school student."
    show k 1 t smile at fdis
    k "\"Well, since we'll be playing only one set, stamina won't be much of a problem. How about we go at each other guns blazing from the start?\""
    mc 1 t "\"Sounds good to me. How do we decide who gets the first serve? Should we just flip a coin?\""
    show k 1 t haughty at fdis
    k "\"If it's okay with you, I'd like for you to take the first serve. I know it's usually your preference and I'd like to give it a try.\""
    mc 1 t shock "\"Uhm... sure, I guess. I mean, if you're really okay with it.\""
    show k 2 t cocky at fdis
    k "\"I am. I think it'll be a great opportunity for me to try out a new strategy I've come up with.\""
    show k 1 t calm at fdis
    k "\"Now, if you don't mind, I'll stay with this side of the court. Shall we get started?\""
    "I nod, wishing him good luck and heading over to my side of the court."
    show k 1 t at fdis
    "What's up with him willingly giving me the first serve?"
    "He's totally underestimating me isn't he?"
    "I walk over to my starting position and one of the freshmen hands me a two balls."
    "I guess Saya's roped them into being our ball boys for this match, huh?"
    "I take a few deep breaths to steady myself. Once I walk onto the court, I shouldn't focus on anything but my opponent."
    "It doesn't matter if it's a tournament match or an exhibition match, it's all still tennis in the end."
    "And I refuse to give anything less than my all when it comes to tennis!"
    stop music2 fadeout 5.0
    play music3 "music/BGM/Straight.ogg" fadein 10.0
    show diagram
    show km1p1i1
    with dissolve
    play sound "music/tennishit.ogg"
    "I throw the ball into the air, moving my body as quickly as I can with a whip-like motion to hit the ball at the peak of the toss."
    show km1p1i2 with dissolve
    "It goes past the net and hits close to the line. A powerful flat serve that goes wide. The ball bounces quickly and swiftly, sliding past Kei-kun's reach."
    play sound "music/tennishit.ogg"
    show km1p1i3 with dissolve
    "Or at least it should have. With a swift motion, he dashes to the ball and returns it, though not perfectly."
    "The ball doesn't go very deep and doesn't have much power behind it. If it's like this, I can handle it easily."
    play sound "music/tennishit.ogg"
    show km1p1i4 with dissolve
    "I reach the ball and counter it, putting as much force as I possibly can without sending it flying out of the court."
    show km1p1i5 with dissolve
    "The ball goes to the opposite side of the court as Kei-kun is standing in right now, hitting the ground and bouncing away before he even starts running again."
    sa 1 t "\"15-0!\""
    show k 1 t calm at fdis
    hide km1p1i5
    hide km1p1i4
    hide km1p1i3
    hide km1p1i2
    hide km1p1i1
    with dissolve
    "Kei-kun looks down at the skid mark left on the floor by the ball, whistling in admiration."
    "Heh, seeing his surprise definitely makes me smile a little."
    "The freshmen all start talking loudly and excitedly after seeing the last rally."
    show k 1 t shock at fdis
    sa 1 t angry "\"{size=+4}Shut up!{/size}\"" with hpunch
    "Saya easily solves that {i}problem{/i} by using her usual sunny disposition."
    "The only problem is she almost gave me a heart attack!"
    "Looking over at Kei-kun, I notice him standing completely frozen, eyes wide as he stares at Saya."
    "She quickly notices his gaze and laughs nervously."
    show k 1 t sigh at fdis
    sa 1 t happy "\"Please continue!\""
    "Well at least she regains her composure quite fast."
    show k 1 t at fdis
    show km1p2i1 with dissolve
    "We both walk back to our positions, Kei-kun taking just a bit longer to compose himself again."
    "After knowing us for a full year, I'm surprised he's not used to Saya's personality yet."
    "I take a moment to bask in this atmosphere."
    "Even if I hesitated to be here right now, I have to admit that being on the court is the best feeling ever."
    play sound "music/tennishit.ogg"
    show km1p2i2 with dissolve
    "Once more, I shoot a flat shot aiming for the lines."
    play sound "music/tennishit.ogg"
    show km1p2i3
    show km1p2i4
    with dissolve
    "Kei-kun dashes to the ball and, although he reaches it, returns the ball into the net."
    sa 1 t "\"30-0!\""
    show k 1 t worried at fdis
    hide km1p2i4
    hide km1p2i3
    hide km1p2i2
    hide km1p2i1
    with dissolve
    "Kei-kun stares at me with a troubled look on his face. I guess he just isn't used to a truly fast serve."
    "There aren't many players with a lot of raw power around for him to practice against so it's no surprise he's still not used to playing against me."
    "Guess that's one benefit to me not playing against him often."
    show k 1 t at fdis
    "I repeat the same strategy once more."
    show km1p3i1 with dissolve
    play sound "music/tennishit.ogg"
    show km1p3i2 with dissolve
    "A flat ball with lots of power is what I excel at."
    play sound "music/tennishit.ogg"
    show km1p3i3 with dissolve
    "Although he gets to the ball with relative ease, he misjudges the timing."
    show km1p3i4 with dissolve
    "His return ends up going too long and flies out of the court by quite a bit."
    show k 1 t shock at fdis
    sa 1 t "\"Out. 40-0!\""
    hide km1p3i4
    hide km1p3i3
    hide km1p3i2
    hide km1p3i1
    with dissolve
    "I can't keep myself from grinning like an idiot."
    "I just might be a little bit of a sadist because crushing an opponent always feels so satisfying."
    "I never get sick of it."
    "Kei-kun probably thought he could come up with some strategy to break my serve and asked me to serve first so he could attack and mess with my head."
    "He probably thought that by breaking my serve, he'd also break my concentration."
    "Instead, it seems the spell has been turned against its user."
    stop music3 fadeout 3.0
    stop music fadeout 3.0
    $ renpy.music.set_volume(1.0, 0.0, channel="music")
    scene SCourt
    show k 1 t wince at fdis, five
    show sa 1 t at offscreenleft
    with fade
    sa 1 t "\"Game [povLastName]. Game count: 3-0! [povLastName] leads.\""
    play sound "music/crowdcheer.ogg"
    "The small crowd that's gathered around our court starts to cheer loudly once more."
    play sound "music/disappointment.ogg"
    "I just wish these guys would shut up. This is way too distracting."
    show k 1 t worried at fdis
    play music2 "music/BGM/The Chase.ogg" fadein 6.0
    "As for Kei-kun, he's seemed largely out of it since the end of the first game."
    "I guess the shock of seeing his strategy failing so catastrophically has broken his concentration."
    "He's completely abandoned his tactics and fine skills in favor of a brute force approach."
    "Tennis is a sport where your mind is just as important as your body."
    "If you start thinking too much about losing, your fear will cause your body to panic."
    "Your body won't move as it normally does and, without noticing, your play becomes affected."
    "Because of that, I managed to easily break through his serve game."
    "And that created a downwards spiral. The more he's dominated, the more he fears an eventual defeat, causing his play to worsen further and making him feel even more dominated."
    "It's a feedback loop that you can't escape from unless you notice that you're in it in the first place. And even then, it's no small feat."
    "Professional players struggle with this type of thing. For a high school student... this is a monumental beast all on its own."
    hide k 1 t worried with dissolve
    play sound "music/sit.ogg"
    "Huh... I'm usually all in favor of rest breaks, but..."
    "Right now, I wish we could play the whole match without stopping."
    "Not because I'd like to, but because I don't want Keisuke to have time to calm down."
    "It might be a shitty thing to say, but I hope he stays in this slump all the way to the end of the match."
    sa 1 t "\"Time!\""
    play sound "music/fabric.ogg"
    "Well, no point dwelling in it. I'll just get back to the court and try to get this match done as fast as I can."
    show k 1 t serious at five with dissolve
    show k 1 t serious at fdis, five
    "..."
    "Hah... this is exactly what I was hoping wouldn't happen."
    "His eyes seem much more focused right now."
    "I guess this small break gave him enough time to get himself back together."
    "I really can't afford to let my guard down."
    show diagram
    show km1p4i1
    with dissolve
    play sound "music/tennishit.ogg"
    show km1p4i2 with dissolve
    "Keisuke tosses the ball high into the air, making contact with it just as it begins to drop again."
    "There's no doubt about it that his serve has gone back to normal."
    "I guess there's no more weakness for me to exploit."
    "The good things in life are always short-lived after all."
    "The ball soars over the net, making contact with the ground deep onto the court."
    play sound "music/tennishit.ogg"
    show km1p4i3 with dissolve
    "I manage to reach the ball and send it back, but I lost my balance for a second and got a late start on my subsequent dash."
    play sound "music/tennishit.ogg"
    show km1p4i4 with dissolve
    "Just as I take a couple of steps towards the center of the court, Kei-kun immediately sends a powerful shot to the side I had been on."
    "Not having had enough time to regain my balance, attempting to change direction again makes me trip."
    "The ball slides through the floor, bouncing again on a sideways arch."
    play sound "music/tennishit.ogg"
    show km1p4i5 with dissolve
    "I somehow manage to reach his shot but, because it stays too close to the ground, I can't make a full swing and end up lacking power."
    "This is likely what he was going for."
    "It seems Kei-kun has decided to attack my counter, which is, admittedly, a rather annoying strategy."
    play sound "music/tennishit.ogg"
    show km1p4i6 with dissolve
    "Right after I return the ball to the other side of the court, he, again, shoots it to the other side of the court to make me run."
    "If this were a three or even a full-set match, I would be seriously worried about my stamina."
    play sound "music/tennishit.ogg"
    show km1p4i7 with dissolve
    "In a flash, Kei-kun has identified the shots I most struggle against and the ones I most want to hit."
    "By doing that, he is aggressively looking to keep his serve by chipping away at me until he can go for a winner."
    "This style of tennis that emphasizes a wide variation of shots and a delicate touch is his specialty. It's thanks to this that Kei-kun managed to overcome his average constitution, becoming a well-known player in our region."
    play sound "music/tennishit.ogg"
    show km1p4i8 with dissolve
    "Still, he has yet to make a breakthrough when it comes to the national competitions."
    "Since I can't fall into a comfortable pace, I end up not being able to hit the ball as I want to and, as such, can't put away a winner."
    show km1p4i9 with dissolve
    "I continue to struggle with the rally until Keisuke eventually runs me out of the point."
    show k 1 t haughty at fdis
    hide km1p4i9
    hide km1p4i8
    hide km1p4i7
    hide km1p4i6
    hide km1p4i5
    hide km1p4i4
    hide km1p4i3
    hide km1p4i2
    hide km1p4i1
    with dissolve
    "Keisuke continues to use this same strategy for the remainder of the game. I'm only able to score a single point before he wins."
    "We promptly start the fifth game."
    "This time, I have to try and hit my best possible serve to keep myself on the lead during my service game."
    show km1p5i1 with dissolve
    "While I fully expect myself to have the advantage on my serve, I still don't want to be caught up on a long rally against him."
    "I don't have that much stamina."
    play sound "music/tennishit.ogg"
    show km1p5i2
    show k 1 t serious
    with dissolve
    "I go for a strong, flat serve to the center of the court."
    "Although it's high risk, the ball makes it right on the edge of the court, painting the line."
    play sound "music/tennishit.ogg"
    show km1p5i3 with dissolve
    "Despite that, Kei-kun reaches it, returning a deep ball with tons of topspin."
    play sound "music/tennishit.ogg"
    show km1p5i4 with dissolve
    "Using the advantage given to me by my serve game, I quickly return a strong flat shot to the other side of the court."
    "The speed of the shot doesn't give him time to ready his next swing. If he doesn't have much time to prepare, he can't send a very precise shot."
    play sound "music/tennishit.ogg"
    show km1p5i5 with dissolve
    "He ends up lightly tapping it to my side of the court."
    play sound "music/tennishit.ogg"
    show km1p5i6 with dissolve
    play sound "music/tennishit.ogg"
    show km1p5i7 with dissolve
    "I rush over to it and strike with everything I have, putting away an easy winner."
    show k 1 t shock at fdis
    sa 1 t "\"15-0!\""
    show k 1 t hostile at fdis
    hide km1p5i7
    hide km1p5i6
    hide km1p5i5
    hide km1p5i4
    hide km1p5i3
    hide km1p5i2
    hide km1p5i1
    with dissolve
    "Kei-kun looks somewhat angry. I see him muttering something to himself before he gets back to position."
    "This is the main reason I avoided playing against him for so long."
    "Kei-kun falls in the category of \"tactical\" players. He is constantly running simulations and thinking up different strategies to deal with any problems he might face."
    "Ordinarily, when faced with a huge hurdle, a player like myself would attempt to find an answer through trial and error."
    "A player like Keisuke though is constantly analyzing the shifts in pattern. Because of that, he can shift into an answer almost instantly."
    "I'm forced to keep changing up shots far too often in an attempt to throw him off."
    "In the end, I'm not truly forcing my way through. I am just taking a detour that forces me to spend extra energy."
    "I just hate having to deal with any wall that my power can't break through."
    "Because I am forced to constantly think and look for alternatives, the strain of having to sustain such a degree of concentration while keeping up my usual high-pace game makes me get tired faster than usual."
    "Still, I can't just shoot blindly, otherwise he will eventually find a way to shut me out."
    show km1p6i1 with dissolve
    "I decide to change up my serves a little bit. By adding a few spin shots to my serves, which are usually all flat anyway, I can throw him off for a while."
    play sound "music/tennishit.ogg"
    show km1p6i2 with dissolve
    "I try putting as much power as I can into this spin serve, though the ball is significantly slower than before. Crap, I'm not too good at using spin."
    "Because of the way a player grips his racket and the hand he uses to hold it, the ball tends to naturally spin to one direction."
    "That's one of the reasons left-handed players are favored in the game, since there aren't many of them and players tend to have already ingrained their reactions to different shots. Any difference, no matter how small, can throw them off."
    "Most players capitalize on this natural spin, hitting spin shots that make the ball slide in that direction."
    "Since hitting a spin towards the opposite direction makes it so the ball doesn't slide so much to the side, it tends to not be as favored."
    "But because it isn't as favored, it becomes unexpected and I use this to catch Kei-kun by surprise."
    play sound "music/tennishit.ogg"
    show k 1 t serious at fdis
    show km1p6i3
    with dissolve
    "He reads my serve and rushes into a position to return, but because the ball doesn't escape as far to the side as he expects it, he ends up hitting the ball too close to the grip of the racket."
    play sound "music/tennishit.ogg"
    show km1p6i4 with dissolve
    "His return is shallow, leaving me an opportunity to attack."
    show k 1 t shock at fdis
    show km1p6i5
    with dissolve
    sa 1 t "\"30-0!\""
    show k 1 t angry at fdis
    hide km1p6i5
    hide km1p6i4
    hide km1p6i3
    hide km1p6i2
    hide km1p6i1
    with dissolve
    k "\"Tch...\""
    "Kei-kun looks just about ready to throw his racket on the floor. He's gripping it so tight that his hands are shaking."
    "I'm not exactly happy to see him like this, but I decide to bury those feelings for now."
    "He's my friend, but when we're on the court, I can't show sympathy."
    show k 1 t serious at fdis
    show km1p7i1
    with dissolve
    play sound "music/tennishit.ogg"
    show km1p7i2 with dissolve
    "This time I go with a wide slice."
    "Once again, since I'm serving the ball to a direction opposite of it's spin, instead of sliding away from the court, it angles itself back in."
    play sound "music/tennishit.ogg"
    show km1p7i3 with dissolve
    play sound "music/tennishit.ogg"
    show km1p7i4 with dissolve
    show km1p7i5 with dissolve
    "The awkward angle of the shot causes Kei-kun to hit another weak return, which I easily put away."
    sa 1 t "\"40-0!\""
    show k 1 t scorn at fdis
    hide km1p7i5
    hide km1p7i4
    hide km1p7i3
    hide km1p7i2
    hide km1p7i1
    with dissolve
    play music "music/crowd01.ogg" fadein 4.0
    "The freshmen all chat excitedly while they watch the match. There are so many voices at the same time that I can barely even make out what they're saying."
    "Well... not that I'm trying to anyway."
    "Kei-kun seems like he can't even notice them, not reacting at all to their voices."
    "That guy's concentration is on a whole other level... and that's already scary enough by itself."
    show km1p8i1 with dissolve
    play sound "music/tennishit.ogg"
    show km1p8i2 with dissolve
    "I ready myself for another serve. I take advantage of the indecision my past two serves created and hit a strong top spin shot wide."
    show k 1 t shock at fdis
    "Kei-kun is caught by surprise. Having tried to anticipate my serve, he ran towards the center but had to double back immediately."
    show km1p8i3 with dissolve
    "Because he can't reach the ball, I score a service ace to take the game."
    play sound "music/crowdcheer.ogg"
    "The freshmen erupt in cheers before being reprimanded by the other club members."
    sa 1 t "\"Game [povLastName]. Game count: 4-1! [povLastName] leads.\""
    show k 1 t scorn at fdis
    hide km1p8i3
    hide km1p8i2
    hide km1p8i1
    with dissolve
    play sound "music/sit.ogg"
    "We take another break."
    "I slide into my seat to rest for a bit, uncapping my bottle of water and taking a quick sip."
    show cg20 with Dissolve(1.0)
    "When I glance over at Kei-kun on the side... he has a really intense look on his face."
    "He might look like the meek, silent type, but he really gets fired up when it comes to tennis, huh?"
    "He mutters something to himself that I can't really make out, sweat rolling down his face and dripping from his matted fur."
    "He's wiping his face using the hem of his shirt."
    "... Why he isn't going for a towel inside his bag I really don't understand."
    "One thing I will say is that for someone who looks so lithe and somewhat fragile, Kei-kun is surprisingly well-built underneath his clothes."
    "You can quickly tell just how much effort he put into nurturing and caring for his body."
    "Even for someone who doesn't seem to naturally very athletic, he managed to build himself to a point where he doesn't have even a little bit excess muscle anywhere."
    "It's something to marvel at really. Even I probably am a little bit thicker on the muscle mass than I should be."
    hide cg20 with Dissolve(1.0)
    sa 1 t "\"Time!\""
    show k 1 t serious at fdis
    "We both get up from our chairs at the same time."
    "If I want to end this match as soon as possible then my goal should be to break his serve."
    "I've had enough time to get used to his tricky style."
    "Not only that, he feels like he's slipping. He's getting impatient and that shows."
    "I should use that to my advantage to break his serve."
    show km1p9i1 with dissolve
    play sound "music/tennishit.ogg"
    show km1p9i2 with dissolve
    "We both get to our positions. Kei-kun sends the ball high before striking it, hitting a strong flat serve to the center of the court."
    "I was already expecting him to do something like that. People tend to put too much force on the shot when they're angry whilst ignoring spin and placement."
    play sound "music/tennishit.ogg"
    show km1p9i3 with dissolve
    "Having gotten to the ball a lot earlier, I have ample time to prepare, hitting my strongest shot back at him."
    show km1p9i4 with dissolve
    "The ball hits the ground and bounces away from his reach, scoring me a return ace."
    show k 1 t angry at fdis
    "It seems that with each passing moment, Kei-kun becomes more and more agitated."
    "He should really try to calm down. Playing like this is only gonna drag him down further."
    sa 1 t "\"0-15!\""
    hide km1p9i4
    hide km1p9i3
    hide km1p9i2
    hide km1p9i1
    with dissolve
    "Well, it can't be helped. If he's not trying to help himself, there isn't anything I can do to help him."
    "And, to be honest, I feel that he'd fly off the rails if I did try."
    show km1p10i1 with dissolve
    "Kei-kun takes a while to get into position."
    "He starts tying his shoes repeatedly, probably trying to calm himself down."
    show k 1 t sigh at fdis
    $ renpy.pause (2.0)
    show k 1 t at fdis
    "..."
    "Well, he definitely looks to have calmed down a bit."
    play sound "music/tennishit.ogg"
    show km1p10i2 with dissolve
    "He serves the ball again, shooting a sliced serve towards the center."
    play sound "music/tennishit.ogg"
    show km1p10i3 with dissolve
    "If it weren't for the spin on the ball, that would practically be a body shot. As soon as the ball gets close, I sidestep it and hit an angled shot to the side of the court."
    "The ball practically paints the line, bouncing very high from all the top spin I put on it."
    "I really have to be more careful with my spin shots. They're barely going in right now. I might actually make a mistake if I keep going like this."
    play sound "music/tennishit.ogg"
    show km1p10i4 with dissolve
    "Kei-kun reaches it and effortlessly hits it back at me with another slice, going right at the center of the court."
    play sound "music/tennishit.ogg"
    show km1p10i5 with dissolve
    "I hit it back with as much power as I can whilst aiming crosscourt, but can't get good contact with the ball and it ends up hitting the upper part of the net."
    "We are both taken by surprise."
    show k 1 t shock at fdis
    show km1p10i6
    with dissolve
    "The ball topples down to Kei-kun's side of the court."
    "He dashes over to the net in an attempt to reach it, but ends up being too late."
    sa 1 t "\"0-30!\""
    hide km1p10i6
    hide km1p10i5
    hide km1p10i4
    hide km1p10i3
    hide km1p10i2
    hide km1p10i1
    with dissolve
    mc 1 u wince "\"Sorry about that. I didn't-\""
    "I apologize, as it's the proper thing to do."
    show k 1 t annoyed at fdis
    k "\"It's fine.\""
    "He nearly spits those words out. That's how angry he is right now."
    "I'm sure he doesn't blame me for it, but it's hard to keep your feelings in check when you're under pressure."
    show k 1 t at fdis
    show km1p11i1 with dissolve
    play sound "music/tennishit.ogg"
    show km1p11i2 with dissolve
    "Kei-kun serves a strong flat, this time aiming wide."
    play sound "music/tennishit.ogg"
    show km1p11i3 with dissolve
    "I dash towards the ball and hit it back, but since I can't get to a good position, the ball ends up being too weak."
    play sound "music/tennishit.ogg"
    show km1p11i4 with dissolve
    show km1p11i5 with dissolve
    "Kei-kun reaches it and puts it away in an instant."
    sa 1 t "\"15-30!\""
    show k 1 t smile at fdis
    hide km1p11i5
    hide km1p11i4
    hide km1p11i3
    hide km1p11i2
    hide km1p11i1
    with dissolve
    "My return was pretty terrible, so there wasn't anything I could do."
    "Keisuke might not look like it, but he's certainly a high level player."
    "If I give him any openings, he'll certainly go for them in an instant."
    show km1p12i1 with dissolve
    play sound "music/tennishit.ogg"
    show km1p12i2 with dissolve
    "Kei-kun serves once again. This time, I have a much easier time reaching it."
    play sound "music/tennishit.ogg"
    show km1p12i3 with dissolve
    "I return an angled shot that hits the ground before the service line and bounces away from the court. Kei-kun is caught by surprise and has to rush to the ball."
    play sound "music/tennishit.ogg"
    show km1p12i4 with dissolve
    "Right after striking, he runs up to the net, probably to try and restrict the angle of my return, but I'm one step ahead of him."
    play sound "music/tennishit.ogg"
    show km1p12i5 with dissolve
    "Right as he reaches the net, I lob the ball high over his head. He immediately starts running back and I don't doubt for a second that he will reach."
    play sound "music/tennishit.ogg"
    show km1p12i6 with dissolve
    "He manages to hit the ball at the last second, barely putting any power to it as the ball bounces a few centimeters away from the net."
    play sound "music/tennishit.ogg"
    show km1p12i7 with dissolve
    "I reach it before its first bounce and, right after it goes high again, I hit it with a drop shot."
    "Since I dropped the ball while being so close to the net, there is barely any power left in it."
    show km1p12i8 with dissolve
    "Kei-kun doesn't even make it to the service line before it double bounces."
    play sound "music/crowdcheer.ogg"
    "The first years erupt in cheers and I'm pretty sure some of the 2nd and 3rd years joined them in it."
    sa 1 t angry "\"I said shut up!\""
    "Well, she certainly has a way of handling the crowd..."
    "That way is fear."
    sa 1 t "\"15-40!\""
    show k 1 t nervous at fdis
    hide km1p12i8
    hide km1p12i7
    hide km1p12i6
    hide km1p12i5
    hide km1p12i4
    hide km1p12i3
    hide km1p12i2
    hide km1p12i1
    with dissolve
    "It seems that the pressure is starting to get to him. His face is a completely open book."
    "No matter how he looks at it, I've been dominating him on his service game and he can't do a thing about it."
    "Right now he would have to score twice in a row just to get us to deuce."
    "I definitely hold the advantage here."
    show km1p13i1 with dissolve
    play sound "music/tennishit.ogg"
    show km1p13i2 with dissolve
    "He serves the ball again, but just like his first serve of this game, he was so anxious to finish things fast that he got predictable."
    play sound "music/tennishit.ogg"
    show km1p13i3 with dissolve
    play sound "music/tennishit.ogg"
    show km1p13i4 with dissolve
    show k 1 t shock at fdis
    "I easily anticipate it and put the ball away with a return ace."
    sa 1 t "\"Game [povLastName]. Game count: 5-1! [povLastName] leads.\""
    show k 1 t sigh at fdis
    hide km1p13i4
    hide km1p13i3
    hide km1p13i2
    hide km1p13i1
    with dissolve
    "As if he had lost all the drive that fueled him so far, Keisuke's shoulders sags."
    "I don't blame him for being discouraged, but right now he looks as if he's already been defeated."
    "What happened to \"try your best until the end\"?"
    "What's the point of continuing to play when you've already given up?"
    "Ugh... I'm starting to get angry because of his attitude."
    "I'll just finish this soon so we can both stop this miserable match."
    scene SCourt
    show k 1 t wince at fdis, five
    show sa 1 t at offscreenleft
    with fade
    sa 1 t wry "\"Game, set and match won by [povLastName]. Count: 6-1!\""
    stop music2 fadeout 4.0
    show k 1 t sigh at offscreenleft with moveoledis
    hide k 1 t sigh
    "Saya has barely finished announcing the score and Keisuke has already walked out of the court, stuffing his racket back into his bag and slipping away with it."
    "Saya doesn't miss a beat, getting down from her seat and walking after him in a rush."
    "Tennis players really have glass hearts sometimes..."
    "A little crowd of freshmen gathers around me, showering me with praise and admiration."
    "... And using this as an opportunity to ask for tips."
    "I make no effort to listen, walking towards the locker room."
    "I just want to rest. I don't care."
    show s 1 v seductive at five with moveiridis
    show s 1 v seductive at fdis, five
    stop music2 fadeout 2.0
    $ renpy.music.set_volume(0.5, 0.0, channel="music3")
    play music "music/tennisambiance.ogg" fadein 4.0
    play music3 "music/BGM/On My Way.ogg" fadein 4.0
    "And right there, standing in front of the door, is Shoichi."
    s "\"Man, you're heartless. Don't you know how to go easy on people? It's good to do it every now and then.\""
    mc 1 t sigh "\"Suuure. Then I'd have him getting mad at me for underestimating him.\""
    "He shrugs."
    show s 1 v smile at fdis
    $ renpy.music.set_volume(1.0, 8.0, channel="music2")
    s "\"The cheering over here was so loud that we could hear it from our side of the building. Coach asked me to come over and see what the fuss was about.\""
    show s 1 v happy at fdis
    s "\"Although I ended up sticking around to watch you play, hehe.\""
    mc 1 t sigh "\"You sure are carefree with your duties, huh?\""
    show s 1 v smile at fdis
    s "\"I enjoy watching you play. Why are you so surprised?\""
    show s 1 v at fdis
    s "\"I have to ask, though. Why didn't you tell me you'd be playing against Urushihara?\""
    mc 1 t annoyed "\"Saya didn't tell me. She decided to keep it a secret until the last minute because I was, as she says it, \"a flight risk\".\""
    s "\"Sounds about right.\""
    mc 1 t annoyed "\"Hey!\""
    show s 1 v laugh at fdis
    s "\"Sorry, but I think she's right. I imagine you'd have gone home the first chance you got if you knew about this.\""
    show s 1 v smile at fdis
    s "\"After all, you've been talking about how annoying it is to play against Urushihara since you first watched him practice.\""
    mc 1 t avoid "\"That's... only partly true...\""
    show s 1 v seductive at fdis
    s "\"Oh, really? What part of what I said was wrong?\""
    mc 1 t sigh "\"... Shut up.\""
    show s 1 v happy at fdis
    s "\"Heh, as easy to rile up as usual.\""
    show s 1 v smile at fdis
    s "\"Oh, right, I nearly forgot. Here!\""
    "Shoichi hands me a can. I can see beads of condensation rolling down from it. It must be really cold."
    show s 1 v happy at fdis
    s "\"I picked up an energy drink for you, figured you'd want one after the match. I know orange is your favorite so I picked that one.\""
    play sound "music/opencan.ogg"
    mc 1 t happy "\"Oooh, thanks. You're a real life saver!\""
    "I immediately start drinking it down without a care in the world."
    "In just a few seconds, the entire can has already been emptied."
    show s 1 v shock at fdis
    s "\"Wow. Were you really that thirsty?\""
    mc 1 t sigh "\"You have no idea.\""
    show s 1 v happy at fdis
    "Without a warning, Shoichi puts a hand on my head and begins to casually pet me."
    "I don't even notice that's what he's doing until he's already started... at which point I'm so shocked by his complete lack of self consciousness about the whole thing."
    "If there's one thing that needs to be said about him it's that he's a very touchy-feely kind of guy."
    "Myself, Saya, his sister, and even Keisuke, on the rare occasion they're not going at each other's throats, have already been made victims to this."
    "It wouldn't be half bad if he kept these things to private places either, but somehow he always tries to pull them off in public."
    $ renpy.music.set_volume(0.5, 0.0, channel="sound")
    play sound "music/slap.ogg"
    "As soon as I snapped back to reality, I slap his hand away from my head... just as he had begun tugging on my ears."
    show s 1 v sigh at fdis
    s "\"Aww, no fun...\""
    "Jeez, you'd figure I killed his pet from the way he just reacted."
    "It's not even like I mind it in the first place. I just don't like when he pulls this sort of stunt in public."
    show s 1 v laugh at fdis
    s "\"Eh, well, what can you do.\""
    "... For some reason, he seems to find my rejection funny."
    mc 1 t avoidb "\"I don't like being messed with in public. You know that.\""
    s "\"Sorry sorry, I'll try to refrain from doing it again.\""
    "That's a lie..."
    show s 1 v smile at fdis
    s "\"By the way, what did you think of Urushihara? This was the first time you've played against him since the prefecturals tournament last year wasn't it?\""
    "I turn around to look for Kei-kun... but can't seem to find him."
    mc 1 t "\"I don't know... he's a good player, I'll give him that, but...\""
    mc 1 t wince "\"I don't think he's ready for a major competition just yet. He'd probably get destroyed by the higher ranking players.\""
    show s 1 v at fdis
    s "\"Didn't he lose on the first round at last year's national tournament?\""
    show s 1 v think at fdis
    mc 1 t sigh "\"Yeah. That's exactly what I mean by it.\""
    s "\"I suppose you're right. I kinda feel bad about him though.\""
    "What Shoichi is talking about is last year's All-Japan Junior tournament, the most important tournament in Japan for tennis players under the age of 18."
    "Keisuke managed to qualify for it last year. Unfortunately for him though, he got matched up against the #4 player on the first round and lost without taking a single set."
    "Competition for that event is brutal. I myself got all the way to the finals, but lost to Takagi Tanabe, the #1 player in the national rank."
    s "\"Urushihara sure got unlucky, huh?\""
    "I nod, pursing my lips."
    "This sort of thing happens every now and then. If you want to be safe and have an easier time on the first rounds, you need to be a seeded player."
    mc 1 t "\"Kei-kun is gonna have to try and get a seed ranking this year. That's pretty much the only thing he can do.\""
    show s 1 v at fdis
    s "\"What would he need to do to become seeded?\""
    mc 1 t sigh "\"Considering his current rank, he'd have to win at the Saitama Prefecture tournament and then place in the Top 4 for the Kanto tournament.\""
    show s 1 v smile at fdis
    s "\"And since we know for a fact he's not going to win the Prefectural, where should he finish on the regional to get a seed?\""
    mc 1 t sigh2 "\"Second place.\""
    "Shoichi whistles in admiration."
    s "\"Urushihara is pretty much screwed, huh? Just goes to show... being #2 in Saitama doesn't really mean much. The competition here is pretty light compared to other areas of the country.\""
    mc 1 t "\"Yeah, that's true. Right now, Tokyo and Hokkaido have the highest concentration of high-ranked players. Saitama is somewhere in the lower end of the rankings.\""
    show s 1 v think at fdis
    s "\"You're probably the only reason Saitama isn't dead last.\""
    mc 1 t "\"I wouldn't go that far... I honestly don't think the level of the players in our area has fallen. I think the competition has just improved a lot.\""
    show s 1 v at fdis
    s "\"What do you mean?\""
    mc 1 t think "\"I mean that the current generation is probably much stronger than the last ones.\""
    mc 1 t think "\"Back when I was still a freshman in high school, I'd routinely beat juniors and seniors.\""
    mc 1 t "\"It was against the other freshmen that I struggled.\""
    show s 1 v think at fdis
    s "\"Huh, I never really thought of it like that... Kinda sucks when you're trying to go pro and have a hard time standing out.\""
    show s 1 v smile at fdis
    s "\"Not that {i}you're{/i} having a problem like that, of course. You already stand out plenty.\""
    "Ah, yes... Shoichi is one of the few people I've told of my desire to go pro."
    "So far, I've only told my family, my coach and a few close friends."
    "Of course, most of the people involved in the tennis scene already {i}expect{/i} me to go pro, so it's not like there's much of a difference."
    "But even at the risk of sounding superstitious, I'm afraid that if I tell many people, I'll end up jinxing it."
    mc 1 t smile "\"What about you? Have you decided when you're going to go pro yet?\""
    show s 1 v sigh at fdis
    s "\"I already told you I'm not.\""
    mc 1 t annoyed "\"Have I ever mentioned that that's a stupid idea?\""
    s "\"Yes. Many times. Too many, in fact.\""
    "Ugh... he's too stubborn."
    "Shoichi is one of the best volleyball players in the country and yet he refuses to even consider the possibility of becoming a professional player."
    "It's just... so much wasted potential..."
    s "\"I can already tell what you're thinking so I'll just stop you right there. I'm not in the mood to have another discussion on me becoming a professional.\""
    mc 1 t sigh "\"Augh! Why not?\""
    show s 1 v at fdis
    s "\"Instead, I'd rather talk about something a little more important.\""
    mc 1 t curious "\"Oh? Like what?\""
    "He really knows how to rope me into changing the subject of conversation."
    "Use my curiosity against me."
    s "\"Your progress... or lack thereof. I honestly don't see much improvement at all from last year. What happened to you?\""
    mc 1 t sigh "\"... I was thinking the same thing.\""
    play sound "music/trash.ogg"
    "I throw the now empty can of sports drink into the nearby trash, where it falls inside with a satisfying clink."
    show s 1 v sigh at fdis
    s "\"I know I ask this a lot, but... are you okay? Are you sure you're not going through any trouble?\""
    mc 1 t sigh "\"I'm fine, big guy. I guess I'm just not putting in enough work, that's all.\""
    "I'm honestly not as convinced of the truth of my words as I might sound."
    "Just thinking about some of the guys I'll have to face again this year almost invokes a feeling of dread."
    show s 1 v smile at fdis
    s "\"Hopefully this year you'll be able to turn things around."
    show s 1 v laugh at fdis
    extend " Tanabe isn't invincible. I'm sure you can beat him if you try hard enough!\""
    "... I'm not so sure of that either."
    mc 1 t sigh "\"Yeah, I suppose... How about we cut this conversation here, though? I'd rather not think about all this stuff right now.\""
    show s 1 v smile at fdis
    s "\"Sure thing. In that case, how about you get into the locker room and at least towel yourself off."
    show s 1 v happy at fdis
    extend " No offense but you're smelling kinda ripe.\""
    play sound "music/stab.ogg"
    "He says that with the most innocent smile in the world... even though he was definitely taking a jab at me to tease me."
    mc 1 t sigh "\"Wow! Thanks for the delicacy on the matter.\""
    show s 1 v smile at fdis
    s "\"Alright. I'll rephrase that."
    show s 1 v happy at fdis
    extend " Dude, you fucking stink! Don't you ever fucking shower?\""
    mc 1 t sigh2 "\"...{w} Never mind.\""
    show s 1 v laugh at fdis
    "Shoichi stands there, grinning like an idiot, his tail wagging left and right."
    "I have to give him props for being able to be so cheery about everything."
    stop music3 fadeout 4.0
    scene SLockers
    show s 1 v smile at fdis, five
    with fade
    "Heading into the locker room, I notice that it's mostly empty save for two members of the volleyball club."
    "The only reason I can even tell who they are is because they have team shirts on them."
    show s 1 v at fdis
    s "\"Tomita, Ayano, the locker room isn't a break room. Stop slacking off and get back to practice.\""
    "The two look at Shoichi with a scared look before dashing away and back into the volleyball courts."
    mc 1 t sigh "\"... Aren't you slacking off too?\""
    show s 1 v laugh at fdis
    s "\"They don't need to know that!\""
    "... Demon."
    $ renpy.music.set_volume(1.0, 0.0, channel="music3")
    play sound "music/flick.ogg"
    "Shoichi flicks me in the forehead, sending a small jolt over my entire body."
    mc 1 t pout "\"What was that for\""
    show s 1 v seductive at fdis
    s "\"You think too loud. I can tell that you're thinking bad things of me just by the look on your face.\""
    mc 1 t "\"Am I really that transparent?\""
    show s 1 v happy at fdis
    s "\"To me you are.\""
    play sound "music/disappointment.ogg"
    "I don't think this is something to be happy about..."
    show s 1 v smile at fdis
    mc 1 t sigh2 "\"You don't have to wait around for me to leave.\""
    show s 1 v happy at fdis
    s "\"But it's more fun this way!\""
    "As always, I can't understand what goes on in his head..."
    mc 1 t sigh "\"You're just staying around because you want to get a private show, aren't you?\""
    show s 1 v laugh at fdis
    "Shoichi chuckles, leaning his back against a nearby locker."
    s "\"Pfft, I wish. But I know the mere thought of getting changed in a public locker already makes you squeamish.\""
    mc 1 t blush "\"W-what? No it doesn't. I do it all the time, you know!\""
    "... It does. It makes me so squeamish..."
    "But I'd die before admitting to that!"
    show s 1 v smile at fdis
    s "\"Jeez, you're sighing and pouting so much. Shouldn't you be happier that you just got a victory?\""
    mc 1 t sigh "\"You're making too much fuss out of something minor. It was just a practice match after all.\""
    show s 1 v seductive at fdis
    s "\"Oh, please. Both are just as important to you. You always say that, remember?\""
    mc 1 t sigh2 "\"... I guess.\""
    show s 1 v happy at fdis
    s "\"You're being too negative here. Look on the bright side. Now you know that you can easily beat Urushihara in an official match. Isn't it great?\""
    "... I wouldn't go that far."
    "I was lucky that I managed to do so well today. I wouldn't bet my chips on it happening again."
    "Kei-kun might not be as skilled, but his tricky style and strategies can corner you if you're not careful."
    stop music fadeout 4.0
    play sound "music/punchlocker.ogg"
    show s 1 v shock at fdis
    show k 1 t doom at offscreenleft
    "Suddenly, the sound of metal banging on metal echoes through the locker, catching us both by surprise."
    show s 1 v shock at fdis, seven
    show k 1 t doom at fdis, three
    with move
    "We both turn around to see Keisuke, staring at us with a face that spells out impending doom."
    "I don't think I've ever seen him this mad before."
    show s 1 v happy at fdis
    s "\"Oh, Urushihara, it's just you. I was afraid someone fell onto a locker or something. You can't do this you know, you've got to respect school property.\""
    "I'm asking myself the same question. When the hell did he get here?"
    "Did he pass by us while we were talking and we didn't notice?"
    "I know for a fact that he wasn't here when we walked into the room."
    "Although from the look on Shoichi's eyes, I can already guess that he knew Kei-kun was here and said those things on purpose."
    "In hindsight, I should have seen this one coming."
    "Shoichi isn't the type to make light of a person's skills so I should have imagined he was plotting something."
    show k 1 t scorn at fdis
    k "\"I'm sorry if I made such a poor opponent. I'll try to do better next time, your highness.\""
    s "\"Don't be silly. We both know such a thing would be impossible.\""
    "Oh boy, are these two going to go at it again?"
    "These two seem to look for every opportunity to take a jab at each other."
    "I don't know how these two manage to be friends when they behave so poorly around each other..."
    show k 1 t doom at fdis
    k "\"Oh, really? And what exactly do you mean by that?\""
    "... I feel like I shouldn't be so calm in a situation like this... but then again, I've already seen this happen so many times that I feel like I've become jaded."
    "I want to go home and be done with this."
    show s 1 v laugh at fdis
    s "\"I mean, come on. This is [povFirstName] we're talking about. You might be good, but you can't possibly think you could compare, right? Now that would just be crazy.\""
    "Why do I get the feeling that I've turned into a babysitter over the past year?"
    menu:
        "Maybe I should just cut them off now and avoid any escalation..."
        "Stop them.":
            play music2 "music/BGM/Mischief Maker.ogg" fadein 3.0
            $ discussion = "Neither"
            mc 1 t angry "{size=+6}\"Enough!!\"{/size}" with hpunch
            show k 1 t shock at fdis, shake1
            show s 1 v shock at fdis, shake1
            "My sudden shouting makes them both jump back in surprise, a look of complete shock on their faces."
            "... Wait, isn't this a little much? All I did was shout a little, what are you two looking so surprised for?"
            "No, don't let yourself calm down. Keep up the strict persona. They need to be taught a lesson!"
            mc 1 t angry "\"That is it, I have had it with the two of you.\""
            mc 1 t sigh "\"You guys have any idea how much of a nightmare it was during this entire break? Saya and I kept having to run around and keep you two from killing each other.\""
            mc 1 t angry "\"We didn't get to relax whatsoever for that whole time. That's it. I'm done. I'm not gonna deal with you two anymore.\""
            mc 1 t sigh2 "\"Either you two apologize to each other right now and stop behaving like little children or I'm done dealing with either of you!\""
            stop music fadeout 4.0
            "..."
            "....."
            play sound "music/disappointment.ogg"
            "Uhm... I know I was just shouting but someone please say something..."
            show s 1 v wry at fdis
            "Shoichi is the first to recompose himself. He clears his throat, looking at me with an apologetic expression."
            s "\"Sorry, [povFirstName]. I guess we crossed the line. I'm sorry we troubled you so much.\""
            show s 1 v avoid at fdis
            s "\"And... uhm..."
            show s 1 v avoidb at fdis
            extend "I'm sorry to you to, Urushihara. I shouldn't have provoked you like that. It was childish of me.\""
            show k 1 t serious at fdis
            "It seems that seeing Shoichi apologizing has somehow snapped Keisuke back to reality."
            "... But what's with that look on his face?"
            "Don't you use this as another chance to pick a fight or I swear I'm going to slap you!"
            show k 1 t angry at fdis
            k "\"..."
            show k 1 t avoid at fdis
            extend " I..."
            show k 1 t avoidb at fdis
            extend " I'm sorry, Urata. I let my emotions get the better of me. Please forgive me... erm... for all of the spring break. You too, [povFirstName]-san.\""
            "Waaah, this went beyond my wildest dreams. I never expected these two to apologize so sincerely to each other!"
            "... I mean... forgetting the fact that they're not even looking at each other in the eye."
            mc 1 t sigh2 "\"It's fine if you two avoid doing this kind of thing again. Honestly, what is it with you two anyway? Why do you keep pulling stuff like this?\""
            show s 1 v avoid at fdis
            s "\"Well... teasing Urushihara is kinda fun... {size=-2}though I guess I've been going a little overboard.{/size}\""
            show k 1 t sigh at fdis
            k "\"And I guess I have fun antagonizing Urata too... {size=-2}it's a bit refreshing when he acts that way.{/size}\""
            "... I can't tell if you two are supposed to be fighting or playing around anymore."
            "What are you two, nine?"
            mc 1 t sigh "\"Like I said, avoid pulling this kind of crap in the future and it'll be fine. You two are friends for God's sake, act like it.\""
            show s 1 v wince at fdis
            show k 1 t sigh at fdis
            s "\"Will do.\""
            k "\"Yeah. Got the message loud and clear.\""
            show k 1 t nervous at fdis
            k "\"Well... uhm... anyway... I have some things I need to do and I should really get to them, hahaha... haha... ha... Err... see you two later.\""
            show k 1 t nervous at offscreenleft with move
            hide k 1 t nervous
            show s 1 v sigh at fdis, five with move
            "Kei-kun finishes drops his towel on top of his bag and runs back to the courts in a hurry."
            s "\"Hah... poor bastard.\""
            mc 1 t curious "\"Huh? What?\""
            show s 1 v wry at fdis
            s "\"It's beyond me to be worrying about Urushihara, but... this is the first time you've ever yelled at him. You probably traumatized the poor guy.\""
            "Now he's a \"poor guy\"?"
            mc 1 t sigh "\"I was yelling at you too. How come he's the only one getting traumatized?\""
            show s 1 v think at fdis
            s "\"Oh, please. How long do you think I've known you for? I'm used to getting yelled at.\""
            "... That's not a good thing to get used to."
            show s 1 v wry at fdis
            s "\"Well, I should probably get back to my own practice, I guess. Sorry again for today. I'll see you later.\""
            mc 1 t smile "\"See ya.\""
            show s 1 v wry at offscreenright with move
            hide s 1 v wry
            "..."
            play sound "music/badjoke.ogg"
            "Haah, I think I was too hard on them..."
            "I tried to do something I'm not used to doing and I messed up..."
            "..."
            "I guess at least now I can have peace."
            "..."
            "I'm not really in a mood to continue practice today."
            "I think I'm just gonna tell Saya that I'm leaving early for the day."
            "I finish toweling myself off and head back to the courts."
        "Ignore them.":
            hide s 1 v laugh at fdis
            hide k 1 t doom at fdis
            play music2 "music/BGM/Punchline.ogg" fadein 5.0
            "Oh, well. It's not my problem anyway."
            "I don't care if they wind up killing each other."
            "Plus, it'd be less trouble for me down the line if they did anyway."
            "Yup, I'll just let them be."
            "Let's see... well, they're not looking my way anyway..."
            play sound "music/fabric.ogg"
            "I guess it's safe for me to strip down for a bit..."
            "Haah, it feels so good taking off those sweaty clothes!"
            "... Though I'll keep my underwear on, thank you very much."
            "Good thing I got an extra absorbent towel!"
            "... Still, these two are loud. Even though I'm trying to tune them out, I can't keep myself from hearing them arguing..."
            "Not that I can make any of what they're saying out though."
            "Let's see, where's my deodorant spray... ah, found it!"
            "Hehe, my trusty partner, I'll never leave the house without you~"
            "You're the only reason I can get by after practice without needing to shower at school after all."
            "Hmm... they don't seem to have noticed me yet..."
            play sound "music/disappointment.ogg"
            "These two really do shut themselves off from the rest of the world when they get going, don't they?"
            play sound "music/fabric.ogg"
            "There, all done and dressed back up!"
            "And they're none the wiser to it, just as it should be."
            "Hmm... I guess they wouldn't notice if I just left, would they?"
            "I planned on letting Saya know that I'd head home early, but... If I don't leave now, I'll lose my chance of slipping away before they notice me."
            "Saya-chan, I'm sorry. I promise to make it up to you later!"
            "I grab my bag and head towards the exit."
            "Just then, the sound of an even louder voice catches my attention."
            "It's Shoichi's voice."
            s 1 v scorn "\"Fine, let's ask him then!\""
            "Him? Please don't let \"him\" be me. Please don't let it be me..."
            show s 1 v scorn at fdis, seven
            show k 1 t hostile at fdis, three
            "Shoichi and Keisuke" "\"[povFirstName]!\" / \"[povFirstName]-san!\"" with hpunch
            "..."
            "....."
            "... Damn it..."
            mc 1 t sigh "\"What?\""
            "Shoichi and Keisuke" "\"{size=+4}Who's the best player?{/size}\""
            mc 1 t shock "\"Eh... what?! Err... P-Pix Santras?\""
            s "\"No! We're not talking about the best tennis player in history. We're talking about which of us is the best player!\""
            k "\"Please settle this argument!\""
            mc 1 t fsmile "\"W-what?\""
            "I... err... uhm... what?"
            mc 1 t sigh2 "\"You two are going to need to give me a little more context here. Who's the best player at... what, exactly?\""
            show k 1 t annoyed at fdis
            k "\"No. Which one of us is the better player in general? Am I a better tennis player than he is a volleyball player?\""
            mc 1 t fsmile "\"You do know that there's no easy way to compare, right? It's two completely different sports an-\""
            show s 1 v displeased at fdis
            s "\"Do your best!\""
            "Ehhh?! But I never even agreed to this in the first place!"
            mc 1 t fsmile "\"Aren't you guys being a little silly? What's the point of even-\""
            show k 1 t scorn at fdis
            show s 1 v frown at fdis
            "Waah, they look scary..."
            "Do I really want to say no to them when they're looking at me like that?"
            "I feel like a little puppy put face to face with two huge wild beasts..."
            "I sigh. I might as put some thought into this and come up with an actual answer."
            "Maybe if I sound like I'm not talking out of my ass, they'll accept the answer and they'll leave me alone."
            "I guess this is the best route I can go for right now."
            "... I probably should have stopped them when I had the chance, huh?"
            "But how am I even supposed to compare the two?"
            "They're both accomplished players in their own fields."
            "Keisuke plays tennis... his playstyle is that of a defensive baseliner."
            "He studies his opponents and comes up with strategies to attack their weaknesses."
            "He's also fairly skilled at a multitude of different shots and has lots of different attack patterns to confuse his opponents."
            "If I had to, I'd say that Keisuke is definitely a player I would keep my eye on in the future."
            "He's not fully developed yet, but he has tons of untapped potential."
            "Now Shoichi..."
            "Uhm... I don't know much about volleyball so I can't really say."
            "I don't understand volleyball strategy at all. Shoichi made me play with him ever since we were little but the only thing I know how to do is spike."
            "I don't understand things like rotations, substitutions or liberos and..."
            "Haah, just thinking about that complicated stuff already has my brain overheating..."
            "But I know for a fact that Shoichi is one of the best players in Japan."
            "Not only on his position, but he's overall considered one of the Top 10 in the country."
            "Shoichi plays as a setter... it wouldn't be an exaggeration to say that he's the team's control tower."
            "He's the one deciding which attacks to pull off at any given moment, not to mention who gets the ball, when and where."
            "He's the one always calling the shots..."
            "If I compare their individual achievements in their fields, Shoichi definitely comes out way ahead."
            "... But if I compare their skills based on my knowledge of their sports, I can't really give a fair evaluation. As far as I know, Keisuke is definitely high-level..."
            "Waah, I can't choose."
            play sound "music/disappointment.ogg"
            "And they're both staring at me with scary faces so I don't want to take much longer to come up with an answer!"
            "Well, if I think about it, Shoichi really should be the logical answer, but..."
            menu:
                "\"Tell the truth: Pick Shoichi.\"":
                    $ discussion = "Shoichi"
                    mc 1 t fsmile "\"I-I guess I'd have to go with... Shoichi."
                    show s 1 v shock at fdis
                    show k 1 t shock at fdis
                    "Just then, I see both of them going wide-eyed."
                    k "\"Huh?!\"" with hpunch
                    show s 1 v seductive at fdis
                    "Kei-kun looks completely taken aback by my answer."
                    "... I guess he really expected me to pick him?"
                    k "\"You're kidding, right?! [povFirstName]-san, you see me practice everyday. How can you say that this... this... brute is better than me?!\""
                    show s 1 v scorn at fdis
                    s "\"Brute? I might be strong, but I'll have you know that when I'm on the court, I rely on skill, not strength.\""
                    mc 1 t "\"It's true. Shoichi might not look it, but he's actually incredibly skilled. His tosses are so accurate, almost like he's threading a needle.\""
                    mc 1 t sigh "\"It feels a little unreal. It's not a matter of wondering where the ball will be. If he's the one handling it, the ball will always be at the perfect place for you to spike.\""
                    mc 1 t "\"I might not be a volleyball player, but over the years where he's made me practice with him, I've experienced it first hand. Shoichi's tosses really are god-like.\""
                    show s 1 v flattered at fdis
                    s "\"Aww, now you're just exaggerating.\""
                    "Why are you even blushing in the first place?"
                    show k 1 t uncomfortable at fdis
                    k "\"N-no way. [povFirstName]-san, are you sure you're not just being partial to him because he's your friend?\""
                    show s 1 v happy at fdis
                    s "\"It was your idea to involve him in the first place. Now suck it up!\""
                    "... You're having way too much fun with this."
                    k "\"But... but...\""
                    show s 1 v seductive at fdis
                    s "\"No buts. I win.\""
                    show k 1 t annoyed at fdis
                    "Keisuke sighs."
                    "Is it bad for me to say that seeing his brow twitching like that is a little amusing?"
                    k "\"Fine, you win this time."
                    show k 1 t doom at fdis
                    extend " I'll get you back for this later, Urata.\""
                    show k 1 t doom at offscreenleft with moveoledis
                    show s 1 v happy at fdis, five with move
                    "Kei-kun shoves the rest of his clothes back in his bag, picking it up and stomping out of the locker room."
                    show s 1 v smile at fdis
                    s "\"Sheesh, what's his problem?\""
                    mc 1 t sigh "\"You are! And could you stop starting fights with him. It's incredibly annoying having to deal with the messes you make.\""
                    show s 1 v think at fdis
                    s "\"{i}I{/i} make messes? Since when? As far as I know, Urushihara was also involved.\""
                    mc 1 t sigh2 "\"We both know you're the one provoking these fights in the first place. Please stop trying to act innocent.\""
                    show s 1 v sigh at fdis
                    s "\"Sheesh. What's gotten into {i}you{/i}? You're usually more fun than this.\""
                    mc 1 t sigh "\"Forgive me for not being enthusiastic after having to deal with my two nearly adult friends having a 5th grade argument.\""
                    show s 1 v laugh at fdis
                    s "\"Hey, hey, there's no reason to be acting so serious. Lighten up a bit!\""
                    "This guy... even when I'm lecturing him on something, he still cannot take me seriously."
                    "Sometimes I wish the serious, business-like Shoichi that always shows up when he's working would make an appearance during everyday activities too..."
                    show s 1 v happy at fdis
                    s "\"Welp, I guess I've pestered you enough for now. Time to head back to my practice.\""
                    mc 1 t sigh2 "\"You've \"pestered\" me enough for an entire week.\""
                    s "\"Aww, don't be like that! Well, anyway, talk to you later!\""
                    mc 1 t smile "\"See ya!\""
                    show s 1 v happy at offscreenright with moveoridis
                    "..."
                    play sound "music/disappointment.ogg"
                    "These two are a real handful... are they really high school students? Feels like I've been warped back to grade school..."
                    "Ah..."
                    "Wait, did Shoichi even get permission to bail out on practice for so long? He was already late to begin with..."
                    play sound "music/disappointment.ogg"
                    "I'd rather not think about it..."
                    "..."
                    "Well, what do {i}I{/i} do now?"
                    "It's true that I haven't done much today, at least when it comes to practice."
                    "But on the other hand, dealing with those two idiots has left me thoroughly exhausted..."
                    "I think I'll just call it a day and head home."
                    "Come to think of it, wasn't I going to do that even before they interrupted me?"
                    "Yeah, I guess I might as well stick with it."
                    "Better tell Saya before I leave though."
                "\"Lie: Pick Keisuke.\"":
                    $ discussion = "Keisuke"
                    "These two really try my patience sometimes..."
                    "But I guess this might be a good chance to teach Shoichi a lesson."
                    "He's the one who started this in the first place."
                    "In fact, he's {i}always{/i} the one starting things with Kei-kun."
                    mc 1 t think "\"Hmm... I think I'll go with...\""
                    mc 1 t happy "\"Keisuke!\""
                    show k 2 t gentle at fdis
                    show s 1 v shock at fdis
                    k "\"Yes!\""
                    "Waaah, I don't think I've ever seen Shoichi's eyes going so wide."
                    "Shit, I have to resist the urge to laugh!"
                    "This is your just desserts!"
                    "What are you even doing picking a fight with your junior in the first place? Idiiiot!"
                    show k 2 t cocky at fdis
                    k "\"See, Urata. I told you there was no way he'd pick you. I am the clearly superior choice after all!\""
                    "Kei-kun is hopping from one side to the other, gloating about it."
                    play sound "music/disappointment.ogg"
                    "Talk about childish."
                    k "\"I knew you'd make the blatantly correct choice, {i}Senpai{/i}. Of course It'd be me.\""
                    "\"clearly superior choice\", \"blatantly correct choice\". Did I give him a confidence boost or a vocabulary boost?"
                    "Also, \"Senpai\"? You've never called me that before. Are you trying to flatter me just because I picked you?"
                    "... Shit, but I do admit that I like being called that."
                    show k 1 t wry at fdis
                    k "\"Now if you'll both excuse me. I have other errands that I need to attend to.\""
                    show k 1 t wry at offscreenleft with moveoledis
                    show s 1 v blank at fdis, five with move
                    "Kei-kun grabs his bag and walks out of the room, all the while humming a little song."
                    "..."
                    "Waah, Shoichi is still giving me the stink eye..."
                    mc 1 t nervous "\"So... uhm...\""
                    s "\"Mind explaining to me what the hell just happened?\""
                    "I kinda want to flee from this situation..."
                    "No, you can't [povFirstName]. Stand your ground!"
                    mc 1 t sigh2 "\"Serves you right for going around and picking fights with your juniors.\""
                    mc 1 t sigh "\"It's also payback for getting me involved in this in the first place. If you don't like it then stop picking fights with Kei-kun.\""
                    show s 1 v avoid at fdis
                    s "\"Yeah, sure. I won't do it again. Does that make you happy, now?\""
                    mc 1 t smile "\"Very.\""
                    show s 1 v wince at fdis
                    s "\"Tch... I'm going back to practice. See you later.\""
                    show s 1 v smile at offscreenright with move
                    hide s 1 v smile
                    "Hmm... maybe I should have remained uninvolved..."
                    "Nah, he had it coming to him."
                    "What should I do now, anyway? I'm really tired after that match, even if it was just one-set."
                    "Hmm... guess I might head home now."
                    "Okay, it's settled. I need to go tell Saya."
    scene SCourt with fade
    $ renpy.music.set_volume(0.5, .0, channel="music")
    play music "music/tennisambiance.ogg"
    play music2 "music/BGM/Autumn Day.ogg" fadein 5.0
    "I'm starting to think I should have done a better job of wiping myself dry..."
    "Eh, not that it matters since I'll be heading home soon."
    "And I don't really smell bad. My deodorant was pretty strong so I doubt anyone could smell anything over it."
    "I'll just grin and bear this damp feeling."
    "Where's Saya though..."
    "Ah, there she is!"
    show sa 1 t considerate at fdis, three with dissolve
    show k 1 t worried at fdis, seven with dissolve
    "Ah, Kei-kun's there too."
    "He seems a bit... tense. What are they talking about?"
    if discussion == "Keisuke":
        show k 1 t smile at fdis
        "Kei-kun is the first to notice me approaching, smiling at me as I do."
        "Guess that whole thing in the locker room has left him in a good mood."
        show k 1 t calm at fdis
        show sa 1 t at fdis
        "He bows to Saya one last time and walks past me before leaving for the locker room."
        show k 2 t gentle at fdis
        $ renpy.pause (1.0)
        show k 1 t wry at offscreenright with moveoridis
        show sa 1 t at fdis, five with move
        mc 1 t think "\"Is he leaving early?\""
        "Saya nods."
        sa "\"Apparently his family asked him to run some errands so he had to leave early.\""
        mc 1 t think "\"Now that I think about it, this is kind of a regular occurrence with him, isn't it?\""
        show sa 1 t wry at fdis
        sa "\"Yeah. It must be hard...\""
        mc 1 t curious "\"What is?\""
        sa "\"Having a family like his. I don't know if I could handle it.\""
        "Huh? Is there something wrong with his family?"
        show sa 1 t think at fdis
        sa "\"Huh? What's with that clueless look you have on your face? Don't tell me you don't know what I'm talking about.\""
        mc 1 t "\"I don't know what you're talking about.\""
        play sound "music/disappointment.ogg"
        show sa 1 t sigh at fdis
        sa "\"Seriously? You really are beyond hopeless...\""
        mc 1 t annoyed "\"Well, I'm sorry if I don't know about everyone else's private lives. Maybe I should just ask him tomorrow.\""
        show sa 1 t talk at fdis
        sa "\"Yeah, you do that.\""
        mc 1 t "\"In the meantime, there's something else I wanted to talk to you about.\""
        show sa 1 t at fdis
        sa "\"Oh, sure. What is it?\""
        mc 1 t "\"I'm heading home.\""
        show sa 1 t happy at fdis
        sa "\"Oh, su-"
        show sa 1 t shock at fdis
        extend " Eh?\""
        "Saya completely freezes."
    else:
        show k 1 t shock at fdis
        "Kei-kun is the first to notice me approaching, his eyes widen when he sees me."
        show k 1 t avoid at fdis
        "Waah, he's totally avoiding looking at me."
        show k 1 t avoid at offscreenright with moveoridis
        show sa 1 t shock at fdis, five with move
        "He bows to Saya as if he were apologizing for... something and then promptly leaves."
        "Saya stares at his fleeing figure completely slack-jawed."
        sa "\"What was that about?!\""
        "Just then, she seems to finally take notice of me and her eyes light up."
        show sa 1 t smile at fdis
        sa "\"Ah, [povFirstName]-kun. That was a great match you two had, it really had my heart racing. I wish I could watch you play more often!\""
        mc 1 t "\"Why don't you start watching my tournament matches more often, then?\""
        show sa 1 t pout2 at fdis
        sa "\"Eh? I'd like to, but we always end up scheduled for matches at the same time.\""
        sa "\"And yours are always over before mine...\""
        show sa 1 t bored at fdis
        "Saya bites her lip, looking over at the door to the locker room again."
        sa "\"Say... do you know if anything's happened to Keisuke? He was looking a bit... uncomfortable.\""
        "Doesn't he always?"
        mc 1 t "\"Nothing much. I just defused another Kei/Shoichi situation.\""
        show sa 1 t sigh at fdis
        sa "\"Ah, another one? They're almost adults already, they really should behave more like it...\""
        play sound "music/disappointment.ogg"
        "Look who's talking..."
        mc 1 t "\"That's not what I came over to talk to you about though.\""
        show sa 1 t smile at fdis
        sa "\"Oh? What's up then?\""
        mc 1 t "\"I'm headed out for the day.\""
        show sa 1 t smile at fdis, jumping
        sa "\"Eh?\""
        "Just then, her smile freezes in place. Almost as if she were expecting me to add a \"just kidding!\" to the sentence."
    show sa 1 t shock at fdis
    sa "\"Ehhh?!\"" with hpunch
    "Could you please not react so dramatically to everyday news?"
    sa "\"You're kidding me, right? Can't you stick around for a bit longer? Practice is only gonna run for two more hours!\""
    mc 1 t sigh "\"Hey, I did my part. I played in that stupid match even though I didn't want to. You can't possibly need me for anything else.\""
    show sa 1 t avoidb at fdis
    "Saya looks up at me with pleading eyes."
    mc 1 t sigh2 "\"... There is something else you want isn't there?\""
    "So transparent..."
    sa "\"I was hoping you could stick around to instruct the new players.\""
    show sa 1 t complain at fdis
    sa "\"Pretty please? I haven't managed to do my own practice because I keep having to help the others...\""
    mc 1 t sigh "\"I don't want to be a poor sport but you knew this would happen when you took the position of captain. Come on, you know what our coach is like.\""
    show sa 1 t considerate at fdis
    sa "\"W-well, that's true. But I just thought, since you're the vice-captain and all...\""
    "So she wants to force me to do the work she initially agreed to do under the excuse that I'm the vice-captain... even though she's the one that forced me to take the position in the first place."
    mc 1 t annoyed "\"What's the one thing I made you promise when I accepted this position?\""
    "She continues to stare at me, but the smile on her face is disappearing ever so slowly."
    mc 1 t sigh "\"Wasn't it you who said all I had to do was make sure the other club members followed the rules and, other than that, I was free to do whatever I wanted?\""
    show sa 1 t pout2 at fdis
    sa "\"Yeah, but-\""
    mc 1 t sigh "\"Wasn't it also you who said that my own training would take precedence over whatever it was I had to do for the club?\""
    show sa 1 t complain at fdis
    sa "\"Sure, but I-\""
    mc 1 t sigh2 "\"Isn't resting after a particularly tough training session also a very important part of practice?\""
    show sa 1 t pout2 at fdis
    sa "\"Guh...\""
    "She's biting her lip in frustration."
    "I feel a bit bad for not letting her speak, but knowing her, she'd just use this as a chance to guilt-trip me into helping and I'm not dealing with that right now."
    show sa 1 t sigh at fdis
    "Saya-chan sighs, her whole body slumping forward as she pouts."
    sa "\"Fine, I understand. You can go.\""
    mc 1 t sigh "\"And you're not going to use this against me in the future?\""
    show sa 1 t pout2 at fdis
    "She looks away, biting her lips."
    "Aha, caught you."
    show sa 1 t considerate at fdis
    sa "\"N-no, I won't. I did promise to let you do as you please...\""
    "Victory."
    show sa 1 t bored at fdis
    sa "\"I guess I better get back to it then. I already see someone beckoning me over... see you tomorrow.\""
    mc 1 t "\"See ya.\""
    show sa 1 t at offscreenleft with move
    "..."
    "Knowing her, I better leave before she has a change of heart."
    stop music fadeout 4.0
    stop music2 fadeout 4.0
    scene SGateE with fade
    play music "music/birds.ogg" fadein 8.0
    play music2 "music/BGM/Dog Days.ogg" fadein 6.0
    "Once I step out of the training building, the warm, orange colored sun rays touch upon my skin."
    "Ah, it feels really good."
    "The orange tinted sky looks so gentle and mild."
    "Today really is a beautiful day..."
    jin "\"Ah, there you are!\""
    mc 1 t curious "\"Eh?\""
    "I hear a nearby voice and reflexively turn around."
    show gin at two
    show jin at six
    show ayako at ten
    with dissolve
    "Standing before me are three of my classmates."
    mc 1 t curious "\"Jin? Gin? Rep?\""
    "The fox smiles at me. Her smile is warm and kind, almost the same as this afternoon sun."
    "She makes me feel at ease."
    ay "\"What a coincidence, [povFirstName]-kun, I was just looking for you.\""
    mc 1 t curious "\"For me? What could you possibly need from me? Wait, it's not bad news, is it?\""
    "She softly giggles, crossing her arms."
    "That's right, her name is Ayako Kitsunegawa. She is our class president this year once again."
    "She's might seem like the calm and collected type, but she's very much a bona fide sadist."
    "But those personality quirks aside, she's usually a very caring and responsible person. Most of us have been in her care since our freshman year."
    "To be honest, there have been very few changes to our class since we joined this school."
    "Other than Shoichi being bumped up to the advanced class, that is."
    ay "\"I'm sure, but I just might be the bearer of bad news. I've been sent here on official business.\""
    mc 1 t sigh "\"I should have guessed. You never come to me when it's good news.\""
    ay "\"Well, now that's a bit unfair, isn't it?\""
    "Despite dreading whatever news she might be about to give, her laugh certainly makes me feel less anxious."
    "But..."
    mc 1 t sigh "\"Not to be a negative nancy, but if you're here on official business, then... what are these two doing here?\""
    jin "\"Wha- \"these two\"?! And after we went through all this trouble to track you down. We had club work to attend to too, you know?!\""
    "Haa, Jin sure is rowdy even this late in the afternoon."
    gin "\"Don't mind him, [povFirstName]-kun. We were actually heading home early when we bumped into Ayako-chan. She asked us to keep watch of the exit to the men's locker room while she went in through the other side.\""
    jin "\"Waah, Nii-san, don't blab on me to him! {size=-2}Also, since when do you call her \"-chan\"?{/size}\""
    "Ah, that makes sense. Since this used to be an all-boys academy up until a few years ago, not all the buildings have been retrofitted to accommodate female locker rooms."
    "Originally, the tennis/volleyball courts actually had the two lockers on separate ends of the building to separate the different clubs."
    "But now the guys and girls of both clubs share lockers instead, and doors were built into the locker rooms so they could access both courts."
    mc 1 t cocky "\"Ah, I see. So you were going to work as a glorified doorman while the Rep went in through the girls' locker room to look for me, huh?\""
    jin "\"Waah, n-no, it's not like that!\""
    "Well, doesn't he like to sound important..."
    "Class Rep giggles again, she hasn't said anything and just settled into watching these two bicker."
    play sound "music/disappointment.ogg"
    "Did she bring them along in the hopes that she'd get to see this very same situation unfold? Waah, she really is a sadist..."
    "By the way, these two guys in front of me might not look like it, but they're actually twin brothers."
    "The larger one, Ginichirou Nezumiro, is the eldest of the two. He's much more mellow and easy to deal with than his brother, but despite this all, he can be really intense when it comes to food."
    "The other, Jinichirou Nezumiro, is definitely one of the rowdiest people I've ever met. He's slow, dim and has a short fuse."
    "But despite these shortcomings, the two of them are genuinely nice people and I definitely enjoy spending time with them every now and then."
    mc 1 t curious "\"So, Class Rep, what exactly did you come here to tell me?\""
    ay "\"Ah, that's right. Sorry, I was having so much fun with this atmosphere that I forgot.\""
    "I'm sure you were purposefully staying out of it so you could watch them bicker for a while longer..."
    ay "\"To be honest, Katsuragi-sensei asked me to come fetch you. She didn't tell me exactly what's going on but it was something about today's morning assembly."
    "Ghk..."
    jin "\"Oh, yeah, that's right. You skipped today again. I imagine she was probably pissed.\""
    gin "\"I don't think she would have minded it so much if you actually bothered to show up to any of the meetings organized over the school year.\""
    mc 1 t avoid "\"W-Well, I can't help it. These are all so boring...\""
    ay "\"Ahaha, that definitely sounds like something you'd say. Well, you shouldn't worry so much, I've done my best to smooth things over with her so she's only a little annoyed now.\""
    mc 1 t shock "\"Wow, really? That's so nice of you, Class Rep!\""
    jin "\"H-hey, it really is. How come you never try to smooth things over for me when I'm the one getting in trouble?!\""
    ay "\"Once you become an important asset to this school's reputation like [povFirstName]-kun then I just might.\""
    jin "\"W-wah, don't say that, Ayako-chan!\""
    ay "\"It's not \"-chan\". Please refer to me as \"Kitsunegawa-san\" or \"Class Rep\".\""
    jin "\"You're kidding, I don't even get to call you by your first name?!\""
    "Even though her words might have sounded harsh, she had a wide grin on her face."
    "No doubt about it, she's only doing it to tease Jin."
    play sound "music/disappointment.ogg"
    "And he's so dumb that he's falling for it..."
    gin "\"Uhm... Jin, maybe we should head home already.\""
    jin "\"Tch, I guess so. I've got a mountain of homework to do too...\""
    ay "\"Oh my, a mountain? I don't remember being assigned any homework today.\""
    jin "\"W-well, that's-\""
    gin "\"That's because he slacked off last year and didn't actually finish all the credits he needed to pass, so he's having to deal with them now.\""
    ay "\"Oh my, I'm surprised the school even allowed him to do that.\""
    jin "\"Waaah, Nii-san, you didn't have to tell her that much!\""
    "Hehe, these two sure are full of energy every day."
    "I didn't even realize how much I missed their attitude during spring break."
    "How can I put it... seeing them like this is kinda... refreshing?"
    "I'm not all that surprised that he was given an extension though. Our school is pretty lax when it comes to people in the athlete programs."
    "We got tons of exposure from them after all. We have some of the best teams in the country in multiple sports."
    mc 1 t sigh2 "\"Well, this was a fun little chat but I guess I really should get going to the staff room. {size=-2}Sensei's mood is probably just gonna get worse if I make her wait.{/size}\""
    ay "\"Ah, that's probably a wise decision.\""
    jin "\"Yeah, dude. It was an honor meeting you.\""
    mc 1 t angry "\"Don't just write me off like that!\""
    gin "\"Hey, [povFirstName]-kun, how about we grab a bite to eat together again one of these days?\""
    mc 1 t smile "\"Ah, sure. Show me to another nice restaurant and I'll take you up on that offer.\""
    gin "\"Okay, it's a deal.\""
    jin "\"{size=-2}Nii-san, how come you're so buddy-buddy with [povFirstName]-san?{/size} {size=-4}I'm kinda jealous...{/size}\""
    "I'd rather avoid this unpleasant encouter, but..."
    "Given that Class Rep was the one tasked with giving me the message, I'm sure there's no way I could go home without her reporting the fact that she managed to pass it along."
    "In other words, I'm dead anyway. Might as well go peacefully."
    stop music fadeout 4.0
    scene SCorridorE with fade
    "I walk into the main building."
    "By the way, other than the multiple minor buildings for the different athletic departments, our school is divided into three main buildings."
    "There's the Main Building which, among others, houses the Staff Room and the club rooms for the most high-profile clubs or the ones with the most expensive equipment."
    "Then there's the Classroom Building. It's a much smaller building with only three floors, one for each of the grades."
    "Over here in our school, each grade is divided from \'A\' to \'E\', so we have fifteen classrooms in total, five for each floor."
    "The senior year is a little different in that the \'A\' class is specifically for advanced studies."
    "It's where they house the most promising students and pass them along classes designed to prepare for college entrance exams and college life in general."
    "Of course, joining 3-A isn't mandatory and there are always a few students that decline it."
    "Class Rep was also offered a spot with them but she refused."
    "Said something about wanting to see her duties as Class Representative to the end."
    "Oh, and the third building is the Club Building. It's where most of the other club rooms are located."
    "Our school is pretty well-known in the country and we have lots of people applying every year. Just getting in is quite difficult."
    "Well, it goes without saying that I had no issues with our entrance exam."
    "Some of the students in here might look like a bunch of good-for-nothings, but every needs to have some measure of intelligence to get in."
    "... Although I still have my doubts when it comes to Jin..."
    show kyoko at four
    show ryoji at seven
    with dissolve
    "Right ahead of me, walking over to the entrance, are two other classmates of mine."
    mc 1 t curious "\"Ah, Kyoko-san, Ryoji, what are you two doing here? And, wait, why are you two together?\""
    "The girl, Kyoko Nekonishi, fires a threatening glare at me. Despite her looks, she can be quite threatening when she wants to."
    "But of course, I'm close friends with Saya so something at this level couldn't even faze me."
    ky "\"Excuse me, could you please not assume something so ridiculous? We just happened to be leaving at the same time.\""
    "The other guy, Ryoji Kumagawa, doesn't even look like he's acknowledged us at all... even though he did stop walking when I called out to them."
    ry "\"{cps=1}...{/cps}\""
    mc 1 t fsmile "\"R... Ryoji?\""
    "Is he ignoring me?"
    "Ryoji furrows his brow, staring even more intently at the gaming console on his hands."
    "Ah, that's true, Ryoji is a videogame maniac so he always seems to have a console on his hands."
    play sound "music/disappointment.ogg"
    "I swear, sometimes I can look his way during class and he'll have his console hidden behind his textbook as if he really thought such a thing could fool anyone..."
    "But despite that, he still gets consistently high grades so the teachers never really complain about his attitude."
    ry "\"{cps=1}...{/cps} Heading home...\""
    "Ah, he spoke."
    "Is he just feeling a bit shy?"
    "It's true that he doesn't tend to participate in conversation unless it's about videogames..."
    mc 1 t curious "\"Were you two visiting your club rooms or something?\""
    "Kyoko nods, a haughty smile on her face."
    "She's always so prim and proper, but she tends to act all lady-like most of the time."
    "Well, despite her distant attitude, she's not a bad person at heart."
    ky "\"I've been made responsible for the Fashion club this year so I was just turning in all the required paperwork at the staff room.\""
    "Ryoji nods along too."
    ry "\"Dealing with paperwork... for the Game Dev club.\""
    mc 1 t curious "\"Wait, Game Dev club? {size=-2}We have one of those at school?{/size}"
    "Just as those words leave my mouth, Ryoji glares at me."
    "Unlike Kyoko, having a 6-foot tall brown bear glaring daggers at you is a really frightening thing and I can't help but feel a chill running down my spine."
    mc 1 t fsmile "\"S-sorry, sorry. I swear I wasn't making fun of it or anything. Hahaha...\""
    "That seems to appease him as his gaze softens up, looking back down at his game."
    "Jeez, it's really not safe to walk around staring at a piece of hardware all the time, you know?"
    ky "\"What about you, [povFirstName]-san? Do you also have paperwork to deal with? Oh, wait, that wouldn't be right. I thought Saya-chan was the one in charge of the Tennis club this year.\""
    mc 1 t smile "\"Yeah, Saya-chan's heading the tennis club. I've been made vice-captain but, really, I'm just along for the ride because she made me do it.\""
    ky "\"Fufu, that really does sound like Saya-chan.\""
    "Despite their completely opposite personalities, I've heard that Saya and Kyoko have become good friends since we met three years ago."
    "Although Kyoko still spends most of her time around Class Rep."
    "They've known each other since childhood after all."
    ky "\"Well, if it's not paperwork then what are you doing here? There are no club meetings for us regular folk right on the first day of class, and your club doesn't even have a room here in the first place.\""
    mc 1 t uncomfortable "\"Ah, well... Katsuragi-sensei sort of asked me to go meet her.\""
    "Kyoko's expression immediately goes dark."
    ky "\"Wow. What did you do to piss her off this time?\""
    mc 1 t flustered "\"Why do you just assume I did something wrong?!\""
    ky "\"This is you we're talking about. You just have that \"quality\" that pisses off most teachers.\""
    mc 1 t flustered "\"H-hey!\""
    ry "\"... I think so too.\""
    "Ryoji nods, his eyes still on his game console."
    mc 1 t annoyed "\"Don't just casually agree with her on that!\""
    "Kyoko laughs. Even when she's casually goofing around, her mannerisms are incredibly refined."
    "Well, she is the daughter of a pretty wealthy family. In fact, they actually own this school."
    ky "\"Well, make sure to tell me the story behind it later. I'd love to hear what kind of punishment the old hag has cooked up this time. See you tomorrow.\""
    show kyoko at offscreenleft with moveoledis
    show ryoji at five with move
    mc 1 t flustered "\"Don't say cruel things so casua- Oh, she's gone.\""
    "She really is good at slipping away unnoticed... is it a cat thing?"
    "Ah, Ryoji is still here though."
    mc 1 t curious "\"Hey, Ryoji, what game are you playing right now?\""
    ry "\"... Moon Fighter Rangers.\""
    mc 1 t curious "\"Ah, that one game based on that children's anime? How many seasons does that thing even have? I think I remember it airing when I was eight.\""
    "Ryoji nods casually, not bothering to confirm or deny what I just said."
    "As always, making conversation with him can be hard."
    mc 1 t laugh "\"Is the game fun?\""
    "He looks up at me with a conflicted expression."
    "H-hey, what's with that look?"
    ry "\"... Shouldn't you... be heading to see the teacher?\""
    "Guh, he caught on to the fact that I was trying to stall."
    mc 1 t sigh2 "\"Yeah, yeah. {size=-2}You can be surprisingly perceptive at times, Ryoji... unnecessarily so.{/size}\""
    "Ryoji nods, pulling a piece of toast from his bag and munching on it."
    "... Wait, a piece of toast from... his bag?"
    "The hygiene implications of what I've just witnessed scare me a bit..."
    ry "\"See you tomorrow.\""
    mc 1 t fsmile "\"Y-yeah, see ya.\""
    show ryoji at offscreenleft with moveoledis
    "Haah, off he goes."
    "... I'm jealous. I wish I could just walk away like that..."
    stop music2 fadeout 4.0
    scene SCorridorE with fade
    play music "music/tickingclock.ogg"
    "..."
    "I've walked all the way to the third floor where the Staff room is located."
    "..."
    "I don't want to go in!" with hpunch
    "But I know that if I don't show up soon, she'll only get angrier."
    "Better to get this over with. Kinda like ripping of a band-aid!"
    play sound "music/disappointment.ogg"
    "... Even though ripping off band-aids is incredibly painful for me because they always wind up ripping a ton of fur off too..."
    "Alright, I won't get anything done if I just stand around. Take a deep breath and..."
    play sound "music/knock.ogg"
    "The sound of my knock echoes through the empty hallway."
    "Waah, my heart is beating really fast right now."
    "Even though I've been skipping these things since my first day of class, this is the first time I've been called in because of it."
    "I kinda just assumed I'd keep getting special treatment because of my status as a tennis player..."
    kat "\"Come in.\""
    scene StaffRoomE with fade
    play sound "music/slidingdoor.ogg"
    mc 1 t nervous "\"Pardon the intrusion.\""
    show kat 1 u smile at five with dissolve
    "It doesn't take much looking around to find Katsuragi-sensei."
    "She is sitting on her chair, legs crossed and turned all the way to look at the door."
    "She has her head leaning against her closed fist... and she looks incredibly intimidating for a regular old woman!"
    kat "\"[povLastName], I was wondering how long it would take you to show up.\""
    "... Just from her tone of voice, I can already tell that the situation is mostly hopeless..."
    "No, I'll still try to act dumb. Maybe that'll save me!"
    "... I wish."
    kat "\"[povLastName]-kun, you must know why it is that I've called you over, right?\""
    mc 1 t avoid "\"W-well... to be perfectly honest it's not as if I don't particularly know what kind of reason would lead you to decide against not calling me h-\""
    kat "\"You're talking in circles to try and confuse me now? That's cute but it certainly isn't going to work. Sit.\""
    mc 1 t frightened "\"Y-yes, ma'am!\""
    play sound "music/disappointment.ogg"
    "... Thoroughly defeated."
    kat "\"We certainly appreciate the amount of exposure your name gives this school. And it's not as if you're doing badly with your studies either given that you're always placing quite high in the school ranks-\""
    mc 1 t nervous "\"Y-yes, see, I'm doing pretty well, so-\""
    play sound "music/stab.ogg"
    kat "\"Let me finish!\"" with hpunch
    mc 1 t frightened "\"Y-yes, ma'am!\""
    "Katsuragi-sensei sighs, picking up a folder that was on top of her desk and opening it up."
    "Is that... a file on me?"
    kat "\"I can see here that your academic records continue to worsen with each passing year. All of your teachers keep mentioning a continuing lack of interest on your part.\""
    kat "\"Not only that, if I pull up your records from grade school and junior high, the drop is almost immediately apparent.\""
    mc 1 t avoid "\"W-well, one can't live solely on past accomplishments, right?\""
    kat "\"If that was the only reason for this drop then I'd certainly let you off the hook, but we both know that that's not the real reason so may we just cut to the chase?\""
    "S-scary... she's really scary."
    "Katsuragi-sensei used to be our homeroom teacher up until last year but she recently got a promotion and became the head teacher and coordinator for the school."
    "So she doesn't have any classes to deal with this year, and instead oversees the progress for all the classes in school."
    "It's an unenviable position... just thinking of the amount of work she must have already gives me a headache."
    kat "\"If only you were trying hard then I could forgive you for this. It's not as if a person can continue to excel for their entire life, drops in productivity are to be expected.\""
    kat "\"But you've completely stopped trying, haven't you? I've also spoken to your coach and he's told me that you've completely stagnated when it comes to tennis as well.\""
    mc 1 t annoyed "\"W-what would he know about it? It's not like he even bothers coming to pra-\""
    play sound "music/stab.ogg"
    kat "\"I wasn't done talking!\""
    mc 1 t frightened "\"Y-yes, ma'am!\"" with hpunch
    kat "\"Coach Mikado theorized that you've been going through a rough period caused by extreme stress due to all the expectations placed on you for the past six years.\""
    kat "\"If that is the case, I'd very much like for you to see our school's psychiatrist and-\""
    mc 1 t annoyed "\"With all due respect, but would that be obligatory?\""
    kat "\"Well, no. We cannot force a student to see a psychiatrist unless he's deemed to be in direct need of psychological assistance.\""
    mc 1 t annoyed "\"Then I'll pass. I'm fine on my own, thank you very much. I don't have any complicated problems like that. I'm just not interested in paying attention to class, that's all.\""
    "She sighs again, rubbing the bridge of her nose with a furrowed brow."
    kat "\"So you'll prefer taking full responsibility for your failures over letting someone help you deal with your situation? Given your talents, I imagined you would want to become a professional.\""
    mc 1 t angry "\"That's...\""
    "Hah..."
    "I can't bring myself to confidently say that that's my plan."
    kat "\"... I'll let you off the hook this time.\""
    mc 1 t shock "\"Huh? Why? I did just say that I've been doing all this on purpose, haven't I?\""
    kat "\"Call it intuition if you will, but I don't believe punishing you for your lack of motivation will somehow help you to become more motivated.\""
    "I stand up from my chair with a half-jump, suppressing the urge to grab her in a tight hug."
    mc 1 t happy "\"T-thank you, Katsuragi-sensei, you really are much nicer than I gave you credit fo-\""
    kat "\"Of course, we have yet to discuss your punishment for skipping on this morning's assembly.\""
    play sound "music/stab.ogg"
    mc 1 t shock "\"Geeh.\""
    "The old fox smiles, looking up at me with a devious look."
    kat "\"What, you didn't really think that I'd also give you a pass for willingly, and with full knowledge of your actions, skipping the assembly to welcome our newest students for the third time in a row, did you?\""
    mc 1 t nervous "\"O-o-o-of course not. The thought never even crossed my mind! Aha... ahahaha...\""
    "I'm doomed..."
    stop music
    scene SCorridorE with fade
    "I end up being forced to be on cleaning duty for the next week as punishment for my actions."
    "Considering everything I've done, I suppose I had it coming, but..."
    "I really wish I had managed to go home free!"
    play music2 "music/BGM/Classical/Presto Agitato.ogg" fadein 30
    "..."
    "Huh?"
    "What's this? Now that I think about it, I think I can hear... something?"
    "It sounds like music... come to think of it, there's a music room nearby, isn't there?"
    "But I thought the only music club still operating in our school was the Light Music club. This sounds more like classical piano."
    "... Not that I know anything about music in the first place. It's just a feeling that I have."
    "Is someone using it at this hour? It's almost 6PM."
    "I guess I'm a little curious about it."
    "Whoever it is, this person plays really well."
    "Maybe this is a recording? No, but it's not coming from any of the school's speakers."
    "And the audio quality is too high. It really sounds like the real deal."
    "Maybe I could go take a look?"
    "It certainly wouldn't hurt to take a peek..."
    menu:
        "Go look.":
            $ jun_met = True
            "Before I can even consciously make a choice, I feel as if my legs are working on their own, dragging me towards the origin of this music."
            "It's as if the piano is calling out to me."
            "I want to listen from up close... no, I {i}need{/i} to listen from up close!"
            "But who could be playing this? The Classical Music club has been disbanded a few years ago. All that's left is an old room with some dusty instruments."
            "Maybe it's a teacher? Or a freshman?"
            "No, wait, club activities haven't started yet so there's no way they'd allow a freshman to be using the club room already."
            "Before I notice it, I'm already at the door."
            "T-that was really close. I nearly walked in without thinking."
            "How would that person even react to it? What would I even say?"
            "\"Sorry I barged into the room but could you keep playing the piano for me?\""
            "... But then again, this does sound really good."
            "Crap, I'm just going around in circles with this logic!"
            "Screw it, I'll just sneak in. The piano is so loud they might not even notice in the first place."
            play sound "music/slidingdoor.ogg"
            scene MusicRoomE with fade
            "I slide the door open as gently as I can."
            "I peek curiously into the room, looking around for the source of the music."
            "And that's when I see him."
            show cg2 with dissolve
            "A boy is sitting in front of the piano, his figure is bathed by the orange rays of the sun that are coming in from the nearby window."
            "He rocks his body back and fourth to the sound of the music, looking incredibly happy at the same time."
            "The tiger rocks his body back and forth in time with the music."
            "Wait, are his eyes closed? I thought that sort of thing only happened in movies!"
            "Droplets of sweat are dripping down from his face, but his expression doesn't falter for even a second."
            "Damn, this guy is intense."
            "The color of his fur is an intense orange, one that becomes almost blinding when touched by the sun's gentle rays."
            "I can feel the music slowly enveloping me, almost as if it really were calling me."
            "It's telling me to come closer."
            "I can't take my eyes off of his performance."
            "I can feel his music echoing deep inside of me."
            "I don't even know what I'm doing, but I know I want to feel more of it."
            "I feel a tightness in my chest, as if I might suffocate, and yet, it's not unpleasant at all."
            "It's like countless waves are crashing against my body."
            "Everything else is blurry, muddled."
            "The boy and his piano are the only thing in focus. They're the only thing that feels {i}real{/i} right now."
            "The closer I get, the harder it is to keep my thoughts in order."
            "I can't even notice whether my legs are moving or not but it's still a fact that I'm approaching him."
            "Nothing else feels important right now so I ignore everything else and just focus on his piano."
            "The piano..."
            play sound "music/tableknock.ogg"
            stop music2
            hide cg2
            with dissolve
            $renpy.pause (0.3)
            play sound "music/ChairScoot.ogg"
            "Then, as if the spell was broken, I'm jolted back to reality by the pain shooting up my leg."
            "It seems that, in my daze, I kneed one of the tables by accident."
            "It freaking hurts!"
            mc 1 t angry "\"Son of a-\""
            "Ah, wait. The piano... stopped?"
            "I look back to the piano and-"
            show j 1 u cshock at fdis, five with dissolve
            "The tiger is holding onto the piano, trying to... keep himself from falling from his chair?"
            "..."
            play sound "music/fall.ogg"
            show j 1 u cshock at fdis, fall
            "Wait, he fell backwards from his chair?!" with hpunch
            show cg18 with Dissolve(1.0)
            mc 1 t shock "\"W-woah!\""
            "He gets back up on his knees, bringing a hand to his head and rubbing it painfully."
            hide j 1 u cshock
            show j 1 u wince at fdis, offscreenleft
            jw "\"Ow...\""
            "Oh God, I really hope he didn't hit his head."
            play music2 "music/BGM/Little by Little I Walk.ogg"
            mc 1 t worried "\"Are you alright?!\""
            jw "\"Y-yeah, I'm f-fine.\""
            show j 1 u wince at fdis, five
            hide cg18
            with Dissolve(1.0)
            "Before I can run over to him, the boy manages to get himself back on the chair, proceeding to get up and turn to me."
            show j 1 u blush at fdis
            "The boy looks away from me, his whole face turning red."
            "His tail lashes nervously behind him, like a cornered, frightened cat."
            "God, I really did a number on him, huh?"
            mc 1 t nervous "\"S-sorry about that. I didn't mean to scare you.\""
            mc 1 t fsmile "\"I just... uhm...\""
            show j 1 u watch at fdis
            "The boy relaxes, if only slightly. He crosses his arm and sits upright on the chair."
            jw "\"Sorry. I didn't know there were still other students around.\""
            mc 1 t curious "\"Hmm...\""
            show j 1 u shockb at fdis
            jw "\"U-uhm... c-can I help you with something?\""
            mc 1 t shock "\"O-oh, no no. Sorry for staring.\""
            "I don't think I've ever seen him before."
            "And I know for a fact that most freshmen wouldn't be in this building today unless they had some business in the Staff room."
            "Did he just wander in here and got into this club room?"
            "No, but it would be kept locked in the first place. There's no way he'd have been able to get in."
            "He also doesn't really strike me as a freshman... he doesn't have that innocent, hopeful spark that you see in the eyes of most freshmen."
            mc 1 t curious "\"Hmm, I'm sorry to ask so suddenly but... are you a freshman here?\""
            "Because you certainly don't look like it."
            show j 1 u think at fdis
            "The boy blinks a few times, cocking his head to the side."
            "Then, as he looks down at his own uniform, he seems to understand my question."
            show j 1 u shock at fdis
            jw "\"Ah, n-no! I-I mean, I'm new here but..."
            show j 1 u wince at fdis
            extend " I just transfered to this school today. I'm actually a senior.\""
            show j 1 u blush at fdis
            jw "\"I had a few problems at home this morning and ended up not being able to show up for the welcoming assembly this morning.{nw}\""
            jw "\"{cps=60}And because I got here too late, classes had already started and the gates were closed, so I was locked outside.{/cps}{nw}\""
            show j 1 u cshock at fdis
            jw "\"{cps=80}I had to stick around until they were open again this afternoon so I could get inside and talk to a teacher.{/cps}{nw}\""
            show j 1 u cshockb at fdis
            jw "\"{cps=90}But she refused to show me around school. I ended up trying to find my class on my own and got lost. And then-{/cps}{nw}\""
            mc 1 t wince "\"Ah, I get it I get it, slow down!\""
            show j 1 u shockb at fdis
            jw "\"Ah, I'm sorry. W-was I talking too fast again?\""
            "Again? Is this a common occurrence for him?"
            "Still, he talks so fast that I can't even keep up with what he's saying."
            "Ah... he's kinda giving me a headache."
            "He definitely looks like the high energy type..."
            "No, that's not even the weirdest thing. How can you say so much about yourself to someone you've only just met?"
            "Wait, is he still talking? Crap, I've been so caught up in my own thoughts that I wasn't paying attention."
            show j 1 u avoid at fdis
            jw "\"...not really good with crowds, and this school has so many students.{nw}\""
            show j 1 u smile at fdis
            jw "\"I got into this room to avoid the giant crowd swarming the Staff room. That's when I noticed the piano.{nw}\""
            show j 1 u happy at fdis
            jw "\"It was really out-of-tune though, so it took me quite some time to get it up and running again.\""
            "The boy strokes the keys of the piano, smiling gently at them."
            "The piano seems to calm him down a bit... and I have to admit, he has a beautiful smile when he lets his guard down..."
            "... Wait... isn't he relaxing a bit too much?! He completely forgot that I'm here, he's just fawning over the piano right now!"
            show j 1 u cshock at fdis, shake1
            mc 1 t fsmile "\"Ahem!\""
            jw "\"Awawawa!\""
            "He certainly is energetic, I'll give him that..."
            mc 1 t "\"Did you say you got here just after today's classes ended?\""
            show j 1 u watch at fdis
            jw "\"Yeah, I did. Why?\""
            stop music2 fadeout 5.0
            play music "music/tickingclock.ogg" fadein 4.0
            mc 1 t "\"Well, it's just...\""
            "I point towards the clock right above the whiteboard."
            mc 1 t fsmile "\"It's already fifteen past six...\""
            jw "\"Eh?\""
            "He looks towards the direction I am pointing, slowly, almost like clockwork."
            "I swear I can almost hear the clicking sounds as his head turns."
            "Once he sees the clock, he freezes."
            show j 1 u cshock at fdis
            stop music fadeout 4.0
            play music2 "music/BGM/Mischief Maker.ogg"
            jw "\"EEEEEHHH?!\"" with hpunch
            "Ah, this guy's too much. How did he not notice time passing?"
            "The sky is completely orange for God's sake."
            show j 1 u cshock at shake
            jw "\"No way! I didn't even get to find my classroom yet. What am I going to do?\""
            "At this point, it's clear as day that he's panicking."
            "And I am probably a horrible person because watching him acting this way is incredibly funny."
            "Hmm... maybe I could do something nice for him and show him around?"
            "It's not like he's a bad guy, just a little rough around the edges."
            "... But then again, I'm not exactly fond of the idea of hanging out someone I don't know..."
            stop music fadeout 4.0
            menu:
                "Show him around.":
                    $ tour_jun = True
                    play music2 "music/BGM/Windswept.ogg" fadein 6.0
                    mc 1 t gentle "\"Well, I suppose I'm free right now. I can show you around some of the more important areas of school if you'd like.\""
                    "I do feel bad for scaring him like that when I came in..."
                    "Poor guy almost had a heart attack."
                    "I remember Shoichi telling me a while ago that I'm always too unfriendly to new people, so I try my best to sound warm and kind."
                    "Ah... it feels refreshing somehow."
                    "It's been a while since I've legitimately tried to be friendly to someone new."
                    show j 1 u shockb at fdis
                    jw "\"Really? {size=+4}Really?!{/size}\""
                    "His eyes go so wide that I can barely even make out the color of his iris now."
                    "This guy has such drastic shifts in emotion that it's starting to give me whiplash."
                    mc 1 t smile "\"Sure. We'd have to be quick though. They'll close things up in about an hour.\""
                    mc 1 t curious "\"Could you just tell me what classroom you were assigned to?\""
                    show j 1 u think at fdis
                    jw "\"Uhm... It was classroom 3-B.\""
                    "3-B? Then that means..."
                    mc 1 t smile "\"Oh, it's the same as me.\""
                    show j 1 u shock at fdis
                    $ renpy.pause (1.0)
                    show j 1 u gentle at fdis
                    "He smiles from ear to ear, his eyes nearly twinkling with excitement."
                    jw "\"Really? That makes everything a lot easier.\""
                    show j 1 u think at fdis
                    jw "\"Oh, by the way, my dad told me something about this school having \"special classes\" for seniors. Can you tell me what that is about?\""
                    mc 1 t think "\"Special classes? You mean college prep? If so, then it's just a specific class where they give students some extra classes to prepare them for entrance exams.\""
                    jw "\"So the best students get special treatment? Isn't that kind of unfair?\""
                    mc 1 t "\"Not really. You're allowed to move up to that class up until the last month of class so, really, anyone can join it as long as they work hard enough.\""
                    show j 1 u bored at fdis
                    jw "\"That's not true. I mean, even if I studied twenty five hours a day, I'd still never place in the top fifty.\""
                    mc 1 t shock "\"Wha-? How much do you usually score in your tests?\""
                    show j 1 u watch at fdis
                    jw "\"I've never had more than fifty in any test I've ever taken.\""
                    "What?! Is this for real?"
                    mc 1 t sigh "\"{size=-6}...you need an 80 point average to graduate, you know...{/size}\""
                    show j 1 u shock at fdis
                    jw "\"Eh?\""
                    "He freezes yet again. Even his tail is completely frozen mid motion."
                    "How is he doing that?!"
                    show j 1 u cshock at fdis
                    jw "\"EHHH?!\"" with hpunch
                    "Aaand, There he goes again."
                    jw "\"No way, no way, no way! What am I going to do now? No one told me this when I applied to this school!\""
                    mc 1 t sigh "\"How did you even pass the transfer exam, anyway? I heard it's harder than our midterms.\""
                    show j 1 u blush at fdis
                    jw "\"I... I didn't have to take one. They took me in for the music program...\""
                    "In other words... kind of like a scholarship?"
                    mc 1 t fsmile "\"Well, I suppose if they've allowed you in without testing you, they might just lower the passing score for you.\""
                    "At least I hope they do. This guy is seriously hopeless if they don't..."
                    show j 1 u bored at fdis
                    jw "\"Ah... ah, is that so. Phew, you really had me worried just now.\""
                    "COMPLETELY BACK TO NORMAL ALREADY?!"
                    show j 1 u happy at fdis
                    j "\"Anyway, I'm Jun. Jun Kobayashi. Pleased to meet you.\""
                    "I hesitate for a second when he extends his hand towards me."
                    "This guy is completely throwing me off my pace..."
                    "As soon as I grab his hand, he starts shaking my hand, excitedly."
                    "Actually, maybe too much excitement."
                    "WAY TOO MUCH EXCITEMENT!"
                    mc 1 t fsmile "\"Alright, alright, that's enough for now, okay?\""
                    show j 1 u watch at fdis
                    "He looks completely clueless as I pull my hand away from his death grip."
                    "Geeze, this guy isn't normal by any definition of the word..."
                    mc 1 t smile "\"I'm [povName]. It's nice to meet you too.\""
                    show j 1 u think at fdis
                    j "\"[povName], huh?"
                    show j 1 u happy at fdis
                    extend " It's a wonderful name! I really like it.\""
                    mc 1 t shock "\"Oh, hm... well... Thank you, {size=-4}I guess...{/size}\""
                    mc 1 t fsmile "\"Y-yeah. Thank you. Anyway, if you don't mind, we should probably get going already. It's starting to get late.\""
                    show j 1 u shock at fdis
                    j "\"Oh, right, I forgot.\""
                    show j 1 u at fdis
                    "He dives behind the piano and picks up his bag (there are books and papers falling off of it. This guy really looks like the messy type.)"
                    "Nothing out of the ordinary with the bag itself, though. The owner apparently makes up for the bag's plainness."
                    show j 1 u smile at fdis
                    j "\"Shall we?\""
                    "We leave the music room and I start showing him around the school."
                    stop music2 fadeout 5.0
                    window hide
                    scene SCorridorE with fade
                    $ renpy.pause(1.0)
                    scene SClassE with fade
                    $ renpy.pause(1.0)
                    scene SGateE with fade
                    $ renpy.pause(1.0)
                    scene SLockers with fade
                    $ renpy.pause(1.0)
                    scene SCourt with fade
                    $ renpy.pause(1.0)
                    window show
                    scene SLockers
                    play music "music/night.ogg" fadein 10.0
                    show j 1 u shock at fdis, five
                    with fade
                    j "\"W-Wow. This school's really big. We haven't even seen everything and my legs are already trembling from all the walking.\""
                    "I think that's more to do with you being out of shape and less to do with the school's size."
                    "... Though I should probably hold off on saying something that tactless."
                    show j 1 u smile at fdis
                    j "\"Hey, [povLastName]-san, what about the other side of the locker room?\""
                    "The other side? Ah, he's looking at the door to the volleyball courts."
                    "Wait, should I even let him go there in the first place?"
                    play sound "music/disappointment.ogg"
                    "When I took him to the Tennis Court, he just kept walking around like a kid in an amusement park, shouting things like: \"So this is what a tennis court looks like!\" and \"It's so amazing\"."
                    "He even took a few pictures. God knows what {i}those{/i} are about."
                    mc 1 t "\"That's for the volleyball courts. I don't think I'm allowed to take you there though. I'm not a member of that club.\""
                    show j 1 u watch at fdis
                    j "\"What about the tennis courts? Did you have permission to take me there?\""
                    "I think the big tennis bag I'm carrying with me should have been enough to tell him I'm a member, but this guy is apparently very dense..."
                    mc 1 t sigh "\"Huh? W-well... I'm a member.\""
                    "Shouldn't the clothes and the big tennis bag I carry around have tipped you off to that?"
                    show j 1 u gentle at fdis
                    j "\"Wow, really? I've never really watched a match live but it totally looks like an awesome sport. {size=-6}I don't know any rules, though.{/size}\""
                    "Gah, too much. This guy is too much!"
                    "He has way too much gas in his tank, I don't know how to deal with people like that."
                    s 1 v "\"[povFirstName]?\""
                    play music2 "music/BGM/Dog Days.ogg" fadein 8.0
                    show s 1 v at fdis, seven with moveiridis
                    show j 1 u shock at fdis, three with move
                    "Just as I hear a voice calling out to me, Shoichi's head peeks out from behind a couple of lockers."
                    "As soon as he notices me, he smiles and walks up to us."
                    "H-He's completely covered in sweat. His clothes look like they've been submerged in water!"
                    show s 1 v smile at fdis
                    s "\"What are you doing here? I thought you had left already.\""
                    show j 1 u avoid at fdis
                    show s 1 v at fdis
                    "He finally notices Kobayashi, who... seems to have tried to hide behind me."
                    s "\"Who's this? A new club member?\""
                    show j 1 u judge at fdis
                    "Kobayashi's entire body goes stiff as he steps out from behind me."
                    "All of his motions have suddenly turned mechanic."
                    j "\"I-I'm Jun Kobayashi. It's a pleasure to meet you!\""
                    play sound "music/disappointment.ogg"
                    "For some reason, he seems even more nervous around Shoichi than he was with me..."
                    "Shoichi studies him for a few seconds, looking incredibly interested in him."
                    show s 1 v wry at fdis
                    s "\"Kobayashi, huh? If I'm not mistaken, you're the student I was asked to accompany today.\""
                    show j 1 u shock at fdis
                    j "\"M-me?\""
                    "Kobayashi looks to be in shock, taking a step back and nearly choking on his own words."
                    "To be honest, even I'm a little bit surprised."
                    "Shoichi was asked to meet a new student? What for?"
                    j "\"You know about me?\""
                    s "\"Yeah. One of the teachers was supposed to show you around school today, but she called in sick.\""
                    s "\"Since I'm the Student Council President, I was asked to do it in her stead, but...\""
                    show s 1 v considerate at fdis
                    s "\"You never showed up.\""
                    play sound "music/stab.ogg"
                    show j 1 u wince at fdis, shake1
                    "Almost as if he were stabbed by an invisible arrow, Kobayashi's entire body shivers at Shoichi's merciless words."
                    show s 1 v sigh at fdis
                    s "\"And here I waited for almost an hour, losing my first class of the day because you didn't show up.\""
                    play sound "music/stab.ogg"
                    show j 1 u fluster at fdis, shake1
                    j "\"Guh...\""
                    "Another invisible arrow..."
                    show s 1 v happy at fdis
                    s "\"You know, I really wish people would call beforehand if they happen to be late for something. It's not like everyone has infinite free time like some people, right?\""
                    show j 1 u flustert at fdis, shake1
                    j "\"Guuuuhhhh...\""
                    "Kobayashi slumps his shoulder in defeat, mumbling a few incoherent apologies."
                    "The fact that Shoichi could say all that with that smile on his face though..."
                    "Scary. Shoichi, you're scary!"
                    mc 1 t fsmile "\"W-Well, he says he got here a bit late and the gates were already closed. So it's not entirely his fault, right, Kobayashi-kun?\""
                    show j 1 u flusterb at fdis
                    "Kobayashi nods."
                    j "\"Ah, y-yes. I'm sorry I was so late. I had been living in a different town until recently and ended up getting lost. I'm so sorry to have inconvenienced you.\""
                    show s 1 v wry at fdis
                    "In what is certainly an uncharacteristic moment for him, Shoichi examines Kobayashi as if he didn't know what to make of the situation."
                    "I guess I'm not the only one who gets thrown off his pace by this guy."
                    show s 1 v considerate at fdis
                    s "\"Well, it's alright, I suppose. I was mostly joking anyway.\""
                    "IT DIDN'T LOOK LIKE YOU WERE!"
                    show s 1 v smile at fdis
                    s "\"I've already been informed of your circumstances. If you want, I can give you a quick tour.\""
                    show j 1 u shock at fdis
                    j "\"Oh, no, it's alright. [povLastName]-san already did.\""
                    show s 1 v shock at fdis
                    "Shoichi looks at me, dumbstruck."
                    s "\"Wait... [povLastName]-kun... helped? A stranger? Of his own free will? Seriously?\""
                    "Don't look so surprised about it!"
                    mc 1 t annoyed "\"Yeah, I did. Got a problem with that?\""
                    show s 1 v smile at fdis
                    s "\"No, not at all. It was just really unexpected.\""
                    s "\"Have you already taken him to the staff room?\""
                    show j 1 u watch at fdis
                    mc 1 t curious "\"The staff room? Why would I have to take him there?\""
                    show s 1 v shock at fdis
                    "Shoichi stares at me in surprise."
                    show s 1 v sigh at fdis
                    s "\"New students have to be assigned a teacher as their counselor when they join. You should know this, we did it two years ago.\""
                    "Oh... Now that he mentioned it, I do remember something like that."
                    "Wait, is this why I'm always having to deal with Katsuragi-sensei? I honestly didn't remember."
                    mc 1 t fsmile "\"Oh, I completely forgot.\""
                    "Y-You don't have to look at me with such disappointed eyes!"
                    "It's not my fault, you know. You can't expect me to remember that. It was a whole two years ago."
                    show j 1 u shock at fdis
                    j "\"I-It's no problem. I mean, even if we don't get to finish everything today, he still helped a lot.\""
                    show s 1 v wry at fdis
                    "Judging from Shoichi's expression, I guess even he must be having serious problems coming up with things to say in this situation."
                    "He does tend to take his responsibilities quite seriously, so he's probably trying to figure out how much he can still do before school closes."
                    show j 1 u watch at fdis
                    s "\"Well, I guess it should be fine. I'll explain to the teacher in charge of admissions that you couldn't show up today. I'm sure he'll understand.\""
                    show s 1 v considerate at fdis
                    s "\"There's not much we can do since all the teachers have already gone home so just hang tight until tomorrow, okay?\""
                    show s 1 v think at fdis
                    s "\"Actually, Kobayashi-san, would you mind if I borrow [povLastName]-kun? I need him to help me with something.\""
                    show j 1 u shock at fdis
                    j "\"O-oh. It's fine. {size=-4}Though I was looking forward to seeing the volleyball courts.{/size}\""
                    show s 1 v laugh at fdis
                    show j 1 u watch at fdis
                    s "\"It's fine if you want to. I can take you to the courts. I was going to ask [povLastName]...\""
                    show s 1 v shock at fdis
                    "Shoichi stumbles on his speech when saying my name."
                    show s 1 v avoid at fdis
                    "For some reason, he tends to treat everyone very formally when around other students, even his own friends."
                    "Still, it sounds pretty weird to hear my last name come out of his mouth. And I'm sure it must be even weirder for him to say it."
                    show s 1 v wry at fdis
                    s "\"Ah, sorry, I'm not used to calling him by his last name.\""
                    mc 1 t sigh "\"If it bothers you so much, why are you doing it?\""
                    "Shoichi starts rubbing the back of his neck."
                    show s 1 v considerate at fdis
                    s "\"You're supposed to use polite speech when you're first introduced to someone, after all.\""
                    mc 1 t sigh2 "\"Stop being so stuck up and call me by my name. You're trying too much to sound like an adult. It's creepy. And annoying.\""
                    "Kobayashi starts laughing."
                    "Shoichi glares at me."
                    show j 1 u cshock at fdis
                    j "\"I-I'm sorry, hahaha. It's- It's okay, hahaha.\""
                    "He takes a minute to steady his breathing before he tries to resume talking."
                    show j 1 u smile at fdis
                    j "\"If you feel uncomfortable calling him that, then you don't need to force yourself just because I'm around. Actually, I really hate polite speech. If you'd prefer, you can just call me Jun.\""
                    j "\"I know I'd like it better if you did.\""
                    show s 1 v happy at fdis
                    "Shoichi ponders it for a second before nodding."
                    s "\"All right. In that case, you can just call me Shoichi.\""
                    show j 1 u gentle at fdis
                    "Kob- no, Jun-kun bows excitedly. This time he doesn't look like a clockwork piece."
                    show s 1 v smile at fdis
                    s "\"Well, since that's out of the way.\""
                    show s 1 v happy at fdis
                    s "\"You can look at the volleyball courts all you want. I'm the only one around right now.\""
                    s "\"I was actually hoping to get [povFirstName] to help me with my training.\""
                    "Shoichi looks at me expectantly."
                    "I think of backing out but, when I turn around, I see Jun-kun beaming with excitement."
                    mc 1 t sigh "\"All right, fine. But let's not take too long, okay? I was intending to go home soon...\""
                    show s 1 v smile at fdis
                    s "\"Yeah, no problem.\""
                    scene Volley
                    show j 1 u shock at fdis, three
                    show s 1 v smile at fdis, seven
                    with fade
                    "Jun-kun starts strolling around, pointing and gasping at everything in sight (even a ball cart. Who gets excited over a ball cart?)"
                    "Shoichi makes his way to the setter position. I see a pretty big pool of sweat beneath his feet."
                    "How long has he been practicing?"
                    show s 1 v happy at fdis
                    s "\"Okay. [povFirstName], get into position and throw me the ball.\""
                    "This is a drill I've already done a ton of times."
                    "Since Shoichi makes me help with his practice constantly, I've learned quite a lot about volleyball."
                    "Also, I seem to be pretty decent at it."
                    "Well, I tend to be pretty decent at most things anyway."
                    "I throw the ball right over Shoichi's head. When it's a little above the net, he jumps, tossing the ball into the air."
                    "I start running as soon as he jumps."
                    "I make sure of the ball's position and I too jump towards it. I aim my spike just over the line."
                    "The ball hits the floor with a resounding \"WHAM\", right on top of the line."
                    show s 1 v laugh at fdis
                    s "\"Nice spike.\""
                    show j 1 u shockb at fdis
                    j "\"WOAH!\"" with hpunch
                    "A deafening voice assaults my ears."
                    j "\"How can you jump so high? And the sound the ball made when it hit your hand was so loud! Doesn't your hand hurt after hitting it like that? And how did you aim it so close to the line? And...\""
                    show s 1 v considerate at fdis
                    show j 1 u watch at fdis
                    s "\"Now, now. How about we time-out for a bit?\""
                    "Even Shoichi is taken aback by his sudden outbursts of excitement."
                    "I've only met him today and I'm already having a hard time dealing with it."
                    "And he studies in the same class as me..."
                    show s 1 v smile at fdis
                    s "\"This is a pretty simple thing if you train your legs. [povFirstName] might not have to jump as often as a volleyball player, but he still has very strong legs from playing tennis.\""
                    show s 1 v think at fdis
                    s "\"As for if it hurts his hand... I guess you could say that it stings a bit, but... I'm not sure if I can call it \"painful\".\""
                    show s 1 v happy at fdis
                    s "\"Aiming is just a matter of practicing a lot, too.\""
                    show s 1 v smile at fdis
                    s "\"Now... Mind if we continue?\""
                    show j 1 u happy at fdis
                    j "\"Please do!\""
                    "Shoichi hands me another ball."
                    show j 1 u watch at fdis
                    "Guh, I can feel Kobayashi's eyes on me right now. He really is watching intently..."
                    "I toss the ball to Shoichi again and we repeat the drill. It goes over his head and, right when it's at the top of the net, he jumps and tosses the ball whilst in midair."
                    "Shoichi's tosses are incredibly accurate and easy to spike. He's the sort of setter that prioritizes easy to spike tosses. As such, he's very well liked by his team."
                    "He's already considered the best setter in our prefecture, maybe even in the whole country, though it'd be hard to tell for sure."
                    "Despite how good he is, the rest of his team is only average so they've only managed to qualify for the National Tournament once."
                    "He'd be really mad at me if I said it out loud, though."
                    "We keep doing this drill for a while. Every now and then, Jun stops us to ask questions. At first he was only asking us things about volleyball but..."
                    show j 1 u think at fdis
                    show s 1 v think at fdis
                    j "\"So, how long have you guys known each other?\""
                    "He's starting to get way too personal!" with hpunch
                    "Shoichi doesn't seem fazed by it in the slightest."
                    "Well, it probably doesn't take too long for a guy as sociable as Shoichi to adapt to this sort of thing."
                    "In fact, he's in a really good mood, constantly smiling and going with whatever Jun asks."
                    s "\"Let me see, I guess it's been... about 12 years, right, [povFirstName]?\""
                    mc 1 t "\"I guess it would be something like that, yeah.\""
                    show j 1 u shock at fdis
                    j "\"Wow. That's a long time to get to know each other.\""
                    show s 1 v smile at fdis
                    s "\"We met during our sports club's training camp.\""
                    show s 1 v laugh at fdis
                    s "\"It turned out that we both went to the same club but had never met since we played different sports.\""
                    show s 1 v wry at fdis
                    s "\"If we hadn't shared a seat in the bus back then...\""
                    "It looks like he is reminiscing."
                    "Come to think of it, I hadn't really paid much attention to how long we've known each other for. When I think about it, I barely do anything without Shoichi these days."
                    show s 1 v laugh at fdis
                    s "\"When I think of it, It's almost like having a younger brother.\""
                    mc 1 t sigh "\"I see what you mean but... Why am I the younger brother? I'm older than you.\""
                    show s 1 v seductive at fdis
                    s "\"You get to be the older brother when you learn to take care of yourself without inconveniencing other people.\""
                    play sound "music/stab.ogg"
                    "Guh..."
                    show j 1 u happy at fdis
                    j "\"It must be nice being so close with someone. I don't have any friends. Not since I last switched schools, anyway.\""
                    show s 1 v happy at fdis
                    "Shoichi smiles. Just the atmosphere around him is already helping keep the shy and jumpy new guy at a better mood."
                    "He's just so good with people that others can't help but relax around him."
                    show s 1 v smile at fdis
                    s "\"You shouldn't worry too much. If you want, you can just hang out with us. You're in the same class as [povFirstName] anyway, right?\""
                    show j 1 u shock at fdis
                    j "\"O-Of course. Thank you very much!\""
                    "And just like that, it seems we've adopted a stray cat..."
                    scene SLockers
                    show s 1 v laugh at fdis, three
                    show j 1 u happy at fdis, seven
                    with fade
                    "We spend almost an hour helping Shoichi practice."
                    show s 1 v happy at fdis
                    s "\"Hey, [povFirstName]. Would you mind waiting around for me? I'll just towel myself off and get changed.\""
                    mc 1 t "\"Sure.\""
                    show j 1 u smile at fdis
                    j "\"Well, I guess I'll get going now. It's already pretty late.\""
                    show j 1 u happy at fdis
                    j "\"[povFirstName]-san, Shoichi-san, thanks for the help!\""
                    show j 1 u at offscreenleft with moveoledis
                    show s 1 v smile at fdis, five with move
                    "Jun-kun bows and takes his leave."
                    show s 1 v avoid at fdis
                    "Shoichi, you're so easy to read. You're obviously annoyed that he added the \"-san\" aren't you?"
                    s "\"I did tell him to drop the honorifics, didn't I?\""
                    mc 1 t sigh "\"You {i}were{/i} acting very formal around him. Poor guy is probably confused.\""
                    show s 1 v at fdis
                    s "\"Well, I guess that's true... He's a pretty interesting boy, though.\""
                    mc 1 t sigh "\"Yeah, tell me about it! ... A little bit too hyper for me.\""
                    show s 1 v at fdis
                    s "\"Really? I find it endearing.\""
                    "I sit down on one of the benches and wait around until Shoichi is done getting dressed."
                    scene SGateN
                    show s 1 u smile at fdis, five
                    with fade
                    play music "music/night.ogg"
                    "It got so late while we were goofing around that it's already gotten dark."
                    show s 1 u shock at fdis
                    mc 1 t curious "\"By the way, Shoichi... how did you get to stay so late in the courts? I noticed that no one came around to close it.\""
                    show s 1 u smile at fdis
                    s "\"I got the keys from my coach.\""
                    mc 1 t shock "\"... I thought they didn't allow students to stay at school after class.\""
                    show s 1 u wry at fdis
                    s "\"Of course they do. All you have to do is ask nicely and sign a term of responsibility.\""
                    mc 1 t sigh2 "\"Sorry, I'm not cut out for that sort of thing.\""
                    show s 1 u considerate at fdis
                    s "\"What? Not cut out for being a normal person?\""
                    label day1_goinghomefinal:
                    scene Street1N
                    show s 1 u smile at fdis, five
                    with fade
                    s "\"Anyway. Did you have fun on your first day?\""
                    mc 1 t sigh "\"Meh. It's the same as every year, really.\""
                    show s 1 u wry at fdis
                    s "\"Well... I thought you'd be a little more excited after practice.\""
                    show s 1 u happy at fdis
                    s "\"You had a great practice match today and you didn't even care about it.\""
                    mc 1 t sigh "\"I wouldn't say that I didn't care, it's just... I don't even know. It didn't give me the usual thrill.\""
                    "Shoichi cuts in front of me, forcing me to stop."
                    play sound "music/flick.ogg"
                    "When I start asking him what he's doing, he flicks me in my forehead."
                    show s 1 u annoyed at fdis
                    s "\"You've been like that for the past three years already. It needs to stop, it's not healthy.\""
                    "I rub at the spot he flicked me. Damn, that stung."
                    mc 1 t annoyed "\"Been like what? I don't know what you're talking about.\""
                    show s 1 u sigh at fdis
                    s "\"How dense can you be? It's obvious for me since I've been watching you play since we were kids.\""
                    show s 1 u at fdis
                    s "\"You have something on your mind, don't you? What is it?\""
                    mc 1 t sigh2 "\"I don't know. If there's anything going on with me, it's certainly not intentional. You think I like making almost no progress in practice?\""
                    show s 1 u shock at fdis
                    s "\"So you've noticed your slow development?\""
                    mc 1 t annoyed "\"Of course I noticed. How dumb would I have to be in order not to?\""
                    mc 1 t wince "\"It's so frustrating. I see players that were clearly weaker than me two or three years ago suddenly beat me with ease.\""
                    mc 1 t annoyed "\"And that, of course, only makes me even more anxious.\""
                    "Shoichi scratches his head in confusion."
                    scene Street2N
                    show s 1 u avoid at fdis, five
                    with fade
                    s "\"I guess I know what you mean. Tennis is a pretty lonely sport. You've only got yourself to rely on.\""
                    show s 1 u wry at fdis
                    s "\"That's why I like volleyball. Your teammates are always there to cover for you and help you along if you're having difficulty.\""
                    mc 1 t sigh "\"The way I see it, I could be playing my best and clearly be the best player and yet still lose because my team dragged me down.\""
                    mc 1 t avoid "\"{size=-8}It's what's been happening to you.{/size}\""
                    show s 1 u doom at fdis
                    s "\"I'm sorry, I didn't catch that. What did you say?\""
                    mc 1 t cshock "\"Nothing.\""
                    show s 1 u think at fdis
                    "We walk along in silence for a few minutes."
                    "I'm usually pretty bad with words. At times like this I usually rely on Shoichi to keep the conversation going."
                    "If he goes quiet too..."
                    show s 1 u wince at fdis
                    s "\"Sorry.\""
                    mc 1 t shock "\"Huh? What for?\""
                    show s 1 u wry at fdis
                    s "\"I know you're uncomfortable talking about this. I shouldn't have said anything.\""
                    mc 1 t fsmile "\"It's... fine. To be honest, Katsuragi-sensei was also saying the same thing.\""
                    mc 1 t fsmile "\"She says I stopped trying to excel. She's not entirely wrong either.\""
                    mc 1 t sigh "\"I'll admit. I used to try a lot harder before, both in tennis and in school. I guess I just lost my drive.\""
                    show s 1 u happy at fdis
                    s "\"Wow. You shouldn't worry about it too much. Even if you're like this now, you're aware of your faults and are working to change.\""
                    show s 1 u wry at fdis
                    s "\"I'm sure things will work out.\""
                    mc 1 t wry "\"Always the optimist, huh?\""
                    show s 1 u happy at fdis
                    s "\"I try.\""
                    show s 1 u laugh at fdis
                    "Shoichi wraps his arms over my neck and pulls me closer, petting my head."
                    "I let him have his fun for a while. I guess I'm in a good mood."
                    "He does take the concept of skinship a little too far sometimes, though."
                    "Before I notice it, we're almost at my house."
                    "Damn, it was so pleasant that I completely zoned out."
                    mc 1 t avoid "\"You can let go of me now.\""
                    show s 1 u seductive at fdis
                    s "\"Oh. Feeling self conscious?\""
                    mc 1 t sigh2 "\"No. I just think I've already let you have enough fun. We're even now.\""
                    s "\"I think you were having way more fun than I was.\""
                    mc 1 t sigh "\"I don't know what you're talking about.\""
                    s "\"Heh. Sure thing.\""
                    "He pulls away from me."
                    show s 1 u wry at fdis
                    s "\"By the way, I know I sound like a broken record but...\""
                    show s 1 u considerate at fdis
                    s "\"This is our last year of high school. It'd be a shame if we spent it freaking out about the future. Let's just take things one step at a time, okay?\""
                    mc 1 t smile "\"Sure. And I guess I should consult with a few coaches about a new training program.\""
                    show s 1 u shock at fdis
                    s "\"Oh, that sounds like a good idea. A change of routine might actually help you with that psychological block of yours.\""
                    show s 1 u smile at fdis
                    s "\"Why don't you ask one of your sponsors to get you a personal coach?\""
                    mc 1 t nervous "\"Nah. I don't want them to think they've got too much power over me.\""
                    show s 1 u sigh at fdis
                    s "\"They already send you equipment and help pay for your travel expenses. Pretty safe to say they've got a lot of power over you and they {i}know{/i} it.\""
                    show s 1 u seductive at fdis
                    mc 1 t avoidb "\"Oh, shut up.\""
                    "Shoichi grins."
                    show s 1 u happy at fdis
                    s "\"Well, not that it matters anyway. I'm sure there are lots of professional coaches in Japan that would like to work with you.\""
                    show s 1 u smile at fdis
                    s "\"Plus, almost all players in the country would jump at the opportunity of practicing with you.\""
                    "Oh, now that he mentioned it, I'm pretty sure I heard something about an exchange program... Oh, that's right."
                    mc 1 t think "\"Actually, I kinda just remembered, but there are a few tennis clubs out of our prefecture holding an exchange program.\""
                    mc 1 t think "\"The minimum requirement is being ranked 12 or higher on the Kanto Junior Ranking."
                    show s 1 u shock at fdis
                    s "\"Does that mean Tanabe would be participating too?\""
                    "Takagi Tanabe is the current #1 player in the U-18 circuit. I've known him since I first played against him on the U-13 Kanto Tournament."
                    "We've already faced each other over twenty times and I've never beaten him. Not even once."
                    mc 1 t think "\"I... think so. His club is the one organizing it all.\""
                    show s 1 u laugh at fdis
                    s "\"That's great, then. Why don't you go? What's your ranking in Kanto right now? 3? 4?\""
                    mc 1 t annoyed "\"2. And I don't know if I should.\""
                    mc 1 t wince "\"I mean, I'd definitely get a good amount of practice, but I'm afraid I might psych myself out if I meet him there.\""
                    show s 1 u annoyed at fdis
                    s "\"You're refusing the opportunity of practicing against the best player in the country? You?! This is more serious than I thought. Your heart's turned to glass.\""
                    mc 1 t sigh "\"Shut up! I'm not afraid of it or anything, I just...\""
                    "Honestly, I might actually be scared."
                    "I have avoided playing Keisuke all this time for no reason other than him reminding me of Takagi."
                    "Maybe I really do have a block."
                    show s 1 u wry at fdis
                    "Shoichi examines me with a concerned look."
                    show s 1 u considerate at fdis
                    s "\"Well, you don't have to worry about it too much. Whether you decide to go or not, you'll still have good practice partners over here.\""
                    show s 1 u wry at fdis
                    s "\"You can always use Urushihara as your Tanabe proxy.\""
                    mc 1 t cocky "\"Kei-kun's skills aren't nearly as refined as Takagi's.\""
                    show s 1 u laugh at fdis
                    s "\"Ouch. Poor Urushihara.\""
                    scene HouseFrontN
                    show s 1 u smile at fdis, five
                    with fade
                    s "\"Well, we're here.\""
                    show s 1 u happy at fdis
                    s "\"Sorry I can't stay for a while, I have some stuff I need to work on right away.\""
                    s "\"Tell Aki-kun and your mom I said hi.\""
                    mc 1 t smile "\"Sure. Message me if you need anything.\""
                    show s 1 u laugh at fdis
                    s "\"Of course.\""
                    show s 1 u laugh at offscreenleft with moveoledis
                    hide s 1 u laugh
                    "Shoichi waves at me without turning back and keeps walking away."
                    "It's a good thing he lives so close, but it tends to get annoying when he pops in without a warning."
                    stop music2 fadeout 6.0
                    scene HouseEntrance with fade
                    play sound "music/door.ogg"
                    mc 1 t think "\"Mom, Aki, I'm home!\""
                    "Hmm... Mom's shoes aren't here. Maybe she's out?"
                    scene LivingRoomN with fade
                    "I hear footsteps coming from the stairs."
                    "My little brother, Akiyoshi, walks down."
                    show a 1 c at fdis, fiveh with moveiledis
                    mc 1 t smile "\"Oh, Aki. You're home already, huh?\""
                    a 1 c sigh "\"What do you mean \"already\"? It's pretty late.\""
                    a 1 c "\"By the way, mom said she'd be late again so you'll have to cook.\""
                    "Straight to the point, huh?"
                    mc 1 t laugh "\"Ah, you're right. I'll get right to it. Sorry you had to wait for me.\""
                    a "\"It's fine. I figured you'd be staying late for practice anyway.\""
                    "Well, it wasn't because of practice, but if he's okay with it, I won't complain."
                    scene KitchenN
                    show a 1 c at fdis, five
                    with fade
                    mc 1 t smile "\"What do you want me to cook for you?\""
                    a "\"Just some rice would be fine. I don't really care.\""
                    mc 1 t sigh "\"You're telling me you went to practice today, worked up a sweat and all you want to eat is rice? You need to eat properly if you want to get stronger.\""
                    a 1 c sigh "\"Guh... you're starting to sound like mom.\""
                    mc 1 t smile "\"Hey, I'm telling you this as an athlete to an aspiring athlete. You need to watch what you eat. What are you going to do if you go to the third set and you can't even run anymore?\""
                    a "\"I'm twelve. We don't play 3-set matches yet.\""
                    mc 1 t happy "\"You will someday. Might as well start working up your stamina right now.\""
                    a 1 c sigh2 "\"Alright, alright. Just make whatever you want.\""
                    show a 1 c at fdis
                    "Time goes by pretty fast when I'm cooking and chatting with Aki."
                    "He seemed to really want to talk, seeing how I could barely get a word in."
                    "It was all about tennis, too."
                    "By the time I finished cooking he was still talking like there was no tomorrow."
                    "It's hard getting him to shut up once he gets started."
                    "Was I this passionate about it when I was his age?"
                    scene LivingRoomN with fade
                    "Oh, wow, it's already 10:30PM."
                    "I told Aki I'd go to sleep just a little while after him, and he's already been gone for over an hour."
                    "Blasted video games. Always distracting me."
                    play sound "music/door.ogg"
                    "I hear the sound of the door opening."
                    show mom 1 s smile at fdis, five with moveiridis
                    "I see my mom coming in. Once she sees me, she looks surprised."
                    mom "\"Oh, [povFirstName], you're still awake. Did you make dinner for Akiyoshi and you? Is everything okay?\""
                    mc 1 c sigh2 "\"Everything's fine, mom. You don't have to freak out every time you come home late. Aki's already gone to bed.\""
                    mom "\"I'm sorry, sweetie. You know I worry about you two.\""
                    mom "\"Oh, and by the way, I got a call from one of your teachers today.\""
                    "W-what?"
                    mom "\"He said you forgot a racket at the locker room. Honestly, you should be more careful, you know those have been custom made for you.\""
                    mc 1 c smile "\"Sorry, sorry...\""
                    "Phew. For a second there, I thought she had spoken to Katsuragi-sensei."
                    "No, wait, there's something wrong with what she just said."
                    mc 1 c sigh "\"That's... weird. I always check my bags before leaving and I had everything with me.\""
                    "I pick up my tennis bag near the door and check it over again."
                    "Yep, everything's here."
                    mc 1 c confused "\"Who's the teacher that called you?\""
                    mom "\"Hmmm... I think his name was Mi... Mina... Mikado? Hold on, I know I wrote it down somewhere.\""
                    "LIES!" with hpunch
                    mc 1 c sigh2 "\"Mikado Amanuma?\""
                    mom "\"Yes, that's it.\""
                    mc 1 c sigh "\"That's our coach. He hasn't shown up for practice for the past three weeks.\""
                    mc 1 c sigh2 "\"I think it's safe to say he doesn't have one of my rackets. He probably just wants me to run some sort of errand for him.\""
                    mom "\"He's still your teacher. You can't just assume he's lying.\""
                    "You don't know him as well as I do."
                    mc 1 c sigh2 "\"Yeah, sure. I'll talk to him tomorrow then.\""
                    "Assuming he ever shows up."
                    mc 1 c smile "\"Good night, mom.\""
                    mom "\"Night, sweetie.\""
                    scene BedroomN with fade
                    "Once in my bedroom, I decide to check my phone."
                    "..."
                    "Oh, it looks like Saya sent me a message."
                    show ph with dissolve
                    show sac
                    show sa1 at Position(xpos=506, ypos=162, xanchor=0, yanchor=0)
                    show sa2 at Position(xpos=506, ypos=232, xanchor=0, yanchor=0)
                    $ renpy.pause (1.0)
                    "..."
                    "I knew it. This is another one of his schemes, isn't it?"
                    "Last time, he told us he was taking us to watch a professional tournament in Tokyo. "
                    "Instead, he took us to the club he used to work for and forced us to work as assistant-coaches for the weekend."
                    "Said it would \"expand our horizons\" if we learned how it was dealing with a player."
                    show asa1 at Position(xpos=574, ypos=282, xanchor=0, yanchor=0) with dissolve
                    $ renpy.pause(1.0)
                    play sound "music/message.ogg"
                    show sa3 at Position(xpos=506, ypos=332, xanchor=0, yanchor=0) with dissolve
                    $ renpy.pause(1.0)
                    play sound "music/message.ogg"
                    show sa4 at Position(xpos=506, ypos=382, xanchor=0, yanchor=0) with dissolve
                    $ renpy.pause(0.5)
                    play sound "music/message.ogg"
                    show sa5 at Position(xpos=506, ypos=432, xanchor=0, yanchor=0) with dissolve
                    $ renpy.pause(0.5)
                    "Well, as long as Saya is dealing with him, there's no need for me to go."
                    show asa2 at Position(xpos=730, ypos=482, xanchor=0, yanchor=0) with dissolve
                    $ renpy.pause(0.5)
                    stop music
                    jump day2

                "It's too much trouble...":
                    $ tour_jun = False
                    play music2 "music/BGM/Windswept.ogg" fadein 6.0
                    "I feel sorry for him, but..."
                    "It's not my job to take care of lost transfer students."
                    "Plus, he seems way too hyper. I think it'd be hard dealing with him for that long."
                    mc 1 t avoid "\"Well, you should probably look for a different teacher tomorrow. Go to the staff room early in the morning and ask for Imayoshi-sensei. He'll probably help you.\""
                    show j 1 u watch at fdis
                    "He nods."
                    jw "\"Yeah, sure, I guess.\""
                    show j 1 u smile at fdis
                    jw "\"Maybe I'll find a teacher that is easier to deal with, right?\""
                    "His hand keeps brushing up against the piano keys every now and again."
                    mc 1 t cocky "\"Could it be you're waiting for me to leave so you can play?\""
                    show j 1 u cshockb at fdis
                    jw "\"HUH?!\"" with vpunch
                    "His incredibly exaggerated reaction tells me that I'm right."
                    mc 1 t smile "\"Sorry. If me being here bothers you, I can leave.\""
                    show j 1 u blush at fdis
                    jw "\"N-no. It's not that... it's just. I've... hmmm...\""
                    "He averts his gaze."
                    "Is he... blushing?"
                    jw "\"It's been a while since I last had an audience. So... hmm...\""
                    mc 1 t curious "\"So... what? You're afraid you might mess up?\""
                    "He nods, meekly. I laugh, and that seems to embarrass him even further."
                    mc 1 t smile "\"Sorry, sorry. I'm not laughing at you, I swear. I kinda know how you feel. I used to be the same way.\""
                    show j 1 u watch at fdis
                    "His ears perk up. He turned to look at me with a puzzled look."
                    jw "\"Do you play?\""
                    mc 1 t fsmile "\"Oh, no, no. I don't mean piano. I could never do something so complicated.\""
                    mc 1 t smile "\"I'm a tennis player, actually. Back when I went to my first tournament, I got so nervous that I didn't realize my shoe became untied.\""
                    mc 1 t laugh "\"I ended up stepping on the string in the middle of a very important point and had a big fall face first into the ground.\""
                    mc 1 t smile "\"It was mortifying, though today I can look back and laugh at it.\""
                    show j 1 u think at fdis
                    jw "\"So you play tennis, huh? I don't really know anything about tennis, even though my father is a big fan.\""
                    show j 1 u wince at fdis
                    jw "\"Isn't it a very difficult sport?\""
                    mc 1 t think "\"Hmm, well... That's kind of a tricky question. I haven't played many other sports so I can't really compare.\""
                    mc 1 t smile "\"At least I wouldn't say it is, but I know other people who might disagree.\""
                    mc 1 t smile "\"Our school has a tennis club, so, if you're interested, you could join and see for yourself.\""
                    show j 1 u wince at fdis
                    jw "\"Ah. No, no. Even if I liked it, I can't really play sports. I'm no good at them.\""
                    mc 1 t smile "\"There's no harm in going just to watch, though.\""
                    show j 1 u bored at fdis
                    jw "\"But what if I end up bothering the club members?\""
                    mc 1 t happy "\"Our practices aren't really open to the public, but I could put in a word for you.\""
                    mc 1 t smile "\"I'm the vice-captain, so I can pretty much do what I want {size=-10}as long as Saya doesn't find out{/size}.\""
                    mc 1 t happy "\"How about this: You play one more song for me and, in exchange, I show you one of our practice sessions?\""
                    show j 1 u shock at fdis
                    "The boy stares at me in disbelief. He flashes a cheerful, toothy smile and seems to get really excited about it."
                    "It's kinda cute to be honest."
                    show j 1 gentle at fdis
                    jw "\"I'd love to.\""
                    "He adjusts himself in his seat and places his hands on the keys."
                    show j 1 u smile at fdis
                    "He glances over to me one last time, still looking a little embarrassed."
                    "I nod once and that seems to give him some confidence."
                    show j 1 u sigh at fdis
                    "He closes his eyes and puts a hand to his chest, murmuring something incoherent."
                    show j 1 u blank at fdis
                    "When he opens them again, he has a very sharp, almost unrecognizable look on his face."
                    "His hands touch the keys again and..."
                    stop music2 fadeout 2.0
                    show cg2 with dissolve
                    play music3 "music/BGM/Classical/Etude Op25 N12.ogg" fadein 4.0
                    "The room is immediately taken over by a fast paced song."
                    "It's not a song I, with my limited knowledge of classical music, have ever heard."
                    "But the notes quickly come together to form a very beautiful, urgent melody."
                    "I can't believe this guy was insecure about his playing."
                    "If this can be played even better than this then this must be an amazing song."
                    "No, even as it is right now, it's nothing short of amazing."
                    "He hammers all the notes in quick succession, his fingers dancing madly on the keyboard."
                    "He doesn't look at me, not even once. As he concentrates further and further, he seems to be completely zoned out."
                    "After a while, he closes his eyes, shifting even further into gear."
                    "You've got to be kidding me. There's an even higher level for him?"
                    "It's like, all of a sudden, everything else has been erased from his world. The only thing that exists is the piano."
                    "My body answers his song. I feel the notes vibrating across my entire body."
                    "I catch myself tapping on a nearby table, following the rhythm."
                    "In a way, he reminds me of Kei-kun."
                    "He also tends to get so absorbed in his matches that he completely loses sight of everything around him."
                    "I just have to be careful not to startle him like I did just a few minutes ago."
                    "It'd be a shame if he stopped abruptly like last time."
                    "He starts playing it faster and faster."
                    "Is this guy some sort of piano genius?"
                    stop music3 fadeout 2.0
                    play music2 "music/BGM/Classical/Etude Op10 N4.ogg" fadein 4.0
                    "Before I notice it, he has already finished the song."
                    "Then, he immediately starts playing another one."
                    "He has a very carefree smile on his face, beaming with energy."
                    "Sweat drips from his eyebrow and falls on his still closed eye."
                    "It must be exhausting to play like this."
                    scene MusicRoomN
                    show j 1 u happy at fdis, five
                    with fade
                    play music "music/night.ogg" fadein 10.0
                    "He keeps rocking his body back and forth with the music, his tail swaying from side to side."
                    "It plucks at the heart strings."
                    stop music2 fadeout 4.0
                    "When he finally stops playing, he keeps his eyes fixed on the piano, panting in exhaustion."
                    "He finally turns to me."
                    jw "\"That... That was the best I've played in a while.\""
                    mc 1 t happy "\"I don't really know anything about classical music but that was amazing. Seriously, it was incredible."
                    jw "\"Hehe... thanks.\""
                    "He smiles bashfully. Not very good at taking a compliment, is he?"
                    jw "\"Ah, it's been a while since I last felt this satisfied with my music.\""
                    show j 1 u wince at fdis
                    jw "\"Actually... I'm feeling really tired now. Did I go overboard again?\""
                    show j 1 u think at fdis
                    jw "\"What time is it?\""
                    "When I look for the clock on the wall, I notice the sun isn't shining through the window anymore."
                    "It couldn't be..."
                    "I look at the window and only see stars."
                    mc 1 t fsmile "\"Oh no...\""
                    "The boy follows my gaze."
                    show j 1 u cshock at fdis
                    play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
                    "He immediately freezes."
                    "We just keep staring at the window, waiting for reality to sink in."
                    "I pull my phone out of my pocket, not believing what I'm seeing."
                    mc 1 t fsmile "\"7...7:49PM...\""
                    mc 1 t wince "\"This might be a problem...\""
                    "I try to remain calm because, from the looks of it, this guy is already starting to panic."
                    mc 1 t fsmile "\"No worries, though. I'll just call Hakumo-sensei and ask her if she can come open things up for us.\""
                    mc 1 t fsmile "\"She lives nearby and every teacher has spare keys for the school.\""
                    "I actually wish I could panic, but it looks like I'd have an unmanageable situation in my hand if I did."
                    "This guy doesn't look any good under pressure."
                    stop music2 fadeout 5.0
                    scene SGateN with fade
                    play music "music/night.ogg"
                    "Luckily, Hakumo-sensei picked up her phone right away. She scolded us quite a lot for managing to get locked inside, though she later said the teacher in charge of our floor should have realized that we were inside."
                    "After all, how would he lock us inside the room and not hear the piano being played?"
                    "Hakumo-sensei offers us a ride in her car. Since I live nearby, I refuse."
                    "The tiger, though, ends up taking it, since he's not too familiar with the town yet."
                    "And just like that, I'm alone in front of school at 8PM."
                    s 1 u laugh "\"Sup!\""
                    mc 1 t dismay "\"GAAH!\"" with vpunch
                    show s 1 u happy at fdis, five with dissolve
                    "I feel a hand touching my shoulder and immediately jump away."
                    "Shoichi is standing behind me, laughing his ass off."
                    play music2 "music/BGM/Dog Days.ogg"
                    show s 1 u laugh at fdis
                    s "\"HAHAHA! Oh my God. Look how far you jumped!\""
                    mc 1 t wince "\"What the hell? What are you even doing here?\""
                    show s 1 u smile at fdis
                    s "\"I was doing some late practice. I've spent the past two hours just practicing serves.\""
                    show s 1 u wry at fdis
                    s "\"My last teammate left a while ago, saying he couldn't feel his legs.\""
                    "You shouldn't force your teammates to play until they can't feel their legs."
                    mc 1 t sigh2 "\"Wait. How are you even here? Shouldn't you have gone home a few hours ago?\""
                    show s 1 u at fdis
                    s "\"Coach let me borrow the keys.\""
                    "Wait... so I could have just called Shoichi?"
                    "No, but we were locked inside the building. Surely he doesn't also have the main building's keys..."
                    "..."
                    "Right?"
                    show s 1 u smile at fdis
                    s "\"Are you going home now?\""
                    mc 1 t sigh2 "\"Yeah. I've had enough with being locked in for today.\""
                    show s 1 u sigh at fdis
                    s "\"Locked in? Seriously? How did you even manage that feat?\""
                    mc 1 t wince "\"I kinda lost track of time. I'm surprised no one found us when they were closing up.\""
                    show s 1 u seductive at fdis
                    "Shoichi grins."
                    s "\"Oh? So it's \"us\", not \"I\". What happened? Do tell.\""
                    mc 1 t sigh2 "\"Ugh, it's a long story. I'll tell you tomorrow.\""
                    s "\"Sure. Who were you even locked in with? Was it Saya-chan?\""
                    mc 1 t wince "\"No, it was... uhm...\""
                    "Crap, I forgot to ask for his name. And I even promised to take him to one of our training sessions..."
                    show s 1 u at fdis
                    s "\"What is it?\""
                    mc 1 t sigh2 "\"Err... it's nothing. Let's just go home already. It's getting kinda late...\""
                    show s 1 u sigh at fdis
                    s "\"You weren't fooling around with a new girlfriend, were you?\""
                    mc 1 t sigh2 "\"No, of course not. I wouldn't do something like that at school. What if I got caught?\""
                    jump day1_goinghomefinal
        "Go home.":
            $ tour_jun = False
            $ jun_met = False
            "As interesting as it might be, the only reason I'm not at practice right now is because I wanted to go home."
            "Staying for this would kind of defeat the purpose of leaving."
            stop music2 fadeout 8.0
            "I keep making my way down the stairs."
            "When I get to the first floor, I see someone standing at the entrance of the tennis/volleyball gym."
            mc 1 t curious "\"Is that...\""
            "I see Shoichi in front of the gym, fully dressed in his volleyball uniform, talking to someone."
            "Wait. Are they arguing?"
            "For some reason, I start feeling uneasy."
            "I decide to speed up so I can reach him faster."
            scene SGateE with fade
            play music2 "music/BGM/loop.ogg" fadein 8.0
            "I run my way down the last flight of stairs, trying to reach them before anything bad goes down."
            show s 1 v avoid at fdis, three
            show h 1 c at seven
            with dissolve
            "As I reach the door, I see the other guy, a wolf nearly as tall as Shoichi himself, holding Shoichi by his collar."
            "I immediately dash over, even though I know I probably couldn't take that guy on a fight."
            "He lifts his arm, ready to punch Shoichi in the face."
            "What strikes me as odd is that Shoichi is offering no resistance. He just stands there, looking down."
            "Before I even have time to think, I throw myself at that guys waist, knocking him down to the ground with the force of the impact."
            "He lets go of Shoichi in surprise, causing him to tumble backwards."
            show s 1 v shock at fdis
            s "\"[povFirstName]?!\""
            "I try getting up, but the wolf immediately grabs me by my neck and flips me around, pinning me beneath him in the floor."
            "He gets ready to punch me."
            "I reflexively hold my hands up to avoid getting hit in the face."
            hw "\"You?!\""
            "Before he can do anything, the wolf is quickly and easily lifted off of me."
            show s 2 v leer at fdis
            "Shoichi presses him up against the wall."
            "Shoichi snarls at the wolf, his expression so blank and devoid of emotion that looking at it makes me uncomfortable."
            "It's enough to make him shrink against the wall, though only slightly."
            show s 2 v rage at fdis
            s "\"Koizumi! You so much as touch him again and I'll beat the everliving crap out of you. Do you understand?!\""
            "The other guy looks away from Shoichi, setting his gaze on me."
            "Though I can't sense any of his earlier aggression, he just fixates his eyes on me."
            "It's unsettling."
            hw "\"Fine. Just let me go already.\""
            "He pushes against Shoichi's arms and Shoichi releases him."
            show h 1 c at offscreenleft with moveoledis
            show s 2 v rage at fdis, three with move
            "He dusts himself off and walks back into the gym building."
            stop music2 fadeout 6.0
            show s 2 v leer at fdis
            mc 1 t angry "\"What the hell was that?!\""
            "My voice comes out a little higher than I intended."
            show s 1 v frown at fdis
            "Shoichi looks me in the eye and I can tell he's angry."
            s "\"What the hell were you thinking? That guy is obviously so much stronger than you!\""
            mc 1 t angry "\"I was trying to help!\""
            show s 1 v scorn at fdis
            s "\"I didn't need any help!\""
            mc 1 t angry "\"He was going to punch your face!\""
            s "\"{size=+4}I know!{/size}\""
            show s 1 v sigh at fdis
            s "\"I know, okay? I was going to let him.\""
            "What?"
            "Don't get me wrong. I'm all for not getting involved in fights, but letting yourself get beat up doesn't sound like a better alternative."
            mc 1 t shock "\"You were going to let him punch you? Are you crazy? Did you hit your head?\""
            show s 1 v blank at fdis
            s "\"Quite the contrary. I hit him.\""
            "I take some time to wrap my head around what he just said."
            "Shoichi... hit him?"
            "As in... punched him?"
            mc 1 t fsmile "\"What do you mean \"I hit him.\"? That doesn't make any sense.\""
            show s 1 v wry at fdis
            s "\"It means exactly what I said. I lost control and I punched him in the face. Didn't you notice his nose bleeding? A few drops even fell on your face.\""
            "As he says it, I finally notice something dripping from my cheek. I touch my hand to it and it comes out red."
            "Blood."
            "I can't even understand what is going on."
            "Shoichi attacked someone? What for? I've never even seen him raise his voice before."
            mc 1 t shock "\"...Why?\""
            show s 1 v sad at fdis
            "Is the only thing I can even think of saying."
            "Shoichi's shoulders sag."
            "He looks me in the eye, opening his mouth many times, but words never coming out."
            "He swallows two, three times, before he finally speaks."
            s "\"I was asked to get him to see his assigned counselor. I was planning to talk to him today after practice but... he had a fight with coach.\""
            s "\"I got him outside so he wouldn't do anything stupid, the only problem was: he was so pissed that he just wanted to pick a fight.\""
            show s 1 v avoidb at fdis
            s "\"He started insulting me and, when I didn't care, he started insulting the other team members. Then he...\""
            "Shoichi stopped. His eyes that were previously unfocused finally seemed to acknowledge my presence."
            "He quickly looked away from me again."
            "I feel like he's hiding something from me."
            show s 1 v avoid at fdis
            s "\"Then I hit him.\""
            mc 1 t "\"You hit him for badmouthing your team?\""
            show s 1 v sad at fdis
            s "\"... Yes.\""
            "He's definitely hiding something."
            "I know he's protective of his team, but he's not the type of person who'd hit someone just for some insults."
            "Heck, he's not the type of person to hit someone for any reason."
            "He's certainly strong, but he's a pacifist at heart."
            "As I get ready to pry further, Shoichi gives me a quick tap on the shoulder."
            show s 1 v wince at fdis
            s "\"Can we just drop this for now? I feel like going home already.\""
            mc 1 t sad "\"Oh, okay. I'm actually on my way home now. We can go together.\""
            s "\"Sure. Just let me go change.\""
            show s 1 v wince at offscreenleft with moveoledis
            hide s 1 u wince
            "He goes inside the gym."
            "Right when I look away, I hear a \"psst\" coming from the door. Shoichi's head is peering through it."
            if povFirstName == "Yuuichi":
                s 1 v wry "\"By the way. Thanks, Yuu.\""
                "He turns around and goes inside."
                "I'm a little surprised. Shoichi never called me \"Yuu\" before."
                "Today has certainly been... interesting."
            else:
                s 1 v wry "\"By the way. Thanks, [povFirstName].\""
                "Shoichi quickly turns around and rushes inside."

            scene Street1E
            show s 1 u smile at fdis, five
            with fade
            play music "music/crowd01.ogg" fadein 6.0
            play music2 "music/BGM/Dog Days.ogg"
            show s 1 u happy at fdis
            s "\"-and scored the point just like that. I didn't know he had it in him!\""
            "Shoichi's mood vastly improved after we left the school."
            "Now he was happily discussing something that happened during practice."
            show s 1 u smile at fdis
            s "\"By the way. Didn't Aki-kun start at his new club today?\""
            mc 1 t smile "\"Yeah. He said he didn't want to join his school's tennis club because they don't make individual training regiments for their players.\""
            mc 1 t happy "\"Can you believe it? He's only twelve and he's already going around saying he'll become a pro player.\""
            show s 1 u wry at fdis
            s "\"Is that so surprising? I seem to remember a certain someone going on about becoming a pro by the time he was ten.\""
            mc 1 t think "\"Eh, maybe I'm being a little hypocritical. Still, I can't say I'm not happy to see how much he loves tennis.\""
            show s 1 u considerate at fdis
            s "\"Definitely. I'd be beyond myself if Hitoka decided to play volleyball, but she doesn't care about sports. It's depressing.\""
            mc 1 t sigh "\"Well, you can't just expect her to like everything you do. Plus, it's not like you're so dedicated to volleyball as to inspire her. You're going home one hour before the end of practice.\""
            show s 1 u seductive at fdis
            s "\"Says the guy that's coming with me.\""
            mc 1 t avoid "\"Ugh... point taken.\""
            scene Street2E
            show s 1 u smile at fdis, five
            with fade
            s "\"By the way, did you guys get the draw for the Saitama tournament?\""
            mc 1 t "\"Not yet. We're still two months away from the tournament.\""
            s "\"Yeah? We already got the draw for the Interhigh Prefecturals, though.\""
            mc 1 t sigh "\"Seriously? Shouldn't the Interhigh be later than the Kanto Tennis Tournament?\""
            show s 1 u happy at fdis
            s "\"It is, but they give us the draw four months in advance anyways. It's so we have time to study the other teams we might face.\""
            mc 1 t sigh "\"Since it's the draw for an individual tournament, the players themselves have to register, so they don't have a list of participants right at the beginning of the school year.\""
            show s 1 u shock at fdis
            s "\"Yeah, you're right.\""
            show s 1 u smile at fdis
            s "\"How do you feel about your odds this year?\""
            mc 1 t think "\"Hmm... that depends. The Saitama Junior should be easy. The level of the competition there isn't all that high, so I'll probably win again.\""
            show s 1 u happy at fdis
            s "\"For the third year in a row.\""
            "I smile."
            mc 1 t fsmile "\"I should also get second place at Kanto again this year.\""
            show s 1 u seductive at fdis
            s "\"Yeah. Not to mention mister number 1 wiped the floor with your face last year.\""
            mc 1 t sigh "\"Could we not mention that?\""
            show s 1 u happy at fdis
            s "\"Sure, whatever. Good for you, though. You might get to practice against him before the All-Japan.\""
            scene HouseFrontE
            show s 1 u smile at fdis, five
            with fade
            mc 1 t sigh "\"I've been getting \"practice\" against him since middle school and I still haven't won a single match.\""
            s "\"Don't be so pessimistic. You should think that this time is going to be different. If you go at it with the same mentality, how can you expect a different result?\""
            mc 1 t sigh "\"Says the guy that constantly goes around saying he won't even reach Nationals this year. That must do wonders for your team's morale.\""
            show s 1 u wince at fdis
            s "\"Guh... point.\""
            play sound "music/door.ogg"
            stop music fadeout 6.0
            scene HouseEntrance
            show s 1 u smile at fdis, five
            with fade
            mc 1 t smile "\"Want to come in?\""
            show s 1 u happy at fdis
            s "\"Sure. How about we play some games?\""
            mc 1 t smile "\"The usual?\""
            "By \"the usual\" we mean countless hours of Sidewalk Fighter and a lot of soda."
            s "\"Yep. Sounds good.\""
            show s 1 u think at fdis
            s "\"But you should probably get changed, first...\""
            mc 1 t shock "\"Ah, good point!\""
            "I'm still wearing my tennis clothes..."
            scene LivingRoomE
            show s 1 u smile at fdis, five
            with fade
            s "\"Which one of us is leading?\""
            mc 1 c smile "\"Me. 1308 to 1306.\""
            show s 1 u laugh at fdis
            s "\"You keep track of the weirdest things, you know.\""
            "I shrug, pressing the power button on the console and taking a seat next to him."
            show s 1 u shock at fdis
            s "\"Oh, you're smelling pretty good now that you've showered.\""
            show s 1 u laugh at fdis
            mc 1 t sigh "\"That's a weird thing to comment on...\""
            show s 1 u smile at fdis
            "We've both pretty much memorized each other's preferred strategies and character's combos, so there is a lot of waiting for someone to make a move and not a lot of actual moving."
            "Probably not how the game was meant to be played. Not that it matters anyway."
            stop music fadeout 4.0
            stop music2 fadeout 6.0
            play music "music/night.ogg" fadein 5.0
            scene LivingRoomN
            show s 1 u wince at fdis, five
            with fade
            s "\"Ah. I lost.\""
            mc 1 t cocky "\"1314 to 1310. The lead is widening!\""
            show s 1 u sigh at fdis
            s "\"Oh, shut up.\""
            play sound "music/lock.ogg"
            "I hear a clicking noise as the keys are turned."
            show a 1 t at fdis, ten with moveiridis
            "I look over my back and see my little brother coming in. As soon as he notices us, he looks surprised."
            a 1 t happy "\"Aniki?! You're home already?\""
            show s 1 u happy at fdis, three
            show a 1 t smile at fdis, eight
            with move
            mc 1 t smile "\"Yeah. I didn't stay for practice.\""
            a 1 t sigh "\"What? Shouldn't you be preparing for the next tournament?\""
            mc 1 t sigh "\"That's a ways away. And it's not like I have to worry about being beaten in the prefectural tournament.\""
            show s 1 u wry at fdis
            s "\"Urushihara would cry if he heard you saying that.\""
            "I pretend not to hear him. I'm good at that."
            mc 1 t happy "\"So, how's the new club?\""
            show a 1 t smile at fdis
            "Aki sets his bag next to ours and sits on the open space next to me. His tail occasionally hits mine with how much it's wagging."
            "He still hasn't learned to be conscious of his tail, it seems."
            a "\"It's good. They all take tennis way more seriously than the people at my school club.\""
            show s 1 u happy at fdis
            s "\"That's great. Maybe you'll finally find yourself a good rival.\""
            mc 1 t think "\"Really? I wouldn't count on it. I've never really had any rivals in my clubs.\""
            show s 1 u sigh at fdis
            s "\"Urushihara would cry if he heard you saying that too.\""
            "I shrug."
            show s 1 u smile at fdis
            s "\"Well, anyway. If Aki-kun is getting home, that must mean it's already late. I should be going.\""
            a 1 t worried2 "\"Already? Why don't you spend the night, Shoichi-nii? Isn't your dad out of town?\""
            show s 1 u happy at fdis
            s "\"He is, but I have some things I have to take care of before I go home. Sorry, Aki-kun, maybe next time.\""
            "Shoichi ruffles Aki's head and picks up his bag."
            a 1 t avoid "\"You better promise you'll stay next time.\""
            show a 1 t smile at fdis
            s "\"Cross my heart.\""
            mc 1 t curious "\"And hope to die?\""
            show s 1 u sigh at fdis
            play sound "music/punch.ogg"
            "Shoichi gives me a karate chop on the head."
            mc 1 t cshock "\"Ow!\"" with hpunch
            s "\"You're listening to too much rock. Start using that free time towards practice, would you.\""
            mc 1 t sigh "\"You're starting to sound like Saya.\""
            show s 1 u happy at fdis
            "Shoichi puts a finger to his lips and winks at me before quickly leaving."
            show s 1 u happy at fdis, offscreenright
            show a 1 t at fdis, fiveh
            with move
            hide s 1 u happy
            play sound "music/lock.ogg"
            "The door makes a quiet click as he goes out."
            a "\"By the way, Aniki. Mom called to say she wouldn't make it for dinner. She asked you to take care of it.\""
            mc 1 t smile "\"Ah, sure, Aki. I'll get right to it.\""
            a 1 t worried "\"Ehhh? There's no rush. Let's spend some time together. We rarely do that nowadays.\""
            "Aki shuffles around in his seat, laying his little head in my arm. He isn't quite tall enough to reach my shoulder."
            "Sometimes I'm a little freaked out to see a mini version of myself walking around the house."
            "Then I remember how much better behaved than me he is and am reminded that there is no way he is a \"little me\"."
            a 1 t happy "\"I actually have a favor to ask you.\""
            mc 1 t happy "\"Sure. What is it?\""
            a 1 t smile "\"My new club has a training program designed to groom prospective pro-players.\""
            mc 1 t smile "\"That's awesome, but what's the favor you want to ask?\""
            a 1 t avoidb "\"Well... when I got there today, the coach they assigned me to said I looked familiar. When he saw my name in the list he asked me \"[povLastName]? Are you related to {i}that{/i} [povLastName] by any chance?\".\""
            "Oh. That's right. The club Aki enrolled in has been trying to scout me out for the past five years."
            a 1 t blush2 "\"When I told him that my brother was {i}the{/i} [povName], he insisted you come over. Apparently they've invited a lot of hopefuls in Kanto over to inspire the new players. He said they sent you an invite too, but you never answered.\""
            "Really? I stopped opening the emails they sent me about two years ago, so I wouldn't really know."
            mc 1 t think "\"That sounds interesting. I guess I could go. When is it?\""
            a 1 t laughb "\"Really? Great. It's next week, on Sunday. Can you really come?\""
            "Even if I couldn't, his tail is wagging so much right now it could double for a feather-duster. There's no way I can say no after seeing him this excited."
            "Shoichi's always saying I'm too much of a doting brother. Is this what he means by that?"
            "But who could say no to such a lovely face? Surely it would be a crime!"
            mc 1 t happy "\"Yeah, yeah. I can come, Aki. Just remind me on Friday so I don't end up forgetting and scheduling some other plans.\""
            a 1 t happyb "\"Yay!\""
            "He immediately plopped down from the sofa, grabbed his school bag, and started running towards his room."
            a 1 t happyb "\"I'm going to tell my friends!\""
            mc 1 t sigh "\"Aki, don't run up the stairs!\""
            a 1 t laugh "\"Got it!\""
            show a 1 t laugh at offscreenleft with move
            "I actually heard him trip over the stairs, but since he didn't fall down and hurt himself I guess I can let it slide."
            scene BedroomN with fade
            "Ah, I ate well."
            "I'm actually surprised with how energetic Aki was during dinner. He couldn't stop talking about how excited his friends were to have me come over."
            "One of these days I'm gonna have to tell him to stop using me to make his tennis buddies jealous."
            play sound "music/message.ogg"
            "Ah, my phone's buzzing."
            show ph with dissolve
            show sac
            show sa1 at Position(xpos=506, ypos=162, xanchor=0, yanchor=0)
            show sa2 at Position(xpos=506, ypos=232, xanchor=0, yanchor=0)
            "Coach did? Wow. I haven't seen him for almost a month now."
            show asaalt1 at Position(xpos=574, ypos=282, xanchor=0, yanchor=0) with dissolve
            $ renpy.pause(1.0)
            play sound "music/message.ogg"
            show sa3alt at Position(xpos=506, ypos=332, xanchor=0, yanchor=0) with dissolve
            $ renpy.pause(1.0)
            show asaalt2 at Position(xpos=574, ypos=382, xanchor=0, yanchor=0) with dissolve
            "I know it's not good to have a consistently bad opinion of someone, but..."
            "He's the kind of guy you expect nothing from and still end up disappointed."
            "Though I do have the habit of having the things I say blowing up in my face, so I'll just stay quiet on this one."
            play sound "music/message.ogg"
            show sa4alt at Position(xpos=506, ypos=432, xanchor=0, yanchor=0) with dissolve
            $ renpy.pause(0.5)
            show asa2 at Position(xpos=730, ypos=482, xanchor=0, yanchor=0) with dissolve
            $ renpy.pause(0.5)
            "Well... it's already pretty late. I might as well turn in."
            stop music
            $ date = None
            jump day2
