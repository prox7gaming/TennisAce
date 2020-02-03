label Day5_Jun:
    scene Street2
    show j 1 u avoid at fdis, five
    with fade
    play music2 "music/BGM/Husigityan O-Ra.ogg"
    "We take a long walk filled with awkward silence."
    "I guess Jun's enthusiasm died again when he noticed we were walking home alone."
    "My uncalled for touching probably freaked him out a bit."
    "God, am I turning into Shoichi?"
    scene JunHouse
    show j 1 u at fdis, five
    with fade
    "We finally arrive at what I assume is his place."
    "It's a lot... different from what I expected."
    "The house itself is a little smaller than all the others around."
    "And the entire exterior is made of what is seemingly old wood."
    "It gives me an impression that this isn't the most stable of houses..."
    "I know this neighborhood isn't very new. Most of the houses here have been renovated and had their exteriors redone."
    "As it stands right now, Jun's house is probably the oldest in the street."
    "Jun unlocks the door and opens it."
    show j 1 u considerate at fdis
    j "\"Please come in.\""
    stop music2 fadeout 2.0
    play music3 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    scene JunLivingRoom with fade
    "The first thing I notice when I walk in is how organized the whole place in."
    "It's completely spotless. Everything looks like it's been meticulously organized and there's not a speck of dust anywhere."
    show j 1 u considerate at fdis, five
    j "\"Sorry about the mess. Please, feel right at home.\""
    mc 1 u wince "\"You call this a mess? You wouldn't even consider my house to be livable, then.\""
    show j 1 u watch at fdis
    j "\"Hmm? How would that be possible? You live there, don't you?.\""
    mc 1 u shock "\"What? Yes, I live there, but-\""
    "He shoots me a quizzical look."
    play sound "music/disappointment.ogg"
    "The joke's gone completely over his head..."
    "Jun takes off his shoes and lays them down in a small shoe cabinet next to the door. I decide to imitate him."
    "I know it's not polite to pry, but I walk around the living room, looking over the whole place in complete awe.\""
    "Even if the outside looks a bit old, the inside is actually quite cozy."
    "This is a nice place!"
    "Ah, I see a piano in the far corner of it. Is that what he uses to practice?"
    mc 1 u think "\"I thought you'd have a soundproof room for it.\""
    j "\"Hmm?\""
    "He follows my gaze and his eyes soon come to rest on the piano."
    show j 1 u happy at fdis
    "Just looking at the piano already has his expression soften. As if just being near it was enough to make him relax."
    show j 1 u wry at fdis
    j "\"We don't really have any rooms in the house that we could convert into a soundproof room. {size=-2}Also, soundproofing is kinda expensive.{/size}\""
    "Is it? I had no idea."
    show j 1 u happy at fdis
    "Jun gently strokes the keys of his piano, looking down at them with visible affection."
    "He must be exercising every ounce of self-control he has to keep himself from sitting down and playing it."
    "... I should probably keep him distracted from it."
    show j 1 u shock at fdis
    mc 1 u think "\"You said you already played all the games you had. Can I see your gaming console?\""
    "Well, I seem to have snapped him back to reality."
    show j 1 u watch at fdis
    j "\"It's in my room though. Follow me.\""
    "He guides me through a tight corridor, leading to a single door."
    "So his bedroom is on the first floor?"
    show j 1 u shock at fdis
    j "\"Oh, wait.{nw}"
    show j 1 u considerate at fdis
    extend " Could you wait out here for a bit while I get changed? I don't like wearing the uniform for too long. {size=-4}It's kinda tight.{/size}\""
    mc 1 u shock "\"Oh, sure.\""
    mc 1 u smile "\"Actually, if you don't mind, could I use your bathroom and get changed too? Since you're gonna do it then I might as well too.\""
    show j 1 u smile at fdis
    j "\"Sure. It's right around that door.\""
    "He points down the hall to a wooden door with the letters \"W.C.\" glued to it."
    mc 1 u "\"WC?\""
    show j 1 u watch at fdis
    j "\"It's something my mom put there. It's supposed to mean something but I have no idea what. She thought it would look nice.\""
    show j 1 u happy at fdis
    j "\"Anyway, I'm gonna get changed. Be back in a bit.\""
    mc 1 u smile "\"Alright.\""
    scene JunBedroom
    show j 1 c watch at fdis, five
    with fade
    "Once we walk in, Jun flicks the light switch on, revealing a small, albeit neatly organized, bedroom."
    "A simple bed was pushed up against the far wall. There were also a few bookshelves with books and a little table with a small TV on top of it."
    "He also had an old, ratty-looking wooden closet right next to the door."
    mc 1 c shock "\"Wow, I didn't expect your room to be so organized!\""
    show j 1 c think at fdis
    j "\"Yeah. We don't have much space so we have to organize as best as we can to make everything fit.\""
    mc 1 c shock "\"Well, you're definitely doing a good job of it. My room isn't nearly as organized... and I'm not a messy person.\""
    show j 1 c gentle at fdis
    "Jun giggles. His voice as he laughs if bright and full of energy."
    "At least I don't have to worry about him being too down after what happened at the doctor's office."
    "Plus, it's funny seeing his whiskers twitching as he laughs."
    show j 1 c happy at fdis
    j "\"It's just a matter of getting used to it."
    show j 1 c think at fdis
    extend " After doing it for years, I feel uneasy if my room gets messy.\""
    show j 1 c watch at fdis
    mc 1 c considerate "\"You {i}definitely{/i} shouldn't come to my house then. The mess would probably give you a heart attack.\""
    show j 1 c considerate at fdis
    j "\"Of all the things likely to give me a heart attack, I don't think a messy house is going to be one of them.\""
    mc 1 c happy "\"Point taken.\""
    mc 1 c smile "\"So, where's your gaming system?\""
    show j 1 c think at fdis
    j "\"Ah, right. Just a second.\""
    "He walks up to his closet, opening one of the small doors on the top part."
    "... No matter how I look at it, he's too small to reach inside."
    show j 1 c wince at fdis
    "He's stretching and standing up on the tip of his toes to reach."
    play sound "music/disappointment.ogg"
    "Wouldn't it be easier to grab a chair?"
    menu:
        "Help him.":
            "I'm afraid he might hurt himself if he keeps doing this."
            "You could say that reaching into a closet is a very mundane activity and there's no way someone could mess it up, but..."
            "I've seen what kind of disasters can happen when he's involved."
            "I'm sure something ridiculous and possibly dangerous could happen so I prefer not to take the risk."
            mc 1 c "\"Let me.\""
            show j 1 c shock at fdis
            $ renpy.pause (1.0)
            show j 1 c watch at fdis, three with move
            "He nods, walking away to give me space to reach into the closet."
            "I also have to stand on the tip of my toes, but I'm actually capable of looking inside the closet and seeing what's in it."
            "Ah, I can see the console in the back of the closet, next to a pile of old CDs."
            "I grab it and proceed to pull it out, but I can feel as if I'm tugging something that's become stuck."
            "The console only moves a little and then it refuses to move anymore... is one of the cables stuck?"
            menu:
                "Pull harder.":
                    $ head = True
                    "Without even giving it a second thought, I decide to pull the console even harder."
                    show j 1 c wince at fdis
                    j "\"Ah, be caref-\""
                    stop music3 fadeout 2.5
                    play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
                    show j 1 c cshock at fdis
                    play sound "music/crash.ogg"
                    "OW!" with hpunch
                    "Without warning, a pile of CD cases comes flying out of the closet, hitting me on the head a bunch of times and falling to the floor."
                    show j 1 c cshock at fdis, shake1
                    j "\"Ahhhh, my CDs!\""
                    mc 1 c annoyed "\"I think my head is more important than the CDs! Son of a- Ow!\""
                    "I think a few of the CD cases fell corner-first on my head."
                    "I reach for it and immediately feel a sting upon touching it."
                    "I bring my fingers back to eye level and, sure enough, I see blood."
                    mc 1 c wince "\"Oh, this isn't good...\""
                    show j 1 c cshock at fdis, shake1
                    j "\"Ahhhh, you're bleeding!\""
                    mc 1 c wince "\"Yeah, could you-\""
                    show j 1 c cshock at fdis, shake1
                    j "\"Ahhh!\""
                    "He flips out completely, running around the room, randomly opening drawers and throwing their contents out as he desperately looks for... something."
                    mc 1 c sigh "\"Just calm do-\""
                    show j 1 c cshock at fdis, shake1
                    j "\"Ahhh, where's the gauze? Where's the first aid kit?! Whe-\""
                    show j 1 c shockb at fdis, shake1
                    "I grab his muzzle with my hand and force it closed, forcefully moving his head so he's looking at me."
                    mc 1 c annoyed "\"Calm down first, look for it after!\""
                    "Once he takes a deep breath and nods, I let go of him."
                    show j 1 c blush at fdis
                    j "\"Sorry.\""
                    stop music2 fadeout 5.0
                    show j 1 c blush at offscreenleft with moveoledis
                    "He scurries out of the room."
                    "Man, this thing stings like hell."
                    "I can feel the warmth of the blood oozing out of the wound."
                    "This is definitely going to be sore tomorrow..."
                    "Jun is away for a couple of minutes. I try to focus on anything but the feeling of something warm running down my head."
                    show j 1 c wince at fdis, five with moveiledis
                    j "\"I brought something to clean the wound. Sit still and hold down!\""
                    "\"Sit still and hold down\"? Here's someone who certainly isn't going to become a famous author any time soon..."
                    show cg6_pan with dissolve:
                        subpixel True
                        yalign 1.0
                        linear 0.7
                        linear 12.0 yalign 0.05
                    play music3 "music/BGM/I Want to Know You - Narration.ogg" fadein 5.0
                    "I decide not to make a fuss."
                    "While I'm a bit worried over having someone like him dressing my wound, I decide to just be a good patient."
                    "Jun sits down on the edge of his bed and asks me to sit on the floor between his legs."
                    "Ah, I see. This way he has easy access to the top of my head."
                    "I do as he says, leaning close until I can feel some of my fur grazing his stomach."
                    "He's very warm."
                    "I'm surprised with how gentle he is..."
                    show cg6_tail2
                    show cg6_jsmile
                    show cg6_mcwince
                    with dissolve
                    show j 1 c zero at fdis
                    j "\"Ah, here. I'm gonna use this now.\""
                    "He makes sure to show me everything that he's using before he actually uses it."
                    "I never stopped to think about it before, but knowing exactly what he's doing as he does it helps keep me relaxed."
                    "Not only that, his touch is so fleeting and soft... I can barely feel anything, let alone pain."
                    "In fact... even as I'm aware that I have a cut somewhere on my head, all that I can feel is a pleasant, caressing touch."
                    show cg6_jconsiderate at fdis
                    show cg6_mcwince at fdis
                    j "\"Oh man, there was so much blood that I thought this would be a more serious wound but this doesn't look bad at all. I'm really glad.\""
                    hide cg6_jsmile
                    show cg6_jsmile at fdis
                    j "\"I guess head wounds just bleed a lot, even if they're pretty minor.\""
                    hide cg6_jthink
                    hide cg6_mcthink
                    show cg6_jthink at fdis
                    show cg6_mcthink at fdis
                    mc 1 c zero "\"The head has a lot more blood vessels than most parts of the body, so there's just more blood to seep out. It doesn't necessarily mean that it's a deep wound..\""
                    hide cg6_jhappy
                    hide cg6_mcsmile
                    show cg6_jhappy at fdis
                    show cg6_mcsmile at fdis
                    j "\"Oh, really? I didn't know that. I'm relieved.\""
                    hide cg6_jshockb
                    hide cg6_mcshock
                    show cg6_jshockb at fdis
                    show cg6_mcshock at fdis
                    j "\"Oh...\""
                    "I hear a light gasp coming from him."
                    hide cg6_jshock at fdis
                    hide cg6_mcwince
                    show cg6_jshock at fdis
                    show cg6_mcwince at fdis
                    mc 1 c zero "\"I-Is there something wrong with my head?\""
                    j "\"What?"
                    hide cg6_jconsiderate
                    show cg6_jconsiderate at fdis
                    extend " Ah, no no. It's just..."
                    hide cg6_jthink at fdis
                    hide cg6_mcshock
                    show cg6_jthink at fdis
                    show cg6_mcshock at fdis
                    extend " Your tail is pretty lively.\""
                    mc 1 c zero "\"Huh?\""
                    "As soon as I become conscious of it, I realize I had been vigorously wagging my tail the whole time."
                    "Not only that, it's been brushing up against Jun's legs the whole time."
                    hide cg6_mcavoidb
                    show cg6_mcavoidb at fdis
                    mc 1 c zero "\"Oh God, I'm sorry.\""
                    hide cg6_jconsiderate
                    show cg6_jconsiderate at fdis
                    j "\"Don't worry about it. It's no big deal.\""
                    "Even if he says so, this is so embarrassing..."
                    "I'm glad he can't see how red my face is right now..."
                    hide cg6_jhappy
                    show cg6_jhappy at fdis
                    j "\"Hehe, it's really soft.\""
                    show cg6_tail at fdis
                    hide cg6_mcthink
                    show cg6_mcthink at fdis
                    "I feel something soft draping over my shoulder."
                    "I reach with my hand since I'm not allowed to move at the moment."
                    hide cg6_jhappyb
                    show cg6_jhappyb at fdis
                    "It's... really soft and... furry?"
                    "Is this... his tail?"
                    "Jun giggles under his breath."
                    j "\"There. Mine's touching you too now. You don't have to be embarrassed.\""
                    "B-but the touching isn't what had me embarrassed!"
                    "... Well, I'll just take this to mean that he doesn't even register my tail wagging as something to be embarrassed about."
                    hide cg6_jwatch
                    hide cg6_mchappy
                    show cg6_jwatch at fdis
                    show cg6_mchappy at fdis
                    mc 1 c zero "\"Thanks, Jun.\""
                    j "\"Hmm? For what?\""
                    hide cg6_mcsmile
                    show cg6_mcsmile at fdis
                    mc 1 c zero "\"For taking care of me. Even though I did this to myself... and kinda wrecked your CDs in the process.\""
                    hide cg6_jhappy
                    show cg6_jhappy at fdis
                    j "\"It's fine. The CDs are just things. I can replace them if any of them broke. I'm just glad you're okay.\""
                    hide cg6_mchappyb
                    show cg6_mchappyb at fdis
                    "Heh... he's really warm..."
                    "Although this time I'm not talking about his body."
                    "He's just such a warm person."
                    hide cg6_jhappyb
                    show cg6_jhappyb at fdis
                    j "\"I have to say I'm surprised. Your fur is really soft, [povFirstName]-san. I'm kinda jealous.\""
                    hide cg6_mcwince
                    show cg6_mcwince at fdis
                    mc 1 c zero "\"It's not all roses. It takes quite a bit of brushing in the morning to keep it from looking like a mess.\""
                    hide cg6_jthink
                    show cg6_jthink at fdis
                    j "\"Oh, I hadn't thought of that."
                    hide cg6_jhappy
                    show cg6_jhappy at fdis
                    extend " I guess I'm fine with my own, then.\""
                    hide cg6_mchappy
                    show cg6_mchappy at fdis
                    mc 1 c zero "\"Hehe. It's not as if your fur weren't soft enough already.\""
                    hide cg6_mchappyb
                    show cg6_mchappyb at fdis
                    "I give his tail a gentle squeeze, petting it a few times."
                    hide cg6_jhappyb
                    show cg6_jhappyb at fdis
                    j "\"Hehehe. Thank you. I actually use a special shampoo for tiger fur.\""
                    hide cg6_jconsiderate
                    show cg6_jconsiderate at fdis
                    j "\"My parents tell me I worry too much, but I kinda got used to always wanting to look my best.\""
                    j "\"Although I guess I've really let myself go in recent years... what with all this extra weight.\""
                    hide cg6_mcthink
                    show cg6_mcthink at fdis
                    mc 1 c zero "\"You weren't always like this?\""
                    hide cg6_mcsmile
                    hide cg6_jsmile
                    show cg6_mcsmile at fdis
                    show cg6_jsmile at fdis
                    j "\"Nah. I used to be pretty fit.{nw}"
                    hide cg6_jconsiderate
                    show cg6_jconsiderate at fdis
                    extend " Although I guess compared to someone like you, I was just thin.\""
                    j "\"I didn't start gaining this extra weight until a few years ago. I really should be more careful with my body, huh...\""
                    j "\"Even though it's been years since I quit performing, I've always taken good care of my fur. Although I do wish it could be shinier and silkier.\""
                    hide cg6_jsmile
                    show cg6_jsmile at fdis
                    j "\"... I'm sounding like a girl, aren't I?\""
                    hide cg6_mchappy
                    show cg6_mchappy at fdis
                    mc 1 c zero "\"A little bit. It's fine though.\""
                    hide cg6_jwatch
                    hide cg6_mcthink
                    show cg6_mcthink at fdis
                    show cg6_jwatch at fdis
                    mc 1 c zero "\"I never really thought much about it. I just keep my fur trimmed so it won't get in my way... but I'm also lazy about it so I let it grow until I can't anymore.\""
                    hide cg6_mcsmile
                    show cg6_mcsmile at fdis
                    mc 1 c zero "\"But being a tennis player, I never really had to worry about my looks.\""
                    hide cg6_mcthink
                    show cg6_mcthink at fdis
                    mc 1 c zero "\"Was it really that big of a deal for you?\""
                    hide cg6_jconsiderate
                    show cg6_jconsiderate at fdis
                    j "\"Kinda. The judges at the competition were always more worried about the music, of course. But they also paid attention to other things.\""
                    hide cg6_jwatch
                    show cg6_jwatch at fdis
                    j "\"To be a performer, you really need to pay attention to detail. Classical music is still considered in many circles to be a high class hobby.\""
                    hide cg6_jconsiderate
                    show cg6_jconsiderate at fdis
                    j "\"So the way you dress, the way you talk, the way you carry yourself. They would judge you based on all of these things.\""
                    j "\"Eventually, it just became second nature for me to take care of my looks. Brushing my fur, using special shampoos, eating healthy foods. I got used to all of that.\""
                    hide cg6_jthink
                    show cg6_jthink at fdis
                    j "\"Although I guess I did fall into the junk food habit after I stopped competing.\""
                    hide cg6_mcwince
                    show cg6_mcwince at fdis
                    "Wow. I never knew all these things were important for someone like him."
                    "This is the kind of thing I never would have guessed if I were just a spectator looking from the outside..."
                    hide cg6_jhappyb
                    show cg6_jhappyb at fdis
                    hide cg6_mcsmile
                    show cg6_mcsmile at fdis
                    "I feel a soft touch against the back of my neck."
                    "My fur immediately stands at attention, but I quickly relax once I realize that it's just his hand."
                    "Jun is slowly and gently petting my neck. Always with the utmost care, almost like he's caressing a small child."
                    show cg6_1 at offscreenleft
                    show cg6_2 at offscreenleft
                    show cg6_3 at offscreenleft
                    show cg6_4 at offscreenleft
                    show cg6_5 at offscreenleft
                    show cg6_6 at offscreenleft
                    show cg6_7 at offscreenleft
                    show cg6_8 at offscreenleft
                    scene JunBedroom
                    show j 1 c smile at fdis, five
                    with dissolve
                    j "\"There. I'm all done. I put a little gauze on it. You don't have to keep it there for long, you can take it off before you go home if you want.\""
                    show j 1 c considerate at fdis
                    j "\"You were a pretty good patient. Usually when I'd hurt myself, I always cause a fuss when my parents tried to treat me.\""
                    show j 1 c smile at fdis
                    j "\"Would you like to lie down for a bit and relax?\""
                    mc 1 c happy "\"Nah, I'll be fine.\""
                    "I have to admit... this is already plenty relaxing on its own."
                    "I lean my head a little further back, resting it against Jun's stomach."
                    "He moves his hand from the back of my neck to the sides, continuing to pet me there."
                    "Oh man, his stomach is so soft and warm too... I could seriously fall asleep like this."
                    show j 1 c happyb at fdis
                    j "\"Are you sure about that? Because you already seem to be falling asleep right where you are.\""
                    mc 1 c happy "\"Mhm.\""
                    "His belly rumbles for a bit as he laughs, echoing a soft chuckle."
                    show j 1 c smile at fdis
                    stop music3 fadeout 5.0
                    j "\"Come on, sleepy head. If you want to stay awake then you should probably get up now.\""
                    mc 1 c wince "\"Aww, five more minutes!\""
                    show j 1 c considerate at fdis
                    j "\"I'm not your mom, you know.\""
                    show j 1 c think at fdis
                    play music3 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
                    j "\"Oh yeah, we should probably clean up the CD mess there.\""
                    mc 1 c think "\"Right... I honestly forgot about that.\""
                    show j 1 c happy at fdis
                    j "\"Since you've already got the console down, we might as well play something, right?"
                    show j 1 c think at fdis
                    extend " Oh, wait, I don't have any two-player games.\""
                    mc 1 c happy "\"I'm fine just watching you play something.\""
                    show j 1 c watch at fdis
                    j "\"Really? Because I'd be fine just watching you play something too.\""
                    mc 1 c smile "\"How about we decide on a game first, then we'll see who gets to play.\""
                    show j 1 c happy at fdis
                    j "\"Okay!\""
                    mc 1 c happy "\"Why don't you go ahead and choose something then?\""
                "Try to release it.":
                    mc 1 c think "\"Can you hold the console for a second? I think one of the cables is stuck.\""
                    show j 1 c shock at fdis
                    j "\"O-okay.\""
                    show j 1 c wince at fdis, five with move
                    "He tiptoes around me to hold the console out of the closet without it falling to the floor while I work on the cable."
                    "I can feel his body pressing against my sides but I don't let it distract me."
                    "It takes a bit of feeling around inside it but I eventually manage to grab hold of the cable."
                    mc 1 c wince "\"Huh... it seems to be stuck under a pile of... cases?\""
                    show j 1 c watch at fdis
                    j "\"Oh, those are the games.\""
                    mc 1 c think "\"Alright, I'll try to push them away. Right now the pile's on top of the cable and I can't pull it out without knocking everything down.\""
                    "I have to tip-toe to try and get good leverage but, after a light bit of pushing and some light tugging, I manage to free up the head of the cable that was stuck between the CDs and the closet's back."
                    mc 1 c smile "\"Got it. You can get the video game down now.\""
                    "Jun lowers the console and gets to work on plugging it in."
                    show j 1 c smile at fdis
                    j "\"[povFirstName]-san, if you don't mind, could you get the games for me too?\""
                    mc 1 c smile "\"Sure.\""
                    "I grab hold of a moderately-sized pile of CD cases and plop it down on the desk, next to the console."
                    j "\"Okay, good. Why don't you pick something you want to play? I don't have anything for two-players, though.\""
                    mc 1 c smile "\"It's fine...\""
        "Just watch.":
            "I decide to keep myself out of this."
            "Knowing Jun, I can definitely imagine this scenario ending in disaster."
            "In that case, I'd rather be as far away as possible."
            "After a light bit of tip-toeing, Jun finally manages to take hold of the console, pulling it out of the closet."
            "Then I watch the chaos unfold."
            "A cable gets stuck somewhere inside the closet."
            stop music3 fadeout 2.5
            play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
            show j 1 c cshock at fdis, shake1
            "Jun tugs hard at it, causing a pile of CD cases next to it to fly out of the closet with it."
            j "\"Whaa-\"" with hpunch
            play sound "music/crash.ogg"
            play sound2 "music/fall.ogg"
            show j 1 c cshock at fdis, rotation, fall
            "Jun falls to the floor, a pile of CDs falling on top of him."
            mc 1 c sigh "\"Jesus, Jun, are you alright?\""
            show j 1 c wince at fdis, five, shake2, getup
            j "\"Ow... I think I fell on my ass...\""
            mc 1 c "\"You didn't hurt anything did you? Come on, let me help you up.\""
            play sound "music/tap.ogg"
            show j 1 c at fdis:
                linear 1.0 yoffset 194
            "He takes my hand and I help prop him up."
            stop music2 fadeout 2.5
            play music3 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
            j "\"I don't think so. My ass hurts a bit, but other than that I'm fine.\""
            show j 1 c cshock at fdis
            hide j 1 c cshock
            show j 1 c cshock at five
            show j 1 c cshock at fdis
            j "\"Ahh, my games! My console!\""
            play sound "music/disappointment.ogg"
            "Shouln't you check to see if {i}you{/i} have any injuries first?\""
            show j 1 c wince at fdis
            j "\"It... it doesn't look broken. I'll plug it in and see if it still works.\""
            mc 1 c sigh "\"At least check if you're not hurt first!\""
            j "\"I'm fine. If I were hurt, I'd know it.\""
            "I swear to God, I want to conk him in the head sometimes."
            show j 1 c smile at fdis
            j "\"Ah, it still boots up okay. Everything is fine.\""
            show j 1 c happy at fdis
            j "\"Why don't you choose something you want to play? I don't have any two-player games anyway.\""
            "Are we just pretending that that whole scene never happened?\""
            j "\"Err... you'll have to pick up the games from the floor first.\""
            "Yep, we are."
            show j 1 c watch at fdis
            mc 1 c "\"It's your console. I think you should be the one to play it.\""
    show j 1 c happy at fdis
    j "\"Nah, I've already played all these games over and over. You play and I'll watch. I'm sure it'll be more fun that way.\""
    "He starts fiddling with the console, double-checking that everything is in order and working properly."
    show j 1 c smile at fdis
    j "\"Why don't you pick something you like? Don't expect anything grand, though. My console is super old.\""
    "I take a closer look at it and, true enough, I recognize it."
    "It's a RubyOne. This thing went out of production almost ten years ago."
    mc 1 c smile "\"I had one of these as a kid. I have many fond memories of its games.\""
    show j 1 c happy at fdis
    j "\"Yeah. I like it a lot too."
    show j 1 c think at fdis
    extend " Haven't played in a while though. I wouldn't mind getting an upgrade.\""
    mc 1 c "\"Why don't you, then?\""
    show j 1 c wince at fdis
    "Even before I could see the look on his face, I already knew I made a mistake."
    show j 1 c wry at fdis
    j "\"We don't have the money for it. My parents are already working two jobs just to pay my m... some personal bills I've piled onto them the past few years.\""
    show j 1 c considerate at fdis
    j "\"I know they'd give me anything I asked, and that's exactly the problem. I don't want them to put themselves through tough times just to get me things.\""
    mc 1 c wince "\"That's... very mature of you, Jun. Not many guys your age are capable of thinking about others like that. It's good that you're so considerate to them.\""
    show j 1 c think at fdis
    j "\"Guys my age? How old do you think I am?\""
    mc 1 c wince "\"Uhh... fifteen... sixteen?\""
    show j 1 c watch at fdis
    "He stares quizzically at me, blinking a couple of times."
    j "\"Why?\""
    mc 1 c wince "\"Uhh...\""
    "... How do I answer that question without hurting his feelings?"
    mc 1 c fsmile "\"I-It's just a hunch I had.\""
    "Jun shakes his head in negative."
    j "\"I'm nineteen.\""
    mc 1 c shock "\"Huh? Nineteen?\""
    "He's older than me? No way!"
    mc 1 c shock "\"H-how can you be nineteen? You're still in High School!\""
    show j 1 c think at fdis
    j "\"And yet, you're perfectly fine with the idea of a fifteen-year old being a senior?\""
    mc 1 c wince "\"W-well...\""
    "It's true that it wouldn't make much sense."
    mc 1 c curious "\"Did you flunk a year then?\""
    show j 1 c shock at fdis, jumping
    $ renpy.pause(1.)
    show j 1 c considerate at fdis
    j "\"W-Well... there were a few personal circumstances last year that forced me to take the year off.\""
    mc 1 c shock "\"Oh no. Did you get sick or something like that?\""
    j "\"Yeah... something like that.\""
    "I try saying something else but he picks one game from the pile and quickly puts it in the console."
    show j 1 c wry at fdis
    j "\"Here, try this one.\""
    "I see the console logo flashing onto the screen as the system whirs itself into life."
    "Jun hands me a controller and sits on the bed, facing the TV."
    "I take a seat on the bed and grab the controller."
    "Since the bed isn't particularly spacious, I'm pressed up against him."
    "It's not uncomfortable at all though."
    "I see the games logo popping up on the screen and immediately recognize it."
    mc 1 c smile "\"Oh, I know this one. I'm a huge fan of the series.\""
    show j 1 c gentle at fdis
    "Jun immediately turns over towards me."
    "The move is so sudden that I nearly jump back, I am only stopped by the wall, that gently conks me in the head again."
    j "\"Really? I love this series, it's my favorite!\""
    "His eyes are almost sparkling with unbridled excitement."
    mc 1 c fsmile "\"Uuuhh... yeah. I have all the new ones at home.\""
    show j 1 c watch at fdis
    j "\"Y-You do? Ahhh...\""
    show j 1 c wince at fdis
    "He starts doing a few breathing exercises. He's looking like a kid trying hard not to throw a tantrum about something they really want."
    mc 1 c smile "\"Uuh... I can have you over sometime so you can play them. Actually, scratch that, I'll lend you my console.\""
    j "\"A-Are you sure? What if I break it?\""
    mc 1 c smile "\"Looking at how neatly your room is organized makes me doubt you might somehow break something on accident.\""
    show j 1 c smile at fdis
    j "\"O-okay. If you're sure.\""
    "Even though he's trying to act modest about it, I can see his eyes glinting with excitement."
    "Hehe, I won't lie. It makes me feel pretty good seeing how genuinely excited I can get him."
    mc 1 c smile "\"I'm sure. I barely play on my own anyway. You can come to my house to pick it up at any time.\""
    show j 1 c gentle at fdis
    j "\"Okay. Thanks!\""
    show j 1 c watch at fdis
    "With all that said, I choose to start a new game, careful not to overwrite his save files (he has so many!) and start playing."
    "It's fun how Jun watches so attentively. He avoids making comments on what I'm doing and just seems to genuinely enjoy watching me play."
    "It's also one of the rare occasions where he actually goes quiet (without things immediately turning awkward, I mean)."
    mc 1 c smile "\"I'm surprised you play these kinds of games, Jun.\""
    show j 1 c think at fdis
    j "\"How so?\""
    mc 1 c "\"Well, it's just that they're very story-heavy. If you don't pay attention to what's going on, you'll get totally lost. Especially with the older ones.\""
    j "\"Hmm... I never really considered that. I do love these games, though. They made me want to become a music composer for a game company when I grow up.\""
    mc 1 c shock "\"A... composer? I thought you wanted to become a pianist.\""
    show j 1 c wry at fdis
    "He looks away from me."
    j "\"I did... when I was a little younger. But I'm just not suited for that kind of life. After I realized that, I was depressed for a while. I started binging games and I avoided the piano.\""
    show j 1 c considerate at fdis
    j "\"But these games and these songs helped cheer me up. I want to be a composer so I can be involved in games that can cheer people up just like they did with me.\""
    mc 1 c shock "\"W-wow... that's pretty thoughtful coming from you. I never considered you the type to think too deeply about your future.\""
    show j 1 c wry at fdis
    j "\"I try not to. I'm not sure what's going to happen to me down the line, it's really scary."
    show j 1 c considerate at fdis
    j "\"But you also can't run away from it forever. I may not be able to become a pianist anymore, but I've found something else I want to do with my life. I'm happy with that.\""
    mc 1 c smile "\"I'm glad you think this way. I'm still surprised, though.\""
    show j 1 c wry at fdis
    j "\"Hehe, it's okay. I've had a long time to think about it, too.\""
    show j 1 c watch at fdis
    "Immediately after saying that, he turns his eyes back to the screen and completely zones me out."
    "... I don't know if I should consider this as having extreme focus or having no focus at all..."
    "Both are troublesome."
    scene JunBedroom
    show j 1 c watch at fdis, five
    with fade
    "It's been so long since I've had this much fun playing an old game."
    "I lose myself down a nostalgia trip, looking at all these characters and maps that I used to love. Finding secrets that I used to know as a kid."
    "This game reminds me why I used to love videogames so much as a kid."
    "I completely lose track of time as we continue to play."
    play sound "music/knock.ogg"
    "?" "\"Jun, sweetie, are you there?\""
    "I hear a female voice coming from the other side of the door."
    "Is this... his mother?"
    show j 1 c think at fdis
    j "\"Ah, yeah, just a sec. I have a friend over.\""
    "?" "\"A friend?\""
    play sound "music/door2.ogg"
    "As soon as Jun opens the door, I stand up to properly greet whoever's on the other side."
    "Somehow I don't think she'd like to see a strange person, even if it's a guy, sprawled over her son's bed when she knows her son had been there just a few moments ago..."
    show j 1 c watch at fdis, three with move
    show yui 1 c smile at fdis, seven with moveiridis
    "I'm greeted to the sight of a big, plump tigress with soft, gentle eyes."
    "As soon as she locks eyes with me, she smiles."
    "?" "\"Oh, hello there. I'm Jun's mother, Yui Kobayashi, it's a pleasure to meet you.\""
    "I bow to her."
    mc 1 c smile "\"I'm [povName]. It's a pleasure to meet you, ma'am.\""
    "When I look up, I see her fawning at me."
    yui "\"Oh, and you're so polite too! You must be the tennis player Jun talked about, then?\""
    show j 1 c wince at fdis, jumping
    j "\"Wait, M-Mom!\""
    "Huh... he's been talking about me to his parents? {i}And{/i} her mentioning it made him jump?"
    yui "Oh, don't be such a stick in the mud, sweetie. He looks so nice. My husband is a big fan of tennis, too. I'm sure he'd love to meet you. Why don't you join us for dinner?\""
    show j 1 c shock at fdis
    j "\"W-wait, Mom!\""
    stop music3 fadeout 2.5
    scene JunLivingRoom
    show j 1 c fluster at fdis, three
    show yui 1 c smile at seven
    with fade
    play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
    play sound "music/tap.ogg"
    "I don't have time to respond as she immediately grabs hold of my wrist and starts pulling me to the living room."
    "Jun follows behind, too shocked to say anything."
    "Meeting her is starting to shed some light into Jun's boisterous personality..."
    "Once we get to the living room, I see a burly tiger sitting on a cushion and watching TV."
    yui "\"Honey, Jun's brought a friend over!\""
    "The man shuffles in his seat, turning to look at us."
    "Jun's Father" "\"A friend, what are y-\""
    "As soon as his eyes fall on me, he freezes."
    "Uhh... I don't think this is a good sign..."
    show j 1 c fluster at fdis, two
    show yui 1 c smile at eight
    with move
    show ats 1 c c smile at five with dissolve
    "He gets up, standing menacingly close to me, his eyes mere slits."
    "Jun's Father" "\"Yoooou!\""
    "His voice is low, almost like a growl."
    "It's enough to make me shiver to my core."
    "It doesn't help that he looks pretty strong and... is that a police cap he's wearing?"
    mc 1 c fsmile "\"S-Sir?\""
    show j 1 c wince at fdis
    j "\"Oh no...\""
    "Jun mutters something under his breath."
    "The father lifts up both of his arms. I instinctively close my eyes and lift my own arms to cover my face."
    play sound "music/tap.ogg"
    show ats 1 c c smile at five:
        ease .2 zoom 1.5 xoffset -30 yoffset 200 #moves right 100px, bottom 50px. set to 0 when you return later.
    "Jun's Father" "\"You're him, you're really him! Oh my God oh my God oh my God!\""
    "The man wraps his arms around me and begins to squeeze me incredibly hard."
    show j 1 c bored at fdis
    mc 1 c shock "\"Whaaa-?!\""
    ats "\"I'm Atsushi Kobayashi. It's such a pleasure to meet you. Oh my god, I can't believe you're actually him!\""
    mc 1 c wince "\"I-It's a pleasure too sir. {size=-4}But can you please let go, you're hurting me...{/size}\""
    show ats 1 c c smile at five:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    ats "\"Oh, sorry, I guess I got a bit too excited, gahahahaha!\""
    "His laugh is so loud that I swear I can feel stuff rumbling around us."
    "My first instinct is to reach up and cover my ears, but I don't want to seem rude."
    mc 1 c wince "\"I-I'm sorry, I'm a bit overwhelmed. Who am I supposed to be?\""
    j "\"Dad's a {i}big{/i} tennis fan. He's been following your career for the past five years. Kept tabs on every single one of your matches. I think he even has most of them on video...\""
    ats "\"Shhh, you don't have to tell him!\""
    "I mean... I prefer to have this told to me. Otherwise I'd assume your reaction just know is how you treat all of your son's friends... in which case you'd come out looking even weirder."
    ats "\"I can't believe you're actually him. When my son told me he met a tennis player named [povName], I thought for sure it was just some happy coincidence. I didn't think for a second-\""
    play sound "music/slap.ogg"
    "He smacks his fist on his palm and, without finishing his sentence, runs to his entertainment center, where he takes a... VHS tape?"
    "VHS, huh? Talk about old-school."
    "He pops it into the VHS player and eventually, image comes up on the screen."
    "I immediately recognize it... because the one on-screen is me."
    ats "\"This... this is you. And this is also you!\""
    "His eyes keep going from the TV to me, he also keeps making extravagant gestures in childish excitement."
    "When I look over to Jun who's standing next to me, he looks completely horrified."
    show j 1 c wince at fdis
    j "\"D-dad, please, settle down.\""
    ats "\"Sorry, sorry. I guess I got too excited. It's just... I can't believe [povName] is standing in my living room. What are you even doing with my son? I never thought he'd be able to make friends with an athlete!\""
    show j 1 c annoyed at fdis
    j "\"{size=-4}Thanks for the vote of confidence...{/size}\""
    "Huh... I guess every kid is embarrassed by their parents at times."
    "It's universal."
    "It's weird how incredibly similar he is to his parents, though. Frighteningly so."
    mc 1 c fsmile "\"W-well, Jun-kun is very fun to hang out with, {size=-4}even if he's a little overwhelming sometimes{/size}.\""
    mc 1 c smile "\"Still, he's a nice guy. We like having him around.\""
    ats "\"Wow. This is just- I just... Wow!\""
    mc 1 c fsmile "\"S-Still, why would you follow me anyway? I'm not even a professional player yet. I know it'd probably be much more exciting to watch professional matches.\""
    ats "\"Not at all. I love seeing diamonds in the rough. And, to be honest, we've never had really talented players in Japan before. You're carrying the hopes of our nation as a player. You're certainly the best. Why {i}wouldn't{/i} I follow you?\""
    mc 1 c fsmile "\"W-Well, I'm not the {i}best{/i}. Not really. I can't compete with other players in the Major leagues and, even in my own league, I still can't get number 1. Tanabe is the better player, if you want to root for someone, it should be him.\""
    "Kobayashi-senior groans, rolling his eyes."
    ats "\"Ah, yes. Tanabe is {i}technically{/i} the superior player right now, but I honestly believe you're more talented than he is. Plus, his game completely lacks passion. It's like watching a chess match. Seeing him play is so boring.\""
    ats "\"You on the other hand always gets me on the edge of my seat. Every play with you is filled with anticipation. You don't hold back, you don't go for the safe option. You just see what you have to do and you go at it!\""
    play sound "music/tap.ogg"
    "Jun's mom places a hand on her husband's shoulder, calling his attentiom."
    yui "\"Honey, I understand you're excited, but please settle down, okay? You're overwhelming our guest.\""
    ats "\"O-oh, right. Sorry.\""
    "THANK YOU!"
    yui "\"By the way, honey, I've invited [povLastName]-kun to have dinner with us. Would you please help me get things ready?\""
    mc 1 c wince "\"W-wait, I-\""
    show j 1 c sigh at fdis
    "Jun leans onto my ear and whispers at me."
    j "\"{size=-4}Just give up. Once she gets something in her head, there's no changing her mind. She'll hold you hostage if she has to.{/size}\""
    "That's... very disturbing."
    "I really hope he doesn't mean it in the literal sense..."
    mc 1 c smile "\"Well, at least let me help, then. I can cook.\""
    yui "\"Such a polite young boy! But that's nonsense, sweetie. Just play around with Jun, everything's almost done. I was going to tell him dinner would be ready in a couple of minutes anyway.\""
    show j 1 c watch at fdis
    yui "\"By the way. Jun, honey, I stopped by that dinner you liked and I picked up some Okonomiyaki for dinner. I know you love it.\""
    show j 1 c wince at fdis
    j "\"Wha- but mom, that place is super expensive!\""
    yui "\"It's not a problem. I wanted to cheer you up after your h-\""
    show j 1 c sigh at fdis
    j "\"{cps=60}{size=+4}Mom!{/size} That's okay, thank you we'regoingbacktomyroomnowbye!{/cps}\""
    scene JunBedroom
    show j 1 c sigh at fdis, five
    with fade
    stop music2 fadeout 2.5
    play music3 "music/BGM/Summer Day.ogg" fadein 5.0
    "Before I even notice what's happening, Jun has started pushing me back to his room."
    "I didn't even know he could move this fast!"
    "After the door is closed and locked, he lets himself slide down to the floor, burying his face in his knees."
    j "\"Oh god, I'm so sorry you had to see that. My parents tend to be a bit much.\""
    mc 1 c considerate "\"Don't worry about it. I'm used to it already.\""
    "You've given me quite a bit of a test-run after all."
    show j 1 c wince at fdis
    j "\"Sorry about my dad in particular. He means well, but he tends to get way too excited about tennis. I hope he didn't creep you out...\""
    mc 1 c wry "\"Not at all. Although I'm really not all that your dad makes me out to be.\""
    show j 1 c pout at fdis
    j "\"That's not true!"
    show j 1 c wince at fdis
    extend " I mean..."
    show j 1 c think at fdis
    extend " I haven't been watching tennis for all that long. I kind of stayed away from the sport just because it was embarrassing being around dad when he's like that, but I really think you're amazing.\""
    show j 1 c gentle at fdis
    j "\"I really like watching you play. I feel like I get to see a [povFirstName]-san that I can't see anywhere else.\""
    mc 1 c happy "\"Aww, thank you. I like seeing you play the piano too. You're really different when you play, I like that.\""
    show j 1 c watch at fdis
    j "\"I am? How so?\""
    mc 1 c think "\"Well, you're a lot more... focused when you're playing.\""
    show j 1 c think at fdis
    j "\"What? That's not true. I'm always focused.\""
    "... This family is severely lacking in the self-awareness department."
    show j 1 c wry at fdis
    j "\"Still, you should probably get yourself ready for a barrage of questions, though. I'm sure dad will make the dinner table conversation all about you.\""
    mc 1 c shock "\"R-really? Alright, then.\""
    "W-what did I get myself into?"
    stop music3 fadeout 2.5
    scene Street1N with fade
    play music "music/night.ogg" fadein 5.0
    "Dinner was pleasant enough. Yui-san made a bunch of delicious side-dishes to complement the Okonomiyaki, which was also quite fancy too, not the kind you'd find in any regular food cart."
    "Like Jun said, though, his dad hit me with question after question about tennis."
    "If it was already hard keeping up with one Jun, having to deal with two other people like him was just..."
    "I'm exhausted!"
    "Right now I'm walking back home, trying to recharge a little."
    show j 1 c wry at fdis, five
    j "\"Are you sure you won't get lost? I can go all the way to your house if you want.\""
    "Of course, Jun insisted on accompanying me partway for fear that I'd get lost... even though I've lived here for years."
    mc 1 c considerate "\"You don't have to. Seriously, don't worry about it. I live nearby anyway.\""
    show j 1 c wince at fdis
    j "\"Y-yeah...\""
    show j 1 c wry at fdis
    j "\"Again, sorry about my parents. I hope they didn't make you uncomfortable. {size=-4}They definitely did with me...{/size}\""
    mc 1 c smile "\"No, far from it. Your parents are... different, but they're really nice people. I feel a little jealous of you. I wish my family were like that.\""
    show j 1 c watch at fdis
    j "\"Is there anything wrong with your family?\""
    mc 1 c think "\"Well... My father isn't around anymore. Mom had to go back to work when we were little to be able to provide for us.\""
    mc 1 c considerate "\"At first it was really hard for us... she kept having to juggle two or more jobs all the time and she'd always be exhausted. She never had time for us back then.\""
    mc 1 c think "\"I basically raised Aki on my own. It was hard to make it work, especially because my training hours were very short when I first started playing, but we managed.\""
    mc 1 c smile "\"Mom eventually got a well-paying job at a law firm and things have been stable for us for a while.\""
    mc 1 c considerate "\"Still, I sometimes miss having a dad. I don't remember much about him.\""
    mc 1 c wry "\"When I first realized I couldn't remember my dad's voice anymore it was... difficult.\""
    show j 1 c wince at fdis
    j "\"O-oh... I'm sorry, I-I didn't know your father had left you guys.\""
    "Left? Ah, I see... he misunderstood me."
    "Well... I guess I'll let it slide. I don't want to make him upset, let alone feel guilty about bringing it up."
    mc 1 c considerate "\"Nah, don't worry about it. I made my peace with it a long time ago.\""
    mc 1 c happy "\"Plus, since I always spent so much time with Aki, the two of us are very close. Not many people can boast about having such a close friendship with their brother.\""
    show j 1 c happy at fdis
    j "\"Yeah. It must be nice... having a brother I mean. I was always an only child.\""
    show j 1 c think at fdis
    j "\"Mom and dad didn't actually plan on having me. I remember my grandmother letting it slip one day that I was an accident."
    show j 1 c wince at fdis
    extend " Mom was beyond pissed with her.\""
    show j 1 c wry at fdis
    j "\"As far as I know, dad got \"fixed\" after I was born so they wouldn't have any other children.\""
    show j 1 c considerate at fdis
    j "\"Still, they've always taken really good care of me and they always make sure I have everything I need. Even when that meant they didn't. It makes me feel really guilty sometimes...\""
    mc 1 c smile "\"That's what parents do, stupid. If you really feel bad about it, then make sure you make something out of yourself. I'm sure your parents just want you to be happy.\""
    j "\"Yeah, you're right.\""
    show j 1 c watch at fdis
    "We reach an intersection. Jun stops walking and I follow suit. He keeps staring at the ground, not saying anything. Eventually, he looks over at me, very shyly."
    show j 1 c smile at fdis
    j "\"Thanks for keeping me company."
    show j 1 c happyb at fdis
    extend " I thought I'd just spend the day feeling lonely and bored, but it turned out to be very fun. Thanks a lot, [povFirstName]-san.\""
    "I think I almost catch a hint of a blush before he turns to look away."
    "It brings a smile to my face."
    mc 1 c smile "\"Any time, Jun. If you ever need something from me, don't hesitate to ask.\""
    show j 1 c smile at fdis
    "He nods."
    j "\"I'm gonna get back home before mom and dad start worrying about me. I'll see you tomorrow, [povFirstName]-san!\""
    mc 1 c smile "\"See ya!\""
    "We have goodbye to each other and Jun jogs his way back home."
    "I watch his back fade away from my sight, thinking over how pleasant today was despite everything that's happened."
    stop music fadeout 2.0
    $ date = None
    jump Day6
    return
