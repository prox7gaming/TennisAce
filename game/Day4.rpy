label Day4:
    window hide
    scene April9 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene Street1 with fade
    window show
    $ date = "day4"
    play music "music/crowd01.ogg" fadein 5.0
    "I still can't believe how many players were invited to Aki's club though."
    "I had somehow hoped that Kitayama (current Kanto No. 3) and Tanabe (current Japan No. 1) would be there, but..."
    "In the end, I was the only seeded player to show up. Talk about disappointing."
    "The coaches asked us to talk about our plans for the future, where I was the only one to sincerely say I planned to go pro."
    "After about four hours of us showing off shots and a few rallies here and there, they finished up the lecture and we were dismissed."
    "I somehow feel a little cheated..."
    "What should I do for the rest of the day? I don't really feel like going home."
    "It's only 10AM..."
    play sound "music/ringtone.ogg"
    "Hmm? Oh, my phone's ringing."
    play sound "music/phonebeep.ogg"
    mc 1 c curious "\"Hello?\""
    "I hear a faint gasp on the other side, followed by the sound of a clearing throat."
    "?" "\"H-Hello... [povFirstName]-san?\""
    "That voice..."
    mc 1 c curious "\"Jun?\""
    play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    j 1 c happy "\"Ah, yes. It's me, Jun.\""
    "His voice perked up considerably."
    j 1 c think "\"Uhmm... Shoichi-san gave me your phone number last week.\""
    j 1 c wince "\"So... uhm... I... I was just lounging around at my house and...\""
    "He beats around the bush quite a bit, sounding pretty nervous to be speaking on the phone."
    j 1 c wince "\"Uhmm... well... You said you were free this weekend so I was wondering i-if you wanted to hang out or something?\""
    "Huh... Just when I was wondering what to do with myself today."
    mc 1 c happy "\"Sure, that sounds like it could be fun. How about we call Shoichi too?\""
    j 1 c gentle "\"Ah, yes. I was going to call him right after inviting you.\""
    mc 1 c curious "\"Okay then. Do you mind if I invite someone else?\""
    j 1 c smile "\"Eh? No, by all means do."
    show j 1 c gentle at offscreenleft
    extend " The more the merrier.\""
    "Hearing his excited voice did wonders for my mood."
    "This Sunday somehow just got much better."
    stop music2 fadeout 2.5
    play music3 "music/BGM/On My Way.ogg" fadein 5.0
    play sound "music/phonebeep.ogg"
    "Well, time to get cracking."
    "I'll try giving Kei-kun a call."
    "I still remember the talk that we had last week. I think it would make him feel better if we made more of an effort to include him."
    "I never really considered it before but, now that I think of it, he only ever hung out with us when Saya was around."
    "I guess he just feels out of place when she isn't around."
    "Of course, that's a stupid notion. Kei-kun is friends with all of us, but..."
    "That does nothing to dispel his concerns, so I'd rather address it."
    play sound "music/calling.ogg"
    $ renpy.pause(2.0)
    k 1 c serious "\"Yes?\""
    "Kei-kun's voice echoed cleanly on the other side of the line."
    mc 1 c  "\"Kei-kun, it's me, [povFirstName].\""
    k 1 c smile "\"Ah, [povFirstName]-san, good morning. What can I do for you?\""
    "..."
    "Too formal."
    mc 1 c smile "\"We're organizing a group outing. Want to join us?\""
    k 1 c smile "\"Sounds interesting. When is it?\""
    "A mischievous idea comes to mind."
    mc 1 c laugh "\"Now.\""
    stop music3 fadeout 2.5
    play music2 "music/BGM/Punchline - Org.ogg" fadein 5.0
    k 1 c shock "\"Wha- Now?!\""
    mc 1 c laugh "\"Yes, hurry up. You're going to be late.\""
    k 1 c uncomfortable "\"Wait a m-\""
    play sound "music/phonebeep.ogg"
    "Aaaand, went through a tunnel!"
    "Oh, man. If I let my guard down, I'm going to break into a fit of laughter."
    "Now to wait until he calls me back."
    "{cps=1}3. 2. 1.{/cps}"
    play sound "music/ringtone.ogg"
    $ renpy.pause(1.5)
    play sound "music/phonebeep.ogg"
    mc 1 c happy "\"Yes, who is it?\""
    "I try my best to feign ignorance."
    k 1 c angry "\"{size=+3}Don't just hang up on someone like that.{/size}\""
    "Unable to hold back any further, I burst out laughing in the middle of the street."
    "Well, at least he's not being super polite and formal anymore."
    "So I've achieved my objective!"
    stop music2 fadeout 2.5
    play music3 "music/BGM/On My Way.ogg" fadein 5.0
    k 1 c sigh "\"Kuh, quit making fun of me..."
    show k 1 c at offscreenleft
    extend " So, where are we meeting?\""
    "Ah, come to think of it... I forgot to ask Jun where we were meeting."
    k 1 c "\"[povFirstName]-san?\""
    mc 1 c happy "\"For the time being just meet me in front of the station close to school.\""
    k 1 c sigh "\"For the time b-... You have no clue where we're going, do you?\""
    mc 1 c gentle "\"Come on, Kei-chan. Where's your adventurous spirit?\""
    "Kei-kun sighs on the other side of the line."
    k 1 c sigh "\"Senpai, please spare me your antics... Fine, I'll meet you there in an hour.\""
    k 1 c annoyed "\"Also. Don't call me \"Kei-chan\".\""
    "Mission \"Acquire Kei-kun\" was successful!"
    "I think I'll try calling Jun again to ask about the meeting place."
    play sound "music/calling.ogg"
    $ renpy.pause(2.0)
    j 1 c think "\"[povFirstName]-san?\""
    mc 1 c curious "\"Jun, I've already invited the other guy. Any luck talking to Shoichi?\""
    j 1 c happy "\"Yes, he said he was free.\""
    j 1 c wince "\"Which reminds me...\""
    mc 1 c curious "\"Yes?\""
    j 1 c avoid "\"I kinda forgot to set up a meeting place, didn't I? I'm sorry. I panicked and told him we were meeting in front of the station close to school. I hope that's okay for you because I-\""
    mc 1 c happy "\"Slow down, it's fine. I told Kei-kun to meet me there too, so everything turned out okay.\""
    j 1 c gentle "\"Ah, what a coincidence. Okay, then. When did you ask him to meet us?\""
    mc 1 c smile "\"He said he'd be there in an hour. I'll probably be a little early since I'm already out of my house anyway.\""
    j 1 c watch "\"You're not at home?\""
    mc 1 c "\"Nah. I just got out of a lecture at my little brother's tennis club.\""
    j 1 c happy "\"I see.\""
    j 1 c smile "\"That's good then. I'll be there in about an hour too.\""
    j 1 c happy "\"See you then.\""
    mc 1 c smile "\"See ya.\""
    play sound "music/phonebeep.ogg"
    "..."
    "It's about a twenty minute walk to the station. How should I kill time until then?"
    "Guess I'll just take a look at the stores nearby."
    stop music3 fadeout 5.0
    scene Station with fade
    "..."
    "Even after browsing the shops in the area, I still got here ten minutes early."
    "Well, there's nothing left for me to do so I'll just wait patiently until they arrive."
    $ renpy.pause(1.0)
    "..."
    $ renpy.pause(1.0)
    "....."
    $ renpy.pause(1.0)
    "........"
    $ renpy.pause(1.0)
    "..........."
    $ renpy.pause(1.0)
    "{size=+4}They're late!{/size}"
    play sound "music/phonebeep.ogg"
    "It's... 11:15?! What's taking them so long?"
    j 1 c gentle "\"Ah, [povFirstName]-san!\""
    "I hear Jun's voice calling me."
    show j 1 c gentle at fdis, five with moveiridis
    "I see him waving frantically amidst a group of people."
    show j 1 c gentle at fdis, two with move
    show s 1 c smile at fdis, five
    show k 1 c smile at fdis, eight
    play music2 "music/BGM/Hanging Out.ogg"
    show j 1 c wry at fdis
    j "\"Sorry I kept you waiting. I had to call Shoichi-san for help because I got lost.\""
    show s 1 c laugh at fdis
    s "\"You really should have offered to pick him up, [povFirstName]. His sense of direction is totally hopeless.\""
    show j 1 c wince at fdis, shake1
    j "\"Guh...\""
    "Well, good to see them getting along at least."
    k "\"Hey.\""
    "Kei-kun on the other hand is completely curt and to the point."
    show j 1 c watch at fdis
    show s 1 c smile at fdis
    mc 1 c curious "\"Wait. I'm not surprised that Shoichi met Jun on the way but...\""
    mc 1 c "\"Wouldn't someone drive you over here?\""
    show k 1 c annoyed at fdis
    k "\"Why? Just because I'm rich I need to have a chauffeur?\""
    mc 1 c wince "\"T-that's not what I meant. Sorry.\""
    "Kei-kun sighs."
    show k 1 c sigh at fdis
    k "\"It's fine, sorry to be so snappy. I had to deal with some family issues last night and couldn't get much sleep.\""
    show k 1 c at fdis
    k "\"To be perfectly honest, I wasn't home when you called. I was running some errands on Daigo Street.\""
    mc 1 c shock "\"Huh? That was just two streets away from where I was.\""
    show k 1 c smile at fdis
    k "\"Oh, is that so? Too bad you didn't mention it. I'd have come over to meet you.\""
    "Did I just wait alone this whole time for no reason at all?!"
    show k 1 c calm at fdis
    k "\"Anyway. What are we going to do? You didn't seem to have a plan when we spoke on the phone.\""
    mc 1 c "\"Huh? I don't. This wasn't my idea.\""
    show k 1 c worried at fdis
    k "\"What? Whose idea was it?\""
    show j 1 c happy at fdis
    "I look at Jun who is happily humming a song whilst spacing out."
    "Kei-kun follows my gaze."
    show k 1 c shock at fdis
    k "\"Wait... Kobayashi? You're kidding.\""
    show j 1 c watch at fdis
    j "\"Huh? What?\""
    "At the mention of his own name, Jun snaps back to reality."
    show s 1 c at fdis
    s "\"Jun, everyone's here already. What did you have in mind for us?\""
    show j 1 c smile at fdis
    j "\"Huh? Nothing at all.\""
    show s 1 c shock at fdis
    sk "\"Huh?!\"" with hpunch
    "Ah, if only they could see the look on their faces. Priceless!"
    show j 1 c watch at fdis
    k "\"[povFirstName]-senpai. Did you know he hadn't planned anything out?\""
    mc 1 c think "\"Well, yeah. I guessed.\""
    k "\"Huuuh?! Why didn't you say something then?\""
    mc 1 c smile "\"This is fine. We'll just think of something now.\""
    show k 1 c avoid at fdis
    k "\"Cut that out, will you? What if I had something better to do?\""
    show s 1 c smile at fdis
    s "\"You wouldn't have accepted a last minute invitation to go out without even knowing the plans.\""
    "Shoichi cuts in with a gleeful smile, apparently taking pleasure in pointing this out."
    "As always, he's pretty quick to compose."
    show k 1 c annoyed at fdis
    k "\"Kuh... Fine, you have a point.\""
    show k 1 c at fdis
    k "\"So? What are we going to do then?\""
    show j 1 c think at fdis
    show s 1 c think at fdis
    "Everyone goes silent."
    show k 1 c angry at fdis
    k "\"{size=+4}Someone say something!{/size}\""
    show s 1 c laugh at fdis
    show j 1 c watch at fdis
    s "\"You're taking this too seriously, Urushihara. We're supposed to be having fun.\""
    show s 1 c smile at fdis
    show j 1 c gentle at fdis
    j "\"Yeah, yeah. Let's just think of something fun to do.\""
    show k 1 c sigh at fdis
    "Their incredible \"go with the flow\" attitude sees Kei-kun completely defeated, sagging his shoulders in defeat."
    k "\"Fine, whatever you say. It's pointless to argue anyway...\""
    show k 1 c at fdis
    k "\"By the way, [povFirstName]-san. What do you mean you \"guessed\" he hadn't thought of anything?\""
    mc 1 c smile "\"Huh? Isn't it obvious?\""
    mc 1 c happy "\"Jun is kind of an airhead.\""
    show k 1 c hostile at fdis
    "He stares at me in shock."
    k "\"{size=-4}Then don't just casually go along with it!{/size}\""
    "Sorry, Kei-kun. Making fun of you is just too funny."
    show k 1 c avoid at fdis
    s "\"It's almost lunch time. We could look for some place to eat before everything gets too packed. We can just window shop afterwards.\""
    "Shoichi ignores Kei-kun's fit and continues as if nothing is happening."
    show j 1 c happy at fdis
    j "\"That sounds like a good idea. I'm hungry!\""
    show k 1 c hostile at fdis
    k "\"Don't just ignore m-"
    show j 1 c watch at fdis
    show k 1 c sigh at fdis
    extend " Ah, forget it, I'd have more luck talking to a wall..."
    show k 1 c avoid at fdis
    extend " I know a pretty nice place nearby.\""
    mc 1 c think "\"No offense but I think I'll veto any suggestion you make.\""
    show k 1 c shock at fdis
    k "\"W-What?! Why?\""
    mc 1 c "\"You really have to ask why? Anything you choose will probably be hopelessly expensive.\""
    show k 1 c avoid at fdis
    k "\"N-nonsense! I mean, it's not super cheap but it certainly isn't that expensive.\""
    "You come from a billionaire family that thinks a ¥18,000 per kilo ice cream is cheap..."
    show k 1 c at fdis
    mc 1 c eyesc "\"Do I need to remind you that you spent over ¥6,000 last week on two scoops of ice cream?\""
    show s 1 c shock at fdis
    s "\"Wha- Seriously? That's... impressive.\""
    show k 1 c angryb at fdis
    k "\"That isn't expensive.\""
    show s 1 c happy at fdis
    s "\"Well, that's to be expected. You have no idea how much regular people like us make, do you?\""
    show k 1 c hostile at fdis
    "Oh God, here we go again."
    k "\"W-what are you talking about? Doesn't your father make a lot of money, too?\""
    show s 1 c smile at fdis
    s "\"My father makes a decent amount, yes. He invests most of it in a trust fund and only spends the bare minimum.\""
    show s 1 c happy at fdis
    s "\"My allowance is lower than [povFirstName]'s.\""
    show k 1 c shock at fdis
    k "\"R-Really? What about you, Kobayashi-san?\""
    show j 1 c think at fdis
    j "\"Hmm? My family is poor.\""
    show k 1 c shock at fdis, shake1
    k "\"Huh?\""
    "He just said that like it's nothing. Impressive!"
    show s 1 c think at fdis
    s "\"How did you get into our school, then? It certainly isn't the cheapest.\""
    show j 1 c watch at fdis
    j "\"I received a full scholarship so I'd join the music program.\""
    show j 1 c think at fdis
    j "\"Though I later found out there isn't much of a program...\""
    show k 1 c sigh at fdis
    show j 1 c smile at fdis
    show s 1 c smile at fdis
    "Kei-kun looks away, defeated."
    show k 1 c at fdis
    s "\"I know a café around here that is pretty decent. Also cheap. We could go there, as long as his Highness is okay with being served commoner's food.\""
    mc 1 c laugh "\"I half expect Kei-kun to see the food they serve and say \"How dare you serve me such filth?\".\""
    show k 1 c angryb at fdis
    k "\"{size=+4}I wouldn't do that!{/size}\""
    show s 1 c laugh at fdis
    show j 1 c gentle at fdis
    "We all laugh."
    "Well, at least we're getting him to loosen up a bit... via extreme annoyance."
    show k 1 c sigh at fdis
    k "\"Oh, shut up. I'll go!\""
    j "\"Then it's decided. Lead the way, Shoichi-san!\""
    show j 1 c watch at fdis
    show s 1 c at fdis
    show k 1 c at fdis
    mc 1 c shock "\"Ah! Wait!\""
    "They all turn around at the last second."
    s "\"What is it, [povFirstName]?\""
    mc 1 c wince "\"We forgot to invite Saya.\""
    show k 1 c shock at fdis
    k "\"Ah...\""
    "Kei-kun looks like he finally noticed. Suddenly, it looks like the blood has drained from his face."
    show j 1 c think at fdis
    j "\"No we didn't. I called her and she didn't answer her phone.\""
    show k 1 c sigh at fdis
    mc 1 c curious "\"Oh, really?\""
    show s 1 c smile at fdis
    s "\"It's a Sunday. She's obviously still in bed.\""
    mc 1 c think "\"Oh, now that you mention it...\""
    "She does tend to sleep in whenever she can."
    k "\"Don't scare me like that. Saya-san would kill me if I forgot about her.\""
    mc 1 c curious "\"How come?\""
    show k 1 c avoid at fdis
    k "\"She told me to always invite her when I go out with you two.\""
    show k 1 c at fdis
    k "\"She said she wanted to avoid you making fun of me.\""
    show k 1 c sigh at fdis
    k "\"Now I see what she meant...\""
    s "\"Don't be a child. Do you really need Saya to defend you from the big bad bullies?\""
    show k 1 c annoyed at fdis
    k "\"Shut up!\""
    show k 1 c sigh at fdis
    k "\"Let's just get going already...\""
    stop music fadeout 2.5
    scene Restaurant
    show j 1 c smile at fdis, two
    show k 1 c at fdis, five
    show s 1 c smile at fdis, eight
    with fade
    "Shoichi takes us to a small restaurant a couple blocks away from the station."
    mc 1 c shock "\"Wow, this place looks really nice.\""
    "We take our seats in a booth far from the entrance."
    show s 1 c happy at fdis
    s "\"Isn't it? I come here very often since I always get home pretty late.\""
    mc 1 c curious "\"I guess now that your dad is out of town, you don't have anyone to prepare food for you when you get back, huh?\""
    show s 1 c smile at fdis
    s "\"Pfft. Dad preparing food? He'd just get home and order something for the two of us. But yeah, now that he's out, it's just me.\""
    show j 1 c think at fdis
    j "\"Huh? Shoichi-san, you only live with your father?\""
    show s 1 c happy at fdis
    s "\"Yes. Is that strange?\""
    show j 1 c think at fdis
    j "\"What about your mother?"
    show j 1 c wince at fdis
    extend " Oh, is she-\""
    show j 1 c watch at fdis
    show s 1 c considerate at fdis
    s "\"No, no. Nothing like that."
    show s 1 c wry at fdis
    extend " My parents got divorced when I was still in Junior High. I've been living alone with my dad ever since.\""
    show k 1 c worried at fdis
    k "\"Ah, is that so? I thought there was a more exciting story behind it.\""
    mc 1 c "\"What exactly were you thinking about? Dead mother? That isn't exactly exciting. It's just downright sad.\""
    show k 1 c at fdis
    k "\"Still. Divorce is way too cliché.\""
    show s 1 c sigh at fdis
    s "\"Yeah yeah. I'm sorry that my life isn't exciting enough for you. Maybe you should tell us your story next.\""
    show k 1 c calm at fdis
    k "\"Maybe.\""
    show j 1 c watch at fdis, five
    show k 1 c calm at fdis, seven
    show s 1 c sigh at fdis, ten
    with move
    show sa 1 m laugh at fdis, one with moveiledis
    sa "\"Good day, how may I se-"
    show sa 1 m shock at fdis
    extend " Eh?!\""
    show k 1 c shock at fdis
    show j 1 c shock at fdis
    show s 1 c happy at fdis
    kjm "\"Eh?!\""
    stop music2 fadeout 2.5
    play music3 "music/BGM/Mischief Maker.ogg" fadein 5.0
    show s 1 c laugh at fdis
    "Shoichi chuckles, trying his hardest to choke his laughter."
    "He's the {i}only{/i} person in this table that doesn't seem at all surprised by the situation."
    sa "\"Waaah?! What are you guys doing here?!\""
    mc 1 c shock "\"I could ask you the same question. We tried calling you on the phone but you didn't pick up. You work here?\""
    "Wait. This restaurant..."
    show k 1 c sigh at fdis
    k "\"This is a Maid Café, isn't it?\""
    show s 1 c laugh at fdis, fidget
    "Shoichi starts laughing uncontrollably."
    show sa 1 m avoidb at fdis
    sa "\"S-Shoichi! You did this on purpose, didn't you?\""
    "Saya's cheeks are so red that it overpowers the color of her fur."
    s "\"Sorry, sorry. I couldn't resist.\""
    show sa 1 m pout at fdis
    "Well, at least he seems to be having fun... unlike Saya, who looks like she just might murder us."
    show k 1 c avoid at fdis
    show j 1 c watch at fdis
    k "\"So Saya-san works at a Maid Café, huh...\""
    mc 1 c curious "\"What is this place even called? I didn't bother checking the name.\""
    show sa 1 m pout2b at fdis
    "Saya starts tugging on her skirt, as if trying to get it to go further down to cover more of her legs, her other hand clutching her chest as she looks away, blushing furiously."
    sa "\"B-...{size=-4}Bunnies Nest...{/size}\""
    show k 2 c gentleb at fdis
    "This time, Kei-kun is the one having to stifle his laughter, his face immediately flushes red as he desperately tries to hold back."
    show sa 1 m poutb at fdis
    sa "\"K...Kei-chan! Don't laugh.\""
    k "\"N-no, sorry. It's just... The name is too much...\""
    "Since when has Saya been working here?"
    show j 1 c happy at fdis
    j "\"This outfit suits you well, Mizoguchi-san.\""
    show sa 1 m avoidb at fdis
    sa "\"Not you too, Kobayashi-kun...\""
    show j 1 c watch at fdis
    "Saya crosses her arms, trying her best to shield herself from our view."
    "Although Jun looks like he actually meant it instead of simply trying to tease her."
    mc 1 c curious "\"How long have you even been working here?\""
    sa "\"S-since our first year of High School.\""
    mc 1 c shock "\"W-Woah. For real? How did no one ever find out?\""
    show s 1 c smile at fdis
    s "\"Pretty surprising, huh? Not at all the sort of thing you imagine Saya-chan doing.\""
    show sa 1 m doom at fdis
    "Saya's gaze turns into a glare, most of it pointed right at Shoichi."
    sa "\"Why do I feel like that was supposed to be an insult...\""
    show k 2 c think at fdis
    show sa 1 m pout2b at fdis
    k "\"How did you even find this place, Urata? It looks so normal and forgettable from the outside. The kind of shop that I'd just walk past without a glance.\""
    show s 1 c happy at fdis
    s "\"It was by coincidence. I got out of practice pretty late and this was the only place that was still open.\""
    sa "\"Yeah... we're usually open pretty late so we can snag customers leaving for their night-jobs...\""
    "Her shoulders sag as she finally gives up on any chance of retaining her dignity."
    "I just know for a fact that I'll tease her relentlessly over this for quite a while still."
    stop music3 fadeout 2.5
    play music2 "music/BGM/Lobby Time.ogg" fadein 5.0
    show sa 1 m shock at fdis
    sa "\"Oh, right!\""
    "She straightens herself up, cleaning her throat and standing upright once more."
    show sa 1 m at fdis
    sa "\"I'm still on the clock. I don't have time to be goofing around.\""
    show sa 1 m laugh at fdis
    sa "\"So, masters. What will you be having?~\""
    "That was fast!"
    "It's like she is a completely different character."
    show k 2 c gentle at fdis
    k "\"This is actually nice. I think I might start coming here more often.\""
    sa "\"Ahahaha. Master, you're so funny!\""
    show sa 1 m doom2 at fdis
    "Saya, still laughing, slowly leans towards Kei-kun."
    show k 1 c shock at fdis
    sa "\"{size=-2}Listen here. You didn't see anything, you didn't hear anything, you don't know anything. If you ever breathe a word of this to anyone I will make you run one thousand laps around the campus. Are we clear?{/size}\""
    show k 1 c uncomfortable at fdis
    k "\"Y-Yes, Ma'am!\""
    show k 1 c sigh at fdis
    show sa 1 m laugh at fdis
    sa "\"So, masters, what will you be having? Our cakes are delicious, you know~. Oh, but growing boys like you need meat, right? How about the steak?\""
    "Everything about her acting feels fake and wrong!"
    "Though I can't really fault the acting itself, I guess. It's just that, having known her for years already, this just looks so wrong..."
    "But I'm sure she could fool strangers into thinking she actually is a peppy little maid girl."
    "I pity the fool that buys into this act..."
    "Well, it doesn't really matter right now. I came here to eat, not to serve as an acting critic."
    "Hmmm... everything on their menu looks good. I just can't pick..."
    show sa 1 m at fdis
    show k 1 c at fdis
    show s 1 c smile at fdis
    s "\"Well, I already know what I'll be having.\""
    mc 1 c sigh "\"Soba noodles?\""
    show s 1 c happy at fdis
    s "\"Ding ding ding. We have a winner!\""
    show sa 1 m think at fdis
    sa "\"That's not much of a surprise. You always get soba.\""
    show s 1 c smile at fdis
    show sa 1 m at fdis
    s "\"I like routine, okay. Nothing wrong with that.\""
    show k 1 c smile at fdis
    k "\"Oh... you guys serve curry...\""
    show sa 1 m laugh at fdis
    sa "\"Yep! Our curry is the best in town, tehee~\""
    "Sorry, Saya, but... the cutesy act coming from you is disturbing..."
    show j 1 c think at fdis
    show sa 1 m smile at fdis
    j "\"Have you ever even eaten curry? I just can't picture someone like you eating curry...\""
    show k 2 c gentle at fdis
    k "\"My mom used to make it for me when I was a kid. Been years since I last had it, though...\""
    show k 1 c smile at fdis
    show j 1 c watch at fdis
    s "\"Well, I guess that means Urushihara is having the curry. I'll order some soba. What about you, Jun?\""
    show j 1 c think at fdis
    j "\"Hmmm... I guess I'll try the gyoza donburi. {size=-4}It's the cheapest thing on the menu.{/size}\""
    show j 1 c watch at fdis
    show sa 1 m happy at fdis
    sa "\"Don't worry, Kobayashi-kun. Our gyoza don is the best!\""
    mc 1 c sigh "\"You're saying that about everything on the menu.\""
    sa "\"Well, it's the truth!\""
    "Statistically unlikely..."
    show sa 1 m smile at fdis
    sa "\"Well, anyway. I'll be right back with your order, masters~\""
    mc 1 c shock "\"W-Wait! What about my order?\""
    show sa 1 m bored at fdis
    sa "\"What are you talking about?\""
    "She drops her mask of jolly good customer service for a second, leering down at me with an unfriendly expression."
    show s 1 c laugh at fdis
    s "\"Your order? Now that's a good joke. As if you're not going to take an hour just to pick something.\""
    sa "\"Yeah, I can't keep waiting forever.\""
    mc 1 c annoyed "\"I don't take that long to choose!\""
    show sa 1 m sigh at fdis
    show s 1 c sigh at fdis
    s "\"Last time we went to the Ramen Shop close to your house, it took you half an hour just to decide on the toppings.\""
    mc 1 c sigh2 "\"I'll have you know that ramen is a form of art. You can't just throw random toppings at it!\""
    s "\"Sure, whatever you say.\""
    show s 1 c smile at fdis
    s "\"Saya-chan, please bring us our order.\""
    mc 1 c avoid "\"W- I already... Gaah, fine!\""
    show sa 1 m at fdis
    menu:
        "\"Give me soba.\"":
            mc 1 c annoyed "\"There. That didn't take long, see?!\""
            show s 1 c happy at fdis
            s "\"Copying other people doesn't count, though.\""
            mc 1 c sigh "\"There's just no winning with you, is there...\""
            show s 1 c smile at fdis
            s "\"Sorry, I already know all your buttons. I'll always win.\""
            show s 1 c happy at fdis
            s "\"Saya-chan, if you please.\""
            show sa 1 m laugh at fdis
            sa "\"Of course~\""
            "Saya bows to us one more time."
        "\"Curry!\"":
            s "\"So you're copying Urushihara, huh? Couldn't you at least choose something less generic?\""
            show k 1 c annoyed at fdis
            show j 1 c wry at fdis
            k "\"This coming from the plain soba guy? Now that's rich.\""
            show k 1 c at fdis
            show s 1 c annoyed at fdis
            s "\"Hey, at least soba has a centuries long tradition of refinement, being prepared by the best noodle artisans in Japan. Curry is just a Japanese version of an Indian dish.\""
            show k 1 c annoyed at fdis
            k "\"It still had to be created and refined. You're just prioritizing the soba because it's a national dish!\""
            "Seriously? You two are going to fight over food now?"
            show k 1 c shock at fdis
            show s 1 c shock at fdis
            sa "\"Uhmm... masters, quiet down please. {size=-2}We do have other customers...{/size}\""
            "Upon Saya's prompting, they scan around the restaurant to find that most of the surrounding tables are staring at us with annoyed faces."
            show k 1 c avoidb at fdis
            show s 1 c avoidb at fdis
            sk "\"Sorry...\""
            show sa 1 m laugh at fdis
            sa "\"Okaay~. I'll be right back with your orders~\""
            "Everyone nods."
        "\"I'll have the gyoza don.\"":
            show k 1 c at fdis
            k "\"You too? Don't you think you need something a little more substantial than gyoza?\""
            show s 1 c at fdis
            s "\"You know, [povFirstName], you don't gain any points if you just copy other people's answers.\""
            mc 1 c annoyed "\"This isn't a test!\""
            show j 1 c gentle at fdis
            "Jun starts laughing out of nowhere, taking us by surprise."
            k "\"What's so funny?\""
            j "\"No, nothing. I just thought that this kind of thing is nice.\""
            s "\"What kind of thing?\""
            show j 1 c smile at fdis
            j "\"Hanging out with friends.\""
            k "\"This is pretty normal for this group here.\""
            show s 1 c wry at fdis
            s "\"Well, he's never tagged along before, remember?\""
            show k 1 c avoid at fdis
            k "\"Ah, yeah, that's true...\""
            "We hadn't met Jun until a week ago, after all."
            sa "\"Ehem!\""
            show s 1 c smile at fdis
            show k 1 c smile at fdis
            show j 1 c happy at fdis
            show sa 1 m laugh at fdis
            sa "\"So, masters, I'll make sure to be right back with your orders~\""
            "Everyone nods."
    show s 1 c at fdis
    show k 1 c at fdis
    show j 1 c watch at fdis
    show sa 1 m at fdis
    sa "\"Ah, and before I forget.\""
    show sa 1 m smile at fdis
    sa "\"Sho.{w=0.5}{nw}"
    show sa 1 m laugh at fdis
    extend "I.{w=0.5}{nw}"
    show sa 1 m happy at fdis
    extend "Chi~{w=1.0}{nw}"
    show sa 1 m doom2 at fdis
    extend " {size=-4}{cps=-20}If you ever pull this sort of stunt again I'll let everyone know about your little secret, am I clear, you little bastard?{/cps}{/size}\""
    show s 1 c shock at fdis
    "The aura of violence around her is so strong that I start to feel cornered just by being nearby her."
    "Shoichi immediately shrinks back in his seat, quaking in fear."
    show sa 1 m laugh at fdis
    sa "\"Okay~ Please just wait for a little bit~\""
    show sa 1 m at offscreenright with moveoridis
    show j 1 c at fdis, two
    show k 1 c at fdis, five
    show s 1 c sigh at fdis, eight
    with move
    "Shoichi is still quaking in terror after Saya leaves."
    s "\"I-I could feel myself losing a few years of my life...\""
    mc 1 c curious "\"What's this secret she's talking about, though?\""
    show s 1 c considerate at fdis
    s "\"N-nothing. It's nothing at all.\""
    show k 1 c calm at fdis
    k "\"Oh, I dunno. From the look on his face, I'd say it's probably something monumental.\""
    show s 1 c wince at fdis
    s "\"S-Shut up!\""
    k "\"You denying it so vehemently only makes us want to know even more.\""
    show s 1 c avoidb at fdis
    s "\"That's not my problem.\""
    mc 1 c happy "\"Then you won't mind if we sniff around to find out what you've been hiding, do you?\""
    show s 1 c shock at fdis
    s "\"Wha-\""
    show k 2 c gentle at fdis
    k "\"Oh, I bet he has some girlfriend that he's hiding!\""
    show j 1 c gentle at fdis
    j "\"Maybe Shoichi-san is dating a beautiful college age big sister type and didn't want anyone to find out.\""
    show s 1 c blush
    s "\"W-wait a sec-\""
    mc 1 c laugh "\"I see. Shoichi, you sly dog.\""
    show s 1 c annoyedb at fdis
    s "\"Would you all just shut up!\""
    show k 1 c smile at fdis
    show j 1 c watch at fdis
    k "\"See? Not fun when you're the one being made fun of all the time, right?\""
    s "\"Ah, shut up already. {size=-4}I'm sorry, okay.{/size}\""
    show j 1 c think at fdis
    j "\"I think the one you should be apologizing to is Mizoguchi-san... She didn't seem at all happy to see us here.\""
    mc 1 c sigh "\"Yeah. If Saya went through the trouble of hiding this from us for this long then she surely didn't want you bringing everyone here.\""
    show s 1 c sigh at fdis
    s "\"Alright, alright. I'll apologize once her shift is over...\""
    show k 1 c haughty at fdis
    k "\"Do you think she'd tell us about this secret he's hiding?\""
    show s 1 c annoyedb at fdis
    s "\"{size=+2}Don't you dare!{/size}\""
    mc 1 c smile "\"Shoichi, everyone's looking at us.\""
    show s 1 c blush at fdis
    s "\"Ah...\""
    "This is what happens when you shout. Now all the surrounding tables are glaring daggers at us again."
    s "\"I-I'm sorry to disturb you...\""
    "He manages to stutter an apology, his face completely red."
    show k 1 c calm at fdis
    k "\"We just might give him an aneurysm if we keep this up. I say we go for it.\""
    show s 1 c annoyedb at fdis
    s "\"Shut up.\""
    show j 1 c gentle at fdis
    j "\"That actually sounds like it might be fun.\""
    s "\"Not you too!\""
    mc 1 c laugh "\"Shoichi, control your voice.\""
    "He freezes again, looking around to see if any tables are looking our way again."
    "Once he ascertains that they are not, he relaxes."
    show s 1 c avoidb at fdis
    s "\"{size=-2}What are you guys doing to me?{/size}\""
    show k 2 c gentle at fdis
    k "\"Think of it as divine punishment.\""
    show s 1 c annoyedb at fdis
    s "\"{size=-2}If it were divine, it wouldn't be coming from you three devils.{/size}\""
    show j 1 c watch at fdis
    j "\"3? Am I a devil too?\""
    s "\"{size=-2}Don't play coy, you joined them in teasing me!{/size}\""
    j "\"I did?\""
    s "\"{size=-2}Wha-{/size}\""
    show s 1 c sigh at fdis
    s "\"{size=-2}Jun, you need to be a little more self-aware.{/size}\""
    show j 1 c wince at fdis
    "Jun blinks in confusion."
    mc 1 c smile "\"You don't need to keep whispering, you know.\""
    show s 1 c avoidb at fdis
    s "\"{size=-2}I don't want to risk it.{/size}\""
    show k 1 c smile at fdis
    k "\"Little doggy here is too much of a good boy to disturb other patrons.\""
    show s 1 c scorn at fdis
    s "\"What'd you say, you bastard?\""
    show k 1 c calm at fdis
    k "\"There, I fixed him.\""
    show s 1 c avoidb at fdis, shake1
    s "\"Kuh...\""
    "It's not often that Shoichi gets toyed around like this."
    "And Kei-kun just hit a nerve right now."
    hide sa 1 m
    "Maybe..."
    menu:
        "Pile it on.":
            stop music2 fadeout 2.5
            play music3 "music/BGM/Mischief Maker.ogg"
            $ mess_with_shoichi = True
            "I'll just have a little bit more fun and then I'll stop."
            show j 1 c watch at fdis
            mc 1 c laugh "\"Oh, come on, Kei-kun, don't say it like that. Poor Sho-chan is already blushing so hard.\""
            show s 1 c shock at fdis
            s "\"Wha- [povFirstName]?!\""
            show k 2 c gentle at fdis
            k "\"Oh, it's true. His face is so red.\""
            mc 1 c laugh "\"Sho-chan, you're so earnest~\""
            "I try imitating the cutesy act that Saya was putting on."
            show s 1 c avoidb at fdis
            show j 1 c gentle at fdis
            "Shoichi's face immediately goes completely red."
            "He puts both his arms on the table and buries his face in them."
            show k 1 c smile at fdis
            s "\"{size=-4}W-What are you doing to me?!{/size}\""
            show j 1 c watch at fdis
            j "\"Oh, his tail is wagging.\""
            "Jun, who had been sitting right next to Shoichi, says it matter-of-factly."
            "Shoichi nearly jumps from his seat."
            show s 1 c shock at fdis, shake1
            s "\"Whaaa- J-Jun-kun, shut up!\""
            show j 1 c wince at fdis
            j "\"Huh?\""
            "Looks like Jun still hasn't caught on to what we're doing. Bless his innocent heart."
            show k 2 c gentle at fdis
            show j 1 c watch at fdis
            k "\"Wow, it's true. His tail is wagging super fast. He could probably sweep the floor with that thing.\""
            show s 1 c avoidb at fdis
            mc 1 c suggestive "\"Did my praising you really make you that ha-\""
            s "\"Please! Change the subject already!\""
            "Shoichi cuts me off before I can finish."
            mc 1 c laugh "\"My, my. Sho-chan, you're so delicate~\""
            "He buries his face in his arms again."
            s "\"I accepted defeat. Now stop, please. My face is so hot right now...\""
            show k 1 c calm at fdis
            k "\"Heh, I've already had my fun.\""
            mc 1 c happy "\"Yeah, this is a good stopping point.\""
            j "\"Stopping point for what?\""
            s "\"A lot more self-aware...\""
            "Shoichi mumbles it out, much to Jun's confusion."
            stop music3 fadeout 2.5
        "Stop tormenting him.":
            $ mess_with_shoichi = False
            "Alright, enough already."
            "While it would truly be deserved for him to suffer teasing and humiliation on par with what he caused Saya, I just don't have the heart to do that to him."
            show k 1 c at fdis
            mc 1 c sigh "\"Come on, Kei-kun, stop that. A restaurant isn't the sort of place to do this kind of stuff.\""
            show k 1 c worried at fdis
            k "\"You're bailing him out already? Come on, at least let me mess with him a little.\""
            mc 1 c "\"If we were in private, I might have, but I don't want to cause a scene in public. Just leave him alone for now, okay?\""
            show k 1 c avoid at fdis
            k "\"Tch. And yet it's fine when he does it.\""
            "Yeah, I can see how it would be a little shitty. It's true that this is a double standard."
            "Sorry, Kei-kun. I'll try to keep an eye to avoid situations like this happening to you in the future too."
            show s 1 c considerate at fdis
            s "\"Thanks, [povFirstName].\""
            mc 1 c happy "\"I didn't do it for you, I did it for the other patrons.\""
            "Shoichi chuckles, his soft voice carrying through the air like music."
            show s 1 c wry at fdis
            s "\"Still... Thanks.\""
            "I shrug."
    if mess_with_shoichi == True:
        play music2 "music/BGM/Lobby Time.ogg" fadein 5.0
    show j 1 c watch at five
    show k 1 c at seven
    show s 1 c at ten
    with move
    show sa 1 m laugh at fdis, one with moveiledis
    sa "\"Alright, it's ready~\""
    if mess_with_shoichi == True:
        show sa 1 m at fdis
        sa "\"Huh? Shoichi, why are you hiding your face on the table?\""
        show k 1 c smile at fdis
        k "\"He's had a brain meltdown.\""
        show s 1 c sigh at fdis
        s "\"Kuh... Who do you think is at fault for that?\""
        show k 1 c calm at fdis
        k "\"Hey, I might have had a hand in this but [povFirstName]-san did most of the work.\""
        s "\"I hate you all...\""
        show k 1 c smile at fdis
        k "\"No you don't.\""
        show s 1 c avoid at fdis
        s "\"... No, I don't.\""
        "Shoichi takes a few deep breaths, seemingly trying to calm himself again."
        "He still can't look us in the eye, though."
        show sa 1 m think at fdis
        sa "\"Hmm... I want to hear the details later.\""
        show s 1 c shock at fdis
        s "\"Wha- Saya!\""
        show sa 1 m doom2 at fdis
        sa "\"This is what you get for outing my secret, you big lug~\""
        show s 1 c wince at fdis
        "Saya flashes a smile full of malicious glee."
        show sa 1 m laugh at fdis
        sa "\"Well, anyhow~\""
    else:
        sa "\"Be careful, it's piping hot!\""
    "She swiftly sets our plates on the table."
    sa "\"Shall I bring anything to drink?\""
    "I'm surprised of how fitting this mild-mannered attitude is to her."
    "How should I put it..."
    "I guess if I were to forget her true character, I could actually be fooled by this act."
    "Yeah, it doesn't seem out of place at all when I think like that."
    scene Restaurant
    show j 1 c smile at fdis, five
    show k 1 c calm at fdis, seven
    show s 1 c smile at fdis, ten
    show sa 1 m laugh at fdis, one
    with fade
    sa "\"I hope to see you again soon, masters!\""
    "As we're leaving, Saya waves at us with a smile on her face."
    show sa 1 m doom2 at fdis
    sa "\"{size=-6}I swear if any of you ever come here again I'll...{/size}\""
    "...though it does little to hide her malicious aura."
    scene Station
    show j 1 c smile at fdis, two
    show k 1 c at fdis, five
    show s 1 c at fdis, eight
    with fade
    play music "music/crowd01.ogg" fadein 5.0
    if mess_with_shoichi == True:
        stop music2 fadeout 2.5
        play music3 "music/BGM/Hanging Out.ogg" fadein 5.0
    else:
        stop music3 fadeout 2.5
        play music2 "music/BGM/Hanging Out.ogg" fadein 5.0
    "We go back to the main street in front of the station."
    "It seems we just hit rush hour, as many people keep pouring out of the station."
    "The streets that until now only had a couple passer-by's here and there are now packed with endless waves of people."
    show j 1 c fluster at fdis, fidget
    j "\"Uhh...\""
    "Jun starts fidgeting uncomfortably, walking closer to me than before. His hand keeps brushing up against my arm multiple times."
    show k 1 c worried at fdis
    k "\"Are you alright, Kobayashi-san? You seem a bit on edge.\""
    "Kei-kun seems to be a bit more mindful of Jun than you'd normally expect him to be."
    "He keeps shooting curious glances at the tiger every few seconds."
    show s 1 c think at fdis
    s "\"Ah, that's right. I forgot that Jun-kun doesn't deal well with crowds.\""
    show k 1 c shock at fdis
    k "\"Waah, seriously?\""
    if jun_met == True:
        mc 1 c wince "\"Oh, crap. I think I remember him saying something about it when we first met.\""
    else:
        mc 1 c shock "\"Really? That's the first I've heard of it!\""
        show s 1 c wry at fdis
        s "\"He mentioned it to me when I was getting him properly introduced to the school buildings and the teachers.\""
        mc 1 c wince "\"Good thing you remember these tiny details...\""
    mc 1 c worried "\"We should probably find a quieter place so he can relax.\""
    show s 1 c think at fdis
    s "\"Hmm...\""
    "Shoichi starts looking around. This is one of those situations where his crazy height makes him useful since he can easily see over the mass of people."
    show s 1 c smile at fdis
    s "\"Ah, there's a sweets shop over there that is almost empty. We could go there for a while.\""
    show k 1 c sigh at fdis
    k "\"Are you sure you're not just saying this because you want to eat some sweets?\""
    show s 1 c happy at fdis
    s "\"Nothing wrong with mixing business with a little bit of pleasure.\""
    show k 1 c uncomfortable at fdis
    k "\"Oh God, that sounded so incredibly wrong.\""
    "Well, good to see at least they are enjoying themselves."
    show j 1 c flustert at fdis, fidget
    j "\"Uuuhhh...\""
    play sound "music/tap.ogg"
    "Meanwhile, Jun has grabbed hold of my arm and is now squeezing it tightly."
    "...!"
    if mess_with_shoichi == True:
        stop music3 fadeout 2.5
        play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
    else:
        stop music2 fadeout 2.5
        play music3 "music/BGM/Mischief Maker.ogg" fadein 5.0
    "W-what's with this crazy strong grip? Crap, I think he's cutting the blood flow to my arm!"
    show k 1 c shock at fdis
    show s 1 c at fdis
    mc 1 c frightened "\"Whatever you do, do it fast, before this living tourniquet makes me lose my arm.\""
    show s 1 c happy at fdis
    "Shoichi chuckles, grabbing hold of Jun's shirt collar and dragging him towards the store."
    "And in the process, I get dragged along with them since Jun refuses to let go of my arm."
    stop music fadeout 2.5
    scene Sweets
    show j 1 c flustert at fdis, two
    show k 1 c worried at fdis, five
    show s 1 c smile at fdis, eight
    with fade
    "By the time we manage to squeeze our way through the crowd of people and into the shop, both Jun and I are almost seeing stars."
    s "\"Jun-kun? Jun-kun! It's okay, you can open your eyes now.\""
    show j 1 c shock at fdis
    j "\"Eh?\""
    "Jun finally snaps out of it, looking around in confusion."
    show j 1 c wince at fdis
    j "\"Where... are we?\""
    show j 1 c shockb at fdis
    mc 1 c wince "\"Shoichi took us into a nearby store now wouldyoupleaseletgoIcan'tfeelmyarm!\""
    if mess_with_shoichi == True:
        stop music3 fadeout 2.5
        play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    else:
        stop music2 fadeout 2.5
        play music3 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    j "\"Ah!\""
    show k 1 c sigh at fdis
    "He finally notices the fact that he still has a death grip around my arm and releases it."
    "I can feel it. I can feel my arm again! Oh happy day!"
    show j 1 c blush at fdis
    j "\"S-Sorry... I'm not good with crowds...\""
    show k 1 c sigh at fdis
    k "\"No kidding.\""
    "Jun rubs his cheeks in embarrassment."
    show s 1 c happy at fdis
    s "\"Come on, none of that matters now. And since we're here in this beautiful store anyway~\""
    "Shoichi starts rubbing his hands, looking like one of those stereotypical, scheming villains that you see in really bad action flicks."
    show s 1 c laugh at fdis
    s "\"Excuse me, can I have three green tea flavored rice cakes? Thank you.\""
    "He hands a bill to the clerk and takes a small paper bag with the sweets."
    show j 1 c shockb
    j "\"Ah...\""
    "Jun whimpers as he sees Shoichi start eating."
    "Shoichi notices it immediately."
    show s 1 c think at fdis
    s "\"Do you want some?\""
    show j 1 c wince at fdis
    j "\"Ah, no no. I don't want to impose.\""
    show s 1 c happy at fdis, five
    show k 1 c worried at fdis, eight
    with move
    s "\"It's no imposition. Here, take one.\""
    "Shoichi walks up to Jun, handing one a cake with a big smile on his face."
    show j 1 c sigh at fdis
    j "\"W-well, if you're really offering then I guess...\""
    "He tries to nonchalantly play it off as if it weren't a big deal, even though his face easily gives it away."
    show j 1 c happy at fdis
    j "\"Hmmm, so good~\""
    show s 1 c smile at fdis, six with move
    s "\"Urushihara, you want one too?\""
    show k 2 c sigh at fdis, nine with move
    k "\"I'll pass. I can't stand Japanese sweets.\""
    show k 1 c avoid at fdis
    "Kei-kun stares at the little rice cake with a measure of disgust that I didn't think was possible from him."
    show k 1 c worried at fdis
    k "\"Plus, if you only have one left then shouldn't you be offering it to [povFirstName]-san first?\""
    show s 1 c laugh at fdis, eight
    show k 1 c worried at fdis, five
    with move
    s "\"Pfft, as if. He hates green tea with a passion.\""
    mc 1 c "\"It's true, I really do.\""
    "I nod to emphasize my point, looking down at the green tea treat with disgust equal to Keisuke's."
    "Shoichi finishes eating both of his sweets and puts the bag in the trash, dusting his hands as he does so."
    show s 1 c smile at fdis
    show k 1 c at fdis
    show j 1 c smile at fdis
    s "\"Well, then I guess we should be going...\""
    show j 1 c fluster at fdis
    j "\"Eh? Can't we stay here just a little longer?!\""
    "Jun asks, half pleading."
    show s 1 c think at fdis
    "Shoichi looks to at least be considering it."
    "Well, if it's Shoichi we're talking about then his next move will probably be..."
    show s 1 c happy at fdis
    s "\"There's a karaoke just around the corner. How about we go there?\""
    "Suggesting something nearby just so he can please Jun."
    "Yep, just as easy to read as always."
    show j 1 c wince at fdis
    j "\"Aren't karaoke places kinda... expensive?\""
    show k 1 c smile at fdis
    show j 1 c watch at fdis
    k "\"It's fine. If the four of us pitch in, we can get a room for a couple of hours dirt cheap.\""
    show s 1 c smile at fdis
    s "\"Oh, I'm surprised you know about that. You go to karaoke often?\""
    show k 1 c avoid at fdis
    k "\"Every now and then.\""
    show j 1 c gentle at fdis
    j "\"Ah, then I'm looking forward to seeing you sing, Urushihara-san!\""
    show k 1 c worried at fdis
    show j 1 c watch at fdis
    k "\"N-no, I don't sing in public...\""
    show s 1 c sigh at fdis
    s "\"Don't say that. What are you going to be doing if you're not gonna take part?\""
    show k 1 c calm at fdis
    k "\"I'm going to make fun of how bad you are. Isn't that obvious?\""
    show s 1 c doom at fdis
    s "\"You trying to pick a fight?\""
    show s 1 c avoid at fdis
    show k 1 c smile at fdis
    mc 1 c sigh "\"Okay! Let's not cause another scene in public, shall we?\""
    "They seem to have complied for the time being... even though they continue glaring at one another."
    "Good grief, it's like walking around with a bunch of fifth graders..."
    scene Karaoke
    if mess_with_shoichi == True:
        stop music2 fadeout 2.5
        play music3 "music/BGM/Lobby Time.ogg" fadein 5.0
    else:
        stop music3 fadeout 2.5
        play music2 "music/BGM/Lobby Time.ogg" fadein 5.0
    show j 1 c gentle at fdis, two
    show k 1 c smile at fdis, five
    show s 1 c smile at fdis, eight
    with fade
    j "\"Wow, this place is so pretty. And it even has air conditioning!\""
    show j 1 c gentle at fdis, offscreenleft
    show k 1 c sigh at fdis, three
    show s 1 c wry at fdis, seven
    with move
    "Jun runs up to the \"air conditioner\" and shoves his face in front of the main fan."
    j 1 c gentle "\"So coooool!\""
    show j 1 c gentle at fdis, two
    show k 1 c worried at fdis, five
    show s 1 c wry at fdis, eight
    with move
    k "\"He... he does know that's just a regular fan right?\""
    mc 1 c considerate "\"I don't think he cares about the difference right now.\""
    "The rapidly spinning blades distort his voice, making it sound robotic."
    "The three of us watch in astonishment as his childish delight over common objects comes out full force."
    j 1 c think "\"Is this the karaoke machine?\""
    "He touches a black box that is standing below a giant plasma screen and it immediately lights up."
    show j 1 c shock at fdis
    j "\"Ahh! Did I break it?\""
    show k 1 c smile at fdis
    k "\"Oh, this one has \'touch buttons\'. The place I usually go to doesn't have them yet.\""
    show j 1 c wince at fdis
    j "\"T-tachi botan?\""
    "It seems that the English has stumped him quite a bit."
    s "\"Touch {i}button{/i}. That means instead of having to actually press down a clickable button, it has a surface that recognizes your touch instead.\""
    show j 1 c shockb at fdis
    show s 1 c happy at fdis
    show k 2 c gentle at fdis
    j "\"Wooahh. So high tech.\""
    "Well, it's true that his enthusiasm puts us all in a better mood."
    mc 1 c smile "\"Not really. It's pretty average, most DVD and Blu-ray players nowadays use those.\""
    show k 1 c calm at fdis
    k "\"It's pretty new for karaoke machines though, especially commercial ones. After all, due to the heavy workload, they have to make sure they're durable so they can't just cram in new features.\""
    mc 1 c talk "\"True.\""
    show k 1 c smile at fdis
    "Kei-kun sits down at the seat closest to the air conditioning machine, picking up the portable tablet screen that shows the music list."
    play sound "music/fabric.ogg"
    k "\"So, who's going to...\""
    show j 1 c gentle at fdis, four with move
    j "\"Me me me! Let me go first!\""
    show k 1 c shock at fdis, six with move
    "Jun nearly crawls over Kei-kun, pressing his face so close to his that they almost touch."
    "Kei-kun jumps back in his seat, completely taken aback."
    k "\"Alright alright, take it! Here's the controller!\""
    "Kei-kun hands him the device."
    show j 1 c think at fdis
    j "\"How do I use this?\""
    "Jun taps the pen on a bunch of different places on the screen, making the TV flash a bunch of random lists."
    show k 1 c sigh at fdis
    k "\"Ah, give this to me!\""
    "Unable to watch it anymore, Kei-kun snatches the controller from his hand and puts it back on the song selection screen."
    k "\"Just choose a song and I'll play it for you.\""
    show j 1 c gentle at fdis
    j "\"Okay!\""
    scene Karaoke
    show j 1 c happy at fdis, two
    show k 2 c gentle at fdis, five
    show s 1 c smile at fdis, eight
    with fade
    if mess_with_shoichi == True:
        stop music3 fadeout 2.5
        play music2 "music/BGM/Fretless.ogg" fadein 5.0
    else:
        stop music2 fadeout 2.5
        play music3 "music/BGM/Fretless.ogg" fadein 5.0
    j "\"Yay!\""
    "Jun's singing is full of passion and excitement. It's more than clear that he's not focused on singing perfectly and is instead just trying to have fun."
    "Even though his voice is nothing to write home about, his natural charisma makes you enjoy watching him."
    "From the corner of my eye, I see Kei-kun tapping his hand on his legs to the rhythm, silently watching as well."
    "Shoichi is merrily humming alongside the music. It seems he also likes this song quite a bit."
    "It's a nice atmosphere."
    if mess_with_shoichi == True:
        stop music2 fadeout 5.0
    else:
        stop music3 fadeout 5.0
    "Eventually, Jun's song ends. He sits down, huffing and puffing."
    show j 1 c gentle at fdis
    j "\"Ahh... that was a lot more draining than I thought.\""
    show s 1 c happy at fdis
    s "\"But did you have fun?\""
    j "\"Yeah!\""
    show s 1 c smile at fdis
    s "\"Then that's all that matters. Look, the machine is giving you a score now.\""
    mc 1 c curious "\"They give out scores?\""
    show k 1 c smile at fdis
    k "\"The newer ones do.\""
    "The machine reads \"Calculating your score, please wait...\" for a few seconds. Jun shifts closer to the screen, waiting impatiently for it."
    "Then, the screen blinks. \"Your score is: 71! Congratulations.\" is what it says."
    show j 1 c pout at fdis
    j "\"Just 71? Booo. Let me try again.\""
    show k 1 c scorn at fdis
    k "\"Let other people have their turn.\""
    show j 1 c wince at fdis, shake1
    "I'm sure he didn't mean to, but Kei-kun's voice just now was a bit more stern than necessary. Not to mention his eyes..."
    show k 1 c uncomfortable at fdis
    show j 1 c watch at fdis
    k "\"Sorry...\""
    "He immediately noticed how it affected Jun though, making sure to apologize promptly."
    show k 1 c worried at fdis
    "He leans back on his seat, uncomfortable."
    show s 1 c considerate at fdis
    s "\"W-Well...\""
    "It seems even Shoichi is at a loss."
    "What was that about?"
    show s 1 c seductive at fdis
    s "\"Urushihara... could it be that you want to sing?\""
    show k 1 c uncomfortable at fdis
    k "\"N-no...\""
    show s 1 c happy at fdis
    "Ah, I see what's going to happen even before it happens."
    s "\"Okay, then. You sing.\""
    show k 1 c shock at fdis
    k "\"H-huh? Me? No way!\""
    show s 1 c smile at fdis
    s "\"Then how about a competition?\""
    show k 1 c avoid at fdis
    "Kei-kun's ears immediately turn towards Shoichi. Slowly, he turns his head in his direction."
    show k 1 c at fdis
    show s 1 c happy at fdis
    k "\"What do you have in mind?\""
    "... I don't know if I should congratulate Shoichi for manipulating Kei-kun that easily."
    show s 1 c smile at fdis
    s "\"We each sing a song, then we'll have these two decide who was the best singer. The loser has to buy lunch for the winner.\""
    show k 1 c sigh at fdis
    k "\"That's all? That's a pretty boring winning prize.\""
    show s 1 c sigh at fdis
    s "\"Not all of us are rich, you know?\""
    show k 1 c doom at fdis
    k "\"So you're saying you're afraid of losing?\""
    "Keh, what's with that face? It's scary!"
    show s 1 c at fdis
    s "\"I'm saying it's a possibility.\""
    show k 1 c serious at fdis
    "Kei-kun's eyes narrow as he considers the idea. He silently muses over it for a few seconds before-"
    show k 2 c cocky at fdis
    k "\"Don't regret it when you lose.\""
    show s 1 c smile at fdis
    "Shoichi smiles again."
    play music2 "music/BGM/Fretless.ogg" fadein 5.0
    show k 1 c serious at fdis
    "Kei-kun stands in place, gripping the microphone tightly with one hand and placing the other on his pocket."
    "Somehow, he looks far more imposing with that mic in his hands."
    "The songs starts playing. It's a rock song that does not match at all with the image of Keisuke that I have in my head."
    "I thought he would pick something more classical sounding..."
    "As the air starts getting more and more tense, I see the screen indicating that the vocals should begin in a few seconds."
    "Instinctively, I hold my breath."
    "Keisuke's voice echoes through the room, crashing against us like countless waves."
    show j 1 c shock at fdis
    show s 1 c shock at fdis
    "From seemingly nowhere, his voice starts to scream out a song, spilling it all out with so much power."
    "It's like the air in front of us exploded. Unable to react, I just stand there in a daze."
    "When I look to the side, I see both Shoichi and Jun gaping at him, both as surprised as I am."
    "Kei-kun continues to sing with so much confidence, as if this sort of thing was natural for him."
    "The song shifts into chorus. His voice goes even higher. I'm surprised he can make those sounds with his voice."
    "He's always so inexpressive when we're talking..."
    stop music2 fadeout 5.0
    show k 2 c gentleb at fdis
    "Before I noticed it, the song has ended. Kei-kun places the microphone back on the table and sits back on the couch, not bothering to look for his score."
    "Out of curiosity, I peer at the screen."
    "\"Your score is: 100! Congratulations, you've achieved a max score!\""
    play music3 "music/BGM/Feelin Good.ogg" fadein 5.0
    mc 1 c shock "\"Are you for real...?\""
    "I don't even know what to say. What is there even to say?"
    s "\"W-wow...\""
    "Shoichi too looks completely flabbergasted. He keeps staring at the score screen, not taking his eyes out of the big, golden \"100\" written on it."
    show j 1 c gentle at fdis
    j "\"K-Keisuke-san, that was amazing!\""
    "We're both caught by surprise when Jun almost screams that line out, making us jump up in our seats."
    "Keisuke doesn't look too surprised. In fact, he's been spacing out in his seat until Jun called him."
    j "\"Why didn't you tell us you were such a great singer? Please, do one more. Encore, encore!\""
    show k 1 c sigh at fdis
    "He looks slightly annoyed by Jun's attitude, resorting to a sigh to show his displeasure."
    "Which, of course, flies by Jun's head."
    j "\"You should totally be a singer!\""
    show k 1 c at fdis
    k "\"I'm not interested in music.\""
    "He says, somewhat harshly."
    show j 1 c pout at fdis
    j "\"But that's such a waste...\""
    show k 1 c avoid at fdis
    k "\"The only thing I want to do is play tennis. Everything else is nothing but a distraction.\""
    "Even though he said so with such conviction, his eyes were looking away."
    j "\"But-\""
    show s 1 c laugh at fdis
    s "\"Alright, I guess it's my turn now, right?\""
    "Jun seemed like he wanted to say more but Shoichi was quick to interject."
    "Probably for the best, too, otherwise the mood might have turned irredeemably sour."
    show s 1 c smile at fdis
    show k 1 c at fdis
    s "\"Let's see... what should I pick, then? Hmm...\""
    scene Karaoke
    show j 1 c pout at fdis, two
    show k 1 c smile at fdis, five
    show s 1 c laugh at fdis, eight
    with fade
    j "\"Ahh, I only got a 79 this time. Booo!\""
    "Jun was pouting and throwing a fit as he got another score below the 80s."
    "Shoichi was too busy laughing at him to care. He nearly knocked down the controller as he thrashed around in his laughing fit."
    show k 1 c sigh at fdis
    k "\"Sheesh, settle down, will you?\""
    "Kei-kun stared at them with an amazed expression. I myself am surprised at how lively these two can be."
    "They really get along surprisingly well."
    show s 1 c smile at fdis
    j "\"But... but I didn't manage get a score over 80 a single time. And everyone else got a bunch.\""
    mc 1 c smile "\"Come on, you shouldn't rely on a machine to give your singing a score. It's not going to be accurate.\""
    j "\"Really? Because Keisuke-san got three perfect scores in a row.\""
    show k 1 c avoid at fdis
    "Kei-kun looks away, seemingly uncomfortable."
    "Well, that much is true. Though it took quite a bit of convincing after he went the first time, we managed to get him to sing a couple more times."
    "Imagine our surprise when both of them were pitch-perfect and got solid 100 scores."
    "Afterwards, he was too embarrassed by the attention given to him by Jun and refused to sing further."
    k "\"You just need to practice more. You sounded good.\""
    "He deflects, trying to take the attention away from himself."
    "Well, that's cute too."
    j "\"Booo.\""
    "Still, Jun remains sour for a bit of time."
    play sound "music/knock.ogg"
    "The sound of knocking echoes from the door."
    "Clerk" "\"Excuse me, your two hours will be over in three minutes. Would you like an extension?\""
    show j 1 c shock at fdis
    j "\"Has it been that long already?\""
    "Man, time sure flew today."
    k "\"I'm sorry. I can't stay any longer. I need to be back to the estate by 4 PM anyway.\""
    mc 1 c shock "\"You live in an estate?\""
    show k 1 c scorn at fdis
    k "\"Got a problem with that?\""
    "The only problem I have is your attitude."
    mc 1 c fsmile "\"No, not at all. It just surprised me.\""
    show k 1 c avoidb at fdis
    k "\"Well... that's fine.\""
    "Oh, is that a hint of red I see on his cheeks?"
    s "\"I should probably get going as well. There are some matters I need to look into for the Student Council before I head home.\""
    show j 1 c think at fdis
    j "\"Shoichi-san, you always seem to be doing a lot in the council. Is it that fun to work with them?\""
    show s 1 c wince at fdis
    s "\"F-fun?\""
    "The question seems to catch him by surprise. His face scrunches up for a few seconds before he can recompose himself."
    show s 1 c wry at fdis
    s "\"I suppose it is.\""
    mc 1 c "\"What do they have you doing this time?\""
    s "\"Well, they took a few matters out of my hands in the last couple of days. Said I needed some time to myself lately...\""
    show s 1 c smile at fdis
    s "\"But I still have to check with the city hall about a campaign we're doing to protect the woods close to campus.\""
    mc 1 c think "\"Ah, right. I remember that was a big part of your election pitch.\""
    show s 1 c happy at fdis
    s "\"Yeah. That and arranging for more scholarships for areas outside of sports. Jun-kun was actually the first student to be given a scholarship using the program I proposed.\""
    "What? Seriously?"
    show j 1 c watch at fdis
    j "\"Does that mean you're the reason I managed to join this school?\""
    s "\"Nah. You have your own merits to thank for that. All I did was set things in motion.\""
    "That little... I had no idea his project had been accepted already."
    "He's been planning this since he first joined our high school two years ago."
    "I can't believe he didn't tell me something like that."
    show s 1 c smile at fdis
    s "\"Well, there are still a lot of things that need to be discussed. While I managed to get approval for music scholarships, I haven't gotten their approval for things like debate that are more theoretical.\""
    show s 1 c sigh at fdis
    s "\"Really... I think I won't be able to see the fruits of my labor while I'm still studying here...\""
    show k 1 c calm at fdis
    k "\"Don't worry. I'll make sure to keep things going for you.\""
    show s 1 c at fdis
    s "\"You say that as if you getting elected next year was already a done deal.\""
    "Kei-kun merely smiles in response."
    show s 1 c smile at fdis
    s "\"Anyway, we should get going soon. Our three minutes should be close to being over and I'm afraid they might charge us another hour if we go over our allotted time.\""
    show j 1 c shock at fdis
    j "\"Waah, you're right!\""
    "All you have to do is talk about being charged more money to make Jun panic."
    "Ahh... so easy to read."
    stop music3 fadeout 5.0
    scene Station
    show j 1 c happy at fdis, five
    with fade
    play music "music/crowd01.ogg"
    j "\"Bye bye!\""
    "Jun waves at the two of them as their backs become farther and farther away."
    play music3 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    "We still have quite a bit of daylight for ourselves... I wonder what I should do now."
    show j 1 c watch at fdis
    j "\"[povFirstName]-san?\""
    "I snap out of my daze as Jun waves his hands in front of my eyes, startling me."
    show j 1 c wry at fdis
    j "\"Jeez, what are you doing spacing out in the middle of the day?\""
    mc 1 c annoyed "\"You're the last person I want to hear that from!\""
    show j 1 c gentle at fdis
    j "\"Pfft...\""
    "He bursts out laughing uncontrollably. A few passers-by turn to look at us in curiosity. I feel my cheeks starting to burn red hot."
    "I don't like having this kind of attention."
    "I try in vain to make him calm down, but he continues laughing out loud for the longest time."
    "Ah, this is so damn embarrassing."
    show j 1 c happy at fdis
    j "\"Ah... I'm sorry. I just thought it was really ironic for me to be saying that.\""
    mc 1 c sigh2 "\"If you're that aware of it then don't say it!\""
    "He gives me a very wide grin, looking really pleased with something."
    show j 1 c smile at fdis
    j "\"Still, I liked it. I had a lot of fun today, too."
    show j 1 c gentle at fdis
    extend " Thanks for going out with me, [povFirstName]-san!\""
    "Ah, crap. What is this adorable creature? What sort of response should I have to this? Ah, my mind is going blank."
    mc 1 c avoidb "\"I-It was nothing...\""
    "I manage to stammer out that line, completely conscious that my cheeks are red."
    show j 1 c wry at fdis
    "I see Jun look down at the ground, kicking up a little dirt, a mournful smile on his face."
    j "\"To be honest, I was feeling a little overwhelmed with pressure lately. There's so much ground I need to cover before I'm ready to take part in piano competitions again... I felt so weak and helpless.\""
    show j 1 c happy at fdis
    j "\"But you helped me to relax. Thanks to you I feel completely renewed again. I'll make sure to put on a great performance next time, so please come watch me!\""
    "His smile melts my heart."
    mc 1 c happy "\"Yeah. I'll be looking forward to it. Just tell me the date and I'll come.\""
    j "\"Yup. I'll make sure to call Shoichi-san and Keisuke-san to thank them properly for going out with us today. Thanks again, [povFirstName]-san!\""
    stop music3 fadeout 5.0
    "Jun turns away, waving at me one last time and starts walking away in large steps, almost hopping around."
    j "\"See you later!\""
    mc 1 c happy "\"See ya!\""
    show j 1 c at fdis, offscreenright with moveoridis
    "It makes me happy seeing him walk so merrily on his way."
    "I stand and watch as his back gets farther and farther away. Waiting around until he is completely away from my sight."
    "I could have probably gone with him half the way home if I wanted to, but for some reason I decided to stay around."
    "Maybe I could still look around at some shops? There's still a few hours until I have to be home and there's nothing for me to do there..."
    "Hmm..."
    "I make up my mind and start walking in the opposite direction."
    stop music fadeout 2.5
    $ date = None
    jump Day5
