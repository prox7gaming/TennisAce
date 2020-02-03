label Day7:
    window hide
    scene April15 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene Station with fade
    window show
    $ date = "day7"
    play music "music/crowd01.ogg" fadein 5.0
    play sound "music/cicadas1.ogg"
    "Saturday finally comes, and not a moment too soon."
    "I'm left standing by myself in front of the train station."
    "Despite still being in Spring, the hot, humid air is more reminiscent of summer."
    "I stand in a small patch of shade, desperately fanning myself with my own hand to avoid dying of a heatstroke."
    "So far, I haven't been very successful."
    "Shoichi made the last minute decision that we should all go out this weekend to \"spend some quality time with friends\"."
    "Of course, this time, we made sure to check if Saya would be available to go out this weekend."
    "It was tough for her, but she managed to make some adjustments to her schedule to have her afternoon shift covered today."
    "... Which brings me to where I am now."
    "{size=+2}Where the hell is everyone?{/size}\"" with hpunch
    play sound "music/phonebeep.ogg"
    "My phone's clock tells me its already 9:40."
    "They were supposed to be here 10 minutes ago!"
    "I think I'm starting to have a deja vu..."
    j 1 c gentle "\"[povFirstName]-san!\""
    "Yup. Definitely a deja vu."
    play music2 "music/BGM/Hanging Out.ogg" fadein 5.0
    "Jun's voice echoes from amidst the crowd, making me turn my head sideways to search for him."
    show j 1 c gentle at fdis, three
    show k 1 c at fdis, seven
    with moveiridis
    "My eyes finally find him walking towards me. Kei-kun also seems to be walking right behind him."
    show k 1 c eyesc at fdis
    k "\"Shhhh! Don't scream out in the middle of the street, you idiot!\""
    play sound "music/realization.ogg"
    show j 1 c shock at fdis, jumping
    j "\"Ah!\""
    "Realization dawns on him. The tiger then covers his mouth with both of his hands."
    "Many of the passerby's are now staring at the two of them in curiosity."
    show k 1 c wince at fdis
    k "\"Sorry, sorry, sorry!\""
    "Kei-kun starts bowing frantically to every person that happens to sneak a glance."
    show j 1 c blush at fdis, fidget
    "Meanwhile, Jun starts fidgeting around where he stands."
    "From the look on his face, I'd say he just realized how many people are actually around here at the time."
    "Now my arm is the one having a deja vu..."
    mc 1 c sigh "\"Why are you two causing a commotion first thing in the morning?\""
    "It takes me a while to make my way around the people who have somewhat stopped moving to look at the two morons who just caused a scene."
    show k 1 c worried at fdis
    k "\"It's not like this was my idea, he just screamed out all of a sudden!\""
    show j 1 c fluster at fdis, fidget
    j "\"Uuuuu...\""
    "Jun is fidgeting in place, his eyes glued to the floor in embarrassment."
    play sound "music/tap.ogg"
    "I try giving him an encouraging pat on the back."
    mc 1 c wry "\"Don't worry about it so much. Just try not to stand out that much next time.\""
    j "\"Uuuu...\""
    "My words seem to have the opposite effect."
    "Oh well, nothing I can do about that."
    mc 1 c "\"By the way, Kei-kun, have you seen Shoichi yet?\""
    show k 1 c sigh at fdis
    k "\"If I had, don't you think he'd be with us already?\""
    "Good point..."
    "Well, it was worth a shot anyway."
    show j 1 c flusterb at fdis
    j "\"C-can we go someplace less crowded?\""
    "I see Jun shaking as he tries to reach for my arm, which I quickly move away from his grasp."
    mc 1 c sigh2 "\"No, sorry, I love my arm way too much to let you do that again.\""
    show j 1 c flusterb at fdis, fidget
    j "\"Uuuuuu...\""
    "Jeez, I can understand not liking crowds. I myself feel claustrophobic in them, but this... this is too much!"
    show k 1 c sigh at fdis
    k "\"[povFirstName]-san, please get him somewhere more quiet before he has a mental breakdown. I'll wait for Urata here.\""
    mc 1 c think "\"Ah, alright, then. Thanks, Kei-kun. Come on, Jun, let's go to that sweets shop we visited last time.\""
    j "\"Uuuuu...\""
    "Not even capable of forming complete sentences anymore. Got it."
    stop music2 fadeout 2.5
    scene Sweets
    show j 1 c flusterb at fdis, five
    with fade
    play music3 "music/BGM/Let It Happen - Narr.ogg" fadein 5.0
    "As we go inside, the sweet smell of cinnamon pleasantly tickles my nose."
    "Well, I don't remember smelling anything like this last time."
    if povFirstName == "Yuuichi":
        "Familiar Voice" "\"Welcome to... Ah, Yuu-kun!\""
    else:
        "Familiar Voice" "\"Welcome to... Ah, [povFirstName]-kun!\""
    show j 1 c flusterb at fdis, three with move
    show ayako at seven with moveiridis
    "Standing behind the counter is the Class Rep, who flashes us a radiant smile as we come closer."
    mc 1 c shock "\"C-Class Rep? What are you doing here?\""
    ay "\"Ahaha, oh my, that's true, you don't know about it. My family actually owns this store, so I help around part time.\""
    "She finally notices Jun standing next to me, clinging to my shirt and quaking from his fear of crowds."
    ay "\"Oh dear, what happened to poor Jun-kun?\""
    mc 1 c sigh "\"Crowds.\""
    "Despite my incredibly short explanation, she gives me a knowing smile, grabbing a bonbon from behind the counter and walking over to us."
    ay "\"Jun-kun, would you like a sweet? It's on the house.\""
    show j 1 c blush at fdis
    "Her warm smile and the smell of the chocolate snap Jun out of his trance."
    "He looks her up and down and shyly takes the bonbon from her hand."
    j "\"T-Thank you...\""
    "She puts a hand on her cheek, giggling cheerfully."
    ay "\"He's so cute, isn't he?\""
    show j 1 c watch at fdis
    "Jun finally lets go of my shirt, carefully unwrapping the small truffle in his hand and popping it in his mouth."
    mc 1 c "\"So, Rep-\""
    ay "\"Oh, no need to call me that when we're out of the school. Just call me Aya-chan.\""
    mc 1 c fsmile "\"Uuuhhh... Ayako-san, we actually came by last week and we didn't see you.\""
    ay "\"Uhmm... I usually work here after class on weekdays and in the morning on Saturdays. Ah, could it be that you came around on Sunday? I usually have that day off.\""
    mc 1 c "\"Yeah, that was it.\""
    mc 1 c smile "\"Still, your family owns this shop, huh? Wow. Must be pretty good money having a business right in the main street.\""
    ay "\"Oh, yes. And we also have some of the best sweets in town, if I do say so myself. I'm actually training to inherit this shop from my grandfather.\""
    "I try imagining the class rep as a business owner."
    "Somehow, her lax personality doesn't seem to fit the ruthless image of a business owner I have in my mind."
    mc 1 c curious "\"What kinds of sweets do you sell here anyway? Last time we came around, we only saw traditional Japanese sweets.\""
    ay "\"Ah, yes. We mainly sell those, but we also make some western sweets too. Nowadays, you have to market to every crowd you can. And, if I'm being honest, I happen to prefer the western sweets anyway.\""
    ay "\"By the way, Jun-kun, the one you just ate is one of our new confections. It's a sweet milk-cinnamon dough filled with Dulce de Leche and covered in chocolate. We started selling it just last week and have been selling out of it every day.\""
    mc 1 c shock "\"Wow, it sounds like it's become pretty popular. How much does it cost? Let me pay for Jun's-\""
    ay "\"Oh, don't be silly, that's on the house. I'm just glad to be able to help. But if you'd like to buy some sweets for yourself, I actually have a display with some samples you can try.\""
    "I glance at Jun, who's entranced watching a rotating display of minicakes and hasn't even registered our conversation going on around him."
    "I much prefer him like this, so I think I'd rather stay indoors for now."
    mc 1 c smile "\"Sure, why not.\""
    scene Sweets with fade
    "I hear the door opening as I'm walking around the shop, sampling a few sweets."
    s 1 c sigh "\"There you two are. Seriously, at least answer your phone.\""
    show k 1 c at fdis, three
    show s 1 c smile at fdis, seven
    with moveiledis
    "I turn around to see Shoichi and Kei-kun standing at the door."
    ay "\"Oh hello, Sho-kun, Kei-chan.\""
    show k 1 c uncomfortable at fdis
    k "\"K-Kei-chan?!\""
    show s 1 c happy at fdis
    s "\"Ah, Ayako-chan? I didn't know you were working part-time too.\""
    ay "\"Well, sort of. My family owns this store, you see, so I help around when I can. Would you guys like to try some samples too?\""
    "She smiles so warmly that it's hard not to feel at ease in her presence."
    "I completely take back what I said, she has a natural gift as a saleswoman."
    show k 1 c worried at fdis
    show s 1 c think at fdis
    "Shoichi and Kei-kun look at each other for a few seconds, as if pondering what to do, before finally shrugging and walking over to the display."
    show s 1 c smile at fdis
    show k 1 c at fdis
    mc 1 c smile "\"Well, I've already decided what I'm gonna get. Re- I mean, Ayako...-san. Could you give me two of each of the sweets I've tried.\""
    if povFirstName == "Yuuichi":
        ay "\"Oh my, that's a lot. Are you sure about this, Yuu-kun? Beyond me to try and decide what you can or can't do, but I'd imagine all that sugar wouldn't be good for an athlete.\""
    else:
       ay "\"Oh my, that's a lot. Are you sure about this, [povFirstName]-kun? Beyond me to try and decide what you can or can't do, but I'd imagine all that sugar wouldn't be good for an athlete.\""
    mc 1 c happy "\"Ahaha, don't worry about it, I'm not gonna eat all of them by myself. I'm taking some for my brother and my mother too.\""
    ay "\"Ahh, I see. What a good son and brother you are. Alright, would you like me to pack them inside a paper bag or a sweets box? The box costs extra, but it makes for a great gift.\""
    mc 1 c smile "\"Hmmm... How about you pack these four in the bag and the rest in the box? That way I can eat mine without unpacking the box.\""
    ay "\"Ah, yes, good choice. Just a second.\""
    "She comes back in less than a minute with my order neatly packed in a brown paper bag and a box filled with sweets in her other hand."
    ay "\"Here you go. It'll be ¥2.010.\""
    show j 1 c at offscreenleft
    mc 1 c smile "\"Okay, just a sec-\""
    mc 1 c "\"Ah.\""
    show k 1 c at fdis, two
    show s 1 c smile at fdis, eight
    with move
    show j 1 c at fdis, five with dissolve
    "I look back and see Jun still walking up and down the shop, looking at all the sweets in sight."
    "Good thing we're the only ones here, otherwise I can imagine how disturbing this would be for other patrons."
    mc 1 c smile "\"Jun, is there something you want? I'll buy it for you.\""
    show j 1 c shock at fdis
    j "\"Ah? R-Really?\""
    "I nod, and his whole face just lights up."
    show j 1 c gentle at fdis
    show s 1 c sigh at fdis
    s "\"Whaaa- [povFirstName], how come you don't make me the same offer?\""
    show k 1 c eyesc at fdis
    k "\"You have money to buy your own sweets, stop being a mooch.\""
    show s 1 c scorn at fdis
    s "\"Shut up!\""
    show j 1 c think at fdis
    mc 1 c sigh "\"Do you two just go looking for a reason to squabble or does it just come naturally to you?\""
    ay "\"Ahahaha. Well, I'm glad to see you're all just as energetic outside of school as you are inside it.\""
    mc 1 c sigh2 "\"I'm not. You're not the one who has to deal with them all day...\""
    show k 1 c scorn at fdis
    "Shoichi and Keisuke" "\"Shut up!\" / \"Shut it!\""
    ay "\"Oh, my. You two are more compatible than I thought.\""
    show s 1 c avoid at fdis
    show k 1 c avoid at fdis
    "The two both look at each other at the same time, before they both look away with a huff."
    mc 1 c sigh2 "\"Why are you making it worse?\""
    ay "\"Ahaha. I'm sorry, it just gets really dull here sometimes.\""
    show j 1 c wince at fdis
    "Jun sheepishly walks up to the counter."
    show s 1 c at fdis
    show k 1 c at fdis
    j "\"U-uhm...\""
    show j 1 c blush at fdis
    j "\"[povFirstName]-san, c-can I take one of each of these? I want to bring some for my parents too...\""
    "Jun points to five different sweets: two bonbons and three mini strawberry shortcakes."
    mc 1 c "\"Is this really all you're taking? For you {i}and{/i} your parents?\""
    "He nods slowly."
    "From the way that he stares longingly at them, I can already imagine he's embarrassed of asking for more."
    menu:
        "Buy what he asked.":
            $ moresweets = False
            "I can only imagine he'd be even more embarrassed if I suddenly decided to ignore his request and buy him more than that."
            "I'll just stick with what he asked."
            mc 1 c "\"Well, you heard him, Ayako-san. Can you give me what he asked for inside a box.\""
            "Ayako-san nods, going out to the back for about a minute."
            "As with last time, she returns incredibly quickly, handing me another box of sweets that was neatly packed so as to be as pretty as possible."
            ay "\"That'll be ¥1.730, plus your own box.\""
            "I nod, fishing inside my wallet for two ¥2.000 bills and handing it over to her."
            "She makes change in the blink of an eye, returning the money back to me."
        "Buy more.":
            $ moresweets = True
            mc 1 c smile "\"Ayako-san, can you give me three of each of these inside a box?\""
            show j 1 c shock at fdis, jumping
            j "\"W-wha?!\""
            "For a half-second, she looks stunned. Then, she giggles, looking very pleased."
            ay "\"That's so sweet of you, you're such a good friend. Alright, I'll be right back.\""
            show j 1 c wince at fdis
            j "\"B-But... [povFirstName]-san, that's too much!\""
            mc 1 c smile "\"No it's not. Don't worry about it, I'm not anywhere close to being over my budget anyway and I won't hear no for an answer.\""
            j "\"B-But...\""
            "The class rep soon comes back with a tall box wrapped in some very pretty gift paper and hands it to me."
            "She also leans in close to my ear and whispers something."
            ay "\"I'm gonna give you a 50\% discount on this. Just pretend it's the full price.\""
            "I nod along."
            ay "\"That'll be ¥2.345, plus your own box.\""
            mc 1 c smile "\"Okay.\""
            "I fish inside my wallet for a ¥5.000 bill and hand it to her."
    ay "\"Thank you for your patronage! What about you boys, have you decided on anything?\""
    "As the two make their orders, I hand Jun's sweets to him inside a plastic bag."
    mc 1 c happy "\"Here, enjoy!\""
    if moresweets == True:
        show j 1 c blush at fdis, fidget
        j "\"T-Thank you, [povFirstName]-san...\""
        play sound "music/tap.ogg"
        "Instead of taking the bag that I'm holding from my hand, he suddenly gives me a tight hug."
        "Despite being caught by surprise, I don't pull away, instead giving him a few pats on his back as he buries his face on my chest."
        ay "\"Oh my...\""
        "I look back to see the class rep covering her mouth with her hands, her face red."
        show s 1 c seductive at fdis
        show k 1 c calm at fdis
        "Shoichi and Keisuke are standing next to each other, grinning."
        s "\"Alright you two, maybe don't do that inside a store in front of the main street. People are looking at you through the window.\""
        "I look out and see that, in fact, many people are passing by and staring at us as they do so."
        "I quickly jump away from Jun, nearly knocking him down when I do so."
        mc 1 c avoidb "\"Uh... sorry. Here's your sweets.\""
        show s 1 c wince at fdis
        "He doesn't even look me in the eyes when he takes the bag from my hands."
        "Ayako-san giggles."
        "Damn it, my face feels so hot right now..."
    else:
        show j 1 c happyb at fdis
        "Jun takes the bag, blushing a bit."
        "His smile makes me melt."
        j "\"Thank you, [povFirstName]-san. I really appreciate it.\""
        "As soon as he says that, he turns around and goes stand in a corner."
        "I can see his tail fidgeting around."
        ay "\"My my, he's so cute when he's embarrassed.\""
        show k 1 c sigh at fdis
        k "\"It gets old.\""
        show s 1 c smile at fdis
        s "\"Really? I don't think so.\""
        mc 1 c sigh "\"Do you two {i}have{/i} to disagree on everything?\""
        show s 1 c at fdis
        show k 1 c at fdis
        "They turn around to look at each other, snapping their eyes at me at exactly the same time, like some creepy movie animatronic."
        "Shoichi and Keisuke" "\"Yeah!\" / \"Yes.\""
        mc 1 c fsmile "\"Oookay... I'm gonna go stand in a corner as far away from the creepy twins as I can.\""
    scene Street1 with fade
    stop music3 fadeout 2.5
    play music "music/crowd01.ogg" fadein 5.0
    "Once we finish shopping around, we exit the store back out to the busy main street."
    show j 1 c fluster at fdis, five
    "We've barely even left it and Jun already starts to freak out."
    j "\"C-Can we go someplace else now? {size=-4}I don't like being out in the street.{/size}\""
    mc 1 c sigh "\"You know, you're gonna have to get used to this sooner or later. The school trip is less than a month away and we've never gone anywhere that wasn't at least twice the size of Saitama.\""
    "At the mention of the school trip, Jun whines pitifully, making me roll my eyes in frustration."
    show j 1 c flustert at fdis, three with move
    show k 1 c worried at fdis, seven with moveiridis
    k "\"Ah, that's true, we have the School Trip in July, huh... I need to talk to my father about it.\""
    mc 1 c "\"Has the school already revealed where your class is going to?\""
    show k 1 c at fdis
    k "\"Yeah, they did yesterday. It's Paris.\""
    show j 1 c fluster at fdis, two
    show k 1 c at fdis, five
    with move
    show s 1 c at fdis, eight with moveiridis
    "Shoichi whistles in admiration."
    show s 1 c at fdis
    s "\"Maybe they'll take the third years somewhere interesting this year too. Last year we went to the Chiba prefecture.\""
    mc 1 c think "\"Didn't we go to Hong Kong when we were first years?\""
    show s 1 c think at fdis
    s "\"Oh yeah... Saya got food poisoning from some questionable dumplings and spent the rest of the trip in bed.\""
    show k 1 c avoid at fdis
    k "\"... Alright, don't eat any foods that haven't been prepared by a reputable restaurant. I'll keep that in mind.\""
    mc 1 c "\"I think it's less to do with the restaurant's reputation and more to do with us. Japanese people have pretty fragile stomachs. It doesn't take much to get us sick.\""
    s "\"Over 80\% of Japan's population is lactose intolerant. You can't really expect much from our stomachs.\""
    show k 1 c sigh at fdis
    k "\"What am I supposed to do, then? Not eat?\""
    mc 1 c smile "\"Stick to the food the hotel staff prepares, I'd say.\""
    show k 1 c wince at fdis
    k "\"What is even the point of visiting a foreign country, then?\""
    mc 1 c sigh "\"The point is actually going around instead of staying stuck to your bed with indigestion.\""
    show k 1 c avoid at fdis
    show s 1 c at fdis
    k "\"... Okay, you win this time.\""
    show j 1 c flustert at fdis, fidget
    j "\"U-Uhm...\""
    play sound "music/tap.ogg"
    "I feel someone grabbing onto my arm."
    "When I look back, I see Jun at the edge of a breakdown, clinging desperately to me."
    mc 1 c sigh2 "\"Oh no, not this again...\""
    "He starts squeezing my arm again."
    "I can already feel the blood flow being cut off..."
    mc 1 c shock "\"Okay, let's move it people. I don't want to lose my arm!\""
    play sound "music/phonebeep.ogg"
    "Shoichi pulls out his phone."
    show s 1 c think at fdis
    s "\"It's still a bit early... Saya asked us to come to the diner for lunch so she could join us after her shift ends, but it's still way too early for lunch. Where should we go?\""
    show k 1 c smile at fdis
    k "\"There's a library nearby. How about we go there?\""
    show s 1 c sigh at fdis
    s "\"Really? A library? On our day off? We should go someplace where we can relax. How about we go to a tea parlor? There's a good one a couple of streets away.\""
    show k 1 c wince at fdis
    k "\"Eww, no, I don't even like tea.\""
    s "\"You don't have to drink the tea. You can just have some snacks.\""
    show k 1 c avoid at fdis
    k "\"Lunch is in less than two hours. We shouldn't be stuffing ourselves with food.\""
    show s 1 c smile at fdis
    s "\"We can show up a bit later. They serve lunch until 2PM anyway. There'd be no point going in too early because we'd have to wait around anyway.\""
    show j 1 c flustert at fdis, fidget
    j "\"A-a-anywhere's fine...\""
    "He squeezes harder. Crap, my arm's tingling..."
    mc 1 c cshock "\"Ow ow ow ow ow, just pick someplace already, I don't care where!\""
    show k 1 c sigh at fdis
    k "\"Why don't we have [povFirstName]-san choose, then? It'd be easier than arguing about it.\""
    show s 1 c happy at fdis
    s "\"That sounds like a good idea. What do you think?\""
    menu:
        "I choose..."
        "The Library.":
            mc 1 c wince "\"No offense, but I'm not a huge fan of tea either. I'd rather go to the library.\""
            show s 1 c sigh at fdis
            s "\"Awww... but it's our day off!\""
            mc 1 c sigh "\"They have fiction too, you know.\""
            s "\"Yeah, but... it's our day off!\""
            mc 1 c sigh2 "\"I thought you liked books.\""
            show s 1 c wince at fdis
            s "\"Iwashopingtodosomethingmoreexcitingwithmyfriendsokay!\""
            show k 1 c sigh at fdis
            k "\"Man, seriously, pause when you talk. I can barely understand what you're saying.\""
            "Shoichi groans. Since I know where the library is, I just turn around and start walking that way."
            show s 1 c avoid at fdis
            show k 1 c smile at fdis
            "When I look behind my back to see if Shoichi is following, I see that Kei-kun has grabbed his arm and is dragging him along by his hand."
            stop music fadeout 2.5
            jump library
        "The Tea Shop.":
            mc 1 c wince "\"Look, I'm not a huge fan of tea either, but the idea of going to a library on my day off is just... no!\""
            show k 1 c wince at fdis
            k "\"Oh, come on, they have fantasy there too!\""
            mc 1 c avoid "\"Yeah, but we're going out as friends. What would be the point of doing that if we're just going to go into a corner and read by ourselves?\""
            k "\"Aww...\""
            show s 1 c happy at fdis, fidget
            s "\"Yes! I knew you'd understand.\""
            mc 1 c sigh2 "\"Yeah yeah, great. Can we please go already, I can barely feel my arm anymore.\""
            show s 1 c laugh at fdis
            s "\"Oh, sure. Good guys, follow my lead! {size=-2}That means you stay put, Urushihara.{/size}\""
            show k 1 c sigh at fdis
            k "\"Har har, very funny. Just lead the way already.\""
            stop music fadeout 2.5
            jump teashop
