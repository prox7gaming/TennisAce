label Day23_Shoichi:
    window hide
    scene June4 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene Bedroom
    window show
    $ date = "day23"
    play sound "music/schoolbell.ogg"
    "I move around in the bed quite a bit before finally awaking."
    "For some reason I just couldn't get comfortable during the night?"
    "I feel a desire to sleep in for a little longer..."
    "My recollections of the previous day's events come back to me slowly."
    "As soon as I remember what Shoichi and I did..."
    "Suffice to say my face feels quite hot right now."
    "Wait, where is he even?"
    show s 1 un smile at fdis, five
    "I look around for a bit, my eyes finally resting on my dresser where I see him hunched over, looking at something."
    play sound "music/fabric.ogg"
    mc 1 u smile "\"I see you finally n-{nw}"
    "?!" with hpunch
    show s 1 un shock at fdis
    mc 1 n wince "\"Ow ow ow ow ow ow!\""
    "Shoichi turns around, shocked at my suddenly crying out in pain."
    "I tried to sit up and it came out of nowhere, sending a shiver up my spine and making the fur in my neck stand at attention."
    s "\"What's going on? Are you okay?\""
    mc 1 n wince "\"I-I'm fine, just...\""
    "..."
    play sound "music/disappointment.ogg"
    "M-my ass hurts."
    "How am I even supposed to tell him something like that?!"
    s 1 un worried "\"... Just?\""
    "Ugh, please don't look at me with those worried eyes..."
    "It's seriously hard to keep a secret when you look at me like that."
    mc 1 n considerate "\"I-it's nothing. I'm fine.\""
    s 1 un wince "\"Come on, you're hiding something from me aren't you?\""
    mc 1 n "\"Y-yes. But I promise it's nothing bad. I'd just... rather not say.\""
    s 1 un "\"Rather not s-{nw}"
    show s 1 un shock at fdis
    extend " O-h.\""
    show s 1 un avoidb at fdis
    "Shoichi's cheeks started getting redder and his eyes darted away from me."
    "I guess even he's embarrassed by it..."
    if day10 == "shoichi":
        mc 1 n considerate "\"S-so. I see you discovered Yamato's tank.\""
        s 1 un wince "\"H-huh?\""
        mc 1 n considerate "\"Yamato's tank. You were looking at it just now.\""
        s 1 un shock "\"Oh! Y-yeah.\""
        show yamato2 with dissolve
        "Shoichi turns back around, staring at the cute little fish tank I have on top of my dresser."
        "Yamato, the emerald colored goldfish swims around inside, as carefree as can be."
        "The day after Shoichi gave him to me, I went to a pet store and bought the most spacious tank I could fit in my room."
        "It's got rocks and algae inside and the back of the tank is even covered with a printed film that makes it look like there are even more plants beyond the limits of the glass tank."
        "Kind of like a... real life green screen effect."
        "There certainly {i}is{/i} a lot of green inside there."
        s 1 un smile "\"He looks pretty happy.\""
        mc 1 n considerate "\"How would you tell? He's a fish.\""
        s 1 un happy "\"Call it a hunch.\""
        "Shoichi leans forward again, staring into the tank."
        "I've got to admit, it does give me a pretty nice view of his backside... what with him wearing nothing but a pair of tight fitting boxer briefs."
        "He waves at Yamato who continues to swim lazily by."
        "If he notices Shoichi at all he doesn't seem to show it."
        "... But then again, he {i}is{/i} just a fish."
        "What else would he do? Wave back?"
        mc 1 n talk "\"This is the first time you've seen Yamato's tank isn't it?\""
        s 1 un "\"Yeah. Even in the times when I came over, I haven't really gone into your room since I gave him to you so I guess it's to be expected.\""
        s 1 un think "\"And last night I didn't even notice him with the lights out.\""
        s 1 un smile "\"This is a pretty nice little tank you got for him. Do you keep the filter connected to that little hose around the back?\""
        mc 1 n "\"Yup.\""
        s 1 un happy "\"By the way, did Aki ever say anything about Yamato? You never told me his reaction.\""
        mc 1 n talk "\"Aki helps me take care of him every now and again. He's really meticulous too. He printed a cronogram for feeding times and taped it to the side of the tank.\""
        s 1 un smile "\"Hah, I knew it. There's no way you'd have been careful enough to plan this out yourself.\""
        mc 1 n sigh "\"Thanks for the vote of confidence.\""
        mc 1 n wince "\"Speaking of Aki, I messaged him last night to ask if everything was okay over at his friend's house and he hasn't answered me yet.\""
        s 1 un "\"Makes sense. He was spending the night at a friend's house. I doubt he'd be checking his phone very much during it.\""
        mc 1 n worried "\"I know. It just... worries me.\""
        s 1 un sigh "\"All Aki has to do is breathe and you'll already be worrying about the quality of the oxygen.\""
        mc 1 n sigh "\"That's not true, I'm not that bad.\""
        s 1 un sigh "\"Really? Need I remind you that on the day I gave you Yamato, you also freaked out about his having a date?\""
        mc 1 n wince "\"H-he's too young to be dating!\""
        s 1 un "\"Face it, man, you're a bit of a paranoid obsessive control freak when it comes to your brother.\""
        mc 1 n sigh "\"What?! No I'm not!\""
        s 1 un sigh "\"And also, you're in denial.\""
        mc 1 n avoid "\"... I'm not that bad.\""
        s 1 un smile "\"Hey, it's not like it's all bad. It shows you care. Just... loosen the strings a little bit.\""
        mc 1 n sigh "\"Easy for you to say, it's not {i}you{/i} that has to worry about someone's well being at almost every waking hour of the day when you're not together.\""
        s 1 un sigh "\"Seriously? I have a teenaged, rebellious baby sister that lives apart from me.\""
        mc 1 n avoid "\"... Point taken."
        play sound "music/fabric.ogg"
        "I get out of the bed, wincing when I feel another sudden flash of pain emanating from my... nether region."
        show s 1 un worried at fdis
        hide yamato2 with dissolve
    else:
        mc 1 n considerate "\"W-what are you even doing anyway? Inspecting my dresser?\""
        s 1 un wince "\"H-huh?\""
        mc 1 n sigh2 "\"My dresser. You were studying it quite intently.\""
        s 1 un think "\"O-oh. Right, right.\""
        mc 1 n sigh3 "\"Please tell me you weren't going through my stuff. {size=-4}I know I've known you for forever and all but that'd be kinda creepy.{/size}\""
        s 1 un "\"I wasn't going {i}through{/i} your dresser. I placed my phone to charge on top of it.\""
        mc 1 n shock "\"Wait, seriously? When? There was no power when we went to bed!\""
        s 1 un sigh "\"Just because you always sleep through the night doesn't mean I do. {size=-4}And you were tossing and turning a lot so it was difficult to stay asleep.{/size}\""
        mc 1 n wince "\"Oh... I don't usually move a lot in my sleep. Sorry I didn't let you sleep.\""
        s 1 un smile "\"It's quite alright.{nw}"
        show s 1 un at fdis
        extend " But yeah. The power was back on the first time I woke up so I decided to plug my phone in.\""
        mc 1 n talk "\"I think I should probably do the same. I didn't get a chance to charge my phone last night.\""
        play sound "music/phonebeep.ogg"
        "I reach for my phone and go over my messages."
        "... Nothing from Aki."
        s 1 un "\"What's with that disappointed face?\""
        mc 1 c worried "\"I... messaged Aki last night but he hasn't answered me yet.\""
        s 1 un "\"Makes sense. He was spending the night at a friend's house. I doubt he'd be checking his phone very much during it.\""
        mc 1 n worried "\"I know. It just... worries me.\""
        s 1 un sigh "\"All Aki has to do is breathe and you'll already be worrying about the quality of the oxygen.\""
        mc 1 n sigh "\"That's not true, I'm not that bad.\""
        s 1 un sigh "\"I've heard you grilling him about the friends he keeps and how long he stays out on days he doesn't have practice.\""
        mc 1 n wince "\"I-I'm just being responsible!\""
        s 1 un "\"Face it, man, you're a bit of a paranoid obsessive control freak when it comes to your brother.\""
        mc 1 n sigh "\"What?! No I'm not!\""
        s 1 un sigh "\"And also, you're in denial.\""
        mc 1 n avoid "\"... I'm not that bad.\""
        s 1 un smile "\"Hey, it's not like it's all bad. It shows you care. Just... loosen the strings a little bit.\""
        mc 1 n sigh "\"Easy for you to say, it's not {i}you{/i} that has to worry about someone's well being at almost every waking hour of the day when you're not together.\""
        s 1 un sigh "\"Seriously? I have a teenaged, rebellious baby sister that lives apart from me.\""
        mc 1 n avoid "\"... Point taken."
        "I get out of the bed, wincing when I feel another sudden flash of pain emanating from my... nether region."
        show s 1 un worried at fdis
    s "\"Are you sure you're okay?\""
    mc 1 n considerate "\"Yeah yeah, I'll live. It just caught me by surprise earlier, that's all.\""
    s 1 un considerate " \"Sorry.\""
    mc 1 n talk "\"For what?\""
    s 1 un worried "\"I... uhm... I took things too fast.\""
    s 1 un avoidb "\"I only planned on giving you o-oral but...\""
    s 1 un wince "\"I got too carried away and was even rough on you. I crossed a line and... I'm sorry.\""
    "I take a deep breath."
    "For some reason... having Shoichi freaking out in front of me calms me down immensely."
    "And I probably shouldn't tell him that cause it might upset him."
    mc 1 n talk "\"No you didn't. You're fine.\""
    s 1 un avoid "\"But I pressured you into it. You wouldn't have agreed if I didn't-\""
    show s 1 un shock at fdis
    "I walk up to him, wrapping my hand around his muzzle and forcing it shut."
    "Shoichi's eyes immediately go wide and he pulls away from me."
    s 1 un displeased "\"Hey, watch it! What do you think you're doing?\""
    mc 1 n smile "\"Keeping you from running your mouth.\""
    s 1 un scorn "\"There are nicer ways to go about that. You could have made me bite my tongue!\""
    "Oh yeah... Isn't that the same thing I did to Haruki last week?"
    "... Oops?"
    mc 1 n considerate "\"Look, I'll be honest. I was really nervous last night and yeah, you pushing me is a big part of why I went with it.\""
    mc 1 n talk "\"But that doesn't necessarily mean it was a bad thing. At least I don't feel like it was. I don't feel disrespected or taken advantage of or... anything really.\""
    mc 1 n considerate "\"In fact, now that it's happened, I feel a lot more comfortable around you because... hey, what else can we do that we haven't already?\""
    s 1 un worried "\"I... guess that's a point?\""
    mc 1 n smile "\"I mean, you're standing in front of me in just your underwear and I'm totally fine with it. Before I would feel uncomfortable even if you had a shirt on.\""
    s 1 un smile "\"Is that why you're okay with being naked in front of me?\""
    "..."
    mc 1 n blank "\"...\""
    "I look down at myself and... remember that I didn't put any clothes on yet.\""
    show s 1 un considerate at fdis
    mc 1 n flustered "\"Waaaah!\"" with hpunch
    s "\"Never mind. I spoke too soon.\""
    mc 1 n flustered "\"T-t-turn around while I put some clothes on! W-where's my underwear?!\""
    s 1 un "\"Wow. Two whole minutes without freaking out... that's a new record, actually.\""
    scene Kitchen
    show s 1 c at fdis, five
    with fade
    play music2 "music/BGM/On My Way.ogg" fadein 5.0
    play sound "music/grill.ogg"
    show hour with dissolve
    $ renpy.pause (1.0)
    hide hour with dissolve
    "The kitchen is completely taken over by the smell of toasted bread."
    "Once Shoichi and I both got dressed, we walked downstairs so we could have breakfast."
    play sound "music/disappointment.ogg"
    "... Moving around is being a little harder than I expected right now."
    "Every time I wince, Shoichi nearly lunges at me with worry."
    "Which of course just means I've begun masking them so he won't keep doing that."
    "I love the guy but he fusses over every little thing and that's just beyond annoying."
    "... Erm, platonically of course."
    "I think..."
    mc 1 c talk "\"Soooo...\""
    "I'm trying to think of something to talk about but it's proving unexpectedly hard."
    "Other than when he tries to jump to my aid, we've barely said two words to each other."
    "Even small talk would be better than nothing right now..."
    s 1 c wince "\"Y-yeah?\""
    "Ugh, why is he being so jumpy?"
    "It's hard to be calm and relaxed around someone acting like a child awaiting punishment."
    mc 1 c sigh3 "\"Come on, Shoichi, I already said everything's fine. Stop looking so guilty.\""
    s 1 c worried "\"I can't help it...\""
    play sound "music/disappointment.ogg"
    "It's been an hour since I said things were fine, why are you still freaking out?!"
    mc 1 c sigh "\"We. Are. Fine. Stop being so weird about it!\""
    "You're making it really hard for me to acting like it's not a big deal."
    s 1 c worried "\"... I just think-"
    play sound "music/tableknock.ogg"
    mc 1 c sigh3 "\"Ugh...\""
    "I groan, placing the plate with the two sandwiches I was preparing down on the counter with a loud clanking sound."
    mc 1 c sigh "\"Oh my God, you're so annoying sometimes!\""
    s 1 c worried "\"F-forgive me if I have a conscience.\""
    "Urge... to strangle... growing."
    mc 1 c sigh "\"Look, I'm only going to say this one more time. You and I are fine. I don't need or want any apologies. I don't feel slighted or disrespected. We are fine. Now sit down, shut up and eat.\""
    s 1 c shock "\"Y-yes sir.\""
    "He quickly does as I say, pulling a chair and grabbing one of the sandwiches from the plate."
    "Shoichi's has toasted bread, cheese, egg, fried chicken katsu and spicy pickled cabbage."
    "I avoided placing the devil's shredded paper on mine though."
    "That stuff has a nasty taste and texture..."
    "Instead I just took a few slices of ham to put in its place."
    s 1 c sigh "\"...\""
    "Shoichi munches on his food with a real bummed out look on his face."
    "I know that look. It's the \"I want to say something but shouldn't\" face."
    "It's amazing, even when he's being completely silent he somehow still finds a way to annoy me."
    mc 1 c talk "\"Alright, fine, out with it.\""
    s 1 c sigh "\"Out with what?\""
    mc 1 c sigh "\"Oh please, you're a terrible secret keeper. You look like a pissed off customer when he's about to leave a negative review on Yelp without saying anything to the staff.\""
    s 1 c sigh "\"Where the hell are you getting these examples?\""
    mc 1 c "\"From the internet but that's not the point. Spill.\""
    s 1 c avoid "\"... I just feel bad about yesterday?\""
    mc 1 c sigh3 "\"But {i}why{/i}?! I already told you so many times that we are fine. Why do you insist on choosing to be annoyed?\""
    s 1 c worried "\"It's not about that. I mean... I dumped a lot of my issues on your plate last night... and then in an effort to get things back on track I became forceful.\""
    s 1 c sigh "\"As soon as I... erm... {i}finished{/i} and after I woke up the first time, I started thinking more clearly.\""
    s 1 c worried "\"My mind was in a really bad place last time and I wasn't thinking straight... even before I got... uhm...\""
    mc 1 c "\"Horny?\""
    s 1 c wince "\"I-I was looking for a different word to say.\""
    mc 1 c talk "\"No reason to, we have the actual word. Carry on.\""
    s 1 c considerate "\"Look. I'm just... even if you say you're fine with it, I'm not.\""
    s 1 c worried "\"I didn't want to go that far. I wanted our first time to be more... special. I wanted to treat you right. To show you just how much you mean to me before we finally... made love.\""
    "\"Made love\"? Wow, I guess he's one of {i}those{/i} guys."
    mc 1 c sigh "\"So is that what this is about? You think our first time was bad?\""
    s 1 c wince "\"N-not \"bad\"! I never said that word. I-it was really good for me. I even got carried away during it because you were just so- I mean...\""
    s 1 c considerate "\"Look, my point is, I built this up inside my head for so long and it wasn't what I expected!\""
    s 1 c sigh "\"Suffice to say, in the scenario I pictured in my head I didn't pressure you into it, make you uncomfortable or ended up crippling you the morning after.\""
    mc 1 c sigh "\"First of all, I'm not crippled. Second of all, you're barely making any sense.\""
    show s 1 c avoid at fdis
    "Shoichi grumbles, looking away from me with a frown."
    "How is it that the dude can get laid and come out of it even moodier than he was before?!"
    "I mean, I'm the one who wound up with a sore ass so why is he complaining?"
    "At least it's easy for me to keep a clear head when he's being so ridiculous."
    "How can I put this... I'm so focused trying to calm him down that I don't have the energy to freak out myself."
    mc 1 c "\"Look, having expectations is all fine and good but if you spend months or years planning something to the finest detail, chances are reality won't be able to measure up. That's just asking to be disappointed.\""
    s 1 c worried "\"I know... I just think you deserved more.\""
    mc 1 c smile "\"Listen, big guy, I already told you I'm fine. Were things a little rushed there? Definitely, I can't disagree with that. But I don't regret anything.\""
    mc 1 c wince "\"... Well, maybe I regret not taking longer to stretch a little bit.\""
    s 1 c considerate "\"Right...\""
    mc 1 c smile "\"I got to spend the night with you, I am surprisingly relaxed about it and I don't feel nearly as self-conscious as I thought I would.\""
    mc 1 c think "\"Besides, I'm so panicky that you probably wouldn't have been able to get me to do it without some amount of coercion.\""
    s 1 c sigh "\"That just sounds dangerous.\""
    mc 1 c happy "\"Hey, if I really didn't want it I would have refused.\""
    "Not that the thought didn't cross my mind at the time but hey, he doesn't need to know that."
    "And I'll die before I admit this to him but... last night actually felt really good."
    "I'm not sure if it was worth being in pain the day after but..."
    mc 1 c "\"With that stuff hopefully dealt with, are you good?\""
    s 1 c considerate "\"... I guess?\""
    "Oh oh. That wasn't a happy \"I guess\".\""
    mc 1 c talk "\"Talk to me.\""
    s 1 c sigh "\"I already talked to you about it last night.\""
    mc 1 c worried "\"You mean... the thing about your dad?\""
    s "\"The very same.\""
    mc 1 c worried "\"I thought you said you didn't want to talk about it anymore.\""
    s 1 c wince "\"I don't {i}want{/i} to but I kind of feel like I have to.\""
    s 1 c worried "\"I've had a lot of pressure put on top of me by him my whole life. I know he's trying to push me into a career he thinks will be good for me but... I can't help but feel like it's not really... me.\""
    s "\"I mean, sure, I'd probably be very good at a management job. I'm organized, good with computers, prompt, punctual. Those are all things he drilled into me over the years.\""
    s 1 c sigh "\"He always said he wanted me to join some kind of company and make my way to the board of directors with time.\""
    mc 1 c wince "\"Isn't that pretty much your dad's career path?\""
    s 1 c considerate "\"Yup. He wants me to follow in his footsteps hardcore.\""
    s 1 c worried "\"And don't get me wrong... his plans are good. Most of what he says makes sense. I could have a really good, comfortable life if I just went with what he decided for me.\""
    s 1 c worried "\"I've told myself over the years that I was fine with it. But now that I've finally run out of time and have to give up volleyball like I promised I would... I feel so conflicted.\""
    s 1 c considerate "\"I didn't think I loved it so much, [povPetName]. It honestly scares me to realize just how hard in denial I was all these years.\""
    s 1 c worried "\"... I don't want to give it up. No matter what he says.\""
    mc 1 c worried "\"That's... I mean, I always thought you were really in denial but you constantly disagreed with me on that so I eventually decided to keep my mouth shut.\""
    s 1 c considerate "\"Sorry about that. I guess you really did know best.\""
    "Aww, if he's gonna be acting so downcast about it then I can't really gloat."
    "... Err, not that I would. No no, I would never!"
    "Also... this is a lot of information to process first thing in the morning."
    "I really want to give him my own opinion on it but..."
    "I feel like this is the sort of thing where I should just be a good boyfriend and listen to his problems."
    "I don't need to give him any advice unless he asks for it."
    mc 1 c worried "\"Do you have any idea what you're going to do about it?\""
    s 1 c worried "\"... I want to tell him that I want to continue. A-at least for the Winter competition.\""
    mc 1 c considerate "\"You know... it's going to be just as hard to give it up then as it is now.\""
    s 1 c considerate "\"I know that. Or at least I do on a rational level.\""
    s 1 c worried "\"I can't really know how I'm going to actually feel when the time comes.\""
    mc 1 c worried "\"... So you're really going to do this?\""
    s 1 c wince "\"I think so. I'll leave it for after midterms. Maybe if I show him some really high grades he'll feel charitable enough to let me.\""
    "... Hearing him say the words \"let me\" really bothers me deep deep down."
    s 1 c worried "\"W-when I do, do you think you could be there with me? You know, for moral support?\""
    mc 1 c wry "\"Of course. If this is what you really want then I'll support you 100\%\""
    s 1 c considerate "\"Thanks... I haven't officially quit the volleyball club yet so I still have some time.\""
    s 1 c wry "\"Besides, it'd be a shame if I left now that the club has the best chance of winning it's had in years.\""
    mc 1 c talk "\"You mean... because of Haruki?\""
    s 1 c smile "\"Yeah. He's still being... Haruki, but he's a lot more cooperative now.\""
    s 1 c think "\"I think getting to actually be on court for the entire match during the finals really made something click inside his brain.\""
    s 1 c smile "\"He's been surprisingly well behaved... or at least as well behaved as one would expect from him.\""
    s 1 c wince "\"If he'd been like that for longer... we probably could have won. As things stood, he didn't mesh well with the team yet due to a lack of familiarity.\""
    "Man, he starts talking volleyball and it's like an immediate mood uplift."
    "You were cowering just thinking of confronting your father two seconds ago and now you're all smiles?"
    "How did you manage to go this long seriously believing you didn't care about the sport?"
    play sound "music/disappointment.ogg"
    "You really are hopeless..."
    mc 1 c talk "\"Hopefully things work out well for you guys.\""
    s 1 c considerate "\"Yeah... I really don't want to be the only senior retiring this early.\""
    mc 1 c curious "\"Are the others all sticking with the club?\""
    s 1 c "\"Yup. For better or worse, our club only really has two types of players. The ones that don't care about their grades and admittance exams and the ones that do well enough to not need to worry about it.\""
    s 1 c think "\"And... well, then there's me. I really don't fall into either of those two camps.\""
    "You fall into the camp of demonic drill sergeant..."
    s 1 c considerate "\"You're looking at me funny...\""
    mc 1 c talk "\"I am? No, I'm pretty sure I'm looking at you pretty normally.\""
    s 1 c think "\"Hmm... Sure, if you say so.\""
    mc 1 c "\"By the way, what are your plans for today?\""
    mc 1 c smile "\"Should we go out? Stay in? Oh, maybe we could go to the arcade?!\""
    s 1 c considerate "\"Those are all wonderful ideas but... uhm... I actually will go home in like an hour or so.\""
    mc 1 c sigh "\"What? Why?\""
    s 1 c sigh "\"This is the weekend before midterms. My dad didn't even {i}want{/i} me to come here in the first place, let alone spend the night.\""
    s 1 c "\"Besides, I already goofed off for all of saturday. I really need to study.\""
    mc 1 c sigh3 "\"Study? That's your great idea on how to spend a Sunday?\""
    s 1 c sigh "\"Yes. Some of us still need to focus on their studies to get good grades.\""
    mc 1 c avoid "\"All this just to placate your father?\""
    s "\"Did you even listen to the stuff I just said to you? I need good grades to have any chances of being allowed to stay on the team.\""
    mc 1 c sigh "\"I heard... doesn't mean I like it.\""
    s 1 c considerate "\"Sorry, [povPetName]. I'd like nothing more than to spend my whole day with you but we both know that's not feasible.\""
    s 1 c smile "\"But hey, maybe Aki will have gotten home by the time I leave. Then he can keep you company.\""
    mc 1 c sigh "\"Suuure. My little brother is a perfect substitute for my boyfriend. He and I can have so much fun together the same way that I could with you.\""
    s 1 c sigh "\"I know you're being sarcastic but eugh.\""
    s 1 c "\"Don't throw a tantrum just because you're not getting your way.\""
    "Wha- A tantrum?! I don't throw tantrums!"
    "... Most of the time."
    s 1 c sigh "\"You're pouting.\""
    mc 1 c pout "\"I'm not pouting, you're pouting.\""
    s 1 c sigh "\"... Maybe I should just go home right now.\""
    mc 1 c shock "\"N-no, I was just kidding!\""
    s 1 c sigh "\"Uhuh.\""
    mc 1 c considerate "\"S-so, you'll stay for another hour, right? W-what can we do with this one hour?\""
    s 1 c "\"There isn't really much to be done. I could help you organize the house. Check if the storm last night caused any damages?\""
    mc 1 c sigh "\"Do all your ideas have to be so boring?\""
    s 1 c smile "\"Yes. It comes with the territory.\""
    play sound "music/chu.ogg"
    "Shoichi leans forward and plants a kiss on my nose."
    s 1 c smile "\"Besides, we already had a {i}lot{/i} of fun yesterday.\""
    "I feel my cheeks going red and look away pretending to cough."
    s 1 c happy "\"Hehe, you're so cute.\""
    mc 1 c avoidb "\"I don't know what you're talking about.\""
    s 1 c smile "\"Come on, this won't take long. Just have to check if the power surge yesterday didn't fry any electronics before we pulled them out of the plug.\""
    mc 1 c sigh3 "\"Do we really have to do this now?\""
    s 1 c "\"Sure. That way we can just relax for a bit before I have to leave.\""
    stop music2 fadeout 2.5
    play music3 "music/BGM/Autumn Day.ogg" fadein 5.0
    scene LivingRoom with fade
    show hours with dissolve
    $ renpy.pause(1.0)
    hide hours with dissolve
    "I'm idly browsing the internet on my phone, feeling too lazy to get out of the couch."
    "Shoichi left almost two hours ago and I've barely done anything since then."
    "I need to start preparing lunch at some point but..."
    "Eh, I don't feel like it right now."
    play sound "music/door.ogg"
    show a 1 c at fdis, fiveh with moveiridis
    "I turn around to the sound of the door being unlocked and opened."
    "A few seconds later, Aki shows up."
    a "\"Morning. Where's Shoichi-nii?\""
    "He drops the messenger bag he took to his friend's house by the side of the sofa and sits next to me."
    mc 1 c "\"He left a while ago. Said he had to study for midterms.\""
    a "\"Oh yeah. Yours are tomorrow aren't they? You should probably study too.\""
    mc 1 c sigh3 "\"I don't need to hear that from you too.\""
    a 1 c "\"Whatever you say. Was everything okay over here? I heard some areas of town lost power last night.\""
    mc 1 c "\"Your friend's house didn't?\""
    a 1 c sigh "\"No. Although a tree fell right in front of his house. Nearly missed the gate. Ended up blocking us in until it was cleared away.\""
    mc 1 c shock "\"What?!\""
    a 1 c "\"It's alright. His house is way further back from the gate's wall so it didn't even come close to it.\""
    a 1 c avoid "\"Well... it did narrowly miss the power cables though.\""
    mc 1 c sigh "\"You're not going on sleepovers again.\""
    a 1 c sigh "\"Uhuh. Sure.\""
    mc 1 c sigh2 "\"I'm being serious here.\""
    a 1 c sigh2 "\"You're being dramatic.\""
    play sound "music/fabric.ogg"
    show a 1 c at fdis
    "The little twerp rolls his eyes, getting up and walking to the kitchen."
    "I follow him around, giving him a real stink eye the whole time."
    "He used to get shape up right away when he was younger whenever I did this but nowadays it's like he doesn't even care."
    a "\"You keep doing that and your face will get stuck that way.\""
    play sound "music/disappointment.ogg"
    "I hate teenage years..."
    a 1 c "\"What about you? How was your night?\""
    mc 1 c sigh3 "\"It was like you said. Power went out. Up until then we had been watching movies and chatting.\""
    a 1 c smile "\"Did you see anything good?\""
    mc 1 c "\"You're trying to change the subject.\""
    a 1 c sigh "\"Look, you're not going to keep me from having a social life just because you're a worrywart. I'll take this up with Mom if I have to.\""
    mc 1 c sigh "\"A tree {i}fell{/i}. It {i}blocked you in{/i}. How are you not more freaked out over this?\""
    a 1 c sigh "\"Because it was a tree falling during a storm. It's hardly that rare and it's not like we have any control over it. Besides, we have trees planted right inside the house's outer gates.\""
    a 1 c "\"For all we know, we're at a higher risk of having a tree fall on our house than they are.\""
    a 1 c sigh "\"Hell, you have two trees growing right outside your window. Are we going to install a moratorium on trees now?\""
    mc 1 c sigh "\"What? \"Moratorium\"? Since when do you even know that word?\""
    "... And did he even use it right? I have no idea."
    a 1 c "\"Look, you're worried about me. I get it. It's kinda cute and all. But you don't have to go all psycho because of it.\""
    mc 1 c sigh "\"It's {i}cute{/i}? Are you seriously talking down to me right now?\""
    play sound "music/tap.ogg"
    "Aki grabs a water bottle from the fridge, taking a sip of water, giving me a couple pats on the side of my arm and walking back to the living room."
    a "\"Good talk.\""
    play sound "music/disappointment.ogg"
    "I can't believe I'm getting completely dismissed here."
    "I'm losing an argument to a child..."
    mc 1 c sigh "\"Stop trying to walk away from me.\""
    a 1 c "\"Stop trying to make up crazy rules.\""
    mc 1 c sigh3 "\"Aki, I'm just trying to look out for you.\""
    a 1 c sigh "\"I don't need you to look out for me. I'm a grown up, I can look out for myself.\""
    mc 1 c sigh "\"You're twelve!\""
    a 1 c "\"My point exactly.\""
    "Am... am I having an aneurysm? Is this what an aneurysm feels like?"
    mc 1 c sigh "\"Aki...\""
    a 1 c sigh2 "\"Look, I appreciate you worrying about me. And I swear if you try to instill rules that actually make sense, I'll do my best to follow them. But you're being way too crazy.\""
    mc 1 c sigh "\"How am I being crazy? You spent the night out on a sleepover, a tree fell in your general vicinity and as a result I'm banning sleepovers forever. What about this is crazy?\""
    a 1 c "\"... Should I just go to my room? You know, the place where things make sense and you're not allowed inside?\""
    mc 1 c sigh "\"Pfft, good luck keeping me from going inside.\""
    a 1 c "\"I installed a lock on my door.\""
    mc 1 c sigh "\"{i}You installed a lock on your door?!{/i}\""
    a 1 c sigh "\"You do know repeating what I say in that weird, huffy tone isn't going to make it any less true, right?\""
    mc 1 c sigh "\"Since when did you install a lock on your door?!\""
    a 1 c "\"Last month. And before you go apeshit over it, Mom signed off on it.\""
    "Apeshit? Where did he even learn to talk like that?"
    "Oh God... is my little brother turning into a delinquent?"
    mc 1 c sigh "\"What? No way, Mom would never agree on that.\""
    a 1 c sigh "\"Of course she would, otherwise you wouldn't have a lock on {i}your{/i} door.\""
    mc 1 c worried "\"That... that is beside the point.\""
    a "\"Mhm, sure is.\""
    mc 1 c sigh3 "\"Okay, fine. I'll let it slide this time but you're on thin ice.\""
    a "\"Whatever helps you sleep at night. I'm going up to my room. Call me if you need help making lunch.\""
    "Aki tries to slip away from me but I grab his arm before he can do so."
    mc 1 c shock "\"Wait!\""
    a 1 c sigh "\"No. You're being really annoying right now.\""
    mc 1 c avoid "\"Alright alright, fine, I'll drop it.\""
    a 1 c "\"Really?\""
    mc 1 c avoid "\"Yes. I was being unreasonable.\""
    a 1 c smile "\"You being unreasonable? Shocking.\""
    mc 1 c sigh "\"Hey, I'm trying to meet you in the middle here, don't be a twat.\""
    a "\"And what brought this sudden change of heart? It's really unlike you.\""
    mc 1 c sigh3 "\"... Shoichi grilled me over it earlier this morning when I mentioned being worried about you. Said I'm too much of an anxious mess when it comes to your safety.\""
    a "\"He's not wrong. Still, I'm sorry you had to hear that.\""
    mc 1 c sigh "\"You could try saying that without a smile on your face.\""
    a 1 c happy "\"Sorry, I'm trying, this is the best I can do.\""
    a 1 c smile "\"I guess Shoichi-nii has to be the voice of reason even when he's not here. I'll have to thank him later.\""
    mc 1 c sigh "\"You're enjoying this, aren't you?\""
    a 1 c happy "\"Immensely.\""
    "The little bastard's laughing at me now."
    "Ugh, I wish I believed in physical punishments."
    a 1 c smile "\"I wish I had gotten home earlier. I need to hang out with Shoichi-nii more.\""
    mc 1 c sigh "\"It's sad that you want to spend more time with him than you do with me.\""
    a 1 c happy "\"You said that, not me.\""
    mc 1 c avoid "\"...\""
    a 1 c smile "\"Aww, don't get upset. I still love you.\""
    mc 1 c sigh "\"I'm not upset. {size=-4}And I love you too.{/size}\""
    a 1 c smile "\"Anyway, I'm hungry. Do you need any help preparing lunch?\""
    mc 1 c smile "\"From you? You can't even cook.\""
    a 1 c sigh "\"Hey, I can be useful in other ways.\""
    mc 1 c happy "\"Alright, feel free to tell me when you discover one of them.\""
    a "\"Aren't you funny all of a sudden?\""
    mc 1 c smile "\"You give me a hard time, I give you a hard time. It's how we maintain our relationship equal.\""
    a "\"You already {i}were{/i} giving me a hard time. Just now.\""
    mc 1 c smile "\"Hmm... denied.\""
    a "\"I take it back, I think I hate you.\""
    $ date = None
    stop music3 fadeout 2.5
    jump Day24_Shoichi
