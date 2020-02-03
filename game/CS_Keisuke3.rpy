label keisukestart_2:
    $ uihide = True
    stop music2 fadeout 2.5
    $ keisukehearts += 1
    scene Station with fade
    play music "music/crowd01.ogg"
    "I stand in front of the station, patiently waiting for Keisuke to arrive."
    "Even though we're supposed to be in class right now, he asked me to skip today for some reason."
    "I guess when I said that I'd come with him as long as I was free, he took that to mean that I'd skip class for it."
    "... Which, to be honest, I totally would... and I did."
    "Still, he's running late."
    "You shouldn't ask someone to skip something for you and then make them wait."
    "It's just not cool."
    "Keisuke" "\"[povFirstName]-saaaan!\""
    play sound "music/running.ogg"
    "A voice calls out to me from amidst the crowd."
    "I strain my eyes to try and find the source among that giant mass of people."
    show k 1 c sigh at fdis, five with move
    k "*pant* *pant* *pant*"
    "Kei-kun finally walks up to me, breathing with difficulty, a few drops of sweat descending from his brow."
    play music2 "music/BGM/City Pulse.ogg" fadein 5.0
    mc 1 c shock "\"Kei-kun, are you okay?\""
    k "\"Y-yeah... just a little winded...\""
    show k 1 c at fdis
    k "\"Sorry I made you wait. There was no way I could slip past Alex today so I had to let him take me to school and then get changed to come over here.\""
    mc 1 c curious "\"Why would you get changed? If you were already dressed in your school clothes you could have just kept wearing them.\""
    show k 1 c sigh at fdis
    k "\"What if someone spots a student that is clearly not at school? They could have called the school on us.\""
    mc 1 c sigh "\"I think you're being a little too paranoid here.\""
    "Ditching school isn't all that uncommon. No one would give a shit anyway."
    mc 1 c think "\"Well, I guess everything's okay either way. I suppose you had no reason {i}not{/i} to change out of your uniform.\""
    show k 1 c smile at fdis
    k "\"You got that right. At least you're not being too fussy about it.\""
    "The only one here that is fussy is you..."
    mc 1 c smile "\"Well, putting that aside for now, have you managed to think of something you want to get for Alex?\""
    show k 1 c avoid at fdis
    k "\"Not really. We don't have much information on him even in our database. He really is a shadow.\""
    show k 1 c calm at fdis
    k "\"Not to worry, though. I've been working really hard on remembering even the most minute details of our interactions and I think I might have struck gold.\""
    "As opposed to going for the more sane approach of... asking."
    mc 1 c think "\"Oh yeah? What was it?\""
    show k 1 c smile at fdis
    k "\"I remember that I caught Alex reading books on old civilizations more than once. In fact, most of the books that I ever saw him read are about that.\""
    show k 1 c avoid at fdis
    k "\"Now, I don't really know which ones he's already read or if he even has a preference for any specific tribe. But I do know for a fact that he likes this sort of stuff.\""
    show k 1 c sigh at fdis
    k "\"Sorry if it's not a very concrete lead but it's all I've got so far.\""
    "Things would be much easier if you'd just talk to him ya know?"
    mc 1 c considerate "\"No problem, let's just hope we can find something that caters to that.\""
    mc 1 c smile "\"Would it be safe to assume that we'll be heading to the book store, then?\""
    show k 1 c smile at fdis
    k "\"Yes. There's a book store nearby that has a great selection of history books from what I've researched online. They might be our safest bet at the moment.\""
    mc 1 c considerate "\"You... only looked for history books?\""
    show k 1 c at fdis
    k "\"Yeah, why?\""
    mc 1 c considerate "\"Nothing, it's just that... well... \"history\" is a pretty broad category. Just because they have history books doesn't mean they'd have books on old civilizations.\""
    show k 1 c at fdis
    k "\"I... didn't think about that.\""
    mc 1 c sigh "\"Well, whatever. Let's just go there and hope they have something.\""
    show k 1 c avoid at fdis
    k "\"Great... now I'm not feeling so sure about this.\""
    mc 1 c smile "\"Don't sweat, you'll be fine.\""
    show k 1 c sigh at fdis
    k "\"How can you be both a source of negativity and positivity at the same time?\""
    mc 1 c happy "\"Lots and lots of practice.\""
    k "\"Either that or you're just crazy.\""
    mc 1 c think "\"Could be a little bit of both for all we know.\""
    show k 1 c uncomfortable at fdis
    k "\"You're not supposed to agree with me, you know?\""
    mc 1 c smile "\"Yeah, I know. It's just more fun this way. Messes with your head.\""
    show k 1 c sigh at fdis
    k "\"Just shut up and let's go already.\""
    mc 1 c think "\"Now you're telling me to shut up? I thought you called me over to ask for my input.\""
    k "\"Yes, and I'm already starting to regret it.\""
    mc 1 c happy "\"Aww, don't be so mean, Kei-kun. I know you love me!\""
    show k 1 c angry at fdis
    k "\"Just shut up already!\""
    stop music fadeout 2.5
    stop music2 fadeout 2.5
    scene Bookstore
    show k 1 c at fdis, five
    with fade
    play music3 "music/BGM/Hanging Out.ogg" fadein 5.0
    "Ah, the refreshing, artificial coldness that comes with air conditioning."
    "Even when it's not overwhelmingly hot, it's still such an amazing feeling to walk into a fully air-conditioned room."
    "It makes me miss my bedroom."
    k "\"I'm gonna take a look at the history section.\""
    show k 1 c at offscreenright with moveoridis
    mc 1 c worried "\"Or you could just... ask the clerk...\""
    mc 1 c sigh2 "\"Goddammit, you could at least let me get a word in before walking off.\""
    "Stupid impatient rabbit."
    "... Or is it a hare?"
    "I can never tell the difference."
    "Good thing this place isn't too big. No chance of me getting lost."
    "Now, the history section should be somewhere around..."
    "Huh?"
    "I-it's not next to the geography section? Those two are usually always together."
    "There are so many bookcases, I can't even tell which is which."
    "Are they color coded? No, doesn't seem like it."
    "There's nothing signaling it either."
    "What the hell is wrong with this place?!"
    "I know this isn't some big franchise bookstore but come the fuck on, at least organize your shit!"
    "There he is!"
    show k 2 c scorn at fdis, five with dissolve
    k "\"... no, no, no...\""
    "Keisuke is inspecting each and every one of the books, mumbling to himself as he checks them."
    "Every now and then he'll pull one out of the bookcase, flip through the pages and then put it back."
    mc 1 c sigh "\"What are you doing?\""
    show k 1 c at fdis
    "As if he only just now noticed my presence, he readjusts himself, turning to look at me."
    k "\"Ah, [povFirstName]-san, there you are."
    show k 1 c sigh at fdis
    extend "Where have you been? Please don't just wander off without a word like that.\""
    mc 1 c shock "\"What?! But you're the one who-\""
    "Ah, you know what, forget it. There's no way I'm gonna be able to get him to realize it himself."
    mc 1 c sigh "\"Either way, have you found something yet?\""
    show k 1 c avoid at fdis
    k "\"Not yet. They really do have a pretty big collection but none of them seems right.\""
    mc 1 c sigh2 "\"You know, we could save ourselves a lot of trouble if you just ask the clerk if they have any books on ancient civilizations in stock.\""
    show k 1 c shock at fdis
    k "\"They can do that?\""
    mc 1 c annoyed "\"Of course they can. What the hell were you expecting?\""
    "You really are out of touch with society..."
    show k 1 c avoid at fdis
    k "\"I... I didn't know. It didn't even occur to me.\""
    mc 1 c sigh "\"How clueless can a person be? Jeez.\""
    show k 1 c wince at fdis
    k "\"You don't need to be that harsh on me...\""
    mc 1 c sigh2 "\"Fine, fine. Let's just go talk to the clerk and see if there's anything here.\""
    show k 1 c avoid at fdis
    k "\"Agreed.\""
    "At least he's not stubbornly fighting me on this."
    "We head to the front desk where the clerk is writing something down on a notebook."
    "He watches us approach, putting the book and the pencil down and standing up to greet us."
    show k 1 c at fdis
    "Clerk" "\"Good morning. What can I do for you?\""
    k "\"I'm looking for books on a specific topic. Do you have any way of checking your system to see if you have any?\""
    "Clerk" "\"Of course. All of our books are tagged in our system using their genre, topics, authors, publisher and year of release. I can certainly check the system to see if we have anything that matches your criteria. What sort of book are you looking for?\""
    mc 1 c "\"We're looking for a book on ancient civilizations.\""
    "The badger shifts his weight, crossing his arms and adopting a thoughtful look."
    "Clerk" "\"Ancient civilizations, huh? You mean things like Ancient Egyptians, Greeks, Romans or things like the Mayans, Aztecs and other ancient tribes?\""
    show k 1 c wince at fdis
    k "\"Is... is there a difference?\""
    "Clerk" "\"Of course. While I can't guarantee we'll have books on either of those without first checking the system, there's a big difference between them depending on what continents they are from. European civilizations are different from American ones which are different from Asian ones. So on and so forth.\""
    show k 1 c avoid at fdis
    k "\"I admittedly don't know much about this kind of thing. The book is supposed to be a gift for a friend who really likes them. I don't know if he has a specific interest in one kind.\""
    "Clerk" "\"Alright, so I guess a broader search is in order then. Let's see what the system has to say about it.\""
    "He types a few words on his computer. It's a pretty old, boxy looking system that looks to be at least six or seven years old."
    "But I guess I can't expect anything very grand from a neighborhood store."
    "The badger purses his lips."
    "Clerk" "\"Unfortunately it seems that we don't have any more books matching that criteria. This might come as a surprise to you but we've completely sold out on all of our books fitting that genre. We've been downsizing the history section lately so we don't hold as many copies of those kinds of books anymore.\""
    show k 1 c sigh at fdis
    k "\"That's really unfortunate."
    show k 1 c avoid at fdis
    extend " I guess I'll have to check another place...\""
    "The man nods, a considerate smile on his face."
    "Clerk" "\"Maybe you might want to check an Antique store? They're more likely to have the things you're looking for. They'd usually have books talking specifically about ancient civilizations and artifacts. Who knows, you might have better luck finding pieces of history there. Just be prepared for the higher prices.\""
    show k 1 c at fdis
    k "\"I don't think that would be a problem but I have no idea where I could find one.\""
    mc 1 c smile "\"We can always use our phones to check.\""
    show k 1 c worried at fdis
    k "\"W-well...\""
    "Clerk" "\"Oh, there's no need. I do happen to know of a few in the city and regularly correspond with their owners. I can write down the addresses for you.\""
    show k 1 c smile at fdis
    k "\"Oh, that's pretty helpful. Thank you!\""
    mc 1 c smile "\"Quite convenient that you'd have this kind of information too.\""
    "The badger smiles, rubbing the back of his head bashfully."
    "Clerk" "\"I'm a college student majoring in Archeology so I'm quite passionate about this kind of thing. I wrote down my personal recommendations of stores you should visit first. Hopefully you'll be able to find what you're looking for.\""
    show k 2 c gentle at fdis
    k "\"Thank you. That's really kind of you!\""
    "Clerk" "\"Any day. I just like seeing people showing an interest in history. Have a nice day.\""
    show k 1 c smile at fdis
    mc 1 c smile "\"You too.\""
    stop music3 fadeout 2.5
    scene Street1
    show k 1 c smile at fdis, five
    with fade
    play music "music/crowd01.ogg" fadein 5.0
    play music2 "music/BGM/On My Way.ogg" fadein 5.0
    "Damn, I miss the cool air-conditioned environment already."
    show k 1 c smile at fdis
    k "\"Well, that was a bust.\""
    mc 1 c smile "\"At least you got some places recommended to you. It's better than nothing.\""
    show k 1 c smile at fdis
    k "\"True. Although I'd still have preferred if we'd managed to end our search here.\""
    mc 1 c happy "\"Wouldn't it have been kinda anticlimactic if we'd come all the way here just to finish everything in five minutes though? Where's the fun in that?\""
    show k 1 c sigh at fdis
    k "\"It's not like we're going out to have fun you know?\""
    mc 1 c smile "\"Doesn't mean we can't have any.\""
    show k 1 c avoid at fdis
    k "\"I... suppose that's true.\""
    show k 2 c gentle at fdis
    k "\"Yeah, you're right. There's no reason why we can't have fun while we're at it, is there?\""
    show k 1 c smile at fdis
    k "\"We already skipped class anyway so there's no way we're going to get in.\""
    mc 1 c happy "\"Yup. You got it.\""
    mc 1 c smile "\"Now, where do you want to go to first?\""
    show k 2 c think at fdis
    k "\"Hmm... well, according to the paper he gave us, his top recommendation would require us to take the subway. It's probably a twenty minute trip.\""
    mc 1 c smile "\"That's not too bad.\""
    show k 1 c smile at fdis
    k "\"Agreed."
    show k 2 c gentle at fdis
    extend " It's also almost lunch time too. How about we stop somewhere to have some food first? My treat.\""
    mc 1 c wince "\"I don't know how I feel about that.\""
    show k 1 c smile at fdis
    k "\"Come on, when are you going to stop being so stuck up about it?\""
    show k 2 c gentle at fdis
    k "\"I'd love to be able to treat you. Are you going to make me beg for your permission?\""
    mc 1 c considerate "\"You've really become fixated on treating me, huh?\""
    show k 1 c smile at fdis
    k "\"That's because it's fun."
    show k 2 c gentle at fdis
    extend " I don't get the chance to go out with you just the two of us often. I really like it when we get time alone together. Is it so weird for me to be having fun?\""
    play sound "music/heartbeat.ogg"
    "!!!"
    mc 1 c shockb "\"T-that's... uhm... wow...\""
    show k 1 c at fdis
    k "\"What? Is something wrong?\""
    mc 1 c avoidb "\"N-no, nothing at all. You just... er... caught me a bit by surprise there.\""
    show k 2 c scorn at fdis
    k "\"What? But I didn't do anything... did I?\""
    "Let's just hope you'll continue to be clueless..."
    mc 1 c considerate "\"I guess I'll accept your offer then.\""
    show k 1 c smile at fdis
    k "\"That's great. Is there any place you'd prefer to go to?\""
    mc 1 c think "\"Not really. I'm fine with whatever.\""
    show k 1 c calm at fdis
    k "\"In that case, I know of a great steakhouse nearby that I'm sure you'd love.\""
    mc 1 c sigh "\"Why do I get the feeling that it's going to be another one of those places where everything costs a kidney?\""
    show k 1 c smile at fdis
    k "\"It's not... or at least I think it's not."
    show k 2 c gentle at fdis
    extend " We'll just have to see when we get there, won't we?\""
    "Not helping one bit..."
    stop music fadeout 2.5
    scene Restaurant
    show k 1 c smile at fdis, five
    with fade
    "I have to admit, this is certainly not what I was expecting."
    mc 1 c pout "\"You tricked me. This is just the diner Saya works at.\""
    show k 2 c gentle at fdis
    k "\"It is. But the look on your face was priceless just now.\""
    show k 1 c smile at fdis
    k "\"You really were expecting me to take you someplace outlandish, weren't you?\""
    mc 1 c avoidb "\"W-well...\""
    show k 1 c calm at fdis
    k "\"It turns out that I really like the food in here so I was kinda itching to come over.\""
    show k 1 c smile at fdis
    k "\"I hope that's okay with you.\""
    mc 1 c smile "\"It is. I like this place... although it'll be a bit weird to not get served by Saya-chan.\""
    k "\"You'll be fine. Start thinking of what you're going to order already so we won't have to wait long, okay?\""
    mc 1 c fsmile "\"Don't you start with that too.\""
    show k 2 c gentle at fdis
    k "\"Sorry, I couldn't resist.\""
    show k 1 c smile at fdis
    "We take a seat in one of the nearby booths, picking up the menus to check what is available."
    k "\"I think I'm just gonna order a grilled steak with mashed potatoes.\""
    mc 1 c think "\"That does sound pretty good... although I was fully expecting you to order curry again.\""
    show k 1 c calm at fdis
    k "\"Curry is good but that doesn't mean I want to have it all the time. I prefer varying on what I eat.\""
    mc 1 c smile "\"The complete opposite of Mr. Shoichi \"Give me Soba\" Urata.\""
    show k 2 c gentle at fdis
    k "\"He'd probably hit you if he heard you calling him that.\""
    mc 1 c laugh "\"Indeed he would. Hahaha.\""
    show k 1 c smile at fdis
    k "\"What about you? Any idea what you'll be having?\""
    mc 1 c think "\"Hmmm... that's a tough question.\""
    show k 1 c worried at fdis
    k "\"I know I said it as a joke but please try not to take too long to come up with your order.\""
    mc 1 c wince "\"Alright alright, I get it. I'll try to be quick. Jeez.\""
    "You and Shoichi really are birds of a feather..."
    show k 1 c at fdis
    mc 1 c think "\"...\""
    show k 1 c avoid at fdis
    mc 1 c think "\".....\""
    show k 1 c sigh at fdis
    mc 1 c think "\"........\""
    show k 1 c angry at fdis
    k "\"Just pick something already!\"" with hpunch
    mc 1 c shock "\"Awawawa, the steak. I'll have the steak!\""
    show k 1 c annoyed at fdis
    k "\"Goddamnit, he wasn't kidding when he said you took a lifetime to pick.\""
    mc 1 c pout "\"It hasn't even been that long.\""
    show k 1 c avoid at fdis
    k "\"We've been here for ten minutes. {size=-2}The waitress is even staring at us because we haven't ordered anything yet.{/size}\""
    mc 1 c fsmile "\"O-oh... hehehe, sorry.\""
    show k 1 c sigh at fdis
    k "\"What am I going to do with you...\""
    show k 1 c at fdis
    k "\"Well, it doesn't matter right now. So you'll have the steak with mashed potatoes like me?\""
    mc 1 c considerate "\"Yeah... to be fair, everything looks so good that I have a hard time picking.\""
    show k 1 c sigh at fdis
    k "\"And yet you still ended up picking the same thing as I did.\""
    mc 1 c pout "\"You didn't give me much time to consider.\""
    show k 1 c annoyed at fdis
    k "\"Ten minutes is more than enough time. You're just too indecisive.\""
    mc 1 c think "\"... Can't argue with that.\""
    "Keisuke calls over the waitress and orders for us, even apologizing about the delay."
    "He really can be quite courteous when dealing with people."
    show k 1 c at fdis
    mc 1 c curious "\"...\""
    k "\"...\""
    show k 1 c sigh at fdis
    k "\"... You're staring at me. Is something the matter?\""
    mc 1 c shock "\"Oh! No no, it's nothing. I'm sorry.\""
    show k 1 c avoid at fdis
    k "\"Is that so?\""
    mc 1 c considerate "\"I was just wondering something. You told me a while ago that you have problems coming to these more... regular stores, if I can call them that.\""
    mc 1 c smile "\"But you still dealt with the waitress without a hitch.\""
    show k 1 c avoidb at fdis
    k "\"It's not like I'm incompetent, you know. I just feel really nervous about it.\""
    show k 1 c avoid at fdis
    k "\"I haven't visited simpler places like these since I began living as the heir to the Urushihara Corporation. Whenever I come to them alone, I'm always afraid that I'll do or say something offensive because I don't know people all that well.\""
    show k 1 c sigh at fdis
    k "\"For good or for bad, most of my life experience has involved rich, sniveling sycophants or servants."
    show k 1 c avoid at fdis
    extend " I haven't really dealt with regular people much before.\""
    mc 1 c curious "\"I've actually always wondered about that. Our school might be pretty well-off but it doesn't seem like the kind of place you'd attend. Why's that?\""
    k "\"...\""
    mc 1 c "\"Kei-kun?\""
    show k 1 c sigh at fdis
    k "\"You... I...\""
    show k 1 c avoid at fdis
    k "\"... You're not wrong. My family was wholly opposed to me studying here. Up until middle school I'd only studied in schools for rich families. The monthly tuition alone was probably enough to buy a house in the suburbs...\""
    mc 1 c uncomfortable "\"That's... kind of a terrifying thought.\""
    show k 1 c sigh at fdis
    k "\"I know... or at least I know nowadays. I never really thought much about it before.\""
    show k 1 c avoid at fdis
    k "\"I really felt out of place when I first transfered to our school. It was only because of you guys that I was able to fit in.\""
    mc 1 c smile "\"I'm glad you did, though. I can't really imagine our group without you in it.\""
    show k 1 c smile at fdis
    k "\"Heh. You're being too polite.\""
    mc 1 c curious "\"Still, what led you to transfer to our school in the first place?\""
    show k 1 c avoid at fdis
    k "\"That's... I think I prefer to leave that story for another day...\""
    mc 1 c worried "\"Aww, you don't want to tell me?\""
    show k 1 c eyesc at fdis
    k "\"To be honest? Not really.\""
    mc 1 c wince "\"Ouch. Way to be blunt.\""
    show k 1 c avoid at fdis
    k "\"Sorry... this just isn't a story that I'm comfortable with telling you...\""
    mc 1 c considerate "\"It's fine. I didn't mean to pry. Sorry about that.\""
    k "\"...\""
    mc 1 c considerate "\"...\""
    "..."
    "Oh boy, talk about awkward silence."
    show k 1 c sigh at fdis
    k "\"Really wish the food would arrive right about now...\""
    mc 1 c considerate "\"True that.\""
    show k 1 c at fdis
    k "\"True that? Since when do you talk like that?\""
    mc 1 c happy "\"Oh, you noticed? I've been meaning to learn to be a little more street-wise, ya know? I figured it might be useful once I'm in the US. It'll let me blend in easier!\""
    show k 1 c sigh at fdis
    k "\"...\""
    mc 1 c confused "\"What? Why are you looking at me like that?\""
    k "\"It's just... there's so much wrong with what you just said that I don't even know where to start...\""
    mc 1 c wince "\"O-oh.\""
    show k 1 c at fdis
    "The waitress appears by our table, plopping down our plates with a smile on her face."
    "The food is steaming hot and looks incredibly appetizing."
    show k 1 c smile at fdis
    k "\"Thank you.\""
    "The girl nods, her smile widening, before leaving to attend to her other tables."
    k "\"I like how quick the service is here.\""
    mc 1 c smile "\"Well, this is a maid cafe run by bunny girls and bunny themed. I'd imagine speed is a theme.\""
    show k 1 c sigh at fdis
    k "\"... Again, there's so much wrong with that that I don't even know where to start...\""
    stop music2 fadeout 2.5
    scene Antique
    show k 1 c at fdis, five
    with fade
    play music3 "music/BGM/Let It Happen - Narr.ogg" fadein 5.0
    "I'm a bit surprised once we walk into the Antiquity shop."
    "I fully expected some dusty old place with little lighting and ugly decor."
    "Instead, it's a pretty cozy environment that doesn't really look all that different from a regular store."
    mc 1 c smile "\"I like this place.\""
    show k 1 c eyesc at fdis
    k "\"That's not hard to achieve. All a store needs is air-conditioning and you already like it.\""
    mc 1 c happy "\"You're not exactly wrong there.\""
    show k 1 c at fdis
    k "\"I certainly wasn't expecting to see a security guard on the front door though.\""
    "?" "\"That's because we have many priceless artifacts here. Things from over a thousand years ago. Safety is our primary concern.\""
    "We turn to look at the front counter where a young looking horse dressed in a black leather jacket leaned on the counter, looking at the two of us with a smirk."
    mc 1 c smile "\"Oh, good afternoon. You work here?\""
    show k 1 c sigh at fdis
    k "\"Of course not. He's just standing behind the counter and talking to customers because it's fun.\""
    mc 1 c wince "\"Y-you didn't have to be rude.\""
    show k 1 c smile at fdis
    k "\"Don't ask stupid questions then.\""
    "The horse chuckles."
    "Owner" "\"I guess you could say so. I'm the owner of this store.\""
    show k 1 c shock at fdis
    mc 1 c shock "\"Wait, you're the owner?!\""
    "He smiles smugly, leaning forward on the counter."
    "Owner" "\"Yes. Why the shock?\""
    show k 1 c avoid at fdis
    mc 1 c uncomfortable "\"I-it's just that... uhm... you look very...\""
    "Owner" "\"Young? Yeah, I get that a lot. Not many people expect the owner of an antiquity shop to be a 28-year old stud.\""
    k "\"{size=-4}Stud? Certainly not modest either.{/size}\""
    "His smile widening, the horse put a hand on his hip."
    "Owner" "\"I also have excellent hearing. And no, modesty and I don't get along.\""
    play sound "music/stab.ogg"
    show k 1 c wince at fdis, shake1
    k "\"S-sorry.\""
    "Owner" "\"It's alright, I don't really mind. This used to be my father's store. I inherited it three years ago when I finished my doctorate's degree in Archeology. So, yeah, I might be young but I'm certainly not a greenhorn. What can I help you with?\""
    show k 1 c at fdis
    k "\"I was originally looking for some books on ancient civilizations that I could gift to a friend of mine who is interested in the subject. I don't suppose you'd have any?\""
    "The owner's smile widens."
    "Jumping over the wooden counter, he walks past us."
    "Owner" "\"I certainly do. Come with me if you will. You're quite lucky. My father didn't stock many books in the past, it was mostly only artifacts, but I find that people pursuing knowledge in history deserve to be coddled. So even if they're not antiques themselves, I still love to have them in my store.\""
    "He walks us upstairs to a second floor where there are many shelves stocked all the way up with books."
    show k 1 c shock at fdis
    k "\"W-woah.\""
    "Owner" "\"Impressive, right? I can confidently say I have the greatest collection of history books in all of Kanto. We get quite a bit of business from professors, college students and history buffs alike. Adding this little library here has more than quadrupled our profits.\""
    "Owner" "\"The lesson here is, never underestimate the small sales.\""
    show k 1 c at fdis
    mc 1 c smile "\"I can see that.\""
    "Owner" "\"Ancient civilizations are the reason I went into Archeology in the first place. Mesoamerican civilizations were the focus of my doctorate dissertation. So lucky for you, you walked into the best store if you're looking for that sort of things.\""
    show k 1 c smile at fdis
    k "\"I can see why the clerk at the book shop recommended me to come here first.\""
    "The horse's grin immediately widens."
    "Owner" "\"Clerk at a book shop? Would that by any chance be a lean, kinda dorky looking badger?\""
    show k 1 c at fdis
    k "\"Yeah, that's him.\""
    "Owner" "\"Heh, that Manabu certainly doesn't waste an opportunity to gush about my store. I'll have to give him a present later. You guys are probably the tenth group of customers he's sent to me in the past week alone.\""
    mc 1 c smile "\"That's pretty nice of him.\""
    "Owner" "\"There aren't many people interested in these things, especially here in Japan. Most Archeology students tend to be interested in Asian history which I myself find pretty boring.\""
    "Owner" "\"But... well, you didn't come here to hear me ramble on, did you? Make yourselves at home. Browse as much as you'd like and feel free to come to me to ask questions.\""
    "He walks back downstairs, leaving the two of us to marvel at the giant collection in front of us."
    mc 1 c talk "\"Damn. These are all coded too. Mayans, Aztecs, Incans, Egyptians, Greeks... there are so many here that it would take me all day to even list them all.\""
    mc 1 c "\"I didn't even know there were enough people interested in history to warrant a store this big.\""
    show k 1 c smile at fdis
    k "\"Neither did I. But I guess this goes to show that history really is a popular subject despite all odds.\""
    mc 1 c happy "\"To be honest, I'd really imagine you being the kind to enjoy this sort of thing.\""
    show k 1 c avoid at fdis
    k "\"Eugh... no. Alex tried to get me into it but it was just too boring for me.\""
    show k 1 c smile at fdis
    k "\"Still, I can understand him liking it and I'm happy that it's a popular enough subject to warrant having a store like this.\""
    mc 1 c smile "\"You really can be Mr. Sunshine when you want to, huh?\""
    show k 1 c at fdis
    k "\"I don't know what you're talking about.\""
    mc 1 c happy "\"Sure you don't.\""
    mc 1 c smile "\"Anyway, do you have any idea what kind of book you want to get for him? They seem to have so many here.\""
    show k 1 c smile at fdis
    k "\"True. I feel tempted to get more than one. Who knows what kind of relic I can find?\""
    mc 1 c happy "\"Alternatively, you could buy him an actual relic.\""
    show k 1 c shock at fdis
    k "\"...\""
    show k 2 c gentle at fdis
    k "\"That's a great idea!\""
    mc 1 c shock "\"W-what? I was joking. Those must cost a fortune!\""
    show k 1 c smile at fdis
    k "\"Oh, yes, because that's somehow going to be a deterrent for me.\""
    mc 1 c think "\"Oh yeah...\""
    show k 2 c scorn at fdis
    k "\"Hmm... now that you mentioned it, I remember seeing a few old looking things in his apartment when I visited.\""
    show k 1 c smile at fdis
    k "\"Although I've only been there once since he rented it not long ago.\""
    mc 1 c "\"Where was he living before that, then?\""
    show k 1 c at fdis
    k "\"The people working for my family are given housing close to our estate. They are still allowed to get apartments or houses of their own in the city but they're only allowed to spend the night in them when they're off shift.\""
    mc 1 c wince "\"That... doesn't sound very nice.\""
    show k 1 c smile at fdis
    k "\"Our servants have access to high speed internet, pools, gyms, sports centers and free food while they're at work.\""
    mc 1 c shock "\"... Where can I sign up?\""
    show k 2 c gentle at fdis
    k "\"Don't be ridiculous.\""
    show k 1 c smile at fdis
    k "\"But I do like the idea of buying him an actual relic. I think that might be even better than a book.\""
    show k 2 c scorn at fdis
    k "\"Let's see... I remember him having something that looked like a fossilized tooth and a few drums that looked to be hundreds of years old...\""
    show k 1 c at fdis
    k "\"I'll go downstairs to ask the owner if he has something like that.\""
    show k 1 c at fdis, offscreenleft with moveoledis
    "..."
    "People that have tons of money to spend are scary."
    scene Antique
    show k 1 c smile at fdis, five
    with fade
    "I walk back downstairs to see Keisuke chatting excitedly with the owner."
    "The horse is beaming with excitement as he points out a few knick-knacks on the shelves."
    "Owner" "\"That one is a portable hand drum used by the Mayans about three thousand years ago. It was used mostly for religious rituals. This one in specific was found next to an altar in a temple.\""
    "Owner" "\"Due to the location it was found in and the fact that it was covered in stains that were later confirmed to be human blood, we believe that this particular drum was used in rituals of human sacrifice.\""
    mc 1 c wince "\"... What the hell kind of conversation did I just walk into?\""
    show k 2 c gentle at fdis
    k "\"Ah, [povFirstName]-san. Naomasa-san was explaining to me about the different drums they have here. I asked him for the oldest and most valuable ones.\""
    mc 1 c sigh "\"... I know your family has a lot of money but can you even pay for that kind of thing?\""
    show k 1 c at fdis
    k "\"Do you need me to show you how much I have in my savings account?\""
    mc 1 c sigh2 "\"No. I'm pretty sure it'd scar me forever...\""
    mc 1 c "\"Also, since when did you know the owner's name?\""
    "The stallion smiles, walking up to me and holding out his hand."
    "Shigeru" "\"That's because once your friend talked about buying something so expensive, I just felt that I needed to properly introduce myself.\""
    "Shigeru" "\"While we have these mostly for show, selling them is incredibly rare. A purchase like that is enough to keep us afloat for years! But I'm just rambling again... I'm Shigeru Naomasa. It's a pleasure!\""
    "... Afloat for years?"
    mc 1 c fsmile "\"H-how much does one of these even cost?\""
    "He purses his lip, grabbing a folded piece of paper that was lying on top of the counter and showing it to me."
    "?!?!?!?!?!"
    mc 1 c shock "\"...\""
    show k 1 c sigh at fdis
    k "\"Don't even think about commenting on it.\""
    mc 1 c uncomfortable "\"... You must really like Alex, huh?\""
    show k 1 c at fdis
    k "\"Of course I do. He practically raised me.\""
    "Still, this... this is a lot..."
    mc 1 c fsmile "\"You're really generous sometimes, huh?\""
    show k 1 c eyesc at fdis
    k "\"I like to think I'm generous all the time.\""
    show k 1 c smile at fdis
    k "\"Still, that ritual drum sounds perfect. I'll take it.\""
    "The stallion's eyes are open so wide that it almost looks like they're twinkling with unbound happiness."
    "Shigeru" "\"That was an incredible choice, sir. I'll have it wrapped and delivered by the end of the day. Thank you very much!\""
    "Smiling, Keisuke pulls out his credit card."
    k "\"I'm the one that needs to thank you. I found a present even better than what I was expecting!\""
    stop music3 fadeout 2.5
    scene Station
    show k 1 c smile at fdis, five
    with fade
    play music2 "music/BGM/Dog Days.ogg" fadein 5.0
    "Keisuke hums cheerfully during all of the subway trip."
    "He seems to be so happy and engrossed in his song that I don't have the heart to interrupt him and chat."
    "In fact, I like hearing his humming voice. It's such a pleasant melody."
    show k 2 c gentle at fdis
    k "\"I can't believe everything worked out so well!\""
    "Those are the first words he says since we left the store."
    mc 1 c smile "\"You certainly do look happy about it.\""
    show k 1 c smile at fdis
    k "\"How could I not be? I got the perfect present for Alex!\""
    "And I can't stop thinking about the fact that that thing is probably worth more than my house."
    mc 1 c "\"How do you plan on giving it to him?\""
    show k 1 c at fdis
    k "\"I still have to figure that part out. I don't want it to seem like I'm trying to buy his forgiveness like you said. I just need to find a way that shows him this is just me trying to make amends.\""
    "A cheaper present probably would have made that easier..."
    mc 1 c smile "\"That sounds fair enough. I'm sure you'll figure something out.\""
    show k 1 c smile at fdis
    k "\"Thanks. And thank you for coming with me too. It was a lot less boring having someone else around.\""
    mc 1 c happy "\"Don't worry about it, it was my pleasure.\""
    mc 1 c smile "\"By the way, if you don't mind me asking, how's that band thing coming along?\""
    show k 1 c at fdis
    k "\"Band thing?\""
    mc 1 c smile "\"You know. You told me a few days ago that you'd joined the Light Music club and their band.\""
    show k 1 c avoid at fdis
    k "\"Oh... right...\""
    mc 1 c happy "\"Did you become a vocalist or a guitarist? Oh, maybe you're doing both? That would be so cool!\""
    k "\"I... err...\""
    mc 1 c confused "\"What's with that unenthusiastic reaction?\""
    show k 1 c sigh at fdis
    k "\"I... haven't performed for them yet. I'm just their manager at the moment.\""
    mc 1 c shock "\"What? Why not?\""
    show k 1 c avoid at fdis
    k "\"Because I was embarrassed. These people are really good. There's no way I could take their place. And why would they let some newcomer play with them when they've been together for two years already.\""
    mc 1 c "\"Isn't that the whole point of a club?\""
    k "\"I... I guess? Still, I can't bring myself to perform in front of them. I'm just so embarrassed that I can't do it.\""
    mc 1 c sigh2 "\"Then what was the point of joining the club in the first place?\""
    k "\"... No comment.\""
    mc 1 c "\"... Can you at least let me come watch their rehearsal?\""
    show k 1 c wince at fdis
    k "\"W-what?\""
    mc 1 c smile "\"If they're that good and you're their manager then there shouldn't be any problem if I just came over to watch right?\""
    mc 1 c happy "\"Maybe you could introduce me to your new friends.\""
    show k 1 c worried at fdis
    k "\"I... I guess I could.\""
    show k 1 c at fdis
    k "\"You know what... you helped me so much with this problem with Alex already..."
    show k 1 c smile at fdis
    extend " Sure, I'll introduce you to them once this situation with Alex is resolved... against my better judgement.\""
    mc 1 c confused "\"Why is it against your better judgement?\""
    show k 1 c calm at fdis
    k "\"No comment on that either.\""
    show k 1 c smile at fdis
    k "\"Anyway, now that we're done with this, I'm gonna get changed into my school uniform and wait until classes end at the ice cream shop. You wanna come with me?\""
    mc 1 c smile "\"Sure. I have nothing better to do anyway.\""
    show k 2 c gentle at fdis
    k "\"Great. I'm sure it won't be boring if you're around.\""
    scene Sky with fade
    "Keisuke and I kill the next hour until the school bell rings before he rushes back to the gates to be picked up."
    "He really is pretty good at skulking around without being found out by his family, I'll give him that."
    stop music fadeout 2.5
    stop music2 fadeout 2.5
    $ date = None
    jump cs_final
