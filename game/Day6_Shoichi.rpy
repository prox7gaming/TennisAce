label Day6_Shoichi:
    window hide
    scene April11 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene Black with fade
    window show
    $ date = "day6"
    play music "music/tickingclock.ogg"
    "My eyes struggle to open."
    "My eyelids feel heavy and unresponsive."
    "No... my whole body feels that way."
    "My throat feels scratchy, hot and uncomfortable..."
    "Somehow, I feel like I'm hot and cold at the same time."
    "I feel as if I had someone sitting on my chest... no matter how much I want to move, my body does not budge."
    "All I can hear is the sound of a ticking clock..."
    "Slowly, I can feel my consciousness returning."
    play sound "music/fabric.ogg"
    scene Bedroom with fade
    "Once my eyes get adjusted to the brightness, I begin to look around."
    "At least my body can move again..."
    "Wait, is this my room?"
    "How did I even get here?"
    "The last thing I remember is... being in the bathroom?"
    "I felt really sick and..."
    "Ugh... my whole body hurts..."
    "As I'm adjusting myself on the bed, I feel something heavy on top of my thigh."
    mc 1 b shock "\"Wha-\""
    show cg15_pan with Dissolve(1.0):
        subpixel True
        yalign 0.0
        linear 0.7
        linear 9.0 yalign 1.0
    "I look down and-"
    mc 1 b shock "\"S-Shoichi?!\""
    "I see Shoichi sitting on a chair, hunched over the bed, peacefully sleeping."
    show cg15
    hide cg15_pan
    with dissolve
    "He's using my legs as a pillow of some sort, breathing slowly and deeply."
    "When did he get here?!"
    "He begins to shift, being stirred awake by my sudden movement and noise."
    "His eyes blink sluggishly."
    "His mouth opens in a comically large fashion as he yawns, sitting up on his chair and lazily rubbing his eyes."
    hide cg15
    show s 1 u wince at fdis, five
    with dissolve
    s "\"Huh- Ah, [povFirstName]?\""
    show s 1 u shock at fdis
    s "\"[povFirstName]?! You're awake! How are you feeling?\""
    mc 1 b wince "\"Like I fought one round too many with an angry badger or something.\""
    mc 1 b "\"What are you doing here?\""
    stop music fadeout 5.0
    play music2 "music/BGM/The People Here.ogg" fadein 5.0
    play sound "music/fabric.ogg"
    "I shuffle around in my bed and, at that moment, I realize something's missing."
    "I do not feel the familiar sensation of fabric against my fur."
    "I look down and underneath the blanket and-"
    mc 1 b shockb "\"Wha- Did you take my clothes off?!\"" with hpunch
    show s 1 u considerate at fdis
    s "\"Yeah, sorry about that. You were covered in vomit when I found you so I don't think you wanted to keep wearing those clothes.\""
    show s 1 u wry at fdis
    s "\"I gave you a quick rinse and got you back into bed. I also put your clothes in the washing machine.\""
    "O-oh..."
    mc 1 b wince "\"Sorry for the trouble. Do you have any idea what happened to me?\""
    play sound "music/fabric.ogg"
    show s 1 u sigh at fdis
    "Shoichi gets up from his chair, stretching his back and yawning."
    "How long has he been out for?"
    show s 1 u at fdis
    s "\"You didn't show up for class today. I tried to give you a call around 10 but you weren't answering either so I decided to drop by and check up on you.\""
    show s 1 u wry at fdis
    s "\"Uhm... I hope you don't mind that I used your spare key by the way.\""
    mc 1 b "\"I don't. What else happened?\""
    show s 1 u wince at fdis
    s "\"I found you collapsed in the bathroom. You were looking awfully pale and I didn't really know what to do, so I cleaned up after you and dragged you to bed.\""
    "My memory is really fuzzy... I don't remember much of what happened after I came home."
    "I... I seem to recall feeling sick..."
    "And there was a lot of puking involved."
    "I remember my legs being so weak that I couldn't stand..."
    show s 1 u sad at fdis
    s "\"I'm sorry...\""
    mc 1 b shock "\"Huh, what about?\""
    s "\"I got a call from Bunta-san, the owner of the food stand we went to yesterday.\""
    show s 1 u wince at fdis
    s "\"He called me to check up on \"my friend\" after he found out his new supplier sent him a shipment of bad shrimps. That's why I decided to drop by when you didn't show up this morning.\""
    show s 1 u sad at fdis
    s "\"So, really, this is all my fault. If I hadn't taken you there yesterday, you'd have been fine. I'm sorry...\""
    mc 1 b shock "\"No no, you don't have to apologize. I'm fine, loo-\""
    "I get up from the bed, jumping back on my fe-"
    "Huh?"
    play sound "music/tap.ogg"
    show s 1 u shock at fdis:
        ease .2 zoom 1.5 xoffset -30 yoffset 200 #moves right 100px, bottom 50px. set to 0 when you return later.
    s "\"Hey!\""
    "It all went by so fast that my mind only registers it afterwards."
    "My legs failed as soon as I tried to put my weight on them and I fell."
    "Shoichi reacted fast and grabbed me before I could hit the floor."
    "Shoichi falls to his knees as he grabs me, my face landing squarely on his chest."
    s "\"[povFirstName], are you okay?\""
    show s 1 u sigh at fdis
    s "\"Jeez, don't be so reckless. You're obviously not okay. You're burning with fever for God's sake!\""
    "My mind doesn't really register his words right away."
    "I try pushing myself away from him, but can't put any force in my arms."
    "My body struggles to even move."
    mc 1 b shock "\"H-huh? Wha- Why can't I...\""
    show s 1 u wry at fdis
    s "\"I told you to calm down. You're weak and severely dehydrated. When was the last time you had a drink?\""
    mc 1 b wince "\"Uh- Uhm... last night at the food cart?\""
    show s 1 u wince at fdis
    s "\"Damn, that long ago? We need to get some food and water in you asap. Hang on, I'll go grab you a glass of water.\""
    show s 1 u wry at fdis:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    "Shoichi grabs me tightly and tries to move me back to the bed."
    "Once his hand touches my stomach, my whole body attempts to pull back, making me yelp in pain."
    show s 1 u considerate at fdis
    s "\"Sorry. Just bear it for now, okay?\""
    play sound "music/fabric.ogg"
    show s 1 u wry at fdis
    "Once he's sure that I'm safely tucked into the bed, Shoichi gets up."
    s "\"I'll be right back, okay? Please stay still while I'm away.\""
    show s 1 u wry at fdis, offscreenright with moveoridis
    "..."
    "I've never been one to listen to orders before."
    "I try moving around a bit, but my body refuses to do as it's told."
    "I can't even hold a tight grip."
    show s 1 u smile at fdis, five with moveiridis
    "Before I even had time to miss him, Shoichi is already back."
    "God, he was so fast. Did he run all the way here?"
    s "\"Here you go, just make sure to t-\""
    play sound "music/tap.ogg"
    show s 1 u shock at fdis
    "I immediately snatch that water glass from his hand."
    "Just looking at it makes me realize how thirsty I am!"
    s "\"Wait!\""
    show Black with Dissolve(0.25)
    hide Black with Dissolve(0.25)
    "My entire vision goes dark for a second."
    "A wave of nausea hits me instantly, my stomach begins to churn."
    show s 1 u wince at fdis
    s "\"Use this!\""
    "Shoichi puts a small bucket in front of my face. I grab it tightly as the water I just drank is violently rejected by my stomach."
    "Yuck..."
    show s 1 u sigh at fdis
    s "\"I was going to tell you to pace yourself, but you really were in a rush, huh?\""
    show s 1 u wry at fdis
    s "\"Your stomach is really upset right now. You have to take it easy so it can have time to adjust.\""
    mc 1 b wince "\"S-sorry.\""
    show s 1 u considerate at fdis
    s "\"Don't worry about it. I'll go... uh, empty the bucket and get you another glass of water. Be right back.\""
    show s 1 u at fdis
    "Just as he gets up to leave, I notice a stain has gotten on the cuffs of his uniform."
    mc 1 b wince "\"S-Shoichi...\""
    "He looks down at the spot I'm staring at."
    show s 1 u wry at fdis
    s "\"Oh, this? Don't worry about it, I'll wash it once I get home.\""
    stop music2 fadeout 5.0
    show s 1 u wry at fdis, offscreenright with moveoridis
    "..."
    "And once again I'm all by myself."
    "Only now do I realize the sun rays hitting the drapes of my bedroom."
    "Wait, it can't be that late already, can it?"
    "I look around for a bit and find my phone on top of my dresser, next to my bed."
    play sound "music/phonebeep.ogg"
    "I pick it up and check the time."
    "13:22... And he said he left class to check on me."
    "That means he's been here for quite a few hours already..."
    "And he's spent all this time taking care of me?"
    "Oh God, I can't believe he went through all this to take care of me."
    "A wave of guilt assaults me."
    "I put the phone down and try getting up again."
    "Even though he told me not to, I just can't stand lying in bed like this."
    "My stomach begins to cramp and my legs try to resist me at every step."
    "They start shivering uncontrollably and I fear I may collapse."
    menu:
        "Give up and get back to bed.":
            $ walk = False
            "No, if I keep going like this and fall, Shoichi wouldn't be here to catch me like last time. I could get really hurt."
            "Plus, I can't bear to trouble him any further."
            "I'll just do as he says and rest, even if it bothers me..."
            play sound "music/fall.ogg"
            "I let myself fall back into bed and take a deep breath."
            "For the time being, I guess there's nothing for me to do but wait."
            show s 1 c smile at fdis, five with moveiridis
            "Shoichi emerges from the door once again, another glass of water in his hand."
            mc 1 b shock "\"You got changed?\""
            show s 1 c smile at fdis
            s "\"As luck would have it, I decided to pack some extra clean clothes today since I wouldn't be having volleyball practice.\""
            show s 1 c happy at fdis
            s "\"Big coincidence, huh?\""
        "Try to get up.":
            $ walk = True
            "I don't care if they object. They're {i}my{/i} legs and they should do as I say!"
            "I try taking a step and feel my body starting to buckle."
            play sound "music/fall.ogg"
            "Instinctively, I reach out for my nightstand, putting as much force on my arm as I can to break my fall."
            mc 1 b wince "\"Crap!\""
            "It takes me a couple of seconds to stabilize, but I manage to hold myself up somehow"
            "Even though I've barely moved, I'm already breathing heavily and panting."
            "Try as I might, I feel completely exhausted."
            "But just this much isn't enough to make me give up!"
            "I try to take another step and, this time, it comes much easier than the last one."
            "Even though my entire body is screaming for me to stop, I refuse to give in."
            "I take a step at a time."
            "I'll be damned if I'll stay in bed just because of food poisoning."
            s 1 c shock "\"What are you doing?!\"" with hpunch
            play music3 "music/BGM/Punchline.ogg" fadein 5.0
            show s 1 c frown at fdis, five with moveiridis
            "I look at the door and see Shoichi rushing towards me."
            play sound "music/tap.ogg"
            "Before I can even react, he's already grabbed me by my waist and lifted me over his shoulder."
            mc 1 b shock "\"W-Woah!\""
            show s 1 c displeased at fdis
            s "\"Seriously, when will you learn?\""
            mc 1 b wince "\"Wha- Why are you so strong?!\""
            play sound "music/fall.ogg"
            "He tosses me back on top of my bed."
            mc 1 b wince "\"Ow! At least put me a down a little more gently.\""
            show s 1 c scorn at fdis
            s "\"No. That's what you get for not listening to me.\""
            show s 1 c sigh at fdis
            "He rubs the bridge of his nose, his entire face scrunched up in a frown."
            mc 1 b curious "\"Huh... wait. Shoichi, you've gotten changed?\""
            show s 1 c think at fdis
            s "\"Oh, this?\""
            show s 1 c smile at fdis
            s "\"As luck would have it, I decided to pack some extra clean clothes today since I wouldn't be having volleyball practice.\""
            show s 1 c happy at fdis
            s "\"Big coincidence, huh?\""
            stop music3 fadeout 2.5
    play music2 "music/BGM/Snowy Day.ogg" fadein 5.0
    show s 1 c smile at fdis
    s "\"Well, not that it matters now. Here's your water. Just go slow this time. Take it half a sip at a time if you can.\""
    "..."
    "....."
    "......."
    show s 1 c considerate at fdis
    s "\"You don't have to stare at the water like that, you know. It's not gonna hurt you or anything.\""
    "But what if I react the same way as last time?"
    "..."
    mc 1 b sigh "\"Just so we're clear, you haven't poisoned this, right?\""
    show s 1 c sigh at fdis
    s "\"Just drink the damn water already before I force it down your throat.\"" with hpunch
    mc 1 b happy "\"Alright, alright. Calm thyself.\""
    "I place the tip of the glass on my lips and let some water run down my mouth."
    "Oh man, I so want to drink this whole thing already."
    "But I can't keep causing trouble for Shoichi, and I'm sure he wouldn't like to get puked on... again."
    show s 1 c at fdis
    mc 1 b curious "\"No bucket this time?\""
    show s 1 c smile at fdis
    s "\"You're not going to throw up.\""
    mc 1 b "\"How do you know that?\""
    s "\"I had to care for Hitoka when we were kids and my parents were out of town."
    show s 1 c think at fdis
    extend " Mom gave me a bunch of instructions on how to treat food poisoning over the phone. I never forgot them.\""
    mc 1 b smile "\"I guess that's a pretty decent perk to having a trained nurse for a mother.\""
    show s 1 c happy at fdis
    s "\"Yep!\""
    show s 1 c smile at fdis
    s "\"I know you're supposed to start taking liquids very slowly so your stomach can get used to ingesting stuff again.\""
    show s 1 c happy at fdis
    s "\"Then, once you can take a glass of water without throwing up, I'll get you some soup so you actually have some nutrients in you.\""
    "Well, I guess I could do worse than water and convenience store soup."
    mc 1 b smile "\"You seem to be plenty prepared for this.\""
    show s 1 c happy at fdis
    s "\"Yeah, well, I had some time while I was waiting for you to wake up, so I went out and bought some ingredients for the soup.\""
    "Wait... ingredients?"
    "He... he's not talking about making it from scratch, is he?"
    "Please God, tell me it ain't so!"
    play sound "music/fall.ogg"
    show s 1 c sigh at fdis
    "Before I can vocalize my doubts, Shoichi's entire body relaxes. He basically throws himself down on the chair he placed next to my bed."
    mc 1 b wince "\"Are you alright?\""
    show s 1 c wry at fdis
    s "\"Oh, yeah, sorry. I'm just a little tired. I stayed up pretty late working on stuff for the council.\""
    mc 1 b sigh "\"You're going to work yourself to death if you keep this up.\""
    show s 1 c considerate at fdis
    s "\"I'll be fine. You don't have to worry about me.\""
    mc 1 b sigh "\"Really? You're going to say that after that whole conversation we had yesterday?\""
    show s 1 c think at fdis
    s "\"...\""
    "... And here I thought he had taken my advice to heart..."
    show s 1 c sigh at fdis
    s "\"I promise if it gets to be too much, I'll say something, okay?"
    show s 1 c considerate at fdis
    extend " It's just that I honestly don't think it's too bad right now. I still have a reduced workload. I was just making up for some delays I had yesterday.\""
    mc 1 b "\"These delays wouldn't happen to be because you took me out yesterday instead of going home to work, would they?\""
    show s 1 c think at fdis
    s "\"Well..."
    show s 1 c wry at fdis
    extend " Kinda?\""
    "... I should have said no to his offer yesterday."
    "... It would have been better for {i}both{/i} of us."
    mc 1 b smile "\"So, {i}doc{/i}, what course of treatment do you have in mind for me?\""
    show s 1 c happy at fdis
    s "\"Really? \"Doc\"?\""
    mc 1 b happy "\"Hey, you're the one in charge of treating me, aren't you?\""
    show s 1 c smile at fdis
    s "\"True enough.\""
    show s 1 c think at fdis
    s "\"We're not gonna do anything too fancy. Just plenty of fluids and rest.\""
    mc 1 b think "\"That's it? What a quack. I knew I should have gone to a {i}real{/i} doctor.\""
    show s 1 c happy at fdis
    s "\"Oh, I can set that up if you want. Yeah, I'll drag you back to the bathroom floor and I'll leave you lying there without your phone. Then you can feel free to call a {i}real{/i} doctor.\""
    "... How can you say something so terrifying with that look on your face?!"
    mc 1 b fsmile "\"Well, on second thought...\""
    s "\"That's what I thought.\""
    show s 1 c smile at fdis
    s "\"Well, now it's just a matter of being patient. You'll keep drinking little sips of water every couple of minutes for a while until your stomach gets better.\""
    mc 1 b smile "\"Aye aye, Captain!\""
    show s 1 c considerate at fdis
    s "\"Now it's \"captain\"? Make up your mind already...\""
    scene Bedroom
    show s 1 c laugh at fdis, five
    with fade
    "Despite the burning sensation in my throat, the painful feeling in my stomach, and overall weakness, I'm having a surprisingly good time."
    show s 1 c smile at fdis
    "It's been so long since Shoichi and I had an entire day just to ourselves without worrying about anything else."
    show s 1 c laugh at fdis
    "It feels good to talk to him for a long time... like we used to do when we were kids."
    "... Although it was still embarrassing to have him dress me up."
    "I don't know what was worse, being only in my boxer briefs or having someone you've known for over a decade play dress-up with your body."
    play sound "music/doorbell2.ogg"
    show s 1 c think at fdis
    "Just then, our attention is snapped towards the echoing sound of the doorbell."
    mc 1 c curious "\"Someone's here? That's weird.\""
    s "\"Oh, that's right. I sent everyone a message after I found you. I told them you were sick and that I was taking care of you.\""
    show s 1 c smile at fdis
    s "\"Jun-kun and Urushihara said they'd come by after class.\""
    show s 1 c considerate at fdis
    s "\"Oh, and Saya-chan asked me to tell you she couldn't make it because she has a shift today. She told me to apologize on her behalf.\""
    mc 1 c shock "\"Wha- it's no trouble. Really, I'm surprised everyone would go out of their way like this to come see me.\""
    show s 1 c laugh at fdis
    s "\"What are you talking about? You're our friend. What did you expect us to do?\""
    play sound "music/AngryKnock.ogg"
    "Jesus, now they're pounding on the door..."
    show s 1 c think at fdis
    s "\"I better go let them in before Urushihara breaks your door down.\""
    show s 1 c smile at fdis, offscreenright with moveoridis
    "After about a minute or two, I start to hear the sound of voices downstairs."
    "Then I hear as they approach... first coming up the stairs and-"
    show s 1 c smile at fdis, five
    show j 1 u happy at fdis, two
    show k 1 u at fdis, eight
    with moveiridis
    "All three of them emerge from the doorway."
    "Jun and Shoichi seem to be excitedly chatting amongst themselves."
    "Meanwhile, Keisuke ignores the two and walks up to me."
    show k 1 u smile at fdis
    k "\"Hey, how are you doing?\""
    show j 1 u shock at fdis
    "After Kei-kun speaks, Jun seems to be reminded of the fact that I'm sick on the bed, as he suddenly turns to look at me."
    show j 1 u wince at fdis
    j "\"Yeah, how are you feeling?\""
    if walk == True:
        mc 1 c think "\"Well... I can barely stand, my throat is on fire, I haven't eaten anything since last night and everything I do eat ends up coming back out so, you know... all in all, can't complain.\""
    else:
        mc 1 c think "\"Well... I can't even stand, my throat is on fire, I haven't eaten anything since last night and everything I do eat ends up coming back out so, you know... all in all, can't complain.\""
    show k 2 u gentle at fdis
    k "\"Talk about optimism."
    show k 1 u smile at fdis
    extend " So Urata's been caring for you all morning, then?\""
    mc 1 c "\"Pretty much. I guess I passed out at some point during the night. Shoichi found me on the floor and brought me back to the bed.\""
    show j 1 u shock at fdis
    j "\"Wha- He managed to lift you? How strong is he?\""
    mc 1 c smile "\"Scientists are still trying to figure that one out.\""
    show s 1 c sigh at fdis
    s "\"Har har, very funny.\""
    show j 1 u gentle at fdis, shake1
    j "\"Pfft, hahaha.\""
    show s 1 c laugh at fdis
    show k 2 u gentle at fdis
    "Jun's laughter is all it takes to lift the mood."
    "Soon enough, we're all laughing together at a silly little joke."
    show s 1 c wry at fdis
    show j 1 u watch at fdis
    show k 1 u smile at fdis
    s "\"Well, either way, [povFirstName] seems to be doing much better. At least he's not throwing up anymore.\""
    show j 1 u wince at fdis
    show k 1 u at fdis
    j "\"Yuck. I didn't need to know that.\""
    show j 1 u watch at fdis
    show k 1 u sigh at fdis
    show s 1 c considerate at fdis
    k "\"He has food poisoning, what did you expect him to be doing? Baking a cake?\""
    show j 1 u think at fdis
    j "\"I don't know. I didn't think about it.\""
    "Well, not thinking about stuff is kind of your forte so I expected this much."
    show j 1 u watch at fdis
    show k 1 u at fdis
    show s 1 c smile at fdis
    mc 1 c curious "\"By the way, did anything happen at class today, Jun?\""
    show j 1 u shock at fdis, jumping
    j "\"Oh, that's right!"
    show j 1 u happy at fdis
    extend " After Sho-san told me you wouldn't be showing up today, I decided to take some notes for you. That way you wouldn't miss much!\""
    show s 1 c smile at fdis, offscreenright with moveoridis
    play sound "music/fabric.ogg"
    "He pulls out a couple of notebooks from his bag."
    j "\"I have the pages marked with some paper.\""
    "I take one of the notebooks he hands me."
    stop music2 fadeout 2.5
    play music3 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    mc 1 c happy "\"Aww, thanks, you didn't have..."
    mc 1 c shock "{fast} to...\""
    "This... this is a bunch of incomprehensible scribbles and- ... IS THAT A DRAWING?!"
    mc 1 c fsmile "\"You {i}really{/i} didn't have to...\""
    "Oh boy, I'd need an advanced linguistics degree to translate all this stuff."
    j "\"It's no problem. I thought you might need these later to study. The teacher said these would be in our midterms.\""
    mc 1 c fsmile "\"Oh God, midterms...\""
    show k 1 u wry at fdis
    "Whilst Jun is standing there, beaming with pride, I see Kei-kun flashing me a compassionate look."
    show k 1 u considerate at fdis
    k "\"I spoke to a few upperclassmen from the club and asked them to take notes too. I've compiled all the relevant stuff here for you.\""
    "He hands a bunch of folders."
    "Wait... are each of these folders separated for individual fields of study? {i}And{/i} they're color coded?!"
    show j 1 u pout at fdis
    j "\"But Keisuke-san, I've already given him my notes.\""
    show k 1 u calm at fdis
    k "\"I know, but it doesn't hurt to be thorough, right?\""
    j "\"I guess not.\""
    show k 1 u smile at fdis
    "Keisuke winks at me."
    "I feel like I should hug you..."
    "I start going through the notes, giving them a cursory glance."
    mc 1 c shock "\"W-wow, these {i}are{/i} thorough...\""
    "There's a whole chapter on integration and advanced calculus."
    "This is college prep stuff. I don't even study this yet!"
    show k 1 u calm at fdis
    k "\"Yeah, I like to be thorough. I didn't know how much of this stuff you already had, so I got all the info I could.\""
    mc 1 c shock "\"There's no way you did all this between the end of class and getting to my house.\""
    show k 2 u gentle at fdis
    k "\"I worked on a lot of it during a particularly boring history class. No biggie.\""
    "I... I can't imagine an honor student like Kei-kun doing something like this in the middle of class."
    mc 1 c happy "\"Thanks a lot, Kei-kun.\""
    show j 1 u pout at fdis, jumping
    j "\"Hey!\""
    mc 1 c fsmile "\"...And Jun.\""
    show j 1 u gentle at fdis
    "... I swear, he's so easy to please."
    stop music3 fadeout 2.5
    play music2 "music/BGM/Let it Happen - Narr.ogg" fadein 5.0
    show s 1 c happy at fdis, five with moveiridis
    show j 1 u watch at fdis
    show k 1 u at fdis
    s "\"I brought a couple more chairs.\""
    "Suddenly, Shoichi emerges from the doorway holding two chairs in his arms and starts setting them next to my bed."
    mc 1 c shock "\"I didn't even notice you leaving.\""
    show s 1 c smile at fdis
    s "\"That's because I didn't want to interrupt the conversation. It seemed like you guys were talking about important stuff.\""
    show k 2 u think at fdis
    k "\"Speaking of important stuff, Coach asked me to pass on a message."
    show k 1 u at fdis
    extend " He said once practice starts again, he has a new training menu he wants you to try.\""
    mc 1 c sigh "\"It's about time, really. The training menu I'm using right now is from back when I was in Junior High.\""
    show k 2 u think at fdis
    k "\"Yeah... He hasn't really altered yours at all. Which is weird, because Mizoguchi-san and I both had ours changed quite a few times since I first joined.\""
    mc 1 c sigh2 "\"He's just being lazy as usual.\""
    show k 1 u at fdis
    k "\"I don't really think so. He might come off as lazy, but he does have a pretty sharp eye for this sort of thing."
    show k 2 u think at fdis
    extend " I guess he just didn't think there was a training menu better suited to you before.\""
    mc 1 c "\"Doesn't really sound like coach.\""
    show s 1 c happy at fdis
    s "\"Nah, I'm sure Urushihara is right.\""
    mc 1 c frownj "\"How would {i}you{/i} know?\""
    show s 1 c smile at fdis
    s "\"Mikado-sensei had to fill in for our coach once when he got sick last year.\""
    s "\"Even though he always looked like he was slacking off, whenever we started practicing, he had this very sharp look on his eyes, as if he was watching for every minor detail.\""
    show s 1 c think at fdis
    s "\"He gave us all a very complete evaluation later. We were actually overwhelmed.\""
    j "\"Sheesh. How did your coach react when he saw it?\""
    show s 1 c smile at fdis
    s "\"Threw a fit over how Mikado-sensei wasn't allowed to alter our training menu... then one month later, gave us the exact same training menu saying {i}he{/i} thought of a better menu for us.\""
    show k 1 u sigh at fdis
    k "\"Now {i}that's{/i} someone I wouldn't trust to handle my training.\""
    show s 1 c think at fdis
    s "\"Oh, that's not even the worst part.\""
    j "\"What {i}is{/i}?\""
    show s 1 c wry at fdis
    s "\"The team believed it.\""
    play sound "music/slap.ogg"
    "Kei-kun facepalms."
    show s 1 c considerate at fdis
    show k 1 u at fdis
    s "\"Sooo... yeah. I'll give you my coach if you give me yours.\""
    mc 1 c think "\"Yeah... On second thought, I think I'll hold onto him.\""
    show s 1 c smile at fdis
    s "\"Good call.\""
    mc 1 c curious "\"Oh, I just remembered. Shouldn't you be practicing for your competition, Jun?\""
    show j 1 u shock at fdis
    j "\"Wha-"
    show j 1 u considerate at fdis
    extend " Ah... yeah, no, it's fine. I had to take a break today, anyway.\""
    mc 1 c shock "\"What happened?\""
    j "\"Nothing much, I just think it's better if I take a little break. I wasn't getting anywhere and this might give me some fresh perspective.\""
    show s 1 c seductive at fdis
    s "\"I sense that something fishy's going on.\""
    show j 1 u shock at fdis
    j "\"What? No, no. There's nothing fishy going on. Nothing's going on. Nothing happ-{nw}"
    show j 1 u wince at fdis
    extend " just change the subject!\""
    show s 1 c considerate at fdis
    s "\"Alright, alright. Calm down. You must really not want to talk about it if you started chattering like a crazy person.\""
    show j 1 u shockb at fdis
    show k 2 u gentle at fdis
    j "\"Wha- I didn't!\""
    k "\"You repeated the same thing three times.\""
    show j 1 u flustert at fdis
    j "\"Uuuuu...\""
    mc 1 c considerate "\"Alright guys, give him a break. I can almost see smoke coming out of his head.\""
    show s 1 c laugh at fdis
    "Kei-kun and Shoichi both laugh as Jun hangs from his seat, pouting."
    show j 1 u wince at fdis
    show s 1 c considerate at fdis
    show k 1 u smile at fdis
    s "\"Calm down, Jun-kun, we're just teasing you a bit.\""
    j "\"I don't think I like this teasing...\""
    show k 1 u calm at fdis
    k "\"Hey, before you joined the group, I was the one getting teased.\""
    show j 1 u think at fdis
    j "\"Oh yeah? How was that like?\""
    show k 1 u doom at fdis
    k "\"Hell.\""
    show s 1 c laugh at fdis
    show j 1 u fluster at fdis, jumping
    show k 1 u smile at fdis
    j "\"Wha- That's not encouraging!\""
    show k 2 u gentle at fdis
    k "\"Good, it wasn't meant to be.\""
    show j 1 u flustert at fdis, shake1
    j "\"Uuuuuuu...\""
    show j 1 u wince at fdis
    mc 1 c considerate "\"Alright, Kei-kun. Seriously, give him a break.\""
    show k 1 u sigh at fdis
    show s 1 c think at fdis
    k "\"Why? You never came to {i}my{/i} rescue when I was getting teased relentlessly by Mizoguchi-san and Urata.\""
    mc 1 c happy "\"Yeah, but you're sassy by nature and they were only giving back what you dished out. Jun is far too pure for that.\""
    show j 1 u judge at fdis
    show s 1 c laugh at fdis
    show k 2 u gentle at fdis
    j "\"Why do I feel like that wasn't a compliment?\""
    s "\"Because it really, really wasn't.\""
    mc 1 c shock "\"Heeey, I didn't mean anything bad by it.\""
    k "\"You didn't mean anything good, either.\""
    show j 1 u watch at fdis
    show s 1 c smile at fdis
    show k 1 u smile at fdis
    mc 1 c sigh "\"Alright, let's just change the subject, okay?\""
    s "\"Sure. What else would you like to talk about?\""
    show k 1 u at fdis
    k "\"Actually, I'm still a little sketchy as to how [povFirstName]-san got sick.\""
    show s 1 c wince at fdis
    "From the corner of my eyes, I can see Shoichi's ears folding over his head."
    s "\"Ah... actually, that one was my fault. I took him to a food joint in the old shopping district and he got sick from some iffy seafood.\""
    show k 1 u sigh at fdis
    show j 1 u shock at fdis
    k "\"Seriously? Someone should report that place to the health department.\""
    show k 1 u at fdis
    show j 1 u watch at fdis
    show s 1 c wry at fdis
    mc 1 c think "\"It's not the diner's fault. He told me that that was his first day with a new supplier. It was a screw up on their part.\""
    show k 1 u sigh at fdis
    k "\"Still, a reputable restaurant is supposed to do rigorous checking on all produce and meats that they sell. It's a matter of public health.\""
    show k 1 u at fdis
    show s 1 c considerate at fdis
    show j 1 u think at fdis
    s "\"Not everyone can afford to check every single thing. That's a very simple diner run by one guy alone. And his cleaning standards are already top-notch.\""
    show k 1 u avoid at fdis
    show j 1 u watch at fdis
    k "\"Alright, fine. I'm sorry I mentioned it.\""
    show s 1 c shock at fdis
    show k 1 u at fdis
    j "\"I'm actually surprised that you care about that. I saw you eating Yakisoba Bread from the school cafeteria today. That's not exactly the cleanest place I've ever seen preparing food.\""
    show k 1 u avoid at fdis
    k "\"I didn't have time to pack a lunchbox yesterday. Desperate times call for desperate measures.\""
    show s 1 c wince at fdis
    s "\"I'd hardly call that a \"desperate\" time. The {i}measure{/i} on the other hand...\""
    show k 1 u sigh at fdis
    show s 1 c at fdis
    k "\"Alright, you know what, let's just change the subject!\""
    show j 1 u think at fdis
    show k 1 u at fdis
    j "\"I think we've spent more time asking to change the subject than we did actually discussing a subject.\""
    show k 1 u smile at fdis
    k "\"Do you want us to get back to teasing you?\""
    show j 1 u cshock at fdis, shake1
    show s 1 c happy at fdis
    j "\"No, thanks!\""
    stop music2 fadeout 2.5
    scene BedroomE with fade
    show j 1 u happy at fdis, two
    show s 1 c laugh at fdis, five
    show k 1 u smile at fdis, eight
    with fade
    play music3 "music/BGM/Hanging Out.ogg" fadein 5.0
    "The hours pass by quickly as the four of us chat about all sorts of things."
    "Videogames, hobbies, music, daily happenings."
    "It's good to be able to sit down and just enjoy some extra time with my friends... even if at the cost of my health."
    "Although I could certainly do without Shoichi's constant reminders about needing to take \"one more sip\"."
    "After two hours of this, I'm about ready to smash that glass into his face."
    mc 1 c smile "\"-yeah, and I was told that if I didn't get it done by the end of the month, I'd-\""
    show s 1 c smile at fdis
    s "\"Oh, [povFirstName], it's time for one more sip of water.\""
    mc 1 c annoyed "\"Shoichi, I swear to god! Can't you at least wait until I'm done talking?\""
    show k 1 u sigh at fdis
    show j 1 u think
    k "\"You do know he's doing it on purpose to annoy you, right?\""
    j "\"You reacting like this is just giving him more reasons to do it.\""
    show s 1 c laugh at fdis
    s "\"See, even Jun-kun got it.\""
    show k 2 u gentle at fdis
    show j 1 u annoyed at fdis
    j "\"Heey!\""
    show s 1 c happy at fdis
    s "\"I meant it as a compliment.\""
    "No you didn't."
    j "\"...{nw}"
    show j 1 u happy at fdis
    show s 1 c laugh at fdis
    show k 1 u sigh at fdis
    extend " Okay!\""
    "Don't just buy it that easily!" with hpunch
    mc 1 c think "\"You know, Shoichi, you really ought to-\""
    show s 1 c happy at fdis
    s "\"[povFirstName], the water.\""
    show k 1 u at fdis
    show j 1 u watch at fdis
    mc 1 c angry "\"Let me finish a sentence or so help me God-\""
    show s 1 c sigh at fdis
    s "\"What? You'll try to get up from the bed? Sure, let me watch you fall face first to the floor.\""
    mc 1 c avoid "\"...Damn it.\""
    show s 1 c smile at fdis
    play sound "music/phonebeep.ogg"
    show s 1 c think at fdis
    s "\"Hmm... I think I should get started on that soup."
    show s 1 c smile at fdis
    extend " You guys will have to excuse me. I have to go downstairs to cook.\""
    show k 1 u uncomfortable at fdis
    "Kei-kun visibly arches upon hearing that."
    show k 1 u avoid at fdis
    k "\"*cough*mycondolences*cough*\""
    show s 1 c scorn at fdis
    s "\"Hey, I'm a good cook!\""
    show k 1 u haughty at fdis
    k "\"Sure you are. And I'm a rock star, Kobayashi is a renowned athlete and, also, pigs can fly.\""
    show s 1 c annoyed at fdis
    s "\"Wha- [povFirstName] likes my cooking, right, [povFirstName]?\""
    mc 1 c fsmile "\"Uh...\""
    "Kei-kun leans close to my ear."
    show k 1 u calm at fdis
    k "\"Blink twice if you need help.\""
    s "\"I {i}heard{/i} that!\""
    show k 1 u smile at fdis
    k "\"Good for you. That means you haven't gone deaf yet.\""
    show s 1 c avoid at fdis
    s "\"You know what, I'll show you. I'll make the {i}best{/i} soup you've ever had and I'll make you beg for forgiveness.\""
    show k 2 u gentle at fdis
    k "\"Oh, wow. I didn't realize we were doing stand-up comedy.\""
    show s 1 c scorn at fdis, offscreenright with moveoridis
    "Shoichi leaves the room huffing in a fit."
    play sound "music/crash.ogg"
    "..."
    show k 1 u calm at fdis
    k "\"Seriously, blink twice if you need any help.\""
    mc 1 c annoyed "\"I didn't need it {i}before{/i}. Now that you've made him angry, it'll be ten times worse!\""
    show j 1 u think at fdis
    j "\"Uhm...\""
    "Jun tries to chime in on the conversation."
    j "\"It can't be {i}that{/i} bad, right? You guys are just kidding, right?\""
    show j 1 u watch at fdis
    show k 1 u sigh at fdis
    k "\"Have you ever tried \"Mystery Food X\"?\""
    j "\"Is that a reference to the P-"
    show j 1 u wince at fdis
    extend " Oh...\""
    "Jun swallows audibly."
    show k 1 u wry at fdis
    k "\"Well, I'd love to stay and have some of that soup, but..."
    show k 1 u avoid at fdis
    extend " Actually, who am I kidding? I'm gonna get as far away from that thing as I can.\""
    mc 1 c shock "\"Wha- You poked the hornet's nest and now you're gonna throw {i}me{/i} under the bus?\""
    show k 1 u calm at fdis
    k "\"I'm gonna throw you so hard you won't even have time to see the bus coming.\""
    j "\"Uh... I think I should go too. I have... uhhh... things that I... need to do.\""
    mc 1 c sigh "\"You're fleeing from \"Mystery Food X\" too, aren't you?\""
    j "\"... Yes.\""
    mc 1 c annoyed "\"Oh, come on!\""
    show k 1 u at fdis
    j "\"Well, no offense, [povFirstName]-san, but I saw Urushihara-san eating the cafeteria's Yakisoba Bread today. If he can eat that and then say that {i}this{/i} is disgusting then I {i}really{/i} don't want to try it.\""
    j "\"And if Shoichi-san comes back and sees Urushihara-san gone, he might try to have me eat in his place.\""
    mc 1 c annoyed "\"Wha- Our cafeteria's Yakisoba Bread isn't that bad!\""
    show j 1 u at fdis
    j "\"Would you eat it?\""
    mc 1 c avoid "\"Not in a million years!\""
    show j 1 u considerate at fdis
    j "\"See?\""
    mc 1 c sigh "\"Ugh... fine. Leave me to my suffering.\""
    show k 1 u calm at fdis
    k "\"Hey, at least there's a bright side.\""
    mc 1 c "\"Which is?\""
    show j 1 u watch at fdis
    k "\"Urata's food might kill you and then you won't have to worry about your food poisoning.\""
    mc 1 c sigh "\"Yeah...\""
    "Kei-kun gets up from his chair, grabbing his backpack and putting it around his shoulder."
    show k 1 u smile at fdis
    k "\"Anyway, it's been fun. Now I'm gonna flee before my life is forfeit. Good luck on your future endeavors.\""
    mc 1 c annoyed "\"Bye, turncoats.\""
    show j 1 u gentle at fdis
    j "\"Bye.\""
    show k 1 u smile at fdis, offscreenright
    show j 1 u gentle at offscreenright
    with moveoridis
    "..."
    "I have awful friends!"
    stop music3 fadeout 5.0
    scene BedroomE with fade
    show s 1 c smile at fdis, five with moveiridis
    show s 1 c shock at fdis
    s "\"Hey, where is everyone?\""
    mc 1 c considerate "\"They... said they had something to do and left.\""
    show s 1 c sigh at fdis
    s "\"Aww, man. And I was looking forward to getting rid of that smug look on Urushihara's face.\""
    "Well, he wouldn't be able to be smug when he's dead so you've got that right."
    "Shoichi sets the tray down on my nightstand and shrugs."
    show s 1 c happy at fdis
    s "\"Oh, well. More for you, I guess.\""
    mc 1 c fsmile "\"O-oh... yaaay...\""
    "Shoichi hands me a plate."
    "It has an acrid, bitter smell. It takes a lot not to gag on the spot."
    show s 1 c smile at fdis
    s "\"I hope you like it. I tried to make it is as nutritious as possible!\""
    mc 1 c fsmile "\"What did you put in this?\""
    show s 1 c think at fdis
    play music2 "music/BGM/Punchline - Org.ogg" fadein 5.0
    s "\"Hmm, let's see... There's onions, potatoes, scallions, tomatoes, carrots, soy milk, sea slug, zucchini-\""
    mc 1 c shock "\"Wait wait wait. Back up a bit. What did you just say?!\""
    s "\"Zucchini?\""
    mc 1 c wince "\"No, the thing before that!\""
    show s 1 c laugh at fdis
    s "\"Oh, you mean the sea slug? Yeah, I was a little skeptical at first, but then I remembered hearing about how they're full of proteins and vitamins from this cooking show I saw a couple years ago. I thought they'd make you feel better.\""
    show s 1 c smile at fdis
    s "\"Why? Is there something wrong?\""
    "{size=+4}There's too much stuff wrong to count!{/size}" with hpunch
    mc 1 c considerate "\"N-no... it's fine. What other stuff did you put in this?\""
    show s 1 c think at fdis
    s "\"Hmm... not much else. Let's see, I put flour for thickening, coffee for a stronger flavor, orange juice for acidity, maple syrup for sweetness and, oh, I also put some sports supplements as well for extra vitamins!\""
    "... Oh my God, I'm gonna die."
    show s 1 c happy at fdis
    s "\"Why don't you give it a taste?\""
    mc 1 c fsmile "\"W-Well, I was thinking I should let it cool down for a bit, right?\""
    show s 1 c smile at fdis
    s "\"Way ahead of you. I served those plates about ten minutes ago and have just been waiting for them to cool down.\""
    mc 1 c fsmile "\"Ohhh... Greaaat...\""
    show s 1 c happy at fdis
    s "\"Go on, try it.\""
    "I look down at the plate set in front of me."
    "It's... it's green... and yellow... and a bit blue too... And the texture just looks like a bunch of snot."
    "I can see bits and pieces of roughly chopped... are these even vegetables? They look mushy and yet hard, as if they were both overcooked and raw at the same time."
    "I gulp many times, trying to summon up the courage to try it."
    "I look up again at Shoichi and I see him sitting there, smiling, his eyes almost glinting, his tail wagging uncontrollably."
    "Aw, crap, he's super excited to cook me food, isn't he? How can I say no to that face?"
    "Shit, this is going to be how I die, isn't it? I wonder what's going to be written on my epitaph..."
    "\"Here lies [povName]. Poisoned by his best friend's soup. What an unlucky bastard.\""
    "I take a spoonful of the horrendous liquid and bring it close to my face. It is a horrible assault on my nostrils from the very beginning."
    "As soon as I put some of it in mouth, I feel like I'm in danger of throwing up."
    "Whether that's from my weak stomach or from how foul this concoction is, I have no idea."
    "All I know is that I think I'm over the notion of having food... possibly forever."
    "It's... hell, it's indescribable. It's full of nasty, slimy parts, and then there are chunky parts too. And it all feels like I'm downing actual slime."
    "I'm kinda glad that I'm sick right now because I get the feeling my body is too weak to fully comprehend the actual taste of this thing."
    show s 1 c laugh at fdis
    s "\"So, what do you think?\""
    "My throat is burning and my eyes are watering, but I somehow manage to suppress my urge to gag."
    "I look over to Shoichi and his wagging tail. He's just so happy that I can't bring myself to say anything."
    mc 1 c fsmile "\"...Yumm...\""
    "I try pretending to like it, though I'm pretty sure anyone can notice it's fake."
    "But then again, that's what I thought all of the other times he's made me eat his food."
    s "\"Great. Enjoy!\""
    show s 1 c smile at fdis
    mc 1 c considerate "\"Y-yeah, about that... Could you go downstairs and get me a glass of water?\""
    show s 1 c happy at fdis
    s "\"Sure, just a sec.\""
    show s 1 c smile at fdis, offscreenright with moveoridis
    "..."
    "As soon as he leaves the room, I open the window beside my bed and tilt both plates over it, throwing away all of their nasty contents."
    "I then set them down on the table and close the windows again."
    show s 1 c smile at fdis, five with moveiridis
    show s 1 c shock at fdis
    "When Shoichi comes back and sees the empty plates, he freezes on the spot."
    s "\"What happened to your soup?\""
    mc 1 c considerate "\"It was really good, so I couldn't help myself. I was feeling really hungry.\""
    show s 1 c wince at fdis
    s "\"Ooh. But still, you should have paced yourself. What if this upsets your stomach again?\""
    mc 1 c wry "\"Oh, I don't think there's any chance of that happening.\""
    "Since I didn't eat it.\""
    show s 1 c happy at fdis
    s "\"I'm glad you liked it so much. There's a lot more downstairs. Here, I'll fill another plate for you.\""
    mc 1 c fsmile "\"Abu- Wha-\""
    "Auughh, somebody kill me already!\""
    mc 1 c considerate "\"N-no. I'm already full. I don't think I can eat anything else.\""
    show s 1 c sad at fdis
    s "\"What? But you only had two plates, right? That's not enough. You haven't eaten anything else since yesterday.\""
    mc 1 c fsmile "\"Y-Yeah, but my stomach's still kinda sensitive, so I don't want to overdo it. I'll just leave it for tomorrow.\""
    show s 1 c think at fdis
    s "\"Hmm... I suppose you're right.\""
    mc 1 c considerate "\"Why don't you have some?\""
    "Hopefully he finally realizes how awful his cooking is and I'm no longer forced to be subjected to such torture."
    show s 1 c laugh at fdis
    s "\"Nah, I made that especially for you. I bought some pre-packaged sandwiches for myself at the convenience store.\""
    "Rats."
    stop music2 fadeout 2.5
    scene BedroomN
    play music3 "music/BGM/Reminiscing.ogg" fadein 15.0
    show s 1 c happy at fdis, five
    with fade
    s "\"Hmmmm hmm hmm hmm hmmmm hmmm hmmmmm hmm hmm hmm~\""
    "Shoichi was sitting by the window, merrily humming as he absentmindedly watched the night sky outside."
    show s 1 c at fdis
    s "\"Ah.\""
    "He notices me watching him and stops what he's doing."
    "He props his knees up onto the chair and hugs them close to his body, grinning."
    show s 1 c smile at fdis
    s "\"What’cha looking so hard at?\""
    "I almost start getting flustered, but then I notice him giggling and immediately relax."
    "He's only messing with me."
    mc 1 c smile "\"Someone's awfully chipper considering the day he- the day {i}we{/i} just had.\""
    show s 1 c happy at fdis
    "He chuckles."
    show s 1 c smile at fdis
    s "\"Maybe. I'm just reminiscing.\""
    mc 1 c happy "\"Oh. Care to tell me what you're thinking of?\""
    show s 1 c happy at fdis
    "Shoichi hugs his knees even tighter, looking out of the window again, a fond smile on his face."
    s "\"Remember when we were kids and I got sick? I didn't get sick often so there aren't many times to think of.\""
    mc 1 c think "\"Hmm... There are still a few occasions that come to mind. There's was this time when both you and Hitoka got sick. There's also the time where you got sick before a championship match...\""
    show s 1 c think at fdis
    s "\"Ah, yeah, that was a bummer."
    show s 1 c smile at fdis
    extend " But the one I'm thinking of is from when we had just started Junior High. I got sick the day before one of your matches and I couldn't go cheer for you...\""
    mc 1 c "\"Ah, yeah, I remember...\""
    "Back then, Shoichi and I had just started Junior High. I was participating on a small tournament organized by the club I went to at the time."
    "Shoichi's mom showed up to cheer for me and to tell me he couldn't show up because he had Bronchitis. As soon as I heard, I just decided I had to finish my matches for the day as fast as I could."
    "I played really sloppy, but it was still enough to overwhelm the other players. In the end, I managed to finish the day's matches quite ahead of schedule."
    "I rushed to Shoichi's house without even bothering to shower just because I was so worried about him."
    mc 1 c think "\"I remember that the first thing you made me do when I came to visit was to take a shower.\""
    show s 1 c think at fdis
    s "\"Well, duh. Your friend shows up to your house smelling like a sweaty arm pit and dripping sweat. What did you think I'd do? Ask you to cuddle?\""
    show s 1 c happy at fdis
    s "\"You spent the rest of the day taking care of me. It was really nice of you.\""
    mc 1 c wry "\"Is this why you decided to drop everything and come over here today?\""
    show s 1 c considerate at fdis
    s "\"Nah. I would have come over regardless. For good or bad, that's just the kind of guy I am.\""
    show s 1 c happy at fdis
    "After he says that, we remain in a comfortable silence."
    "It's true what he said. Shoichi is the kind of person who always does anything for his friends and family. No matter what kind of sacrifices he has to make, you can always count on him to be by your side."
    "Even though I've grown used to it by now, I have a hard time understanding it sometimes."
    "As the clouds shift in the sky, the moon starts getting covered and the light begins to wane. As if on cue, Shoichi gets up from his chair and walks over to me."
    "He presses his hand against my forehand and holds the other one against his own."
    show s 1 c smile at fdis
    s "\"Your fever's gone down. That's good. I guess you should be all better by morning.\""
    mc 1 c happy "\"All thanks to you, really.\""
    show s 1 c happy at fdis
    "His hand goes from my forehead to the top of my head and he starts stroking me slowly."
    "While I'd usually be tempted to push his hand off, this time I feel comfortable enough to just sit there and enjoy the attention."
    "We stay like this for a few minutes. His warm hand softly ruffling the fur on my head is soothing. I can almost drift off to sleep right then and there."
    "Eventually, as I start to doze off whilst sitting upright, I feel a pat on my shoulder."
    show s 1 c wry at fdis
    s "\"It’s starting to get pretty late. I think you should be fine to go to class tomorrow, so it’s better if we call it a night here.\""
    mc 1 c think "\"Ah, yeah. I guess so. Are you going to head home now?\""
    show s 1 c think at fdis
    s "\"Actually, I was thinking of spending the night here if that’s okay with you."
    show s 1 c wry at fdis
    extend " It’s pretty late for me to be going home, plus I’d like to keep an eye on you for the night anyway.\""
    mc 1 c smile "\"Sure. I’ve been inviting you to spend the night for a while anyway.\""
    show s 1 c happy at fdis
    s "\"Heh. Yeah. I guess I’ll finally take you up on that offer. I'll just take a bath before I go to sleep.\""
    mc 1 c think "\"I also need to take a bath. The last time I did was before I left for school yesterday. It’s overdue already.\""
    show s 1 c laugh at fdis
    s "\"Oh, good. You noticed it on your own! I was worried I'd have to drag you to the bathroom and drown you in the tub.\""
    mc 1 c happy "\"For the record, still not the worst way to die.\""
    show s 1 c at fdis
    s "\"Really? What do you think would be worse than drowning in your tub?\""
    "Eating your soup..."
    stop music3 fadeout 5.0
    scene BedroomN with fade
    show s 1 c smile at fdis, five with moveiridis
    play music "music/night.ogg" fadein 5.0
    s "\"Oh, you've set the futon for me. Thanks.\""
    mc 1 c smile "\"It's no biggie."
    mc 1 c "\"By the way, what are you going to do about your school uniform tomorrow?\""
    s "\"I'll just wake up a little earlier than usual and head home to fetch a clean one.\""
    mc 1 c think "\"Okay. If I don't wake up at the same time as you, just take the extra copy of the keys with you when you lock the door. You can give them back to me at school tomorrow.\""
    show s 1 c at fdis
    s "\"You still plan on going?\""
    mc 1 c think "\"Well, yeah. I feel fine. Plus, I can't miss two days on a row. {i}And{/i} I need to practice.\""
    show s 1 c avoid at fdis
    "Shoichi shifts his weight around from one leg to another repeatedly, looking uncomfortable.\""
    s "\"I don't know if I like the idea of you going back to practice so soon after getting sick.\""
    mc 1 c sigh "\"Don't worry, {i}Mom{/i}. I told you, I'm already feeling fine. The only reason I was so weak was because of dehydration. Plus, I've already missed two days of practice because of the fumigation debacle.\""
    s "\"True, but..."
    show s 1 c sigh at fdis
    extend " Ah, fine. I don't want to be over dramatic or pushy. I'll just drop it.\""
    mc 1 c happy "\"{i}Thank you{/i}.\""
    "I throw myself at my bed.\""
    mc 1 c sigh "\"Ugh... I spent the entire day lying around like this. I want to actually do something.\""
    show s 1 c seductive at fdis
    s "\"Well, if you're okay with not getting any sleep and being too tired to study tomorrow, let alone practice, you could, I don't know, play video games all night long.\""
    mc 1 c happy "\"... Okay!\""
    play music2 "music/BGM/Punchline.ogg" fadein 5.0
    show s 1 c shock at fdis
    s "\"What?! {i}No{/i}!\""
    play sound "music/tap.ogg"
    "I get up, walking over to him and giving him a tap on the shoulder."
    mc 1 c laugh "\"I have to say, you really do have some great ideas every now and then.\""
    s "\"I was {i}joking{/i}!\""
    mc 1 c laugh "\"I don't care.\""
    "I start making my way downstairs."
    show s 1 c displeased at fdis
    s "\"Come back here, you've got to get to sleep!\""
    mc 1 c happy "\"Nope!\""
    scene LivingRoomN with fade
    "I make my way downstairs, turning on the lights in the living room, turning my game console on and flopping down onto the couch."
    s 1 c scorn "\"Oh, come on, you can't be serious.\""
    show s 1 c scorn at five, with moveiledis
    "Shoichi followed me downstairs, staring at the TV screen in dismay."
    s "\"[povFirstName], come on, you need to rest.\""
    mc 1 c smile "\"I've spent the entire day resting! I haven't done anything today. And it's only... 10:45?\""
    mc 1 c scorn "\"What the hell, I don't even go to sleep at 10:45!\""
    show s 1 c wince at fdis
    s "\"Neither do I, but just because you're feeling better doesn't mean you {i}are{/i} better. You still need time to recover.\""
    mc 1 c sigh "\"Shoichi, I'll be fine. Thirty minutes of playing videogames isn't going to turn me into a zombie due to lack of sleep. Stop being so fussy.\""
    show s 1 c scorn at fdis
    s "\"Wha- I'm not being fussy.\""
    mc 1 c think "\"Shoichi, hmm... I don't know how to tell you this, but... you turned into your mother.\""
    show s 1 c shock at fdis
    s "\"What?! Nooooooo. No, no no no no no no. I'm {i}nothing{/i} like my mother. She's- she's bossy, and demanding, and she fusses about every little thing.\""
    show s 1 c wince at fdis
    s "\"Oh, and her cooking, she's a {i}horrible{/i} cook. She'd come up with all these nasty concoctions that she thought would make us feel better when we were sick...\""
    show s 1 c shock at fdis
    s "\"Oh my God!\""
    mc 1 c smile "\"Yes?\""
    show s 1 c wince at shake1
    s "\"I {i}am{/i} my mother!\""
    "Shoichi sits down on the couch next to me, still gaping, massaging the sides of his head with his hands."
    mc 1 c wry "\"You alright there?\""
    show s 1 c sigh at fdis
    s "\"What? Oh, yeah yeah. It's just that... Oh God, I was trying so hard not to turn into my father, I didn't think something like this could happen!\""
    mc 1 c considerate "\"Hey, it's okay. I mean, so you're a little fussy, so what? That just means you always have your friends and family in mind, and that's sweet.\""
    show s 1 c wince at fdis
    s "\"Maybe... God, I don't even know what to say...\""
    mc 1 c wry "\"Well, you co-\""
    show s 1 c scorn at fdis
    s "\"Except I do. Screw this, let's play videogames!\""
    "He grabs the player 2 controller and sits back down on the couch with the speed of a sprint runner."
    "Well, that was... easy."
    "As I navigate the menus to put on a game for the two of us to play, Shoichi pokes me on the side of my stomach, grinning."
    show s 1 c happy at fdis
    s "\"At least I'm not a bad cook like my mom. Imagine how awful that would be."
    "...So close."
    stop music2 fadeout 5.0
    $ date = None
    jump Day7
    return
