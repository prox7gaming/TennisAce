label keisukestart_0:
    $ uihide = True
    stop music2 fadeout 2.5
    $ keisukehearts += 1
    scene SportStore with fade
    play music2 "music/BGM/Dazzling Sunlight.ogg" fadein 5.0
    "Ah, the cool, air-conditioned interior of a shop."
    "There is no better way to spend time whilst leisurely browsing the new arrivals."
    "To be honest, I don't really have much of a reason to be here today. I've already bought new shoes just a little while ago."
    "But I couldn't resist the temptation to pass by after class and see what's new."
    "I love looking at the shoes and rackets that they have on display."
    "Somehow, even if I buy the very same shoes from the display, they always look so much more beautiful when they're not mine..."
    "... I might have a slight shopping addiction."
    "Hmm?"
    show k 1 u avoid at five, fdis with dissolve
    "Is that... Kei-kun?"
    "Huh, I'll be damned. Seeing Keisuke at a store like this without anyone accompanying him..."
    "I mean... I know he goes out every now and then, but I never imagined that he did his own shopping himself."
    "Even though I've seen him do it before, as far as I'm aware, he only did it because we had already brought him along with us when we went to the stores."
    "So it was more of a \"Oh well, since I'm here anyway then I might as well\" reflex than him actually doing something regularly."
    "I'm also a little surprised that he's here after class."
    "I figured that, since the court has been closed down for a few weeks, he'd just be practicing at home."
    mc 1 u smile "\"Yo.\""
    stop music2 fadeout 2.5
    play music3 "music/BGM/Punchline - Org.ogg" fadein 5.0
    show k 1 u shock at fdis
    $ renpy.pause(1.0)
    show k 1 u worried at fdis
    k "\"[povFirstName]-san, what are you doing in a place like this?\""
    mc 1 u sigh "\"That should be my line, you know? It's much more likely that you'd run into me inside a sporting gear store than into you.\""
    show k 1 u wince at fdis
    k "\"I guess you're right.\""
    mc 1 u curious "\"What brings you here? I figured you just had your servants do your shopping for you. Never thought to see you inside a store like this unless you were out running errands for someone.\""
    show k 1 u sigh at fdis
    k "\"Not you too...\""
    mc 1 u "\"Did I say something wrong?\""
    show k 1 u avoid at fdis
    k "\"Technically... no. It's true that I usually have other people do my errands for me...\""
    show k 1 u sigh at fdis
    k "\"It's just that... everyone always keeps assuming that that's the case. Even if it's true, it's so annoying.\""
    mc 1 u smile "\"So you decided to come here alone today to... prove something to someone that isn't even here?\""
    show k 1 u avoid at fdis
    k "\"Not really. I just hate that people always tell me that I'm out of touch with the real world.\""
    k "\"I get that I can say or suggest things that are unrealistic for regular people without realizing it but that doesn't mean I embrace it.\""
    mc 1 u "\"So you decided to go out today on your own to prove that you're good enough to handle things yourself?\""
    show k 1 u smile at fdis
    k "\"I guess you could say it's something like that."
    show k 1 u avoid at fdis
    extend " Truth be told, other than when I'm with you guys or when people ask me to go on errands, I never go out to shop.\""
    show k 1 u at fdis
    k "\"And even when I do, I always stick to the... err... more \"refined\" places.\""
    if day10 == "keisuke":
        mc 1 u smile "\"You mean the rich people shops? Like the ice cream parlor or the cake shop you took me to?\""
    else:
        mc 1 u smile "\"You mean the rich people shops like the ice cream parlor you took me to?\""
    show k 1 u wince at fdis
    k "\"I... err... I guess you could call them that...\""
    mc 1 u happy "\"Don't kid yourself thinking that it's just a way to call them. That's exactly what those places are.\""
    k "\"Guh...\""
    "Heh. Teasing him is so much fun."
    mc 1 u smile "\"So you decided to go out on your own and check out the stores that us common folk tend to go to, huh?\""
    show k 1 u worried at fdis
    k "\"I wouldn't really put it that way... I just didn't want to feel like I'd be completely useless without supervision.\""
    show k 1 u sigh at fdis
    k "\"For better or worse, I've never been alone to an establishment that didn't get some prior screening by my family.\""
    show k 1 u avoid at fdis
    if day10 == "keisuke":
        k "\"Even the bank I use was selected by Alex. Sure, it was without my family's knowledge but I still needed help.\""
        mc 1 u happy "\"And yet you still chose these same kinds of places whenever you have the chance. You're really not good at going out of your comfort zone, huh?\""
    else:
        k "\"Even the bank I use was selected by Alex. Sure, it was without my family's knowledge but I still needed help.\""
        mc 1 u curious "\"Who's Alex?\""
        show k 1 u at fdis
        k "\"Oh, right, you don't know him..."
        show k 1 u avoid at fdis
        extend " He's... my personal bodyguard and butler.\""
        mc 1 u "\"I feel like I should be saying something like \"You have a personal butler?!\" but at this point I think I've become too jaded to this kind of thing.\""
        k "\"I wish that weren't the case...\""
        mc 1 u happy "\"Man, it's kinda funny to think that even when you're aware of this, you still only suggest super expensive places for us to go to. You really stick to your comfort zone a lot, huh?\""
    show k 1 u wince at fdis
    play sound "music/stab.ogg"
    k "\"Guh...\""
    "Hmm... at what point does this classify as cruelty?"
    "... I probably still have a few more uses before then."
    mc 1 u smile "\"Either way, what did you come here to do? I can help you if you want.\""
    show k 1 u avoid at fdis
    k "\"Doesn't that kind of defeat the purpose of coming alone?\""
    mc 1 u think "\"You did come all the way here by yourself, didn't you? What does it matter if I just give you my opinion on what shoe you should buy?\""
    show k 1 u sigh at fdis
    k "\"I... suppose you're right.\""
    mc 1 u happy "\"I'll only be helping you make a decision. Once you do, you're on your own.\""
    show k 1 u smile at fdis
    k "\"Yeah, I guess I can roll with that.\""
    mc 1 u smile "\"Alright, so what were you looking into getting?\""
    show k 2 u scorn at fdis
    k "\"Let's see... even if I notice and react in time to my opponent's plays, I just can't seem to run fast enough to get to it, so ideally I'd need some more spring in my step. What would you recommend for that?\""
    mc 1 u worried "\"... I don't know... Other than more training, magic is the only thing left.\""
    show k 1 u shock at fdis
    $ renpy.pause(1.0)
    show k 1 u avoidb at fdis
    k "\"R-right, I'm being unrealistic here, aren't I?\""
    mc 1 u considerate "\"A bit, yeah.\""
    show k 1 u wince at fdis
    k "\"Then just... just something that could help propel me forward more easily? Maybe take a bit of the load off my knees.\""
    mc 1 u think "\"That... might be done. Give me a second.\""
    "I take a look at the assortment of running shoes, track shoes, volleyball shoes..."
    "I ignore all characterizations and just look for the ones that might be most suitable to his needs."
    "Of course, I don't consider myself an expert in shoes, but I do know many times this labeling just serves to sell you a prettier-looking version of a more basic model."
    show k 1 u at fdis
    mc 1 u smile "\"This one should serve you well. It's usually for running but it does have tiny springs on the soles that are meant to cushion the impact on your knees and propel you forward.\""
    mc 1 u "\"This is a pretty pricey model... but then again, I doubt that would be a problem for you of all people.\""
    show k 1 u smile at fdis
    k "\"You're right, it's not a problem. I like the color on it too. It's definitely not as flashy as the other ones I've been seeing around.\""
    mc 1 u smile "\"Yeah. That's a tactic they use to draw you in. Make it super flashy so it'll catch your eye first and you won't even notice the competition that outdoes it before you're already leaving the store with your new shoes.\""
    show k 1 u calm at fdis
    k "\"I never thought about that before but I'm certainly not going to be complaining about it right now.\""
    show k 1 u smile at fdis
    k "\"Thank you, [povFirstName]-san.\""
    mc 1 u happy "\"It's no problem. Do you want me to show you some other models so you could maybe have a bigger range of options?\""
    show k 2 u gentle at fdis
    k "\"You're starting to sound just like a salesman.\""
    mc 1 u laugh "\"Am I? I didn't notice. Hahaha.\""
    show k 1 u smile at fdis
    k "\"Still, you were a big help."
    show k 1 u avoidb at fdis
    extend " I'm a bit ashamed to admit but I was feeling a little... embarrassed of asking the clerk for help.\""
    mc 1 u "\"Why's that? You've talked to tons of clerks when you were out with us.\""
    show k 1 u sigh at fdis
    k "\"Yeah. And again, that's the key."
    show k 1 u at fdis
    extend " Even when I'm with you guys, I at most make an order and that's it. Having to actually ask for help... I can't help but feel like I'm being judged.\""
    mc 1 u smile "\"You're crazy... but not entirely wrong.\""
    show k 1 u wince at fdis
    k "\"Wait, what? How does that even work?\""
    mc 1 u smile "\"That's what they are paid to do. They are paid to always assume that you don't know anything that you're talking about and always try to push products you don't need because, again, if you don't know what you're talking about then how will you know you don't need it?\""
    mc 1 u happy "\"It's a bit annoying, sure, but once you show them you actually know your stuff they tend to back off.\""
    mc 1 u talk "\"Of course, not all of them are like that. It's just that some shops tend to always push their salespeople to do stuff like that, even if it makes customers uncomfortable. The margin of profit is all that matters.\""
    show k 1 u at fdis
    k "\"You seem to know quite a bit about this stuff. I'd never have guessed... I don't remember you ever mentioning having a part-time job.\""
    mc 1 u considerate "\"That's because I don't. But that doesn't mean salespeople don't talk. They're people too just like you and me.\""
    mc 1 u happy "\"I just picked a store I really liked, and after they saw me there a bunch of times, the workers there started opening up to me. You hear all kinds of things, all you need to do is be willing to listen.\""
    mc 1 u smile "\"Which, for your information, is the very same store we're standing in right now.\""
    show k 1 u calm at fdis
    k "\"Wow... I wasn't expecting that sort of thing from you.\""
    mc 1 u pout "\"What? Why the hell not? I'm a good listener!\""
    show k 1 u smile at fdis
    k "\"Yeah. You really are. I just never gave you proper credit before. My bad.\""
    mc 1 u shock "\"..."
    show mc 1 u avoidb at offscreenleft
    extend " Not a problem.\""
    show k 1 u smile at fdis
    k "\"Heh. You look kind cute when you're caught by surprise.\""
    mc 1 u avoidb "\"W-what? I wasn't-\""
    show k 2 u gentle at fdis
    k "\"It's fine, don't worry about it so much. The same happens to me.\""
    show k 1 u smile at fdis
    k "\"You know, I never really thought about it a lot before, but..."
    show k 2 u gentleb at fdis
    k "\"Isn't having people that you feel safe letting your guard down around a wonderful thing?\""
    play sound "music/heartbeat.ogg"
    "!!!"
    show k 1 u at fdis
    k "\"[povFirstName]? Are you still with me here?\""
    mc 1 u avoid "\"O-oh, y-yeah, I'm still here. Sorry, I got a little distracted.\""
    show k 1 u smile at fdis
    k "\"No problem. We weren't talking about anything important anyway.\""
    k "\"I think I'm gonna pick these ones after all.\""
    show k 2 u gentle at fdis
    k "\"Hey, since you're already here with me anyway, how about you go all the way with me?\""
    mc 1 u dismayb "\"W-what?! I-I don't think that's an appropriate thing to ask me here of all places!\"" with hpunch
    show k 1 u shock at fdis
    $ renpy.pause(1.0)
    show k 1 u sigh at fdis
    k "\"... What exactly did you even think of in the first place?\""
    mc 1 u dismayb "\"H-huh?\""
    show k 1 u avoid at fdis
    k "\"... I was asking you if you wanted to accompany me to the cashier while I finished the transaction.\""
    mc 1 u dismay "\"Eh?!\""
    show k 1 u sigh at fdis
    k "\"... Get your mind out of the gutter...\""
    mc 1 u dismay "\"S-sorry!!!\"" with hpunch
    show k 1 u avoid at fdis
    k "\"Whatever... I'll just choose to pretend this never happened.\""
    show k 1 u smile at fdis
    k "\"... It's not like you'd be a bad choice anyway.\""
    mc 1 u shockb "\"W-what does that mean?\""
    show k 1 u haughty at fdis
    k "\"That's for me to know and you to obsess about.\""
    mc 1 u shockb "\"W-wait, Kei-kun!\""
    show k 1 u smile at fdis
    "Kei-kun grabs the shoes he decided to buy and takes them to the cashier without giving me even a sideways glance."
    k "\"Good afternoon. I'd like to buy these shoes, please.\""
    "Cashier" "\"No problem. Did you find everything you were looking for?\""
    show k 1 u calm at fdis
    k "\"Yes, the selection was great. I couldn't be happier about it.\""
    "Cashier" "\"I'm very glad to hear that, sir. Are you part of our rewards program?\""
    show k 1 u at fdis
    k "\"No. What's that?\""
    "Cashier" "\"You sign up for a special credit card that you can use in our stores. Whenever you make a purchase using it, you get points that you can later trade for rewards. Would you like me to sign you up?\""
    show k 1 u avoid at fdis
    k "\"I... I don't think so. I already have a pretty good credit card, I don't really need another.\""
    "Cashier" "\"Are you sure?\""
    k "\"Yes. I'm sure...\""
    "I can notice Kei-kun fidgeting a bit as he answers the clerk's questions. He's not even making eye contact anymore."
    "I guess he wasn't joking when he said he's not used to this kind of thing?"
    "Wait, don't the stores he usually goes to have reward card programs?"
    "Cashier" "\"That'll be ¥71.649, sir.\""
    show k 1 u at fdis
    k "\"Okay. Just give a se-\""
    show k 1 u shock at fdis
    stop music3
    k "\"?!\""
    "Kei-kun immediately stands fully upright, repeatedly patting his pockets with no success."
    mc 1 u curious "\"Is everything alright?\""
    show k 1 u avoid at fdis
    play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
    k "\"I... I can't find my wallet...\""
    mc 1 u fsmile "\"A-are you joking? Cause that's not a v-\""
    show k 1 u worried at fdis
    k "\"I'm not joking... I... I can't find my wallet...\""
    mc 1 u shock "\"Oh, shit. O-okay. Here's what we're gonna do. I'll buy these for you right now... even though that'll probably clear my entire bank account. You can give me the money back later, is that okay?\""
    show k 1 u avoidb at fdis
    k "\"Y-yeah... thank you...\""
    stop music2 fadeout 2.5
    scene Street2
    show k 1 u avoid at fdis, five
    with fade
    play music "music/crowd01.ogg"
    "Once the shoes were paid for, we immediately went outside to look for Keisuke's lost wallet."
    k "\"I... I can't believe something like that happened... it's mortifying.\""
    mc 1 u considerate "\"Don't worry about it too much. You were able to buy the shoes in the end. It's no biggie.\""
    show k 1 u avoidb at fdis
    k "\"Yeah, but what if you hadn't come along? Can you imagine how stupid I'd look if I just showed up by myself and realized I didn't have my wallet?\""
    k "\"That'd be pathethic.\""
    mc 1 u wry "\"These things happen. You shouldn't beat yourself up over them.\""
    mc 1 u considerate "\"Now how about we get to looking for your wallet instead of sulking around?\""
    show k 1 u worried at fdis
    k "\"Yeah, you're right... as you usually tend to be.\""
    show k 1 u avoid at fdis
    k "\"... I shouldn't have come here after all...\""
    mc 1 u nervous "\"Oh, come on, you can't say something like that. Bad things are bound to happen eventually. You can't just stay stuck in your shell because of that.\""
    show k 1 u worried at fdis
    k "\"Maybe... but because of it I'm now causing you problems...\""
    mc 1 u considerate "\"You're not ca-\""
    show k 1 u avoidb at fdis
    k "\"And, oh God, what happens if we don't find my wallet? There's no way I can hide this from my family. All my documents were there. My credit card was there. I'll have to freeze my account and order new documents.\""
    show k 1 u nervous at fdis
    k "\"And... and... Alex would...\""
    mc 1 u curious "\"What's this about Alex?\""
    show k 1 u sad at fdis
    k "\"... Alex would take the blame...\""
    mc 1 u shock "\"What? Why would he ever get the blame? He has nothing to do with what happened here!\""
    k "\"You really think they'll see it like that? Alex is charged with taking care of me whenever I'm not at school...\""
    show k 1 u worried at fdis
    k "\"Since there's no way I'd have lost my wallet at school, they'll know that it got lost while I was supposed to be with Alex...\""
    show k 1 u sad at fdis
    k "\"Which to them can only mean one of two things. Either he wasn't paying close attention to me while we were outside... or he wasn't with me at all...\""
    show k 1 u worried at fdis
    k "\"I've been used to leaving him behind when I go out because I don't like the supervision but... but even when it was found out, he'd get nothing more than a slap on the wrist...\""
    mc 1 u considerate "\"Come on, this is just a lost wallet. You really think they'll be that upset over that?\""
    mc 1 u wry "\"Plus, we haven't crossed that bridge yet. We'll discuss this when we get there, okay?\""
    k "\"... Okay...\""
    mc 1 u happy "\"Great. Now do try to calm down a bit for me, okay?\""
    mc 1 u considerate "\"I do need you to try and remember where you've been to so we can retrace your steps.\""
    show k 1 u avoid at fdis
    k "\"I... I didn't really do anything much... I came here straight after class ended so if the wallet fell out of my pocket, it had to have fallen on the way.\""
    mc 1 u smile "\"We can retrace your steps and try to see if we find where you dropped the wallet. Is that good for you?\""
    show k 1 u worried at fdis
    k "\"It's as good a plan as any...\""
    mc 1 u considerate "\"Not exactly the mindset I'm looking for here but I guess I'll take it...\""
    mc 1 u confused "\"But... wait...\""
    show k 1 u at fdis
    k "\"What is it?\""
    mc 1 u confused "\"If you came here right after class just like I did, how come you got here so much earlier than me? We didn't even run into each other on the way.\""
    show k 1 u avoid at fdis
    k "\"Oh... that... I took a shortcut.\""
    mc 1 u confused "\"A... a shortcut?\""
    show k 1 u sigh at fdis
    k "\"There's a long alley you can cross on the way here."
    show k 1 u avoid at fdis
    extend " I used it to cut my trip time by half...\""
    mc 1 u angry "\"An alley? Of all the things you could have done, you took an alley?! Don't you know how many unsavory elements can roam those? You're lucky you didn't get mugged. Of all the stupid thing you could ha-\""
    show k 1 u sad at fdis
    "I immediately stop when I notice the look on Keisuke's face."
    mc 1 u avoidb "\"... Sorry. You're already beating yourself up over it enough as it is. I don't need to pile it onto you...\""
    k "\"It's... fine...\""
    mc 1 u considerate "\"Well, you didn't get mugged so I guess it's fine. How about we just go check that alley and make sure you didn't drop your wallet there.\""
    show k 1 u sigh at fdis
    k "\"Yeah. That sounds like the best thing we can do at the moment.\""
    scene Alley
    show k 1 u avoid at fdis, five
    with fade
    "We search the alleyway top to bottom for a good twenty minutes, earning quite a few suspicious glances from passer-bys."
    "Regardless, we seem to have no success in finding the missing wallet."
    k "\"It's... it's hopeless... It's not here. It's nowhere in here.\""
    show k 1 u avoidb at fdis
    k "\"Damn it, how could I have been so careless?\""
    mc 1 u wry "\"We don't know that for a fact yet. Why don't you tell me all that happened on the way to the store? Maybe something unusual happened and you dropped your wallet then? Maybe you tripped and fell?\""
    show k 1 u avoid at fdis
    k "\"No, I think I would have remembered if something like that happened, don't you think? It was all very mundane. The most \"out there\" thing to happen was me bumping into a guy...\""
    mc 1 u curious "\"Wait... you bumped into someone?\""
    show k 1 u sigh at fdis
    k "\"Yeah. But that's completely irrelevant so I don't know w-\""
    mc 1 u confused "\"Tell me more about that.\""
    show k 1 u shock at fdis
    k "\"Wha- why? I ju-\""
    mc 1 u considerate "\"Just humor me for a second.\""
    show k 1 u avoid at fdis
    k "\"...\""
    show k 1 u sigh at fdis
    k "\"I was walking down the alleyway when this guy bumped into me. It wasn't anything huge, we just hit shoulders.\""
    show k 1 u avoid at fdis
    k "\"He must have been drunk because how else would he manage to bump into someone else in plain daylight?\""
    "..."
    "... This... can't be..."
    show k 1 u at fdis
    k "\"What? What's with that look on your face?\""
    mc 1 u fsmile "\"I...\""
    k "\"What? Tell me!\""
    mc 1 u sigh2 "\"... This guy... was he wearing a hoodie?\""
    show k 1 u shock at fdis
    k "\"Yeah! How did you know?!\""
    mc 1 u worried "\"... You didn't bump into him. You got pick-pocketed...\""
    show k 1 u shock at fdis
    k "\"{size=+2}What?!{/size}\"" with hpunch
    mc 1 u worried "\"How can you be this clueless? People don't just bump into you in plain daylight, especially in the middle of a secluded alley.\""
    show k 1 u wince at fdis
    k "\"But... but how can you know I was pick-pocketed just from that?\""
    mc 1 u sigh2 "\"Do you see your wallet anywhere?\""
    show k 1 u avoid at fdis
    k "\"... Good point...\""
    show k 1 u sigh at fdis
    k "\"Fuck... Alex is so gonna get the blame for this...\""
    mc 1 u considerate "\"Maybe... maybe he won't be that mad at you?\""
    show k 1 u avoid at fdis
    k "\"I don't know why he wouldn't be... I always pull stunts like this and he takes the fall for them... the only difference is that it never bugged me much because I'd just pay him back whenever he got a deduction on his salary.\""
    show k 1 u avoidb at fdis
    k "\"But I... I can't pay him back if he gets fired... I can't get him his job back if that happens...\""
    mc 1 u wry "\"In this case you'll just have to do your best to avoid that from happening.\""
    k "\"I... I think I should go home right now...\""
    mc 1 u shock "\"Woah woah woah, hold on!\""
    "I cut in front of him before he has a chance to storm off."
    show k 1 u worried at fdis
    k "\"What is it this time?\""
    mc 1 u wince "\"You can't go home until you file a police report. If you don't do that, you have no way to prove that your documents got stolen and the thief can use them to do whatever he wants.\""
    show k 1 u avoid at fdis
    k "\"I... fine...\""
    "Good thing he's not being stubborn right now..."
    stop music fadeout 2.5
    $ date = None
    jump cs_final
