label shoichistart_1:
    $ uihide = True
    stop music2 fadeout 2.5
    $ shoichihearts += 1
    scene SRooftop with fade
    play music "music/breeze.ogg"
    "Once more, I come up to the roof to take some time for myself."
    "As usual, this is the best place on campus to just lie down and nap."
    "?!"
    "Wait, there's someone else here!"
    show h 1 u at five with dissolve
    "A white wolf is sitting on the floor, lazily looking up at the sky."
    if jun_met == False:
        "I recognize him right away."
        "He's the wolf from the volleyball club that Shoichi got into a scuffle with last month."
        "He's the guy Shoichi punched."
    else:
        "I don't remember ever seeing him before."
        "Even if I don't know them all by names, I am at least familiar with all the seniors in school."
        "Maybe this guy is a junior? Or even a freshman?"
    "As I stand on my spot watching him and trying to decide whether to stay or leave, the wolf speaks up."
    h "\"Are you going to stand there and gawk at me all day?\""
    "His tone isn't the friendliest I've ever heard, which further makes me unsure."
    "The wolf turns his head towards me, looking me in the eye."
    h "\"Didn't think I'd run into you here.\""
    mc 1 u curious "\"You know who I am?\""
    h "\"Of course I do. You're the guy that the captain is always fawning over.\""
    if jun_met == False:
        "He must mean Shoichi."
        mc 1 u annoyed "\"And you're the one who got into a fight with Shoichi back in April. K-Kisada... Koshiumi...\""
        "The wolf sighs."
        h "\"It's Koizumi. And I didn't expect you to remember my name either way. I'm surprised you even remember what happened.\""
        mc 1 u "\"It's not every day that someone tries to attack one of my friends.\""
        h "\"Point taken.\""
        "The corners of his lips curve upwards."
        "The wolf, Koizumi, gets up and dusts himself off."
    else:
        mc 1 u curious "\"The captain?\""
        h "\"Heh. Figures you wouldn't know me. I've seen you visit our courts a ton of times since I joined but you never bothered to learn who we are.\""
        mc 1 u shock "\"Ah, wait. Are you one of Shoichi's teammates?\""
        "One of his eyebrows twitches."
        h "\"Teammate... I guess you could call it that.\""
        "The wolf gets up from the floor and dusts himself off."
    h "\"Yeah, I'm one of his teammates. Although I doubt he even cares about people like me at all.\""
    mc 1 u shock "\"W-wha? What do you mean? Shoichi cares about everyone on his team!\""
    "The wolf scowls, crossing his arms."
    h "\"As if I'd believe in some pretty little fairytale like that. If he cared so much then he wouldn't always act so high and mighty towards us.\""
    mc 1 u wince "\"H-high and mighty?\""
    h "\"Yeah. All he cares about is improving himself. He doesn't care if other people can't follow him, he just leaves everyone behind without a second thought.\""
    h "\"Pushing everyone so hard past their limits that they quit, forcing us to take tosses that we have no way to deal with.\""
    h "\"Must be nice being a genius. You don't have to worry about anyone else beneath your station. He really is a volleyball idiot.\""
    "!"
    mc 1 u annoyed "\"Those words... you will take them back right now.\""
    h "\"Huh?\""
    "The wolf pushes his hands into his pockets, leaning back with a smug smile on his face."
    h "\"Ooh, don't tell me I've managed to upset you? Pfft, you guys really are all birds of a feather. Let me guess, the little genius here is feeling sore because the bills fit him too?\""
    h "\"Just so you know, I've been watching the captain very closely since I first joined this school. I know a lot about him and I know about you too. I know for a fact that everything I just said is the truth.\""
    mc 1 u annoyed "\"And yet you call him a genius? Is that a word you like to use so you don't have to admit to the fact that you never even bothered to try?\""
    "His posture immediately shifts, the fur on the back of his neck bristling up and his eyes closing partly, giving him a very dangerous look."
    h "\"What did you just say?\""
    mc 1 u cocky "\"I just find it funny that you'd say you've been watching him all this time and yet you'd call him a genius. You say that he's a genius and that's why you can't keep up with him?\""
    mc 1 u annoyed "\"You're just trying to push the responsibility over your own weakness onto someone else, aren't you?\""
    "For a second I'm afraid I might have said too much."
    "I can't help but get heated up when I hear people talking badly about my friends and I might have ended up saying too much."
    "But I also absolutely refuse to back down after everything he's said."
    "Surprisingly enough, the wolf's gaze softens. He stares at me with a look of derision and disgust."
    h "\"Heh, you've got quite a mouth on you, huh. You two really are alike.\""
    mc 1 u annoyed "\"What's that supposed to mean?\""
    h "\"He also got really heated up when I talked smack about you back then.\""
    if jun_met == False:
        "Wait... back then?"
        mc 1 u shock "\"Do you mean... when you and Shoichi got into that fight?\""
        "His smile widens."
        h "\"Oh, he never told you? The bastard was completely fine with me insulting him and his stupid little team. But you should have seen his face when I started talking about you. He went completely berserk.\""
        "W-what? He never told me that."
        mc 1 u shock "\"Are you saying that Shoichi hit you because of me?!\""
        "There it is. The look on his face is that of absolute satisfaction."
        "As if he had finally reached the point he had been looking for."
        h "\"Yeah. You should have seen him. As soon as I opened my mouth to insult you, he was like a white knight riding to your rescue. Seriously, that guy is so obsessed with you... it's disgusting.\""
        "W-what? He's obsessed with me? Since when?"
        mc 1 u shock "\"W-what are you talking about?\""
        "Koizumi scowls."
        h "\"Jesus, how do you manage to operate when you're this dense?\""
    else:
        mc 1 u curious "\"Back then? What are you talking about?\""
        h "\"Oh, you didn't know? The captain and I got into a fight last month. He nearly broke my nose, too. Damn thing kept bleeding for hours.\""
        mc 1 u angry "\"W-what?! No way. No way Shoichi would hit someone. You're lying!\""
        h "\"Tch, suit yourself. I'm only telling you what happened. If you find it that hard to believe then ask him about the guy he punched back in the first day of class.\""
        "The wolf smiles haughtily."
        h "\"I'm actually kinda curious about it. He's always so damn concerned with acting like the perfect person. I wonder, what would he consider the bigger sin? Admitting to have assaulted someone or lying about it?\""
        h "\"He's so damn obsessed with you that I'm sure he'd consider either one of those to be an unacceptable blow to your image of him.\""
        "T-this guy... I feel every nerve in my body screaming at me to slug him."
        "But I have to keep my cool. I'm sure he's only provoking me because he wants me to do it."
        mc 1 u annoyed "\"I don't know about anything like that. And since when has Shoichi been obsessed with me? Now you're just making up stories to try and cause some strife? How pathethic are you?\""
        "His eyes contracted again. I could see his fists shaking through the pockets in his pants."
        "Two can play this game."
        "The wolf takes a deep breath, stabilizing himself."
        "I can already see that this guy has temper problems."
        h "\"You say he's not obsessed, huh? Of course, you'd really have to be dense not to notice. I'm surprised you can even function normally like that.\""
    mc 1 u annoyed "\"W-what?\""
    "The wolf walks towards me."
    "I fully prepare myself in case he tries to hit me."
    "If he even attempts to, I'll- ?!"
    "He gently places a hand on my chin, lifting my face up to look him in the eye."
    "His eyes are much softer than before and brimming with curiosity."
    h "\"You know, I've always been curious. I never understood what it is that the captain sees in you.\""
    mc 1 u curious "\"Huh? W-what Shoichi sees in me?\""
    "What's this guy talking about?"
    h "\"Hmm... I guess you're kinda good looking. Could that be it? I don't think he's that shallow though... What's so good about you anyway?\""
    "I'm left completely astonished."
    "His sudden gentleness is so unexpected that I'm left without a reaction."
    "Then he leans in..."
    label kisstimed:
    $ time = 0.7
    $ timer_range = 0.7
    $ timer_jump = 'kiss_timeout'
    show screen countdown
    menu:
        "Push him away!":
            hide screen countdown
            $ harukiss = False
            "My body immediately reacts, pushing the wolf away."
            "He hits the wall behind him, painfully rubbing his head."
            h "\"You little-\""
            "He takes another step towards me, his fists clenched."
            "Just as I begin fearing the worst."
            play sound "music/metaldoor.ogg"
            show h 1 u at three with move
            show s 1 u at fdis, seven with dissolve
            $ renpy.pause(1.0)
            show s 1 u shock at fdis
            s "\"[povFirstName]? Koizumi? What are you two-\""
            "The wolf composes himself again, putting both hands back into his pockets and staring at Shoichi with a cold glare."
            h "\"Captain... you really are on time.\""
            mc 1 u wince "\"O-on time?\""
            show s 1 u at fdis
            s "\"Yeah. I called Koizumi to meet me up here since Coach asked me to talk to him about something."
            "!"
            "Wait... did he try to kiss me on purpose so Shoichi would walk in on us?"
            mc 1 u shock "\"Y-you... you tried doing that so Shoichi would see us?!\""
            show s 1 u scorn at fdis
            s "\"Doing {i}that{/i}? What's {i}that{/i}?\""
            "A cocky smile appears on the wolf's face as he stares us both down, acting so incredibly high and mighty."
            h "\"That's none of your business.\""
            s "\"Whaaat?!\""
            h "\"What I do on my free time is none of your business.\""
            s "\"What you do to [povFirstName] is my business. I already told you to stay away from him!\""
            mc 1 u shock "\"Wait, you did what?!\""
            show s 1 u wince at fdis
            "Shoichi's ears immediately fold as he realizes the words he just spoke."
            "The wolf's smile widens in satisfaction."
            h "\"See. I told you this guy is completely obsessed with you. He even goes around telling people not to go anywhere near you.\""
            show s 1 u scorn at fdis
            s "\"Wha- Haruki, that's not-\""
            mc 1 u annoyed "\"Shoichi, you've been telling people to stay away from me?!\""
            show s 1 u wince at fdis
            s "\"N-no, that's not...\""
            "The wolf laughs."
            h "\"Goddamnit, you two are so pathetic. Enjoy your time together. I'm out.\""
            "He begins walking towards the door."
            play sound "music/tap.ogg"
            show s 1 u scorn at fdis
            s "\"Hang on there, Haruki. You and I still need to talk!\""
            h "\"Let go.\""
            "The glares at Shoichi, his eyes shoot daggers at the both of us."
            show s 1 u wince at fdis
            "Surprisingly, Shoichi hesitates."
            "The wolf uses this one second to pull away."
            show s 1 u shock at fdis
            h "\"See you at practice. Remember to take breaks during your make out session to breathe.\""
            show h 1 u at offscreenright with moveoridis
            show s 1 u avoid at fdis, five with move
            play sound "music/metaldoor.ogg"
            "..."
            show s 1 u displeased at fdis
            s "\"Are you alright, [povFirstName]?\""
            mc 1 u worried "\"I'm... I'm fine. He was just being an ass.\""
            "Somehow, I don't think I should tell Shoichi that the guy tried to kiss me."
            "He'd probably just get more upset."
            show s 1 u avoid at fdis
            s "\"Yeah. Being an ass is his specialty. Coach asked me to talk to him about that today.\""
            show s 1 u sigh at fdis
            s "\"Goddamnit, why does he always have to make everything so difficult?\""
            jump afterkiss
    label kiss_timeout:
        $ harukiss = True
        "Before I can muster a reaction, I feel something soft and moist touching my lips."
        "My body immediately tenses up, frozen in place."
        "The wolf continues to hold my chin up with his fingers, putting his other hand on my waist and clenching it tightly."
        "Somehow, even though my mind is shorting out, I know that I'm supposed to push him away."
        "But my body refuses to answer."
        play sound "music/metaldoor.ogg"
        "The sound of the door echoes and I hear someone taking a few steps before stopping."
        show h 1 u at three with move
        show s 1 u shock at fdis, seven with moveiridis
        "The wolf's lips pull away from mine, looking for the source of the sound."
        "I myself turn around just in time to see Shoichi standing frozen in the doorway."
        mc 1 u shock "\"S-Shoichi?!\""
        h "\"Hey, there, captain. What brings you here?\""
        "The wolf's tone of voice is clearly pleased, almost mocking him."
        show s 2 u rage at fdis, four with move
        play sound "music/tap.ogg"
        "Shoichi lunges at the wolf, grabbing him and pushing him away from me."
        s "\"Haruki, what the hell were you doing with [povFirstName]?!\""
        "Shoichi's face is contorted in a look of pure hatred, with so much rage in his eyes that I myself feel a slight twinge of fear."
        "The wolf merely smiles mockingly."
        h "\"What, are you blind? What did it look like we were doing? We were kissing. You have a problem with that?\""
        "Shoichi clenches his fist, lifting an arm up in the air an-"
        mc 1 u shock "\"Shoichi, stop!\""
        play sound "music/tap.ogg"
        "I grab his arm from behind, trying to pull him away from the still smiling wolf."
        s "\"Let me go, [povFirstName]! Let me go!\""
        "Goddamnit, he's way too strong for me."
        h "\"Jeez, are you that upset that I got to your precious [povFirstName] first? If you're going to be that jealous then you should just con-\""
        play sound "music/punch.ogg"
        s "\"{size=+4}SHUT UP!{/size}\"" with hpunch
        play sound "music/fall.ogg"
        "Shoichi's arms flies out of my grasp and his fist lands squarely into the wolf's face, knocking him down."
        play sound "music/tap.ogg"
        "I grab Shoichi as he tries to throw himself down on top of the guy."
        mc 1 u wince "\"S-Shoichi, stop it! Stop. Get off of him!\""
        s "\"Goddamnit, [povFirstName], let go of me! Let go of me!\""
        "I have to wrap both of my arms around his waist and put all of my body weight to try and pull him away."
        mc 1 u wince "\"Stop! If you do anything else to him you might get expelled!\""
        s "\"I don't care!\""
        "The wolf puts one of his feet on Shoichi's stomach, pushing him away."
        "He gets up from the floor, rubbing his bloodied nose."
        h "\"Jeez, you really are an animal. What do you even see in this guy? He's not even a good kisser.\""
        "Even though he's bleeding from his nose and from his lip, he still stares at Shoichi with cold, defiant eyes."
        h "\"Whatever. Jeez, I don't understand what the fuss is all about. You two are so weird.\""
        "He walks to the door while I hold Shoichi and keep him from going after the wolf again."
        h "\"See you at practice, captain. You two weirdos enjoy yourselves.\""
        show h 1 u at offscreenright with moveoridis
        show s 2 u rage at fdis, five with move
        play sound "music/metaldoor.ogg"
        "..."
        show s 1 u blank at fdis
        "Just as soon as he leaves, Shoichi's body goes slack, falling butt first to the floor and dragging me with him."
        "We both sit there in silence for a few seconds, my hands still wrapped around his waist."
        s "\"Are you alright?\""
        mc 1 u worried "\"I'm fine.\""
        "..."
        s "\"Did he... he didn't hurt you, did he?\""
        mc 1 u sigh "\"The only thing hurting right now is my pride.\""
        "Did that guy... did he really just kiss me out of the blue?"
        "Why?"
        s "\"... What were you two doing up here together?\""
        mc 1 u shock "\"Huh?\""
        show s 1 u scorn at fdis
        "Shoichi gets up, turning around to look at me."
        s "\"I asked what were you two doing up here together!\""
        mc 1 u shock "\"Wha- I came up here to take a nap and he was already here. Then he started taunting me an-\""
        s "\"Then why the hell were you kissing when I walked in?!\""
        mc 1 u shock "\"Wha- Wait, Shoichi, you don't think I was kissing him because I wanted to?\""
        s "\"It's not like not kissing someone is that hard. You just don't kiss them! If you really didn't want to then why were you-\""
        mc 1 u angry "\"Do you really think I'd just kiss a complete stranger?!\"" with hpunch
        show s 1 u shock at fdis
        $ renpy.pause(1.0)
        show s 1 u avoid at fdis
        s "\"... No.\""
        "... I don't get it."
        "I... I'd understand him being upset if the guy had assaulted me."
        "Well, technically he did, but..."
        "Why is he so upset at me? All he seems to care about is whether or not I kissed the guy?"
        "I don't get it!"
        mc 1 u worried "\"Shoichi, are you alright?\""
        s "\"I'm fine.\""
    label afterkiss:
        "..."
        "For some reason, that guy... Haruki's words stay with me."
        "Shoichi is obsessed with me... that's what he said."
        "I didn't believe it, but..."
        "After what happened just now... after what was said just now..."
        "A small part of me can't help but believe it."
        "Is Shoichi really obsessed with me?"
        "Why?"
        "\"What's so good about you anyway?\""
        "Those words echo in my head many times."
        "Could it be that Shoichi..."
        "No. No way. No way in hell it could be true."
        "I mean... we're both guys and... and he's been my friend for so long..."
        "... Why does my heart feel so heavy?"
        "I don't understand..."
        show s 1 u sad at fdis
        s "\"[povFirstName], are you sure you're alright? You're spacing out.\""
        mc 1 u shock "\"H-huh? O-oh, sorry about that.\""
        "Damn it, it's so obvious to him that I have something on my mind right now."
        "But seriously, what was this all about?"
        "I honestly don't understand. My mind is going around in circles without being able to grasp the situation."
        show s 1 u avoid at fdis
        s "\"Sorry to have acted so horribly in front of you... he really played me like a fiddle.\""
        mc 1 u worried "\"I don't think I've ever seen someone be able to anger you that much before.\""
        s "\"Yeah... somehow that guy seems to know all of my buttons...\""
        "And yet... the thing that made you really lose it was when it came to me."
        "Come to think of it, the only times I've ever seen you really get angry at other people was when I was involved..."
        "Goddamn it, no, I shouldn't be thinking about this."
        "That guy just said this stuff to get in my head. There's no way that..."
        "There's no way that Shoichi... is like that..."
        show s 1 u sigh at fdis
        s "\"Ugh... this is all such a headache...\""
        s "\"I wish he wouldn't act like this all the time. I want to believe he's not really a bad guy but then he goes and pulls crap like this...\""
        mc 1 u curious "\"Would you mind telling me more about this guy?\""
        show s 1 u shock at fdis
        $ renpy.pause(1.0)
        show s 1 u sigh at fdis
        s "\"Why do you even wanna know? You looking to get buddy-buddy with him?\""
        mc 1 u sigh "\"After today? Hardly. And I don't like you asking something like that after the shit he pulled.\""
        "Jeez, was he right? Are you really jealous?"
        show s 1 u wince at fdis
        s "\"S-sorry...\""
        mc 1 u "\"I just want to understand what this all was about.\""
        show s 1 u sigh at fdis
        s "\"Not even I understand, so good luck with that.\""
        if jun_met == False:
            s "\"Plus, there's not much else to tell. I already told you most of his story back in April.\""
            mc 1 u "\"Refresh my memory.\""
            s "\"Seriously?\""
            "I nod."
        else:
            s "\"I shouldn't either way... I don't think he'd like me telling you about him...\""
            mc 1 u "\"After what he did today, do you even care?\""
            show s 1 u avoid at fdis
            s "\"..."
            show s 1 u displeased at fdis
            extend " No.\""
            mc 1 u smile "\"See?\""
        show s 1 u sigh at fdis
        s "\"Okay, well, where should I start?\""
        s "\"Haruki's a member of the volleyball club, but he keeps getting in trouble with the Coach and the other members all the time. He doesn't know how to work as a member of the team.\""
        s "\"The sad part is that he's a really good player, but because he's such a liability, Coach doesn't let him play. He's not even on the bench.\""
        show s 1 u avoid at fdis
        s "\"I was asked to talk to him and get him to see the school's counselor after it was found out that his dad got arrested for being abusive.\""
        show s 1 u scorn at fdis
        s "\"It turns out that his father was a drunkard piece of shit who'd abuse his wife and son whenever he got drunk.\""
        show s 1 u avoid at fdis
        s "\"Haruki grew up for his entire childhood having to deal with that. It fucking sucks...\""
        show s 1 u scorn at fdis
        s "\"That's why I don't want to believe he's a bad guy. Deep down, I think he's really a good person. But because his childhood was so fucked up, I think he just doesn't know how to deal with people, so he keeps others away.\""
        show s 1 u sigh at fdis
        s "\"But in the end, this is nothing more than my opinion so what do I know...\""
        mc 1 u wry "\"I think you're an excellent judge of character so you just might be right.\""
        show s 1 u avoid at fdis
        s "\"I hope so. But it still doesn't excuse his behavior today. The shit he pulled with you...\""
        if harukiss == True:
            show s 1 u scorn at fdis
            s "\I mean... he kissed you. That's... that's just... that's just unforgivable!\""
            mc 1 u "\"Why?\""
            show s 1 u wince at fdis
            s "\"Wha- what do you mean \"why\"? I mean... he... he kissed you. Aren't you upset because of that?"
            show s 1 u scorn at fdis
            extend " Don't tell me you actually liked it!\""
            mc 1 u scorn "\"Of course I didn't. And that's beside the point. But why would you care so much about that? You're not worried whether he hurt me or anything. All you're focusing on is the fact that he kissed me!\""
            show s 1 u shock at fdis
            $ renpy.pause(1.0)
            show s 1 u avoid at fdis
            s "\"I... that's...\""
            "Shoichi... could it really be?"
            "No, get this out of your head!"
            "Shoichi just cares about you and is worried about you. That's all!"
            "Ugh... I'm letting that bastard's words influence my thought process."
            show s 1 u sad at fdis
            s "\"Sorry, [povFirstName]. I guess my priorities might be a little messed up...\""
            mc 1 u considerate "\"It's fine. Sorry to have gotten upset about it. You're just worrying about me because I'm your friend, right?\""
            show s 1 u wince at fdis
            s "\"Y-yeah. T-that's all there is to it...\""
            "Why does his voice sound so unconvincing?"
            "No. This is Shoichi I'm talking about. If he said that's what it is then I'll believe him!"
            "... It'd be too awkward otherwise..."
        else:
            s "\"Talking crap about you... he even called you pathetic... I have half a mind to punch him in the face.\""
            mc 1 u sigh "\"For both your sakes, please refrain from doing that.\""
            show s 1 u sigh at fdis
            s "\"Yeah yeah, I know.\""
        show s 1 u displeased at fdis
        s "\"Either way, he really needs to get his shit together. Coach is really close to just kicking him off the team altogether.\""
        mc 1 u worried "\"Things sound really rough for him...\""
        show s 1 u sigh at fdis
        s "\"It's not like he's blameless on the matter though...\""
        mc 1 u considerate "\"I know. I still feel bad for him though.\""
        mc 1 u worried "\"Family is supposed to be a safe place. They're supposed to take care of you and protect you, not abuse you... You and I are lucky we grew up in loving families, even if they did have their problems.\""
        show s 1 u wince at fdis
        s "\"Y-yeah... loving families... right.\""
        mc 1 u curious "\"Is something the matter?\""
        show s 1 u considerate at fdis
        s "\"No, not at all. I was just... just thinking that you're right. We really were lucky, huh?\""
        show s 1 u wince at fdis
        s "\"But people like Haruki or Urushihara didn't have the same luck as we did...\""
        "Yeah... now that I think about it, Kei-kun's family is also pretty messed up from what he's told us."
        "Damn it... I'm starting to get pissed off at these people."
        "How can they mistreat someone who's too young to fight back?"
        "You're essentially just screwing them up for life!"
        "... Although I guess Kei-kun has managed to come out of it mostly unscathed."
        mc 1 u "\"What are you going to do about him now?\""
        show s 1 u avoid at fdis
        s "\"Honestly, I have no clue... If he just shows up to practice today without me having talked to him like Coach asked, he's just going to piss Coach off even more.\""
        show s 1 u sigh at fdis
        s "\"I'll probably corner him before practice starts and I'll have a talk with him. Make sure he can't get away this time.\""
        mc 1 u "\"Try not to lose your patience though.\""
        show s 1 u wince at fdis
        s "\"I won't. You don't need to worry about that.\""
        "Somehow I have a hard time believing it..."
        mc 1 u considerate "\"I guess me coming to the roof kinda ruined your plans to talk to him, huh?\""
        show s 1 u at fdis
        s "\"It's not your fault. There's no way you could have known he'd be here.\""
        show s 1 u sigh at fdis
        s "\"Honestly, it was my fault. I should have thought that you could have shown up. It's not unusual for you to come up here during lunch break.\""
        mc 1 u think "\"Hmm... when I think about it that way...\""
        show s 1 u considerate at fdis
        s "\"You're agreeing with me now?\""
        mc 1 u happy "\"Pfft, hahaha.\""
        show s 1 u smile at fdis
        s "\"What? Now you're laughing at me. Jeez, you're awful.\""
        mc 1 u smile "\"Sorry, sorry.\""
        mc 1 u think "\"So everything he pulled now was just an act so he could manipulate you into forgetting to scold him?\""
        show s 1 u sigh at fdis
        s "\"It seems like it. That wolf is much more devious than I gave him credit for.\""
        mc 1 u smile "\"Kinda reminds me of someone I know.\""
        show s 1 u wince at fdis
        s "\"Wha- I'd never do something that'd end up hurting other people.\""
        mc 1 u think "\"Maybe. But you can come up with some pretty crafty plans to get your way when you want to.\""
        show s 1 u sigh at fdis
        s "\"Jeez, back when you went to my house and now today... you really have a pretty bad image of me, don't you?\""
        mc 1 u happy "\"I have no idea what you're talking about!\""
        s "\"Aren't you a funny one.\""
        show s 1 u think at fdis
        s "\"Well, either way I guess we should get going."
        show s 1 u at fdis
        extend " Lunch break is almost over and I'm pretty sure neither of us has gotten anything to eat yet.\""
        mc 1 u think "\"You're certainly right on that front.\""
        show s 1 u smile at fdis
        s "\"Plus, Jun and Saya must be worried about us.\""
        mc 1 u considerate "\"You're probably right on that front too.\""
        "Although I did plan to just sleep lunch away, all of this mess has suddenly made me very hungry..."
        s "\"Shall we get going?\""
        mc 1 u happy "\"Yeah!\""
        "..."
        "But still..."
        "Hopefully I can get Haruki's words out of my head..."
        stop music fadeout 2.5
        $ date = None
        jump cs_final