label library:
    scene Library with fade
    play music2 "music/BGM/In That Mood - Narr.ogg" fadein 5.0
    "After a brief walk to a nearby library (I say brief, but ten minutes of Jun grabbing desperately at my arm, among a crowd, underneath a sweltering heat made me feel like I was in my personal hell), we finally find it."
    "While it's not a huge building by any means, it's also not something to scoff at."
    "Walking through the doors, I feel a puff of cold air coming from the air conditioned interior, which, I have to say, feels damn good against my fur."
    show j 1 c sigh at fdis, five with moveiridis
    j "\"Ahhh.\""
    "Even Jun instinctively lets go of my arm, as the cold air seems to help him relax a bit."
    "Actually, looking to the side, everyone's expression seems to have softened up immediately upon entry."
    "I guess I wasn't the only one suffering under that heat."
    show j 1 c at fdis, two with move
    show k 1 c calm at fdis, five
    show s 1 c smile at fdis, eight
    with moveiridis
    s "\"This... this feels pretty good, actually.\""
    show k 1 c haughty at fdis
    k "\"See, I told you the library was a good idea.\""
    show s 1 c sigh at fdis
    s "\"Oh, sure. That's why you wanted to come to the library... because of their air conditioning.\""
    show k 1 c sigh at fdis
    k "\"Hey, that's a hell of a lot better than wanting to get {i}tea{/i}! As if it weren't hot enough already, you wanted us to get hot drinks?\""
    show s 1 c wince at fdis
    s "\"Cold tea is a thing that exists, you know!\""
    show k 1 c at fdis
    k "\"And by any chance were you going to get it?\""
    show s 1 c avoid at fdis
    s "\"... No.\""
    show k 1 c calm at fdis
    k "\"See?!\""
    "As I prepare myself to slap some sense in the two of them (seriously, who argues inside a library?), my work is suddenly turned moot by the arrival of a librarian."
    "A portly, graying otter wearing some kind of neat black vest and a collered white shirt."
    "Librarian" "\"Would you two keep it down? This is a library!\""
    show s 1 c wince at fdis
    show k 1 c worried at fdis
    show j 1 c watch at fdis, offscreenleft with moveoledis
    show k 1 c worried at fdis, three
    show s 1 c wince at fdis, seven
    with move
    play sound "music/stab.ogg"
    "Shoichi and Keisuke" "\"Sorry...\""
    "After chewing them out for a couple of minutes, the grumpy librarian gets back to his post, leaving the two embarrassed idiots standing around looking at their feet."
    mc 1 c sigh "\"Are you guys trying to set up a new record or something? Nearly getting kicked out half a second after walking in?\""
    show s 1 c annoyed at fdis
    show k 1 c annoyed at fdis
    "Shoichi and Keisuke" "\"Shut up!\" / \"Shut it!\""
    "The two get so defensive that they forget to control their voices, prompting the otter librarian to peek his head out from behind a stack of books, glaring daggers at the two."
    show s 1 c wince at fdis
    show k 1 c avoidb at fdis
    "Shoichi and Keisuke" "\"Sorry...\""
    "I try my best to stifle my laughter, managing to keep it down to a strangled chuckle. Shoichi gives me the evil eye, obviously angry."
    show s 1 c displeased at fdis
    show k 1 c sigh at fdis
    s "\"You were trying to get us in trouble, weren't you?\""
    mc 1 c happy "\"Look, Shoichi, I won't lie to you...{w} I won't answer you either. Hey, comic books!\""
    show s 1 c displeased at fdis, offscreenright
    show k 1 c sigh at fdis, offscreenright
    with moveoridis
    "And just like that, I sprint away from the two, leaving an angry looking Shoichi behind."
    "It's only after I look back as I flee that I realize Jun wasn't with us anymore."
    "Hmm... did he go somewhere and we didn't notice?\""
    "Admittedly, I was having way too much fun watching Kei-kun and Shoichi getting yelled at that I didn't pay attention."
    "Oh, the irony of a librarian yelling at people for making too much noise is just hysterical!"
    "Ah, wait, is that..."
    show j 1 c at fdis, five with moveiledis
    play sound "music/pageflip.ogg"
    "Yup, right in front of the comic books section, flipping through a couple of pages of a random book, is Jun."
    "I try waving to him as I approach, but it's abundantly clear that he's lost complete sight of his surroundings."
    "I stop right next to him."
    "So close, in fact, that I can actually feel the heat coming off his body."
    "And yet, he doesn't even blink at my presence. How spaced out do you have to be to do that?"
    play sound "music/tap.ogg"
    "I place a hand on his shoulder."
    mc 1 c "\"He-\""
    show j 1 c cshock at fdis, jumping, shake1
    j "\"Aggh!\""
    "Jun immediately jumps away, letting out a blood curdling scream that I'm sure even astronauts could hear."
    "His fur is completely bristled up and his tail is lashing like mad. His eyes are mere slits as he stares at me with a frightened look."
    mc 1 c shock "\"Jesus Christ, are you trying to jump start my heart?!\""
    show j 1 c blush at fdis
    j "\"S-Sorr-\""
    mc 1 c wince "\"No time for that, let's hide before the angry librarian comes to strangle the living daylight out of you!\""
    show j 1 c shock at fdis
    j "\"Wha- Is that even a thing?!\""
    play sound "music/tap.ogg"
    "I grab Jun's wrist and drag him to a nearby nook, pressing him against the wall."
    "It's a bit cramped in here and I can feel my whole body pressing against his torso, but I try to ignore it."
    show j 1 c blush at fdis
    j "\"U-Uhm-\""
    mc 1 c "\"Shhh! {size=-2}Be quiet.{/size}\""
    "Jun swallows and nods, looking away."
    show cg14_pan with Dissolve(1.0):
        subpixel True
        xalign 0.0
        linear 0.7
        linear 9.0 xalign 1.0
    "Just in time too."
    "From the corner of my eye, I can see the otter walking up to the section we were just in."
    "Good thing I can see him from between the spaces in the bookshelves."
    "The spot we're in is fairly dark, but I don't want to count on that to stay hidden, so as soon as he looks our way, I press even tighter against the wall."
    "Which, of course, also means pressing even tighter against Jun."
    j 1 c zero"\"{size=-2}Wha- [povFirstName]-san?!{/size}\""
    mc 1 c zero "\"{size=-2}Shh, he's looking our way.{/size}\""
    show cg14
    hide cg14_pan
    with Dissolve(1.0)
    "The otter looks around for a second, frowning and scanning the place in search of the voice he heard."
    "Luckily there was no one else in that section as I would feel bad if someone took the blame for us."
    "It's very clear the older man is deeply unhappy but he still abandons his search somewhat quickly."
    "I suppose he's probably too busy to keep this up for all that long?"
    "Whatever reason he might have, I won't complain since it gets us off the hook all that much faster."
    "As I sigh in relief and look down, I finally notice Jun's eyes are glued to my face, his cheeks red through his orange fur."
    j "\"{size=-2}I-Is he gone?{/size}\""
    mc 1 c zero "\"Ah, y-yeah.\""
    hide cg14
    show j 1 c blush2 at six
    with dissolve
    "Damn it, why am I getting embarrassed all of a sudden?"
    "I push myself away from him, breaking up the contact between our bodies."
    "At the last second, I catch myself thinking of how soft he is, but I quickly banish that thought from my head."
    "I try to think of something to say, but my brain has suddenly gone completely blank."
    "I also can't help thinking that his embarrassed expression is too cute."
    "Gaah- What am I thinking? That's just ridiculous."
    "No, no. I'm just thinking that because Jun is our group's mascot. Surely that has to be it. Mascots need to be cute after all!"
    s 1 c sigh "\"Ahem!\""
    show j 1 c cshock at fdis, jumping
    "The sudden noise so close by makes us both jump, although I instinctively cover Jun's mouth."
    "Good thing too, because that means my hands manage to muffle his scream."
    show s 1 c sigh at fdis, one behind j
    show k 1 c serious at fdis, nine behind j
    with dissolve
    s "\"What the hell are you two doing? And in public of all places?\""
    "I was so focused on watching the librarian that I didn't even notice these two walking up to us."
    mc 1 c shock "\"W-Wha. No, it's not what you think!\""
    show k 1 c sigh at fdis
    k "\"I'm not exactly sure what I think this is. All I know is that it doesn't look appropriate for minors.\""
    mc 1 c annoyed "\"Wha- no, that's not what happened!\""
    show k 1 c avoid at fdis
    k "\"Senpai, I don't really care if you swing that way, but this sort of thing is just inappropriate in a public place.\""
    play sound "music/stab.ogg"
    mc 1 c cshock "\"Wha-\"" with vpunch
    s "\"I'm just surprised that I've known you for all these years and never knew that's what you liked.\""
    play sound "music/stab.ogg"
    mc 1 c cshockb "\"W-Wait-\"" with vpunch
    show j 1 c think at fdis
    "Juns tugs at my shirt, trying to get my attention."
    j "\"What are you guys talking about?\""
    "My brain is almost completely fried by the sudden burst of data."
    "ERROR, ERROR. OVERHEAT!"
    scene Library
    show s 1 c at fdis, one
    show k 1 c at fdis, eight
    show j 1 c watch at fdis, five
    with fade
    s "\"Ah, I see. So that's what happened.\""
    "It takes quite a bit of time to both explain the situation and to get them to believe what I'm saying."
    "Luckily for me, with Jun here to corroborate everything, it's a little easier to convince them."
    show k 1 c eyesc at fdis
    k "\"I'm just happy to know that I don't associate myself with a degenerate.\""
    play sound "music/stab.ogg"
    "Guh..." with vpunch
    show j 1 c think at fdis
    show k 1 c at fdis
    j "\"I don't get it, though. Why did we have to hide? I mean, a lecture isn't really that bad.\""
    show k 1 c avoid at fdis
    k "\"A lecture isn't really the problem.\""
    show j 1 c watch at fdis
    j "\"What do you mean?\""
    "Kei-kun points to a sign on a far off wall, with Jun's gaze following the direction he was pointing at."
    j "\"Let's see..."
    show j 1 c shock at fdis
    extend " Eh?\""
    "..."
    play sound "music/tap.ogg"
    show j 1 c cshock at fdis, jumping, shake1
    show k 1 c sigh at fdis
    show s 1 c wince at fdis, five, with move
    j "\"Ehhhh?!\"" with vpunch
    show j 1 c wince at fdis
    "Shoichi grabs the tiger from behind, covering his mouth to keep him from crying out in shock."
    "On the sign, among many things, it says: \"Any and all noises louder than regular chatter will be subject to a fine, starting at ¥6000.\""
    show s 1 c think at fdis, one with move
    s "\"I guess your idea of covering his mouth was better than I gave you credit for, [povFirstName], even if I resent having to use this kind of method.\""
    mc 1 c "\"Well, no one wants to lose money, and I figured Jun would have a harder time dealing with that than most.\""
    show j 1 c wince at fdis, fidget
    j "\"S-six thousand yen...\""
    play sound "music/disappointment.ogg"
    "Waaah, his eyes look so lifeless..."
    play sound "music/tap.ogg"
    show k 1 c at fdis
    show s 1 c smile at fdis
    mc 1 c "\"Hey, Jun.\""
    show j 1 c watch at fdis
    j "\"Ah.\""
    "Well, at least he seems to have snapped back to reality."
    mc 1 c curious "\"Why did you scream out like that when I called to you?\""
    show j 1 c wince at fdis
    j "\"A-ah... that's because...\""
    mc 1 c curious "\"?\""
    j "\"I-I was reading a horror comic.\""
    "Ah..."
    mc 1 c sigh "\"Don't tell me that... you were so scared of the comic that you freaked out when I touched you.\""
    show j 1 c avoid at fdis
    j "\"W-well...\""
    "Bingo!"
    mc 1 c smile "\"Alright, take me to this comic you were reading!\""
    show j 1 c shock at fdis
    j "\"Wha- Why?\""
    mc 1 c happy "\"I wanna see what's so scary about it.\""
    show j 1 c wince at fdis
    j "\"B-But-\""
    s "\"I'm actually a little curious about it too, now that you mention it.\""
    show k 1 c calm at fdis
    k "\"Same here. I wanna see what the fuss is all about.\""
    show k 1 c smile at fdis
    show s 1 c smile at fdis
    show j 1 c sigh at fdis
    j "\"Alright, fine. I'll show it to you guys...\""
    show j 1 c at fdis
    "Reluctantly, Jun takes us to the spot where he found the dreaded comic book."
    show j 1 c wince at fdis
    "... Except he keeps looking at the shelves instead of actually getting it."
    mc 1 c sigh "\"Come on, just point at which one it is and we'll check it out by ourselves.\""
    j "\"O-Okay...\""
    "Jun points to a small, thick comic book that has a black cover with the drawing of a blood splatter on the cover."
    "Charming."
    show s 1 c at fdis
    s "\"The name's... \"Augur\"? Let's see...\""
    play sound "music/pageflip.ogg"
    "He flips the book around."
    s "\"A series of grizzly murders occurs in the small village of Oguro after the arrival of a woman who claims to be a seer. Warning, contains graphical depictions of..."
    show s 1 c wince at fdis
    extend " murder, dismemberment, bloodletting, nudity, rape, torture and infanticide?\""
    "..."
    show s 1 c sigh at fdis
    s "\"Jeez, what's something like this doing in the comic book section of a public library?!\""
    show k 1 c at fdis
    k "\"Let me see this.\""
    "Kei-kun snatches the book away from Shoichi's hand, quickly opening it and looking around."
    show k 1 c smile at fdis
    k "\"Aha!\""
    mc 1 c curious "\"What is it?\""
    show k 1 c calm at fdis
    k "\"This book isn't stamped.\""
    mc 1 c "\"... So?\""
    show k 1 c sigh at fdis
    k "\"All library books have a stamp marking them as library property. I bet some prankster put this here thinking it'd be funny if a little kid read it and became traumatized.\""
    show s 1 c think at fdis
    s "\"Well...\""
    "Shoichi turns to look at Jun, who's hiding behind me, peeking at the book from behind my back."
    show s 1 c considerate at fdis
    show k 1 c at fdis
    s "\"... can't say they didn't succeed...\""
    mc 1 c sigh2 "\"Good point... We should probably take it to the front desk to be disposed of.\""
    show k 2 c think at fdis
    k "\"{i}Or{/i}... we could take it home and keep it.\""
    show s 1 c sigh at fdis
    s "\"Seriously? You're stealing library books now?\""
    show k 1 c at fdis
    k "\"It's not stealing. Whoever left this here certainly didn't expect to see it again. What's the problem if someone who might enjoy it takes it home?\""
    show s 1 c smile at fdis
    s "\"Want me to tell everyone in school that you read comics with graphical depictions of rape and murder?\""
    show k 1 c avoid at fdis
    k "\"... Yeah, let's bring it to the front desk.\""
    "That was easier than I thought it'd be."
    scene Library
    show s 1 c at fdis, two
    show k 1 c at fdis, eight
    show j 1 c watch at fdis, five
    with fade
    play sound "music/scribbling.ogg"
    "We take it to the reception desk, where the same otter that we had been hiding from is scribbling away at a few notebooks."
    "Honestly, how short staffed is this place?"
    mc 1 c fsmile "\"Excuse me...\""
    "Librarian" "\"Yes?\""
    "Once we lock eyes, the otter scowls."
    "Librarian" "\"Oh, it's you. You wouldn't happen to be the ones who were screaming inside the library just a couple of minutes ago, would you?\""
    mc 1 c fsmile "\"W-we've actually come here to show you this. It was in the comics section and it doesn't have a library stamp. It's also not exactly a... uhh, appropriate book to have in the reach of children.\""
    "I look down at a name tag he has on his desk."
    "It reads Ben... kei?"
    "Why is it written in romanized script?"
    show k 1 c avoid at fdis
    "Keisuke hands him the accursed comic book."
    "And yes, Keisuke, we can all tell that you wanted to keep it. No need to make that face."
    play sound "music/pageflip.ogg"
    "The otter reads the back of the book and begins to flip the pages."
    play sound "music/pageflip.ogg"
    "His face gets progressively whiter as he continues reading to give it a cursory read."
    play sound "music/pageflip.ogg"
    "Then, just when I thought it couldn't get any whiter, his face begins to turn red, seething with rage."
    "Benkei" "\"You found this? In the library?\""
    mc 1 c "\"Yes, in the comic book section.\""
    "His face goes slack. With just those few words, it's as if I suddenly made his entire world collapse."
    "He leans back on his chair, taking off his specs and rubbing the bridge of his nose with a long, exasperated sigh."
    "When I think he's about to punch something, his face suddenly relaxes. He takes off his specs and leans back on his chair, sighing."
    "Benkei" "\"These damn kids think it's so funny to pull \"pranks\" like this...\""
    show k 1 c worried at fdis
    k "\"This has happened before?\""
    "Benkei" "\"Yes, it's the third time this month. This is actually one of the tamer ones too. The first time they hid a western porn book in the children's books section.\""
    show s 1 c wince at fdis
    s "\"Wha- Are you serious?!\""
    show j 1 c think at fdis
    j "\"Western porn? Why not just call it porn? Is there any difference between the two?\""
    show k 1 c at fdis
    k "\"Well, that's because the western stuff h-\""
    show k 1 c shock at fdis
    show s 1 c considerate at fdis
    play sound "music/tap.ogg"
    mc 1 c fsmile "\"You mustn't. He's still too pure!\"" with hpunch
    k "\"Waah.\""
    "The right answer here is to keep silent about it."
    show k 1 c sigh at fdis
    show s 1 c smile at fdis
    show j 1 c watch at fdis
    "Benkei" "\"Well, anyway, thank you for your help. I'm sorry for being... uncouth earlier. Most of my colleagues called in sick today and I'm overworked right now. I shouldn't have taken my anger out on you kids.\""
    show s 1 c wry at fdis
    s "\"Oh, no, it's okay. We deserved it. We were being too loud.\""
    "The otter smiles."
    "Benkei" "\"Oh, by the way, what's that other book in your hands, boy?\""
    "Only after he mentions it do I notice that Kei-kun is holding a second book."
    show s 1 c at fdis
    k "\"Ah, this? I was hoping to check this out.\""
    mc 1 c sigh "\"Why do you even need to check out a book at a library? Your father could probably buy this whole damn place and everything in it!\""
    show k 1 c sigh at fdis
    k "\"Yes, {i}my father{/i} could. I think you forget the fact that the company belongs to him, not me.\""
    show k 1 c at fdis
    k "\"Plus, just because you can doesn't mean you should. I prefer renting books from the library because that helps them stay in business.\""
    "He hands the book in his hands to the otter, who smiles as he receives it."
    "Benkei" "\"That's awfully nice of you, sonny. Let's see here... \"Red Rose Hotel?\", that's some advanced reading you have here. Very good taste, too!\""
    mc 1 c think "\"R-Re-Rent?\""
    show k 1 c calm at fdis
    k "\"\"Red Rose Hotel\". It's English. It's a mystery book from 1944. I've read most of this author's books by now, but this one is his first work and it's very hard to find nowadays.\""
    show k 1 c worried at fdis
    k "\"Wait, I'm surprised you didn't understand that. Don't you usually have good grades in English?\""
    mc 1 c sigh "\"Good grades in a test doesn't exactly mean you'll understand people talking in that language right in front of you...\""
    show k 2 c think at fdis
    k "\"Ah, maybe that's true.\""
    "Benkei" "\"Well, can I see some ID please?\""
    show k 1 c smile at fdis
    k "\"Oh, sure.\""
    play sound "music/typing.ogg"
    "Keisuke hands him his ID card and the man starts inputting data on his computer."
    "As soon as he rereads his name, though, he stops."
    "Benkei" "\"Urushihara... As in the Urushihara Corporation?\""
    show k 1 c avoid at fdis
    k "\"Ah, yes. That's right.\""
    "The otter whistled in admiration."
    "Benkei" "\"Your friend wasn't joking when he said you could buy this whole building. I feel like I'm in the presence of royalty.\""
    show k 1 c uncomfortable at fdis
    k "\"Something like that, yeah.\""
    "Benkei" "\"Okay, boy, how long do you want to have the book for?\""
    show k 1 c at fdis
    k "\"One month, for now. Can I extend the time later if I don't finish it by then?\""
    "Benkei" "\"Sure. All we ask for is a down payment of 50\% if you plan on having it for more than two weeks. That'll be ¥900.\""
    show k 1 c smile at fdis
    k "\"Sure. One second.\""
    "Keisuke fishes out a ¥1000 bill from his wallet and hands it to the Otter, who gives him back the change."
    "Benkei" "\"Thank you. Enjoy your book!\""
    show k 2 c gentle at fdis
    k "\"Yeah, thanks!\""
    show k 1 c smile at fdis
    "Keisuke turns to us, putting the book inside his bag."
    k "\"Okay, we can go now.\""
    show s 1 c sigh at fdis
    s "\"Uhh... we've been here for less than fifteen minutes.\""
    k "\"I know, but I've got what I came here for. I don't care anymore. Plus, weren't you opposed to coming here in the first place? You should be celebrating.\""
    show s 1 c wince at fdis
    s "\"Yeah, but... I like the air conditioning.\""
    show k 1 c calm at fdis
    k "\"You'll live. Come on, I still want to swing by the sports gear store.\""
    s "\"We didn't all get together just to follow His Majesty's script, you know...\""
    show k 1 c eyesc at fdis
    k "\"No, you all got together to go to a stupid cherry bloom at the park. If I'm gonna be forced to go see {i}that{/i}, you can at least accompany me to the two places I want to go.\""
    show s 1 c sigh at fdis
    s "\"... Damn it, fine.\""
    mc 1 c think "\"Well, I guess I might as well buy a new pair of tennis shoes while we're there. My old ones are getting a bit worn.\""
    s "\"We both know you'll just buy the exact same model of shoe again.\""
    mc 1 c smile "\"Of course. My old ones are perfect in every way. Why change?\""
    jump afterwards

