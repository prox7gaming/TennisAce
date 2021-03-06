label Day25_Keisuke:
    window hide
    scene June9 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene SClass
    play sound "music/crowd01.ogg"
    window show
    $ date = "day25"
    "It is finally the end of exam week."
    "The mood inside the classroom as as gloomy as can be."
    "Most students either left silently or just hung around hunched over their desks and contemplating their mistakes in life."
    show j 1 u wince at fdis, fiveh with dissolve
    "Right next to me is one such student."
    mc 1 u talk "\"You don't look so good.\""
    j 1 u considerate "\"I-I'm fine...\""
    mc 1 u sigh3 "\"Seriously, you look a little pale and you have bags under your eyes. Have you been sleeping at all?\""
    j 1 u avoid "\"... Probably not as much as I should.\""
    mc 1 u sigh "\"I know this goes without saying but you do know there's no point in getting good grades if you're dead from it, right?\""
    j 1 u considerate "\"Now you're just being dramatic...\""
    play sound "music/fall.ogg"
    show j 1 u shock at fdis
    "Jun tries to stand but his legs start to wobble and he falls back down to his chair."
    mc 1 u shock "\"Jesus, are you alright?\""
    j 1 u considerate "\"Y-yeah. I just got up too fast. It made me lightheaded... {size=-4}and I'm also kinda really hungry.{/size}\""
    mc 1 u sigh "\"... Please tell me you've been eating right.\""
    j "\"... Hehe.\""
    mc 1 u sigh3 "\"Come on, Jun, don't do this sort of thing.\""
    j 1 u wince "\"I'll be fine. I just need to rest a little bit.\""
    j 1 u considerate "\"I was kinda considering going to the music room to practice a little before heading home but I don't think that'd be a good idea.\""
    mc 1 u sigh "\"It very much wouldn't. Do I need to carry you home in order for you to be responsible?\""
    j 1 u avoid "\"N-no. I can head home by myself, it's fine.\""
    mc 1 u sigh "\"And are you actually going to eat and then sleep or are you going to go to your piano and start being an idiot?\""
    j 1 u considerate "\"I promise I'll take care of myself. I'm just a little tired cause this week was really rough.\""
    j 1 u wince "\"I'm not very good at studying, especially on my own, and then seeing the lack of results just puts so much stress on me that I kinda crumble...\""
    j 1 u considerate "\"It gives me this weird, sinking feeling in the pit of my stomach, as if it were twisting himself into knots.\""
    "... None of that sounds good at all."
    mc 1 u sigh "\"You better go home right away. I really don't want you wandering around the school when you're like this.\""
    j 1 u wince "\"Don't worry, I will. I really don't like feeling so tired.\""
    j 1 u think "\"I mean, I got a little bit of extra energy when I reached that good state of sleep deprivation where you start to see spots and feel really energetic.\""
    j 1 u considerate "\"But that was last night and it's already gone now.\""
    "..."
    "{size=+4}How can you call that good?!{/size}" with hpunch
    play sound "music/disappointment.ogg"
    "This tiger really worries me sometimes..."
    show j 1 u watch at fdis
    mc 1 u sigh3 "\"Just... just go home already. Please. I'll call you a taxi if I need to. {size=-4}I don't know if I want you walking home like this.{/size}\""
    j 1 u considerate "\"I'll be fine, seriously. I can take care of myself.\""
    mc 1 u sigh "\"Are you sure? Because from the way you're talking I get the feeling you'd be hit by a car.\""
    j 1 u wince "\"I-I'm not that tired. I can still pay attention when crossing the road.\""
    "For some reason I'm not sure if I believe him..."
    "But it's not like I can force him to do something either."
    "And he did say he already intends to go straight home..."
    play sound "music/disappointment.ogg"
    "Ugh, how can someone put themselves in this kind of situation?"
    mc 1 u sigh3 "\"Fine... I'll let it slide this time.\""
    j 1 u considerate "\"Than-"
    mc 1 u sigh "\"But if something like this happens again I am dragging you to the doctor's office by the hand and forcing you to sleep there. Got it?\""
    j 1 u wry "\"Y-yeah... got it.\""
    show j 1 u sigh at fdis
    "Jun quickly shoves his things haphazardly inside his bag and picks it up."
    show j 1 u watch at fdis
    "This time he gets up on his feet much more slowly and carefully."
    show j 1 u wince at fdis
    "He taps his feet on the ground a few times, almost as if he were testing something."
    j 1 u happy "\"Alright, no other problems. Good as new!\""
    mc 1 u sigh3 "\"You're most definitely not \"good as new\".\""
    j 1 u smile "\"I'll talk to you later, [povFirstName]-san. Have a good weekend.\""
    mc 1 u worried "\"Yeah, you too.\""
    play sound "music/slidingdoor.ogg"
    show j 1 u smile at offscreenright with moveoridis
    "..."
    "As he's leaving it occurs to me tha the didn't say a word about his performance on the exams."
    play sound "music/disappointment.ogg"
    "I really hope all that effort and terrible sleeping and eating habits weren't for nothing..."
    "I think I'm gonna try checking up on the others."
    "Keisuke is probably gonna be meeting up with his band members from now until the time when they go to the music store to rehearse."
    "I kinda feel like I'd be in the way so I'd rather not..."
    play sound "music/slidingdoor.ogg"
    stop music fadeout 2.5
    play music2 "music/BGM/On My Way.ogg"
    scene SClass with fade
    show minutes with dissolve
    $ renpy.pause(1.0)
    hide minutes with dissolve
    "I messaged Saya and Shoichi, wanting to talk to the two and see how they went with their tests."
    play sound "music/phonebeep.ogg"
    "Saya messaged me back less than a minute later saying we could talk for a bit before she had to leave for a shift at the diner."
    show s 1 u at fdis, three
    show sa 1 u talk at fdis, seven
    with dissolve
    "I quickly spot Saya sitting at her desk and talking to Shoichi who is standing right next to her."
    show sa 1 u at fdis
    mc 1 u talk "\"Oh, hey there. I didn't know you were gonna be here too, Shoichi. You didn't even read the message I sent you.\""
    s 1 u talk "\"You sent me a message? Sorry, I had my phone turned off so I didn't know.\""
    show s 1 u at fdis
    mc 1 u "\"What are you doing here?\""
    sa 1 u talk "\"He's been coming to my classroom every day the past week so we can talk about the exams and compare answers.\""
    mc 1 u worried "\"O-oh... I didn't know that. How come you didn't invite me?\""
    s 1 u sigh "\"I would have but you refused to keep studying with me so I didn't think you'd be all to interest in spending your free time after class doing more studying.\""
    sa 1 u think "\"It's more like reviewing instead of studying but he's still got a point.\""
    show sa 1 u at fdis
    mc 1 u considerate "\"Ah... sorry. I shouldn't have said anything.\""
    s 1 u "\"It's alright. Don't take it so seriously.\""
    mc 1 u talk "\"How did you two do by the way? I just tried talking to Jun before he went home and he was a mess... to put it lightly.\""
    sa 1 u considerate "\"Yeah, I know... I kinda ran into him being all zombie-like this morning. I saw him nearly walk straight into a column.\""
    mc 1 u sigh "\"...\""
    "I really shouldn't have let him go home all on his own."
    s "\"Hopefully he'll have done at least passably well.\""
    mc 1 u considerate "\"As in... getting the bare minimum to pass?\""
    s 1 u considerate "\"I don't think I can really ask for much more than that.\""
    "That's a fair point."
    "It's kinda sad how low our expectations are at this point..."
    sa 1 u laugh "\"By the way! A little birdie told me a little secret!\""
    mc 1 u sigh3 "\"Oh no... Shoichi, what the hell did you tell her?\""
    s 1 u wince "\"Wha- Why do you immediately think it's me? You don't even know what she's going to say!\""
    "Because whenever something like this happens you're usually the one blabbing to her so she can make fun of me."
    sa 1 u happy "\"Soooo, there's some really hot gossip going around the school that you've been spending a lot of time droning around the Light Music Club~\""
    "Oh no..."
    "Please don't tell me someone somehow figured out that Keisuke and I-{nw}"
    sa 1 u laugh "\"They've been saying you're interested in Ichigo-chan~\""
    show s 1 u shock at fdis
    mc 1 u shockb "\"What?!\"" with hpunch
    s "\"W-whoa. Is this true?\""
    show s 1 u wince at fdis
    mc 1 u wince "\"Of course it's not true! Who the hell told you that?!\""
    show s 1 u at fdis
    sa 1 u talk "\"Hmm? Really? I heard it from one of the girls in my class.\""
    mc 1 u sigh3 "\"Why are the girls in your class gossiping about me? I don't go to this class.\""
    sa "\"Yeah but Ichigo-chan does.\""
    mc 1 u shock "\"Wait, really?\""
    sa 1 u shock "\"You... you didn't know that?\""
    mc 1 u sigh "\"Of course not. Why would I ever need to know that?\""
    sa 1 u wry "\"So you're really not interested in Ichigo-chan?\""
    mc 1 u sigh "\"Not beyond a anthropological level, no.\""
    sa 1 u bored "\"Aww... that's a bummer...\""
    "A... bummer?"
    "Why are you getting so invested in something that doesn't even concern you?"
    "Let alone with absolutely zero confirmation?!"
    mc 1 u sigh3 "\"Dare I ask why exactly?\""
    sa 1 u considerate "\"It's just that it would have been the first time {i}you've{/i} ever been interested in a girl so I got excited for a second. Plus, I like Icchan too so it'd be nice if she became part of our group.\""
    "Icchan? Does anyone even call her that?"
    "Is that even Japanese?"
    mc 1 u sigh3 "\"Please spare me this kind of thing. I have no interest in her.\""
    sa 1 u bored "\"Aww...\""
    s "\"And here I thought that that could explain why you've been hanging out with Urushihara so much.\""
    mc 1 u sigh "\"I'm pretty sure the most simple explanation for that is because I wanted to hang out with him.\""
    sa 1 u talk "\"So you've just been hanging around the band because you wanted to spend time with Kei-chan?\""
    mc 1 u sigh "\"Of course! Why would you even think I'd have another reason?\""
    sa 1 u wry "\"W-well... I just thought he wouldn't have the free time for that anymore after the festival... {size=-4}guess nothing came out of his confession...{/size}\""
    show s 1 u shock at fdis
    "?!" with hpunch
    "I am immediately reminded something critical that I had forgotten."
    "Saya already knew Keisuke planned to confess to someone so me spending so much time with him, especially after the date of when he told her he was going to confess..."
    "She could end figuring it out thanks to that."
    s "\"Confession? Who's confession? Urushihara? T-to whom?!\""
    sa 1 u shock "\"Whoa, calm down there and breathe a little. What's gotten into you.\""
    show s 1 u worried at fdis
    "I can see the gears turning inside Shoichi's head."
    "I already thought that he'd gotten a little suspicious from the way he was acting when he ran into Keisuke at my place on Sunday."
    s "\"You said Urushihara was going to confess to someone? I didn't even know he had feelings for someone like that. W-who was he confessing to?\""
    sa 1 u wry "\"I don't know. Believe me, I tried to get him to tell me but he said he just wanted me to help him come up with words to say without me knowing who he was saying them too.\""
    sa 1 u sigh "\"And I really wanted to know cause it got me really curious.\""
    mc 1 u considerate "\"I-I don't think it's nice to pry into our friends' lives like that, don't you guys agree?\""
    sa 1 u bored "\"Booo. You're so boring sometimes. Just let me have fun.\""
    s 1 u considerate "\"R-right. Besides, nothing probably came off of it otherwise we'd have been told by now, right?\""
    sa 1 u talk "\"I'd sure hope so but Kei-chan can be really good at keeping secrets if he wants to.\""
    s 1 u worried "\"No kidding...\""
    show sa 1 u at fdis
    "Oh man... Shoichi's definitely suspicious."
    "If he hasn't figured it out it's just because he thinks there's no way something like that could happen."
    "But he's shooting me weird looks every now and again that make my skin crawl."
    "It definitely seems like he's onto something..."
    mc 1 u considerate "\"A-anyway, we came here to talk about the exams right? How did you guys fare? I just realized we kinda skipped that question.\""
    sa 1 u talk "\"Oh, right. I went well I suppose. I had a little bit of trouble with the world literature portion but other than that it was mostly fine.\""
    sa 1 u considerate "\"I... kinda skipped the syllabus for that one cause I got lazy.\""
    mc 1 u smile "\"Wow. And you have the guts to look me in the eye and say that {i}I{/i} don't study.\""
    sa 1 u pout "\"But you don't!\""
    show sa 1 u at fdis
    s 1 u considerate "\"I think I went fine for the most part. Social Studies is probably going to be my best grade though.\""
    sa 1 u talk "\"Really? I thought you hated Social Studies. What makes you so confident.\""
    show sa 1 u at fdis
    s 1 u smile "\"[povFirstName] studied with me for a bit on Sunday. It helped so much of it click in my head and the whole subject made a lot more sense after.\""
    s 1 u considerate "\"I really don't like subjects like that in general though. Especially sociology and philosophy. Everything is so... subjective. I really prefer things to be a bit more set in stone.\""
    mc 1 u talk "\"What did you expect from a subject that is basically the mad ramblings of a bunch of long dead old dudes from 5000 years ago or something?\""
    s 1 u sigh "\"The ancient Greeks are from 330BC.\""
    mc 1 u talk "\"Are you sure? Then what was it that happened 5000 years ago?\""
    s "\"I don't know. A lot of things probably, just not the ancient Greek philosophers.\""
    sa 1 u think "\"Hmm... I think 5000 years ago was around the time the ancient Egypt began developing.\""
    show sa 1 u at fdis
    s 1 u "\"Ah, that's true. I forgot about that one.\""
    mc 1 u wince "\"Ugh... I hate history. Too many dates to memorize.\""
    s 1 u sigh "\"You hate anything that makes you use your head.\""
    mc 1 u smile "\"Not entirely wrong.\""
    show s 1 u at fdis
    sa 1 u talk "\"What about you, [povFirstName]-kun? How do you think you did on the test?\""
    mc 1 u "\"I probably did fine. Not great but well enough to maintain my point average.\""
    s "\"Your point average is already stupidly high for someone that puts in no effort whatsoever.\""
    mc 1 u smile "\"Aww, thank you.\""
    s 1 u sigh "\"That wasn't a compliment. That was consternation.\""
    mc 1 u happy "\"I appreciate both.\""
    show s 1 u at fdis
    show sa 1 u happy at jumping, fdis
    sa "\"Hey, at least clubs will start operating again next week. I'm really itching to start practicing again.\""
    s 1 u worried "\"Oh... yeah, I forgot about that.\""
    sa 1 u shock "\"D-damn, I'm sorry, I totally forgot!\""
    show sa 1 u wry at fdis
    s 1 u considerate "\"It's fine. I have to get used to it sooner rather than later anyway.\""
    mc 1 u wince "\"Did something happen?\""
    sa 1 u sigh "\"Come on, [povFirstName]-kun... it's hard to stand up for you when you keep forgetting things like this.\""
    s 1 u worried "\"I'm gonna announce my retirement from the volleyball club next week.{nw}"
    show s 1 u considerate at fdis
    s " I'll announce who will be the club's new captain and then... that's it for my volleyball career.\""
    mc 1 u worried "\"O-oh... I'm so sorry, Shoichi.\""
    s 1 u smile "\"... It'll be fine. It's not like it's the end of the world, right? It's just volleyball.\""
    s 1 u happy "\"I'm mostly just going to miss having the frequent exercise and getting to spend time with the team. Other than that it's not a big deal.\""
    sa "\"If you say so...\""
    s 1 u smile "\"I do, so cheer up. I don't wanna see you looking so sad. It's just a high school club. It's not going to matter in five or ten years.\""
    mc 1 u sigh3 "\"I... guess that's one way to look at it.\""
    "A way that I really can't bring myself to agree with but..."
    "At the end of the day, Shoichi's feelings for volleyball are his own."
    "If he can see it as just a fun little hobby then that's his thing."
    "I could never think that way about tennis, even if I've spent the past few years running away from it."
    "It just doesn't click in my head."
    show s 1 u at fdis
    sa 1 u considerate "\"Uhm... I'm really sorry to cut out conversation short but I kind need to run otherwise I'll be late for my shift.\""
    s 1 u talk "\"Sure. Run along. I have other things I need to do too anyway.\""
    sa 1 u talk "\"You do?\""
    s 1 u smile "\"Yeah. Gonna swing by the student council room, work on expediting a few documents so there'll be one less thing to worry about next week. Pretty easy stuff.\""
    sa 1 u sigh "\"Just don't go overworking yourself.\""
    s 1 u happy "\"Hah, I wouldn't do something like that. You have my word.\""
    sa 1 u smile "\"Alright, see you boys later!\""
    s 1 u smile "\"Bye bye.\""
    mc 1 u talk "\"Have a good shift.\""
    stop music2 fadeout 2.5
    play sound "music/slidingdoor.ogg"
    show sa 1 u smile at offscreenright with moveoridis
    show s 1 u at fdis, five with move
    "She grabs and bag and almost literally runs out the door, slamming it loudly behind her."
    "That girl is way too full of enthusiasm."
    s 1 u considerate "\"I should probably get going too. The sooner I get my work done the sooner I get to have home and relax.\""
    mc 1 u worried "\"Right...\""
    "Shoichi walks to the door, his bag hanging from his shoulder and swaying with every step."
    "I watch his tail drooping between his legs."
    "For some reason, my chest feels a little bit tight."
    mc 1 u worried "\"Hey, Shoichi...\""
    s 1 u talk "\"Hmm? Yes?\""
    mc 1 u worried "\"You'd... tell me if there was anything going on with you... right?\""
    s 1 u considerate "\"Huh? What kind of question is that?\""
    mc 1 u wince "\"Just... if you were down or upset or... anything bad was going on... you'd let me know, right?\""
    s 1 u wry "\"Of course. You'd be the first one I'd tell.\""
    mc 1 u worried "\"Do you promise?\""
    s 1 u considerate "\"Yes, I promise. What, do you want me to pinky swear it too like we're back in fifth grade?\""
    mc 1 u considerate "\"N-no. I was just thinking some stuff and wanted to make sure, that's all.\""
    s 1 u wry "\"Sheesh, don't be such a weird. I'll talk to you later.\""
    mc 1 u wry "\"See ya.\""
    play sound "music/slidingdoor.ogg"
    show s 1 u wry at fdis, offscreenright with moveoridis
    "..."
    "For some reason I don't feel good..."
    "I... kinda want to go home right now..."
    "No no. I have to shake this weird feeling off."
    "I still want to meet up with Keisuke."
    "I did promise we'd see each other on Friday after the tests."
    "And maybe we could make plans for that date he said he wanted to take me to."
    "... Heh, it's a little embarrassing to be looking forward to this kind of stuff."
    "God, it's so weird to think that I have feelings for someone... much less a guy."
    play sound "music/disappointment.ogg"
    "My life is turning out so weird lately..."
    play music2 "music/BGM/The People Here.ogg" fadein 5.0
    scene SCorridor
    show ka 1 u smile at fdis, zero
    show i 1 c smile at fdis, two
    show k 1 u at fdis, four
    show ku 1 c smile at fdis, six
    show mi 1 c smile at fdis, eight
    show sh 1 c at fdis, ten
    with fade
    "I make my way to the band's clubroom but as soon as I reach the hallway, I find them all gathered in front of the room, sitting and standing around chatting."
    k 1 u smile "\"Ah, [povFirstName]! There you are!\""
    mc 1 u talk "\"There who is where?\""
    k 2 u gentle "\"I was wondering if you were going to show up.\""
    mc 1 u considerate "\"You were expecting me?\""
    ku "\"You've kinda been showing up out of the blue a lot of the time so we've kinda started to expect at this point.\""
    mc 1 u sigh "\"Come on, it hasn't been that often. Maybe a handful of times at the most.\""
    ka "\"It's alright, you shouldn't be embarrassed or selfconscious about it. It's nice to have a friendly face that isn't necessarily a band member.\""
    i "\"I thought that was already Kei-chan's job.\""
    k 1 u sigh "\"Hysterical.\""
    show k 1 u at fdis
    mc 1 u talk "\"Are you guys going to go to the store to rehearse again today?\""
    k 1 u smile "\"Yeah, but that's a few hours away still. We're all going to head home before we go for it.\""
    mc 1 u sigh "\"Really? I thought you'd all head there together from school.\""
    k 1 u sigh "\"Are you kidding? Rehearsal starts at 8PM. There's no way we'd hang around doing nothing for four hours just so we could head there together.\""
    sh "\"It's not very efficient.\""
    mi "\"Or smart.\""
    mc 1 u considerate "\"Okay okay, I got it. I'm stupid.\""
    i "\"No one said that.\""
    mc 1 u talk "\"So what are you guys doing here right now then?\""
    mi "\"We were just celebrating the end of the exams and how we all got through it in one piece.\""
    ku "\"Some more than others...\""
    "The monkey sighs, leaning his back against the wall."
    ku "\"My parents are going to really get on my ass if I don't score high enough in these.\""
    k 1 u sigh "\"I did tell you to study. I tried to help you study. You wanted nothing to do with it.\""
    ku "\"You could have pushed me a little more! You know, been more insistent!\""
    k 1 u sigh2 "\"What am I, your mother?\""
    mc 1 u smile "\"You certainly look very young for your age, Miss.\""
    k 1 u sigh "\"Go to hell.\""
    i "\"We were all about to head home anyway so if you want to you can already pick Kei-chan up.\""
    k "\"Please stop calling me that. I've asked you multiple times.\""
    show k 1 u at fdis
    ka "\"Everyone, just make sure you're all in time. Even if we're sharing the cost six ways those soundproof rooms are still very expensive so I'd rather not waste any time.\""
    mi "\"Yeah, Kurusu. Don't be late again!\""
    show ku 1 c smile at fdis, jumping
    ku "\"I told you I was helping an old lady cross the street!\""
    sh "\"You're always helping someone do something and you always end up being late.\""
    show ku 1 c smile at fdis, fidget
    ku "\"I'm not gonna give up on my basic decency just to save some time!\""
    i "\"Alright, we'll disband for now. See you all at 8PM!\""
    ku "\"Cheers.\""
    mi "\"Gotcha.\""
    sh "\"Bye bye.\""
    k 1 u smile "\"See you in a few.\""
    show ka 1 u smile at fdis, offscreenleft
    show i 1 c smile at fdis, offscreenleft
    show ku 1 c smile at fdis, offscreenleft
    show mi 1 c smile at fdis, offscreenleft
    show sh 1 c at fdis, offscreenleft
    with moveoridis
    show k 1 u smile at fdis, fiveh with move
    "The band members all go on their ways, heading in different directions down the hallway."
    "I suppose some of them might still have business in the building?"
    k "\"Heh. I have to admit, part of me was expecting you to head straight home after school.\""
    mc 1 u considerate "\"I considered it but I thought you might want to see me.\""
    k 2 u gentle "\"You thought right.\""
    show k 2 u gentleb at fdis:
        ease .2 zoom 1.5 xoffset -30 yoffset 200
    play sound "music/fabric.ogg"
    "Keisuke takes a quick step towards me and before I can react, plants a peck on my cheek before nuzzling against my neck."
    mc 1 u flustered "\"W-whoa. W-we're in public.\""
    k "\"Don't worry, everyone's already left.\""
    play sound "music/chu.ogg"
    show k 1 u smile at fdis:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    "He gives me another kiss, this time on my neck, before stepping away again."
    k "\"That's just my way of telling you I missed you this week.\""
    mc 1 u avoidb "\"I-I missed you too.\""
    k 2 u gentle "\"Hehe, you look so cute when you're red.\""
    mc 1 u sigh "\"I object to this entire conversation.\""
    k 1 u smile "\"You love saying that don't you?\""
    mc 1 u sigh "\"Maybe...\""
    k 1 u smile "\"I'll admit, I'm happy you came over. Even if we might not have that much time together.\""
    mc 1 u wince "\"We won't?\""
    k 1 u sigh "\"Sadly we won't... I need to go home. My father wanted me home straight away once tests were finished so we could talk about my academics or something like that.\""
    mc 1 u worried "\"That sounds like a pain in the ass.\""
    k 1 u wry "\"Eh. It could be worse. For better or worse I'm used to it. It was one of his demands if I wanted to be allowed to go to this school.\""
    mc 1 u wince "\"You had to be allowed to go here?\""
    k 1 u sigh "\"Yeah... I know this is a really good school and all but... do you really think someone of my... {i}birth{/i} would usually go to a place like this?\""
    mc 1 u wince "\"I... I guess I always wondered about that a little bit.\""
    k 1 u "\"I had my own reasons for wanting to go here but that went against my father and grandmother's plan so it was a lot of struggle to get them to agree to it.\""
    k 1 u sigh "\"Of course, the agree came with several strings attached. One of them is that I always keep them updated on my studies and that I study a lot at home to make up for the... \"deficiencies\" of lower grade education.\""
    k 1 u avoid "\"Ugh. Just saying that out loud already has me annoyed.\""
    stop music2 fadeout 2.5
    "I never knew about that."
    "I mean, I guess I never asked so it's only fair that he didn't tell me but still."
    "I did always think it was a little strange that someone coming from such a rich family would be in this school."
    "It is a private school and all and a very prestigious one at that but far from the sort of place I'd imagine the son of a worldwide company CEO to attend."
    play music2 "music/BGM/Thinking of You Loop.ogg" fadein 5.0
    mc 1 u talk "\"Why did you even choose to come to this school anyway?\""
    k "\"That's... it's a bit...\""
    k 1 u sigh "\"... Alright, I'll tell you. Just... don't laugh at me, okay?\""
    mc 1 u wince "\"Uhm... okay?\""
    k 2 u sigh "\"Just... just remember I cheered you up when Aki was making fun of you about wanting to be more like me. Remember I didn't... make fun of you or anything.\""
    mc 1 u sigh "\"Yes, I remember that. Just spill the beans already!\""
    k 1 u worried "\"Right. Sorry, I'm rambling.\""
    k 1 u wry "\"So... back when I was graduating from Junior High, I was still very much an unknown player. I wasn't even considered particularly strong in the prefecture, let alone the region or the country.\""
    k 2 u sigh "\"And back then, there was this player I really admired a lot. I loved watching his matches. I thought his confidence was... magnetic. I'd admired him for years, really.\""
    k 1 u avoid "\"... You see where I'm going with this, right?\""
    mc 1 u shock "\"O-oh... wait, you came to our school for me?\""
    k 1 u worried "\"... Are you going to be creeped out if I say yes?\""
    mc 1 u considerate "\"Maybe just a little bit.\""
    k "\"Ugh...\""
    mc 1 u smile "\"Still, I'm actually kinda flattered. You acted like you had no idea who I was when you first joined the tennis club though.\""
    k 1 u considerate "\"Of course I did. Do you have any idea how embarrassing it would be if I joined the club and immediately started gushing over you? How uncool would that be?\""
    mc 1 u happy "\"Haha, I don't know. We might have started hanging out earlier if it wasn't for that.\""
    k 1 u wry "\"Hmm... maybe. But I have to say, I don't regret having our relationship take the trajectory it took.\""
    k 1 u calm "\"I'm happy with where we are now, even if it's just at the very start.\""
    mc 1 u considerate "\"You're really sappy today aren't you?\""
    k 2 u gentle "\"Hehe.\""
    k 1 u smile "\"I guess in a way I've been interested in you from the very start... just not always romantically.\""
    mc 1 u considerate "\"Aww man, I don't really know how to react to this. I wish I could say the same but I had no idea who you were when we first met.\""
    k 2 u gentle "\"Ahahaha, I wouldn't have expected you to know.\""
    k 1 u smile "\"One thing that I always liked when I watched you play is how you always seemed really humble and yet above everything at the same time.\""
    k 2 u gentle "\"Like... you didn't look down on other players but you didn't really feel obligated to act super chummy with them just for the sake of keeping a good image.\""
    k 1 u smile "\"You've always been really unapologetically you. That's something I really respect.\""
    mc 1 u considerate "\"It's definitely gotten me in trouble it's fair share of times though.\""
    k 2 u gentle "\"Yeah, I'll bet it did.\""
    k 1 u wry "\"Anyway, I really need to get going now. I'll try to text you before rehearsal.\""
    mc 1 u smile "\"Okay. Hopefully you'll have a good day still.\""
    k 1 u calm "\"I got to see and talk to you. It's alright a pretty good one.\""
    mc 1 u considerate "\"You're a flatterer aren't you?\""
    k 2 u gentle "\"I try.\""
    show k 1 u smile at fdis
    play sound "music/fabric.ogg"
    "Keisuke grabs my hand, giving it a quick gentle squeeze."
    k "\"I'll see you later.\""
    show k 1 u smile at fdis, offscreenleft with moveoledis
    "Keisuke walks down the hallway, disappearing when he turns the corner to go down the stairs."
    "I watch him go with a big, goofy smile on my face."
    "Leaning against the hallway window, I stare at the campus grounds, watching to see when he leaves the building."
    "I watch his tiny little figure downstairs making its way out of the campus while idly touching the spot on my neck that he had kissed."
    "I have... butterflies in my stomach."
    "This is such a nice feeling to have... no wonder Saya-chan was excited at the idea of me falling for someone."
    "I guess it just didn't work out the way she thought it would."
    stop music2 fadeout 2.5
    stop music fadeout 2.5
    $ date = None
    scene PatreonKeisuke with fade
    "WOTB: Hey guys, hope you all enjoyed this demo of Tennis Ace."
    "WOTB: As you guys may or may not already know, all development in Tennis Ace is possible thanks to all my amazing patrons and other supporters who make it possible for me to dedicate the time to work on the game as well as commission the art for it."
    "WOTB: If you haven't already (and if you're able) maybe you could consider help to support us too! Just click {a=https://patreon.com/tennisace}{color=#3badff}here and you'll be taken right to our Patreon!{/color}{/a}"
    "WOTB: Once again, thank you all and we'll see each other with the next demo!"
