label keisukestart_4:
    $ uihide = True
    stop music2 fadeout 2.5
    $ keisukehearts += 1
    scene SCorridor
    show k 1 u avoid at fdis, five
    with fade
    "Kei-kun and I stand outside of a room, staring tentatively at the door."
    "I'm waiting for any indication of opening the door on his part."
    "And he..."
    "...{w} Well, truth be told, I have no idea what he's waiting for."
    "Kei-kun called me this morning and asked me if I wanted to meet his bandmates."
    "I immediately agreed, which I guess he wasn't expecting since he sounded so shocked on the phone."
    "I guess part of him still hoped I'd say no."
    mc 1 u curious "\"...\""
    k "\"...\""
    mc 1 u curious "\"...\""
    k "\"...\""
    mc 1 u curious "\"Are we... are we waiting for something?\""
    k "\"Yeah... waiting for the world to end so I don't have to go through the circus that's going to ensue when I introduce you to them.\""
    mc 1 u fsmile "\"W-wha? Come on, I'm not that bad!\""
    k "\"It's not you I'm worried about...\""
    mc 1 u shock "\"Huh?\""
    show k 1 u sigh at fdis
    k "\"Never mind...\""
    show k 1 u avoid at fdis, eight with move
    k "\"Come on, I'll introduce you to them... Try not to be too weirded out.\""
    play sound "music/slidingdoor.ogg"
    play music2 "music/BGM/Feelin Good.ogg" fadein 5.0
    scene SBand
    show k 1 u avoid at fdis, five
    with fade
    k "\"Good afternoon.\""
    "I step into the room following Keisuke, scanning the insides with great curiosity."
    mc 1 u curious "\"Whoa. So this is what a band room looks like?\""
    "There are so many instruments in here, many of which I don't even recognize."
    "I also notice the walls have a weird look to them, as if they were made of a different material than the rest."
    "And there's a... booth?"
    "Some kind of door leading to a booth on the other side."
    show k 1 u at three with move
    show i 1 u smile at seven with moveiridis
    i "\"Welcome back, Kei-chan!\""
    show k 1 u sigh at fdis
    k "\"Ichigo-san, I've already asked you to stop calling me that.\""
    "Ichigo? That fussy Keisuke is already calling her on a first name basis?"
    "Is there something going on in here?"
    i "\"And good afternoon to you, [povLastName]-kun.\""
    "Before me stands a beautiful girl, a calico cat with silky fur dressed in a white shirt with her school blazer tied around her waist."
    mc 1 u "\"Hey there, Minazuki.\""
    show k 1 u at fdis
    k "\"You two know each other?\""
    "Before I can respond, Ichigo wraps her arms around mine and leans dangerously close to my body, smiling lecherously."
    mc 1 u shockb "\"H-huh?!\""
    i "\"Oh, didn't you know? [povLastName]-kun and I used to be L. O. V. E. R. S.\""
    show k 1 u shock at fdis
    k "\"W-wha-\""
    "?" "\"{size=+4}What?!{/size}\""
    "Another voice echoes loudly inside the room."
    show k 1 u shock at fdis, two
    show i 1 u smile at five
    with move
    show ku 1 u smile at eight with moveiridis
    "A guy runs up to me, a literal monkey with brown fur. His eyes are completely wide as he grabs my collar."
    mc 1 u wince "\"Gah!\""
    "?" "\"Y-y-y-you used to date Ichigo-san?\""
    mc 1 u wince "\"C-can't... breathe...\""
    "He's shaking me so much that I start to get nauseous."
    "?" "\"Kurusu, stop monkeying around.\""
    show k 1 u sigh at fdis, one
    show i 1 u smile at three
    show ku 1 u smile at five
    with move
    show ka 1 u smile at nine with moveiridis
    "Another male voice echoes from behind the monkey. A jet black figure looms behind him, grabbing the guy by his shoulder and dragging him away from me."
    ku "\"B-but, Kagaho-san, he used to date Ichigo-san!\""
    "The other guy, a raven, sighs, rubbing his temple as he stares down the monkey."
    "The casual reactions of Keisuke and Minazuki tells me that this is a common occurrence."
    ka "\"No he didn't. Can't you tell that she was joking?\""
    ku "\"Huh?!\""
    "His eyes go even wider, which I didn't even think was possible."
    "He keeps staring between me and Minazuki in disbelief."
    mc 1 u sigh "\"Minazuki and I were classmates as freshmen. We got paired up for class projects a few times. Minazuki, please clear up this crazy misunderstanding you created...\""
    ku "\"O-oh. I-I'm sorry, I shouldn't have reacted like that!\""
    "He bows profusely, his body stiff as a plank."
    i "\"Don't worry about it too much, Kurusu-kun. It was just a joke.\""
    play sound "music/disappointment.ogg"
    "No, you should worry about it. That joke nearly had me thrown to the floor..."
    "?" "\"I see that Kurusu is already causing trouble for our guest.\""
    show ka 1 u smile at seven with move
    show mi 1 u smile at nine
    show sh 1 u at ten
    with moveiridis
    "Two girls walk in from the separate booth on the other end of the room, a raccoon and a coyote."
    show k 1 u avoid at fdis
    k "\"Everyone's already here, huh?\""
    "?" "\"Yeah. You were late after all.\""
    show k 1 u sigh at fdis
    k "\"Still... I didn't expect Kurusu-san to get here before I did...\""
    ku "\"What's that supposed to mean?\""
    show k 1 u at fdis
    k "\"Exactly what I said.\""
    "Is this tension that I feel?"
    show k 1 u calm at fdis
    k "\"Well, not that it matters anyway.\""
    show k 1 u smile at fdis
    stop music2 fadeout 2.5
    play music3 "music/BGM/Spring Classroom.ogg" fadein 5.0
    k "\"[povFirstName]-san, these are the members of the Light Music club. We have Ichigo Minazuki as the vocalist.\""
    i "\"Hiya!\""
    "She waves at me with a happy smile on her face."
    k "\"Kurusu Sajiuma is the guitarist.\""
    ku "\"It's nice to meet ya!\""
    "The monkey strikes an energetic pose, puffing his chest."
    k "\"Kagaho Fujioka is the bassist... and unofficial leader of the band.\""
    "Kagaho, the raven, crosses his arms, looking at Keisuke with annoyance."
    ka "\"I don't remember ever agreeing to something like that.\""
    i "\"Hence why he said unofficial!\""
    show k 1 u eyesc at fdis
    k "\"We also have Miyu Ishikawa and Shoko Hisokawa as the drummer and keyboardist respectively.\""
    mi "\"Nice to meet you, Senpai!\""
    "The raccoon smiles politely at me, absent-mindedly playing with a drumstick and flipping it between her fingers."
    sh "\"Hi.\""
    "The coyote crosses her arms, looking away from me, barely speaking a word."
    mi "\"Hey, Shoko-chan, you shouldn't be so dry with someone you just met. At least greet him properly.\""
    ka "\"Miyu, don't forget that you yourself weren't even looking at him.\""
    mi "\"Kuh... busted, huh?\""
    "This is... an interesting group."
    mc 1 u smile "\"It's nice to meet you all. I'm Keisuke's friend, [povName].\""
    i "\"Well, some of us already knew you from before so I guess me introducing myself is kinda pointless.\""
    ka "\"Some of us also know about you, even if we've never met you before. After all, you are an incredibly popular person in this school.\""
    mc 1 u considerate "\"That... might be true.\""
    mi "\"It's not like any of us care about sports anyway. We're here for the music.\""
    show k 1 u avoid at fdis
    k "\"Miyu-san, that's a bit...\""
    ku "\"Some of us do care about sports!\""
    "The monkey, Kurusu, flails his arms, looking very annoyed."
    show k 1 u sigh at fdis
    k "\"Kurusu-san, you're overreacting...\""
    ka "\"Again.\""
    "Kurusu pouts, glaring at the two guys."
    ku "\"You all pick on me way too much.\""
    ka "\"You make it easy.\""
    "Uhm..."
    "I'm not really sure how I should be acting here..."
    "I know I wanted to be introduced to them but I have no idea how to react to this group dynamic..."
    mc 1 u considerate "\"Uhm... what's going on here?\""
    show k 1 u avoid at fdis
    k "\"This is more or less the daily interactions that can be had in this group. Thrilling isn't it?\""
    ka "\"It's not like we like it either. It's mostly Kurusu's fault either way.\""
    ku "\"What? How is it my fault?!\""
    mi "\"It is your fault.\""
    sh "\"Agreed.\""
    i "\"It's totally your fault.\""
    k "\"No arguments here.\""
    ku "\"Whaaat? Now you're all turning on me?!\""
    "Oh man, this group is even more dysfunctional than mine..."
    mc 1 u considerate "\"I... I'm sorry?\""
    i "\"What are you apologizing for?\""
    mc 1 u worried "\"I don't know. I just felt like I should...\""
    show k 1 u sigh at fdis
    k "\"You've been here for less than five minutes and you're already overwhelmed?\""
    mc 1 u considerate "\"A little.\""
    ka "\"I apologize on behalf of our... wilder member.\""
    ku "\"Don't apologize on my behalf!\""
    "Definitely an interesting group..."
    show k 1 u at fdis
    k "\"Well, [povFirstName]-san, these are the members of the band. Since you wanted to meet them so bad, is there anything you'd like to ask them?\""
    i "\"Oh, what's this, a Q&A? This will be great practice for when we get famous!\""
    ku "\"Hell yeah, give me the spotlight!\""
    ka "\"Nobody is going to give you the spotlight.\""
    ku "\"But I'm the lead guitarist!\"" with hpunch
    mi "\"You're also a pain in the ass to deal with.\""
    ku "\"Kuh...\""
    mc 1 u think "\"Err... okay, putting that aside...\""
    mc 1 u happy "\"Oh, I know! Does your band have a name?\""
    show k 1 u sigh at fdis
    k "\"{size=-2}That's the best you could come up with?{/size}\""
    i "\"Now, Kei-chan, that's not a bad question at all. You don't need to be so harsh on him.\""
    show k 1 u avoid at fdis
    k "\"Fine... {size=-2}Also, don't call me Kei-chan.{/size}\""
    ka "\"Our band is called \'Strawberry Five\'.\""
    mc 1 u fsmile "\"S-Strawberry Five? Is there any particular reason for that name?\""
    ka "\"Isn't it obvious?\""
    "The raven turns to look at their vocalist, who stares between the two of us with an innocent smile on her face."
    i "\"Before you even think it, no, this name wasn't my idea.\""
    mi "\"Here here, the name was totally my idea!\""
    "The raccoon waves excitedly with a big smile on her face."
    ku "\"Yeah. Up until Miyu joined this year we didn't really have a name... Although I think I preferred when we didn't.\""
    sh "\"You were outvoted. Stop complaining.\""
    "Even the coyote, whom I completely forgot was there, cut in to say something."
    ku "\"Guh... even Shoko-chan is laying in on me now...\""
    mc 1 u curious "\"You guys had a vote?\""
    "The raven nods."
    ka "\"It was about two weeks before Keisuke joined. There were three in favor of the name and two against.\""
    mc 1 u curious "\"Two against? So you were against it, Kagaho-san?\""
    ka "\"No. Ichigo was.\""
    mc 1 u fsmile "\"Huh?\""
    "I turn to look at the cat."
    "She looks at me with a pout on her face, crossing her arms."
    i "\"Why would you think I'd want my name plastered on the band? I'm not that vain.\""
    show k 1 u smile at fdis
    k "\"I have to admit that I do like the name though.\""
    i "\"Not you too, Kei-chan...\""
    "She sighs, shrugging and shaking her head sideways."
    i "\"Well, we did lose the vote so there's no point dwelling on it any further. Do you have anything else you'd like to know?\""
    mc 1 u think "\"Hmm... How many gigs have you guys played so far?\""
    show k 1 u at fdis
    k "\"None.\""
    mc 1 u shock "\"N-none?\""
    i "\"Up until Miyu joined we didn't really have a drummer so we couldn't perform. Plus...\""
    mc 1 u curious "\"Plus?\""
    mi "\"Ichigo-san isn't happy with the current roster. She wanted us to have another vocalist.\""
    mc 1 u curious "\"Double vocals?\""
    i "\"Yeah. I just don't think a girl with a voice like mine can sing all the songs I'd want our band to do.\""
    ku "\"But your voice is incredible, Ichigo-san!\""
    i "\"I'm not saying I think I'm bad. I just don't think I'm a perfect fit for the genre. Plus, I think having a male singer together with me could open so many doors for us.\""
    mc 1 u suggestive "\"A male singer huh?\""
    show k 1 u shock at fdis
    "Keisuke immediately notices the look on my face."
    mc 1 u suggestive "\"In that case, why don't y-\""
    play sound "music/punch.ogg"
    show k 1 u annoyed at fdis
    "I feel a hard kick on my shin."
    mc 1 u dismay "\"Ow!\"" with hpunch
    "The band members all stare at me in shock... with exception to the cat and the raven who seem completely unaffected by it."
    k "\"Oops. Sorry, I slipped.\""
    mc 1 u wince "\"K-Keisuke, please be a little more gentle with me...\""
    show k 1 u avoid at fdis
    k "\"I make no promises.\""
    "Jeez, I'm just trying to help you..."
    i "\"If you're suggesting we have Kei-chan as another singer, I wholeheartedly agree with you.\""
    show k 1 u shock at fdis
    "Band Members" "\"Huh?!\"" with hpunch
    "Even Kagaho reacted this time."
    k "\"W-what? M-me as a singer? What are you talking about?\""
    mi "\"Y-yeah, Ichigo-san, you can't just decide that out of nowhere. We asked Keisuke-san if he could play an instrument or sing when he first joined and he said no.\""
    ku "\"That's not even the only problem here. I've been practicing for the past two years to become the secondary singer with Ichigo-san, you can't just have someone else take my place!\""
    ka "\"Don't be ridiculous, we already told you your voice sucks. We're not having you as a singer, plain and simple.\""
    play sound "music/stab.ogg"
    ku "\"Guh...\""
    sh "\"Ichigo-chan... can you explain?\""
    show k 1 u worried at fdis
    k "\"I'd like to hear an explanation as well. Where did that idea even come from? Don't let [povFirstName]-san's joking around confuse you, I can't-\""
    i "\"I know you can sing.\""
    show k 1 u shock at fdis
    k "\"Huh?\""
    "She mutters something like that as if it were nothing."
    show k 1 u uncomfortable at fdis
    k "\"I-I don't know what you're talking about, I'm a horrible si-\""
    i "\"I heard you on the rooftop a while ago.\""
    show k 1 u shock at fdis, jumping
    k "\"Huh?\""
    mc 1 u shock "\"On the rooftop?\""
    "Could it have been on the same day that I walked in on him singing?"
    "I can't imagine him having done it more than once."
    "Ichigo nods."
    i "\"Yeah. I was thinking of going upstairs to the rooftop to skip class that day and I heard someone singing. I didn't know who it was at first but I heard him muttering to himself every now and then.\""
    i "\"Talking about how he got the lyrics wrong or how the note should have been higher. That's when I recognized that it was Kei-chan.\""
    show k 1 u worried at fdis
    k "\"W-what? Y-you heard that?\""
    "She nods again."
    i "\"You're a very good singer. I've been wanting to get you to become our lead singer since I heard you on the roof. I was actually going to bring it up today but your friend brought the subject up for me.\""
    mc 1 u considerate "\"I... uhm... I'm sorry?\""
    show k 1 u sigh at fdis
    k "\"Stop apologizing.\""
    mc 1 u considerate "\"Sorry...\""
    show k 1 u avoid at fdis
    ka "\"Keisuke, is it true that you can sing?\""
    k "\"...\""
    ka "\"... Keisuke?\""
    k "\"...\""
    "He's gone completely silent..."
    mc 1 u "\"Yeah. Kei-kun can sing and play guitar really well!\""
    show k 1 u shock at fdis, jumping
    k "\"[povFirstName]-san!\""
    ku "\"W-wait, he can play the guitar too?!\""
    mi "\"Great! That means we can finally kick Kurusu out and have a normal guitarist!\""
    ku "\"W-what?!\""
    sh "\"Agreed...\""
    "Wow, these people are merciless."
    i "\"You can play the guitar too? I didn't know that.\""
    show k 1 u worried at fdis
    k "\"I... I mean... it's not like... it's not like I'm {i}good{/i} or anything. It's just... it's just a hobby...\""
    ka "\"Yes. Because the rest of us play professionally, don't we?\""
    show k 1 u wince at fdis, shake1
    k "\"I-I'm sorry, I didn't mean-\""
    ka "\"It's fine. I just don't like the fact that I was lied to.\""
    show k 1 u worried at fdis
    k "\"I...\""
    i "\"Kei-chan, could you show the rest of us? Both your singing and your guitar?\""
    show k 1 u wince at fdis
    k "\"T-that's a bit...\""
    ka "\"We're not gonna bite or anything you know. From the very beginning we said this club was open to anyone who was willing to learn an instrument, so long as they actually put in the effort.\""
    ka "\"Even if it turned out that you're not all that good, we'd just help you practice.\""
    sh "\"It's true. I had never touched a keyboard before until I joined this club.\""
    show k 1 u worried at fdis
    k "\"I... I need some time to think about it.\""
    mc 1 u happy "\"Come on, what's the worst that can happ-\""
    show k 1 u annoyed at fdis
    k "\"Not another word from you, blabbermouth!\""
    mc 1 u dismay "\"S-sorry!\""
    show k 1 u avoid at fdis
    i "\"Come on, Kei-chan, don't be so upset at him. It's not like he said something horrible about you.\""
    mc 1 u pout "\"Yeah. You joined this club because you wanted to sing, didn't you?\""
    show k 1 u worried at fdis
    i "\"You did?!\""
    k "\"There you go running your mouth again. This is why I didn't want to bring you in the first place...\""
    mc 1 u considerate "\"Hehehe... sorry.\""
    "I have to learn to keep my mouth shut sometimes."
    "... Even if Kei-kun's reactions are funny as hell."
    show k 1 u sigh at fdis
    k "\"I... [povFirstName]-san and some of my friends had heard me singing before and seemed very supportive of it so I decided to give it a try.\""
    show k 1 u avoid at fdis
    k "\"But when I saw how good all of you were, I chickened out because I didn't think there was any way I could compare.\""
    i "\"Is that so? I thought you were a better singer than me. That's why I wanted you to be the lead vocal.\""
    show k 1 u sigh at fdis
    k "\"With all due respect, Ichigo-san, I can't see that h-\""
    ka "\"I can.\""
    show k 1 u shock at fdis
    ku "\"You're... you're kidding, right?\""
    "Everyone but Ichigo and I stares at the raven with shock and confusion."
    "The dude, on the other hand, seems completely unaffected by it."
    ka "\"I joined this band because I believed Ichigo was something special and I decided to support her no matter what she did. If she thinks her becoming backing vocal to someone else is the best decision then I choose to trust her.\""
    show k 1 u worried at fdis
    k "\"That's insane...\""
    i "\"Hehe, don't underestimate us founding members. We know what we're talking about. Kagaho and I have created this band from the ground up ourselves. Who do you think scouted all of our other talented members?\""
    k "\"I... don't know?\""
    ku "\"... I was just a member of the Judo club until Ichigo-san saw me playing around with an acoustic guitar last year and invited me to join the band...\""
    mi "\"Ichigo-san is the one who got me to transfer to this school after she saw me practicing the drums by myself at a rehearsal studio.\""
    sh "\"She was the one who said the keyboard would be a good fit for me when I mentioned wanting to join the band...\""
    k "\"W-wow... I didn't know any of that.\""
    ka "\"Ichigo is a good judge of talent and character. She's the only reason this band got together in the first place.\""
    i "\"Hehehe, stop it you guys. You're going to make me blush~\""
    "At least she's modest..."
    show k 1 u avoid at fdis
    k "\"Can I have some time to think about it?\""
    i "\"Of course. I don't want to pressure you.\""
    show k 1 u sigh at fdis
    k "\"That's funny. Because that's exactly what you're doing.\""
    i "\"Don't mind it!\""
    show k 1 u avoid at fdis
    k "\"Yeah, right...\""
    ka "\"I have to admit, I'm also interested in hearing this. I've never seen Ichigo praise another vocalist like this.\""
    show k 1 u wince at fdis
    k "\"I'm nothing special. I promise you that.\""
    ka "\"Somehow I don't buy it.\""
    show k 1 u sigh at fdis
    k "\"Yeah yeah. Believe whatever you want to believe...\""
    "Jeez, he doesn't have to act like it's the end of the world."
    "This {i}is{/i} the reason you even joined this club in the first place."
    mc 1 u smile "\"Come on, Kei-kun. I'm sure you can wow all of them. You're amazing after all!\""
    show k 1 u avoid at fdis
    k "\"You've never seen them perform before. Don't say such ridiculous things without knowing what they're capable of.\""
    mc 1 u considerate "\"Sorry...\""
    k "\"You sure are apologizing a lot today.\""
    mc 1 u considerate "\"I guess...\""
    play sound "music/fabric.ogg"
    mc 1 u shock "\"Huh?\""
    ku "\"Ichigo-san?!\""
    "Ichigo launches herself at me, wrapping both of her arms around my right arm and looking up at me with a devious smile."
    i "\"Well, we can certainly fix that.\""
    ka "\"Are you suggesting what I think you're suggesting?\""
    "I look at the raven to see him smiling knowingly at the two of us."
    i "\"You bet!\""
    "Kagaho nods, turning his back to us and walking towards the instruments at the center of the room."
    ka "\"Everyone in positions. We're going to play now.\""
    ku "\"Oooh, are we gonna show him what we can do?\""
    mi "\"Well, it's not like we weren't going to rehearse today anyway. Having one more person in here isn't going to make much of a difference.\""
    sh "\"I agree...\""
    scene SGateE with fade
    stop music2 fadeout 2.5
    stop music3 fadeout 2.5
    "..."
    "My ears are ringing so much..."
    "I mostly blanked out while they were playing."
    "I remember thinking that they were amazing and then... blank."
    "I ended up watching the band playing for over an hour."
    "So that's Keisuke's band, huh?"
    "I have to admit, they sounded really great... I might have just become a fan."
    "I still think they could sound even more amazing with him in it though..."
    "Hmm... their vocalist said she wanted to get Kei-kun to join them as a vocalist..."
    "Maybe I can look for a way to push him into doing that..."
    "Yeah, I think that's just what I'm going to do!"
    "But for now, I'm going to head home and lie down for a bit. I'm still feeling a little dizzy from the loud music..."
    stop music fadeout 2.5
    $ date = None
jump Day13_Keisuke