label teashop:
    scene TeaShop
    show s 1 c smile at fdis, eight
    show j 1 c watch at fdis, five
    show k 1 c at fdis, two
    with fade
    play music2 "music/BGM/In That Mood - Narr.ogg" fadein 5.0
    "Shoichi leads us to a small, secluded shop that is a little distant from the main street."
    "The place is mostly empty (not that I can imagine a tea shop being packed), but the inside looks as far removed from a Japanese teashop as I can imagine."
    "As soon as we walk in, we are greeted by a small wolf boy who doesn't look to be much older than us."
    "Clerk" "\"Welcome, can I get you anything?\""
    "He flashes us a toothy smile and hands us a small flyer with their entire menu."
    "Wow, it's really compact..."
    show j 1 c shock at fdis
    show k 1 c shock at fdis
    "Clerk" "\"Ah, Urata-kun, it's nice to see you again! Been a while since you last came by.\""
    show s 1 c considerate at fdis
    show j 1 c watch at fdis
    show k 1 c at fdis
    s "\"Ahaha, yeah... I've been getting that a lot recently.\""
    "Clerk" "\"Busy with school work again? You always seem to disappear a couple times a year when things start getting hectic.\""
    show s 1 c wry at fdis
    s "\"Yeah, I guess you can say that. Plus, senior year and all that, the pressure to get into a good college just eats up even more of my free time.\""
    mc 1 c fsmile "\"Uh... Shoichi, introduce us.\""
    show s 1 c think at fdis
    s "\"Oh, right. Everyone, this is Tadanori-senpai. He was one of my seniors on the Volleyball club back when I was a first year. Tadanori-senpai, this is everyone!\""
    show k 1 c sigh at fdis
    k "\"You call that an introduction? I'd have gotten more useful information out of a name tag.\""
    "Tadanori" "\"Well, we don't use name tags here. This is just a small tea shop after all. And you are?\""
    show k 1 c at fdis
    k "\"Keisuke Urushihara. Nice to meet you.\""
    "Tadanori" "\"Ah, from the Urushihara corporation, right? Didn't know Urata-kun was friends with such a big shot.\""
    show k 1 c avoidb at fdis
    k "\"B-big shot? That's not...\""
    mc 1 c smile "\"I'm [povName]. It's a pleasure to meet one of Shoichi's former teammates.\""
    "The wolf's smile widens, flashing us some teeth."
    "Tadanori" "\"Ah, so you're the famous [povFirstName] I heard so much about when I was in the club with Urata-kun here.\""
    mc 1 c wince "\"Uhh...\""
    show s 1 c wince at fdis
    s "\"T-Tadanori-senpai, not now!\""
    "The wolf flashes a devious look as he turns away from Shoichi."
    "Tadanori" "\"Urata-kun here used to talk about you a lot. I think I heard your name more often than any of my teammates that year.\""
    show s 1 c sadb at fdis, jumping
    s "\"T-Tadanori-senpai!\""
    "Tadanori" "\"Ahaha, don't be so uptight, Urata-kun. You should enjoy your youth while you still have it.\""
    "You would be more believable if you weren't laughing right now."
    "Tadanori" "\"Why don't you guys have a seat and call me over when you're ready to order.\""
    show s 1 c wince at fdis
    "Shoichi immediately begins pushing us towards some far away seats."
    "His attempt at getting us away from Tadanori-san is praiseworthy but also incredibly obvious."
    show k 1 c calm at fdis
    k "\"Well... that was something.\""
    "Kei-kun speaks up once we're finally seated."
    mc 1 c smile "\"Say, Shoichi, did you really talk about m-\""
    show s 1 c avoidb at fdis, jumping
    s "\"Shut up!\""
    "Shoichi buries his red face in his arms."
    show k 1 c smile at fdis
    show j 1 c considerate at fdis
    k "\"You keep saying that and it's gonna turn into your catchphrase.\""
    show s 1 c annoyed at fdis
    "Shoichi shoots him a dirty look, but Kei-kun cuts him off before he gets to say anything."
    show k 1 c eyesc at fdis
    k "\"Yeah yeah, \"Shut up\". Got it.\""
    show j 1 c wince at fdis
    j "\"Hmm...\""
    show k 1 c at fdis
    show s 1 c at fdis
    mc 1 c smile "\"Hey, Jun, what are you thinking so hard about?\""
    show j 1 c shock at fdis, jumping
    j "\"Huh? Oh, I was trying to decide what I can order from the menu. At least it's not crazy expensive in here.\""
    mc 1 c happy "\"I can pay for you if you want.\""
    show j 1 c wry at fdis
    j "\"Thanks but no thanks. I don't want to turn into a mooch.\""
    show k 1 c calm at fdis
    k "\"Unlike some people.\""
    show s 1 c scorn at fdis
    s "\"Hey, I'm not a mooch.\""
    show k 1 c smile at fdis
    k "\"Funny you'd said that considering I never mentioned any names. Well, I guess if the shoe fits...\""
    show s 1 c sigh at fdis
    s "\"Don't go around thinking you're oh so slick, I know who you were talking about.\""
    show k 2 c gentle at fdis
    k "\"Hey, if the shoe fits...\""
    show s 1 c scorn at fdis
    s "\"I'll stuff the shoe down your throat...\""
    show j 1 c think at fdis
    j "\"Boy, that escalated quickly.\""
    mc 1 c sigh "\"Sometimes I wonder how you two manage to be friends.\""
    show k 1 c annoyed at fdis
    "Shoichi and Keisuke" "\"Who says we're friends?\""
    mc 1 c smile "\"That does.\""
    show k 1 c avoid at fdis
    show s 1 c avoid at fdis
    show j 1 c considerate
    "They both look at each other in the eye and then look away in disgust."
    j "\"Getting some real \"creepy twins\" vibes from you two...\""
    "Shoichi groans."
    mc 1 c sigh "\"Seriously, though. You two are oddly in sync today.\""
    show s 1 c sigh at fdis
    show k 1 c at fdis
    s "\"Well, we can't disagree about everything all the time.\""
    show j 1 c watch at fdis
    j "\"That's the exact opposite of what you said earlier.\""
    show s 1 c happy at fdis
    show k 1 c smile at fdis
    show j 1 c considerate at fdis
    s "\"Well, life's filled with contradictions.\""
    mc 1 c sigh2 "\"Could you please try making sense?\""
    show s 1 c smile at fdis
    show k 1 c at fdis
    show j 1 c watch at fdis
    s "\"Anyway, what are you guys thinking of ordering? I'm gonna go with-\""
    mc 1 c sigh "\"Let me guess. Green tea.\""
    show s 1 c happy at fdis
    s "\"Bingo!\""
    show k 1 c scorn at fdis
    "Kei-kun examines his flyer with the undivided attention you'd see from someone reading a very good book."
    mc 1 c fsmile "\"Uuhhh... Kei-kun? That's a very... intense look you have on your face right now.\""
    show k 1 c avoid at fdis
    k "\"Oh, I'm sorry. It's just...\""
    mc 1 c curious "\"Just?\""
    show k 1 c scorn at fdis
    k "\"I. Hate. Tea!\""
    "He tosses his menu back on the table, leaning back in his seat with a heavy sigh."
    show k 1 c sigh at fdis
    k "\"I'll just get a coffee. They don't really have anything of note other than a ridiculous amount of types of tea.\""
    show s 1 c considerate at fdis
    s "\"Ah, yeah. This place is kinda lacking in drinks other than tea. They sorta aim towards people who love tea the most. It's one of the biggest selections in the city. I'm sure we could find {i}something{/i} you like if we-\""
    show k 1 c scorn at fdis
    k "\"I'll. Have. A. Coffee.\""
    show s 1 c sigh at fdis
    s "\"Okay. And certainly {i}nothing but coffee{/i}.\""
    show k 1 c annoyed at fdis
    k "\"I don't appreciate the mockery.\""
    show s 1 c happy at fdis
    s "\"Too bad. I do.\""
    "Just when it looks like they're going to start arguing again..."
    show j 1 c bored at fdis
    j "\"Could you two cut it out. {size=-2}There are people staring at us.{/size}\""
    show s 1 c shock at fdis
    show k 1 c shock at fdis
    "The two start looking around and realize that most of the people in the teashop are staring intently at them."
    show j 1 c sigh at fdis
    show k 1 c wince at fdis
    show s 1 c wince at fdis
    s "\"S-Sorry...\""
    mc 1 c sigh "\"Every single time...\""
    j "\"Well, of course people would notice. This place is dead quiet. Any sound becomes easy to notice.\""
    show j 1 c watch at fdis
    mc 1 c curious "\"How did you realize they were staring at us, though? You didn't lift your eyes from your menu.\""
    show j 1 c think at fdis
    j "\"I have good hearing. I heard people whispering about us.\""
    show k 1 c sigh at fdis
    show j 1 c watch at fdis
    k "\"Oh, great. We barely just came here and already we're being talked about.\""
    show j 1 c bored at fdis
    j "\"You should keep your voice down, then, if you don't want that.\""
    show s 1 c wince at fdis, jumping
    s "\"Jeez, I've never seen Jun-kun being this blunt before.\""
    j "\"Well, I don't like having attention drawn to myself, and you guys are getting everyone to look at us, so I'm feeling a bit displeased...\""
    show k 1 c shock at fdis
    show s 1 c shock at fdis
    "They fall into bewildered silence for a few seconds."
    k "\"Is... is it just me or does the fact that he's always goofy just make this now look even more serious?\""
    "We all nod in agreement."
    show j 1 c watch at fdis
    j "\"Hmm... I think I'm gonna go with the Oolong Tea. It's not too expensive and I tend to like it. Hmm... can I maybe afford something to eat too?"
    show j 1 c wince at fdis
    extend " {size=-4}I also have to eat lunch later...{/size}\""
    show s 1 c think at fdis
    show k 2 c think at fdis
    "We all exchange glances between each other, silently sharing our thoughts."
    show s 1 c considerate at fdis
    show k 1 c at fdis
    s "\"Please let us pay for your food!\""
    show j 1 c shock at fdis, jumping
    j "\"What? No, I don't want to take advantage!\""
    show k 1 c sigh at fdis
    k "\"We'll beg if we have to.\""
    show j 1 c wince at fdis
    j "\"But-\""
    mc 1 c sigh "\"No buts. We're paying for it.\""
    "Before he can disagree, I call Tadanori-san over to our table."
    show k 1 c at fdis
    show s 1 c smile at fdis
    show j 1 c shockb at fdis
    "Tadanori" "\"Hey, you guys ready to order?\""
    mc 1 c smile "\"Yeah, can I have an Oolong Tea, a Green Tea, Two Coffees and a Rice Cracker platter for the four of us?\""
    "Tadanori-san writes our order on a small notepad and then taps it with his pen a few times."
    "Tadanori" "\"Okay. I'll be right back with your order.\""
    "He walks back to the kitchen, first stopping by the front door to receive some other people who have just arrived."
    mc 1 c happy "\"There, I ordered. Now we'll have a shared plate of snacks to eat and it'll be a waste for you to not eat them.\""
    show j 1 c wince at fdis, jumping
    j "\"Wha- But...\""
    show k 1 c avoid at fdis
    k "\"... You didn't have to order for me.\""
    mc 1 c smile "\"Ah, don't worry about it. It wasn't any trouble.\""
    show k 1 c sigh at fdis
    k "\"No, seriously, you shouldn't have... I hate rice crackers...\""
    show s 1 c sigh at fdis
    show j 1 c considerate at fdis
    s "\"Is there anything you actually {i}like{/i}?\""
    show k 1 c avoid at fdis
    k "\"In this tea shop? I hardly think so.\""
    s "\"Seriously, rich guy who hates tea. That's like a bear who doesn't like honey.\""
    show k 1 c at fdis
    k "\"Now you're just being speciest, not all bears like honey.\""
    show j 1 c watch at fdis
    s "\"Do you know any that don't?\""
    show k 1 c avoid at fdis
    k "\"... That's beside the point!\""
    j "\"If you ask me, that's entirely the point.\""
    play sound "music/stab.ogg"
    show k 1 c wince at fdis, shake1, jumping
    k "\"Guh...\"" with vpunch
    mc 1 c sigh "\"You know, for a guy who looks so cute and innocent, you do have a way of cutting into conversation at the exact moment you can cause the most damage.\""
    show j 1 c happy at fdis
    "He looks awfully cheeky smiling like that."
    show s 1 c at fdis
    show j 1 c watch at fdis
    show k 1 c at fdis
    s "\"Well, ignoring his Majesty's pickiness-\""
    show k 1 c hostile at fdis
    k "\"Hey!\""
    show s 1 c smile at fdis
    s "\"I was thinking of visiting the park. The Cherry Trees are supposed to be in bloom today.\""
    show j 1 c shockb at fdis
    j "\"Ah!\""
    "Jun's eyes are nearly sparkling with excitement at hearing those words."
    show j 1 c happyb at fdis
    j "\"It's been years since the last time I saw the Cherry Trees!\""
    show k 1 c sigh at fdis
    show j 1 c watch at fdis
    show s 1 c at fdis
    k "\"Well, I guess at least one of us is excited for it. It's the same thing every year.\""
    show s 1 c sigh at fdis
    s "\"Seriously, did you come along {i}just{/i} to complain?\""
    show k 1 c smile at fdis
    k "\"Actually, I was planning on getting new strings for my racket, but that works too.\""
    s "\"Ugh... Remind me again, why do I still invite you to these things?\""
    show k 1 c calm at fdis
    k "\"Because you {i}looooove{/i} me.\""
    play sound "music/slap.ogg"
    show j 1 c gentle at fdis
    "Shoichi facepalms."
    mc 1 c sigh "\"... You two look like an old married couple.\""
    show s 1 c scorn at fdis
    show k 1 c avoid at fdis
    "Shoichi and Keisuke" "\"Shut up!\" \ \"Shut it!\""
    mc 1 c sigh "\"... Oookay.\""
    show s 1 c avoid at fdis
    show j 1 c watch at fdis
    s "\"Ahem..."
    show s 1 c smile at fdis
    extend " Anyway, Saya's supposed to get off her shift at one and then she'll have her own lunch, so I think we'll be leaving the diner at about two or so.\""
    show s 1 c happy at fdis
    s "\"So if we leave the diner at about two o'five, we should get to the park by two thirty, that is assuming the train isn't late, of course.\""
    show k 1 c sigh at fdis
    k "\"Okay, uhh... what exactly are we supposed to do at the park?\""
    show s 1 c smile at fdis
    s "\"Sight-seeing.\""
    show k 1 c angryb at fdis
    k "\"... We see those sights every year!\""
    s "\"I know, but Jun-kun was living in a different town for the past six years and it's been a while since he's visited the Omiya Park. I figured he'd enjoy walking around and visiting the stalls.\""
    show k 1 c sigh at fdis
    k "\"... And are the rest of us supposed to die of boredom in the meantime?\""
    show s 1 c at fdis
    s "\"We'll be walking around the park in a group of five people. If you manage to get bored doing that then you certainly deserve a prize.\""
    "Keisuke places his head down on the desk and groans loudly."
    show j 1 c bored at fdis
    j "\"Again, people whispering.\""
    show k 1 c avoid at fdis
    show s 1 c wince at fdis
    k "\"Sorry."
    show k 1 c at fdis
    show s 1 c at fdis
    extend " Look, it's all well and good that you've planned out this whole outing for Kobayashi's sake, but aren't we all supposed to be enjoying ourselves here?\""
    show k 1 c sigh at fdis
    k "\"Going out in this ridiculous heat to a park that's far as hell from my house just to see some cherry trees I see every single day is pushing it. They're not even all that they're cooked up to be, it's not really all that fun.\""
    show j 1 c think at fdis
    j "\"What's wrong with the cherry tr-\""
    show j 1 c wince at fdis, jumping
    show s 1 c shock at fdis
    mc 1 c shock "\"No, don't!\""
    show k 1 c annoyed at fdis
    k "\"I'll tell you what's wrong with them.\""
    show s 1 c sigh at fdis
    mc 1 c sigh "\"Aww...\""
    "Shoichi and I both groan loudly."
    show k 1 c at fdis
    k "\"Back when I first moved into my current house, my father decided the best way to make me feel comfortable was to have a bunch of Cherry Blossoms planted just outside the garden at our house.\""
    show j 1 c think at fdis
    j "\"Wait, you actually had cherry blossoms planted at your house?!\""
    show k 1 c avoid at fdis
    k "\"Yes, now please, let me finish! Anyway, eventually, when the trees grew big enough to blossom, he decided to invite a bunch of his friends to come \"appreciate\" the sight. Those friends of his, of course, had to bring their horrible, spoiled kids with them.\""
    show k 1 c sigh at fdis
    k "\"So, while the adults were outside taking a tour through our cherry blossom garden, I was forced to stay inside with this big, mean bulldog kid who kept tormenting me for the whole day. And when they were finally gone, my dad told me they'd be repeating this \"tour\" for the rest of the week.\""
    show j 1 c watch at fdis
    j "\"... So?\""
    show k 1 c worried at fdis
    k "\"What do you mean \"so?\". Cherry Blossoms are the reason I was bullied for a whole week as a kid!\""
    show j 1 c wince at fdis, jumping, shake1
    j "\"Wha- That's your big reason?\""
    mc 1 c sigh "\"Yep, it is...\""
    show j 1 c bored at fdis
    j "\"Well, it's ridiculous!\""
    s "\"Also yep.\""
    show k 1 c angryb at fdis
    k "\"Hey, none of you were there!\""
    show j 1 c annoyed at fdis
    j "\"I don't care if I wasn't there. What sort of backwards logic did you use to end up blaming the {i}cherry blossoms{/i}?! What's wrong with you?!\""
    show k 1 c shock at fdis
    k "\"Wha- Now you're just being mean.\""
    show j 1 c pout at fdis
    show s 1 c considerate at fdis
    j "\"Well... you're dead inside!\""
    "Tadanori" "\"Uhh... Should I come back later?\""
    "Oh, damn, we didn't even notice him coming back."
    mc 1 c smile "\"Oh, not at all. Actually, do you have any popcorn, this is hysterical!\""
    show k 1 c annoyed at fdis
    k "\"Sh-\""
    mc 1 c think "\"Yeah yeah, \"shut it\", got it. Just get back to fighting.\""
    show j 1 c shockb at fdis
    j "\"Wha- I wasn't- But I-\""
    "Only then did Jun finally realize that his little outburst had landed everyone's eyes directly on him."
    show j 1 c blush at fdis
    show s 1 c smile at fdis
    show k 1 c sigh at fdis
    j "\"{size=-4}... sorry.{/size}\""
    "Tadanori-san sets our bowl of crackers and our beverages on the table and leaves us."
    s "\"Well, that's... {i}a{/i} way of stopping an argument.\""
    mc 1 c smile "\"Who says I was trying to stop it?\""
    "I pick one of the crackers and plop it in my mouth, smiling smugly at Shoichi."
    show k 1 c avoid at fdis
    k "\"Well, at least one of us is having fun...\""
    mc 1 c happy "\"So much fun!\""
    show s 1 c happy at fdis
    show j 1 c watch at fdis
    show k 1 c at fdis
    s "\"Well, since you enjoyed that, why don't we talk about the stupid things {i}you{/i} hate for a second?\""
    mc 1 c happy "\"Go right ahead, I have no such things.\""
    show s 1 c smile at fdis
    s "\"Oh yeah? One word. Milk!\""
    mc 1 c avoid "\"Wha- It tastes weird!\""
    show s 1 c sigh at fdis
    s "\"No it doesn't. It tastes like milk! I'd understand if you were allergic, but you're not.\""
    show k 2 c gentle at fdis
    k "\"You hate milk?!\""
    mc 1 c annoyed "\"Hey, don't laugh at me, Mr. \"I hate cherry trees\".\""
    show k 1 c avoid at fdis
    "Keisuke opens his mouth to say something, but no words come out from it."
    "He ends up leaning back in his seat again and looking away."
    mc 1 c annoyed "\"Okay, this is how you wanna play, huh? Well... Shoichi hates Rock music!\""
    show s 1 c shock at fdis
    show j 1 c shock at fdis
    show k 1 c worried at fdis
    "Shoichi and Jun" "\"Why?!\" \ \"What?!\""
    k "\"Dude, you hate rock music?\""
    show s 1 c wince at fdis
    s "\"It's just noise!\""
    "Tadanori" "\"Guys, guys!\""
    "Tadanori-san shows up once again, a perplexed look on his face."
    "Tadanori" "\"Would you please keep it down, the other patrons are complaining about you.\""
    play sound "music/stab.ogg"
    show k 1 c wince at fdis
    show s 1 c wince at fdis
    "[povFirstName], Shoichi and Keisuke" "\"Sorry...\""
    "After giving us the warning, he walks away, leaving all of us looking awkwardly to the sides, to the disapproving faces of the other patrons."
    show j 1 c happy at fdis
    j "\"You're right. This is funny!\""
    "We all start glaring at him, causing him to stop laughing and look down awkwardly."
    mc 1 c sigh "\"Look. I'm sure we all got a little bit carried away. How about we just pretend nothing ever happened.\""
    show s 1 c sigh at fdis
    show k 1 c sigh at fdis
    show j 1 c smile at fdis
    "Shoichi, Keisuke and Jun" "\"Okay.\" / \"Agreed.\" / \"Alright.\""
    "We sit around in uncomfortable silence, looking down at the table without touching our food."
    show k 1 c avoid at fdis
    k "\"... I once caught Urata dancing in the Student Council room when he thought no one was around!\""
    show s 1 c shock at fdis, shake1, jumping
    show j 1 c shockb at fdis
    show k 1 c calm at fdis
    s "\"Noooooo!\""
    "We all turn to stare at Shoichi."
    show s 1 c annoyedb at fdis
    show k 1 c at fdis
    s "\"You wanna play with fire? I can play with fire. Urushihara on-\""
    mc 1 c wince "\"Please, let's not do this again...\""
    show s 1 c sadb at fdis
    s "\"But he started it!\""
    mc 1 c annoyed "\"I don't care. Behave!\""
    show s 1 c avoidb at fdis
    s "\"Fine!\""
    mc 1 c sigh "\"... Seriously, though? Dancing?\""
    show s 1 c grumblingb at fdis
    s "\"I was bored!\""
    show j 1 c think at fdis
    j "\"What sort of dance was it?\""
    s "\"No kin-\""
    show k 1 c calm at fdis
    k "\"Tango!\""
    show j 1 c shockb at fdis
    show s 1 c shock at fdis
    "Jun and Shoichi" "\"W-Wow!\" / \"Why?!\""
    mc 1 c sigh "\"Alright, you behave too. It's bad enough that I have to chaperone one man-child, I don't need a second one on my back.\""
    show s 1 c annoyedb at fdis
    s "\"Are you calling me a man-child?\""
    mc 1 c think "\"What?! Nooo... {size=-2}not explicitly{/size}.\""
    show s 1 c annoyed at fdis, jumping
    s "\"Wha- You suck!\""
    mc 1 c smile "\"Thank you.\""
    s "\"That wasn't a compliment!\""
    mc 1 c happy "\"Too bad, I took it as one.\""
    s "\"Just shut up and eat!\""
    mc 1 c smile "\"Alright.\""
    "I grab a handful of rice crackers and cram them all into my mouth."
    mc 1 c think "\"Raik thif?\""
    "I sound like I'm speaking complete gibberish because of all the food in my mouth."
    show j 1 c gentle at fdis
    show k 1 c uncomfortable at fdis
    show s 1 c sigh at fdis
    s "\"... And I'm the man-child?\""
    scene TeaShop with fade
    " -30 minutes later."
    show s 1 c sigh at fdis, eight
    show j 1 c smile at fdis, five
    show k 1 c smile at fdis, two
    with dissolve
    j "\"... -no, the Lich boss in the Forbidden Graveyard actually changes elemental affinity every time you hit his weakness, so you have to recast Libra every time you perform a Super Effective hit.\""
    show k 1 c calm at fdis
    k "\"Oh, that explains it! I thought he was just some sort of superboss who became immune to his elemental weakness after you hit it once.\""
    show j 1 c think at fdis
    j "\"Nah, that would just be lazy game design. If they did it like that, you'd have to grind for over five hours just to stand a chance using non-elemental attacks. You should also unequip all elemental equipments and rely only on magic casters to get you through it.\""
    show k 1 c at fdis
    k "\"So what party setup would you recommend for that fight?\""
    show j 1 c smile at fdis
    j "\"Well, the standard would be-\""
    "For the past ten or twenty minutes, Shoichi and I sat in silence, hearing those two have an excited discussion about the latest installment in the Fantasy Universe series."
    "There has been no chance for us to either weigh-in or change the subject whatsoever."
    show k 1 c worried at fdis
    k "\"But wouldn't having three Wizards for that fight make you way too vulnerable to non-elemental magic?\""
    show j 1 c think at fdis
    j "\"As long as you have a Cleric with the Elemental Conversion spell, you should be good.\""
    show k 1 c smile at fdis
    k "\"Ah, in that case, I could also try-\""
    "Shoichi taps me on the shoulder, leaning in and whispering on my ear."
    s "\"{size=-2}Do you understand anything they're saying?{/size}\""
    mc 1 c sigh "\"{size=-2}All I can get from this conversation is that Kei-kun likes RPGs and I, apparently, do not...{/size}\""
    "Even though I actually do like them... this conversation is just so incredibly boring."
    "I have gotten into RPGs before but never like this..."
    s "\"{size=-2}You know, I was actually thinking of trying that game, but... I think I'm over it.{/size}\""
    j "\"I hadn't really thought about it this way. So in the ending, you-\""
    mc 1 c sigh "\"{size=-2}You think they'd notice if we slipped away?{/size}\""
    s "\"{size=-2}I think they wouldn't notice a bomb dropping on top of us.{/size}\""
    mc 1 c sigh2 "\"{size=-2}What do you say we pay for the bill and leave?{/size}\""
    show s 1 c think at fdis
    s "\"{size=-2}You don't think that would be a little rude?{/size}\""
    show j 1 c happy at fdis, jumping
    j "\"Ah, you know what other game I'm looking forward to try? Dungeon Master 3!\""
    show k 2 c gentle at fdis
    k "\"Yeah! I'm a big fan of the series!\""
    show s 1 c sigh at fdis
    s "\"{size=-2}Oh, screw this, I'm out!{/size}\""
    "Shoichi gets up to leave and I decide to follow behind him."
    "We barely manage to take two steps when..."
    show j 1 c smile at fdis
    j "\"What do you think, Shoichi-sa-"
    show j 1 c wince at fdis
    show s 1 c wince at fdis
    extend " Shoichi-san?!\""
    show k 1 c at fdis
    "For the first time since their conversation started, someone decides they want our input on it."
    s "\"{size=-2}Damn it...{/size}\""
    show k 1 c avoid at fdis
    k "\"Uh... where are you two going?\""
    s "\"W-well. We were- I mean, we- How can I-\""
    play sound "music/slap.ogg"
    "When it seems that his brain is frozen trying to look for a response, I slap him atop the head."
    show s 1 c shock at fdis
    s "\"We were going to the bathroom!\""
    "That seemed to work, but..."
    show j 1 c think at fdis
    show k 1 c at fdis
    j "\"Together?\""
    show s 1 c considerate at fdis
    s "\"Yeah!\""
    j "\"Why?\""
    s "\"W-Well... [povFirstName] wanted to show me something!\""
    show j 1 c shockb at fdis
    show k 1 c shock at fdis
    "Keisuke and Jun" "\"What?\""
    mc 1 c sigh "\"... What?\""
    show s 1 c wry at fdis
    s "\"Yeah! [povFirstName] said there was something on his... his butt that he wanted to show me! Right, [povFirstName]?!\""
    mc 1 c angry "\"No, you psycho!\""
    show j 1 c wince at fdis
    show s 1 c wince at fdis
    show k 1 c sigh at fdis
    "Jesus, how can you be {i}that{/i} bad at lying?"
    k "\"You were going to ditch us, weren't you?\""
    show s 1 c considerate at fdis
    "Shoichi and [povFirstName]" "\"No!\" / \"Yes\""
    show s 1 c shock at fdis
    "Shoichi immediately turns to me, bewildered!"
    s "\"Why?!\""
    show s 1 c wince at fdis
    show j 1 c watch at fdis
    mc 1 c scorn "\"Oh please, like they were going to believe us after that stupid excuse you made up. \"Oh, we're going to the bathroom because he's gonna show me something on his butt\". What are you, eight? You suck at lying.\""
    s "\"What? No I don't.\""
    show k 1 c at fdis
    show j 1 c think at fdis
    "Keisuke and Jun" "\"Yes you do.\" / \"You kinda do, yeah.\""
    show s 1 c sad at fdis
    "Shoichi hangs his shoulders, defeated."
    j "\"Why were you ditching us?"
    show j 1 c wince at fdis, jumping
    extend " Oh, were we talking too much? I'm sorry, I didn't notice!\""
    show k 1 c sigh at fdis
    show j 1 c watch at fdis
    k "\"So, basically, you drag us all here with the pretense of \"having a good time\", and when we finally are doing just that, you decide that it's annoying and try to run away? That's kinda crappy of you two.\""
    show s 1 c wince at fdis
    s "\"But I- I just- I didn't- It was [povFirstName]'s idea!\""
    mc 1 c shock "\"Hey!\""
    show s 1 c wry at fdis
    s "\"Sorry... I just had to get the attention off of me.\""
    k "\"Didn't really work. You know what, let's just move on. I want to swing by the sports gear store anyway.\""
    show s 1 c displeased at fdis
    s "\"Wait, who says we're going there?\""
    show k 1 c scorn at fdis
    k "\"You dragged me out to do something I hate and then tried to ditch me in a teashop {i}you{/i} wanted to come to in the first place. Need I say more?\""
    show s 1 c avoid at fdis
    show k 1 c smile at fdis
    s "\"... Let's just go to the damn store.\""
    show j 1 c happy at fdis
    j "\"Oh, yay, I've never been to a sporting goods store before.\""
    mc 1 c think "\"I guess I could use some new tennis shoes anyway.\""
    show s 1 c sigh at fdis
    s "\"Do you even have money in your budget for that?\""
    mc 1 c smile "\"I've been saving up for it, I just wasn't planning on buying it this month.\""
    show j 1 c think at fdis
    show k 1 c at fdis
    j "\"Oh, wait, is there even time for us to go around the shops before we get to the diner?\""
    play sound "music/phonebeep.ogg"
    "Shoichi pulls his phone out of his pocket and presses the button, lighting up the screen."
    show s 1 c think at fdis
    show j 1 c watch at fdis
    s "\"Well, it's still 11AM. I think we can walk around for a bit and still be there by 1PM. Saya should get off work around that time, so she might even be able to join us to eat.\""
    mc 1 c think "\"I wouldn't bet on that happening, but sure, two hours to walk around should be plenty of time.\""
    show s 1 c at fdis
    "We all walk to the counter and pay our bill."
    "Jun tries one more time to convince us to let him pay for his portion, but we just ignore him."
    "Tadanori" "\"Please come again!\""
    "Tadanori-san sees us off with a cheerful grin and a bow, waving as we leave the store."
    jump afterwards

