label Day16_Jun:
    window hide
    scene May28 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    play music "music/crowd01.ogg" fadein 5.0
    scene ConcertLobby with fade
    window show
    $ date = "day16"
    "I sit on a bench, fiddling with my phone as I wait around."
    "I know that I ended up being a bit early but I didn't expect to wait around this long."
    "God, they're late..."
    "Then again, considering who I'm talking about..."
    "?" "\"[povFirstName]-san?!\""
    "I hear a voice calling my name in shock and surprise."
    "A smile immediately creeps up onto my face as I look up to see who it is."
    show j 1 c shock at fdis, five
    show ats 1 n c smile at two
    show yui 1 c smile at eight
    with fade
    "I muster my best innocent smile when I see the family of tigers looking down at me."
    "Jun's dad waves excitedly at me, a beaming smile on his face."
    "Jun himself has the most wide open eyes, completely shocked to see me."
    mc 1 c happy "\"Hey there.\""
    j "\"Wh-what are you doing here?\""
    mc 1 c smile "\"I asked your mom yesterday where your competition would be taking place and what the time was so I could come watch.\""
    show j 1 c wince at fdis
    j "\"What? M-mom!\""
    yui "\"Oh my, wasn't I supposed to tell him?\""
    mc 1 c happy "\"Hahaha. Sorry, I told her you had given me the details but that I forgot.\""
    j "\"I can't believe this!\""
    mc 1 c smile "\"What I can't believe is that you really thought I was gonna miss this just because it was a little far away. Come on, give me some credit.\""
    show j 1 c blush at fdis
    j "\"But... but I didn't want to bother you.\""
    mc 1 c considerate "\"And that attitude of yours is the only thing that bothers me.\""
    show j 1 c avoid at fdis
    j "\"Did you tell the others too?\""
    mc 1 c think "\"No. While I'm pretty much a bum and have nothing important that needs to be done, they're very much obsessing about their roles in the festival just like you said.\""
    mc 1 c smile "\"I didn't want them to get distracted. Besides, I like being the only one here.\""
    show j 1 c sigh at fdis
    j "\"God, you're a handful...\""
    mc 1 c happy "\"Guilty as charged.\""
    show j 1 c watch at fdis
    yui "\"Hmm... I'm very happy to see you here but I don't know how I feel about deceiving my little Junbug.\""
    show j 1 c shock at fdis
    j "\"M-mom!\""
    mc 1 c laugh "\"Junbug?! Oh my God, that is going on twitter right now!\""
    show j 1 c wince at fdis
    j "\"N-no!\""
    mc 1 c smile "\"Relax, I'm just kidding. There's no way I'd do something like that to you.\""
    show j 1 c sigh at fdis
    j "\"Thank God...\""
    show j 1 c watch at fdis
    mc 1 c smile "\"I'm sorry for lying to you, Ma'am. I just couldn't sit at home knowing Jun was having a competition today. I had to come support him no matter what.\""
    show j 1 c blush at fdis
    j "\"[povFirstName]-san...\""
    "Jun's face goes bright red and he can't even hold my gaze."
    "His mom and dad both smile upon seeing him like this, seeming somewhat happy to see their son looking embarrassed."
    yui "\"You know what, I don't really mind. Thank you for coming over to support him.\""
    ats "\"Yeah, I really appreciate you going out of your way for Jun.\""
    mc 1 c happy "\"It's my pleasure!\""
    show j 1 c sigh at fdis
    j "\"Alright that's nice really great comeonletsgetmeregistered!\""
    show j 1 c sigh at fdis, offscreenright
    show ats 1 n c smile at offscreenright
    show yui 1 c smile at offscreenright
    with move
    "Jun pushes both of them aside and away from me."
    "I know it shouldn't but seeing him so embarrassed and scurrying to get his parents away from me makes me laugh."
    stop music fadeout 2.5
    scene ConcertBackstage
    show j 1 s sigh at fdis, five
    show ats 1 n c smile at two
    show yui 1 c smile at eight
    with fade
    play music2 "music/BGM/Summer Day.ogg" fadein 5.0
    "Unlike last time where we had to see Jun off at the lobby, this time they allowed us to accompany him to the backstage."
    "I suppose since Jun's parents were already supposed to be accompanying him anyway, he felt bad about leaving me alone outside."
    "He got changed as soon as we arrived here and I have to admit he really does look quite dashing in his suit."
    "Of course, I'd never be caught alive saying that."
    mc 1 c worried "\"Are you sure you don't need anything? Maybe I can go fetch you some water or something?\""
    j "\"I already told you I'm fine. [povFirstName]-san, relax.\""
    mc 1 c worried "\"But...\""
    show j 1 s wince at fdis
    j "\"[povFirstName]-san, I already have a lot on my plate here. I can't be babysitting you too.\""
    play sound "music/stab.ogg"
    "H-hey!" with hpunch
    "Both of Jun's parents laugh as they watch our conversation."
    "They both seemed to be satisfied just watching us talk silently."
    "They're probably really amused seeing me get shot down so many times..."
    mc 1 c wince "\"Sorry. I'm just not used to you being so calm. I keep expecting you to flip out at any second like you did last time.\""
    yui "\"That's exactly why we came along. Well... partly because of that. The main reason was because after last time, we just didn't want to risk him skulking out of the house to come without our permission.\""
    show j 1 s considerate at fdis
    j "\"Ahaha... I already said I was sorry. Can we please not talk about this again?\""
    yui "\"Sorry, I'm gonna use that as leverage until the day I die.\""
    show j 1 s wince at fdis
    j "\"Great. I'm gonna get guilt tripped for the rest of my natural-born life.\""
    "The older tigers both chuckle to themselves, no doubt feeling amused and happy at their son's attitude."
    mc 1 c worried "\"How are you so calm? Last time you were a wreck.\""
    show j 1 s think at fdis
    j "\"Well...{nw}"
    show j 1 s smile at fdis
    extend " I still remember the words of encouragement you said to me back then. I repeat them inside my head whenever I get nervous.\""
    mc 1 c shockb "\"Wha...\""
    show j 1 s think at fdis
    j "\"Plus, this is a much smaller venue. My main competition would be Akutagawa-kun and he's not taking part in this competition.\""
    mc 1 c curious "\"He's not?\""
    show j 1 s watch at fdis
    j "\"No. He's already a well established pianist. I did some digging after the last competition and found out he's placed among the top 5 junior pianists in the country. He can get into any school he wants after this. He doesn't need to join small competitions.\""
    show j 1 s smile at fdis
    j "\"Since I'm trying to draw as much positive attention as I can, I have to take part in any competition I can, no matter how small. That's why I even went through the trouble of joining a competition in another town.\""
    mc 1 c worried "\"Huh... You have it rougher than I thought.\""
    show j 1 s think at fdis
    j "\"Hmm... depends on your point of view. If you think about it, I'm just trying to stand out.\""
    show j 1 s watch at fdis
    j "\"That little shtick I did at the last competition actually got me a lot more attention than I thought. Positive one too. If everything goes well here, I might not even need to win as many competitions as I thought.\""
    show j 1 s smile at fdis
    j "\"In the end, I'm just making up for lost time.\""
    mc 1 c curious "\"That's... good?\""
    show j 1 s happy at fdis
    j "\"It is!\""
    "Huh..."
    "I've got to admit, I'm not used to seeing him so calm and... well, calm."
    "It kinda feels like someone slipped some Nyquil into his morning juice box."
    "I'm only used to seeing him either super happy and bouncing around or super freaked out and bouncing around."
    "He's so subdued right now that it's kinda scary."
    "Sure, makes him look a bit more mature, but... still scary."
    show j 1 s watch at fdis
    mc 1 c "\"Did you manage to properly rehearse your setlist?\""
    show j 1 s think at fdis
    j "\"Yeah. I didn't pick anything too difficult for this competition since I knew competition wouldn't be too fierce.\""
    show j 1 s considerate at fdis
    j "\"Come to think of it, maybe I'm being a tad too overconfident here?\""
    mc 1 c smile "\"There's nothing wrong with being confident in yourself. In fact, I'd say it was about time. You have so much skill, it just won't do for you to keep acting like you're some kind of bottom of the barrel beginner.\""
    show j 1 s avoid at fdis
    j "\"Oh come on. I'm not {i}that{/i} bad am I?\""
    mc 1 c curious "\"Can I lie?\""
    show j 1 s sigh at fdis
    j "\"Forget it...\""
    show j 1 s smile at fdis
    ats "\"I'm just glad that someone came over to support Jun. I was really upset when he said he hadn't told any of his friends.\""
    show j 1 s wince at fdis
    j "\"Dad...\""
    ats "\"I know, I know. You didn't want to be a bother, blablabla. I've heard that story about ten times already.\""
    show j 1 s sigh at fdis
    j "\"Then stop giving me a hard time about it.\""
    ats "\"Don't be stupid, kid. Just because I remember it doesn't mean I agree with it.\""
    yui "\"Thank you for going through all this trouble just to support Jun, [povFirstName]-kun.\""
    j "\"Oh my God, will you guys stop? I swear I'll ask security to escort you out of here.\""
    yui "\"Stop being so fussy. We're just talking to your friend.\""
    show j 1 s annoyed at fdis
    j "\"You mean you're embarrassing me in front of my friend.\""
    mc 1 c smile "\"Don't worry. I don't see any reason for you to be embarrassed here. I certainly don't mind.\""
    show j 1 s wince at fdis
    j "\"You and I see things very differently...\""
    mc 1 c smile "\"Like that's not already a given?\""
    show j 1 s avoid at fdis
    j "\"Huh?\""
    mc 1 c happy "\"Nothing.\""
    mc 1 c smile "\"What time is your performance?\""
    show j 1 s watch at fdis
    j "\"It should be soon. About twenty minutes or so I think. I don't quite remember off the top of my head.\""
    yui "\"Do you want us to leave you alone for a bit so you can concentrate?\""
    show j 1 s think at fdis
    j "\"Hmm... I'm not sure.\""
    mc 1 c talk "\"Are you sure you don't need anything?\""
    show j 1 s considerate at fdis
    j "\"[povFirstName]-san, stop fussing over me so much. I'm fine.\""
    mc 1 c wince "\"Alright...\""
    show j 1 s smile at fdis
    j "\"Oh, I just remembered. Could you guys go get my phone? I think I left it in the car. I wanna look something up online before I go out there to perform.\""
    ats "\"Of course. I'll be right back.\""
    yui "\"I'll go with your father to make sure he still remembers where he parked the car.\""
    ats "\"Hey, I'm not that forgetful!\""
    show yui 1 c smile at offscreenright
    show ats 1 n c smile at offscreenright
    with move
    stop music2 fadeout 2.5
    "They both walk out of the room, with Atsushi-san pouting whilst his wife pokes fun at him."
    "God, I hope I have a marriage like that when I'm their age."
    show j 1 s happy at fdis
    j "\"Hehe, that was easier than I thought.\""
    show j 1 s smile at fdis
    mc 1 c curious "\"What was?\""
    show j 1 s gentle at fdis
    "Jun pulls his phone out of his pocket, laughing."
    mc 1 c shock "\"Wha- You have it? Then why did you-\""
    show j 1 s considerate at fdis
    j "\"I wanted some time alone to talk to you but they'd just keep hounding me if I tried to ask.\""
    show j 1 s gentle at fdis
    j "\"Now they'll be looking for it for a while so the coast is clear for a bit.\""
    play music3 "music/BGM/I Want to Know You - Narration.ogg" fadein 5.0
    mc 1 c shockb "\"You wanted time alone with me? Why?\""
    show j 1 s wince at fdis
    j "\"I wanted to properly thank you for going through all this trouble to come over here and cheer for me.\""
    show j 1 s considerate at fdis
    j "\"No matter how much I try to keep myself from being selfish and bothering the people around me, you always find a way to do the things I was too afraid to ask.\""
    mc 1 c smile "\"I knew it. You wanted us to come cheer for you today after all didn't you?\""
    show j 1 s wince at fdis
    j "\"Of course I did... but I also understand everyone's circumstances. I know I can't be selfish and think only about what I want.\""
    show j 1 s considerate at fdis
    j "\"I wanted you guys to come keep me company but I couldn't bring myself to ask since I knew you'd agree even though you're all so busy.\""
    mc 1 c smile "\"Well, you're not getting rid of me that easy. If I can make time to spend with you then I will without complaint. Isn't it obvious by now? I like spending time with you, you dork.\""
    show j 1 s shockb at fdis
    j "\"{cps=5}...{/cps}{nw}"
    show j 1 s happyb at fdis
    extend " Thank you. It means a lot.\""
    j "\"I feel like I can stay calm just by having you here. I'm sure I'd be a little freaked out otherwise, but just having you next to me makes me feel like I'll be okay.\""
    mc 1 c considerate "\"God, that's a really sappy thing to say.\""
    show j 1 s wince at fdis
    j "\"Sorry.\""
    mc 1 c smile "\"You don't have to apologize, dumbass. I appreciate the sentiment and I feel the same.\""
    show j 1 s happyb at fdis
    j "\"Yeah.\""
    show j 1 s happyb at fdis:
        ease .2 zoom 1.5 xoffset -50 yoffset 230
    play sound "music/fabric.ogg"
    "Before I can react, my body is enveloped in a tight hug from this fuzzy ball of orange fur."
    "Smiling, I wrap my own arms around him, making sure to hug him tightly for extra encouragement."
    show j 1 s smile at fdis:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    j "\"I promise I'm going to win today.{nw}"
    show j 1 s happy at fdis
    extend " Maybe I'll even dedicate my performance to you today.\""
    mc 1 c considerate "\"That's a little...\""
    show j 1 s think at fdis
    j "\"Sappy?\""
    mc 1 c "\"You got it.\""
    show j 1 s considerate at fdis
    j "\"Sorry... My head has been swimming in all these sappy thoughts lately. It's hard to think straight sometimes...\""
    mc 1 c smile "\"It's alright. You're an artist. I suppose you're bound to romanticize life a bit.\""
    show j 1 s think at fdis
    j "\"Hmm... I wonder about that...\""
    show j 1 s watch at fdis
    mc 1 c smile "\"Now that your parents are out of ear-shot, be honest with me. How confident do you feel about winning today?\""
    show j 1 s happy at fdis
    j "\"I actually feel really confident.\""
    mc 1 c happy "\"That's great. I'm sure you're going to do amazing today, just like you always do.\""
    j "\"Hehehe. Thanks.\""
    show j 1 s think at fdis
    j "\"I kinda wish the others were here too...\""
    mc 1 c sigh "\"Then you should have invited them too, you dumbass.\""
    show j 1 s considerate at fdis
    j "\"I know that. I wasn't complaining, I was just thinking out loud.\""
    show j 1 s watch at fdis, two
    show ats 1 n c smile at five
    show yui 1 c smile at eight
    with move
    ats "\"Jun, are you sure you left your phone in the car?\""
    "Just then, his parents come back, looking at Jun with worry."
    yui "\"We looked everywhere for it but we just couldn't find it. Oh dear, if you've lost it...\""
    show j 1 s happy at fdis
    j "\"Actually, I found it right after you guys left. Turns out I left it in the pocket of my shorts.\""
    "He picks up the phone from his pocket and dangles it in front of their eyes for effect."
    "I sigh, thinking to myself that there is no way they are going to fall for this."
    "But..."
    yui "\"Oh, was that it? Thank God. I was worried we'd have to buy you a new one. Those phones can be really expensive.\""
    ats "\"Let's just be glad that wasn't the case. That could have been really troublesome.\""
    play sound "music/disappointment.ogg"
    "They both fall for it so quickly and easily that I'm left amazed."
    "Come on guys. You're both adults, you can't be this gullible..."
    "Employee" "\"Jun Kobayashi, you're up next.\""
    show j 1 s shock at fdis
    j "\"Ah. It looks like I have to go prepare myself.\""
    yui "\"Wow that was quicker than I thought. Didn't you say it'd be another twenty minutes?\""
    show j 1 s think at fdis
    j "\"I said I {i}thought{/i} it would be twenty minutes. I wasn't sure.\""
    show j 1 s smile at fdis
    ats "\"At any case, I'm going to go look for some seats for the three of us. Good luck, son. We'll be praying for you.\""
    show j 1 s considerate at fdis
    j "\"Don't be so dramatic, Dad...\""
    ats "\"I'm not being dramatic. If anything happened to you, I-\""
    show j 1 s sigh at fdis
    j "\"Dad...\""
    "Jun cuts him off with a stern voice. The tiger swallows his words, hesitating for a few seconds before smiling once again."
    ats "\"Well, not important. Any way, good luck. Your mom and I will be watching you from the crowd.\""
    show j 1 s smile at fdis
    j "\"I'm sure you will.\""
    yui "\"Good luck, love.\""
    j "\"Thanks.\""
    "He hugs the two of them as they continue to wish him good luck over and over again."
    "After he's done with his parents, he turns to look at me."
    show j 1 s happy at fdis
    j "\"If I win, you better treat me to a good meal.\""
    "!"
    "He's never asked me to treat him to anything before."
    "For some reason, hearing that brings a big smile to my face."
    mc 1 c happy "\"Alright. If you win, you can choose a restaurant and I'll take you there.\""
    show j 1 s think at fdis
    j "\"No, not a restaurant. I want you to cook for me.\""
    mc 1 c shock "\"Me? I don't think I could cook on par with a restaurant.\""
    show j 1 s gentle at fdis
    j "\"Shoichi-san said you're a really good cook.{nw}"
    show j 1 s smile at fdis
    extend " If I win, I wanna see if that's true.\""
    mc 1 c smile "\"Alright. Whatever you want. Just make sure you do win.\""
    show j 1 s happy at fdis
    j "\"Of course!\""
    stop music3 fadeout 2.5
    scene ConcertHall
    show yui 1 c smile at three
    show ats 1 n c smile at seven
    with fade
    "It takes us a couple of minutes to walk to the hall and find some seats."
    "While the place isn't nearly as full as the other concert hall where Jun had his first competition, there's still quite a bit of people inside."
    "In the back of my head, I keep worrying that he will choke and break down."
    "I silently chastise myself for thinking like this."
    "I have no right to doubt him when he's as confident in himself as he was."
    "I'll just cheer for him and I'll be there to congratulate him once he's won."
    "That is all I need to do right now."
    "We watch Jun walk onto the stage."
    "He walks with firm steps and a straight back, bowing to the audience before reaching the piano."
    "As soon as he sits at the piano, I see him reach for his pocket."
    "It seems like he pulled something out, but it's so small that I can't see."
    "Whatever that thing is, he holds it against his chest for a few seconds, his eyes closed."
    "Right now, everyone in this hall has their eyes on Jun."
    "I just know he'll put on a performance that will charm the entire audience."
    "Just like he charms me more and more every time he plays."
    play music2 "music/BGM/Classical/Etude Op10 N11.ogg" fadein 2.5
    "Once he's finished his preparations, Jun reaches for the piano."
    "His entire body begins to rock from side to side as his fingers dance across the keys."
    "A beautiful melody echoes from the piano, enrapturing everyone in the audience."
    "As soon as he begins to play, any and all whispers are forcibly silenced."
    "Even if this song doesn't sound as difficult as the other pieces I've heard him perform, it captures my heart nonetheless."
    "In this warm and dry room, I can see the lone tiger atop that stage, the lights all shining on him."
    "I see particles of dust floating across the air and around his body that looks so small all the way from up here."
    "To me it seems like even the air around him is dancing gracefully to the sound of his piano."
    "Jun's piano is gentle, captivating and beautiful. Even more so than usual."
    "I feel like all the confidence he had is being transfered into the song."
    "He's boldly advancing and carving a path for himself, earning the admiration and the hearts of each and every member of the audience."
    "I don't think even the judges will be able of resisting his charm today."
    "My feet tap restlessly as I resist the urge to get up from my seat and try to get closer."
    "This seems to be a recurring feeling whenever I watch him perform."
    "I want to get closer. I want to feel his melody echoing inside my chest."
    "For a moment, I feel as if a thousand butterflies are flying around in my stomach."
    "I hear the last notes being played with a held breath, my heart beating faster and faster to the sound of the music."
    "My mind has gone completely blank and I feel as if I were floating around in the air."
    "Ah... this is bad."
    "I feel like I'm getting completely taken in by this tiger..."
    stop music2 fadeout 2.5
    play music "music/crowd01.ogg"
    scene ConcertLobby
    show j 1 c watch at fdis, five
    show yui 1 c smile at three
    show ats 1 n c smile at seven
    with fade
    "Once every single one of the contestants finished presenting, Jun got changed and we left back to the lobby."
    "I have to admit, I much prefer being in this open, well ventilated lobby over that crowded waiting area."
    "That place felt like an oven."
    mc 1 c smile "\"How are you feeling about your chances, Jun-kun?\""
    j 1 c smile "\"I feel pretty good about them. I feel like I did really well. And besides, I played my best, that's all that really matters.\""
    ats "\"You can't be satisfied with just that. You have to reach for the stars, kid!\""
    j 1 c think "\"But there's no oxygen in space, is there? Wouldn't I suffocate if I tried.\""
    "Atsushi-san's face immediately warps to one of confusion."
    ats "\"That... that's not-\""
    j 1 c shock "\"Plus, how would I even get to space? Don't rockets cost a fortune? Oh, could it be you're gonna give me a spaceship for my birthday?!\""
    ats "\"...\""
    "Atsushi-san stares at his son in dismay."
    "Yui-san chuckles, looking between the two of them with a big smile on his face."
    yui "\"In case you haven't noticed, he's mocking you, dear.\""
    ats "\"Of course I can notice it! I'm just asking myself where the hell he got the habit of being like this.\""
    j 1 c happy "\"Hehehe, it's a secret.\""
    show j 1 c watch at fdis
    "Just then, we notice a commotion forming around the notice boards in the lobby."
    j 1 c shock "\"Ah. Maybe they're posting the results already. Let's go look!\""
    show j 1 c watch at fdis
    "The four of us push through a small crowd so we can finally reach the boards."
    "Surely enough, we see the results have just been posted there."
    "I scan the pieces of paper looking for the results and."
    mc 1 c smile "\"Hehehe... you won, Jun. And with a perfect score even!\""
    j 1 c shock "\"Wow. I can't believe I got a perfect score!\""
    "Atsushi-san begins tousling Jun's fur, laughing."
    ats "\"Now that's my boy. You really are amazing!\""
    j 1 c happyb "\"Hehehe.\""
    yui "\"We should think of a way to celebrate! How about we go to a restaurant?\""
    ats "\"Ooh, I like that idea!\""
    j 1 c considerate "\"Erm... I kinda already have plans to celebrate.\""
    yui "\"Oh?\""
    "They both stare at him in surprise, silently urging him to say more."
    j 1 c smile "\"[povFirstName]-san still has to make good on his promise to me after all!\""
    mc 1 c considerate "\"Seriously? I'm pretty sure dinner at a restaurant would be a much better celebration than me cooking for you.\""
    j 1 c happyb "\"Nope! I know what I want and I want that.\""
    "The two older tigers look at each other, smiling widely."
    yui "\"Alright then. As long as you have fun then we have no problems with that.\""
    ats "\"Come on, we need to drive home. And you're coming with us too, [povFirstName]-kun.\""
    mc 1 c laugh "\"Yes, sir.\""
    stop music fadeout 2.5
    scene KitchenN
    show j 1 c happy at fdis, seven
    show a 1 c smile at fdis, three
    with fade
    play music "music/night.ogg" fadein 5.0
    play sound "music/grill.ogg"
    "I make an effort to try to pay attention to the conversation at hand without burning the food that I'm preparing."
    a "\"And what was it like performing in front of that huge crowd?\""
    j "\"It was really fun. I just felt really confident and ended up enjoying myself a ton this time around!\""
    "Jun and my little brother are engrossed in conversation as the tiger relates the events of the day to Aki."
    "As soon as we got home, Aki and Jun began chatting up."
    "Aki was really excited when he heard about the results of the competition."
    "For some reason, these two seem to get along astoundingly well."
    "I want to make a joke about them both having the same mental age but Jun would probably get mad if I did."
    play music2 "music/BGM/Snowy Day.ogg" fadein 5.0
    mc 1 c talk "\"Jun, how do you want your steak?\""
    show j 1 c smile at fdis
    j "\"Oh. Medium well for me, please.\""
    mc 1 c smile "\"Gotcha. What about you, Aki?\""
    a "\"Yeah, I'll have the same.\""
    mc 1 c happy "\"Okay.\""
    "I don't know why Jun was so excited to have me cook for him but in the end what he asked me to prepare wasn't even that special."
    "Just some grilled steak with rice, steamed vegetables and a side of miso."
    "I swear, he's either really easy to please or he's still not comfortable asking for much."
    "Although he did ask me to cook for him point-blank."
    mc 1 c "\"Bring your plates over here. It's almost done.\""
    j "\"Okay.\""
    "The two had been hanging around by the kitchen island, just side-eying me and the food so they could swoop in like a couple of hungry hawks as soon as it was finished."
    "They tried to act sly about it but it was just too darn obvious."
    mc 1 c smile "\"I know you didn't ask for it but I also prepared some western style gravy for you to pour on top of the meat if you want.\""
    show j 1 c happy at fdis
    j "\"That sounds lovely, thank you!\""
    a 1 c "\"Did you remember to save some for Mom?\""
    mc 1 c smile "\"Of course I did. By the way, do you know when she'll be back?\""
    "Aki shrugs, preparing his plate without even bothering to look my way."
    a "\"She said something about a late deadline and spending the night in the office... or at someone's place. I didn't really pay attention.\""
    mc 1 c sigh "\"You have to stop being so lazy around the house. You should at least pay attention when people talk to you.\""
    a 1 c sigh "\"... I was doing my homework.\""
    mc 1 c shock "\"Wha- On a Sunday?\""
    a 1 c "\"Just because we don't have class doesn't mean I get to stop studying...\""
    show j 1 c think at fdis
    j "\"[povFirstName]-san, I think you're forgetting that you're talking to Akiyoshi-kun here, not yourself.\""
    show j 1 c happy at fdis
    mc 1 c sigh "\"Very funny.\""
    show j 1 c watch at fdis
    mc 1 c talk "\"By the way, Aki, how are you doing with your studies?\""
    a "\"I'm doing okay. Oh, but the cram school I go to is having a parent/teacher conference next week and Mom said she was too busy to go. I was wondering if you could go in her place.\""
    j "\"Can [povFirstName]-san even do that?\""
    mc 1 c "\"As long as I'm over sixteen and have a signed document from our Mom explaining that I'm going in her place then yeah. I've been doing this for Aki for a while now.\""
    a "\"Yeah, Mom is really busy most of the time. She's almost never out of work.\""
    mc 1 c considerate "\"Actually, she's kinda working even when she's home.\""
    a 1 c sigh2 "\"She's probably gonna die from a heart attack before she turns fifty if she keeps this up.\""
    mc 1 c sigh "\"Aki, that's a horrible thing to say!\""
    show a 1 c at fdis
    "The little twerp shrugs at me, stabbing his steak and cutting it up with a knife."
    a "\"That's what happens to people that overwork themselves. This steak is really good by the way.\""
    "I really wish he wouldn't say such morbid things so casually..."
    show j 1 c shockb at fdis
    j "\"Wow. This really is delicious.\""
    mc 1 c "\"It's just a steak, it's nothing special.\""
    show j 1 c happyb at fdis
    j "\"I really like it though. I've been wanting to eat your homemade food for a while now, [povFirstName]-san. I'm happy I finally managed to.\""
    mc 1 c smile "\"God, you're so easily pleased.\""
    j "\"No I'm not. It just so happens that the things you need to do to please me are easy for you.\""
    mc 1 c considerate "\"Sure. If you say so.\""
    show j 1 c smile at fdis
    j "\"Still, this is really delicious. You've {i}got{/i} to cook for me more often.\""
    mc 1 c smile "\"I wouldn't mind. Just drop by for dinner every now and again. In exchange, I want to eat some of your food too. You've been bringing a lot of delicious looking stuff to school and I want myself some of that.\""
    show j 1 c happy at fdis
    j "\"It's a deal!"
    show j 1 c smile at fdis
    extend " Man, I wish I could eat your food every day.\""
    show j 1 c shockb at fdis
    a "\"Is this how grownups flirt? Doesn't sound very romantic to me.\""
    j "\"W-what?!\""
    mc 1 c shock "\"Aki!\""
    a "\"What? Did I say something wrong?\""
    show j 1 c blush2 at fdis
    mc 1 c sigh "\"Of course you did. Why would you say something like that in the first place?\""
    a "\"Aren't you guys dating?\""
    mc 1 c shockb "\"{size=+2}What?!{/size}\""
    "Aki stops chewing, staring at the two of us with a raised eyebrow."
    "I can't really get a reading on what he's thinking sometimes and it really bugs me."
    a 1 c avoid "\"Oh. I thought... you know, after you went through all that trouble to surprise him today and how close to each other you're being. Was I wrong?\""
    mc 1 c sigh "\"Of course you were wrong! I mean- Come on, look at what you're even suggesting. We're both guys!\""
    "He nods, cracking a half-smile as he looks me up and down."
    a 1 c "\"Yeah, I can see that. We're not in 1945 anymore though. Two guys can date each other. It's normal.\""
    "He shrugs, as if that were his way of saying \"and that's that\"."
    mc 1 c sigh "\"Where are you even getting this?\""
    a 1 c smile "\"TV. And the internet.\""
    mc 1 c sigh2 "\"I have got to install parental control on your phone.\""
    a 1 c "\"Won't do you any good. I'm better at using this stuff than you are. It wouldn't take me five minutes to crack it.\""
    mc 1 c sigh2 "\"Just stop saying weird stuff and we'll be fine.\""
    a 1 c sigh "\"Weird stuff, huh?\""
    "He shoots the two of us another suspicious look before sighing."
    a "\"{size=-4}God, you're both so clueless...{/size}\""
    mc 1 c confused "\"What? I didn't hear you.\""
    a 1 c "\"Nothing. Anyway, I'm gonna go eat in my room, I still have to finish doing my homework. You two have fun.\""
    mc 1 c "\"Sure. Make sure to bring your plate down so I can wash it once you're done.\""
    a "\"Don't be stupid. I'll wash it myself later.\""
    show a 1 c at fdis, five with move
    show j 1 c shock at fdis
    "Aki walks up to Jun, whispering something in the tiger's ears."
    show j 1 c blush at fdis
    "Jun's eyes shoot wide for a second before he covers his mouth with his hands and looks away from the two of us, his face red."
    mc 1 c sigh "\"Aki, what did you just say to him?\""
    a 1 c smile "\"Nothing. Anyway, I'll talk to you later. Homework calls.\""
    show j 1 c blush2 at fdis, five
    show a 1 c smile at fdis, offscreenright
    with move
    "He quickly runs up the stairs, carrying his plate with him."
    mc 1 c sigh2 "\"Aki, don't run on the stairs when you're carrying a knife!\""
    a 1 c "\"Sure!\""
    "That little twerp..."
    mc 1 c "\"Are you alright? Your face is as red as a tomato. And that's saying something when I can see you blush through your fur.\""
    j "\"It's nothing...\""
    show j 1 c considerate at fdis
    j "\"But man, this food is really delicious. What's your secret?\""
    scene SkyN with fade
    "Jun and I chat about the foods we like to prepare for a bit before he has to leave for the night."
    "Despite my insistence that I walk him home, he has me see him off at the door and we wish each other a good night."
    "I wonder what was that thing Aki whispered to him before he went back upstairs..."
    stop music2 fadeout 2.5
    stop music3 fadeout 2.5
    stop music fadeout 2.5
    $ date = None
    $ schoolfestival = "jun"
    jump SchoolFestival
