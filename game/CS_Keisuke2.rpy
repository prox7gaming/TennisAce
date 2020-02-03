label keisukestart_1:
    $ uihide = True
    stop music2 fadeout 2.5
    $ keisukehearts += 1
    scene SCorridor with fade
    "Considering the amount of people in the hallway, I'd say Keisuke's class went out for lunch sooner than expected today."
    "I wonder if something happened."
    play sound "music/slidingdoor.ogg"
    show k 1 u avoid at fdis, five with dissolve
    "Just as I'm about to reach for the door, it opens on its own and Keisuke shows up from the other side."
    show k 1 u shock at fdis
    play music2 "music/BGM/Feelin Good.ogg" fadein 5.0
    k "\"[povFirstName]-san?\""
    mc 1 u nsmile "\"Hey... is this a good time?\""
    show k 1 u avoid at fdis
    k "\"As good a time as any. What's up?\""
    mc 1 u wry "\"I wanted to check up on you. You didn't seem to be doing too well the last time we talked.\""
    show k 1 u annoyed at fdis
    k "\"I'm just fine. I don't need you to babysit on me.\""
    mc 1 u smile "\"It's not babysitting. I'm just making sure my friend is okay. There's nothing wrong with that, is there?\""
    show k 1 u avoid at fdis
    k "\"I... I suppose not...\""
    show k 1 u sigh at fdis
    k "\"Ugh, I'm sorry. I shouldn't have snapped at you.\""
    show k 1 u avoid at fdis
    mc 1 u smile "\"It's no big deal. I'm just assuming you're under a bit of stress.\""
    show k 1 u sigh at fdis
    k "\"Yeah..."
    show k 1 u avoid at fdis
    extend " I had no choice but to come clean to my father about what happened. There was no way I could hide having to order all those new documents from him and it would have been even worse if he had to find out elsewhere.\""
    show k 1 u sad at fdis
    k "\"And Alex was blamed for it, just as I feared.\""
    mc 1 u shock "\"Shit, that's horrible. He didn't listen to reason?\""
    show k 1 u sigh at fdis
    k "\"I... I don't even know."
    show k 1 u avoid at fdis
    extend " My father isn't one given to be unreasonable but... I told him that I was the one that went out without Alex and that it was my fault that this happened but he still wouldn't take it...\""
    k "\"Father threatened to fire him if this happened again... and Alex said nothing."
    show k 1 u sad at fdis
    extend " Not to me, not to my dad. He should have been livid. He should have gotten mad at me... but he didn't... somehow that makes it all even worse.\""
    mc 1 u wince "\"Is there anything you can do about it?\""
    show k 1 u sigh at fdis
    k "\"Since no action was officially taken this time, there's not much I can do. Alex got out just with a warning, even if it was an unwarranted one.\""
    show k 1 u avoid at fdis
    k "\"I, on the other hand, got served with an hour long lecture about my personal safety and how I'm not supposed to be ditching my, as he calls them, \"safety escorts\".\""
    show k 1 u worried at fdis
    k "\"What's so wrong with valuing my freedom? This is ridiculous.\""
    mc 1 u wry "\"There's nothing wrong with it. We all want freedom, it's in our nature. Your dad is just being unreasonable.\""
    show k 1 u avoid at fdis
    k "\"I suppose that's one way to look at it...\""
    mc 1 u smile "\"Do you have any idea what you'll do now?\""
    show k 1 u sigh at fdis
    k "\"I already told you, there's nothing for me to do.\""
    mc 1 u sigh2 "\"I'm not talking about legal stuff, Einstein. I'm asking you what you'll do to take personal responsibility and own up to it.\""
    mc 1 u sigh "\"Or are you just gonna let this all happening without doing anything to make it up to Alex?\""
    show k 1 u shock at fdis
    k "\"Oh!"
    show k 1 u avoidb at fdis
    extend " I... wasn't thinking of doing anything...\""
    mc 1 u blank "\"...\""
    show k 1 u wince at fdis
    k "\"D-don't look at me like that...\""
    mc 1 u sigh2 "\"How can you go on a spiel about feeling bad about the whole thing and wanting to take responsibility for it but you don't even think of doing something to make it up to him?\""
    show k 1 u avoidb at fdis
    k "\"I... I just hadn't thought of it, okay?\""
    mc 1 u sigh "\"You're horrible sometimes.\""
    play sound "music/stab.ogg"
    show k 1 u wince at fdis, shake1
    k "\"Guh...\""
    show k 1 u worried at fdis
    k "\"...{w} Maybe you're right.\""
    mc 1 u smile "\"Just maybe?\""
    show k 1 u sigh at fdis
    k "\"Don't act so smug. You have a long life ahead of you, you're bound to be right every now and then. Don't let it get to your head.\""
    mc 1 u happy "\"Aye aye, Chief.\""
    show k 1 u avoid at fdis
    k "\"And don't sass me either.\""
    mc 1 u happy "\"No can do, Chief.\""
    show k 1 u sigh at fdis
    k "\"I guess I shouldn't have expected any different from you, huh?\""
    "Oh good, he got the message."
    "I watch as his nose twitches a few times."
    "A telltale sign that he's deep in thought... or smelling something."
    mc 1 u smile "\"Any ideas?\""
    show k 1 u avoid at fdis
    k "\"I don't know... what do you usually do when you need to apologize to someone for something you did?\""
    mc 1 u "\"Well, ideally you'd want to do something for them that's heartfelt. What sorts of things does Alex enjoy? Maybe you can buy him something he'd really want as an apology.\""
    mc 1 u think "\"Not that I'm endorsing an attempt to buy forgiveness but I don't really think there's much you can do since you've already apologized.\""
    show k 1 u nervous at fdis
    k "\"...\""
    mc 1 u fsmile "\"You... you have apologized... haven't you?\""
    k "\"I...\""
    mc 1 u sigh2 "\"Oh my God!\""
    show k 1 u avoidb at fdis
    k "\"It slipped my mind, okay?!\""
    mc 1 u annoyed "\"How can so many simple things slip your mind? This is basic decency we're talking about. You do something that hurts someone? You apologize! How hard can it be?\""
    show k 1 u nervous at fdis
    k "\"...\""
    mc 1 u angry "\"Say something, for God's sake!\""
    show k 1 u wince at fdis, shake1
    k "\"I-I'm sorry!\""
    mc 1 u angry "\"Not to me, you idiot!\""
    k "\"Guh...\""
    mc 1 u sigh "\"Look, you should apologize to him before you even think of doing something else.\""
    show k 1 u avoid at fdis
    k "\"I... I'd rather get him something first.\""
    mc 1 u sigh2 "\"If yo-\""
    k "\"Yeah yeah, I know. If I just buy him something without apologizing first it'll just look like I'm trying to buy his forgiveness.\""
    k "\"But I'd rather give him something meaningful and from the heart {i}while{/i} I apologize profusely... so he can see that I was thinking about it this whole time.\""
    show k 1 u worried at fdis
    k "\"Do you... do you think that would work?\""
    mc 1 u think "\"...\""
    show k 1 u wince at fdis
    k "\"You have nothing to say?\""
    "..."
    "To be honest, I don't."
    "I'd prefer if he weren't so stubborn but I think I've already grilled him enough for a single day."
    "Err... what would be a gentler way to say this?"
    mc 1 u considerate "\"W-well, I suppose you know him better than I do so I think you're better equipped to answer that question.\""
    show k 1 u avoid at fdis
    k "\"I... I guess so...\""
    show k 2 u scorn at fdis
    k "\"Let's see... what could I get to show Alex that I'm sorry for what I did...\""
    mc 1 u "\"Your best bet would probably think about what kinds of things he likes and try to get him something he could possibly want. Can you think of anything that he might want?\""
    k "\"...\""
    mc 1 u "\"...\""
    "..."
    mc 1 u sigh "\"Well?\""
    show k 1 u avoid at fdis
    k "\"I... don't know.\""
    mc 1 u wince "\"O-oh... okay, uhm...\""
    mc 1 u smile "\"Oh, what about the kinds of things he likes? Does he have any hobbies?\""
    show k 1 u worried at fdis
    k "\"... I don't know.\""
    mc 1 u fsmile "\"D-did he ever mention anything he might want?\""
    show k 1 u avoidb at fdis
    k "\"Not that I know of...\""
    mc 1 u nervous "\"Erm... w-what about anything that he might have mentioned being interested in but having never tried?\""
    k "\"I... I don't know.\""
    mc 1 u blank "\"...{w} Do you know anything about him?\""
    k "\"I..."
    show k 1 u sad at fdis
    extend " I thought I did...\""
    mc 1 u wince "\"Come on, you can't think of anything? Nothing at all?\""
    k "\"... No.\""
    mc 1 u wince "\"That's...\""
    "That's awful. How can you not know anything?"
    k "\"I... I need fresh air.\""
    play sound "music/running.ogg"
    show k 1 u sad at fdis, offscreenleft with move
    "Keisuke runs off without warning."
    mc 1 u shock "\"W-wait, Kei-kun!\""
    stop music2 fadeout 2.5
    "Ignoring all the heads turning towards us, I try to follow."
    scene SRooftop with fade
    play music "music/breeze.ogg"
    play sound "music/metaldoor.ogg"
    "I peek my head through the roof, looking for any signs of the white hare."
    mc 1 u sigh2 "\"Goddamnit, where did he go?\""
    "I knew I should have ran after him but at the time I was too worried about people staring at me to move."
    "Never again will I be that stupid."
    mc 1 u nervous "\"Kei-kun? Are you here?\""
    "..."
    "Keisuke" "\"Yeah...\""
    show k 1 u avoid at fdis, five with move
    "Stepping from behind a corner, Kei-kun shows up in front of me, his eyes avoiding my gaze."
    k "\"I thought I lost you back at the second floor.\""
    mc 1 u smile "\"Sorry to say but this school isn't really big enough for you to shake someone off your trail.\""
    k "\"Evidently.\""
    "Dammit, can't you at least look me in the eyes when you talk to me?"
    mc 1 u considerate "\"Sorry, I shouldn't be joking right now.\""
    mc 1 u wry "\"How are you feeling?\""
    k "\"Like a terrible person...\""
    mc 1 u considerate "\"Oh, come on, don't be like that. You're not a terrible person.\""
    show k 1 u scorn at fdis
    k "\"Is that so? Then tell me what kind of \"good\" person knows absolutely nothing about someone who practically raised them? Not even one thing!\""
    show k 1 u worried at fdis
    k "\"And it's not just Alex... I... now that I think about it, I know a lot less about you guys than you all know about me.\""
    k "\"Even though you guys have always been pretty open about yourselves while I tended to keep my own secrets locked down tight... somehow, I still know less about you guys than I should.\""
    k "\"I'm just so... so self-absorbed... I've always been disgusted by my family and by how little they cared about other people... and yet I now realize I'm just the same as them.\""
    mc 1 u nsmile "\"Oh, come on, isn't it a bit too early for you to be having core-shaking realizations?\""
    show k 1 u sigh at fdis
    k "\"I thought you said you were done with the jokes.\""
    mc 1 u smile "\"It's a little hard to stop joking when you're being this edgy about the whole thing.\""
    show k 2 u gentle at fdis
    k "\"You're... God, you're an idiot.\""
    "Heh, at least that made him feel a little better."
    "I can already tell that his body relaxed a bit."
    play music2 "music/BGM/I Want to Know You - Narration.ogg" fadein 5.0
    mc 1 u happy "\"Yup. I'm an idiot. Probably the biggest one around here. And you want to know something else?\""
    mc 1 u smile "\"You're my friend. No matter what you think of yourself.\""
    show k 1 u shock at fdis
    k "\"W-what?\""
    mc 1 u happy "\"Oh, don't look at me like that.\""
    mc 1 u smile "\"So you're a little self-absorbed. So what? We all have our flaws. Like how I'm incredibly lazy. Or how Shoichi is fussy to the point of annoyance. Or how Jun has the attention span of a goldfish.\""
    mc 1 u considerate "\"It's our flaws that make us interesting people. Can you imagine how dull it would be if you were only surrounded by a bunch of perfect people? First of all, you'd never feel like you could measure up to their brilliance.\""
    mc 1 u smile "\"It's okay to make mistakes. You just have to learn from them and grow.\""
    mc 1 u happy "\"Really, that's one of the funnest parts of life. Things would be so boring if failure didn't exist.\""
    show k 1 u avoid at fdis
    k "\"...\""
    "..."
    "Huh. I didn't expect him to stay silent after that."
    "It was such a nice speech too. I fully expected him to applaud me while in tears, getting on his knees and glorifying my awesomeness!"
    "... Okay, okay. I might be exaggerating a little bit."
    "But I certainly didn't expect silence of all things."
    k "\"...\""
    mc 1 u fsmile "\"Did I... did I say something wrong? {size=-2}You're awfully quiet.{/size}\""
    show k 2 u gentle at fdis
    k "\"Pfft-\""
    mc 1 u shockb "\"H-huh?\""
    k "\"Ahahaha, [povFirstName]-san, you got so worked up over this. Even more than I did.\""
    mc 1 u shockb "\"W-wha? Cut it out. I was just trying to make you feel better. Were you just messing with me this whole time?!\""
    show k 1 u smile at fdis
    k "\"Of course not. Don't be crazy.\""
    show k 1 u avoid at fdis
    k "\"Don't get me wrong, I'm still upset about the whole thing.\""
    show k 1 u smile at fdis
    k "\"But your words gave me hope that I can still do better.\""
    show k 2 u gentle at fdis
    k "\"Indeed, it's not too late for me to do better.\""
    show k 1 u smile at fdis
    k "\"I'll do my best to become a more attentive friend. I won't let anyone call me self-absorbed anymore.\""
    "... Well, technically the only one who called you that was you yourself."
    "But I don't think this piece of information is very important right now. I'll just stay silent about it."
    "Still, it's good to see him feeling better... even if the change was very surprising."
    mc 1 u smile "\"I'm glad I was able to help. I was worried that I might have been too hard on you back there...\""
    show k 1 u calm at fdis
    k "\"Nah, don't worry about it. My heart's not made of glass, you know. I can take criticism.\""
    "Said the person that immediately ran away when faced with said criticism."
    "But then again, I don't think this piece of information is going to be very useful either."
    show k 2 u scorn at fdis
    stop music2 fadeout 2.5
    play music3 "music/BGM/Autumn Day.ogg" fadein 5.0
    k "\"I guess I should start by sniffing around Alex's information a little bit. Try to get to know what kinds of things he likes before I buy him my apology present.\""
    mc 1 u fsmile "\"You're still going on about that?\""
    show k 1 u at fdis
    k "\"I can't just leave it unresolved. And I absolutely refuse to apologize without being able to give him something to make up for what I've done.\""
    mc 1 u fsmile "\"Some people are happy with just a heartfelt apology you know.\""
    show k 1 u annoyed at fdis
    k "\"Well, too bad. He's getting both.\""
    "... So stubborn."
    mc 1 u wry "\"Fine, fine, I get it.\""
    mc 1 u curious "\"How are you planning on getting that information though?\""
    show k 2 u scorn at fdis
    k "\"Hmm... that's a good question, too...\""
    mc 1 u "\"You have no idea?\""
    show k 1 u smile at fdis
    k "\"None.\""
    "... I thought so."
    show k 1 u calm at fdis
    k "\"Nevertheless, I will think of something.\""
    show k 1 u smile at fdis
    k "\"And don't think I've forgotten about you either.\""
    mc 1 u shock "\"M-me? What did I do?\""
    show k 2 u gentle at fdis
    k "\"It's not about what you did, silly, it's about who you are.\""
    show k 1 u smile at fdis
    k "\"You're probably the closest friend I have at this time. It annoys me to know that I've never really paid you as much attention as I should have.\""
    mc 1 u shockb "\"W-wha- You're just exaggerating!\""
    show k 1 u calm at fdis
    k "\"No I'm not."
    show k 1 u smile at fdis
    extend " I want to get to know you better, [povFirstName]-san. You've been so good for me since we met. Even more so since the start of this school year.\""
    show k 2 u gentle at fdis
    k "\"I want to find a way to thank you for being so great all the time.\""
    mc 1 u avoidb "\"I'm... I mean... I don't... Ugh... do whatever you want.\""
    k "\"Of course.\""
    show k 1 u smile at fdis
    k "\"Could I ask you to accompany me into town soon? I don't know yet when I'll next be available but I want you to help me pick my present for Alex.\""
    mc 1 u think "\"Me? How am I going to help? I don't really know anything about Alex.\""
    show k 2 u gentle at fdis
    k "\"Alright, maybe not help me pick so much as keep me company.\""
    show k 1 u smile at fdis
    k "\"I feel like it's much easier for me to stay calm and composed when you're nearby.\""
    mc 1 u confused "\"I... guess? That's such a weird thing to have someone say to you.\""
    show k 2 u gentleb at fdis
    k "\"Haha. Your reaction to it certainly is amusing.\""
    show k 1 u smile at fdis
    k "\"So it's okay for me to count on you?\""
    mc 1 u smile "\"Sure. As long as I'm available, I'll keep you company. I also have fun when we're going out so it's not like this is a bad deal for me or something.\""
    show k 2 u gentle at fdis
    k "\"Alright. It's a deal. I'll message you when I've found a good day for it.\""
    show k 1 u smile at fdis
    k "\"For now, we should probably head back downstairs. We only have five minutes left in our lunch break and I haven't even touched my food yet.\""
    mc 1 u wince "\"Crap, neither have I. We better hurry.\""
    show k 2 u gentle at fdis
    "Keisuke was smiling and laughing the whole time we were running back down the stairs."
    "For some reason, the thought \"Keisuke looks kinda cute when he's smiling\" flashed through my head for a moment before quickly being dispersed by my stomach growling."
    stop music fadeout 2.5
    stop music3 fadeout 2.5
    $ date = None
    jump cs_final
