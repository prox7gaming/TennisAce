label Day14_Shoichi:
    play music2 "music/BGM/The People Here.ogg" fadein 5.0
    scene ShoppingFestival with fade
    "I walk among the mass of people around, trying to follow behind the giant mound of blue fur that walks ahead of me."
    "For some reason, today his back seems so much larger than usual."
    "The stalls around us are all exploding with activity, with people coming and going ceaselessly."
    "From the corner of my eyes I can see so many familiar faces."
    "I see Class Rep and Kyoko running a dart board, excitedly calling people over to try them out."
    "Saya-chan and the tennis club members are all lining up to eat some ramen at another nearby stall."
    "Jin and Gin are arguing with each other because Gin seems to have eaten all the food they were supposed to serve their customers."
    "Kei-kun is arguing with our teachers about something, making obscene gestures that are so unlike him."
    "Jun's dressed as a taiko drummer, pounding on the drums on top of a stage with a bright smile on his face."
    "Vic-kun and Ryoji are walking around and trying different games. Ryoji still looks just as bored as always though."
    "I also catch a glimpse of a white wolf, but he merely turns away from me when our eyes meet."
    "For some reason, Takehiko-san is throwing a ball into a target, causing Hitoka to fall into a pit of water when he hits it."
    "He looks so much happier than I'm used to seeing him. It's such a bizarre sight."
    "I keep walking behind Shoichi this whole time, but it feels like we never go anywhere."
    "I try calling out to him but realize my voice doesn't work."
    "I reach for my throat, trying to utter some kind of sound, but as I grow more desperate, my voice refuses to come out."
    "That's when I realize... despite all these people being here, despite them doing all of these things..."
    "I can hear no sound."
    play music "music/rain.ogg" fadein 2.5
    "Then, something begins to echo."
    "I realize that it's the sound of rain, slowly increasing in intensity."
    "Even though it's so faint and subtle, it also feels as if it's roaring and drowning everything else around."
    "Wait..."
    "How... how did I even get here in the first place?"
    "A feeling of not belonging starts to assault me as my chest grows tighter."
    "Everything feels so... so hazy. Almost as if it could disappear if I reached out to touch it..."
    scene Black with fade
    "I close my eyes as I grip my chest, the fear that's been building up inside of me is so overwhelming that it's almost blinding."
    "I try to remember what I'm supposed to be doing but my mind feels as if it's covered in a thick haze."
    "Where... am I?"
    "How... did I get here?"
    play sound "music/tap.ogg"
    "Just as I feel like I might be completely taken by the confusion, I feel a hand gripping my shoulder."
    scene AlleyNight
    show s 1 c smile at fdis, five
    with fade
    "My eyes shoot open to reveal Shoichi right in front of me."
    "We're no longer in the festival..."
    if day10 == "shoichi":
        "I feel like this place is familiar somehow, but my mind can't connect..."
    else:
        "Is this... an alley? It's so damp and dark and hidden away from sight..."
    show s 1 c happy at fdis
    s "\"...\""
    "Shoichi's mouth moves as he begins to talk... but no sound comes out of it."
    "My brain can't comprehend what's going on as it desperately attempts to fill the gaps."
    "I try to understand what is going on but the fog just continues to grow heavier."
    show s 1 c wry at fdis
    "Shoichi continues to speak without making any actual sound."
    "I can feel as if the vibrations of his voice are echoing through my body, but my ears refuse to hear."
    "I try to look around me, trying to figure out what's going on."
    show s 1 c flattered at fdis
    "I feel my hand being squeezed as Shoichi suddenly leans closer to me."
    stop music2
    stop music
    scene Black with fade
    s2 "\"I love you.\""
    scene AlleyNight
    show s 1 c flattered at fdis, five
    with fade
    play music "music/rain.ogg" fadein 2.5
    "Everything blacks out for a split second then as his words seem to hit me like a truck."
    "The whole world went dark for me... I could hear nothing but Shoichi's voice..."
    "But just as soon as that darkness came, it vanished, bringing everything back into focus."
    "Shoichi still stood in front of me with a big smile on his face. He looked me up and down, expectantly."
    "My heart, which had been racing this whole time, suddenly felt like it stopped."
    "The only sound I could hear was the rain roaring all around us."
    "Those words kept playing on repeat inside of my head."
    "Ugh... why is it so hard to concentrate?"
    "Unable to think of anything but the words that still lingered in the air, I nodded."
    show s 1 c wryt at fdis:
        ease .5 zoom 1.5 xoffset -30 yoffset 200
    "Tears welled up in his eyes as the husky leaned closer to me."
    "The smell of damp fur tickled my nose... which was funny because he wasn't wet at all."
    "As my childhood friend approached me slowly, just a little closer at a time until our noses could almost touch."
    "A hand cupped my cheek, stroking me softly."
    "I tried to turn my face and look away but he gently pulled my head back to look right at him."
    "His lips moved one more time, even though I still couldn't hear any words."
    "... But yet, I could feel the enormity of them hitting me again."
    "It was the same words as last time."
    "\"I love you.\""
    stop music
    scene Black with fade
    "Something wet brushes up against my lips and my brain glitches out again."
    "Unable to comprehend what is happening, my vision goes dark."
    "All I can feel is the gentle sensation of someone else's lips pressed up against mine."
    "I'm being kissed by Shoichi..."
    "... and somehow... I am dimly aware that I begin to kiss back."
    scene ShoichiBedroom with fade
    play music "music/night.ogg"
    "My eyes shoot open violently."
    "As the haze begins to lift from inside of my mind, I begin to make out shapes again."
    "I'm... in Shoichi's room?"
    "Ah... that's right. I'm spending the night here because it was too late to walk back home..."
    "I was... dreaming?"
    "What... why was I dreaming of that?"
    if day13bed == True:
        show cg4a_5 with dissolve
        "I turn around in bed... only to see Shoichi's face lying right next to mine."
        "My whole body freezes for a second as I try to remember why Shoichi's in bed with me."
        "My recollections start catching up with me again and I remember accepting his offer to share his bed."
        "I watch him breathing peacefully in his sleep..."
        "Somehow, seeing him like this has such a calming effect on my heart."
        "The rush of emotions that I had been feeling is completely drowned out, leaving only a single emotion on the forefront."
        "The sound of my heart beating echoes inside of my head..."
        show cg4a_6 with Dissolve(1.5)
        "... I lean in closer to him. I can feel his breathing against my face."
        hide cg4a_5
        "He looks so calm and peaceful like this... it makes me so happy seeing him this way."
        "I touch the tip of my nose against his..."
        "I can feel a desire building up inside my chest..."
        "I lean in a little further and..."
        play sound "music/fabric.ogg"
        hide cg4a_6 with dissolve
        play music2 "music/BGM/Mischief Maker.ogg"
        "{size=+4}What the hell am I doing?!{/size}" with hpunch
        "My brain finally catches up to what I'm doing as the last remnants of my sleepy daze lifts from my mind, causing me to immediately jump away before I can go through with what I was about to do."
        "{size=+4}Get a grip, me!{/size}" with hpunch
        "I lie on my back, as far away from Shoichi as I can get without falling out of the bed."
        "Covering my eyes with my hand, I let the realization of what I was about to do sink in."
        "Seriously, what the hell is wrong with me? I have a dream of kissing my best friend and suddenly wake up only to try and do it?"
        play sound "music/disappointment.ogg"
        "That would definitely be sexual assault..."
        "Getting carried away by a dream and nearly kissing someone because of it... I'm just so pathetic..."
        "It's all that damn wolf's fault for putting these thoughts in my head in the first place!"
        stop music2 fadeout 2.5
        play sound "music/fabric.ogg"
        show cg4a_5 with Dissolve(1.0)
        "..."
        "I turn to look at Shoichi again."
        "Despite my rowdiness, he still sleeps undisturbed."
        "Good thing I didn't wake him up... that would just be embarrassing."
        "... But I can't deny that I've been thinking a lot about him lately... even if it's just been trying to make sense of what he feels for me."
        "Whether what that guy said is true or not, I don't know, but..."
        "..."
        "Maybe I..."
        hide cg4a_5 with Dissolve(1.0)
        play sound "music/fabric.ogg"
        "Not letting my brain finish that thought, I turn around in bed and try to go back to sleep."
        "... I should probably avoid having mind-shattering realizations in the middle of the night when I'm still sleepy."
        stop music
    else:
        "I turn around in bed... or at least what passes for a bed."
        "Damn, this futon is uncomfortable..."
        "My eyes fall onto Shoichi's back... or at least the portion of it I can see from down here."
        "I can see his chest going up and down. My ears can barely pick up the sound of his breathing."
        "For some reason, hearing him breathing peacefully in his sleep makes me feel calmer... happier..."
        "The dream I had keeps playing on repeat in my head."
        "Me and Shoichi... kissing?"
        "The idea feels so strange to me. It's not something I ever would have thought of."
        "It's that stupid wolf's fault in the first place for making me think of this..."
        "And yet... the idea doesn't repulse me at all?"
        "..."
        "Maybe I..."
        "Not letting my brain finish that thought, I turn around in bed and try to go back to sleep."
        "... I should probably avoid having mind-shattering realizations in the middle of the night when I'm still sleepy."
        stop music
    window hide
    scene May22 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    play music2 "music/BGM/Dazzling Sunlight.ogg" fadein 5.0
    scene SClass with fade
    window show
    $ date = "day14"
    play sound "music/schoolbell.ogg"
    "The sound of the bell ringing snaps everyone's attention away from the lecture."
    "My stomach is definitely thankful for the arrival of lunch break though."
    show shima 1 u smile at five with dissolve
    shima "\"Oh, is it time already? Class sure did fly today.\""
    "A few students mumble half-hearted agreements, probably trying to appease the teacher."
    "Today we had another class filled with subjects that are nowhere on our curriculum and shouldn't have been assigned to us at all."
    "It's good that he's passionate about his work as a history teacher but he should really focus on the stuff he's supposed to be teaching instead of just talking about whatever he wants..."
    shima "\"Well, I guess that's it for today. Make sure you kids check the material once you get home. For now, enjoy your lunches.\""
    show shima 1 u smile at offscreenright with moveoridis
    play sound "music/slidingdoor.ogg"
    "The class mumbles a few agreements as Shima-sensei grabs his things and walks out the door."
    "Pretty sure we're not about to win any awards for enthusiasm."
    show j 1 u wince at fdis, five with dissolve
    "I turn to look to my side and see Jun staring down at his books with a conflicted look on his face."
    "I swear I can hear the gears turning desperately inside of his head."
    mc 1 u smile "\"Hey, Jun, what are you thinking so hard about?\""
    show j 1 u shock at fdis
    $ renpy.pause(1.0)
    show j 1 u wince at fdis
    j "\"It's... erm... I'm trying to remember all this material for the midterms. They're supposed to be the week after the festival, right?\""
    mc 1 u "\"Yeah. I'm surprised you're even bothering to study for it.\""
    j "\"I need to pass if I want to go to Germany...\""
    mc 1 u think "\"I guess that's true...\""
    mc 1 u "\"Are you feeling well though? You only just came back to school after being on bed rest.\""
    show j 1 u considerate at fdis
    j "\"I'm feeling fine. Mostly just lost. I have no idea what any of this is supposed to be."
    show j 1 u avoid at fdis
    extend " And don't even get me started on the math...\""
    mc 1 u wince "\"Yeah, a few days away will certainly do that to you.\""
    show j 1 u sigh at fdis
    j "\"Aaaah, I give up. I can't memorize any of this. I just have a ton of dates floating around in my head and I have no idea what any of them are for.\""
    mc 1 u considerate "\"I can try tutoring you later if you think that would help.\""
    show j 1 u wry at fdis
    j "\"Yeah, I think it would. Thanks."
    show j 1 u considerate at fdis
    extend " Uhm... how about we talk about something else at the moment? I kinda don't want to think about this right now.\""
    mc 1 u smile "\"Of course. Say, how was your weekend? I was meaning to visit you but ended up getting a bit busy. Sorry about that.\""
    show j 1 u think at fdis
    j "\"I did say I didn't want you guys to go out of your way for me so I wasn't expecting anyone.\""
    show j 1 u watch at fdis
    j "\"Things were just really boring for the most part. Not much to do at home other than play videogames, and I already beat all the games I have.\""
    mc 1 u talk "\"What about the piano? You could have snuck in some practice at least, no?\""
    show j 1 u considerate at fdis
    j "\"You'd think so, but... my parents didn't really want me stressing over the piano while I was recovering.\""
    mc 1 u wince "\"Jeez, isn't that a little overboard? I know you hit your head and all but it wasn't even a big injury. I thought you'd have been totally cleared by the weekend.\""
    j "\"{size=-2}You'd certainly think so...{/size}\""
    mc 1 u curious "\"What do you-\""
    play sound "music/slidingdoor.ogg"
    show j 1 u watch at fdis, two with move
    show sa 1 u happy at fdis, five
    show s 1 u smile at fdis, eight
    with moveiridis
    "My sentence is cut-off by the sound of the room's back door being opened, with Saya and Shoichi walking in together."
    sa "\"Osu!\""
    s "\"Morning.\""
    show sa 1 u smile at fdis
    "The difference between their greetings is certainly very noticeable."
    show j 1 u happy at fdis
    j "\"Osu!\""
    mc 1 u talk "\"Morning. Kinda rare to see you both walking in together. What gives?\""
    show s 1 u at fdis
    s "\"Nothing much. Saya-chan and I just bumped into each other in front of the door.\""
    play sound "music/chairscoot.ogg"
    "The two of them grab chairs as Jun and I push our tables together so the four of us can sit together."
    "We all take out our lunchboxes and put them on top of the table."
    show sa 1 u think at fdis
    sa "\"You know, I have a feeling the teachers are trying to kill us from boredom before the festival so we won't be able to enjoy it...\""
    mc 1 u considerate "\"Say that to Jun. His head was about to burst just five minutes ago.\""
    show sa 1 u at fdis
    show j 1 u wince at fdis
    j "\"[povFirstName]-san, don't say it like that...\""
    show s 1 u smile at fdis
    s "\"Do you need someone to help you study? I can try to see if I get some free time...\""
    show j 1 u considerate at fdis
    j "\"No, it's alright. I'll be fine.\""
    show j 1 u watch at fdis
    sa "\"How are you feeling though? Are you sure you're well enough to be back in class?\""
    show j 1 u avoid at fdis
    j "\"I was well enough since I got discharged from the hospital. My parents are just really paranoid...\""
    show s 1 u at fdis
    s "\"Paranoid, huh...\""
    show j 1 u watch at fdis
    j "\"By the way, I was gonna ask before you guys walked into the room. You asked about how my weekend went, [povFirstName]-san, but what about yours?\""
    mc 1 u worried "\"My weekend? Well...\""
    "Whenever I try to think about my weekend, that stupid dream just flashes back to my head..."
    show s 1 u annoyed at fdis
    s "\"Actually, I'd like to ask the same thing myself. You were gone by the time I woke up and didn't answer your phone all day on Sunday.\""
    show j 1 u shock at fdis
    j "\"Wha- You guys spent the night together?\""
    show sa 1 u talk at fdis
    sa "\"Was it because of the party?\""
    show sa 1 u at fdis
    show j 1 u wince at fdis
    j "\"Par- Oh, right, you were gonna throw a party for your dad.\""
    show s 1 u sigh at fdis
    show j 1 u watch at fdis
    s "\"Yeah. [povFirstName] spent the night on Saturday since it was too late for him to go home on his own. Then I woke up and he was just gone. He didn't answer any of my texts either.\""
    mc 1 u considerate "\"Y-yeah, I just thought I should get home early. I already wasn't supposed to spend the night out so I'm sure my mom wanted me home as soon as possible.\""
    show s 1 u annoyed at fdis
    s "\"That still doesn't explain why you couldn't pick up your phone.\""
    mc 1 u wince "\"I... I was busy with homework... I let a lot of it pile up.\""
    show s 1 u sigh at fdis
    s "\"Seriously? You're really irresponsible, you know that?\""
    mc 1 u judge "\"I don't want to hear that after all the work I put in to help you throw that party.\""
    s "\"Then get your homework done in time.\""
    "... Truth be told, I just wanted to get out of his house as fast as I could."
    "As soon as the sun cracked, I picked up my things and left."
    "Just seeing him in front of me already has me feeling both embarrassed and anxious for some reason."
    if day13bed == True:
        "I didn't want to run the risk of doing something stupid..."
    else:
        "I just felt like talking to Shoichi would be really awkward after that dream..."
    show s 1 u at fdis
    show sa 1 u talk at fdis
    sa "\"How's your dad doing anyway? Did he like the party?\""
    show s 1 u sigh at fdis
    show sa 1 u at fdis
    s "\"He... seemed to enjoy it. He was very tired from the trip but he still socialized a lot. He was nothing but compliments for [povFirstName] the whole time too.\""
    show sa 1 u laugh at fdis
    sa "\"That's great! I'm really glad things worked out well.\""
    s "\"Yeah, sure...\""
    "Saya and Jun don't even notice it, but since I was there that night I know how torn up Shoichi is about the whole thing."
    "I'm still angry at Takehiko-san for only criticizing his son despite everything Shoichi did for him."
    show s 1 u at fdis
    show sa 1 u at fdis
    s "\"I saw Hitoka at the party. She stayed the night too.\""
    j "\"Who's Hitoka?\""
    sa "\"She's Shoichi's little sister. She's a freshman here in our school. And I thought you weren't going to invite her to that.\""
    show s 1 u sigh at fdis
    s "\"I wasn't. Someone else took care of that for me.\""
    "Even though I'm looking anywhere but at him, I can still feel Shoichi's eyes burn a hole on my face."
    "Maaan, he's still pissed about that whole thing."
    mc 1 u fsmile "\"Y-yeah... that was a very unfortunate decision huh?\""
    s "\"I'm still gonna get back at you for that.\""
    show sa 1 u think at fdis
    sa "\"What's the problem in having her there anyway? I'm sure she was all too happy to go.\""
    s "\"Oh, she sure was. Especially cause this dumbass here felt the need to tell her I purposefully didn't invite her in the first place. She was all too happy to go just so she could chew me out for it.\""
    show sa 1 u bored at fdis
    "Saya winces, scratching at the back of her neck with an uncomfortable expression."
    sa "\"Oh, ouch... Knowing Hitoka-chan, that can't have been pretty.\""
    s "\"It wasn't.\""
    mc 1 u considerate "\"Hehe... I'm really sorry?\""
    s "\"Sorry doesn't make up for it, pal. I'm gonna have your ass for that later.\""
    show j 1 u think at fdis
    j "\"It was nice knowing you, [povFirstName]-san.\""
    show sa 1 u at fdis
    sa "\"You will be missed.\""
    mc 1 u wince "\"D-don't just write me off like that!\""
    show s 1 u at fdis
    mc 1 u considerate "\"Uhm... I know I already said this last night but I'm really really really sorry. I swear I'll find some way to make this up to you.\""
    s "\"You could start by smoothing things over with her. The last thing I need is Hitoka clinging to me all the time like I'm a little child in need of an adult escort.\""
    show j 1 u at fdis
    j "\"Wouldn't she be the little child though? Since you're her big brother and all?\""
    show s 1 u sigh at fdis
    s "\"Believe me, the fact that I'm her older brother won't keep her from patronizing me in the slightest.\""
    show j 1 u wince at fdis
    j "\"Ah... I see...\""
    show j 1 u watch at fdis
    show s 1 u at fdis
    s "\"You can imagine my joy at the prospect of being babysat by her.\""
    show j 1 u smile at fdis
    j "\"At least you'll get to spend more time with your sister. That's got to be a nice thing, right?\""
    show s 1 u sigh at fdis
    s "\"... I suppose.\""
    show j 1 u watch at fdis
    show sa 1 u talk at fdis
    sa "\"Oh man, that wasn't a happy \"I suppose\".\""
    show sa 1 u at fdis
    "Shoichi sighs, slumping forward on the table with a defeated look on his face."
    s "\"I've just had so much stuff to worry about lately. I didn't need to add another one to the list.\""
    sa "\"You're her older brother though. You can't just ignore her forever.\""
    show s 1 u wince at fdis
    s "\"It's not supposed to be forever... just until I can get my problems dealt with...\""
    sa "\"Do you even have that many problems to deal with? That's the first I've heard of it.\""
    show s 1 u sigh at fdis
    s "\"Between the volleyball club, the student council, entrance exams and my own grades? I'm pretty sure I don't need to tell you about those and that's already a lot.\""
    s "\"Now that dad's back, I also have to worry about that too.\""
    j "\"Why do you have to worry about your dad?\""
    show s 1 u avoid at fdis
    s "\"I'd... rather not get into that.\""
    show j 1 u shock at fdis
    j "\"O-oh. I'm sorry, I shouldn't have asked.\""
    show s 1 u sigh at fdis
    s "\"You're fine. The man's just a piece of work...\""
    show sa 1 u bored at fdis
    sa "\"Takehiko-san, that's Shoichi's dad's name, is a pretty overbearing man. I'm sure he's gonna have to deal with a lot of pressure now that he's back home.\""
    s "\"You'd be right about that. Can you believe I have to deal with a curfew again?\""
    show sa 1 u at fdis
    show j 1 u wince at fdis
    j "\"A curfew? Not even I have that.\""
    mc 1 u considerate "\"That's not too bad though, right? I mean... you're not the type to be out of the house late anyway.\""
    show s 1 u at fdis
    s "\"I have to be home by 6PM. Club activities can easily go over that on some days.\""
    mc 1 u wince "\"O-oh...\""
    show s 1 u sigh at fdis
    s "\"Yeah... \"oh\".\""
    show s 1 u at fdis
    s "\"Actually, can we just talk about something else? I don't want to think about this right now.\""
    show j 1 u smile at fdis
    j "\"Yeah, sure!\""
    show sa 1 u laugh at fdis
    sa "\"How about we talk about your lunch? I bet it's gonna be pretty and delicious today too!\""
    show s 1 u sigh at fdis
    show sa 1 u at fdis
    s "\"Actually, I had to buy a premade lunch at the convenience store. Hitoka was feeling spiteful towards me and didn't bring me any today.\""
    show j 1 u think at fdis
    j "\"Gee, I wonder why.\""
    mc 1 u fsmile "\"W-well, maybe this is an opportunity to rely on her less. After all, you two don't even live together.\""
    s "\"I don't want to hear that from you. You're the cause of all this.\""
    mc 1 u wince "\"S-sorry...\""
    show s 1 u at fdis
    s "\"What is it with you today? You're just rolling along with the punches. Usually you'd have some kind of snarky remark on the ready.\""
    mc 1 u avoid "\"I don't know what to tell you...\""
    show s 1 u sigh at fdis
    s "\"Are you sure you're okay?\""
    mc 1 u fsmile "\"I-I'm fine. Seriously!\""
    "I'm pretty sure my voice went up by one or two keys when I said \"I'm fine\", but if anyone's noticed it, they decided to just ignore it."
    show s 1 u at fdis
    s "\"Anyway, I'm pretty sure you guys are gonna have way better food than I do today.\""
    show j 1 u happy at fdis
    j "\"I have chicken karaage!\""
    show sa 1 u shock at fdis, jumping
    sa "\"Damn. Your mom really went out of her way today!\""
    show j 1 u watch at fdis
    j "\"Actually, I'm the one who makes my lunches. She just leaves out the ingredients for me to use.\""
    sa "\"Wait, you can cook?!\""
    show j 1 u think at fdis
    j "\"I studied in a boarding school {i}and{/i} my parents work two jobs. I'm used to doing chores.\""
    show sa 1 u pout2 at fdis
    sa "\"Damn... everyone's better at this kind of thing than I am.\""
    mc 1 u smile "\"Not everyone.\""
    "I give Shoichi a sly, knowing glance."
    show sa 1 u at fdis
    "Saya immediately realizes what I mean."
    sa "\"Oh right.\""
    s "\"What?\""
    "Shoichi looks between the two of us with confusion."
    "It... honestly bothers me..."
    "I feel awkward just looking at him."
    "Talking to him with the others around isn't too bad but..."
    "I'm not really being myself, am I?"
    "Ugh... my head hurts."
    stop music2 fadeout 2.5
    scene SRooftop with fade
    play sound "music/metaldoor.ogg"
    play music "music/breeze.ogg"
    "I come out to the rooftop after class has ended for the day."
    "Like most days, there's a nice breeze here on the rooftop, ruffling my fur and helping me deal with the heat."
    "I'm glad the rooftop is restricted access to the students. At least that makes it so I don't have to share this place with anyone else."
    "The only real mystery is why they never lock the door if they don't want anyone coming here."
    "Even though we have practice today, I decide to take a few minutes to myself so I can relax before I go there."
    "This weekend has been a little rough on my sanity..."
    "Ugh, I'm worrying about this whole thing with Shoichi more than I should be."
    "I thought I'd resigned myself to accept him no matter whether him having feelings for me is true or not but..."
    "I... I can't get it out of my head..."
    "I've been thinking about it more and more since the idea was first planted..."
    "As I'm walking to the spot I usually nap in, I hear some shuffling."
    show h 1 u at five with dissolve
    h "\"Who's- Oh.\""
    "From behind the vent, I see the one person I wish I would never run into again."
    play music2 "music/BGM/Auto.ogg" fadein 15.0
    h "\"Well, isn't this awfully coincidental. We meet again.\""
    mc 1 u shock "\"What- Why are you here?\""
    "My brain immediately starts scrambling."
    "I don't even want to think about being in the same room with this guy and yet here he is, right in front of me."
    "If there's a God, he either really hates me or has a really twisted sense of humor."
    h "\"I could ask you the same question.\""
    mc 1 u judge "\"I'm always here. This is kind of my place.\""
    h "\"Your place? Didn't see your name anywhere here. Must have missed it. Unless you're the \"Rooftop\" whose name I saw on the door.\""
    "The wolf shrugs, staring at me with what is either absolute boredom or a really good poker face."
    if harukiss == True:
        mc 1 u sigh "\"Don't act smart with me. I come here every day and I've never seen you here before... before...\""
        h "\"Before we shared saliva?\""
        mc 1 u sigh2 "\"Before you forced yourself on me, you mean.\""
        h "\"Whatever you say. You're not even a good kisser anyway.\""
        mc 1 u sigh "\"What? I'll have you know that I'm a great kisser!\""
        h "\"Is that so? I'm sure the captain would love to test that out for himself.\""
        mc 1 u wince "\"Ugh... just shut up already...\""
    else:
        mc 1 u sigh "\"Don't act smart with me. I come here every day and I've never seen you here before that day when you tried pushing me.\""
        h "\"Oh please. We both know I wasn't trying to {i}push{/i} you.\""
        mc 1 u avoidb "\"I... I don't know what you're talking about.\""
        h "\"Pft. Whatever you say. What does that guy even see in you in the first place? You're so bland.\""
        mc 1 u sigh "\"Could you just shut up already? Stop bringing Shoichi into this.\""
    h "\"Why? Have I struck a nerve?\""
    mc 1 u judge "\"You know you did.\""
    h "\"It's not my fault he's always obsessing about you whenever you're around. He's like a dog in heat. Seeing the way he acts around you frankly makes me want to puke.\""
    "The wolf has the biggest shit eating grin on his face."
    "Oh, he's so fucking smug it honestly pisses me off... which I'm sure is his objective in the first place."
    "I know I should control myself... I know I shouldn't say anything about it... but I feel like my blood is boiling as I begin to seethe with rage."
    "He can say whatever the hell he wants about me but... to bad-mouth Shoichi in front of me..."
    "He has a lot of nerve..."
    menu:
        "I... I'll just..."
        "Be the better man":
            stop music2 fadeout 2.5
            $ harukill = False
            "I start reciting math in my head to try and cool off."
            "Nothing gets my brain to shut off and disengage quicker than math does."
            "I just stand here, staring at that stupid smile on his face without doing or saying anything?"
            h "\"What's wrong? Cat's got your tongue? Aww, poor little captain will be so sad about that.\""
            "Even though every fiber of my being wants to do nothing but punch his teeth in, I refuse to be that kind of person."
            "He can throw whatever abuse he wants at me, I'm not gonna take the bait."
            "He wants to get a rise out of me? Then he'll have to work for it because I'm not giving it to him that easy."
            mc 1 u blank "\"Whatever you say.\""
            play music3 "music/BGM/Punchline - Org.ogg" fadein 5.0
            h "\"Huh?\""
            "The smile on his face instantly vanishes, being replaced by a look of confusion and consternation."
            "He must not be used to people just ignoring him like this."
            "Come to think of it... he probably acts this way to push people away on purpose."
            "Why he'd want to do that... I have no idea."
            "But he probably doesn't know how to act when people don't fight back."
            "Which is kind of already a victory by itself."
            h "\"What? Not gonna say anything? I know you might not be the most creative guy but come on, you can't be that stupid.\""
            mc 1 u blank "\"Well, sorry. Must be having an off day.\""
            "I make sure to sound as monotone as I possibly can."
            "He frowns."
            h "\"Nothing? You've got nothing to say to that? No witty one-liners, no snarky responses? Anything?\""
            mc 1 u blank "\"Nope, sorry. I'm all snarked out.\""
            "He eyes me up and down for a few more seconds, studying me."
            h "\"What's wrong with you? Did you get hit in the head or something? Can't you tell that I'm insulting you?\""
            mc 1 u considerate "\"You are? Must have gone over my head.\""
            "I have to admit, the look of confusion on his face is hilarious."
            "Finally, he turns away sighing."
            "The wolf sits down on the floor, leaning his back against the vent pipe and just looking away from me."
            h "\"Jeez. Didn't know you were a bore too.\""
            stop music3 fadeout 2.5
        "Talk back":
            $ harukill = True
            mc 1 u judge "\"Oh yeah? You wanna know what I think?\""
            "I know Shoichi wants to believe he's a good guy deep down... and I know I shouldn't use what he told me against this guy, but..."
            "The wolf lifts an eyebrow, that stupid smile still plastered over his face."
            "All forms of self-control on my part fail one after another."
            mc 1 u suggestive "\"I think you're just some lost little kid who likes to act tough when, in fact, deep down you're just pushing everyone away because you're afraid they'll hurt you like daddy did.\""
            "The smile immediately vanishes."
            "His eyes go cold... I don't see a hint of emotion on his face."
            "No smile, no frown, no expression."
            h "\"What are you talking about?\""
            mc 1 u "\"Oh, you know. Daddy got drunk and decided to take his frustrations out on you and your mommy. Pretty cliché if I say so myself.\""
            "His eyes widen in shock. He stares at me with his mouth agape, doing that thing fish do when they open and close their mouths repeatedly."
            h "\"W-who told you that?\""
            "When his voice finally comes out again, it's shaky and uncertain."
            "I already knew from the start that I was going too far... but only now do I begin to regret it."
            "My reaction is akin to responding to an insult with a nuke."
            "I look down at the floor, scratching the back of my neck."
            stop music2 fadeout 2.5
            mc 1 u avoid "\"I... uhm... I'm so-\""
            play music3 "music/BGM/Auto Pilot.ogg"
            h "\"{size=+4}Who told you?!{/size}\"" with hpunch
            "He shouts at me, snapping my attention and my eyes back to him."
            "The wolf stares at me with bared fangs and bristled fur."
            "His eyes have shrunk to the point of looking like slits."
            "He's snarling at me, his breathing rapid and erratic."
            "At any second now I'm afraid he might jump at me."
            "I take a step back and lift my arms in the air, trying to deescalate the situation."
            mc 1 u wince "\"I'm... I'm sorry, okay. I just-\""
            h "\"Was it that fucking dog? Was he the one that told you? It had to be him!\""
            mc 1 u wince "\"He only told me because he didn't want me to get angry at you or report you for what you did. He was trying to protect you.\""
            h "\"Protect me? I don't need to be protected. I don't need to be pitied, damn it. I'm more than capable enough of protecting myself.\""
            mc 1 u fsmile "\"I-I'm not saying you do, it's just...\""
            h "\"Just what?\""
            mc 1 u avoid "\"Shoichi just... cares. Even if you're an insufferable piece of shit, which you are, he still cares about you because you're a member of his team... so he wants to help you.\""
            "The wolf looks me up and down, raising an eyebrow."
            "He seems to have calmed down somewhat... or at least he's no longer ready to lunge at my neck."
            h "\"If this is you trying to be comforting then you really suck at it.\""
            mc 1 u annoyed "\"Well... fuck you too.\""
            stop music3 fadeout 2.5
            "Haruki sighs, leaning his back against the vent and sliding down until his ass is seated on the floor."
            h "\"{size=-2}Just perfect...{/size}\""
            "He mutters those words, more to himself than to anyone else."
            h "\"Oh, and I just might kick his ass for telling you this.\""
            mc 1 u sigh "\"Please don't... I don't want to see him getting cuffed cause he put you in the hospital.\""
            h "\"Oh, you don't think I can take him in a fight?\""
            mc 1 u considerate "\"I don't think there's a high-schooler in this country that can. That guy is freakishly strong.\""
            "He looks away, but not before I can catch a glimpse of something that looks like a hint of a smile on his face."
            h "\"Yeah, I kinda noticed that.\""
    "He's lost all of the attitude he had just a few minutes ago."
    "Instead he stares quietly at the roof's guard rails... or maybe he's looking at the sky beyond them."
    play music2 "music/BGM/Dog Days.ogg" fadein 5.0
    mc 1 u wince "\"So... uhm... why are you here?\""
    h "\"Why? You want me to leave?\""
    "His voice doesn't have any sign of derision or malice in it anymore."
    "It echoes clear and, honestly, sounds quite a bit bored."
    "Instead of trying to taunt me or annoy me, it sounds like he just doesn't care."
    "It kinda catches me off-guard how quickly his personality flipped."
    "... Or maybe he's always like this?"
    mc 1 u avoid "\"That's... not what I'm saying. I just wanna know why you decided to start coming here all of a sudden. Like I said, I come here all the time and had never seen you here before.\""
    "The wolf sighs, rubbing his forehead."
    h "\"Don't you have other people to annoy instead of me? Friends, maybe?\""
    mc 1 u considerate "\"Sure, but none of them are here right now so I guess you're the one I'm stuck with.\""
    h "\"I can still walk out.\""
    mc 1 u "\"Sure... that was also true five minutes ago though and you didn't.\""
    "He sighs again. This guy sure can sigh."
    h "\"If you're not going to do anything to amuse me then you could at least be quiet.\""
    mc 1 u talk "\"Yeah? Well, too bad then. I'm not here to satisfy your whims.\""
    if harukill == False:
        h "\"Oh, so {i}now{/i} you've got snark.\""
        mc 1 u smile "\"It comes and goes. There's a lot of demand for it so stocks fluctuate wildly.\""
        h "\"Tch. You're such a shithead.\""
        if harukiss == True:
            mc 1 u sigh "\"Look who's talking. I can still report you for what you did remember?\""
            h "\"What? And admit a man kissed you against your will? Please, like you'd ever do that.\""
            mc 1 u frownj "\"You don't know me at all.\""
            h "\"Sure I do. When I don't hear the captain talking about you I see the two of you chatting it up in the lockers for everyone to hear. You really need to learn the concept of an inside voice.\""
            mc 1 u avoidb "\"I... that's...\""
        else:
            mc 1 u sigh "\"Look who's talking.\""
            h "\"Oh, wow. Great comeback. \"Nuh uh, you are\". I don't know how I will ever recover.\""
            mc 1 u blank "\"If you say so.\""
            h "\"Pft. So you're just going to blank me out whenever it's convenient to you?\""
            mc 1 u blank "\"I don't know what you're talking about.\""
    else:
        h "\"Clearly. You're merciless too. I didn't think anyone would ever be cruel enough to just throw that shit on my face to spite me.\""
        mc 1 u avoidb "\"Y-yeah... I'm... uhm... I'm so-\""
        h "\"Stop apologizing. It's not needed and, frankly, it's annoying. Own up to what you did already.\""
        play sound "music/stab.ogg"
        "This guy's attitude makes me come and go on the whole \"feeling bad about it\" thing..."
    h "\"Although I've got to admit... no one's ever treated me like that before. It's refreshing. Kinda amusing too.\""
    mc 1 u sigh "\"You found that... amusing? Jeez, you really are a broken toy.\""
    h "\"Pretty much. But I own up to it.\""
    mc 1 u sigh2 "\"That doesn't give you a pass to be an insufferable cunt though.\""
    if harukill == True:
        h "\"Man, you really do have an impressive vocabulary of insults. You talk to your mother that way?\""
        mc 1 u sigh "\"No. Only to shitty little juniors who think they're so smart and amazing.\""
        h "\"Pft. I take back what I said. I might actually like you.\""
        mc 1 u sigh "\"Pass.\""
    else:
        h "\"So which is it going to be? Are you going to cuss me out or tune me out? Make up your mind already?\""
        mc 1 u blank "\"I don't know what you're talking about.\""
        h "\"Pft. You're either a giant idiot or... actually, come to think of it, there's no alternative.\""
        mc 1 u blank "\"I guess.\""
        h "\"Jeez, stop doing that already. It's boring when you do that.\""
        mc 1 u smile "\"In case you haven't noticed, that's the goal.\""
        h "\"Yeah yeah. Well, I at least have to give you props for being original. No one's ever done {i}that{/i} to annoy me before.\""
        mc 1 u sigh2 "\"It's not supposed to make you happy, you know.\""
        h "\"Well, sucks to be you. You don't get to tell me how I'm supposed to feel.\""
    mc 1 u "\"Also, you still haven't answered my question of why you came up here.\""
    h "\"Oh God, you're not gonna let that go are you?\""
    mc 1 u "\"Don't plan to, no. You're already up here with me and you already know being a cunt will get you nowhere so what's the harm in talking.\""
    h "\"...\""
    "He looks up at me with a frown."
    "It almost looks like he's weighing whether he should be forthcoming or keep acting like a jerk."
    "Well, if he chooses to be a jerk then I can at least tell Shoichi that I tried but that there's no redeeming this guy."
    "Instead, he sighs one more time, scratching the top of his head and looking away from me."
    h "\"The first time I came here, I did so because I was called by the captain... but while I was waiting for him, I really liked the breeze up on the roof. And how quiet it is.\""
    mc 1 u shock "\"Oh...\""
    h "\"What? Are you gonna make fun of me for it?\""
    mc 1 u considerate "\"N-no. That's not what I was thinking at all. Honestly, those are the same reasons why I like it up here.\""
    h "\"Hmm.\""
    "I'm... kinda surprised by it."
    "That he would list the exact same reasons why I like to be here... that's one hell of a coincidence."
    h "\"...\""
    mc 1 u worried "\"...\""
    "He's not exactly very talkative is he?"
    "Honestly, why am I even trying to talk to this guy in the first place?"
    "... Is what I would like to say, but I already know the answer to that."
    "Shoichi believes he's actually a good guy who just needs someone to talk to..."
    "Well, Shoichi is also incredibly naive. No one's ever just going to solve his issues just by talking."
    "I'm pretty sure that even if Shoichi's right, this guy's still gonna need years of therapy to readjust."
    "But... it doesn't hurt to try talking to him I guess."
    mc 1 u talk "\"Can... I ask you a question?\""
    h "\"You've already been bugging me this whole time. Might as well.\""
    "I'll just choose to take that as a wholehearted agreement."
    mc 1 u curious "\"Why do you antagonize Shoichi so much? You've got nothing but criticism about him.\""
    h "\"Am I supposed to like the guy?\""
    "Actually, I already think that you do... but I think it's best to omit that for now."
    mc 1 u "\"Not what I mean. Just... you've got to know that he means well, right?\""
    "The wolf shrugs."
    h "\"What he means doesn't matter to me. It's the things he does that annoy me. He always keeps telling me to do things. Who does he think he is to boss me around?\""
    mc 1 u wince "\"He... he's kinda bossy, yeah. But he only does that because he wants to help.\""
    h "\"He does that because he thinks he knows better. There's no question about it anymore. Everyone in the club treats him as our only hope of victory. We have to rely on him for everything.\""
    h "\"No matter what you do or how well you do, he always gets the credit in the end. Frankly, it's infuriating. Why should I work together with that guy?\""
    mc 1 u talk "\"I'm sure if you told him how you feel he-\""
    h "\"Told him how I feel? He's not my goddamn shrink. Why should I have to tell him how I feel?\""
    "Ugh... does he have to go against everything I say?"
    mc 1 u considerate "\"Look, just... take it from someone who knows him well. Shoichi really does mean to help, he just might not always come across that way.\""
    h "\"Yeah, sure. Someone who knows him well. Is that why you never realized how hopelessly he's fallen for you? Because you know him {i}so{/i} well?\""
    mc 1 u avoid "\"...\""
    "He cocks his head to the side, eying me with curiosity."
    h "\"What? Not going to deny it?\""
    mc 1 u avoid "\"I'm... not sure I can anymore.\""
    h "\"Oh.\""
    "That's it. He merely mutters an \"oh\" and looks away from me awkwardly."
    mc 1 u sigh2 "\"That's all you're going to say? \"Oh\"? Last time you had a lot more that you wouldn't stop talking about.\""
    h "\"Last time you were in denial. What the hell do you expect me to say to that? You basically just admitted it.\""
    mc 1 u avoidb "\"... Oh.\""
    h "\"See? Nothing to be said.\""
    mc 1 u sigh "\"Yeah...\""
    h "\"I guess this is the point when I'm supposed to \"wish you the best\" or something like that? I don't really want to but I guess talking to you was kinda fun so I suppose I should.\""
    mc 1 u avoid "\"Thanks but I think I'll pass.\""
    "He shrugs once more."
    h "\"Hey, suit yourself. I'm trying to be nice here.\""
    mc 1 u confused "\"I'm surprised you even know how.\""
    h "\"If you prefer me to go back to insults then I can do that too.\""
    mc 1 u sigh2 "\"... Pass even harder.\""
    h "\"Then stop complaining about what you already have.\""
    mc 1 u sigh "\"Yeah yeah... whatever you say.\""
    mc 1 u sigh3 "\"You know, if only you were nicer to people, you'd see that they wouldn't shun you so much.\""
    h "\"Now why the fuck would I want to do that?\""
    mc 1 c considerate "\"Come on, just keep it in mind, okay? Try toning your sardonic attitude just a tad. I'm sure you'll eventually notice a difference.\""
    "He stays silent, apparently choosing to ignore my words."
    "Well... if he decides to even just think about it a little bit then I'll already be happy."
    "I really think he'd have a lot more success if he just learned to cooperate with people."
    scene Sky with fade
    "We both stare at the sky and the clouds that are lazily passing by above us."
    "The sensation of the wind ruffling my fur is calming as always."
    "I can definitely understand why he'd like it up here."
    "It's... peaceful, in a sense."
    "... I guess for someone that's had the kind of life he has, \"peaceful\" would sound really alluring."
    "... And here I am thinking about him as if I've got him all figured out."
    "In reality, all I know is one little thing about him... and yet, I let that define him in my mind and suddenly I already have an image of him formed in my head."
    "If... if other people treat him like this once they find out about what happened then I can definitely understand why he'd be annoyed all the time."
    "In a sense I guess I can relate... I remember always being looked at with pity after my dad died."
    "Once teachers and other adults found out, I was no longer my own person."
    "I was just the boy whose father died in a car accident..."
    "Ugh... the last thing I wanna be doing is relating to this guy..."
    "Or maybe I'm just trying to justify his actions because I don't want Shoichi to be wrong about him."
    "I can only imagine how disappointed he'd be if that were the case... and I don't want to see that."
    h 1 u "\"What do you plan to do?\""
    mc 1 u shock "\"Huh?\""
    scene SRooftop
    show h 1 u at five
    with fade
    "His voice snaps me out of whatever daze I had found myself in."
    "Man, I really have to stop spacing out everywhere."
    h "\"You know... about him being all gay for you. What do you plan on doing?\""
    mc 1 u avoidb "\"... Do you have to put it that way?\""
    h "\"Alright, I'll rephrase. What do you plan on doing about him being all GaGaGa for you?\""
    mc 1 u sigh2 "\"... How is that any better?\""
    h "\"You never asked for better, you just asked me not to say it that way.\""
    mc 1 u sigh2 "\"... Point taken.\""
    mc 1 u avoid "\"Either way... I don't know what I'll do. I'm still... not 100\% sure that he's really... you know...\""
    h "\"Gay? Queer? A flaming homosexual?\""
    mc 1 u sigh2 "\"Could you stop framing things that way? I was looking for a metaphor.\""
    h "\"And I said the actual words. Anyway, go on.\""
    "Urge to smack him rising rapidly... Must. Not. Smack."
    mc 1 u sigh "\"I'm still not sure if he's those things you said. I don't know if I should say something about it or not...\""
    h "\"Unless you plan on confessing to him then I'd just avoid the subject altogether. You'd just hurt him.\""
    mc 1 u confused "\"I didn't expect to see you giving me legit advice.\""
    "Haruki shrugs, looking bored and uninterested."
    h "\"I'm a little box of surprises. Besides, if you two start dating, I can only imagine how glorious the trainwreck would be so I kinda want to see it.\""
    mc 1 u sigh2 "\"Of course you'd have a shitty reason for doing it.\""
    h "\"Just because I can be nice doesn't mean I always want to.\""
    mc 1 u avoid "\"Either way, I don't know what to do...\""
    h "\"If you like him, kiss him. If you don't, say nothing. It's not exactly hard.\""
    mc 1 u sigh2 "\"I'm not just going to kiss him out of the blue. What are you, insane?\""
    "A sly smile appears on his face as he stares up at me."
    "It sends a shiver down my spine."
    h "\"Funny that that's the part you focused on. Could it be that you just accidentally admitted to liking him too?\""
    mc 1 u shockb "\"W-what?! N-no!\""
    h "\"Pft. God, you get flustered so easy.\""
    mc 1 u annoyed "\"Fuck you!\""
    h "\"Sorry, no can do. It looks like there's already someone else you want to fuck.\""
    mc 1 u sigh2 "\"Ugggh...\""
    "God, give me patience because if you give me strength I'm going to smack this guy..."
    h "\"Hey, you've got no reason to hold out on me. Just tell me the truth.\""
    mc 1 u sigh "\"Why am I even supposed to open up to you? You're an ass.\""
    h "\"True. But I'm also the only person who knows so I'm the only one you can talk to about it.\""
    h "\"Besides, you don't really like me so you don't have to worry about saying something that'll hurt my feelings.\""
    mc 1 u avoid "\"That's... a fair point...\""
    "Why do I find myself agreeing with this guy?"
    mc 1 u avoidb "\"I... don't know how I feel about it. When you first told me I didn't believe it but... it kept repeating inside my head. I started getting more conscious of him and noticing the tiniest things...\""
    mc 1 u sigh2 "\"I've done nothing but think about it since then...\""
    h "\"Oh man, I really did a number on you, huh?\""
    mc 1 u sigh "\"Yes you did. Another thing to add to the list of \"reasons I don't like you\".\""
    h "\"If it's any comfort, I'm pretty sure other people's lists are way longer than yours.\""
    mc 1 u sigh "\"That is no comfort at all.\""
    h "\"Good. I was hoping it wouldn't be.\""
    mc 1 u sigh "\"You're an asshole.\""
    h "\"Thank you. You too.\""
    "..."
    h "\"It looks to me that you've already fallen for the guy and just didn't realize it yet. Honestly, that's just disgusting.\""
    mc 1 u shockb "\"What? There's no way I... I...\""
    h "\"Okay, here's a little experiment to prove it to you. Think about kissing a guy... think about kissing me.\""
    if harukiss == True:
        mc 1 u sigh "\"Been there, done that.\""
        h "\"Yeah yeah. Just shut up and do it.\""
    else:
        mc 1 u sigh2 "\"What? Why would I-\""
        h "\"Just shut up and do it already.\""
    "I grumble a bit but decide to do it."
    "I close my eyes and think of him... I think of his body lightly grazing against me. Of his face slowly getting closer to-"
    mc 1 u dismay "\"No no no no. No way!\"" with hpunch
    h "\"{size=-4}Jeez, at least try to sound a little less disgusted.{/size} Anyway, that's your baseline. This is how you feel about kissing other guys.\""
    mc 1 u sigh "\"Could also just be because you're a little shit and I don't like you. It might not have anything to do at all with me liking Shoichi... or other guys for that matter.\""
    h "\"Sure, whatever makes you sleep at night, man. Anyway, now imagine it's the dog kissing you instead.\""
    "..."
    "I don't even have to think much about it. Just as soon as I close my eyes, that dream starts playing again."
    "I remember all the times I thought Shoichi looked handsome..."
    "For some reason, those thoughts would cross my mind without me even thinking it."
    if day5 == "shoichi":
        "Like when he took me out to the shopping district and he told me about all the things that had been stressing him out lately... the way he pulled me by the hand made my heart beat fast..."
        if day10 == "shoichi":
            "Or the day when he took me to the festival and give me the goldfish that I now have in an aquarium in my room... the smile on his face back then was wonderful."
            if day13bed == True:
                "... Or just a few days ago when we shared a bed. The look on his face as it was so close to mine made me want to melt..."
        else:
            if day13bed == True:
                "... Or just a few days ago when we shared a bed. The look on his face as it was so close to mine made me want to melt..."
    else:
        if day10 == "shoichi":
            "Like the day when he took me to the festival and give me the goldfish that I now have in an aquarium in my room... the smile on his face back then was wonderful."
            if day13bed == True:
                "... Or just a few days ago when we shared a bed. The look on his face as it was so close to mine made me want to melt..."
        else:
            if day13bed == True:
                "... Like just a few days ago when we shared a bed. The look on his face as it was so close to mine made me want to melt..."
    "I think of Shoichi's arms wrapped around me... of his lips pressed up against mine..."
    "The thought alone makes my heart beat fast... but I don't feel any disgust at all."
    "The idea... doesn't bother me in the least..."
    h "\"Well, your face is going red and you're not screaming out in shame and disgust so I'm gonna go ahead and say you have your answer.\""
    mc 1 u avoidb "\"... I'm still not sure.\""
    h "\"Oh for fuck's sake. Just go tell him already you fucking fag!\""
    mc 1 u sigh "\"Excuse me, what did you call me?\""
    h "\"Get used to it. That's what people are going to be calling you once you two dorks start being even more lovey-dovey in public than you already are.\""
    mc 1 u sigh "\"We are {i}not{/i} lovey-dovey.\""
    h "\"Up until a few weeks ago he was {i}not{/i} in love with you. Up until a minute ago you were {i}not{/i} crushing on him... See the pattern here?\""
    mc 1 u sigh "\"Fuck you.\""
    h "\"You wish. Anyway, I'm outta here. All this love talk is making me want to puke. If you'll excuse me.\""
    mc 1 u sigh "\"Knock yourself out... literally. Against a door preferably.\""
    h "\"See you later too.\""
    play sound "music/metaldoor.ogg"
    show h 1 u at offscreenright with moveoridis
    "Well... that was fun... somewhat."
    "..."
    "What the fuck am I supposed to do now though?"
    "I slide down with my back against the same vent Haruki had been leaning on until now."
    "Ugh... I need to clear my head..."
    "I just... want to stop having these thoughts already..."
    stop music fadeout 2.5
    stop music2 fadeout 2.5
    $ date = None
    jump Day15_Shoichi
