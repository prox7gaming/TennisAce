label Day13_Jun:
    $ persistent.picked_character = "Jun"
    window hide
    scene May21 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    play music2 "music/BGM/The People Here.ogg" fadein 5.0
    scene Cafe with fade
    window show
    $ date = "day13"
    "Today I've been called here to this café by a friend."
    "He's noticed how stressed I've been lately and decided to try and help me destress."
    "I have to say, I truly appreciate the thought."
    "We've only been here for a little while and I have to say that I definitely feel better."
    "Who knew talking could be so therapeut-"
    show s 1 c sigh at fdis, five
    s "\"[povFirstName], are you even paying attention to what I'm saying?\""
    mc 1 c wince "\"Oh, sorry, what?\""
    s "\"Jeez, here you go spacing out again.{nw}"
    show s 1 c at fdis
    extend " It's like you were a thousand miles away.\""
    mc 1 c considerate "\"Sorry sorry. I guess I was a little lost in thought.\""
    show s 1 c think at fdis
    s "\"No kidding.\""
    "Yes, Shoichi was the one to invite me here."
    "He called me early this morning and asked me if I'd like to meet him here for lunch."
    "I was a little skeptical of the idea but now I'm glad that I came."
    mc 1 c smile "\"Okay, I'm back now. What were you saying again?\""
    show s 1 c sigh at fdis
    s "\"Are you sure? I don't really feel like talking to a wall again.\""
    mc 1 c considerate "\"It's not gonna happen again, I swear.\""
    show s 1 c think at fdis
    $ renpy.pause(1.0)
    show s 1 c smile at fdis
    s "\"If you say so then I guess it's okay.\""
    s "\"Anyway, I was asking how your class' preparations for the festival were going. It's already right around the corner.\""
    mc 1 c think "\"It was kind of a mess at first. No one could really agree on anything.\""
    mc 1 c smile "\"In the end, everyone decided to open a little restaurant. Gin insisted on the idea and since we had nothing better planned, we went with it.\""
    show s 1 c at fdis
    s "\"What kind of food will you guys be serving?\""
    mc 1 c think "\"I think it was supposed to be Sichuan cuisine but I don't remember now. I just know it was supposed to be traditional Chinese food. You'll have to ask Gin if you want more details.\""
    show s 1 c smile at fdis
    s "\"If it's him then I'm sure it'll be okay. That guy's knowledge of food can put critics to shame.\""
    mc 1 c happy "\"He certainly is no regular glutton.\""
    show s 1 c considerate at fdis
    s "\"Calling him a glutton is a little insensitive though...\""
    mc 1 c smile "\"Oh come on, it's not like he's here to hear it.\""
    s "\"You really can be mean when people aren't listening, huh?\""
    mc 1 c wince "\"W-what? I'm not mean.\""
    show s 1 c smile at fdis
    s "\"Hehe, don't worry. I'm just yanking your chain.\""
    mc 1 c sigh2 "\"Is that so?\""
    "I can't even tell anymore."
    show s 1 c happy at fdis
    s "\"Since you guys will be working on a restaurant, does that mean I'll get to see you in an apron?\""
    mc 1 c sigh "\"In your dreams. I bailed out on it as fast as I could. I'm helping with the decor, organization and shopping and that's it.\""
    show s 1 c sad at fdis
    s "\"Aww, must you trample on my dreams like that?\""
    mc 1 c sigh2 "\"Don't give me the puppy dog eyes now...\""
    show s 1 c happy at fdis
    s "\"Busted, huh?\""
    "With a lighthearted conversation like this, it's hard to believe the kinds of things that have been happening lately."
    "In fact, just thinking about it already gives me a sinking feeling in my chest..."
    "But I promised Shoichi that we'd have some fun today so I don't want to let anything get in the way."
    show s 1 c smile at fdis
    play sound "music/shopbell.ogg"
    "Clerk" "\"Welcome, sir. We are full at the moment but if you'll be patient, a table should clear out for you in a few minutes!\""
    "Since we're so close to the entrance, it's hard not to hear when someone walks in."
    s "\"By the way-\""
    ukn "\"Hey, aren't you...\""
    stop music2 fadeout 2.5
    play music3 "music/BGM/On My Way.ogg" fadein 5.0
    show s 1 c at fdis, seven with move
    show aku 1 c smile at three with move
    aku "\"You are, you're the guy that was with Kobayashi back at the piano competition!\""
    "This lion walks right up to us, interrupting our conversation."
    s "\"You know this guy, [povFirstName]?\""
    mc 1 c think "\"Well...\""
    menu:
        "I don't remember":
            mc 1 c considerate "\"Sorry, I don't really remember...\""
            "Without missing a beat, the lion smiles again."
            aku "\"I wouldn't expect you to. I traded a few words with Kobayashi over a month ago and you just happened to be with him. No one would expect you to remember something like that.\""
            show s 1 c at fdis
            s "\"But apparently you do.\""
            aku "\"Well, not to toot my own horn but I have excellent memory.\""
            show s 1 c smile at fdis
            s "\"It must be useful to have something like that... maybe if [povFirstName] had it, he'd be able to recall stuff beyond what he ate yesterday for lunch.\""
            mc 1 c sigh "\"Excuse you, my memory doesn't stop at my dinner two days ago!\""
            s "\"Oh, sorry. Lunch two days ago?\""
            mc 1 c avoid "\"... Yesterday's lunch.\""
            show s 1 c happy at fdis
            s "\"Oh, you had a chance to exceed my expectations and you failed miserably. Kudos!\""
            mc 1 c sigh2 "\"Shut up...\""
            aku "\"Pfft...\""
            "Great, now the lion is trying to hold back his laughter."
            mc 1 c avoid "\"Since you seem to know a bit more about me than I do you, would you mind introducing yourself?\""
            aku "\"Oh, right, sorry about that. My name is Shinji Akutagawa. I guess you could say I'm Kobayashi's rival.\""
            show s 1 c smile at fdis
            s "\"Well, fancy that. I think I remember mentions of you back at the competition.\""
            aku "\"I'd certainly hope so given that Kobayashi had to change his set list just to deal with me.\""
            show s 1 c think at fdis
            s "\"Oh yeah, that did happen didn't it?\""
        "I remember":
            mc 1 c talk "\"Yeah. I met him when Jun and I were waiting for you guys back at the piano competition.\""
            mc 1 c think "\"Come to think of it, he even talked to us after the competition was over and I'm pretty sure you were with us. Don't you remember?\""
            show s 1 c sigh at fdis
            s "\"You really expect me to remember someone I saw once over a month ago?{nw}"
            show s 1 c at fdis
            extend " If anything, I'm surprised {i}you'd{/i} remember.\""
            mc 1 c sigh "\"My memory isn't that bad. You don't need to be so surprised.\""
            "The lion looks between the two of us with a smile on his face."
            mc 1 c curious "\"Your name... Akutagawa, right? Sorry if I got it wrong, I'm not really good with names.\""
            aku "\"It's alright, and you remembered it correctly. To be honest, I never introduced myself when we met so you even knowing my name at all is already surprising.\""
            mc 1 c considerate "\"It's hard to forget a guy who delivers a full-blown villain speech in broad daylight.\""
            aku "\"F... full-blown villain speech?\""
            mc 1 c judge "\"I will make sure the name Shinji Akutagawa is one you'll never forget!\""
            mc 1 c talk "\"It was something like that.\""
            show aku 1 c at jumping
            aku "\"Huh?! Y-y-you remember that? No. Forget it. Forget it right this instant!\""
            show s 1 c happy at fdis, shake1
            s "\"Pfft...{w}"
            show s 1 c laugh at fdis, shake1
            extend " Ahahahahahahahahaha! No way, he really said that?\""
            aku "\"S-shut up. Just forget I ever said anything like that!\""
            mc 1 c considerate "\"Sorry... asking me to forget that scene is a little...\""
            "I don't want to say the word \"impossible\" but no better word comes to mind..."
            aku "\"Guh...\""
    show s 1 c smile at fdis
    s "\"Well, either way, it's good to meet an acquaintance of Jun's. My name is Shoichi Urata. We go to the same school.\""
    mc 1 c smile "\"And I'm [povName]. I sit next to Jun in class.\""
    aku "\"It's a pleasure to meet you. To be honest, I didn't know Kobayashi had any friends outside of the competitors we knew as children.\""
    show s 1 c at fdis
    s "\"Why is that?\""
    aku "\"Well, I might be a bit biased since I never got to see how he acted out of the competitions but he was always very focused and withdrawn. He didn't goof around much like the rest of us did.\""
    mc 1 c think "\"I'd certainly expect to see a bunch of children goofing off, even if they're facing against each other in a competition.\""
    mc 1 c "\"It's not that different from the tennis tournaments in that sense. The children's tournaments are a lot more relaxed.\""
    aku "\"Right. But he never really mingled with us so I just thought he wasn't the type of person to have any friends.\""
    show s 1 c think at fdis
    s "\"That doesn't sound at all like the Jun we know.\""
    mc 1 c considerate "\"Yeah... saying that he's a goofball would probably be putting it lightly.\""
    show s 1 c considerate at fdis
    s "\"True...\""
    show s 1 c at fdis
    aku "\"By the way, isn't he with you guys right now?\""
    mc 1 c "\"Nah. He's on bed rest right now. He was actually in the hospital up until a few days ago.\""
    "The lion's eyes immediately go wide in shock."
    aku "\"Wha- No way. Don't tell me it happened again?\""
    show s 1 c avoid at fdis
    mc 1 c shock "\"Again? What happened again? Did something happen to him before?\""
    aku "\"Ah...\""
    "As soon as he sees the look on my face, Akutagawa looks away from me."
    aku "\"It's nothing. Forget I said any-\""
    mc 1 c annoyed "\"Forget you said anything? It's a little late for that isn't it? What are you talking about?\""
    s "\"[povFirstName], that's enough.\""
    mc 1 c annoyed "\"What do you mean that's enough? Aren't you the least bit curious about this? He basically just said that Jun was in a hospital before too!\""
    s "\"We all know Kobayashi has a frail health. Would it really be all that surprising for him to have visited a doctor before?\""
    mc 1 c annoyed "\"Don't play that game with me. We both know when someone sees that a person was in the hospital that means they were admitted to it, not just getting a check-up.\""
    show s 1 c sigh at fdis
    s "\"Even so. Whether that's true or not, don't you think that's up to Jun to tell us. You shouldn't go prying into other people's pasts.\""
    mc 1 c avoid "\"But...\""
    "That bad feeling I've been having up to now returns with force."
    mc 1 c annoyed "\"Akutagawa-san, won't you please tell me what you meant by that \"again\" comment?\""
    aku "\"I-it's really not my place...\""
    mc 1 c angry "\"So you're saying he was admitted to a hospital once before?\""
    aku "\"I-\""
    show s 1 c scorn at fdis
    s "\"{size=+2}[povFirstName]!{/size}\"" with hpunch
    "!?"
    show s 1 c sigh at fdis
    s "\"There are people staring at us, man. Let it go already...\""
    "When I look around us, I see the people in the other surrounding tables all staring at us."
    mc 1 c avoidb "\"Crap...\""
    s "\"You really don't think sometimes...\""
    "How am I supposed to think?"
    "So Jun has been in a hospital before?"
    "Now I have a ton of questions swimming in my mind..."
    aku "\"I'm sorry, I really shouldn't have said anything.\""
    show s 1 c wry at fdis
    s "\"Don't worry about it. You didn't know.\""
    aku "\"Why was he admitted to the hospital if you don't mind telling me?\""
    show s 1 c at fdis
    s "\"He tripped during practice and hit his head on the corner of the piano.{nw}"
    show s 1 c considerate at fdis
    extend " There was a little bleeding but it wasn't all that serious. He was in and out of the hospital in very little time.\""
    aku "\"Ah, I see...\""
    show s 1 c at fdis
    "Waitress" "\"Sir, we have a table open for you now.\""
    "One of the staff members calls out to Akutagawa."
    aku "\"Oh, thank you very much, I'll be right there!\""
    "The lion turns to us again."
    aku "\"Do tell Kobayashi that I send him my best regards and hope he'll be well, okay?\""
    show s 1 c smile at fdis
    s "\"Of course.\""
    show aku 1 c smile at offscreenleft with moveoledis
    show s 1 c at fdis, five with move
    s "\"...\""
    "Once Akutagawa leaves, the two of us fall completely silent."
    show s 1 c wry at fdis
    s "\"I can see the gears in your head turning you know.\""
    mc 1 c worried "\"...\""
    show s 1 c sigh at fdis
    s "\"Silence, huh?\""
    show s 1 c considerate at fdis
    s "\"I guess your good mood is ruined no matter how I look at it, right?\""
    mc 1 c worried "\"... Sorry.\""
    show s 1 c wry at fdis
    s "\"It's okay. There's nothing wrong with being worried about a friend. In fact, it's a good thing.\""
    show s 1 c considerate at fdis
    s "\"Just make sure you don't let it completely eat you up from the inside.\""
    show s 1 c smile at fdis
    s "\"Well, we've already finished eating anyway. Would you like to just call it quits early and head home?\""
    mc 1 c shock "\"You'd be okay with that?\""
    show s 1 c sigh at fdis
    s "\"What the hell do you take me for? You think I'd be mad if you weren't feeling up to it anymore? I'm more worried about how you feel than about a little failed hang out.\""
    mc 1 c wince "\"I-I see...\""
    mc 1 c wry "\"Then... I guess I'm gonna head home after all.\""
    show s 1 c happy at fdis
    s "\"Alright, let me just get the check so we can be on our way.\""
    stop music3 fadeout 2.5
    scene Street2
    show s 1 c at fdis, five
    with fade
    play music "music/crowd01.ogg" fadein 5.0
    "We walk out into the streets."
    "The crowd that comes with rush hour had just begun to die down but it was still full of people everywhere."
    show s 1 c smile at fdis
    s "\"Well, I guess I'm gonna take this opportunity to go grocery shopping. I have to start stocking on the foods my dad likes to eat now after all.\""
    mc 1 c worried "\"Sorry for cutting our time together short.\""
    show s 1 c considerate at fdis
    s "\"Don't be ridiculous. I'm the one who offered it.\""
    show s 1 c smile at fdis
    s "\"Tell Jun I said hi, okay?\""
    mc 1 c shock "\"H-huh?!\""
    show s 1 c happy at fdis
    s "\"You heard what I said.\""
    show s 1 c smile at fdis
    s "\"See ya.\""
    show s 1 c smile at fdis, offscreenright with moveoridis
    "..."
    mc 1 c sigh2 "\"So he knew I wanted to go see Jun, huh?\""
    "He could have just said so from the start."
    "Idiot."
    "..."
    "It might be bad for me to just show up to ask him stuff from his past out of the blue..."
    mc 1 c worried "\"... maybe I should bring some sort of gift with me?\""
    "Great, now I've started talking to myself."
    stop music fadeout 2.5
    scene JunBedroom with fade
    play sound "music/door2.ogg"
    yui 1 c smile "\"Jun, darling, you have a visitor.\""
    show j 1 c watch at fdis, five with dissolve
    j "\"A visitor?\""
    show j 1 c shock at fdis
    play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    j "\"[povFirstName]-san?\""
    mc 1 c smile "\"Heya.\""
    j "\"What are you doing here?\""
    mc 1 c considerate "\"What, can't I want to check up on a friend?\""
    show j 1 c wince at fdis
    j "\"You can, but that's the kind of thing you'd usually warn people about beforehand.\""
    mc 1 c wince "\"Sorry, am I getting in the way of something.\""
    show j 1 c considerate at fdis
    j "\"No no, of course not. I'm just surprised you dropped by, that's all.\""
    mc 1 c considerate "\"Ah... I see...\""
    show j 1 c watch at fdis
    j "\"...\""
    j "\"Are you... alright?\""
    mc 1 c shock "\"H-huh? O-of course I'm alright. Why do you ask?\""
    show j 1 c considerate at fdis
    j "\"I guess... I just got a feeling?\""
    mc 1 c wince "\"A... feeling?\""
    show j 1 c wry at fdis
    j "\"Yeah. What with you showing up all of a sudden and looking a bit down... I just got the feeling that something was up.\""
    mc 1 c worried "\"...\""
    "He really is more perceptive than I give him credit for."
    mc 1 c considerate "\"It's alright, you don't have to worry about me.\""
    show j 1 c think at fdis
    j "\"If you say so.\""
    show j 1 c smile at fdis
    j "\"Well, since you're already here, why don't we sit down and chat for a bit?\""
    show j 1 c watch at fdis
    j "\"?!\""
    j "\"What's that plastic bag you've got with you?\""
    mc 1 c shock "\"Oh, right!\""
    mc 1 c happy "\"Here, I bought these for you. It's some of your favorite sweets and a few savory snacks.\""
    show j 1 c wry at fdis
    j "\"O-oh... I see. You bought me more stuff...\""
    mc 1 c annoyed "\"... What's with that face that says you don't like what you see?\""
    show j 1 c considerate at fdis
    j "\"N-no, it's not that!\""
    show j 1 c wry at fdis
    j "\"It's just... you've been doing so much for me lately...{nw}"
    show j 1 c considerate at fdis
    extend " {cps=*0.5}It makes me feel guilty...{/cps}\""
    mc 1 c shock "\"Guilty? Why would it make you feel guilty?\""
    j "\"I mean... I can't really do anything for you in return, right?\""
    mc 1 c shock "\"?!\""
    show j 1 c wry at fdis
    j "\"I don't really have money to spare so I can't buy you your favorite snacks, or give you a present like that keychain.\""
    show j 1 c considerate at fdis
    j "\"{cps=*0.5}Even if it's something cheap, I still can't do it...{/cps}\""
    mc 1 c annoyed "\"Who says you have to give me anything in return?\""
    show j 1 c shock at fdis
    j "\"Huh?\""
    mc 1 c avoidb "\"... I'm just doing this because I want to. Don't think too much about it.\""
    j "\"...\""
    show j 1 c happy at fdis
    j "\"Hehe, [povFirstName]-san, you're kinda cute when you're embarrassed.\""
    mc 1 c sigh2 "\"Just shut up and take the bag already...\""
    j "\"Okay.\""
    show j 1 c shockb at fdis
    j "\"Oooh, cheese crackers!\""
    mc 1 c "\"Oh, yeah. I just picked them up at the grocery store on a whim. You like them?\""
    show j 1 c happy at fdis
    j "\"Yeah. I love cheese almost as much as I love sweets.\""
    mc 1 c happy "\"That's great then!\""
    "Jun puts the bag on top of his desk, tucking it away into a corner."
    mc 1 c curious "\"You're not gonna eat it?\""
    show j 1 c considerate at fdis
    j "\"Not while I have a guest over. That'd be impolite.\""
    show j 1 c watch at fdis
    mc 1 c talk "\"I never took you for the kind of person to worry about politeness.\""
    show j 1 c considerate at fdis
    j "\"Seriously, what kind of person do you take me for?\""
    "An adorable air-head with questionable common sense?"
    "... Wait, did I just call another guy \"adorable\"?"
    "..."
    mc 1 c considerate "\"Never mind...\""
    show j 1 c shock at fdis
    $ renpy.pause(1.0)
    show j 1 c bored at fdis
    j "\"You just thought of something bad, didn't you?\""
    play sound "music/stab.ogg"
    mc 1 c wince "\"N-no way!\"" with hpunch
    show j 1 c think at fdis
    j "\"Well, never mind that.{nw}"
    show j 1 c smile at fdis
    extend " What would you like to do?\""
    "Quick to switch gears as always..."
    "I swear, sometimes the things he says aren't good for my heart..."
    mc 1 c sigh2 "\"Err... let me recompose myself for a bit...\""
    show j 1 c watch at fdis
    j "\"Huh? Recompose yourself? What do you mean?\""
    mc 1 c worried "\"Not everyone is as quick to switch gears like you, you know...\""
    j "\"Switch gears?\""
    "He's hopeless... and I don't know why I'm surprised."
    mc 1 c "\"By the way, what have you been doing for the past few days that you've been cooped up here?\""
    show j 1 c think at fdis
    j "\"Well... I haven't been allowed to touch the piano so I've just-\""
    mc 1 c confused "\"Wait, you can't play the piano? Why? What would be the problem with that?\""
    show j 1 c shock at fdis
    j "\"Oh!{nw}"
    show j 1 c considerate at fdis
    extend " Uhm... err... I guess they just don't want me to move around too much.\""
    "He's a terrible liar!"
    "... But the question is, even if I know he's lying, should I let him know that I know?"
    "There's no telling how he might react if I ask for clarification."
    menu:
        "Press further":
            $ pressjun += 1
            stop music2 fadeout 2.5
            "..."
            "I hope this doesn't blow up in my face."
            mc 1 c judge "\"Jun-kun...\""
            show j 1 c shock at fdis
            j "\"-kun? Why are you calling me like th-\""
            mc 1 c sigh2 "\"You're a terrible liar, you know.\""
            play sound "music/stab.ogg"
            show j 1 c wince at fdis, shake1
            j "\"L-liar?\""
            mc 1 c sigh "\"Just now you couldn't even look me in the eye. Not only that, you were completely at a loss for what to say. It sounded like you were trying to come up with an excuse on the spot.\""
            j "\"N-no, that's not...\""
            mc 1 c avoid "\"Come on, is it really something you can't tell me? I thought we were friends.\""
            j "\"C-come on, don't say that, we are friends... it's just...\""
            "I feel like a major tool for pulling out the friend card at a time like this but if I'm going to push him for information then I might as well go all the way."
            "Jun, sorry, I'm gonna be a merciless for a bit..."
            j "\"...\""
            show j 1 c avoid at fdis
            j "\"F-fine, I'll tell you. {size=-2}Stop looking at me like that...{/size}\""
            "!"
            "It worked?"
            show j 1 c wince at fdis
            j "\"... My parents are afraid it could happen again...\""
            mc 1 c shock "\"Happen again? You mean the same accident as before? Isn't that a little unrealistic?\""
            show j 1 c considerate at fdis
            j "\"Y-yeah... you're totally right.\""
            "..."
            "I'm still not totally convinced."
            "I feel like he's still hiding something."
            "Does this have anything to do with what Akutagawa said?"
            "..."
            "Just from the look on his face I can already tell that I shouldn't say anything further."
            "He already looks pretty overwhelmed as is."
            "I... I'll let it go for now..."
            "I don't want to pile stress onto him while he's supposed to be recovering from an injury."
            mc 1 c avoid "\"I see... sorry to have pushed you.\""
            show j 1 c wry at fdis
            j "\"...\""
            "Ah... I think I've completely ruined his mood..."
            play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
        "Let it go":
            "No... as much as I want to know what's going on, I also remember how angry he can get when pushed."
            "Shoichi said it himself, I shouldn't pry too much..."
            "... Ugh, being reasonable sucks..."
            mc 1 c worried "\"Well, I guess that's kind of a valid reason...\""
            "It really isn't..."
            j "\"Y-yeah. It's a bit unreasonable, isn't it?\""
            mc 1 c curious "\"If you haven't been able to play the piano, what have you been up to recently?\""
            show j 1 c wry at fdis
            j "\"Mostly just playing games and doing some light reading.\""
            show j 1 c happy at fdis
            j "\"Sora-kun actually loaned me a couple more games before I got discharged from the hospital so I've at least had something to do.\""
            show j 1 c think at fdis
            j "\"Other than that, Ayako-san has been dropping by some notes and the homework I need to do to keep up with our classes.\""
            "!?"
            show j 1 c watch at fdis
            j "\"What's with that surprised look on your face?\""
            mc 1 c considerate "\"No, it's nothing.\""
            "... I totally forgot to take notes for him. That's something I could have been doing to help."
            mc 1 c considerate "\"Sorry...\""
            show j 1 c shock at fdis
            j "\"Huh? What for?!\""
            "For being an idiot..."
            mc 1 c considerate "\"Never mind that...\""
            mc 1 c "\"What kinds of games have you been playing?\""
            show j 1 c think at fdis
            j "\"Well, Sora-kun brought me a lot of stuff to play with.\""
            show j 1 c smile at fdis
            j "\"Other than the occasional sports title, it was mostly fantasy games and RPGs.\""
            mc 1 c smile "\"Oh. That's right up your alley then.\""
            show j 1 c happy at fdis
            j "\"Yup!\""
            show j 1 c think at fdis
            j "\"I've only tried two so far because... well, RPGs aren't the kind of game you can clear that quickly.\""
            show j 1 c smile at fdis
            j "\"Still, I've been having a lot of fun.\""
            mc 1 c smile "\"Any titles I might know?\""
            show j 1 c think at fdis
            j "\"Well, they're both games for the Ninmax 2S Portable. Do you have it?\""
            mc 1 c think "\"Ah. No, I went with Senben's PBS when I picked the latest generation of portables.\""
            mc 1 c curious "\"Isn't it cross-platform compatible.\""
            show j 1 c considerate at fdis
            j "\"These two aren't.\""
            mc 1 c "\"Well, bummer, I guess.\""
            mc 1 c happy "\"Still, I'm glad you've at least been having fun.\""
            show j 1 c happy at fdis
            j "\"Thank you!\""
    mc 1 c "\"Oh, I just remembered. Shoichi asked me to say hi to you.\""
    show j 1 c watch at fdis
    j "\"Is that so? How is Shoichi-san doing?\""
    mc 1 c think "\"A bit stressed from working on the school festival but otherwise pretty okay.\""
    mc 1 c smile "\"We actually got together this morning and went to a café.\""
    show j 1 c shock at fdis
    j "\"Sounds fun. I wish I could have been there!\""
    show j 1 c watch at fdis
    j "\"Wait, if Shoichi-san was with you then why didn't he come over too?\""
    mc 1 c considerate "\"He had other things he needed to get done.\""
    mc 1 c think "\"If I remember correctly, he said he needed to go grocery shopping to pick up the things his father likes.\""
    show j 1 c smile at fdis
    j "\"Oh yeah. He did mention his dad was coming back home.\""
    mc 1 c considerate "\"He even asked for my help organizing a welcome home party but that idea was a bust...\""
    show j 1 c watch at fdis
    j "\"How come?\""
    mc 1 c sigh2 "\"... I couldn't convince him not to cook.\""
    show j 1 c wince at fdis
    j "\"O-oh...\""
    "Those poor guests. They never even saw it coming...\""
    mc 1 c worried "\"Let us not speak further of the dead... there is nothing we can do to bring them back.\""
    show j 1 c considerate at fdis
    j "\"[povFirstName]-san, I know you're kidding but you're kinda scaring me...\""
    mc 1 c happy "\"Is that so? Sorry. I guess I got too into the joke.\""
    show j 1 c wince at fdis
    j "\"Still... I imagine that party can't have been pleasant...\""
    mc 1 c sigh "\"I'm still surprised Takehiko-san didn't yell at him or anything... I guess the shock was too great.\""
    show j 1 c considerate at fdis
    j "\"Maybe he just didn't want to hurt Shoichi's feelings.\""
    mc 1 c sigh2 "\"Shoichi gave an entire room full of people food poisoning. Pretty sure he was past the point of caring about feelings.\""
    show j 1 c wince at fdis
    j "\"Guh...\""
    mc 1 c avoid "\"It's a good thing Shoichi's sister showed up... she managed to get him out of the house before the disaster rolled out so he didn't get to see it.\""
    show j 1 c shock at fdis
    j "\"Wait... so Shoichi-san doesn't know what happened?\""
    mc 1 c sigh2 "\"No... Hitoka sent him \"shopping for last minute preparations\" and all the guests left before he got back.\""
    mc 1 c avoid "\"... She then threatened me so I wouldn't tell Shoichi.\""
    show j 1 c wry at fdis
    j "\"... I'm not sure if I should call him lucky or not.\""
    mc 1 c avoid "\"{i}He's{/i} lucky. It's the people eating his food that aren't.\""
    show j 1 c considerate at fdis
    j "\"Right...\""
    show j 1 c watch at fdis
    j "\"Did I miss anything else for these days I've been absent? What about Keisuke-san or Mizoguchi-san?\""
    mc 1 c think "\"There's not much to tell. Saya has been taking more shifts than usual to save up for a new phone.\""
    mc 1 c talk "\"As for Keisuke, all I know is that he's spending more time with that band he joined. Since there are no tennis club practices for a while yet, I haven't seen much of him.\""
    show j 1 c wince at fdis
    j "\"That's kinda sad...\""
    mc 1 c considerate "\"We're not his only friends after all.\""
    mc 1 c talk "\"Plus, we want to avoid scheduling any group hang outs until you're back on your feet and can come with us.\""
    show j 1 c shockb at fdis
    j "\"W-what?\""
    show j 1 c considerate at fdis
    j "\"I... I really appreciate the thought but you guys don't have to stop having fun just because I'm not around...\""
    mc 1 c smile "\"Don't be ridiculous. How many times do I have to tell you you're a member of this group? The fun is in having everyone hanging out together.\""
    show j 1 c happyb at fdis
    j "\"...\""
    "Heh, so now he's blushing?"
    mc 1 c suggestive "\"Looks like someone is happy to hear that.\""
    show j 1 c shockb at fdis
    j "\"I... I didn't say anything!\""
    mc 1 c laugh "\"You didn't have to. One look at your face was enough to tell me what you're feeling.\""
    show j 1 c wince at fdis
    j "\"... Am I that obvious?\""
    mc 1 c smile "\"To say you wear your emotions on your sleeve would be an understatement.\""
    show j 1 c wince at fdis, shake1
    j "\"Guh...\""
    mc 1 c smile "\"It's not a bad thing. You're easy to talk to because of it.\""
    j "\"R-really?\""
    mc 1 c happy "\"Of course!\""
    "It also makes teasing you a lot more fun but, you know, I'm not gonna bring that up."
    mc 1 c think "\"It really makes what that guy said sound really strange when I think about it...\""
    show j 1 c watch at fdis
    j "\"What guy?\""
    mc 1 c considerate "\"O-oh, uhm... err... nothing, I'm just thinking out loud.\""
    "Wait, why am I even hiding this?"
    "What would be the harm in telling him we met Akutagawa anyway?"
    "..."
    mc 1 c wry "\"Well... actually, Shoichi and I met someone at the café and he kinda told us about your past.\""
    show j 1 c shock at fdis
    j "\"W-what?! Who? What did he say?\""
    mc 1 c talk "\"Shinji Akutagawa. That lion guy from your competition.\""
    show j 1 c wince at fdis
    j "\"W-what? Really?\""
    mc 1 c talk "\"Yeah. He told us you used to be really withdrawn as a kid... so much so he didn't even think you had friends at all.\""
    mc 1 c considerate "\"I just thought that that description really didn't sound like you.\""
    j "\"...\""
    show j 1 c considerate at fdis
    j "\"It's kinda true...\""
    mc 1 c shock "\"R-really?\""
    show j 1 c wry at fdis
    j "\"Yeah. At least where the competitions were concerned, I never really talked to the other kids.\""
    show j 1 c considerate at fdis
    j "\"I used to be really competitive when I was a kid so... I refused to mingle with the competition. Pretty petty, huh?\""
    mc 1 c worried "\"I... would have never guessed.\""
    show j 1 c wry at fdis
    j "\"Everyone has a past, after all...{nw}"
    show j 1 c happy at fdis
    extend " Plus, it's been over seven years since that time and I was a kid. Of course I matured a lot since then.\""
    mc 1 c shock "\"You did?!\""
    show j 1 c pout at fdis
    j "\"Why do you sound so surprised?\""
    mc 1 c considerate "\"M-me? Surprised? You must be imagining things!\""
    "Crap, I just blurted out what came to my mind without thinking!"
    mc 1 c fsmile "\"W-well, the important thing is that you're a different person now and you can get along with the other competitors now, right?\""
    show j 1 c annoyed at fdis
    j "\"I'm not letting that little comment go that easily.\""
    play sound "music/stab.ogg"
    "Guh!" with hpunch
    "I think I'm in need of rescuing just about now..."
    mc 1 c considerate "\"L-letting what go? I have no idea what you're talking about! Hahahaha...\""
    j "\"...\""
    play sound "music/stab.ogg"
    "Guh." with hpunch
    "Stop glaring at me like that, I got the message!"
    mc 1 c avoid "\"... Sorry.\""
    play sound "music/knock.ogg"
    yui 1 c smile "\"Jun, sweetie, I'm coming in.\""
    play sound "music/door2.ogg"
    stop music2 fadeout 2.5
    play music3 "music/BGM/On My Way.ogg" fadein 5.0
    show j 1 c watch at fdis, three with move
    show yui 1 c smile at seven with moveiridis
    "Saved by the gong!"
    "Or in this case, Jun's mother."
    yui "\"Do you boys want to have a snack? I baked some cookies.\""
    show j 1 c bored at fdis
    j "\"Mom, you don't need to fret so much just because there's someone over.\""
    yui "\"Oh, don't be such a stick in the mud. You have so few friends, of course I'm going to treat them with the utmost care.\""
    show j 1 c wince at fdis, shake1
    play sound "music/stab.ogg"
    j "\"Guh...\""
    show j 1 c bored at fdis
    j "\"Thanks for the vote of confidence...\""
    mc 1 c considerate "\"Uhm... cookies sound great, Kobayashi-san.\""
    "Please don't leave me alone with him until he forgets what just happened!"
    yui "\"Of course it sounds great. It's cookies. Why don't you boys come to the living room and I'll bring them to you!\""
    mc 1 c happy "\"Sure!\""
    show yui at offscreenright with moveoridis
    show j 1 c bored at fdis, five with move
    mc 1 c smile "\"I have to admit, I never thought your mom would be the stereotype \"I made cookies for you kids\" type.\""
    show j 1 c considerate at fdis
    j "\"She just likes playing host to other people. We used to have visitors and dinner parties all the time when I was younger.\""
    mc 1 c curious "\"You don't anymore?\""
    show j 1 c wince at fdis
    j "\"Not since mom started working two jobs.\""
    show j 1 c considerate at fdis
    j "\"With Dad picking up more shifts and mom having to get a second job, they barely have any free time anymore. She just's took a week off to keep an eye on me...\""
    mc 1 c shock "\"W-why do your parents need to work so much? Do you guys have that many expenses?!\""
    show j 1 c wince at fdis
    j "\"That's...\""
    j "\"...{nw}"
    show j 1 c considerate at fdis
    extend " I really shouldn't be talking about my parent's financial situation. Sorry.\""
    "..."
    "Something's weird here."
    "I can't imagine a small family like this living in a small house could accrue enough expenses to warrant that much work."
    "My mom might have a better than average job but she's still capable of supporting Aki and me without working herself to death!"
    "... Well, she still works herself to death but that's because she likes her job. She could also take things easy and she would still earn enough to support us."
    mc 1 c worried "\"Isn't your father a cop? I thought cops made good money.\""
    show j 1 c wry at fdis
    j "\"Like I said, I shouldn't be talking about their money situation...\""
    show j 1 c considerate at fdis
    j "\"And besides that, my dad is just a low-ranking patrolman. The pay isn't all that great.\""
    show j 1 c think at fdis
    j "\"...\""
    show j 1 c watch at fdis
    j "\"Wait, how did you know my dad was a cop?\""
    if day5 == "jun":
        mc 1 c sigh "\"He was wearing his police cap the first time I came over, remember?\""
        show j 1 c think at fdis
        j "\"He was?\""
        mc 1 c sigh2 "\"Why else would I say he was?\""
        mc 1 c avoid "\"He was also wearing it when he picked you up from the hospital.\""
    else:
        mc 1 c sigh "\"He was wearing his police cap when he picked you up from the hospital.\""
    show j 1 c wince at fdis
    j "\"Oh, right... he's not supposed to wear it outside when he's off shift but he tends to forget it's on...\""
    "... How can you forgot that you have a {i}cap{/i} on?"
    "Actually, never mind, this is the Kobayashi family I'm talking about. If they're anything like their son, it is entirely believable..."
    "Well, his mom doesn't seem that bad at least..."
    if day5 == "jun":
        "She was a little... enthusiastic the last time I came here, but she didn't strike me as being as eccentric as her son... or husband."
    show j 1 c watch at fdis
    j "\"Either way, we should probably go outside already before mom comes to fetch us.\""
    show j 1 c considerate at fdis
    j "\"Trust me, you don't want to annoy her...\""
    "Considering all the scary women I already have in my life, I can't even muster a look of surprise to this statement..."
    "Sometimes when I think of how Saya pretty much bosses all of us around, I start wondering whether we're all just beta males..."
    "Ugh, that thought just sends chills down my spine. I don't want to be a bunny's little toy!"
    scene JunLivingRoom
    show j 1 c watch at fdis, five
    with fade
    "We both sit at the living room table directly across from each other."
    "I have to admit, even though this house is small, it's very cozy."
    "For some reason, I feel right at home here... that's not something I've ever been able to say about any place other than my own home."
    j "\"By the way, [povFirstName]-san, you were telling me about how you ran into Akutagawa-kun before...\""
    "Oh God, I thought he'd forgotten about it already!"
    "I-Is he still mad at me for that unfortunate comment?"
    mc 1 c considerate "\"Y-yeah, I was. What about it?\""
    show j 1 c wince at fdis
    j "\"Did... did he say anything else? About me, I mean...\""
    mc 1 c worried "\"Why do you ask?\""
    show j 1 c pout at fdis
    j "\"You're the one who brought up the fact that you bumped into him today in the first place. Of course I'm going to ask about it!\""
    mc 1 c considerate "\"I guess that's true...\""
    "Man, I'm not used to seeing him looking annoyed at me."
    "It somehow feels ten times worse than having someone like Saya upset... probably because I'm already used to seeing her upset."
    mc 1 c worried "\"We didn't really talk for long, you know. He just bumped into us while he was waiting for a table at the cafe. It was less than five minutes.\""
    show j 1 c bored at fdis
    j "\"He still had time to tell you about me not getting along with the other kids in that time.\""
    mc 1 c considerate "\"I suppose that's true too.\""
    show j 1 c bored at fdis, three with move
    show yui 1 c smile at fdis, seven with moveiridis
    yui "\"Alright, sorry it took me a while. I had some trouble getting these out of the baking tray.\""
    show j 1 c watch at fdis
    j "\"Did you forget to line it with parchment paper again?\""
    yui "\"Oh, I didn't forget, we just ran out.\""
    show j 1 c wince at fdis
    j "\"Ugh, not again...\""
    mc 1 c curious "\"Again?\""
    show j 1 c considerate at fdis
    j "\"We seem to run through rolls of parchment paper like they're candy.\""
    yui "\"I suppose it's my fault. I'm always baking whenever I'm home. It helps me to relax.\""
    show j 1 c bored at fdis
    j "\"It's also the reason why we've gained so much weight these past few years...\""
    mc 1 c talk "\"I understand that your parents might not have much time but what's your excuse for not trying to exercise, then?\""
    show j 1 c wince at fdis
    j "\"W-well, that's...\""
    yui "\"Didn't Jun tell you? He-\""
    show j 1 c considerate at fdis
    j "\"I really hate exercising. Yeah, I already told him that. I just hate feeling sweaty and all that!\""
    "Jun's mom stares at him with wide open eyes. However, as quickly as her shock came, she flashed us another smile."
    yui "\"Yes, I suppose you would have told him already, then... Would you boys like something to drink? Milk? Maybe some tea?\""
    j "\"[povFirstName]-san hates tea.\""
    mc 1 c considerate "\"It's true, I really do.\""
    yui "\"Oh no, not another tea hater... Atsushi is already a handful.\""
    show j 1 c smile at fdis
    j "\"That's just because Dad is really whiny about it.\""
    mc 1 c curious "\"Whiny?\""
    show j 1 c think at fdis
    j "\"Oh yeah. Whenever mom brews some tea, he starts complaining about how awful the house smells and how it makes him feel sick.\""
    show j 1 c gentle at fdis
    j "\"He really sounds like a little kid throwing a tantrum. Hahaha!\""
    "... The similarities are uncanny."
    yui "\"You shouldn't laugh about that. You're so much like your father in many ways, you know.\""
    show j 1 c wince at fdis
    j "\"Ugh, please don't say that. I don't complain nearly as much as he does...\""
    yui "\"Your father didn't use to complain as much as he does now either. It comes with age, darling. You're so much like your father when he was your age, it's a bit scary.\""
    j "\"N-no, anything but that...\""
    mc 1 c smile "\"Oh, come on, you don't want to grow up to be like your father?\""
    show j 1 c bored at fdis
    j "\"God no, he has no common sense. He does so many embarrassing things when we're out in public...\""
    "And the similarities continue to pile up."
    "Jun's mom shoots me a knowing, amused glance, almost as if she could read my mind."
    "I guess she really knows him even better than he knows himself, huh?"
    yui "\"Well, in that case, should I just bring you boys some milk?\""
    show j 1 c happy at fdis
    j "\"Of course! Milk and cookies are a match made in heaven!\""
    mc 1 c smile "\"Well, I don't think I would go that far but I wouldn't say no to something to drink. Sorry to inconvenience you out of the blue, ma'am.\""
    yui "\"Oh, don't be silly. I love having people over. Not to mention how happy it makes me to have Jun's friends come visit him. I was starting to worry that he had no real friends since no one had dropped by these past few days.\""
    show j 1 c wince at fdis
    j "\"Mom, I already told you, it's nothing serious, they have no reason to come here. Actually, I told them not to come here myself!\""
    mc 1 c considerate "\"It's true. He really did tell us that we didn't need to come.\""
    yui "\"Well, that is no way to treat your friends. If they're worried about you then they have every right to visit. It's only natural.\""
    show j 1 c bored at fdis
    j "\"Yeah yeah, whatever you say...\""
    "I don't really know much of this woman but... damn, I like her already."
    yui "\"I will be right back.\""
    show yui 1 c smile at offscreenright with moveoridis
    show j 1 c wince at fdis, five with move
    j "\"...\""
    mc 1 c curious "\"Is something wrong?\""
    show j 1 c shock at fdis
    j "\"Huh? Ah, n-no!\""
    show j 1 c considerate at fdis
    j "\"I was just thinking some stuff over...\""
    mc 1 c talk "\"Are you thinking about what your mom said? About you not wanting us to visit.\""
    show j 1 c wry at fdis
    j "\"Kinda. I didn't want to be a bother to anyone, that's why I said that.\""
    show j 1 c considerate at fdis
    j "\"I didn't even realize that me not having visitors was upsetting her.\""
    mc 1 c sigh2 "\"Of course it would be. What else could she think when her son has been on bed rest for days and no one bothered to drop by to see him?\""
    show j 1 c wince at fdis
    j "\"I guess you're right.\""
    mc 1 c smile "\"You don't \"guess\" I'm right. I {i}am{/i} right.\""
    show j 1 c bored at fdis
    j "\"Yeah yeah. Don't get cocky.\""
    mc 1 c smile "\"Still, your mom is pretty nice. You never really talk much about your parents so I didn't really know what to expect.\""
    if day5 == "jun":
        mc 1 c considerate "\"Granted I've met her before, but... I was so overwhelmed by your dad at the time that I didn't really pay much attention to your mom.\""
        show j 1 c considerate at fdis
        j "\"Yeah, Dad can go a little overboard at times...\""
        show j 1 c think at fdis
        j "\"As for my mom, she's really nice. She can also be strict at times and boy is she scary when she's angry... but most of the time she's really sweet.\""
    else:
        show j 1 c think at fdis
        j "\"She's really nice. She can also be strict at times and boy is she scary when she's angry... but most of the time she's really sweet.\""
    mc 1 c happy "\"It's a pretty neat change of pace. I'm not really used to talking to many parents.\""
    show j 1 c watch at fdis
    j "\"How come?\""
    mc 1 c think "\"Well, my mom is always working too. She's the kind of person that you'd call \"in love with the job\".\""
    mc 1 c "\"I haven't talked to Shoichi's mom since his parents split up years ago and... well, Keisuke's entire family is kind of an unknown.\""
    mc 1 c think "\"I suppose I've talked to Saya's parents quite a few times. They're mostly normal people. None of them has their daughter's temper at least.\""
    show j 1 c considerate at fdis
    j "\"Mizoguchi-san really is scary sometimes isn't she?\""
    mc 1 c smile "\"Yeah, tell me about it.\""
    show j 1 c think at fdis
    j "\"Hmm... now that you mention it, I don't think I've ever met your mom either.\""
    show j 1 c considerate at fdis
    j "\"Actually, I don't think I've never been close enough friends with anyone to meet their parents.\""
    mc 1 c confused "\"Really? Even when you were a kid?\""
    show j 1 c smile at fdis
    j "\"I told you, I wasn't the most sociable person. I had a few kids I was friendly with, most of them were my classmates, but I was never the type to go out to play and whatnot.\""
    show j 1 c considerate at fdis
    j "\"I guess I'm also the kind of person you could call \"in love with the job\". Although in my case, piano isn't really a job.\""
    mc 1 c smile "\"It can be. With your skills, I'm sure you could do it.\""
    show j 1 c wry at fdis
    j "\"If only that were true...\""
    "Hmm... I can't quite put my finger on it, but..."
    "I'm getting this weird vibe from Jun today."
    mc 1 c curious "\"Is everything okay with you? For real? We haven't really talked in a couple of days... outside of trading a few messages at least.\""
    show j 1 c considerate at fdis
    j "\"Yeah, I'm fine. I just hate being cooped up in here for so long. It's almost worse than the hospital.\""
    mc 1 c shock "\"How come? I thought you'd feel better if you got to rest at home.\""
    show j 1 c wry at fdis
    j "\"It makes me feel like an invalid... just because of a tiny little problem, everyone is suddenly treating me like I'm made of glass. Of course, the fault is mostly with my parents, but...\""
    show j 1 c considerate at fdis
    j "\"Is it so bad not wanting to be treated differently?\""
    "... I never really noticed he'd been thinking things like that."
    "I suppose it's not the kind of thing one can notice just by looking but still..."
    mc 1 c worried "\"I hope I haven't been guilty of the same...\""
    show j 1 c wry at fdis
    j "\"... A bit. Mostly you've just been pampering me a lot.\""
    show j 1 c considerate at fdis
    j "\"Lost of presents and snacks... and you might not notice it but you're also being more soft spoken around me.\""
    mc 1 c wince "\"I... I'm sorry. I thought you'd like the presents...\""
    show j 1 c gentle at fdis
    j "\"Don't get me wrong, I love them. Especially the keychain. It's one of my most prized possessions now since it's the first real gift I've ever gotten from a friend, even if you say it was just a cheap afterthought.\""
    show j 1 c wry at fdis
    j "\"But at the same time...{nw}"
    show j 1 c considerate at fdis
    extend " I don't know, I might just be weird. I'm not even really sure how I feel about it. I really like it but I also feel really bad about it... I'm a mess, hehe...\""
    mc 1 c worried "\"Sorry. I'll try to rein it in a little.\""
    show j 1 c wry at fdis
    j "\"It's okay. This isn't your problem. It's my own awkwardness at fault.\""
    show j 1 c considerate at fdis
    j "\"I'm just not good at depending on other people. I always feel like such a burden when others go out of their way for me... even though I know they're doing it because they want to and it makes them happy to care for me.\""
    show j 1 c wry at fdis
    j "\"Like I said, I really am a mess. And being cooped up inside the house with no one to really talk to just makes me mull over those thoughts again and again. It's not healthy.\""
    mc 1 c curious "\"Isn't your mother here? Can't you talk to her?\""
    show j 1 c wince at fdis
    j "\"I can't talk to her about this. I'd just add to the issues she has to deal with. I don't want to put another burden on her...\""
    mc 1 c wry "\"I think you're being too self-conscious here. She's your mother, I'm sure she'd want to do whatever makes you feel more at ease.\""
    show j 1 c wry at fdis
    j "\"That's kind of what scares me. You don't know how far my parents would go to do that...\""
    mc 1 c considerate "\"I guess I'll concede to that point.\""
    show j 1 c smile at fdis
    j "\"But like I said, I really am grateful for everything you guys have been doing for me!\""
    show j 1 c happy at fdis
    j "\"You're all so nice and caring. It kinda makes me feel all warm and fuzzy on the inside!\""
    show j 1 c wince at fdis
    j "\"... Just don't tell anyone I said that.\""
    mc 1 c smile "\"Oh, for sure. If Keisuke and Shoichi ever heard that line, there'd be no end to the teasing.\""
    j "\"Just thinking about it already makes my skin crawl...\""
    "At least he seems like he's cheered up a little."
    mc 1 c smile "\"Do you feel better being able to talk about your feelings more openly?\""
    show j 1 c happy at fdis
    j "\"Yeah... I feel a bit silly for talking about all this mushy stuff to you but... I really feel like I can trust you enough for that.\""
    mc 1 c laugh "\"Of course you can. We're friends, aren't we?\""
    show j 1 c wry at fdis
    j "\"Yeah... {size=-4}just friends.{/size}\""
    mc 1 c curious "\"What was that?\""
    show j 1 c happy at fdis
    j "\"Oh, nothing, I just agreed with you!\""
    mc 1 c confused "\"By the way, where's your mom? Didn't she just go to the kitchen to grab milk?\""
    show j 1 c think at fdis
    j "\"Oh, I have an idea where she might be.\""
    mc 1 c curious "\"Huh?\""
    show j 1 c considerate at fdis
    j "\"Look at the cookie plate. There's six.\""
    mc 1 c "\"So?\""
    show j 1 c wry at fdis
    j "\"She always makes twelve.\""
    mc 1 c confused "\"Okay... and?\""
    show j 1 c think at fdis
    j "\"Just take a good look at her lips when she comes back and you'll see.\""
    "Huh?"
    show j 1 c watch at fdis, three with move
    show yui at seven with moveiridis
    yui "\"Sorry I took so long, I kinda lost track of time!\""
    "Yui-san comes back with two glasses of milk for us, setting them down in front of us and taking another seat.\""
    mc 1 c curious "\"You didn't get any for yourself, ma'am?\""
    yui "\"Oh no, don't be silly, I'm not gonna eat the cookies. I'm on a diet.\""
    "Jun lightly taps my foot from under the table, shooting me a weird look."
    "I decide to do as he says and try focusing my eyes on his mom's face and-"
    "... Is that..."
    play sound "music/disappointment.ogg"
    "She has a few cookie crumbs stuck to the fur around her mouth."
    "She didn't do what I think she did, did she?"
    show j 1 c considerate at fdis
    j "\"Sure you are, mom. And I have to say, that diet really seems to be working. I can see the difference already.\""
    yui "\"Really?! Oh, I'm so glad! I thought I noticed some slimming too but I wasn't too sure and I didn't want to assume. Maybe it would just be my brain playing tricks on me. Hahaha!\""
    mc 1 c considerate "\"Hahaha, that's so true...\""
    stop music3 fadeout 2.5
    play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    scene JunBedroom
    show j 1 c watch at fdis, five
    with fade
    "Eventually, Yui-san excuses herself claiming that she has to do some more housekeeping, leaving Jun and I to return to his bedroom."
    mc 1 c considerate "\"She wasn't... she wasn't really eating the cookies in secret, was she?\""
    show j 1 c considerate at fdis
    j "\"Yes she was... it's pretty much taboo for Dad and I to mention this kind of thing so we just play dumb and tell her she's been losing weight whenever she starts on another one of her diets.\""
    show j 1 c think at fdis
    j "\"Mom tends to get too excited about all these new diet fads but she can't stick to them for more than a few days before she cracks. She still pretends to be doing them while she eats sweets in secret though.\""
    mc 1 c considerate "\"I guess everyone in your family has a big sweet tooth huh?\""
    show j 1 c considerate at fdis
    j "\"That's an understatement.\""
    "Having seen him attack a box of Japanese sweets, I can also agree with that assessment."
    show j 1 c think at fdis
    j "\"Actually, now that you mentioned sweets, how are the preparations for the school festival going?\""
    "?!"
    mc 1 c fsmile "\"Uhm... what, if anything, does the school festival have to do with sweets?\""
    show j 1 c shock at fdis
    j "\"Oh.\""
    show j 1 c happy at fdis
    j "\"Ehehehe, sorry. It's just that when you said \"sweets\" it reminded me of Ayako-san.\""
    show j 1 c think at fdis
    j "\"Then when I thought about her, it reminded me of school, which reminded me of the school festival.\""
    mc 1 c wince "\"... Your train of thought is all over the place.\""
    show j 1 c happy at fdis
    j "\"I like to think outside the box.\""
    "I don't think there's even a box to begin with when it comes to you."
    show j 1 c watch at fdis
    mc 1 c talk "\"But to answer your question, the preparations are going fine. Our class is mostly finished.\""
    show j 1 c smile at fdis
    j "\"That's great! What have you been put in charge of?\""
    mc 1 c think "\"I'm not in charge of anything, I'm just helping out with the decorations, shopping, etc.\""
    show j 1 c think at fdis
    j "\"Hmm... Since Ayako-san told me the class would be opening a restaurant, I thought you'd be cooking.\""
    mc 1 c sigh "\"God no. I like cooking for myself and for friends but there's absolutely no way I'd cook for a huge crowd.\""
    show j 1 c watch at fdis
    j "\"Really? I thought you'd jump at the opportunity.\""
    mc 1 c sigh2 "\"The only thing that could make me jump at the opportunity of cooking for that many people would be if the alternative were to have Shoichi cook.\""
    show j 1 c wince at fdis
    j "\"That's a very scary alternative...\""
    "One that sadly did happen..."
    "Those poor guests."
    mc 1 c "\"Did the rep talk to you about what you might end up doing for the festival?\""
    show j 1 c think at fdis
    j "\"A bit. She offered to let me give a hand with the organization.\""
    mc 1 c smile "\"Maybe that means we get to work together.\""
    show j 1 c considerate at fdis
    j "\"I turned her down though.\""
    mc 1 c shock "\"Why?\""
    show j 1 c wry at fdis
    j "\"My last school didn't do a festival so I was really looking forward to doing something more involved.\""
    show j 1 c gentle at fdis
    j "\"I was thinking of asking to work as a waiter for the restaurant!\""
    "{cps=1}...{/cps} Those poor guests."
    mc 1 c considerate "\"Are you sure that's the best idea for you? You'd be running up and down, carrying a ton of plates and hot food for most of the night.\""
    show j 1 c smile at fdis
    j "\"Doesn't it sound fun?\""
    "I can already imagine the chaos... forgotten orders, spilled drinks, dropped plates."
    "Our class' restaurant will be a bust, won't it?"
    show j 1 c think at fdis
    j "\"Too bad you won't be working at the nights of the festival though.\""
    mc 1 c sigh2 "\"I want to actually enjoy the festival. Go around the stalls and check everything out. I don't want to be cooped up working all night.\""
    show j 1 c watch at fdis
    j "\"Shifts exist, you know. You'd probably only work for one of the days.\""
    mc 1 c smile "\"Nope. I don't want to lose even a single day. The school festival is great for relaxing and having fun. There's no way I'm gonna spend it working.\""
    show j 1 c bored at fdis
    j "\"Ugh, you're such a special snowflake.\""
    mc 1 c wince "\"W-what?\""
    show j 1 c happy at fdis
    j "\"Nothing.\""
    mc 1 c worried "\"You might act innocent but at this point it's pretty obvious that you're not.\""
    show j 1 c think at fdis
    j "\"I don't know what you're talking about.\""
    mc 1 c sigh2 "\"Sure you don't.\""
    "Beware the quiet ones, that's all I'll say."
    mc 1 c "\"Either way, we should all try to get at least one free day to hang around together.\""
    show j 1 c watch at fdis
    j "\"That might be a bit difficult. The five of us are distributed across three different classrooms so it'd be pretty difficult to get our schedules to sync up.\""
    mc 1 c smile "\"Speak for yourself, I'm free as a bird.\""
    show j 1 c annoyed at fdis
    j "\"That's because you're lazy.\""
    mc 1 c smile "\"Pota{i}to{/i}, po{i}ta{/i}to.\""
    show j 1 c watch at fdis
    j "\"Whatever.{nw}"
    show j 1 c smile at fdis
    extend " Hey, if the theme for the restaurant is Chinese, does that mean we'll get Chinese styled uniforms?\""
    mc 1 c "\"The girls will probably wear Chinese dresses. I have no idea what the guys will be wearing though. Is there even a male alternative to that?\""
    show j 1 c think at fdis
    j "\"Hmm... I don't know of any.\""
    show j 1 c happy at fdis
    j "\"I wonder if I'd look like a Kung-Fu master with the waiter uniform.\""
    mc 1 c fsmile "\"It's a waiter uniform, not a Kung-Fu Gi.\""
    show j 1 c think at fdis
    j "\"Would a Kung-Fu gi even be called a \"Gi\" in China?\""
    mc 1 c "\"Of course not. That's a Japanese word. Why would they use it in China?\""
    show j 1 c watch at fdis
    j "\"Well, what's it called, then?\""
    mc 1 c fsmile "\"Uhm... I have no idea.\""
    show j 1 c think at fdis
    j "\"Then you can't say for sure it's not called a Gi, can you?\""
    mc 1 c sigh "\"I see where you're going with your logic but that doesn't make it right.\""
    show j 1 c watch at fdis
    j "\"Why not?\""
    mc 1 c annoyed "\"Because they don't speak Japanese in China!\""
    j "\"How do you know? Have you ever been to China?\""
    "..."
    mc 1 c sigh2 "\"This whole discussion was just you messing with me, wasn't it?\""
    show j 1 c happy at fdis
    j "\"What was your first clue?\""
    "Ugh... felines."
    mc 1 c "\"Will your parents show up for the festival?\""
    show j 1 c think at fdis
    j "\"They said they wanted to but I wouldn't count on it. They're always so busy, especially Dad.\""
    mc 1 c think "\"Well, I'd imagine a cop is pretty busy most of the time.\""
    show j 1 c considerate at fdis
    j "\"Yeah. It's really sad how little free time they have. It really makes me feel bad.\""
    mc 1 c smile "\"Hey, it's not like it's your fault.\""
    show j 1 c wince at fdis
    j "\"Right...\""
    mc 1 c think "\"Hmm... I wonder what I'm gonna be doing for the first day of the festival. They haven't released the class plans yet so I don't know what kind of stalls will be open.\""
    show j 1 c considerate at fdis
    j "\"Do you really have to plan this kind of thing in advance?\""
    mc 1 c smile "\"Of course. That's the only way to maximize the amount of stalls visited in the smallest amount of time.\""
    j "\"Just sounds like a big waste of brain energy.\""
    mc 1 c "\"Brain energy?\""
    show j 1 c watch at fdis
    j "\"You know, thinking power.\""
    mc 1 c worried "\"T-thinking power?\""
    "Are you sure you're really nineteen?"
    mc 1 c sigh2 "\"Jun, don't waste those precious neurons...\""
    show j 1 c think at fdis
    j "\"Huh?\""
    "Exactly."
    mc 1 c "\"In other news, I heard Kei's band is planning to perform at the festival this year.\""
    show j 1 c shock at fdis
    j "\"Ooh, that's exciting! Will he be on stage?\""
    mc 1 c avoid "\"Nah, he's just their manager.\""
    show j 1 c watch at fdis
    j "\"How come? He's a really good singer.\""
    mc 1 c sigh2 "\"I asked the same thing but he didn't care to answer.\""
    show j 1 c think at fdis
    j "\"He really sells himself short sometimes, huh?\""
    mc 1 c "\"Agreed.\""
    mc 1 c smile "\"I have to admit, it'd be pretty cool to see him singing with a band.\""
    show j 1 c happy at fdis
    j "\"Yeah, it would. I'm sure he'd wow any audience with his voice.\""
    mc 1 c smile "\"I just wish he could have a little more confidence in himself. No matter how much we say we like his voice he just doesn't seem to believe it.\""
    show j 1 c think at fdis
    j "\"I'm tempted to call him humble but he's a little too extreme about it.\""
    mc 1 c sigh2 "\"He's like that about everything. Tennis, grades, singing. No matter how good he is, it's never enough.\""
    mc 1 c avoid "\"It's a bit annoying to be honest.\""
    show j 1 c considerate at fdis
    j "\"Well, don't let it get to you. Everyone has their quirks.\""
    "Said the quirkiest person I know."
    show j 1 c think at fdis
    j "\"I wish I had a good singing voice.\""
    mc 1 c confused "\"You can already play the piano super well, why would you need to sing?\""
    show j 1 c watch at fdis
    j "\"Yeah, but people don't care about the piano as much as they care about good singers.\""
    show j 1 c think at fdis
    j "\"After all, the piano is something anyone can learn with enough patience and practice. Your voice is something you're born with.\""
    mc 1 c talk "\"You can still improve your voice.\""
    show j 1 c considerate at fdis
    j "\"Well, yeah, sure you can. But a person that was born with an average voice can only take it so far. You'll never be truly great unless you were born great.\""
    show j 1 c think at fdis
    j "\"He's really lucky in that sense. His voice is really amazing.\""
    mc 1 c smile "\"Could it be that the happy go lucky tiger is jealous of someone for once?\""
    show j 1 c considerate at fdis
    j "\"For once? I'm jealous of lots of people, I'm no saint.\""
    show j 1 c think at fdis
    j "\"I'm jealous of your athleticism for instance.\""
    mc 1 c smile "\"That is also something you can improve on with practice.\""
    show j 1 c considerate at fdis
    j "\"You'd think so but that's not always the case...\""
    mc 1 c curious "\"Why not?\""
    show j 1 c sigh at fdis
    j "\"Let's just say that I'm not cut out for sports and leave it at that.\""
    mc 1 c think "\"I don't know, you can't just say something so vague and t-\""
    show j 1 c annoyed at fdis
    j "\"I said we'll leave it at that.\""
    mc 1 c wince "\"Y-yes, sir!\"" with hpunch
    "Jeez, what did I do to tick him off this time?"
    "I guess he wasn't kidding when he said being cooped up here was stressful..."
    mc 1 c considerate "\"Uhm, so... do you have any plans for what you're gonna do after your parents allow you to leave the house tomorrow?\""
    show j 1 c watch at fdis
    j "\"Just the same as always, school and practice.\""
    show j 1 c considerate at fdis
    j "\"Oh, and... speaking of school...\""
    mc 1 c "\"Yeah?\""
    j "\"You know how I said that Ayako-san has been dropping by notes for me?\""
    mc 1 c curious "\"I do. What about it?\""
    show j 1 c wry at fdis
    j "\"Well, she's also been dropping some homework by and... well...\""
    show j 1 c wince at fdis
    j "\"I... kinda haven't done it... any of it.\""
    "..."
    "....."
    show j 1 c shock at fdis
    j "\"Uhm... aren't you going to react to that at all?\""
    mc 1 c sigh2 "\"Why would I? I could see this punchline coming from a mile away.\""
    show j 1 c wince at fdis
    j "\"Y-you could?\""
    mc 1 c sigh2 "\"Of course. I'd never expect you to do your homework out of your own volition.\""
    show j 1 c wince at shake1, fdis
    play sound "music/stab.ogg"
    j "\"Guh...\""
    show j 1 c sigh at fdis
    j "\"You really have no faith in me, do you?\""
    mc 1 c smile "\"Knowing you and not having faith in you are two different things.\""
    j "\"Doesn't sound all that different to me...\""
    show j 1 c wince at fdis
    j "\"Well, anyway... uhm... could I...{nw}"
    show j 1 c considerate at fdis
    extend " Could I ask you to help me with it?\""
    mc 1 c smile "\"Sure. No problem.\""
    show j 1 c shock at fdis
    j "\"Wait, really? You will?\""
    mc 1 c sigh "\"Why are you so surprised? I've already been helping you study anyway. How would this be any different?\""
    show j 1 c think at fdis
    j "\"Hmm... when you put it that way, I guess it really isn't.\""
    mc 1 c suggestive "\"Well, it might be different in the sense that it'll be much easier. Trying to get you to remember stuff is definitely a herculean task.\""
    show j 1 c wince at fdis
    j "\"I don't know the meaning of the word \"herculean\" but I'm just going to assume that was an insult.\""
    mc 1 c happy "\"More like friendly quip.\""
    show j 1 c think at fdis
    j "\"Whatever. As long as you help me with my homework, you can joke as much as you like.\""
    mc 1 c suggestive "\"Oh, really? As much as I like, you say?\""
    show j 1 c wince at fdis, shake1
    j "\"U-uhm... m-maybe not as much as you like...\""
    mc 1 c happy "\"Pfft, hahahaha. Alright, alright. Just get me your books and I'll help you.\""
    mc 1 c smile "\"But I absolutely won't do it for you. Be aware of that.\""
    show j 1 c wince at fdis, shake1
    play sound "music/stab.ogg"
    j "\"Guh...\""
    mc 1 c think "\"Well... depending on how big the pile is, I might be a bit more generous with information so we'll move through it faster.\""
    show j 1 c gentle at fdis, jumping
    j "\"Yay!\""
    "So easy to please."
    stop music2 fadeout 2.5
    scene JunBedroom
    show j 1 c watch at fdis, five
    with fade
    play music "music/scribbling.ogg"
    "Once we get started, Jun remains seated on his desk, diligently working."
    "He only stops a few times to ask me questions and then gets right back to it once he understands the subject matter."
    "Even if he hates studying, his focus is really scary once he gets going."
    "I definitely expected to be a little more... involved in this process."
    "Right now I'm just sitting next to him, idly twiddling my thumbs and waiting for him to call me again."
    show j 1 c think at fdis
    j "\"Hmm...\""
    mc 1 c curious "\"Ran into a problem?\""
    show j 1 c shock at fdis
    j "\"Huh? Oh, not really.{nw}"
    show j 1 c think at fdis
    extend " I was just thinking over this question. The text is pretty long so it's confusing me a little."
    mc 1 c smile "\"Ah, yeah, some of them are designed with that in mind. They throw a bunch of pointless information at you to see if you can separate them from the important stuff.\""
    show j 1 c wince at fdis
    j "\"That's super annoying.\""
    mc 1 c happy "\"Right once again.\""
    show j 1 c think at fdis
    j "\"Hmm...\""
    "..."
    "I can't believe I'm going to say this but I kinda wish his laziness would win out just so I could do something more interesting than staring at the ceiling."
    "I guess I might be an enabler..."
    show j 1 c watch at fdis
    j "\"...\""
    show j 1 c wince at fdis
    j "\"...\""
    show j 1 c shock at fdis
    $ renpy.pause(1.0)
    show j 1 c watch at fdis
    j "\"...\""
    "Watching him just sitting quietly and studying is also a pleasant feeling, somehow."
    "It just feels so different from the usual Jun, bouncing around all over the place and running his mouth whenever possible."
    "Kinda like watching a rowdy little puppy dog sleeping."
    "... Great, now my mind has further demoted him from child to lap dog... or cat."
    "Man, he'd be super mad if he could peer into my thoughts right now."
    "Still, he's a much better student than I give him credit for."
    "I'm sure he could get very far if he applied himself a little more."
    stop music
    j "\"Hey, [povFirstName]-san?\""
    mc 1 c shock "\"Y-yeah? What is it?\""
    show j 1 c wince at fdis
    j "\"I got finished with my history homework and decided to get started on the math, but...\""
    show j 1 c avoid at fdis
    j "\"But... uhm... I'm not good with calculus, so...\""
    show j 1 c considerate at fdis
    j "\"This might be a stupid question, but... what's a sine and cosine?\""
    "..."
    mc 1 c sigh2 "\"That's not even calculus. That's trigonometry...\""
    show j 1 c shock at fdis
    j "\"Oh, really?{nw}"
    show j 1 c avoid at fdis
    extend " Then what about hypotenuse?\""
    "{cps=1}...{/cps} I take back what I said before, this is going to be more work than I thought."
    play music2 "music/BGM/On My Way.ogg" fadein 5.0
    scene JunBedroom
    show j 1 c sigh at fdis, five
    with fade
    j "\"Oh God, why did schools have to invent homework?\""
    mc 1 c think "\"Yes, how dare they want to make sure their students are learning.\""
    show j 1 c annoyed at fdis
    j "\"Don't patronize me.\""
    mc 1 c smile "\"I have no idea what you're talking about.\""
    j "\"Of course you do-\""
    play sound "music/door2.ogg"
    show j 1 c watch at fdis, three with move
    show ats 1 c d smile at seven with moveiridis
    ats "\"Hey, Jun, your mom tells me [povFirstName]-kun is visiting?\""
    show ats 1 c d smile at jumping
    show j 1 c bored at fdis
    ats "\"It's true, you really are here!\""
    j "\"Oh no...\""
    mc 1 c considerate "\"Hello, sir. I'm sorry for the intru-\""
    show ats 1 c d smile:
        ease .2 zoom 1.5 xoffset -30 yoffset 200
    play sound "music/tap.ogg"
    "He immediately walks up to me and shakes my hand enthusiastically."
    ats "\"I'm so glad to have gotten to see you in the flesh again. You're so much more imposing than I remembered. I still can't believe my son is really friends with you!\""
    mc 1 c fsmile "\"I-I'm happy to be your son's friend, sir.\""
    j "\"Dad, please stop. You're creeping [povFirstName]-san out.\""
    show ats 1 c d smile:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    ats "\"Oh, I'm so sorry, I really didn't mean to offend.\""
    mc 1 c considerate "\"N-no, you're fine, sir. This is your house after all.\""
    show j 1 c annoyed at fdis
    j "\"Which, by the way, I've already asked you tons of times to knock before you come in, Dad.\""
    ats "\"Why? It's not like you've got something to hide.\""
    j "\"That's not the point. It's the expectation of privacy. What if I were getting changed? What if I had just gotten out of the shower?\""
    ats "\"But I knew you had a friend over so of course that wouldn't be true.\""
    show j 1 c bored at fdis
    j "\"Yeah, sure, this time. But this is hardly the first time this happens. And you {i}have{/i} walked in on me when I was changing before!\""
    "The older tiger shrugs, staring at his son with a dumb smile on his face."
    "A smile that I know well, because it's exactly like the one his son wears."
    ats "\"So what? It's not like you're packing anything I've never seen before. Besides, you've seen me naked many times before.\""
    mc 1 c fsmile "\"Wait, seriously?\""
    show j 1 c annoyed at fdis
    j "\"Unfortunately, yes. But only because he has a tendency of walking around the house in no clothes. Or leaving the bathroom door unlocked. Or not closing his bedroom door when he changes.\""
    ats "\"It's not like I have anything to hide.\""
    j "\"That's not the point. The point is that I don't want to see you naked, damnit!\""
    ats "\"Jeez, you're so fussy. I wonder what side of the family you got that from. Certainly wasn't mine!\""
    show j 1 c sigh at fdis
    j "\"...\""
    "Jun's now doing breathing exercises while his father laughs at his own jokes."
    "Yeah, I can definitely see how this sort of behavior could get on someone's nerves."
    ats "\"Oh, right. It's already late, [povFirstName]-kun. Would you like to have dinner with us?\""
    mc 1 c wince "\"Oh, uhm, I really shouldn't. Like you said, it's pretty late and I don't want to intrude.\""
    ats "\"Don't be silly, it's no problem. We'd be delighted to have you with us.\""
    mc 1 c wince "\"B-but-\""
    show j 1 c wince at fdis
    j "\"[povFirstName]-san, I know it sucks for me to ask, but... I still haven't finished my homework either.\""
    show j 1 c avoid at fdis
    j "\"Could you stay until I'm done? Math is my worst subject and I left it for last. I don't think I'll be able to do it without your help.\""
    mc 1 c wince "\"Right, that's true, we're not done yet...\""
    ats "\"See? That's the perfect opportunity. You can have dinner with us and then continue working on it with Jun!\""
    ats "\"By the way, are you two doing homework together or are you just helping Jun?\""
    mc 1 c smile "\"I'm helping him deal with the surplus of homework he let pile up.\""
    ats "\"I thought you told me you were dealing with it as you were getting it.\""
    show j 1 c wince at fdis, shake1
    j "\"Guh...\""
    show j 1 c avoid at fdis
    j "\"W-well, you see...\""
    "The tiger shakes his head."
    ats "\"Don't be lazy, Jun. At least do your work diligently.\""
    j "\"Yes, Dad...\""
    ats "\"Well, now that this was dealt with, your mother says dinner will be ready in about ten minutes. Please join us, [povFirstName]-kun.\""
    mc 1 c considerate "\"Y-yeah. I think I'll take you up on your offer after all.\""
    "I can't quite leave Jun with his homework unfinished."
    "I have a feeling that the instant I walked out the door, he'd just put it aside and forget it existed."
    "... Considering what I've seen from him so far, I really can't allow him to pass up any opportunities to improve on his studies."
    "... No one needs a 20-year old high school student after all."
    mc 1 c curious "\"By the way, Kobayashi-san-\""
    ats "\"Oh, please, feel free to call me Atsushi.\""
    show j 1 c think at fdis
    j "\"There's no real point calling anyone by their last name here, [povFirstName]-san. We're all Kobayashi after all.\""
    mc 1 c considerate "\"I guess that's true...\""
    "He's never called Aki by his last name either so I suppose I should try to treat his family with the same courtesy."
    mc 1 c curious "\"Atsushi-san, you're a police officer, aren't you?\""
    ats "\"Oh, Jun's told you about my job?\""
    mc 1 c considerate "\"No... actually, that was just a guess of mine.\""
    "Although I did have it confirmed after I first asked."
    ats "\"I guess? How were you able to guess? No, wait, don't tell me. It's because of my cop aura, right? I just scream of law enforcement don't I? That has to be it. Ha ha ha ha!\""
    show j 1 c avoid at fdis
    j "\"Ugh, Dad...\""
    "He really seems to be enthusiastic about his job, at least..."
    mc 1 c considerate "\"Actually... it's because of your police cap. I think you were using it when I saw you last.\""
    ats "\"?!\"" with hpunch
    ats "\"Oh, shoot. I always forget to take it off.\""
    show ats 1 n d smile with dissolve
    ats "\"Ugh... I've already gotten chewed out by my superiors over this so many times before too...\""
    "He puts on a squeaky, high-pitched tone of voice, like a child mocking something someone else has said."
    "This certainly isn't the most flattering display."
    ats "\"\"Kobayashi, you're not supposed to go out in public wearing your cap if you don't have your uniform. You're not on the clock!\" is what they'd say...\""
    "I have to say I agree with them..."
    "More importantly, how does he even manage to forget a cap on his had?"
    "Does he never change shirts? They can't {i}all{/i} be button up shirts, can they?"
    "Air-headed, jokey, somewhat childish... I really see who Jun takes after."
    "Yui-san was right on the mark when she said the two are more alike than Jun realizes."
    "Mother always knows best, huh?"
    ats "\"Anyway, I'm going to go kiss the cook before dinner is ready. See you kids in a few minutes!\""
    show ats 1 n d smile at offscreenright with moveoridis
    show j 1 c bored at fdis, five with move
    "Atsushi-san winks at us and leaves the room with an exaggerated waving gesture."
    j "\"You see what I mean? No common sense...\""
    mc 1 c considerate "\"I-is that so?\""
    "You're really not one to talk at all, Jun..."
    mc 1 c smile "\"Still... seeing your dad like that, it kinda makes me happy.\""
    show j 1 c watch at fdis
    j "\"Huh? Why?\""
    mc 1 c happy "\"You guys just seem so close. I can't help but smile when I think about it.\""
    show j 1 c shockb at fdis
    j "\"W-what?\""
    show j 1 c blush at fdis
    j "\"W-what's so special about that? We're a regular family... this kind of thing is normal, isn't it?\""
    mc 1 c wry "\"At least one would hope so, but it's not always the case.\""
    mc 1 c considerate "\"You and Saya are pretty much the only ones who have perfectly normal, ordinary families like that.\""
    show j 1 c avoid at fdis
    j "\"We are?\""
    mc 1 c wry "\"Yeah... they might not talk much about it, but both Keisuke and Shoichi have serious problems with their families.\""
    mc 1 c considerate "\"Shoichi's parents are divorced and because of it, he barely sees his mom and sister...\""
    mc 1 c worried "\"And Keisuke hasn't seen his mother in years... not to mention the fact the he doesn't even speak to his father or grandmother.\""
    j "\"I hadn't really considered that... My family has always been like this so I never bothered to think about how things would be if they weren't.\""
    "That's called taking things for granted."
    show j 1 c at fdis
    j "\"But what about you, [povFirstName]-san? You said Mizoguchi-san and I are the only ones with normal families but as far as I know, you also have a loving family.\""
    mc 1 c considerate "\"Loving doesn't mean normal. I don't have a father anymore, remember?\""
    show j 1 c shock at fdis, shake1
    play sound "music/stab.ogg"
    $ renpy.pause(1.0)
    show j 1 c avoid at fdis
    j "\"I'm sorry, I didn't even think-\""
    mc 1 c smile "\"Relax. This sort of thing doesn't bother me, I already told you that before.\""
    mc 1 c happy "\"But that's kind of my point. You'd think families like yours would be the norm but that's not really always the case.\""
    mc 1 c smile "\"It just makes me happy to see such a tight-knit, loving family like that.\""
    mc 1 c happy "\"You're really lucky.\""
    show j 1 c shockb at fdis
    j "\"[povFirstName]-san...\""
    show j 1 c happyb at fdis
    j "\"Hehe, I guess you're right.\""
    "There we go."
    "He's been so stressed and looking so serious all day."
    "The glimpses I got of his smile weren't nearly as frequent as I'm accustomed to."
    "Someone like you really should be smiling more often. That smile really suits you, Jun..."
    mc 1 c happy "\"Anyway, how about we take a break from all this homework and go eat?\""
    show j 1 c smile at fdis
    j "\"Okay!\""
    scene JunLivingRoom
    show j 1 c smile at fdis, five
    show yui 1 c smile at two
    show ats 1 n c smile at eight
    with fade
    "We walk out into the living room just as Yui-san is setting up the dinner table."
    "Atsushi-san is sitting in front of the TV, watching some news report."
    ats "\"Unbeliavable, they're going to up the public transport fare again!\""
    yui "\"You already knew this was bound to happen sooner or later.\""
    ats "\"Yeah, but still... it's the second increase in three years.\""
    yui "\"I for one think it was a miracle that the fare has kept steady for that long. The entire world's economy is going through a crisis after all.\""
    "Atsushi-san grumbles unhappily at his wife's words."
    show j 1 c watch at fdis
    j "\"Oh, hey, you changed your shirt, Dad?\""
    ats "\"Yeah, your mother made me get changed.\""
    yui "\"Of course I did. Did you see how filthy his other shirt was? That is unacceptable when we have guests over!\""
    mc 1 c sigh "\"{size=-2}Why only when you have guests over...{/size}\""
    show j 1 c considerate at fdis
    j "\"{size=-2}Mom actually complains about it all the time but he just responds that he doesn't have to look good for anyone in his own home. She's just using you as an excuse to have him get changed.{/size}\""
    mc 1 c curious "\"Oooh.\""
    "She's much more sly than I thought she'd be."
    "I guess you have to be if you want to bring order to a household that has both Jun and his Dad in it."
    show j 1 c smile at fdis
    j "\"By the way, Dad, how was work today. Did you make any arrests?\""
    "Upon hearing his son's question, Atsushi-san makes a long, exaggerated sigh, shaking his head with much gusto."
    ats "\"Unfortunately not. People seem to be sticking with the law much more frequently these days...\""
    "Why do you say that as if it were a bad thing?"
    "As a cop, shouldn't that make you happy?!"
    show j 1 c happy at fdis
    j "\"Oh, don't worry. I'm sure someone's bound to do something bad at some point and then you can bust them!\""
    ats "\"Yes, that's what I keep telling myself every day. Fingers crossed for some big robbery. Maybe a murder if I get lucky!\""
    "What the hell is wrong with this family?!"
    yui "\"I will not have such morbid conversation at the dinner table, you two.\""
    show j 1 c think at fdis
    j "\"But no one's sitting at the table yet.\""
    yui "\"I don't care. You two just stop talking about murders. In fact, stop wishing for any crime to happen entirely.\""
    "Thank you!"
    "At least there's a voice of reason in this household."
    "How she manages to put up with the two of them is beyond my understanding."
    "Yui-san just might have the patience of a saint."
    yui "\"Either way, the food is at the table. Why don't we all eat now?\""
    show j 1 c happy at fdis
    j "\"Okay!\""
    mc 1 c smile "\"Pardon the intrusion.\""
    if day5 == "jun":
        yui "\"Oh, it's not intrusion at all. It's our pleasure to have you over again, [povFirstName].\""
        "Everything on the table looks delicious."
        "If there's one thing I know after having dinner before, it's that Yui-san is a wonderful cook."
    else:
        yui "\"Oh, it's not intrusion at all. It's our pleasure to have you over, [povFirstName].\""
        "Everything on the table looks delicious."
    "I really can't wait to dig in."
    "I just hope I don't look too eager."
    ats "\"Oh, Yui, you made Yakiniku. What's the occasion?\""
    yui "\"There's no occasion. I just wanted to cook something extra tasty since we have a visitor. I even used the best meat we had.\""
    ats "\"Oooh, I was already feeling impatient since you wouldn't use it.\""
    yui "\"Of course. Good meat is supposed to be saved for guests or special occasions.\""
    mc 1 c considerate "\"I-is that so?\""
    "I'm not sure if I should feel guilty for getting them to waste their good food on me or not."
    show j 1 c think at fdis
    j "\"{size=-2}Dad is grateful that you're having dinner with us because that means he gets to eat good meat.{/size}\""
    mc 1 c talk "\"Oooh, I see.\""
    "At least I don't have to worry about that anymore."
    "We all take our seats at the table."
    show j 1 c smile at fdis
    j "\"Here's your plate, [povFirstName]-san. Eat as much as you'd like.\""
    mc 1 c smile "\"Thanks.\""
    ats "\"Hey, [povFirstName]-kun, you don't mind if I ask you a few questions, do you?\""
    mc 1 c happy "\"Oh, is this an interrogation, officer?\""
    ats "\"Bahahahaha, of course not!\""
    show j 1 c bored at fdis
    j "\"I wouldn't trust dad's word on that. If you say yes to this, he's gonna have you answering questions all night.\""
    ats "\"H-hey, that's not true.\""
    mc 1 c considerate "\"Uhm... I'm a little scared now...\""
    ats "\"I'm not that bad!\""
    show j 1 c at fdis
    j "\"That's a little hard to believe.\""
    show ats 1 n c smile at shake1
    ats "\"Guh...\""
    yui "\"Jun, don't tease your father.\""
    show j 1 c smile at fdis
    j "\"Me? Teasing? I would never!\""
    yui "\"You've become a lot more snarky lately. What's been happening to you?\""
    show j 1 c think at fdis
    j "\"I have no idea what you're talking about.\""
    "I do. It's called \"bad influences\"."
    show j 1 c watch at fdis
    mc 1 c smile "\"Anyway, sure, you can ask me anything, Atsushi-san.\""
    ats "\"Oh, yay!\""
    "\"Yay\"? I never thought I'd see the day where I'd see a grown man pumping his fists in the air and shouting out \"yay\"."
    ats "\"Okay, so, there are lots of things I'm curious about-\""
    show j 1 c bored at fdis
    j "\"Here we go.\""
    ats "\"BUT... I'm going to keep myself under control and only ask you a couple questions.\""
    j "\"Sure you are.\""
    ats "\"Come on, Jun, at least have {i}some{/i} faith in your good old father here!\""
    j "\"Give me a reason to and I will.\""
    show ats 1 n c smile at shake1
    ats "\"Urk...\""
    "It's like two old ladies having an argument."
    "This is... surreal."
    ats "\"Alright, alright. I'll just ask ONE question. Is that better for you?\""
    show j 1 c smile at fdis
    j "\"I really doubt you will.\""
    yui "\"So do I.\""
    ats "\"Yui, you're supposed to be on my side here!\""
    yui "\"Says who?\""
    ats "\"Says the marriage certificate we have framed in our bedroom!\""
    yui "\"As far as I know, all that says is that we're legally married. I don't remember reading any passages saying that you must side with your spouse at all times.\""
    ats "\"You two are really mean sometimes, you know...\""
    "And now Atsushi-san is hanging his head down, shoulders sagging, pouting and dejected."
    "Quite a pitiful sight for a man his age."
    yui "\"Oh, hush, honey. You know we're just joking.\""
    ats "\"I guess... Anyway, back to you, [povFirstName]-kun!\""
    "Boy, he sure bounced back pretty fast."
    ats "\"One thing that I've always been curious about. What made you take up tennis in the first place? You play with so much passion on the courts, I always wondered what made you choose the sport.\""
    mc 1 c think "\"Huh... I've been interviewed a few times but no one has ever bothered to ask me that question.\""
    ats "\"I know. I read all of your interviews and never saw that question anywhere. That's why I wanted to ask!\""
    "... I can't tell whether I should be disturbed by this statement or not."
    mc 1 c talk "\"My own father taught me to play tennis as a child and I ended up sticking with it. Didn't really notice at first how good of a fit it was for me. Honestly, nowadays I can't even begin to imagine my life without it.\""
    ats "\"Ooh, that's such a prim and proper answer. Your father really raised you well. I would really like to meet the man that raised one of my favorite tennis players!\""
    show j 1 c wince at fdis, shake1
    j "\"Glk...\""
    "Jun chokes on his food, coughing and hacking to try and steady his breathing again."
    "I give him a few taps on the back to help him out."
    j "\"D-dad...\""
    ats "\"What? What's with that reaction? Are you alright?\""
    j "\"I-I'm fine, but... you really shouldn't ask that.\""
    ats "\"H-huh? Why not?\""
    mc 1 c considerate "\"I already told you not to worry about it, Jun. I'm used to it. I get asked about my dad all the time by teachers, coaches and the likes.\""
    mc 1 c wry "\"My father is deceased, Atsushi-san. He died in an accident twelve years ago. It was a hit-and-run.\""
    ats "\"!\""
    "Both of Jun's parents immediately freeze at my words."
    "Yui-san shoots a glare at her husband before reaching out to put a hand on top of my own."
    "Atsushi-san struggles to come up with words, uselessly muttering incoherently to himself."
    yui "\"I'm really sorry to have brought something like that up, [povFirstName]-kun. It was tactless...\""
    mc 1 c considerate "\"No, really, you guys don't have to worry about it. It's something that happened a long time ago, it's not a big deal anymore.\""
    "I really wish people would stop trying to be so considerate over it... it's a lot harder to try to act like nothing happened when everyone is so concerned about my feelings all the time."
    "I hate being put on the spot like this..."
    mc 1 c "\"You don't have to feel upset or anything by this. There's no way anyone could know without being told so, really, it's not your fault.\""
    ats "\"I-I'm really sorry...\""
    mc 1 c considerate "\"Again, it was nothing. Please stop apologizing...\""
    "It just makes it all that much harder to pretend it never happened."
    mc 1 c happy "\"So, uhm... Atsushi-san, you're a police officer, right? What's that like?\""
    "I try to get them to change the subject of conversation. Both for my own sake as well as theirs."
    "From behind the table, I feel something soft rubbing against my back."
    show j 1 c considerate at fdis
    "Jun flashes me a smile... is he trying to comfort me?"
    "In that case, the thing rubbing against my back is probably his tail, right?"
    "I make sure to smile back at him."
    "Bless his heart. He's trying to make me feel better even though I'm insisting that everything is fine."
    show j 1 c watch at fdis
    ats "\"Well, it's a lot less glamorous than it sounds... I just go on patrols quite often. Sometimes alone, sometimes with a partner. I mostly just patrol around the downtown area.\""
    ats "\"So it's really just a lot of walking, some driving and mostly just general boredom.\""
    mc 1 c worried "\"Oh... I'm sorry to hear.\""
    show j 1 c think at fdis
    j "\"Don't let Dad fool you. He loves his job anyway.\""
    mc 1 c shock "\"O-oh...\""
    show j 1 c watch at fdis
    ats "\"I never said I didn't love it. I just said it wasn't as exciting as some people would think.\""
    mc 1 c talk "\"To be honest, not many things are as exciting as others think.\""
    ats "\"That's true too.\""
    yui "\"Hmm... I don't know. I would take being a police officer over what I do any day.\""
    mc 1 c smile "\"What is it that you do, Yui-san?\""
    yui "\"Well, right now I'm working two jobs. On weekdays I'm a saleswoman at this precious little boutique downtown. On weekends I help with stocking at a perfume store.\""
    mc 1 c shock "\"S-stocking?\""
    show j 1 c think at fdis
    j "\"Again, don't be fooled. Mom works with the stocking department... by doing count and general logistics. She doesn't carry anything.\""
    mc 1 c wince "\"O-oh...\""
    "This family loves giving people the wrong idea don't they?"
    yui "\"Hahaha, the look on your face was priceless though. For just a second you were thinking \"Just how strong is this woman?\" weren't you?\""
    "... I take it back, every last person in this house is nuts."
    "The \"happy-go-lucky\" levels are off the charts here."
    stop music2 fadeout 2.5
    scene JunHouse
    show j 1 c watch at fdis, five
    with fade
    play music "music/night.ogg" fadein 5.0
    "It takes me almost two hours to finally get Jun all the way through his homework."
    "I swear, I've never seen someone as bad with math as this guy."
    "Still, after that trial is over, he comes outside to see me off."
    j "\"Are you sure you don't want me to walk you home?\""
    mc 1 c smile "\"Nah, I'm fine. My house isn't that far away.\""
    "Plus, I don't trust you walking around the streets at night. If you're capable of getting lost in broad daylight, I'm not going to take my chances."
    mc 1 c happy "\"Thank you for having me over for dinner. It was really fun, even if we didn't plan for it.\""
    show j 1 c happy at fdis
    j "\"Agreed. We should do that more often.\""
    show j 1 c smile at fdis
    j "\"And thanks for dropping by to visit me. I really appreciated having company today.\""
    show j 1 c considerate at fdis
    j "\"I really hated being cooped up in the house with no one to really talk to.\""
    mc 1 c think "\"That's kind of your own fault. You're the one who told us not to visit.\""
    show j 1 c wince at fdis
    j "\"I guess that's true. Kinda dug my own grave there.\""
    mc 1 c smile "\"Well, just try not to get put under house arrest again and this won't be a problem.\""
    show j 1 c considerate at fdis
    j "\"I kinda want to object to you calling it a house arrest but... it's kinda fitting in a way.\""
    mc 1 c happy "\"Isn't it? Hahaha.\""
    "Jun's tail lazily waves from one side to the other."
    "The calm, refreshing breeze ruffles through our fur."
    "At this moment, I feel oddly satisfied for some reason."
    "Spending this day with Jun was much more... rewarding than I thought it'd be."
    "I don't remember enjoying myself like this in years."
    "Man, I guess I've really come to appreciate his company too, huh? I didn't realize how much I'd missed him the past few days."
    mc 1 c smile "\"I guess I'll see you at school tomorrow then.\""
    show j 1 c happy at fdis
    j "\"Yeah. Why don't you drop by the music room after class? It's been a while since I played for you.\""
    mc 1 c happy "\"Of course. I can't wait to hear your piano again!\""
    mc 1 c smile "\"Just don't go tripping on any shoelaces, okay?\""
    show j 1 c considerate at fdis
    j "\"Yeah yeah. I'll make sure to double-check before I try to get up and walk.\""
    mc 1 c smile "\"Have a good night, Jun. See you tomorrow.\""
    j 1 c happy "\"Good night!\""
    scene SkyN with fade
    "I begin my short walk home."
    "As I turn around to look at his house one last time before turning at the intersection, I see the little tiger still hanging around at the front."
    "He waves at me once he realizes I can see him, bringing another smile to my face."
    $ date = None
    jump Day14_Jun
