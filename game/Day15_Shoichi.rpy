label Day15_Shoichi:
    window hide
    scene May25 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene SGateE with fade
    window show
    $ date = "day15"
    "I sit down at a nearby bench to rest after a particularly draining exercise session."
    "Even though the courts are being converted for use in the festival, Coach found us a loophole."
    "We can still do most of our aerobics training outside the courts and then just go inside the locker room to get changed."
    "This way we at least don't stay idle."
    "Some of us also take the time to practice our swings. Basically, as long as we're not using an actual ball, it's all golden."
    "The feeling of my muscles on fire has gotten so common over the years that it's almost soothing in its own way."
    "I take a chug out of my bottle of energy drink, rejoicing upon feeling the cool liquid inside my mouth."
    "Practice is the one thing that can get me to clear my mind... and these past few days I've needed to do that more than ever."
    "Coach certainly seemed pleased to see me working out with so much vigor."
    "Never mind the fact that he has no idea why I'm doing it in the first place."
    show sa 1 t smile at fdis, five with dissolve
    sa "\"How's progress?\""
    "Saya shows up while I wasn't looking and takes the seat next to mine."
    mc 1 t talk "\"I've been doing some progress on improving my backhand. I don't want it to end up being targeted again like it was in that match with Yuuya.\""
    show sa 1 t talk at fdis
    sa "\"That's the Akita you faced in the finals right?\""
    "I nod, taking another sip of my drink."
    mc 1 t sigh "\"... Man, that was tough.\""
    if yuuyawin == True:
        sa "\"I'll bet. I didn't expect to see you working that hard for a win before playing against Tanabe-kun.\""
    else:
        sa "\"I can imagine. I haven't seen anyone beating you other than Tanabe. It really caught me by surprise.\""
    show sa 1 t at fdis
    mc 1 t sigh2 "\"I don't even want to think of playing against that guy... but yeah, that's why I'm working on my backhand.\""
    mc 1 t avoid "\"It just made me realize that if a guy who knows absolutely nothing of strategy can still figure out that my backhand is an easy weakness to exploit then I need to address it.\""
    play sound "music/tap.ogg"
    show sa 1 t laugh at fdis
    "Saya gives me a few taps on the back, smiling cheerfully."
    sa "\"It's so good to see you putting in some effort again.\""
    mc 1 t sigh "\"What are you talking about? I always put effort into it.\""
    show sa 1 t at fdis
    sa "\"The fact that you're even saying that just shows how out of touch with reality you are.\""
    mc 1 t sigh2 "\"Oh, fuck off...\""
    show sa 1 t doom2 at fdis
    sa "\"Are you really gonna take that tone with me?\""
    "She cracks her knuckle as a warning and I immediately gulp."
    mc 1 t fsmile "\"I-I mean, you're right. Yeah, that's it. You're right. I've been lazing around a lot. Hahaha.\""
    show sa 1 t laugh at fdis
    sa "\"That's better.\""
    "Jesus, this girl is terrifying when she wants to be."
    show sa 1 t smile at fdis
    sa "\"Well, I should be getting ready to go home. I'm just going to give the freshmen some advice and then I'll be going.\""
    mc 1 t smile "\"See ya. Have a safe trip home.\""
    sa "\"You too.\""
    show sa 1 t smile at fdis, offscreenright with moveoridis
    "She gives me a little wave as she hops away and towards a group of freshmen that seemed to be waiting for her."
    "I'm surprised by how dutiful she is to the club."
    "I suppose she was always the responsible type, her personality just does a damn good job of masking that."
    mc 1 t sigh2 "\"Better get going too...\""
    "And now I'm talking to myself... wonderful."
    stop music fadeout 2.5
    scene SLockers with fade
    "Despite the protests of my legs, I walk towards my locker so I can get changed and go home."
    "I swear I can hear some creaking here and there with each step I take."
    "Guess I've been overdoing it a little lately."
    show s 1 v at fdis, five with dissolve
    "I see Shoichi standing in front of my locker with his arms crossed, leaning his back against the metal door."
    s "\"Ah, there you are.\""
    "I look away from him, walking right to the door and nudging him away so I can open it."
    mc 1 t worried "\"Here I am.\""
    s "\"Uhm... do you want to go somewhere together now that practice is over?\""
    mc 1 t worried "\"Don't you have to keep up with your curfew?\""
    show s 1 v think at fdis
    s "\"... I should be fine if it's just one time.\""
    mc 1 t sigh "\"Your dad will chew you out if you get home late.\""
    show s 1 v at fdis
    s "\"I know. I'm okay with that. I just want us to hang out for a bit.\""
    mc 1 t worried "\"... I think I'll pass.\""
    "I still can't even look him in the eye."
    "Every time I do I keep having those thoughts again."
    "Ever since that stupid Haruki told me all those weird things, I've been confused."
    "What's wrong with me?"
    show s 1 v annoyed at fdis
    s "\"...\""
    mc 1 t worried "\"You should probably get changed. If you stay in those sweaty clothes for too long your fur is going to stink more than it already is.\""
    s "\"Mhm...\""
    "God, this is awkward..."
    show s 1 v sigh at fdis
    s "\"Can you at least wait for me while I get dressed?\""
    mc 1 t considerate "\"I... I really am in a hurry to get home right now.\""
    show s 1 v judge at fdis
    "I'm afraid of even looking up to see what his face is like right now."
    "I wouldn't be surprised if he were really mad at me right now."
    "I know I'm being unreasonable."
    "I know I'm being obvious."
    "I'm just weaseling out of an uncomfortable situation without doing anything about it."
    "I know that."
    "But..."
    "I don't even know what's happening to me right now."
    "If I do or say the wrong thing... I could potentially ruin my friendship with him."
    "... And the thought of that alone already terrifies me."
    show s 1 v displeased at fdis
    s "\"...\""
    show s 1 v displeased at fdis, offscreenleft with moveoledis
    "Without saying another word, Shoichi walks away from me."
    "He's probably gone to get changed."
    "I take this opportunity to finish getting changed myself."
    "As fast as I can so I can get out of here..."
    scene SGateE with fade
    "Before I noticed, I had already zoomed out of the door with my bags hanging from my shoulder."
    "I should probably be in the clear for now."
    "Ugh... I'm not being normal lately... and it's only been getting worse these past couple weeks."
    "So many things just started clicking into place lately... things I never even had a second thought about suddenly seem so suspicious."
    "I hate it..."
    play sound "music/tap.ogg"
    "All of a sudden I feel a hand firmly grabbing me by the shoulder and stopping me as I walk."
    show s 1 c displeased at fdis, five with moveiridis
    "I'm spun around where I stand and am greeted to Shoichi."
    "His face looks incredibly annoyed and angry."
    "My eyes instinctively go down to my feet."
    s "\"You're coming with me.\""
    mc 1 c flustered "\"S-Shoichi, I really need to-\""
    show s 1 c scorn at fdis
    s "\"That's not optional!\"" with hpunch
    "He grabs me by my wrist and starts pulling me back towards the school building."
    mc 1 c shockb "\"W-wait, Shoichi!\""
    "He doesn't give an ear to my complaints and forcibly drags me away without a word."
    scene SRooftopE
    play sound "music/metaldoor.ogg"
    play music "music/breeze.ogg" fadein 5.0
    show s 1 c annoyed at fdis, five
    with fade
    "The metal door closes behind me with a loud bang as Shoichi nearly slams it shut."
    "For some reason, he's dragged me towards the rooftop."
    s "\"Talk to me.\""
    mc 1 c avoid "\"I... talk about what?\""
    show s 1 c scorn at fdis
    s "\"For God's sake. Do you think I'm stupid or something? You've been ignoring me all week. How about you start with that?\""
    mc 1 c considerate "\"I... I don't know what you're talking about. That's ridiculous.\""
    show s 1 c sigh at fdis
    s "\"Come on, do you really think I'm that dumb? You've been ignoring me ever since you spent the night at my place.\""
    show s 1 c annoyed at fdis
    s "\"You barely talk to me when we're together with everyone else. You actively go out of your way to avoid spending time alone with me.\""
    show s 1 c scorn at fdis
    s "\"You don't answer your phone, you don't text back. You're not slick. It's pretty damn obvious that you're avoiding me.\""
    mc 1 c worried "\"That's...\""
    show s 1 c sigh at fdis
    s "\"Look, [povFirstName]... I don't know what happened but... I'm sorry, alright?\""
    mc 1 c shock "\"H-Huh?!\""
    play music2 "music/BGM/Reminiscing.ogg" fadein 5.0
    show s 1 c avoidb at fdis
    s "\"I... maybe I was too hard on you because of that thing with my sister. I know you meant well and I'm sorry I got so-\""
    mc 1 c wince "\"{size=+4}No!{/size}" with hpunch
    extend " That's... that's not it at all.\""
    show s 1 c considerate at fdis
    s "\"I see... Look, I might not know what it is but... Whatever it is I did, I'm sorry.\""
    mc 1 c shock "\"W-why are you apologizing to me? If you don't even know what happened...\""
    show s 1 c wry at fdis
    s "\"Because some things are more important to me. Getting ignored by you hurts. You have no idea how much it hurts.\""
    show s 1 c considerate at fdis
    s "\"So it doesn't matter to me what I did or didn't do... if it means you'll stop ignoring me, I'll apologize however many times I need to.\""
    play sound "music/heartbeat.ogg"
    "..."
    "I'm speechless."
    "My chest suddenly feels really tight."
    mc 1 c worried "\"Stop it... You don't have to apologize. It's nothing you did...\""
    show s 1 c sad at fdis
    if povFirstName == "Yuuichi":
        s "\"Then what is it, Yuu?\""
    else:
        s "\"Then what is it, [povFirstName]?\""
    "..."
    "I can't think of any words."
    "Seeing the look on his face makes my chest hurt even more for some reason."
    "Not being able to bear it, I look away from him."
    show s 1 c wry at fdis
    s "\"There you go again... You're not even looking at me.\""
    mc 1 c worried "\"That's not...\""
    s "\"It has to be something. Come on. Just tell me... please...\""
    "Why is he saying this?"
    "Why is he being so sweet and understanding?"
    "If he realizes what I've been doing then why isn't he mad at me?"
    "Why is he only making me feel more confused?"
    if povFirstName == "Yuuichi":
        s "\"... Yuu?\""
    else:
        s "\"... [povFirstName]?\""
    "Shoichi calls my name out one more time."
    "He sounds so strained. As if he's already nearing his breaking point..."
    "Seeing him like this... hearing him call my name like this..."
    "{cps=10}Why does it make my chest hurt so much?{/cps}"
    mc 1 c worried "\"I... I've just been really confused... and worried lately... Even before the party thing.\""
    show s 1 c wince at fdis
    s "\"What do you mean?\""
    mc 1 c worried "\"I'm just... unsure about how... how you feel for me...\""
    "Even though I've wanted to keep quiet about this, before I notice it, the dam inside of me bursts."
    show s 1 c shock at fdis
    s "\"W-what? What's that even supposed to mean?\""
    "I swallow one. Two. Three times in an attempt to get the words to come to me."
    "I decide to leave out the part with Haruki because I don't know how he'd react..."
    "The last thing I need right now is for him to get into a fight with someone over that."
    mc 1 c worried "\"It's just... I've noticed a lot of the things you do or say to me... aren't the kinds of things you do for... for just anyone...\""
    mc 1 c flustered "\"And... and once I realized that... A lot of the things you've done for me in the past... I started seeing them in a different light...\""
    mc 1 c flustered "\"And I don't know anymore whether... whether you think of me as a friend or...\""
    "My voice trails off before I can finish that last sentence."
    "No... it's more like I can't bring myself to finish that sentence."
    "Because it's the last step."
    "After I open this door, there's really no coming back."
    "Even if he can piece together what I'm trying to say from all this... even though I know that wouldn't be hard at all for him to do..."
    "I still can't bring it to words."
    "Because whether my suspicions turn out to be correct or not..."
    "Voicing them out loud would just change everything..."
    show s 1 c avoidb at fdis
    s "\"...\""
    mc 1 c worried "\"... Shoichi?\""
    "His eyes dart to the floor, looking away from my gaze."
    "His face is... red?"
    "Something clicks inside of my head."
    "I realize that... he can't deny it."
    "The reason he can't look at me is because he cannot deny it."
    mc 1 c worried "\"Shoichi... now you're the one avoiding {i}me{/i}.\""
    show s 1 c considerate at fdis
    s "\"Sorry... It's just that you really caught me by surprise...\""
    show s 1 c wry at fdis
    s "\"... So you noticed before I had the chance to tell you, huh? Man, I really hate myself for letting that happen.\""
    play sound "music/heartbeat.ogg"
    "!"
    "Even though I already knew it... hearing it said in actual words makes my heart skip a beat."
    "Why... why is my heart beating so fast?"
    "Why is it that I... somehow feel happy to hear it?"
    "What's... what's going on with me?"
    mc 1 c flustered "\"So... so it's true...\""
    show s 1 c avoidb at fdis
    s "\"Yes... I'm sorry..."
    if day5 == "shoichi":
        show s 1 c considerate at fdis
        extend " To be fair... I did try telling you before... But you didn't hear me that time.\""
        mc 1 c shockb "\"What?\""
        show s 1 c wry at fdis
        s "\"Heh... So you pieced all of this together but totally forgot that other time? When we went to the festival and were hiding from the rain in that alley at night...\""
        play sound "music/flashback.ogg"
        show AlleyNight behind s
        show s 1 c flattered at fdis
        with flash
        s "\"I... you.\""
        play sound "music/flashback.ogg"
        hide AlleyNight
        show s 1 c wry at fdis
        with flash
        "..."
        mc 1 c shockb "\"I... I can't...\""
        show s 1 c considerate at fdis
        s "\"Jeez... it's just like you to be this dense.\""
        mc 1 c flustered "\"...\""
        show s 1 c avoidb at fdis
    else:
        show s 1 c sad at fdis
        extend " I've wanted to tell you for so long, but... I just... I was so afraid of how you'd react.\""
        show s 1 c avoidb at fdis
        s "\"I was afraid you'd hate me...\""
        mc 1 c worried "\"Shoichi, I never... I...\""
    s "\"So this is why you've been avoiding me this past week... you figured it out...\""
    mc 1 c avoidb "\"Yeah...\""
    show s 1 c wryt at fdis
    s "\"... You're probably disgusted by it, huh?\""
    mc 1 c shockb "\"W-what?\""
    s "\"It's okay, I'll... I'll leave you alone. You don't have to say anything...\""
    "The sound of Shoichi choking on his words as he says them breaks my heart."
    hide s 1 c wryt with dissolve
    "He turns around and begins to leave."
    mc 1 c shockb "\"Wait!\"" with hpunch
    play sound "music/tap.ogg"
    show s 1 c shock at fdis, five with dissolve
    "Before he can walk away from me, I reach out and pull him back."
    "I don't know why but my body just moved on its own."
    mc 1 c angry "\"Don't just decide how I'm supposed to feel without even letting me talk, damn it!\"" with hpunch
    "The words come out of my mouth before I even notice it."
    mc 1 c worried "\"Ah... I'm sorry, I didn't mean to yell...\""
    show s 1 c considerate at fdis
    s "\"... It's alright.\""
    "Shit... My mind is drawing a blank."
    "Say something..."
    "Just say something!"
    show s 1 c wry at fdis
    s "\"I should pro-\""
    mc 1 c flustered "\"Wait! Just... just let me collect my thoughts...\""
    "Shoichi nods, pulling away his arm that I'm still clutching in my right hand."
    show s 1 c wryt at fdis
    s "\"Okay... Just say what you have to say.\""
    play sound "music/heartbeat.ogg"
    "Ah... how am I supposed to think straight when he's looking at me like that?"
    "Even though he's smiling and trying to put on a brave face... he's crossing his arms so tightly around his body that his hands are shaking."
    "Just seeing this I already know what he's thinking."
    "{cps=10}He's preparing himself to be rejected.{/cps}"
    mc 1 c flustered "\"I've been very confused lately... about my own feelings.\""
    show s 1 c shock at fdis
    s "\"What?\""
    "I see his hands relaxing for only a split-second."
    "Collecting every shred of courage I have, I swallow one last time before speaking."
    mc 1 c avoidb "\"Ever since I realized... {i}this{/i}... about you, I've just... been thinking about it all the time.\""
    mc 1 c flustered "\"I just... can't get it out of my head. I can't get {i}you{/i} out of my head. I've even had dreams about you and I don't know why. My chest hurts right now and I don't know why.\""
    mc 1 c avoidb "\"I... don't know what's going on with me...\""
    show s 1 c at fdis
    s "\"...\""
    "He's oddly silent right now."
    "The things I just said... it sounds oddly like a confession now that I think about it..."
    "But I don't even know what I'm trying to say anymore."
    "The inside of my head is so jumbled up that I feel so lost..."
    show s 1 c flattered at fdis
    s "\"Pfft... hahahaha!\""
    mc 1 c shockb "\"Wha- Shoichi?!\""
    s "\"Sorry, sorry. I... I know I shouldn't be laughing right now.\""
    show s 1 c wry at fdis
    s "\"[povFirstName]... I think you might have a crush on me.\""
    mc 1 c flustered "\"I... I do?\""
    show s 1 c flattered at fdis
    s "\"Jeez, you're so slow on the uptake. How can you not notice it yourself?\""
    mc 1 c avoidb "\"I don't know... is this really it? I've... never had romantic feelings for anyone before... I don't know what it's supposed to be like...\""
    mc 1 c flustered "\"I guess... I'm a bit... curious?\""
    "I don't want to accept it but this is pretty much what that wolf told me."
    "God, I wanted him to be wrong just out of spite..."
    mc 1 c flustered "\"Do I... really have a crush on you?\""
    show s 1 c considerate at fdis
    s "\"Beats me.\""
    mc 1 c shockb "\"What? But you just said-\""
    show s 1 c wry at fdis
    s "\"Come on. How am I supposed to tell you what {i}you{/i} feel? I'm not a mind reader.\""
    show s 1 c considerate at fdis
    s "\"Besides, you already know that I have feelings for you. It would be at the very least very suspect if I tried to convince you that you have feelings for me, no?\""
    mc 1 c avoidb "\"I... I guess...\""
    "Shoichi reaches out with his hand, tenderly brushing it against my cheek."
    show s 1 c wry at fdis
    s "\"Do you feel better after getting it out in the open?\""
    mc 1 c avoidb "\"Not really. I'm still confused... what about you?\""
    show s 1 c flattered at fdis
    s "\"I... I feel so relieved.\""
    mc 1 c flustered "\"Really?\""
    show s 1 c wry at fdis
    s "\"Yeah. You have no idea how scared I was of your reaction. I thought for sure I'd lose you if you ever found out. I've been carrying these feelings and this fear for years.\""
    mc 1 c flustered "\"Y-years?\""
    show s 1 c flattered at fdis
    s "\"Yeah...\""
    show s 1 c avoidb at fdis
    s "\"... Please, let me say this properly for once...\""
    "Shoichi's hand grasps mine..."
    "I swallow loudly in anticipation and then nod."
    show s 1 c blush at fdis
    if povFirstName == "Yuuichi":
        s "\"Yuu... I love you. I've loved you since we were kids.\""
    else:
        s "\"[povFirstName]... I love you. I've loved you since we were kids.\""
    play sound "music/heartbeat.ogg"
    mc 1 c shockb "\"I... Ah...\""
    "I choke on my words, unable to come up with something to say."
    show s 1 c wry at fdis
    s "\"Yeah?\""
    mc 1 c avoidb "\"I... I don't know... I don't even know if I really have a crush on you and... and now love? I...\""
    show s 1 c considerate at fdis
    s "\"Don't worry about it. I've had feelings for you for the longest time."
    show s 1 c wry at fdis
    extend " They've had more than enough time to develop and reach this point... while you've only been thinking of me recently. If you do have feelings for me at all, I don't expect them have reached that point.\""
    "He's being so... so understanding."
    "My heart is beating so fast... I've never felt this way before."
    mc 1 c avoidb "\"I don't know what to do... I don't know how to be sure...\""
    show s 1 c smile at fdis
    s "\"I can think of one way to be sure.\""
    mc 1 c avoidb "\"What do you m-\""
    play sound "music/fabric.ogg"
    show cg5_1 with Dissolve(1.0)
    "Before I can wrap my head around what is going on, Shoichi puts his arm around my waist and pulls me closer to him."
    "My hand instinctively goes for his chest to keep us from bumping together."
    "That's when he wraps his other hand around mine... gently stroking the back of my hand with his fingers."
    "He gets so close to me that our noses touch... I can feel his breathing on my face."
    "My mind immediately goes blank... everything else seems to disappear from my sight."
    "The only thing I can properly see is Shoichi right in front of me."
    s2 "\"How about this?\""
    "He looks down at me, his big green eyes staring right into me, sparkling with so much life that I can feel myself getting lost in his gaze..."
    "It's at this moment, with him cradling me so close to him that I can finally feel the enormity of his affection for me."
    "My heart speeds up even faster, so fast that I'm afraid it's going to burst."
    "But I also notice one other thing..."
    mc 1 c zero "\"Your heart's beating really fast...\""
    "Shoichi chuckles, pressing his nose a little closer to mine."
    "The tip of his nose is warm and fuzzy... and having it this close to me makes my face feel hot."
    s2 "\"Of course it is. Look at the position I'm in. There's no way I wouldn't be nervous right now.\""
    mc 1 c zero "\"I have a hard time imagining you being nervous... You look so confident most of the time.\""
    s2 "\"Heh... thanks for having so much faith in me. Right now though... right now I'm terrified. Just feel it for yourself.\""
    "Shoichi squeezes my hand, pushing it even harder against his chest."
    play sound "music/heartbeat2.ogg"
    "I can feel his heart beating rapidly against his chest... maybe even faster than my own."
    mc 1 c zero "\"Ah...\""
    s2 "\"See?\""
    "He smiles at me and that immediately makes me melt."
    mc 1 c zero "\"Sho...ichi...\""
    "I can't even seem to form words at this moment."
    "My brain is swimming in so much white that I feel as if I'm about to crash."
    s2 "\"Would you... let me go one step further?\""
    "My mouth feels so dry right now."
    "I'm flashing back to that dream I had last week... and that I have been thinking of since then."
    "I feel like my heart's about to stop."
    "Still, silently, I nod."
    "Shoichi leans a little closer to me..."
    scene Black with fade
    "I close my eyes."
    stop music2 fadeout 10.0
    stop music fadeout 10.0
    show cg5_3:
        subpixel True
        yalign 1.0
        linear 0.7
        linear 12.0 yalign 0.25
    play sound "music/chu.ogg"
    "..."
    "That's when I feel something warm and moist gingerly pressing against my lips."
    "Shoichi's touch is gentle, almost fleeting."
    "It's almost as if he's holding himself back out of fear he'd make me flee."
    "My body, however, immediately reacts to this situation."
    "I press into the kiss..."
    play music3 "music/BGM/I Want to Know You.ogg" fadein 5.0
    show cg5_2 with Dissolve(2.0)
    "For a second, I truly believe that my heart has stopped."
    "I can't hear anything... I can't see anything..."
    "All I have is the feeling of Shoichi's lips against mine."
    "In that moment, for some reason, I feel like I can truly let go of my worries."
    "I accept his kiss and his embrace and just let myself do what comes naturally to me."
    "My heart sings in joy... a joy I've never felt before."
    "This is... my first kiss with my best friend..."
    "And yet it doesn't disgust me at all."
    "I truly feel like I belong here."
    "Nothing has ever felt so right for me before..."
    scene SRooftopE
    show s 1 c flattered at fdis, five
    with fade
    "That's when Shoichi pulls away from me."
    "I immediately miss the feeling of his body pressed up against mine."
    "When I realize that I miss it, I suddenly feel really self-conscious and embarrassed."
    "Though I imagine it can't be too different for him, since Shoichi's face is still bright red."
    mc 1 c flustered "\"That... that was...\""
    show s 1 c smile at fdis
    s "\"Would it be too cliche if I said it was everything I'd hoped it would be?\""
    mc 1 c avoidb "\"Uaah... that's... really embarrassing to hear...\""
    show s 1 c flattered at fdis
    s "\"Hehe. You're really cute when you're embarrassed though.\""
    show s 1 c wry at fdis
    s "\"But... uhm... how did it feel for you?\""
    "I have a hard time putting it to words... or at least speaking the words I think out loud."
    "I can't help but feel embarrassed."
    "I mean... this is Shoichi I'm talking about."
    "To suddenly be talking about this kind of thing with him... {i}about{/i} him..."
    "It's embarrassing..."
    mc 1 c avoidb "\"I... I think we're good to... give it a try.\""
    show s 1 c shock at fdis
    s "\"You mean... give dating a try?\""
    mc 1 c avoidb "\"Y-yeah...\""
    "Oh man, my face feels so hot right now."
    play sound "music/fabric.ogg"
    show cg5_1 with Dissolve(1.0)
    "Shoichi immediately pounces me, wrapping me in another tender hug."
    mc 1 c zero "\"Waah, S-Shoichi!\""
    s2 "\"Sorry. It's just... you have no idea how happy it makes me to hear you say that.\""
    "He might think I have no idea but... the speed with which his heart is beating is already a dead giveaway."
    mc 1 c zero "\"Oh man, this is so embarrassing...\""
    s2 "\"Hehe, I'll bet. I've had a lot longer to get used to the idea than you did. It's okay if it feels weird for you for a while.\""
    mc 1 c zero "\"... I never said it felt weird though.\""
    s2 "\"Hehe...\""
    if povFirstName == "Yuuichi":
        s2 "\"Hey, Yuu?\""
    else:
        s2 "\"Hey, [povFirstName]?\""
    mc 1 c zero "\"Yeah?\""
    s2 "\"I know you're not ready to say it back... and I don't want you to feel pressured to do it. I don't even know if we'll ever get to a point where you will be, but...\""
    s2 "\"Right now, because I've been holding back for so many years, I just want to say it again.\""
    s2 "\"I love you.\""
    "The sun's light shining on his face causes his eyes to seem like they're twinkling... it makes everything seem so much more real..."
    "The intensity of his feelings is so much that I blush and look away."
    "It's so embarrassing."
    mc 1 c zero "\"... You idiot.\""
    s2 "\"Hehe. Yeah, I'm an idiot... And I can be {i}your{/i} idiot. You just have to ask me to be.\""
    mc 1 c zero "\"{cps=5}... Yeah.{/cps}\""
    play sound "music/fabric.ogg"
    show cg5_4 with Dissolve(1.0):
    "I curve my body forward, resting my forehead on his neck."
    "At least for right now, none of this feels wrong."
    "At least for right now, for the first time in over two weeks, my mind isn't racing with ideas and worries anymore."
    $ date = None
    stop music3 fadeout 2.5
    jump Day16_Shoichi