label afterwards:
    stop music2 fadeout 2.5
    scene SportStore
    show s 1 c smile at fdis, eight
    show j 1 c watch at fdis, five
    show k 1 c at fdis, two
    with fade
    play music3 "music/BGM/Hanging Out.ogg" fadein 5.0
    "After a bit of walking around, we eventually find a large store that sells all of the things we need."
    show j 1 c watch at offscreenleft
    show s 1 c smile at offscreenright
    show k 1 c at offscreenright
    with move
    "Once we go in, everyone almost immediately separates."
    "Kei-kun goes towards the tennis gear, Shoichi peruses the volleyball section and Jun just walks around aimlessly."
    "Since I'm not particularly fussy about what to buy, I just find a shoe I like, take it to the front counter and am done in less than three minutes."
    "It's not like I'm buying a newer model either way. I'm just buying the exact same as my last one, because it's a bit spent."
    "Unfortunately, the other three don't seem anywhere close to finishing up their business. Or, in the case of Jun, finish doing absolutely nothing."
    "I don't want to just sit around and wait, either, so I guess I'll just join up with one of them."
    menu:
        "I..."
        "Tag along with Jun":
            show j 1 c watch at fdis, five with dissolve
            "I find Jun perusing the tennis racket section. He keeps looking at all the different models in the display, his eyes filled with boundless curiosity."
            "As soon as he notices me approaching, he gives me a beaming smile."
            j "\"Hey, hey, [povFirstName]-san, what's the difference between all of these rackets?\""
            mc 1 c curious "\"That's sudden. Why the interest?\""
            show j 1 c think at fdis
            j "\"Well, my dad's a big fan of tennis and now I have two friends who are big names in the world of tennis, so I thought I might as well learn a bit more about the sport. I don't really know anything about tennis.\""
            mc 1 c think "\"Well, I'm no expert on the subject. I'm pretty sure Kei-kun could give you a more thorough explanation on that. But, to be fairly simplistic, different rackets can have different weights, shapes, sizes and forms to accommodate different styles of play.\""
            mc 1 c "\"For instance, mine was custom made for me. It has a heavier head-side, a bigger head and a longer neck. It's basically made for a power hitter, to maximize the amount of energy that's transfered to the ball from the swing.\""
            show j 1 c shock at fdis
            j "\"Oooh. And are there rackets for other types of players? Like rackets for people who want more precise shots or rackets for people who want more spin?\""
            mc 1 c smile "\"Yeah. As a matter of fact, Keisuke uses one designed to enhance spin. Although, considering the changes he's been making to his playstyle recently, I wouldn't be surprised if he changed to a control one.\""
            show j 1 c think at fdis
            j "\"I never really thought there'd be so much complexity to a sport like tennis.\""
            mc 1 c happy "\"Every sport has complexity if you try to really learn their details. Of course, not everyone does. Not even I have the patience to learn every little nuance of everything on the sport. I just memorize what's relevant for me and move on.\""
            show j 1 c watch at fdis
            j "\"But what if you end up in a situation where you don't know what's happening?\""
            mc 1 c "\"I mean, just because I have theoretical knowledge of what's going on doesn't mean I'll know how to deal with it. That's why I prefer to just let my body adapt on its own. You know, learn with practice.\""
            show j 1 c think at fdis
            j "\"Hmm... I thought you just liked to slack off.\""
            play sound "music/stab.ogg"
            "Ugh..." with vpunch
            "He can sometimes say the cruelest things without even realizing it."
            show j 1 c wry at fdis
            j "\"Still, tennis rackets, huh...\""
            "Jun stares longingly at the display, looking at all the different models they have for sale."
            mc 1 c smile "\"Why don't you try it?\""
            show j 1 c shock at fdis
            j "\"Huh? Try what?\""
            mc 1 c happy "\"Tennis. I could give you a few lessons to get you started. Who knows, you might like it.\""
            show j 1 c wince at fdis
            j "\"Ah, no no. I couldn't. I can't really play sports.\""
            mc 1 c "\"Why not?\""
            j "\"W-Well...\""
            show j 1 c considerate at fdis
            j "\"Let's just say I have my reasons. Hehe...\""
            "Ugh, I regret asking this one."
            mc 1 c wince "\"Ah... yeah, sure. Hey, look at those cool basketballs!\""
            show j 1 c shock at fdis
            j "\"Huh? Where?!\""
            "Luckily, he's at least easily distracted..."
        "Look for Shoichi":
            "Let's see, Shoichi should be at the volleyball section, and that is... ah, there he is!"
            show s 1 c think at fdis, five with dissolve
            "I find Shoichi holding a volleyball, tossing it between his hands and giving it a few squeezes."
            s "\"... too soft.\""
            mc 1 c smile "\"Hey, what are you up to? Shopping for my birthday gift?\""
            show s 1 c smile at fdis
            s "\"Oh, sure. Your birthday's in three months and yet, here I am, shopping for a gift already.\""
            mc 1 c happy "\"Aww, and you want to make sure to buy it early so you won't run the risk of them running out of stock, how nice!\""
            "He puts the ball back on its pedestal and grabs hold of another one."
            mc 1 c curious "\"For real, though, what are you doing?\""
            show s 1 c at fdis
            s "\"Trying to find a new ball. My old one is a bit worn.\""
            mc 1 c "\"Why don't you pick a random one? Not like you get to play with your own ball during matches.\""
            show s 1 c sigh at fdis
            s "\"Exactly, that's why I'm trying to find something as close to standard-issue as possible. If I get used to a ball that's too light or too heavy, it'll mess with my game. Plus, there's always the matter of durability.\""
            mc 1 c think "\"Hmm... what's even the point if you only practice at school either way?\""
            show s 1 c smile at fdis
            s "\"Well, I need to have a practice partner to train my set-ups. Unfortunately, this store doesn't sell practice partners. It does, however, sell balls, which I can at least use to practice my serve.\""
            mc 1 c wince "\"You know, you should stop refining your serve already. That thing's scary enough as is.\""
            show s 1 c happy at fdis
            "He shrugs."
            s "\"I figure I'm already golden on the accuracy front, but my serve isn't really all that potent yet.\""
            mc 1 c wince "\"You kidding? Your arm's a frigging cannon.\""
            show s 1 c smile at fdis
            s "\"Eh, can't hurt to improve. Me scoring a ton of service aces can't end up hurting our chances in the Inter-High.\""
            mc 1 c sigh "\"Are you sure you're not trying to do everything on your own? Now you're trying to score all the points by yourself.\""
            show s 1 c considerate at fdis
            s "\"Not {i}all{/i} the points. Just as many as I can.\""
            mc 1 c smile "\You say pota{i}to{/i}, I say po{i}ta{/i}to.\""
            show s 1 c happy at fdis
            "He chuckles, giving me a small pat on the back."
            s "\"Don't worry, I promise I'm not biting off more than I can chew. It's just that practicing is fun.\""
            mc 1 c think "\"For you at least. It's always a wonder seeing how many players come out from your court barely able to walk after you handle practice.\""
            show s 1 c think at fdis
            s "\"Oh come on, that's not fair. I'm not {i}that{/i} strict on them!\""
            mc 1 c sigh "\"Didn't you have four first years quitting on the first week this year?\""
            show s 1 c wince at fdis
            s "\"Well...\""
            mc 1 c think "\"Look, I won't say anything, okay. Just try to match up to your teammates' pace before you end up killing someone.\""
            show s 1 c considerate at fdis
            s "\"Will do."
            show s 1 c smile at fdis
            extend " Oh, hey, this ball is pretty close to what I want!\""
            "He never changes, does he..."
        "Talk shop with Kei-kun":
            show k 1 c at fdis, five with dissolve
            "I quickly find Kei-kun next to the gear repair section, perusing many different string kits."
            mc 1 c smile "\"Hey, find what you're looking for?\""
            show k 1 c avoid at fdis
            k "\"Oh, hey, [povFirstName]-san. No, not really. They don't have the brand I usually buy in stock.\""
            mc 1 c curious "\"Which one do you usually get?\""
            show k 1 c at fdis
            k "\"D'Oro. I like the flexibility of it.\""
            mc 1 c wince "\"Oof, I don't think you're gonna find imported products in a store like this.\""
            show k 1 c sigh at fdis
            k "\"Yeah. I was pretty sure I saw it once before, but I asked the clerk and he said they never sold it before."
            show k 1 c worried at fdis
            extend " I didn't realize that my stock was already through and no stores in town sell that particular brand.\""
            mc 1 c "\"Well, you could order it online. Or buy from a different brand.\""
            k "\"... I don't really want to wait. Even if I order express delivery, it's still bound to take three or four business days and I don't want my old strings to interfere with practice. What brand would you recommend?\""
            mc 1 c think "\"Me? Hmm... personally, I usually go with Sakura, but I don't know if you'd like them. They tend to be a bit sturdier.\""
            show k 2 c think at fdis
            k "\"Hmm... Do you think they have any test rackets in the store that I could use to check the stringing?\""
            mc 1 c "\"What, you thinking of hitting a ball indoors to get a feel for the string?\""
            show k 1 c sigh at fdis
            k "\"No, of course not. I'd just do some manual tests to see if it could do as a replacement until I can get my hands on some D'Oro ones.\""
            mc 1 c think "\"Why don't we ask a clerk? Let's see, where can I fi- Ah, there he is, excuse me!\""
            show k 1 c at fdis
            "A bat wearing the store's uniform happened to pass us by and I grabbed his attention."
            "Clerk" "\"Yes, how may I help you?\""
            mc 1 c smile "\"Do you have any display tennis rackets equipped with some Sakura Red strings that my friend could take a look at?\""
            "Clerk" "\"Hmm... we should have one in the back. Let me check for you.\""
            "The clerk walks out to the back of the store to look for the racket Kei-kun wanted to test."
            k "\"Sakura Red?\""
            mc 1 c smile "\"Ah, yeah. That's the same type I use from that brand. They usually sell three different lines: Red, Blue and Black. The Red line is better for players who use a lot of topspin. Since you started changing your style a little bit, I figured that might help you.\""
            show k 2 c think at fdis
            k "\"Ah, I see. That makes sense."
            show k 1 c smile at fdis
            extend " Thanks, [povFirstName]-san!\""
            mc 1 c smile "\"Don't thank me yet. We don't know if they actually have it here for you to check it out.\""
            "Clerk" "\"Excuse me sir. Here.\""
            "The clerk comes back with a racket in hand and gives it to me."
            mc 1 c smile "\"Oh, thanks. Here, Kei-kun, check it out.\""
            show k 1 c at fdis
            "Keisuke starts doing a marathon of tests, such as pushing and pulling the strings, trying to force the gaps in the strings, etc."
            show k 1 c smile at fdis
            "After a good five minutes of vigorous testing, he shakes the racket a bit and gives a satisfied nod."
            k "\"Yeah, this'll work!\""
            mc 1 c happy "\"Great. We'll take a pack of Sakura Reds then.\""
            "Clerk" "\"Very well. Would you like to bring your racket to the store so we can make the switch?\""
            k "\"No thanks, I already have someone to do that for me.\""
            "Clerk" "\"Alright. That'll be ¥8399.\""
            k "\"Got it. Is it okay if I pay with my card?\""
            "Clerk" "\"No problem, sir. Come right this way."
    stop music3 fadeout 2.5
    scene Street1 with fade
    play music "music/crowd01.ogg" fadein 5.0
    " -20 minutes later."
    mc 1 c smile "\"Did everyone get what you were looking for?\""
    show s 1 c happy at fdis, eight
    show j 1 c think at fdis, five
    show k 1 c smile at fdis, two
    with dissolve
    s "\"Yep.\""
    k "\"Yeah.\""
    j "\"I wasn't really looking for anything.\""
    mc 1 c smile "\"Well, good. Then we're all done with the shopping. Just in time too. How about we head to the diner?\""
    show s 1 c smile at fdis
    show j 1 c happy at fdis
    j "\"Oh, good. I was starting to get really hungry.\""
    show s 1 c think at fdis
    s "\"No wonder, it's almost 1PM. Plus, we've been walking around for a while.\""
    show k 1 c at fdis
    k "\"I wonder how full the diner must be right now. It's lunch time on a Saturday. I think it's safe to assume the place will be packed.\""
    show s 1 c smile at fdis
    show j 1 c watch at fdis
    s "\"No problem. I texted Saya a while ago and asked her to save us a seat right around 1PM. But we have to get there soon. Don't want her to get in trouble with her bosses for it.\""
    show k 1 c calm at fdis
    k "\"Heh, you're craftier than I gave you credit for, Urata.\""
    show s 1 c happy at fdis
    s "\"Glad you're finally taking note of my talents.\""
    mc 1 c sigh "\"Oh please. Any five year old with a cellphone could have done that.\""
    show s 1 c smile at fdis
    s "\"Could've, should've, would've... didn't.\""
    show j 1 c wince at fdis
    j "\"Can we please just hurry to the diner? I don't really like being outside in the crowd...\""
    "Oh God, not this again."
    "Jun's tail is lashing rapidly from one side to the other and I can see him slowly walking over towards me."
    "My arm is still recovering from the last death grip."
    mc 1 c sigh "\"Okay people, hurry up, this is a matter of life or death!\""
    stop music fadeout 2.5
    scene Restaurant with fade
    play music2 "music/BGM/On My Way.ogg" fadein 5.0
    "The diner is completely packed, with the waitresses running around to try and serve all costumers in a timely manner."
    "No matter how hard I look, I can't find Saya or an empty seat."
    show s 1 c at fdis, eight
    show j 1 c shock at fdis, five
    show k 1 c at fdis, two
    with dissolve
    j "\"Waaah...\""
    show k 1 c wince at fdis
    k "\"Damn, I knew it'd be full, but I wasn't expecting it to be like this.\""
    sa 1 m "\"Ah, there you are!\""
    show k 1 c at fdis, five
    show j 1 c watch at fdis, seven
    show s 1 c smile at fdis, ten
    with move
    show sa 1 m smile at fdis, one with moveiledis
    "Saya shows up from behind a huge group of people and hurries to us."
    "I've got to give it to her, she moves very gracefully among all these stacks of chairs."
    s "\"Yo, Saya-chan. Any luck saving us a table?\""
    show sa 1 m laugh at fdis
    sa "\"Hehe, of course I got one~"
    show sa 1 m smile at fdis
    extend " It's close to the back, though, it was the only way to keep new costumers from taking it. Come on, follow me.\""
    "Saya guides us through a giant labyrinth of chairs and people. Walking through this mess is a lot harder than she makes it seem. I almost trip on someone's tail or feet or chair quite a few times."
    "It's hard to avoid bumping into others..."
    "We reach a small table for 4 right next to the entrance to the kitchen and are seated."
    "Saya doesn't waste her time pulling out a notepad to take in our order."
    show sa 1 m laugh at fdis
    sa "\"Hello, masters~ Thank you for joining us today, sorry about the wait, teehehe~ Do you guys know what you want to order?\""
    mc 1 c sigh "\"Okay, this was funny the first time but it's gotten old already. Please don't do that...\""
    show k 1 c uncomfortable at fdis
    k "\"Agreed.\""
    show s 1 c sad at fdis
    s "\"Aww, I like it.\""
    show j 1 c wince at fdis
    j "\"It's weird to see Mizoguchi-san talking like that. It just doesn't fit the image I have of her in my mind...\""
    show sa 1 m complain at fdis
    "Saya's entire body relaxes and she takes a deep sigh."
    sa "\"Oh, Christ, thank god. My face is already tired from all this smiling. So, do you guys know what you'll have?\""
    show sa 1 m bored at fdis
    sa "\"Please choose quickly, though, my boss only let me hold a table empty for fifteen minutes because I promised her I'd get you guys in and served as fast as bunnily possible.\""
    show s 1 c smile at fdis
    show sa 1 m at fdis
    s "\"Well, I guess since we don't have much time to be picky, I'll just go with a regular burger and fries.\""
    show k 1 c calm at fdis
    k "\"Same here.\""
    show j 1 c happy at fdis
    j "\"Hmmm~ It's been a while since the last time I ate a good burger! Same for me!\""
    mc 1 c sigh "\"Wow, so much for originality... Give me a burger and fries too.\""
    show sa 1 m happy at fdis
    sa "\"Alright! Thanks for the help guys. I'll come by to ask about drinks when the burgers are close to coming out.\""
    show s 1 c happy at fdis
    show j 1 c smile at fdis
    show k 1 c smile at fdis
    s "\"Sure. Thanks for saving us a table.\""
    show sa 1 m laugh at fdis
    sa "\"You got it! Be right back~\""
    show sa 1 m smile at fdis, offscreenright with moveoridis
    "Saya takes a few seconds to breathe in and turns her Moe act back on, walking into the crowd of awaiting patrons."
    show s 1 c smile at fdis, eight
    show j 1 c watch at fdis, five
    show k 1 c smile at fdis, two
    with move
    s "\"Well, can't say she's not good at her job.\""
    k "\"Yep. I was expecting her to be a comically useless waitress but she's actually very competent. Could do without the act, though.\""
    show j 1 c happyb at fdis
    j "\"Y-You mean you don't like the maids, su~ That's so mean of you, master~\""
    show k 1 c shock at fdis
    k "\"Wha-\""
    "Jun suddenly tries to imitate the same cute act that Saya had been employing."
    "Destructive power is off the charts!"
    s "\"Whew, you're pretty good at this too, Jun-kun. Maybe you've got talent for this job.\""
    mc 1 c smile "\"You should definitely be a maid!\""
    show j 1 c wince at fdis
    show k 1 c at fdis
    j "\"Whaa- But I'm a guy!\""
    mc 1 c happyb "\"Just imagine how cute he'd look in a maid costume.\""
    show j 1 c cshockb at fdis
    show s 1 c considerate at fdis
    show k 1 c sigh at fdis
    j "\"Waaaaaa, pervert! I'm sitting with a huge pervert!\""
    mc 1 c sigh "\"Oh, shut up, I'm just kidding.\""
    show j 1 c wince at fdis
    j "\"Really? You swear?\""
    mc 1 c sigh "\"Yes, I promise that I'm not picturing you in a maid costume.\""
    j "\"... okay.\""
    "I totally am, though. It's too good to ignore!"
    show j 1 c watch at fdis
    show k 1 c at fdis
    show s 1 c smile at fdis
    k "\"By the way, do any of you know when the Moon Festival is going to be held this year?\""
    show s 1 c think at fdis
    s "\"June 15th. Why?\""
    show s 1 c at fdis
    show k 1 c sigh at fdis
    k "\"My father and his usual eccentricity. He decided to buy a booth area for this year's festival and wants me to tend to it.\""
    mc 1 c curious "\"What, why would he do that?\""
    show k 1 c avoid at fdis
    k "\"I told one of the female servants that one of my friends is also a \"maid\" at a cafe and that somehow got reported to my father.\""
    k "\"And, for some reason that's beyond me, he says I too should have an experience with costumer service. \"To keep you humble\", he said.\""
    show s 1 c think at fdis
    s "\"That's... not a bad idea, actually. The reasoning is all over the place, but it's not a bad idea.\""
    mc 1 c "\"It sounds interesting enough. You think he'll actually go through with it?\""
    show k 1 c wince at fdis
    k "\"Who knows. My old man is weirder than Pee Wee German.\""
    show j 1 c think at fdis
    show s 1 c at fdis
    j "\"He can't really be all that bad.\""
    show j 1 c wince at fdis
    show s 1 c considerate at fdis
    show k 1 c worried at fdis
    k "\"He once bought a pair of \"Mustache\" glasses and started wearing them around the house for a month. No reason for it. He just said he wanted to try a new \"style\".\""
    j "\"... okay, so he's a bit peculiar. Nothing bad about that.\""
    show s 1 c at fdis
    show j 1 c watch at fdis
    k "\"If you say so. I just don't like getting involved in his crazy ideas. He makes the weirdest purchases and investments I've ever seen.\""
    show s 1 c think at fdis
    s "\"Don't they always work, though? I've read a few magazine articles about him that said he'd buy stocks and investments no one else would because they were clearly \"failing\", only for the market to turn around and for it to become hugely popular.\""
    show s 1 c at fdis
    show k 1 c sigh at fdis
    k "\"Yeah, that actually happened. My father's business sense is scary, to say the least. I don't even question him on his purchases anymore, because somehow he always seems to be right.\""
    show j 1 c think at fdis
    j "\"Maybe it's insider trading?\""
    show k 1 c avoid at fdis
    show j 1 c watch at fdis
    k "\"I actually thought that too, but it wouldn't really make sense. He's way too random for it to be that.\""
    show s 1 c considerate at fdis
    j "\"Maybe he just acts weird to throw people off his track!\""
    show k 1 c sigh at fdis
    k "\"If that's true then he's a god damned evil mastermind.\""
    show s 1 c at fdis
    show k 1 c at fdis
    s "\"Hey, Urushihara, I just realized something. You've never talked about your mother before.\""
    show k 1 c worried at fdis
    k "\"There's not much to talk about. She was a common woman who used to work on my fathers company and got involved with him. When she got pregnant of me, he sent her away to take care of me by herself.\""
    k "\"His wife divorced him and he didn't find a new one, so he ended up taking me in when I was little to inherit the company.\""
    k "\"Of course, that all means nothing if he has another son. In that case, I'd just be cast out and the new kid would inherit everything.\""
    show j 1 c wince at fdis
    show s 1 c considerate at fdis
    j "\"Oh, wow, that's awful! Your father actually told you he'd do that?!\""
    show k 1 c serious at fdis
    show s 1 c at fdis
    k "\"Not really, but it was implicit. Plus it's not like I care either way. I never wanted to take over his company in the first place.\""
    mc 1 c think "\"Well, you certainly seem nonchalant about it. So I guess that's our thing now? We share stories about our fucked up households?\""
    show k 1 c eyesc at fdis
    show j 1 c watch at fdis
    k "\"Why don't you tell us yours, then? I've never heard you talk about your father. Did he skip out on you?\""
    show s 1 c wince at fdis
    s "\"H-How about we avoid the depressing conversations for now? This isn't exactly dinner table conversation...\""
    show k 1 c at fdis
    k "\"All I know about it is that you basically raised your brother yourself, didn't you?\""
    show s 1 c sigh at fdis
    s "\"You're just ignoring me?\""
    mc 1 c think "\"Yeah, since my dad wasn't around, I took care of Aki whenever mom wasn't home.\""
    show s 1 c wince at fdis
    s "\"H-hey, don't you start ignoring me too...\""
    mc 1 c happy "\"Sorry, Shoichi. I'm fine, though. Honestly, it's not like it was a bad thing either. Aki and I are really close thanks to it.\""
    s "\"You mean to say that you're a super brocon, right?\""
    mc 1 c sigh "\"Eww, don't say that. Just hearing those words coming off your mouth makes me queasy.\""
    show s 1 c smile at fdis
    s "\"Heh, sure.\""
    show j 1 c think at fdis
    j "\"I haven't met your brother yet.\""
    show s 1 c happy at fdis
    s "\"Oh, Aki? You'd like him. Total opposite of {i}this{/i} lazy bum. Nowadays, it's hard to tell which one is the older brother.\""
    mc 1 c sigh "\"Shut up. You can clearly tell I'm the oldest!\""
    show k 1 c avoid at fdis
    k "\"Yeah, sure. I'm pretty sure your brother takes up after your mom. Super responsible and mature. I have a hard time believing he's a twelve-year old.\""
    show s 1 c smile at fdis
    show j 1 c watch at fdis
    s "\"Plus, Aki's hella cute. He's definitely gonna be a heartbreaker when he's older.\""
    mc 1 c avoid "\"God, I hope not. He's too nice for that.\""
    show s 1 c sigh at fdis
    s "\"Says one of the nicest guys I've ever met... who's also broken more hearts than I have won.\""
    mc 1 c wince "\"W-Well...\""
    show j 1 c wince at fdis
    show k 1 c at fdis
    j "\"What do you mean? [povFirstName]-san is a heartbreaker?\""
    show s 1 c at fdis
    s "\"Ah, that's right. I sometimes forget you're new."
    show s 1 c smile at fdis
    extend " [povFirstName]-san doesn't know how to say no to people he's not familiar with. He's got this stupid desire to please strangers. And he's also pretty popular with the girls to boot...\""
    show k 1 c avoid at fdis
    k "\"He basically gets asked out by a girl, can't say no, dates her for a couple of weeks, slowly stops talking to her and answering her until she breaks up with him. Classic modus operandi.\""
    mc 1 c wince "\"T-That's not-\""
    show s 1 c sigh at fdis
    s "\"The frightening part is that he still gets girls confessing to him despite him having a reputation as a player.\""
    mc 1 c sigh "\"A very ill-gained one at that! I am most certainly {i}not{/i} a player!\""
    show k 1 c worried at fdis
    k "\"Not just girls, either. He had a guy confess to him once last year.\""
    show j 1 c shock at fdis
    show k 1 c at fdis
    j "\"Whoa! Did you go out with him too?!\""
    mc 1 c shock "\"What?! No no no, of course not. I turned him down flat-out.\""
    show s 1 c happy at fdis
    s "\"I actually saw the confession. You hesitated.\""
    mc 1 c annoyed "\"Of course I hesitated! Didn't you get the memo? I can't say no to people!\""
    show s 1 c laugh at fdis
    show k 2 c gentle at fdis
    show j 1 c think at fdis
    "I have a strong urge to slap these two for laughing at me like this."
    j "\"Hmm...\""
    mc 1 c "\"What's up, Jun?\""
    show j 1 c wince at fdis
    show s 1 c at fdis
    show k 1 c at fdis
    j "\"Oh, it's just that it sounds a little unfair...\""
    mc 1 c curious "\"What do you mean?\""
    j "\"For the girls who confess to you... Having you say yes to them should mean you feel the same. So if you accept their feelings only to slowly cut off contact until they break up with you... sounds like you're dealing more damage than you would if you just said no.\""
    play sound "music/stab.ogg"
    "Ugh..." with vpunch
    mc 1 c sigh2 "\"I... hadn't thought of it like that...\""
    show s 1 c sigh at fdis
    s "\"That's because you never think things through. I told you multiple times that you should start turning them down, but you don't listen.\""
    show s 1 c happy at fdis
    s "\"Well, at least it gives you something to think about.\""
    mc 1 c wince "\"Y-Yeah...\""
    "Oh God, what have I done..."
    show k 1 c at fdis, five
    show j 1 c watch at fdis, seven
    show s 1 c smile at fdis, ten
    with move
    show sa 1 m smile at fdis, one with moveiledis
    sa "\"Hey guys, I'm ba-"
    show sa 1 m at fdis
    extend " Oh, [povFirstName], what's wrong with your face?\""
    mc 1 c sigh2 "\"... I was born with it.\""
    sa "\"No, not that. You look upset. Did something happen?\""
    mc 1 c wince "\"W-Well, I-\""
    show sa 1 m think at fdis
    sa "\"Oh, no, wait. I don't have time to chat, we're packed up. Sorry, I'll talk to you later, I just came by to ask about drinks. What will you guys have?\""
    mc 1 c annoyed "\"You guys suck!\""
    show sa 1 m considerate at fdis
    sa "\"Again, sorry, but we're really busy right now."
    show sa 1 m smile at fdis
    extend " Anyway, drinks! You guys having them?\""
    scene Restaurant with fade
    mc 1 c smile "\"Well, those burgers were actually pretty good.\""
    "Even though the place was jam-packed, the kitchen still managed to get our food out in record time."
    "I also need to give Saya props for how well she deals with everything. Her service is excellent even when the house is full."
    show s 1 c smile at fdis, eight
    show j 1 c happy at fdis, five
    show k 1 c calm at fdis, two
    with dissolve
    s "\"I told you before, the food here is excellent. That's why I come here so often.\""
    show k 1 c sigh at fdis
    k "\"Sure, that's why.\""
    show j 1 c think at fdis
    j "\"Mizoguchi-san should be out any minute now, right?\""
    show k 1 c at fdis
    show j 1 c watch at fdis
    k "\"She hasn't shown up in the front of the house for a while now, I think she's gone to the back to have her lunch and leave.\""
    mc 1 c "\"Well, either way, we've already finished eating so we shouldn't hold this table if we're not gonna order anything anymore.\""
    show s 1 c happy at fdis
    s "\"That's true. Let's just pay the bill and wait out front.\""
    show s 1 c smile at fdis
    "We vacate our table and make our way to the cashier table to make our payment."
    show k 1 c at fdis, two
    show j 1 c watch at fdis, four
    show s 1 c smile at fdis, six
    with move
    show sa 1 c complain at fdis, eight with moveiridis
    sa "\"-make it up to you, Miki!\""
    "Girl" "\"Don't worry about it so much, Saya-chan. You've covered for me a bunch of times before and I never did anything to thank you for it.\""
    "Saya is already here by the time we arrive."
    show sa 1 c smile at fdis
    "She spots us approaching and smiles at us."
    sa "\"Oh, hey guys. You about done?\""
    mc 1 c smile "\"Yeah. We were coming over to pay the bill.\""
    show sa 1 c laugh at fdis
    sa "\"Oh, sure. Miki, their table totaled ¥5850.\""
    "Girl" "\"All right, thanks, Saya-chan!\""
    show j 1 c shock at fdis
    j "\"Whoa, you got our table memorized?\""
    show sa 1 c smile at fdis
    sa "\"Heh, I have all my tables memorized. I am excellent at my job, after all!\""
    show s 1 c happy at fdis
    show j 1 c watch at fdis
    s "\"Saya has great memory so it's no wonder."
    show s 1 c think at fdis
    extend " Ah, let me handle payment, you guys just pay me back later.\""
    show s 1 c smile at fdis, offscreenright with moveoridis
    show k 1 c at fdis, three
    show j 1 c watch at fdis, five
    with move
    "Shoichi walks up to the cashier and starts chatting with her."
    sa "\"So, what do you guys have planned for today? I canceled a shift for it so it better be good.\""
    mc 1 c "\"Shoichi didn't tell you? We're going to the park to watch the Cherry Blossoms.\""
    show sa 1 c laugh at fdis
    sa "\"Ooh, flower seeing, how romantic~ It'd have been a lot better if we had made a picnic, though.\""
    show k 1 c sigh at fdis
    k "\"Sure. Eat whilst a bunch of flower petals fall on your food and drinks. Talk about romantic...\""
    show sa 1 c pout at fdis
    sa "\"Puh puh! You're such a spoilsport, Kei-chan!\""
    show k 1 c avoid at fdis
    show sa 1 c pout2 at fdis
    k "\"Don't call me Kei-chan!\""
    show k 1 c at fdis
    show sa 1 c happy at fdis
    sa "\"Anyway, I like it. It sounds like it'll be fun!\""
    show k 1 c sigh at fdis
    k "\"No it doesn't.\""
    show sa 1 c bored at fdis
    sa "\"Oh, shut up, you're dead inside anyway!\""
    show k 1 c avoid at fdis
    show j 1 c considerate at fdis
    k "\"Jeez, I'm not even allowed to have an opinion anymore...\""
    show k 1 c at fdis, two
    show j 1 c at fdis, four
    show sa 1 c at fdis, six
    with move
    show s 1 c smile at fdis, eight with moveiridis
    s "\"Okay, all done. You guys ready to go?\""
    sa "\"Yeah. Lead the way!\""
    scene Street1 with fade
    stop music2 fadeout 2.5
    play music3 "music/BGM/Hanging Out.ogg" fadein 5.0
    play music "music/breeze.ogg" fadein 5.0
    "Outside the diner, a comfortable breeze blows."
    "I close my eyes and enjoy the comfortable wind ruffling my fur."
    "This really is a godsend in this particularly hot day."
    show j 1 c happy at fdis, five with move
    j "\"Ah...\""
    "Jun notices it too, letting his fur flutter against the wind."
    mc 1 c smile "\"Well, the weather sure took a nice turn all of a sudden.\""
    show j 1 c happy at fdis, four with move
    show k 1 c at fdis, two
    show sa 1 c happy at fdis, six
    show s 1 c smile at fdis, eight
    with dissolve
    sa "\"It's the world telling us it likes our plans!\""
    play sound "music/running.ogg"
    mc 1 c smile "\"Well, I certainly don't mind th-\""
    mc 1 c shock "\"Whoa!\"" with hpunch
    play sound "music/fall.ogg"
    show s 1 c shock at fdis
    show k 1 c shock at fdis
    show j 1 c shock at fdis
    show sa 1 c shock at fdis
    "Someone comes running off the street and bumps into me."
    s "\"Whaa, careful!\""
    "Shoichi reacts fast and grabs me before I can fall to the ground."
    "The other person isn't as lucky."
    mc 1 c wince "\"Hey, watch where you're going will y-\""
    "Girl" "\"Ow ow ow...\""
    "Fallen on the ground is a small akita girl, rubbing her back with a painful expression on her face."
    show sa 1 c sigh at fdis
    sa "\"Are you alright? Here, let me help.\""
    "Saya extends a helping hand and the girl takes hold of it, propping herself up."
    "Girl" "\"Thanks... And you, watch where you're going. What if I had gotten seriously hurt?\""
    mc 1 c shock "\"Wha- But I-\""
    show sa 1 c at fdis
    show k 1 c at fdis
    show j 1 c at fdis
    show s 1 c sigh at fdis
    s "\"You're the one who should watch it. What are you doing running around in the middle of the street, of course you're gonna bump into someone. You should be the one apologizing.\""
    "Girl" "\"What? But I'm so much smaller than he i- Ah!\""
    "As soon as her eyes focus on me, they go wide."
    "Girl" "\"You!\""
    "Her expression immediately turns sharp and she points at me with a yell."
    show sa 1 c think at fdis
    sa "\"You know her?\""
    mc 1 c think "\"Not that I recall...\""
    "Girl" "\"Wow, I can't believe I'd run into you here. Talk about an interesting turn of e-\""
    "Voice" "\"Mikiko, wait!\""
    show j 1 c watch at fdis, three
    show k 1 c at fdis, one
    show sa 1 c at fdis, five
    show s 1 c at fdis, seven
    with move
    show y 1 c smile at fdis, ten
    "Another akita runs towards us from the crowd."
    "He stops dead in his tracks when he sees the girl and walks up to her with a look of concern."
    "Boy" "\"Damn it, Mikiko, I told you not to go running off on your own. What if you ended up bumping o- Oh, you're talking to someone? Are these people you know?\""
    show s 1 c sigh at fdis
    s "\"Not really. Your friend there came running and crashed into my friend here.\""
    "Boy" "\"Wha- Jeez, Mikiko, I told you this was going to happen.\""
    "Mikiko" "\"Ah, whatever. Look, Yuu, look who it is!\""
    show s 1 c at fdis
    "She points at me, euphoric."
    "I have to take a step back because her finger nearly jabs me in the face."
    mc 1 c wince "\"Wow, careful there!\""
    "The boy follows her pointing finger and, as soon as his eyes fall on my face..."
    "Boy" "\"Ah!\""
    "Mikiko" "\"See, see. What did I tell you?!\""
    mc 1 c wince "\"Uhh... I'm sorry, what the hell is going on here?\""
    "The boy seems to completely ignore me."
    "Boy" "\"Ufufu, I never thought I'd run into you in the middle of the street. I've wanted to meet you in person for the longest time. Hmm... you're a lot bigger than I thought you'd be. {size=-2}Though I guess that makes sense...{/size}\""
    show s 1 c think at fdis
    s "\"Do you guys know [povFirstName] from somewhere?\""
    show s 1 c at fdis
    "Boy" "\"I sure do! He's been my idol for the longest time! Hehe, I can't wait to meet you again. That's gonna be loads of fun!\""
    "Boy" "\"I wish I could stay and chat, but we're actually late. Come on Mikiko, we have to hurry!\""
    "Mikiko" "\"Eeeh? But aren't you gonna do a declaration of war or something?!\""
    "Boy" "\"Don't be silly, there's no need for that. See you at the end of the month, [povLastName]-san! Bye!\""
    show y 1 c smile at offscreenright with moveoridis
    show j 1 c watch at fdis, four
    show k 1 c at fdis, two
    show sa 1 c at fdis, six
    show s 1 c at fdis, eight
    with move
    "He grabs the girl's wrist and drags her along the crowd as she kicks and protests."
    mc 1 c wince "\"W-Wait, I didn't get your... name...\""
    show s 1 c think at fdis
    show k 1 c avoid at fdis
    s "\"Well... that was odd.\""
    show s 1 c at fdis
    show sa 1 c think at fdis
    sa "\"You think it was someone who knew about you as a tennis player?\""
    s "\"Had to be. There's no other logical explanation for what happened.\""
    mc 1 c sigh "\"What just happened isn't \"logical\" no matter how you try to explain it.\""
    show k 1 c shock at fdis
    k "\"Ah!\""
    show sa 1 c shock at fdis, jumping
    show j 1 c shock at fdis, jumping
    show s 1 c shock at fdis, jumping
    "We all jump up in surprise as we hear Kei-kun shouting from behind us. Once he notices our reaction, he quickly apologizes."
    show k 1 c wince at fdis
    k "\"Oh, sorry, but that doesn't matter right now. I knew that guy was familiar to me!\""
    show j 1 c watch at fdis
    show s 1 c at fdis
    show sa 1 c at fdis
    j "\"You know him, Urushihara-san?\""
    show k 1 c avoid at fdis
    k "\"Yeah I do. He's a rising star in the world of tennis. One year younger than me, so he should be a first-year in High School by now. He was an unknown until two years ago, so I'm not surprised you haven't heard of him.\""
    show s 1 c think at fdis
    s "\"Oh, so when he said \"See you at the end of the month\", he must have meant the Prefecturals.\""
    show k 1 c at fdis
    k "\"Yeah, must have been that. His name is Yuuya Kokonose. To say he's a genius is to put it mildly. He's the sort of guy who plays completely by instinct, there's not real logic behind what he does. And he adapts to everything you do crazy fast too.\""
    show k 1 c worried at fdis
    k "\"He's the sort of player I hate playing against the most.\""
    show sa 1 c sigh at fdis
    show s 1 c smile at fdis
    show k 1 c at fdis
    s "\"Huh. That description reminds me of someone, actually.\""
    "Shoichi looks at me. Keisuke and Saya follow his gaze, nodding along."
    sa "\"Fits the bill spot-on, if I must say.\""
    k "\"Yeah, he's definitely very similar to [povFirstName]-san. The biggest difference between you two is that his style is more... explosive? I don't really know how to put it.\""
    show k 1 c avoid at fdis
    show sa 1 c at fdis
    k "\"Even if you don't focus too much on strategy, you're still always trying to come up with a way to avoid your opponent's strengths and play to their weaknesses. He doesn't. He willingly plays against them in their own game to let himself adapt. And he's crazy fast too.\""
    k "\"You can be completely crushing him one game and then get the tables completely reversed on you in the next one. I've played against him three times and haven't won once...\""
    show k 1 c at fdis
    show s 1 c at fdis
    s "\"You think he'd be trouble for [povFirstName] if they ended up playing each other?\""
    show k 1 c avoid at fdis
    k "\"Hmm... it's hard to say. If he's still the same way he was two years ago when I last played him, I'd say no, but I doubt he is.\""
    play sound "music/tap.ogg"
    show s 1 c happy at fdis
    "Shoichi puts a hand on my shoulder."
    s "\"Well, I guess that just means you have one more rival to worry about.\""
    mc 1 c sigh "\"As if I didn't have enough already...\""
    show s 1 c smile at fdis
    show k 1 c at fdis
    "He gives me a reassuring smile, though it doesn't really do much to take my mind off of it."
    "Yuuya Kokonose, huh... A player just like me? If we end up playing each other, that might end up as an interesting twist of fate."
    "Not that I believe in those things, of course."
    show j 1 c think at fdis
    j "\"Uhh... guys?\""
    stop music fadeout 2.5
    "Sho, Kei, Saya and [povFirstName]" "\"Yeah?\""
    j "\"Don't we still have to take a train to the park? Doesn't it have a fixed schedule?\""
    show s 1 c wince at fdis
    show k 1 c worried at fdis
    show sa 1 c shock at fdis
    "Sho, Kei, Saya and [povFirstName]" "\"Ah...\""
    s "\"Oh, shit, that's right. Come on, we're gonna have to run to the station!\""
    show j 1 c shock at fdis
    j "\"Wha- But I-\""
    mc 1 c avoid "\"No buts or we're gonna lose it!\""
    show j 1 c wince at fdis
    j "\"Didn't what just happen teach you guys anything about running on the street?!\""
    stop music3 fadeout 2.5
    scene BedroomN with fade
    play music "music/night.ogg" fadein 2.5
    "Ah, thank the gods for warm water. A good bath is all I needed today."
    "God, how my bed looks inviting right now."
    "Sheesh, I feel drained even though we didn't do much today..."
    "Well, I guess we ended up running around a lot."
    play sound "music/knock.ogg"
    a 1 c "\"Aniki, I found the videos you asked me to look for.\""
    mc 1 c smile "\"Ah, thanks, Aki. I'll be down in just a second."
    "No rest for the wicked, I suppose."
    scene LivingRoomN with fade
    show a 1 c at fdis, fiveh with dissolve
    "Aki's on the couch, fiddling around with the laptop and plugging it into the TV."
    a "\"What's with the sudden interest in other players?\""
    mc 1 c "\"I ran into the guy in the street today and one of my friends told me he might be trouble so I just got curious.\""
    a "\"Hmm... Well, from what I saw in the video, I don't think he will. But then again, the video is from last year...\""
    "He turns on the TV and it immediately opens to a paused video of a tennis court."
    a "\"The quality isn't all that great, but then again, this was taken from a phone.\""
    "He presses the play button as the screen comes to life. In it, I see the image from behind a certain Akita as he runs around returning all of his opponents shots."
    "Voice 1" "\"Go, Yuu!\""
    "Voice 2" "\"Yuuya, you can do it!\""
    "Voice 3" "\"Yuu-kun, I love you!\""
    "Voice 4" "\"Yuu-kun, go out with me!\""
    mc 1 c shock "\"Waah, he seems to be insanely popular.\""
    a "\"He reminds me a bit of you, actually. His style is very similar too.\""
    mc 1 c avoid "\"I can see that...\""
    "I guess he wasn't kidding when he said I was his idol. Did he base his play style around imitating mine or is it just coincidence?"
    a 1 c sigh2 "\"Well, either way, I don't think there's much for you to worry about. He's good, but his shots lack power, he's not as precise and his footwork is crude.\""
    mc 1 c "\"When did you become an expert on the subject?\""
    a 1 c avoid "\"Oh please, I've been watching you since I was a kid. Of course I can tell the difference between the imitation and the real thing.\""
    mc 1 c avoid "\"Huh, still...\""
    "Something about this guy bothers me, but I can't quite put my finger on it."
    a 1 c smile "\"Well, you can stay here watching the vid if you want. I'm going out with friends tomorrow morning so I'm crashing early. Good night.\""
    mc 1 c smile "\"Yeah, night, Aki.\""
    "I run my hand around his head, ruffling his fur."
    show a 1 c smile at fdis, offscreenleft with moveoledis
    "He gives me a warm smile and goes back upstairs."
    mc 1 c "\"... Why do you make me feel so uneasy?\""
    "Well, I guess I don't have much more to gain from staring at this video. As Aki pointed out, his style is basically a carbon-copy of mine, taken down a few pegs."
    "It don't see any reason to worry, and yet..."
    "I turn off the TV and the laptop."
    mc 1 c sigh "\"Guess I'm off to bed...\""
    stop music fadeout 2.5
    $ date = None
    jump Day8
