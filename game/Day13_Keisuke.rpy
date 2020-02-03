label Day13_Keisuke:
    $ persistent.picked_character = "Keisuke"
    window hide
    scene May21 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    play music "music/cicada01.ogg" fadein 5.0
    scene KeiHouse with fade
    window show
    $ date = "day13"
    "As soon as I step outside of the car, a wave of dry heat assaults me."
    "The sudden shift in temperature sends a shiver down my spine."
    "Kei-kun had sent one of his limousines to pick me up today and that thing has such a powerful AC inside that I felt like I was inside of a blizzard."
    "Well... I might be exaggerating just a tad, but it's true that this thing gets cold as hell."
    show kur 1 u smile at five with dissolve
    kur "\"Good evening, sir. The young master has been expecting you.\""
    mc 1 c talk "\"Young ma- Oh, right, that's Keisuke. I'm not used to hearing him being called that way.\""
    "The fox chuckles, his voice carrying softly and almost melodically through the air."
    "I have to say, he does have a certain... air of elegance to him, even if he is a butler."
    "I guess that's to be expected from someone that works with the rich?"
    kur "\"I suppose there are many things about the young master that would surprise you.\""
    mc 1 c talk "\"I'm not sure if \"surprised\" is the right term for this situation here.\""
    kur "\"Well, no matter. Shall I take you to the young master's room? Or maybe you'd prefer to eat something before you go to him? I could offer you some tea.\""
    mc 1 c shockb "\"N-no, that's fine. I already had lunch.\""
    kur "\"I understand. In that case, follow me.\""
    hide kur 1 u smile with dissolve
    "With a smile, the butler calmly points down the hallway and turns to walk away from me."
    "Huh... did Keisuke grow up with this kind of pampering every day?"
    "In that case, I think he actually turned out more down-to-earth than I'd expect."
    "The more you know..."
    stop music fadeout 2.5
    scene KeiRoom
    play sound "music/slidingdoor.ogg"
    show kur 1 u smile at eight
    with fade
    kur "\"Excuse me, young master. Your guest has arrived.\""
    play music2 "music/BGM/In That Mood.ogg" fadein 5.0
    show k 1 c smile at fdis, five
    show sa 1 c at two
    with dissolve
    k "\"Ah, [povFirstName]-san. Thank you for bringing him here, Kuroda.\""
    kur "\"It was my pleasure. Don't hesitate to call if I am needed.\""
    show k 1 c calm at fdis
    k "\"I won't.\""
    kur "\"Very well. If you'll excuse me, I must return to my duties.\""
    show kur 1 u smile at offscreenright with moveoridis
    show k 1 c smile at fdis, seven
    show sa 1 c smile at fdis, three
    with move
    k "\"Welcome to my house, [povFirstName]-san.\""
    if day5 == "keisuke":
        mc 1 c talk "\"I'm happy to have been invited here again, although... Saya-chan, what are you doing here?\""
        show k 1 c at fdis
        show sa 1 c pout2 at fdis
        sa "\"What do you mean what am I doing here? Am I not allowed to visit a friend?\""
        mc 1 c worried "\"That's not what I mean. I'm just surprised to see you here since Kei-kun said he never invited anyone else to his place. I thought I was the first.\""
        show k 1 c sigh at fdis
        show sa 1 c at fdis
        k "\"Yes, you were the first to visit my house if that is so important to you. I just thought that it was about time that I had someone else over.\""
        show k 1 c at fdis
        k "\"You yourself were the one who told me that I should open up to my friends more, weren't you? So I decided to invite my other closest friend to come today.\""
        mc 1 c smile "\"Ah, I see. I'm glad you're taking my advice!\""
    else:
        mc 1 c talk "\"I'm happy to have been invited, although... I can't lie that I'm a little jealous. It seems I wasn't the first person you ever invited, huh?\""
        "I shoot Saya a curious glance."
        mc 1 c talk "\"Saya-chan, what are you doing here?\""
        show k 1 c at fdis
        show sa 1 c pout2 at fdis
        sa "\"What do you mean what am I doing here? Am I not allowed to visit a friend?\""
        mc 1 c worried "\"That's not what I mean. I'm just surprised to see you here since Kei-kun said he never invited anyone else to his place. I thought I was the first.\""
        show k 1 c sigh at fdis
        show sa 1 c at fdis
        k "\"This isn't a competition, you know.\""
        show k 1 c at fdis
        k "\"Besides, Mizoguchi-san is my closest friend. Does it really surprise you that much that I'd invite her?\""
        mc 1 c talk "\"I guess that's true.\""
    show sa 1 c laugh at fdis
    sa "\"Hey, [povFirstName]-kun, what do you think of this place? Isn't it huge? My jaw nearly hit the floor when I first saw it.\""
    mc 1 c talk "\"It really is. I get the feeling that I'd easily get lost in this place if I didn't have someone guiding me around.\""
    show k 1 c smile at fdis
    show sa 1 c at fdis
    k "\"It's not just a feeling. Getting lost here isn't hard at all.\""
    sa "\"Seriously?\""
    show k 1 c worried at fdis
    k "\"One time, right after I moved here, I got lost in the back garden. It took the servants two hours to find me.\""
    mc 1 c wince "\"Sheesh. Why would someone want a house this needlessly big in the first place?\""
    show k 1 c sigh at fdis
    k "\"I'm afraid the answer isn't gonna do much to help clarify stuff. From what I've learned over the years, it's for no reason other than \"we can\".\""
    show k 1 c at fdis
    sa "\"You're not like that though. Why is that?\""
    show k 1 c worried at fdis
    k "\"Who knows. Perhaps my upbringing before I moved here gives me a little sense of perspective? It's not as if I'm perfectly average either. I'm well aware that I sometimes do or say outlandish things out of my own naivety.\""
    mc 1 c laugh "\"Like thinking a place that charges near minimum wage for a tub of ice cream is \"cheap\".\""
    play sound "music/stab.ogg"
    show k 1 c wince at fdis, shake1
    k "\"Y-yeah. Something like that.\""
    show sa 1 c talk at fdis
    sa "\"You're still pretty easy to talk to. I was really surprised when I found out you were some mega rich kid because you really don't act like it.\""
    show k 1 c considerate at fdis
    show sa 1 c at fdis
    k "\"Heh. I'll choose to take that as a compliment.\""
    show k 1 c smile at fdis
    k "\"By the way, [povFirstName]-san, Saya-chan and I were going to play some games. Wanna join us?\""
    mc 1 c smile "\"Oh? You mean we're not gonna have an obnoxiously fancy tea party?\""
    show k 1 c at fdis
    k "\"Do you even {i}want{/i} something like that?\""
    mc 1 c happy "\"Of course not. I'm sure it'd be very boring anyway.\""
    show k 1 c sigh at fdis
    k "\"Thank God. I was afraid I'd have to actually entertain the idea of drinking tea.\""
    mc 1 c sigh "\"Just because others are doing it doesn't mean you have to too.\""
    show k 1 c avoid at fdis
    k "\"But what about peer pressure?\""
    mc 1 c sigh "\"If we jumped off a building would you just follow suit?\""
    show k 1 c smile at fdis
    k "\"Depends. Are we doing bungee jump?\""
    mc 1 c sigh2 "\"Forget it. The main point is, we don't want a tea party and you don't have to have tea.\""
    show sa 1 c laugh at fdis
    sa "\"I don't know... I kinda like the idea of dressing up and feeling fancy while drinking tea. I wonder if that would make me a proper lady?\""
    show k 1 c worried at fdis
    k "\"That's not...\""
    mc 1 c cocky "\"I think you'd need to grow a pair of boobs first if you wanna be considered a lady.\""
    show sa 1 c at fdis
    show k 1 c shock at fdis, jumping
    play sound "music/recordscratch.ogg"
    stop music2
    "Kei-kun makes a weird choking sound, turning to look at Saya with a gaping mouth."
    "The words slipped out of my mind before I even gave them much thought."
    mc 1 c fsmile "\"I-I mean... y-you're already a real lady, Saya-chan.\""
    "I begin to cower from her, taking a few slow steps back, anticipating the physical punishment that undoubtedly awaits me."
    "Instead, Saya blinks, looking at the two of us confused."
    play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
    sa "\"Why are you guys staring at me like that?\""
    mc 1 c shock "\"Huh?!\""
    show k 1 c worried at fdis
    k "\"Mizoguchi-san... didn't you hear what he just said?\""
    sa "\"I did. So? I mean, he's not wrong.\""
    show k 1 c shock at fdis
    k "\"Wha-\""
    mc 1 c confused "\"Who are you and what did you do to Saya?\""
    play sound "music/badjoke.ogg"
    show sa 1 c talk at fdis
    sa "\"What? Am I supposed to turn into a fire-breathing dragon every time someone makes a joke at my expense or something?\""
    mc 1 c sigh "\"Yes.\""
    show k 1 c worried at fdis
    k "\"That's what we've come to expect of you over time anyway.\""
    show sa 1 c sigh at fdis
    sa "\"...\""
    "..."
    mc 1 c sigh2 "\"Just yell at me already so we can get this over with.\""
    show sa 1 c pout at fdis, jumping
    sa "\"What? No!\""
    mc 1 c avoid "\"Come on. It's for my own peace of mind.\""
    show sa 1 c sigh at fdis
    sa "\"What do I have to do with your peace of mind?!\""
    k "\"I have to admit, this feels really weird.\""
    sa "\"Wha- I don't want to just go around whacking people upside the head whenever they tease me!\""
    show k 1 c sigh at fdis
    k "\"Really? Cause all the experience I've had dealing with you over this past year tells me otherwise.\""
    mc 1 c avoid "\"Seriously. What's with all those bruises we got in the past for making jokes then?\""
    show sa 1 c pout2 at fdis
    sa "\"That's for when you crossed the line!\""
    mc 1 c confused "\"And talking about your nonexistent breasts isn't crossing the line?\""
    show sa 1 c annoyed at fdis
    sa "\"Stop calling them nonexistent!\""
    mc 1 c confused "\"See? This {i}does{/i} upset you. Why the hell aren't you hitting me?\""
    "Saya huffs, her nose twitching multiple times with all those big jets of air."
    sa "\"Has it ever occurred to you that maybe I don't want to be that kind of violent person anymore?\""
    "I sneer, shaking my head sideways."
    mc 1 c sigh2 "\"Yeah, right. As if I'm ever going to buy that excuse.\""
    show sa 1 c shock at fdis
    sa "\"Wha-\""
    show k 1 c worried at fdis
    k "\"It really is hard to believe.\""
    show sa 1 c pout at fdis, jumping
    sa "\"Hey!\""
    mc 1 c sigh "\"You're, like, the most violent person I know.\""
    k "\"Ditto.\""
    sa "\"Do you two really have such a low opinion of me?!\""
    show k 1 c sigh at fdis
    k "\"Mizoguchi-san, there's a difference between an opinion and a fact.\""
    "She grits her teeth, clenching her fists in what are the telltale signs of her fury."
    sa "\"Did I get invited here just so the two of you could mock me?\""
    show k 1 c worried at fdis
    k "\"No. But at this point, I'm not even sure if you're really \"here\". Perhaps I'm dreaming this whole thing up...\""
    mc 1 c sigh "\"That {i}is{/i} one way to explain her weird behavior.\""
    play sound "music/slap.ogg"
    show k 1 c shock at fdis, jumping
    show sa 1 c angry at fdis
    sa "\"Just shut up already!\"" with hpunch
    mc 1 c shock "\"OW!\""
    show k 1 c wince at fdis
    k "\"W-why did I get slapped too?!\""
    show sa 1 c annoyed at fdis
    sa "\"You joined in and mocked me too!\""
    show k 1 c worried at fdis
    k "\"T-that wasn't mocking. I was legitimately concerned that something was wrong.\""
    mc 1 c sigh2 "\"See? I told you. You {i}are{/i} violent.\""
    mc 1 c avoid "\"Damn, this stings... {size=-2}at least all is right with the world again.{/size}\""
    k "\"I don't like this outcome but at least it's one that makes sense...\""
    sa "\"You two suck!\""
    "She crosses her arms, grumbling unhappily."
    show sa 1 c complain at fdis
    sa "\"{size=-2}Jeez, and now I've lost the bet too...{/size}\""
    show k 1 c at fdis
    k "\"Bet? What bet?\""
    show sa 1 c pout2 at fdis
    "She looks away with a huff."
    "I notice that her cheeks are slightly reddened now."
    sa "\"I-It's not your concern.\""
    "Ah..."
    mc 1 c sigh "\"Wait a second...\""
    show sa 1 c avoidb at fdis, jumping
    "As soon as she hears my tone of voice, Saya's entire body freezes."
    mc 1 c sigh2 "\"Did... did you make a bet with someone that you'd be able to stop hitting people or something of the sorts? Because {i}that{/i} would make a lot more sense.\""
    show k 1 c shock at fdis
    k "\"Ah!\""
    show sa 1 c avoidb at fdis, shake1
    "As if he noticed it too, Keisuke looks over at Saya who is now making it a point to look away from us."
    sa "\"I-I don't know what you two are talking about.\""
    show k 1 c sigh at fdis
    k "\"Mizoguchi-san...\""
    show sa 1 c avoidb at fdis, jumping
    "Keisuke's voice came out abnormally stern, almost commanding. Saya jumped and straightened herself out immediately in response."
    show k 1 c doom at fdis
    k "\"Please tell me that I did not just get hit because of a {i}bet{/i}.\""
    sa "\"I-I mean, it wasn't because of the bet... exactly. I-I slapped you because you were-\""
    k "\"So this bet does exist? And if it weren't for this so called bet, you would have reacted when [povFirstName]-san first teased you and I would have remained uninvolved in the whole thing?\""
    show sa 1 c pout2b at fdis
    sa "\"I-I mean... n-not exactly.\""
    k "\"Mizoguchi-san...\""
    "Saya gulps loudly, looking away from the two of us."
    mc 1 c sigh2 "\"Are you freaking kidding me? Who even makes a bet like that? Not hitting people should be a matter of common sense.\""
    show k 1 c sigh at fdis
    k "\"Indeed. What a vulgar little wager...\""
    sa "\"J-Jeez, d-dial down on the judgment a little!\""
    show k 1 c doom at fdis
    k "\"No.\""
    play sound "music/stab.ogg"
    show sa 1 c pout2b at fdis, shake1
    sa "\"Guh...\""
    mc 1 c annoyed "\"Who did you even make a bet with? Anyone who knows any of us even just a little bit would have been able to predict something like this happening...\""
    show sa 1 c sigh at fdis
    sa "\"W-what? Of course not!\""
    show k 1 c at fdis
    k "\"It doesn't take much to imagine that we'd be confused if you suddenly stopped acting like normal. It also doesn't take much to imagine that you'd eventually reach your breaking point if we kept making comments about it.\""
    sa "\"What you guys are suggesting here would require a prophetic degree of foresight...\""
    mc 1 c sigh "\"Would it? Would it really?\""
    show sa 1 c avoidb at fdis
    sa "\"Of course it would. The whole idea is ridiculous!\""
    show k 1 c avoid at fdis
    k "\"Hmm... as much as I hate to admit, it's hard to think of a person that could make those kinds of leaps in logic. Without the gift of hindsight, it {i}would{/i} take a lot of imagination.\""
    mc 1 c sigh2 "\"No... I can think of just the person...\""
    show k 1 c at fdis
    k "\"Really? Who?\""
    show sa 1 c pout2 at fdis
    play sound "music/phonebeep.ogg"
    mc 1 c sigh2 "\"One second.\""
    play sound "music/calling.ogg"
    "..."
    "?" "\"Hello? [povFirstName]?\""
    mc 1 c sigh "\"... Were you the one who made a bet with Saya?\""
    "..."
    "From the other side of the call, laughter begins to echo."
    "Seems he wasn't able to keep a straight face even through the phone..."
    s 1 c laugh "\"Did she lash out on you guys yet?\""
    mc 1 c angry "\"You knew this would happen!\"" with hpunch
    show k 1 c worried at fdis
    k "\"Who did you call?\""
    "Kei-kun stands around, confused. He leans closer to me in an attempt to hear Shoichi's voice on the other end of the line."
    "Meanwhile, Saya is looking away from us both."
    s 1 c smile "\"Of course I did. I know you and Saya better than anyone else. It's not hard for me to imagine you piling on the grief on her until she cracked.\""
    mc 1 c sigh "\"... I swear, I'm gonna hit you tomorrow.\""
    s 1 c happy "\"Be my guest. In the meantime, this is punishment for not inviting me along.\""
    mc 1 c wince "\"I can't invite you to someone else's house!\""
    s 1 c smile "\"I know. That's why I made sure that this would happen with Urushihara around. That way he gets punished too.\""
    mc 1 c annoyed "\"... You're evil.\""
    s 1 c happy "\"Perhaps. Either way, I've got to go. Have fun! Oh, and remind Saya-chan that she owes me ¥6000.\""
    play sound "music/phonebeep.ogg"
    mc 1 c sigh "\"...\""
    show k 1 c at fdis
    k "\"Who was that?\""
    mc 1 c sigh2 "\"Shoichi.\""
    show k 1 c shock at fdis
    k "\"Wha-"
    $ renpy.pause (0.5)
    show k 1 c scorn at fdis
    extend " I'll kill him. I'll just kill him tomorrow.\""
    mc 1 c annoyed "\"Not if I get to him first.\""
    show sa 1 c pout2 at fdis
    sa "\"Aren't you guys going a little too far over a prank?\""
    mc 1 c judge "\"I got slapped over that \"prank\" of his, so no.\""
    show k 1 c at fdis
    k "\"To be fair, you would have gotten slapped regardless. I'm the only one here who's gotten hit unduly.\""
    mc 1 c shock "\"What? No way!\""
    show sa 1 c talk at fdis
    sa "\"Uhm... he's right though. I would have slapped you after the first comment if it weren't for the bet.\""
    mc 1 c pout "\"You hit me and now you're gonna side with him?!\""
    show sa 1 c at fdis
    sa "\"Side with him? There are no sides here. What are you talking about?\""
    mc 1 c sigh2 "\"Ugh... nevermind.\""
    "My cheek's still tingling..."
    show k 1 c sigh at fdis
    k "\"I feel like I've been played.\""
    mc 1 c avoid "\"We've all been played... but it was mostly Saya.\""
    show sa 1 c sigh at fdis
    sa "\"Do you want me to hit you again?\""
    mc 1 c wince "\"N-no, ma'am.\"" with hpunch
    show sa 1 c at fdis
    k "\"Spineless.\""
    mc 1 c annoyed "\"Be quiet.\""
    stop music2 fadeout 2.5
    play music3 "music/BGM/Let It Happen - Narr.ogg" fadein 5.0
    show k 1 c at fdis
    k "\"Well, feel free to continue grumbling like a child. I'm going to get back to what we were doing before.\""
    mc 1 c shock "\"Wha- You mean you won't help me plot Shoichi's demise?!\""
    show k 1 c sigh at fdis
    k "\"Demise? What are you, a child? I'm just gonna try to have fun like we were going to.\""
    show sa 1 c think at fdis
    sa "\"Yeah, [povFirstName]-kun. I'm the one who lost money here, why are you complaining?\""
    show sa 1 c at fdis
    mc 1 c sigh "\"Does my dignity mean nothing to you people?\""
    show k 1 c at fdis
    k "\"No.\""
    show sa 1 c pout2 at fdis
    sa "\"Nu-uh.\""
    show k 1 c eyesc at fdis
    show sa 1 c at fdis
    k "\"Not one bit, in fact.\""
    mc 1 c annoyed "\"... You two are horrible.\""
    show k 1 c smile at fdis
    k "\"It's my pleasure."
    show k 1 c at fdis
    extend " Now, to choose a game to play... or what console to play.\""
    show sa 1 c smile at fdis
    sa "\"Why don't you just help us, [povFirstName]-kun. That way it'll go faster.\""
    mc 1 c sigh "\"{size=-2}Jeez, no one really cares at all...{/size}\""
    show k 1 c sigh at fdis
    k "\"Stop mumbling to yourself and get over here already.\""
    mc 1 c wince "\"You're so mean!\""
    k "\"Yeah yeah. Haven't you heard? I'm horrible. Now get to it.\""
    mc 1 c sigh "\"What's the point? We can't play most games with only three people.\""
    show k 1 c shock at fdis
    show sa 1 c think at fdis
    k "\"Ah...\""
    sa "\"Oh yeah, that's true.\""
    show k 1 c sigh at fdis
    k "\"Fuck...\""
    show sa 1 c at fdis
    mc 1 c shock "\"What? Did I just hear you {i}curse{/i}?. The prim and proper Kei-kun?\""
    show k 1 c shock at fdis
    $ renpy.pause(1.0)
    show k 1 c avoidb at fdis
    k "\"You heard nothing.\""
    mc 1 c happy "\"I'm {i}pretty{/i} sure I-\""
    show k 1 c angry at fdis
    k "\"You. Heard. Nothing!\""
    mc 1 c shock "\"Waah! Okay, okay. I heard nothing!\""
    show k 1 c sigh at fdis
    "Keisuke sighs, rubbing his forehead, his nose and brow twitching repeatedly."
    show sa 1 c talk at fdis
    sa "\"What will we do? Should we just play normal 2-player games and trade controllers?\""
    mc 1 c think "\"We could also just pick up some 4-player party game and play against a CPU.\""
    show sa 1 c pout2 at fdis, jumping
    sa "\"But playing against the CPU is super boring.\""
    mc 1 c sigh "\"It's better than having to trade controllers. That means one-third of everyone's time will be spent not playing.\""
    show sa 1 c at fdis
    sa "\"That's true...\""
    show k 1 c at fdis
    k "\"Actually, I have an idea.\""
    mc 1 c curious "\"Oh?\""
    play sound "music/phonebeep.ogg"
    "Kei-kun fiddles with his phone, typing something on it.\""
    show k 1 c calm at fdis
    k "\"There. It shouldn't take very long now.\""
    show al 1 u at offscreenright
    mc 1 c curious "\"What did you-\""
    play sound "music/slidingdoor.ogg"
    show sa 1 c shock at fdis, two behind k
    show k 1 c smile at fdis, five
    with move
    show al 1 u at eight behind k with moveiridis
    al "\"You called me?\""
    sa "\"Eep!\""
    "Just then, a towering, muscled wolf wearing a tight butler vest walked into the room."
    "His eyes looked stern and unapproachable. Definitely not the friendlist looking person I've seen."
    if day10 == "keisuke":
        "It seems Alex hasn't changed at all since I last met him... although I suppose that's to be expected."
    sa "\"B-big...\""
    "The wolf's ears twitched at those words, focusing his eyes on the frightened looking bunny."
    show sa 1 c shock at fdis, jumping
    sa "\"Eep!\""
    show k 1 c sigh at fdis
    k "\"Calm down, Saya-chan. He's a friend.\""
    show k 1 c smile at fdis
    k "\"This is Alexander, he's been my butler and friend for years. Feel free to call him Alex.\""
    al "\"Hello.\""
    "The wolf nods at us, looking us both up from top to bottom."
    al "\"I am also his bodyguard. {i}That{/i} is my main occupation.\""
    show k 1 c avoid at fdis
    k "\"There's no need to bring that up, Alex. It's not like I'm in need of protection in the first place.\""
    al "\"Oh. You mean to tell me that I imagined the pay-cut I received after your wallet was stolen just a few days ago?\""
    play sound "music/stab.ogg"
    show k 1 c wince at fdis, shake1
    k "\"Guh... Fair point.\""
    "The wolf's eyes settle on me."
    "Even though I know I shouldn't, I still get a little nervous when that piercing gaze is pointed right at me."
    show k 1 c at fdis
    al "\"If I remember correctly, you are [povFirstName], yes?\""
    if day10 == "keisuke":
        mc 1 c shock "\"Y-yeah. We met a while ago. Nice to see you again.\""
        al "\"Mhm.\""
    else:
        mc 1 c shock "\"H-how do you know?\""
        al "\"He's told me in the past of his friend \"[povFirstName]\" who was a shiba and had your features. I'm not going to go through the trouble of giving you the description he used.\""
        mc 1 c fsmile "\"I-I see. It's a pleasure to meet you, A-Alex.\""
        al "\"Mhm.\""
    "His voice and expression are so maddeningly devoid of emotion."
    "What's with so many people around me being so hard to read?"
    al "\"And you're the one that was with Keisuke when his wallet was stolen.\""
    stop music3
    "My stomach immediately sinks at those words."
    "Oh God, he's going to blame me for that isn't he?"
    show k 1 c serious at fdis
    k "\"Alex...\""
    "Keisuke's fur bristles up around his neck as he stares dangerously at the wolfman that easily towers over him."
    "Without even looking at his employer, Alex holds up a hand as if to say \"wait\"."
    al "\"Thank you for teaching this foolish fool about how careless he's been.\""
    show k 1 c shock at fdis
    play music2 "music/BGM/Dazzling Sunlight.ogg" fadein 5.0
    "Keisuke, Saya and I nearly hit the floor with our jaws once he utters those words."
    "Then, as if to say that he was having fun at our expense when we thought he was about to chastize me, the corners of his mouth quirk up in amusement."
    show k 1 c angryb at fdis
    k "\"Did... did you just call me a fool? {i}Twice{/i}.\""
    al "\"I'll call you that a third time if need be. Maybe even a fourth for good measure.\""
    k "\"Alex!\""
    show sa 1 c laugh at fdis
    sa "\"Snnrk...\""
    "Saya looks away from the two, covering her mouth as she attempts to keep herself from bursting into laughter."
    k "\"D-don't laugh!\""
    al "\"You seem to be very flustered at the moment. Should I get you some tea?\""
    k "\"And don't tease me either!\""
    "... These two have a friendlier relationship than I thought they would considering their circumstances."
    "I guess I was worried over nothing, huh?"
    show sa 1 c at fdis
    al "\"Regardless, [povFirstName]. Thank you for going through the trouble of helping this fool to get me a gift. It was ultimately unnecessary, but I still appreciate the gesture.\""
    k "\"There it is. You just called me a fool again!\""
    al "\"Yes, I did. You have good ears, {i}Young Master{/i}.\""
    show k 1 c worried at fdis
    k "\"Eugh... don't call me that. It just sounds gross when you do it.\""
    al "\"As you wish, {i}My Lord{/i}.\""
    show k 1 c angryb at fdis
    k "\"We're not in the middle ages!\""
    al "\"I see. Forgive me, {i}Your Grace{/i}.\""
    show k 1 c sigh at fdis
    k "\"... Now you're just mocking me, aren't you?\""
    al "\"What was your first clue?\""
    "Even I'm unable to hold back my laughter as they continue to bicker amongst themselves."
    "Or, in this case, Kei-kun continues to bicker with what is basically a giant brick wall, as Alexander's facial expression doesn't shift even a little bit through this whole exchange."
    show k 1 c avoid at fdis
    k "\"Yeah yeah, make fun of me, why don't you...\""
    al "\"Excuse me, Keisuke, but if you're just going to sulk around instead of telling me what you wish for me to do then may I be excused?\""
    show k 1 c sigh at fdis
    k "\"... I'm not going to take the bait this time.\""
    al "\"Oh, too bad. I'm one for two, I guess.\""
    show k 1 c at fdis
    k "\"The reason I called you over is because we need one other player.\""
    al "\"One other pla-\""
    "Alexander at first begins to repeat Keisuke's request until the words sink in and he starts looking from the hare to the entertainment center right next to us."
    "After a few seconds he wordlessly points at the videogames and then back at him, as if asking confirmation on the seemingly absurd request he was just given."
    show k 1 c haughty at fdis
    k "\"Yes, I {i}am{/i} asking you to play games with us.\""
    al "\"Keisuke, I hardly think that's appro-\""
    show k 1 c calm at fdis
    k "\"You're my personal butler among other things, no? That means you do what I ask you to do. I'm asking you to play games with us. I hardly think that's a complicated request.\""
    "The wolf raises an eyebrow as if he was still having trouble believing the words he was hearing."
    al "\"While that is the gist of things, I do not think your grandmother would approve of such a thing.\""
    show k 1 c at fdis
    k "\"Grandmother doesn't approve of anything. Besides, the old hag isn't home now, is she?\""
    al "\"No. The mistress is visiting a friend's estate in the next town over and isn't expected home until tomorrow.\""
    show k 1 c calm at fdis
    k "\"See? There's nothing to worry about.\""
    al "\"I disagree, but I see that your mind is made up.\""
    show k 1 c smile at fdis
    k "\"It is. You'll play games with us. End of story.\""
    "The wolf closes his eyes, pondering those words for a while."
    al "\"Very well. Either way this is hardly the most absurd request you've made of me over the years.\""
    show k 2 c gentle at fdis
    k "\"There is some truth to that, yes.\""
    show sa 1 c talk at fdis
    sa "\"Uhm...\""
    "Saya lifts up her hand as if she were trying to ask a question of the teacher in class."
    "Well, I'll admit that it was hard to find an opportunity to interject in the middle of their conversation."
    "Kinda like... there was no space left for someone else in that exchange?"
    "I guess she's gonna ask how we'll choose the pairs. That's what I was about to as-"
    sa "\"I have no idea what's going on right now, but Mr. Wolf looks really climbable. Can I climb him?\""
    show k 1 c shock at fdis
    "..."
    mc 1 c sigh "\"... What?\""
    "Even Alexander's expression falters for a second, looking at Saya with confusion and incredulity transparently showing on his face."
    al "\"I am not a rock climbing wall.\""
    show sa 1 c pout2 at fdis
    sa "\"Awww...\""
    "For some reason, she seems incredibly dejected at her weird request being denied."
    k "\"Mizoguchi-san, please have {i}some{/i} sense of timing.\""
    show sa 1 c at fdis
    sa "\"When is it ever the right timing for you to ask to climb someone?\""
    show k 1 c avoid at fdis
    k "\"... Fair point.\""
    show k 1 c at fdis
    "I clear my throat, calling everyone's attention towards me."
    mc 1 c sigh2 "\"If I may redirect this conversation back to normality?\""
    show k 1 c sigh at fdis
    k "\"Please do. I beg you.\""
    mc 1 c "\"How will we decide on the pairs? I know we haven't even decided what games to play, but it {i}would{/i} be much easier to decide who we're going to be playing with first.\""
    show k 2 c think at fdis
    k "\"Hmm... that's true.\""
    show k 1 c at fdis
    k "\"I think I'd be able to get along well with whoever I were to pick as my partner so maybe it wouldn't be fair for me to be the one choosing. On the other hand, if we were to leave it to chance, I'm the only one that does well no matter the result.\""
    show sa 1 c talk at fdis
    sa "\"That's true. Maybe we should have Alexander pick since the only good pairing for him would be with you?\""
    al "\"While I appreciate the sentiment, I believe the guests should get to pick before the servant.\""
    mc 1 c considerate "\"That's... a surprisingly hardcore thing to hear, even if it's true.\""
    sa "\"What should we do, [povFirstName]-kun?\""
    mc 1 c curious "\"Maybe we should flip a coin to decide which of us two gets to pick?\""
    show sa 1 c smile at fdis
    sa "\"I like that idea, let's go with that. Do you have a coin?\""
    mc 1 c avoid "\"Erm... no.\""
    show sa 1 c bored at fdis
    sa "\"Then that's a stupid idea. Why did you suggest that?\""
    "What happened to you liking the idea? Jeez, so quick to judge..."
    k "\"I have a coin. Here, I'll flip it. [povFirstName]-san, you call it.\""
    show sa 1 c pout2 at fdis
    sa "\"Why does [povFirstName]-kun get to call it?!\""
    show k 1 c annoyed at fdis
    k "\"Because it was his idea.\""
    "Saya grumbles unhappily, crossing her arms and tapping her foot a few times."
    sa "\"That's fair, I guess...\""
    k "\"Okay. Call it before I flip.\""
    show sa 1 c at fdis
    menu:
        "Heads":
            mc 1 c curious "\"Heads.\""
            show k 1 c at fdis
            k "\"Alright, I'll flip it now.\""
            play sound "music/cointoss.ogg"
            "..."
            k "\"It's heads. [povFirstName]-san gets to pick.\""
            show sa 1 c pout2 at fdis
            sa "\"Rats.\""
            mc 1 c sigh "\"Don't be a sore loser.\""
            "She merely huffs in response."
            k "\"Who will you pick as your partner?\""
            show sa 1 c at fdis
            mc 1 c think "\"Hmm... that's a very good question.\""
            menu:
                "Alexander":
                    mc 1 c smile "\"I'll go with Alex.\""
                    show sa 1 c annoyed at fdis
                    sa "\"Boo, I wanted to pick him!\""
                    show k 1 c worried at fdis
                    show sa 1 c at fdis
                    k "\"Why Alex? It's the one disadvantageous pairing for you.\""
                    mc 1 c considerate "\"I mean, if you think about it, the only way we'd be able to make good pairings for everyone with Alex around would be if I partnered with Saya. That's kinda restrictive.\""
                    show k 2 c annoyed at fdis
                    k "\"Hmm... I suppose you're right about that.\""
                    show k 1 c at fdis
                    k "\"Still, you don't know Alex at all. Will you two even be able to cooperate?\""
                    mc 1 c excited "\"We both have mouths. It's all a matter of communication!\""
                    show k 1 c sigh at fdis
                    k "\"Why do I get the feeling that these words are going to blow up royally in your face?\""
                    show k 1 c at fdis
                    k "\"What about you, Alex? Are you okay with pairing up with [povFirstName]-kun?\""
                    al "\"I don't mind it. Besides, I think this is a good opportunity to get to know the person you spend so much time with a little better.\""
                    show k 1 c avoid at fdis
                    k "\"So this turned into a character interview...\""
                    mc 1 c smile "\"I'm okay with that. After helping you pick that gift for Alex and talking about him so much, I kinda want to know him better.\""
                    al "\"Agreed. Those are logical reasons that I can live with. I believe we'll make for a good duo.\""
                    mc 1 c happy "\"Hehe. Onto victory, I say!\""
                    show k 1 c sigh2 at fdis
                    k "\"Just don't come to me to complain later...\""
                    scene KeiRoom with fade
                    "It took a lot of digging around before we'd each found games that we wanted to play."
                    "Alexander refrained from joining the discussion on what we should play, but he still picked up a game from the pile."
                    "I guess he's just not very vocal about his preference?"
                    "Either way, since we couldn't settle on which one we'd choose with everyone having a different opinion, we decided to leave it to chance again."
                    "The four of us played Rock Paper Scissors until the winner was decided."
                    show al 1 u at five with dissolve
                    "In this case, it was Alex."
                    show al 1 u at eight with move
                    show sa 1 c at fdis, two
                    show k 1 c at fdis, five
                    with dissolve
                    al "\"I'm not really sure what to do here.\""
                    show k 1 c smile at fdis
                    k "\"Just pick whatever you like.\""
                    al "\"There isn't something I \"like\". I never play videogames.\""
                    show k 1 c at fdis
                    k "\"You've played them with me a few times. It's not like you're completely inexperienced with them.\""
                    al "\"True, but I also don't know them enough to just choose something.\""
                    show k 2 c think at fdis
                    k "\"I suppose that's true...\""
                    mc 1 c curious "\"Do you have a genre you like? Maybe we could help you pick a game if you told us what kind of game you'd go for.\""
                    show k 1 c smile at fdis
                    k "\"Oh, that's actually a good idea.\""
                    show k 1 c at fdis
                    al "\"Hmm... I haven't played many games with Keisuke before, but I seem to remember doing better with the shooters.\""
                    mc 1 c fsmile "\"S-shooters?\""
                    al "\"Yes. Is that a problem?\""
                    mc 1 c considerate "\"Not a problem... per se. I'm just not very good at those...\""
                    al "\"Oh. Right, I should pick something that my partner excels at so we have a higher chance of winning.\""
                    mc 1 c shock "\"No no. Just pick whatever you like. It'll be fine!\""
                    al "\"Are you certain?\""
                    show sa 1 c sigh at fdis
                    sa "\"Jeez, can't you two just settle on something already? We're supposed to be playing a game, not watching a debate.\""
                    al "\"Right. I'm sorry. I guess I'll go with a shooter. What are the options?\""
                    show sa 1 c at fdis
                    show k 2 c annoyed at fdis
                    k "\"Well... I don't play shooters all that often so I don't have many to begin with. If you also include the fact that it has to be 4-player compatible then there's only one or two that I have.\""
                    show k 1 c smile at fdis
                    k "\"I'll just pick whichever one is newest.\""
                    al "\"Fair enough.\""
                    "Keisuke starts fiddling with his games to look for the one we're going to play whilst Saya walks up to him, probably so they can talk about what they're going to do."
                    show k 1 c smile at fdis, offscreenleft
                    show sa 1 c at offscreenleft
                    show al 1 u at five
                    with move
                    mc 1 c curious "\"Are you any good with shooters?\""
                    "I look at the wolf with curiosity, trying to somehow get a feel for my partner."
                    "We do need to cooperate in order to win after all."
                    al "\"I think so. We'll see.\""
                    mc 1 c worried "\"... That doesn't exactly fill me with confidence.\""
                    al "\"Would you prefer I lie?\""
                    mc 1 c sigh2 "\"No, I prefer knowing what to expect. I just wish I could have more confidence in what I'm expecting.\""
                    al "\"I'll do my best, I suppose. How's that for encouragement?\""
                    mc 1 c considerate "\"A little better, but not by much.\""
                    al "\"I see.\""
                    "Oh man, we're going to get massacred aren't we?"
                    "Keisuke finally finds the game and pops the disc into the console, turning on his TV and giving each of us a controller."
                    "We're welcomed to a rather sober-looking menu screen that immediately gets passed onto multiplayer mode."
                    show al 1 u at fdis, eight
                    show k 1 c at fdis, five
                    show sa 1 c at fdis, two
                    with move
                    k "\"Alright, I've put us into character selection... or at least what passes for it in this game. It's only really choosing what appearance you want.\""
                    k "\"You get to pick your weapons as soon as the map loads so don't forget to do that.\""
                    mc 1 c worried "\"Got it.\""
                    sa "\"Why are you looking so glum?\""
                    mc 1 c wince "\"Shooters really aren't my thing so I'm afraid I'll be useless here.\""
                    show sa 1 c smile at fdis
                    sa "\"I don't play them much either but I think they can be really fun.\""
                    mc 1 c sigh2 "\"I think I just have to hope for the best.\""
                    show k 1 c smile at fdis
                    k "\"You shouldn't have to worry much. Alex might be humble about it, but even without experience he's pretty good at shooters.\""
                    mc 1 c shock "\"Wait, really?\""
                    show k 1 c sigh2 at fdis
                    k "\"Yeah. It's one of the reasons I never play them with him. He always kicks my ass. There's no fun to be had when you're constantly getting killed.\""
                    al "\"Sorry.\""
                    show k 1 c smile at fdis
                    k "\"You don't have to apologize. It's just a me thing.\""
                    show k 1 c at fdis
                    k "\"Is everyone ready?\""
                    mc 1 c worried "\"I think so. As ready as I can be anyway.\""
                    k "\"I'll press Start then.\""
                    "As soon as we get past the loading screen, we're spawned in what looks like a desert base map."
                    "The place seems to be in ruins, with lots of rubble fallen all over the place, holes in the walls and floor that you can walk through and a lot of other stuff."
                    "I have to admit, I'm pleasantly surprised by the level of detail."
                    mc 1 c "\"{size=-2}What do you think we should do?{/size}\""
                    "I lean towards Alex to ask him for advice on our situation before the killing starts."
                    al "\"Just make sure to always check the rooms before walking in. Peek over the walls and things of the sort, always look where you're going. That should keep you from getting taken out from behind.\""
                    mc 1 c shock "\"I'll keep that in mind. Anything else?\""
                    al "\"Don't die.\""
                    mc 1 c wince "\"T-that's not helpful.\""
                    "The wolf grins, looking somehow very amused by my hesitation."
                    al "\"I know.\""
                    "He's definitely having fun at my expense..."
                    "Alex and I move around the map together. It quickly becomes obvious to me that I'm just walking around randomly while he follows me."
                    "It seems that he's trying to watch my back even though I have no idea what I'm doing."
                    "The gesture certainly makes me feel a little touched that he's so thoughtful over someone who might just end up weighing him down."
                    "I try resisting the urge to peek at Saya and Keisuke on the screen to find out where they are. That would just be unsportsmanlike behavior."
                    al "\"Watch o-\""
                    play sound "music/blaster.ogg"
                    mc 1 c dismay "\"Gah!\"" with hpunch
                    "Before I have time to react, my character is hit squarely in the chest by something."
                    "Luckily, my health didn't drop to 0 and I was able to hide behind the corner we were turning to escape."
                    al "\"I told you to check before turning corners.\""
                    mc 1 c dismay "\"W-what the hell was that?\""
                    al "\"A blaster shot. Probably from a sniper rifle. That's why I told you to be careful.\""
                    mc 1 c shock "\"T-there's a hole on my character's chest. Why is there a hole in my character's chest?!\""
                    k "\"Oh yeah. I forgot to tell you. This game is pretty gory.\""
                    show sa 1 c laugh at fdis
                    sa "\"Cool!\""
                    mc 1 c frownj "\"Not cool! I don't want to see a freaking hole seeping out blood from my chest!\""
                    show sa 1 c smile at fdis
                    sa "\"Then don't get shot.\""
                    al "\"It's just a little bit of blood. Stop freaking out.\""
                    mc 1 c avoid "\"How can you guys be so nonchalant towards this stuff?\""
                    k "\"It's digital blood, I don't know what's got you so riled up.\""
                    show k 1 c smile at fdis
                    k "\"Besides, you're leaving your guard down.\""
                    al "\"Duck.\""
                    mc 1 c shock "\"What?\""
                    al "\"Duck!\""
                    play sound "music/blaster2.ogg"
                    "Two shots fly right above my head less than a second after I hit the crouch button on the controller."
                    mc 1 c dismay "\"Waaah! H-he can hit me from here?\""
                    al "\"We're in a bad position here. Let's retreat for now.\""
                    show sa 1 c laugh at fdis
                    sa "\"Like I'll let you!\""
                    play sound "music/explosion.ogg"
                    "Suddenly my whole screen turns into a shower of red as I watch an explosion coming from below my character, turning him into a million small bits and pieces."
                    mc 1 c dismay "\"Awawawawawa.\"" with hpunch
                    show k 1 c haughty at fdis
                    k "\"Nice! [povFirstName]-san eliminated. Now for Alex.\""
                    show sa 1 c at fdis
                    mc 1 c dismay "\"W-what the hell just happened?\""
                    al "\"You were standing around without paying attention to the map and didn't see them closing into your position.\""
                    mc 1 c wince "\"W-weren't you with me? Did you just abandon me? Alex, why didn't you help me?!\""
                    al "\"I'm not a babysitter. Those who get distracted are the first ones to die on the battlefield.\""
                    mc 1 c pout "\"This isn't a battlefield!\""
                    al "\"At present it is.\""
                    mc 1 c sigh2 "\"You're acting way too hardcore about a videogame.\""
                    show k 1 c at fdis
                    k "\"[povFirstName]-san, you're complaining too much. It's just a game. Relax.\""
                    mc 1 c pout "\"I just watched myself get blown up to a million pieces. That's not \"just a game\", that's nauseating. Why do you even have a game like this?!\""
                    k "\"I bought it so I could play with Alex, although we never got around to doing it much.\""
                    al "\"I already told you that I don't have the time to play videogames often.\""
                    k "\"So I've heard.\""
                    mc 1 c sigh "\"Excuse me, but aren't you doing the exact same thing you chastised me for doing not thirty seconds ago?\""
                    al "\"Hardly.\""
                    play sound "music/blaster.ogg"
                    "I watch Alex shoot at what seemed like nothing."
                    "Then someone's head pops through the corner at that exact second and gets immediately blown out by the stray shot."
                    show sa 1 c shock at fdis, jumping
                    show k 1 c shock at fdis
                    sa "\"What the-\""
                    k "\"Mizoguchi-san!\""
                    mc 1 c shock "\"How did you do that? Did you just shoot at random?\""
                    al "\"Of course not. If you pay attention, you can hear the sounds of footsteps. I just calculated how long it'd take for that person to reach the corner and shot.\""
                    mc 1 c avoid "\"You've got to be kidding me.\""
                    show sa 1 c bored at fdis
                    al "\"It's not hard. It's just a matter of experience.\""
                    "I'm scared to ask what this \"experience\" might be so I'll just keep my trap shut."
                    al "\"What was it that you said? Oh, that's right. One eliminated, only Keisuke to go.\""
                    show k 1 c worried at fdis
                    k "\"Crap.\""
                    al "\"Hiding won't do you any good. Here, the order might be inverted but I'll make sure to return your earlier present grenade.\""
                    show k 1 c shock at fdis
                    k "\"Wai-\""
                    play sound "music/explosion.ogg"
                    show k 1 c shock at fdis, shake1
                    k "\"Ahhh!\""
                    mc 1 c avoid "\"Ugh... all this gratuitous gore is still sickening.\""
                    al "\"I like it.\""
                    mc 1 c sigh2 "\"... I see.\""
                    "This guy is terrifying in his own way."
                    "A screen pops up announcing our team's victory as well as performance stats."
                    mc 1 c avoid "\"Zero percent accuracy... I guess that's to be expected since I didn't fire a single shot.\""
                    "I got totally carried by Alex. It's embarrassing to have played so badly."
                    sa "\"Haah, I wish I'd have gotten Alex as my partner instead...\""
                    show k 1 c angryb at fdis
                    k "\"H-hey!\""
                    show sa 1 c at fdis
                    sa "\"Oh, did I say that out loud?\""
                    show k 1 c avoid at fdis
                    k "\"You did. It's not like you did much either. You got killed instantly.\""
                    show sa 1 c pout at fdis
                    sa "\"Hey, I'm the one who killed [povFirstName]!\""
                    k "\"Like that was a hard thing to do.\""
                    "It seems that defeat hasn't done their teamwork any favors."
                    "Talk about a fragile alliance."
                    show sa 1 c pout at offscreenleft
                    show k 1 c at offscreenleft
                    show al 1 u at five
                    with move
                    al "\"I can give you a few tips on how to play better if you'd like.\""
                    mc 1 c shock "\"R-really?\""
                    al "\"Yes. Knowing Keisuke, he'll probably want to play a few more rounds so he can win at least once.\""
                    mc 1 c avoid "\"Yeah, he can be really competitive when he wants to be.\""
                    al "\"I'll try to explain it in a way that makes it easy for you to understand. Make sure to pay attention.\""
                    mc 1 c shockb "\"Y-yes sir!\""
                    "I guess he doesn't think I'm completely hopeless yet."
                "Keisuke":
                    mc 1 c smile "\"Keisuke, I choose you!\""
                    show k 1 c sigh2 at fdis
                    k "\"What am I, a Pokemon?\""
                    mc 1 c happy "\"Something like that!\""
                    show sa 1 c shock at fdis
                    sa "\"Wait, does this mean that I get Alex?\""
                    mc 1 c considerate "\"Yeah. Sorry if you do-\""
                    show sa 1 c laugh at fdis
                    sa "\"Cool!\""
                    show sa 1 c laugh at fdis, offscreenright, jumping
                    show al 1 u at offscreenright
                    with move
                    "She immediately hops right next to the wolf, who stares at her with confusion."
                    sa 1 c laugh "\"Can I climb you?\""
                    al "\"We've been over this.\""
                    sa 1 c pout2 "\"Aww.\""
                    show k 1 c at fdis
                    k "\"Glad to see Mizoguchi-san is... happy?\""
                    mc 1 c confused "\"Your guess is as good as mine.\""
                    show k 1 c smile at fdis
                    k "\"Well, might as well take this chance to show them who's boss.\""
                    mc 1 c happy "\"Damn right! {size=-2}Though I never thought I'd hear you using that expression in my life.{/size}\""
                    label KeiPair:
                    scene KeiRoom with fade
                    "It took a lot of digging around before we'd each found games that we wanted to play."
                    "Alexander refrained from joining the discussion on what we should play, but he still picked up a game from the pile."
                    "I guess he's just not very vocal about his preference?"
                    "Either way, since we couldn't settle on which one we'd choose with everyone having a different opinion, we decided to leave it to chance again."
                    "The four of us played Rock Paper Scissors until the winner was decided."
                    show k 1 c smile at fdis, five with dissolve
                    "In this case, it was Keisuke."
                    show sa 1 c sigh at fdis, two behind k
                    show al 1 u at eight behind k
                    with dissolve
                    sa "\"Did we really have to go with a tennis game of all things?\""
                    show k 1 c calm at fdis
                    k "\"I won that competition fair and square. I get to pick.\""
                    show sa 1 c pout2 at fdis
                    sa "\"But it's so booooring!\""
                    show k 1 c sigh2 at fdis
                    k "\"You're a tennis player. How can you even say something like that?\""
                    sa "\"Playing tennis is only fun if you're actually playing it. Tennis games are just dull.\""
                    mc 1 c talk "\"I actually agree with Saya-chan on this one.\""
                    show k 1 c sigh at fdis
                    k "\"You guys make me sad...\""
                    show k 1 c at fdis
                    show sa 1 c at fdis
                    mc 1 c "\"Besides, isn't this going to be hard for Alex? He's the only one here that isn't a tennis player. Does he even know the rules.\""
                    al "\"I do. There's no need to worry about me.\""
                    show sa 1 c laugh at fdis
                    sa "\"See? Isn't my partner awesome?\""
                    mc 1 c annoyed "\"We haven't even loaded into the game yet. Save the gloating for later.\""
                    sa "\"We're going to ruin your asses. Just you wait.\""
                    mc 1 c sigh "\"At least learn to trash-talk properly. That sounds like a line straight out of a gay porn movie.\""
                    show sa 1 c at fdis
                    show k 1 c sigh2 at fdis
                    k "\"How would you even know?\""
                    mc 1 c considerate "\"Hey, imagination is a thing that exists you know.\""
                    k "\"Translation: \"I have no idea. I just wanted to say that\", right?\""
                    mc 1 c happy "\"Pretty much.\""
                    show k 1 c sigh at fdis
                    k "\"You're ridiculous...\""
                    show sa 1 c happy at fdis
                    "Saya leans towards Alexander's ears. The wolf curves himself down so she can reach him on the tip of her toes."
                    sa "\"{size=-2}Let's just let them implode before we start, then we'll have it in the bag.{/size}\""
                    show k 1 c scorn at fdis
                    show sa 1 c at fdis
                    k "\"I heard that.\""
                    mc 1 c sigh "\"Same here.\""
                    show k 1 c serious at fdis
                    k "\"Let's just pick our players and get started already. I suddenly feel an itch to play.\""
                    mc 1 c sigh "\"How should we divide our tasks? Should we have one player dedicated to the baseline and the other to the net?\""
                    k "\"Sounds good to me. I'll let you handle the baseline since you have better sense for that.\""
                    mc 1 c sigh "\"Got it.\""
                    al "\"I think your attempt at stealthy trash-talking just served to fill them with motivation.\""
                    show sa 1 c complain at fdis
                    sa "\"Damn...\""
                    show sa 1 c at fdis
                    "We look through a list of famous professional players in the current circuit and immediately pick out the ones we want to play as."
                    "Keisuke picks a player well known for his precise volleying and good footwork. I pick a player that has strong shots and serve."
                    "Alex goes with a defensive player while Saya picks an ultra-aggressive serve-and-volleyer."
                    "Right off the bat, I can already tell that this isn't the most realistic game out there."
                    "No matter how much power I put into my shots, they always seem to land inside the court with no problems."
                    "Not only that, it seems that timing is absolutely irrelevant in this game. You just press the button when you feel like it and as long as the ball hasn't gone past you yet, you get it perfectly."
                    "Not the most engaging way to start a match but I guess it'll have to do."
                    "It's not like they can do a perfect 1-to-1 conversion of the real life game to this virtual system."
                    "Wonky controls aside, there doesn't seem to be much cohesion to what Saya and Alex are doing. They're just... kinda doing their own thing with no rhyme nor reason."
                    k "\"I'm gonna try a sharp angle shot that'll leave us a little open. Walk back a few steps to increase your defensive range!\""
                    mc 1 c "\"Will do.\""
                    "On the other hand, with Keisuke barking out short, cohesive orders, it's hard for us to not be organized."
                    "It's not very fun getting constantly told what to do, but I'll just let it slide since what he says is usually the ideal thing to do regardless.\""
                    show k 1 c haughty at fdis
                    k "\"Yeah, that's right. If we go at them this way, they'll have no choice but to back up into a more defensive position.\""
                    show sa 1 c complain at fdis, shake1
                    sa "\"Guh... Kei-kun, stop analyzing us!\""
                    show k 1 c annoyed at fdis
                    k "\"Don't be ridiculous. If you can't play using your brains then that's your problem. I'll use mine, thank you very much.\""
                    show sa 1 c pout2 at fdis
                    sa "\"I would so hit you for that comment just now but I can't let go of my controller.\""
                    al "\"I will allow no such thing under my watch.\""
                    show k 1 c serious at fdis
                    mc 1 c think "\"Careful, Saya-chan. If you try to hit Kei-kun with Alex around, he just might throw you out the window.\""
                    show sa 1 c pout2 at fdis, fidget
                    sa "\"Ugh, so annoying...\""
                    "We chose to only play a one-set match so it wouldn't go on for very long."
                    show sa 1 c at fdis
                    "Tennis games, even the less realistic ones, have the annoying habit of being super realistic when it comes to the time it takes to get through a match."
                    "Saya and Alexander's play is disorganized enough that we have a clear advantage, but not so much that we can just blaze through them."
                    "As a result, the game turns into a slogfest where one side is playing very aggressively and the other very defensively. The match ends up going really long."
                    "Since we're talking about a videogame where stamina and mental state aren't a thing that exists, there is never a point where one side just can't keep up anymore."
                    "It takes us almost a full hour just to get through the first set."
                    "The end result is, predictably, a total victory for Keisuke and I."
                    "Alex didn't play badly despite not having any experience with tennis, but the lack of organization between him and Saya meant they lost many easy points or attempted to go on the offensive and left areas of the court open."
                    "We get by with a 6-3 score. Overall, not a bad result for the two of us."
                    show k 1 c at fdis
                    k "\"It was so easy that I almost feel bored by the result.\""
                    show sa 1 c annoyed at fdis
                    sa "\"Now you're just saying stuff you know will annoy me because I can't hit you.\""
                    show k 1 c calm at fdis
                    k "\"Why don't you give it a try? I've always wanted to see a flying bunny.\""
                    sa "\"You're so dead tomorrow...\""
                    show k 2 c gentle at fdis
                    k "\"Perhaps. But for today, I'm just gonna have fun at your expense.\""
                    sa "\"I hate you.\""
                    show k 1 c smile at fdis
                    k "\"No you don't.\""
                    show sa 1 c sigh at fdis
                    sa "\"... No, I don't.\""
                    al "\"Shall we try again?\""
                    mc 1 c think "\"I guess we could play one more set.\""
                    show sa 1 c pout at fdis
                    sa "\"Of course we'll play again! I'm not quitting till I win.\""
                    show k 1 c sigh2 at fdis
                    k "\"We don't have all night to play just to satisfy your ego.\""
                    show sa 1 c pout at fdis, jumping
                    sa "\"Rude!\""
                    show k 1 c at fdis
                    k "\"Not rude. Honest.\""
                    show k 1 c calm at fdis
                    k "\"But I suppose there's no harm in playing one more set.\""
                    "Ah, the famous last words."
                    "\"Just one more won't hurt\". Then they go on to do it over and over again."
                "Saya":
                    mc 1 c smile "\"Saya is probably the most sensible choice to make.\""
                    show k 1 c smile at fdis
                    k "\"I agree.\""
                    show sa 1 c pout2 at fdis
                    sa "\"Awww, but I wanted to pair up with Alex!\""
                    mc 1 c sigh "\"Gee, sorry I wanted to partner up with my friends.\""
                    show sa 1 c think at fdis
                    sa "\"You're forgiven, I guess. Still, I wanted to pick Alex!\""
                    mc 1 c sigh2 "\"{size=-2}Great, not five seconds and I'm already regretting my choice.{/size}\""
                    show k 1 c considerate at fdis
                    show sa 1 c at fdis
                    k "\"It's for the best. This way we make sure that both pairs have good synergy. You and Mizoguchi-san know each other far longer than anyone else here. Meanwhile, I'm the only one that knows Alex.\""
                    show k 1 c smile at fdis
                    k "\"I hope these results are to your liking, Alex.\""
                    "The wolf's lips quirk up in a half-smile, the tip of his left canine showing."
                    al "\"Of course it is. I can't complain about having you as my duo.\""
                    show k 1 c calm at fdis
                    k "\"Great. Let's show these two how well we can work together.\""
                    al "\"Yes.\""
                    "He might not talk much but I can definitely sense the excitement burning up in Alexander's huge frame."
                    "This competition might be a bit more heated than I first thought it'd be."
                    scene KeiRoom with fade
                    "It took a lot of digging around before we'd each found games that we wanted to play."
                    "Alexander refrained from joining the discussion on what we should play, but he still picked up a game from the pile."
                    "I guess he's just not very vocal about his preference?"
                    "Either way, since we couldn't settle on which one we'd choose with everyone having a different opinion, we decided to leave it to chance again."
                    "The four of us played Rock Paper Scissors until the winner was decided."
                    show sa 1 c at fdis, five with dissolve
                    "In this case, it was Saya."
                    show sa 1 c at fdis, two with move
                    show k 1 c at fdis, five
                    show al 1 u at eight behind k
                    with dissolve
                    k "\"Alright, the game's loading. Everything should be set-up just fine.\""
                    mc 1 c sigh "\"I still think it's kinda ridiculous for the person who wants to call herself a proper lady to choose a game called \"Bloodrage Fighters\".\""
                    show sa 1 c pout2 at fdis
                    sa "\"Just because I like fighting games doesn't make me less girly!\""
                    "Since when have you been girly?"
                    "At least that's the question that comes to mind, but I have enough sense not to say it out loud this time."
                    show k 1 c sigh2 at fdis
                    show sa 1 c at fdis
                    k "\"I don't know why you're complaining. Fighting games are some of your best genres, [povFirstName]-san.\""
                    mc 1 c worried "\"Old school fighting games, sure. These newer, tag-team based games I've never really touched.\""
                    show k 1 c smile at fdis
                    k "\"I guess this might just be a learning experience for us both.\""
                    mc 1 c "\"What do you mean \"for us both\"? The game's yours. You must have played it already.\""
                    show k 1 c sigh2 at fdis
                    k "\"I have a lot of games. Do you really think I've played them all? This one is still in my to-play list.\""
                    al "\"Keisuke has barely played any of the games in his collection. He just buys them to serve as an adornment.\""
                    show k 1 c worried at fdis
                    k "\"T-they didn't need to know that!\""
                    al "\"Does anyone ever {i}need{/i} to know anything.\""
                    show k 1 c sigh2 at fdis
                    k "\"Don't try to be a philosopher.\""
                    al "\"I hardly think such an innocuous question would qualify as \"philosophy\" but as you wish.\""
                    show sa 1 c complain at fdis
                    sa "\"Are you girls done talking or do you need me to give you some time to go do your makeup too?\""
                    mc 1 c sigh "\"You don't have to get so intense over a little gaming competition you k-\""
                    show sa 1 c annoyed at fdis
                    sa "\"I'm not intense. You'll know when I'm getting intense!\""
                    "And here I thought the fact her voice was at least two octaves higher than usual was already a telltale sign. Guess I was wrong."
                    show k 1 c sigh at fdis
                    show sa 1 c at fdis
                    k "\"{size=-2}Every time...{/size} Yeah yeah, we're ready. Let's pick our fighters.\""
                    show k 1 c at fdis
                    "Since neither of us have ever played the game before, we just each pick a random fighter that we think looks cool."
                    "Saya picks a guy in a giant suit of armor that carries a sword almost as tall as he is."
                    "My guess is that he's probably the type to deliver slow but powerful blows... guess I won't know until we try."
                    "Since her character looks fairly slow and I want to make sure we're at least a little bit balanced, I go with a female character in a skimpy outfit (because of course she'll be wearing one) who looks like she'd be fast."
                    "Alex and Keisuke also pick two fairly generic looking characters who don't really seem to stand out much at all."
                    show sa 1 c laugh at fdis
                    sa "\"Alright, [povFirstName]-kun, you'll be going first. Make sure to tag out if you feel like you're in trouble.\""
                    show sa 1 c at fdis
                    mc 1 c excited "\"Leave it to me!\""
                    show k 1 c serious at fdis
                    k "\"I'll be going first on our side. I accept nothing but absolute victory.\""
                    al "\"If you say so. I don't really mind if we lose.\""
                    show k 1 c sigh at fdis
                    k "\"Come on, Alex. I'm trying to be serious here and you're ruining my Feng Shui.\""
                    al "\"You don't even know what that is, do you?\""
                    show k 1 c smile at fdis
                    k "\"Nope. I haven't the faintest clue.\""
                    al "\"I figured.\""
                    "I make sure to try to memorize the basic commands that show during the loading screen."
                    "I just glance over the tag command since I don't really intend on using it."
                    "Sorry, Saya-chan. Fighting games are kind of my thing. I refuse to let something silly like never playing this one before stop me from steamrolling everyone!"
                    show k 1 c serious at fdis
                    "As soon as the match starts, Keisuke's character gets right on top of me."
                    "He doesn't seem to be doing much more than basic button mashing, but his character seems to be a speedy type that can unleash his attacks very fast."
                    "They don't do much damage when I'm guarding but they seem to fill the Guard Break meter very fast."
                    "I do a sliding tackle to knock him down and start consistently testing different button combinations to try to figure out my character's combos."
                    mc 1 c curious "\"Ooh, I think I just discovered one of her specials. What was the combination again? A-B-A-B-B-B-A-A?\""
                    show k 1 c worried at fdis
                    k "\"Wha- how are you doing all that?\""
                    mc 1 c laugh "\"I'm just trying out different button combinations and memorizing what they do. It's better than casual button mashing.\""
                    show k 1 c scorn at fdis
                    k "\"Oh yeah? I'll show y-\""
                    show k 1 c shock at fdis
                    $ renpy.pause(1.0)
                    show k 1 c uncomfortable at fdis
                    k "\"Did... did you just take out half of my health bar in one blow?\""
                    mc 1 c laugh "\"I guess I just found out her second special.\""
                    show k 1 c avoid at fdis
                    k "\"C-crap... Alex, I think I might need to tag out.\""
                    al "\"Alright. I'll try to handle things in your stead.\""
                    show k 1 c sigh at fdis
                    k "\"Ugh, this is so humiliating...\""
                    mc 1 c happy "\"Hey, you said it yourself. I'm the authority on fighting games here.\""
                    show k 1 c sigh2 at fdis
                    k "\"I hope Alex wipes that smug grin off your face.\""
                    mc 1 c happy "\"Pfft, as if-\""
                    "Just then, Alex somehow unleashes a special out of nowhere. His characters begins spinning her spear and hitting me with an ultrafast, multihit combo."
                    "Each individual hit doesn't do much damage but at the same time, they don't seem to be filling my character's KO meter at all and he just stands still taking them."
                    mc 1 c shock "\"W-why aren't I falling to the floor? I should fall to the floor after six or seven consecutive hits!\""
                    al "\"Beats me. She just keeps spinning her spear as long as I keep holding down this button.\""
                    show sa 1 c shock at fdis
                    "I watch as his special bar slowly drains down, taking my health bar with it."
                    "Because of the beating I was giving Keisuke, their team special bar was at full charge and it takes a while for it to fully drain."
                    "By the time it hits 0, Alex's character has landed 89 hits on me with no chance for a parry or a dodge, taking over seventy percent of my health bar with him."
                    mc 1 c shock "\"N-no way. My health bar!\""
                    sa "\"[povFirstName]-kun, tag out. Tag out!\""
                    mc 1 c wince "\"Hang on, I can do this!\""
                    "I try to mount a desperate defense, but miss a few key inputs here and there and fail my combos."
                    "Alex throws my character to the air and begins hitting me as I fall, tossing me up again and resetting the combo animation."
                    "Did he just casually walk into an infinite combo input by pure chance?!"
                    "I watch my bar hit 0 as I'm juggled like a ragdoll without being able to make a single input."
                    mc 1 c shock "\"You're kidding me...\""
                    show sa 1 c annoyed at fdis
                    sa "\"Jeez, I told you to tag out. You useless ball of fur!\""
                    mc 1 c wince "\"H-hey, mean...\""
                    show k 1 c haughty at fdis
                    k "\"Jeez, Alex just got a Perfect on you. I know I asked him to wipe that smug look off your face but I didn't think he'd do it so well.\""
                    mc 1 c nervous "\"Shut up!\""
                    show sa 1 c at fdis
                    "I'm relegated to a spectator seat, watching Alex and Saya fight it out."
                    "Somehow, she seems to have stumbled into her character's Perfect Dodge combo as she's dodging most of the attacks Alex used to beat me."
                    mc 1 c shock "\"Wait, what?! How are you this good?\""
                    show k 1 c smile at fdis
                    k "\"I have to admit, you two are much better at this game than I thought you'd be. And here I thought the biggest problem would be [povFirstName]-san.\""
                    mc 1 c sigh2 "\"Stop gloating already. No one likes a sore winner.\""
                    show k 1 c haughty at fdis
                    k "\"Said the sore loser.\""
                    mc 1 c sigh "\"Just shut up and watch.\""
                    show k 1 c worried at fdis
                    show sa 1 c annoyed at fdis
                    sa "\"Will the two hens stop clucking over there? We're trying to concentrate here!\"" with hpunch
                    k "\"S-sorry.\""
                    mc 1 c worried "\"My bad...\""
                    show sa 1 c at fdis
                    "Jeez, I know she's competitive but this is kinda ridiculous..."
                    "It seems that Saya and Alex are evenly matched despite the odds."
                    "I don't know how but the two of them seem to have figured out most of their character combos even faster than I did."
                    "I know I don't tend to play newer fighting games and they tend to be more streamlined for ease of use but my pride is a little hurt right now."
                    show k 1 c shock at fdis
                    k "\"W-wait, Alex!\""
                    "In a split second, I see Alexander try a grapple that is immediately reversed, followed by a max special from Saya that drops him down to 0 HP."
                    al "\"Rats...\""
                    "He mumbles those words with the most neutral looking face I've ever seen for someone that just lost a close match."
                    "Keisuke holds his controller as his character jumps back into the fighting pit."
                    "Despite his attempts to hold her back, it takes Saya less than ten seconds to engage in a long-winded combo that ends up throwing him out of the ring."
                    show sa 1 c laugh at fdis
                    show k 1 c shock at fdis, shake1
                    k "\"N-no!\""
                    mc 1 c shock "\"Holy shit. Saya-chan, you just kicked both their asses!\""
                    sa "\"Damn right I did!\""
                    show k 1 c sigh2 at fdis
                    k "\"I can't believe it. I really thought Alex would carry us to victory...\""
                    al "\"Sorry.\""
                    show k 1 c avoid at fdis
                    k "\"It's alright. I was useless to us anyway.\""
                    al "\"That you were.\""
                    show k 1 c sigh at fdis
                    k "\"{size=-2}No hesitation, huh...{/size}\""
                    sa "\"Are you guys ready to have your butts kicked again?!\""
                    show k 1 c serious at fdis
                    k "\"Hell no. We're winning this time.\""
                    al "\"Is this going to be one of those scenarios where we have to keep playing until we win?\""
                    show k 1 c scorn at fdis
                    k "\"You bet.\""
                    "Alex sighs, rubbing the bridge of his nose."
                    al "\"This is going to take a while...\""
        "Tails":
            mc 1 c curious "\"Tails.\""
            show k 1 c at fdis
            k "\"Alright, I'll flip it now.\""
            play sound "music/cointoss.ogg"
            "..."
            k "\"It's heads. Mizoguchi-san gets to pick.\""
            mc 1 c wince "\"Damn...\""
            show sa 1 c laugh at fdis
            sa "\"Oh, yay! I pick Alexander!\""
            show k 1 c worried at fdis
            k "\"Wha... you're not even going to think about it?\""
            sa "\"Nah. I wanna partner up with him. He looks very climbable!\""
            "Keisuke and I both look from Saya to Alexander, marveling at the wolf's expression."
            "Despite how unflappable he seemed so far, even he's unable to keep his face from showing incredulity and confusion at the bunny's words."
            "Saya cheerfuly hops to his side, looking him up from top to bottom before huffing with contentment."
            sa "\"Yup, you're definitely good enough!\""
            "She flashes him a thumbs up, to which he responds with a single raised eyebrow."
            "He looks at the two of us as if to ask \"what's wrong with her?\". We are unable of doing anything but shrugging, feeling as confused as he is."
            show k 1 c at fdis
            k "\"Saya-chan, are you feeling okay today?\""
            show sa 1 c smile at fdis
            sa "\"Yeah I am. Why?\""
            show k 1 c worried at fdis
            k "\"Well, I mean... you've always been a little weird at times but this really kinda takes the cake.\""
            show sa 1 c talk at fdis
            sa "\"Since when am I weird?\""
            show k 1 c at fdis
            mc 1 c confused "\"What do you mean \"since when\"? You've been weird since I first met you. You think I don't remember the way you acted on that bus way back then?\""
            show sa 1 c think at fdis
            sa "\"Shhhh. That is neither here nor there.\""
            mc 1 c sigh2 "\"Yes, ma'am...\""
            "Why can't I have normal friends?"
            show sa 1 c at fdis
            show k 2 c annoyed at fdis
            k "\"I guess this means the pairings have been decided... In a very weird fashion, but that doesn't matter in the end.\""
            show k 1 c at fdis
            k "\"Alex, are you okay with having Saya as your partner?\""
            "The wolf shrugs, his face back to his usual cool, detached demeanor."
            al "\"Makes no difference to me.\""
            show k 1 c smile at fdis
            k "\"Okay. I guess this means we can finally decide on the games to be played.\""
            mc 1 c smile "\"This is probably going to take a while though.\""
            show k 1 c sigh at fdis
            k "\"Yeah, you're right about that... at times like this, I feel like such a large collection is more restricting than it is liberating.\""
            show sa 1 c laugh at fdis
            sa "\"Who cares, let's just pick something that looks fun!\""
            show k 1 c at fdis
            mc 1 c considerate "\"We have no way to know if it's fun just judging by the boxart. Have a little patience.\""
            show sa 1 c pout2 at fdis
            sa "\"Booo. Boring.\""
            mc 1 c confused "\"Why are you acting so weird all of a sudden?\""
            show sa 1 c at fdis
            sa "\"I'm not acting weird. You just forgot how I usually am cause I've been such a minor character this whole time.\""
            mc 1 c sigh "\"Minor character? Are you {i}trying{/i} to not make sense?\""
            show sa 1 c laugh at fdis
            "She laughs, showing me her tongue with a cheeky smile on her face."
            sa "\"A little bit of this, a little bit of that. Whatever it takes to get some love around these parts.\""
            mc 1 c avoid "\"{size=-4}I'm surrounded by idiots...{/size}\""
            jump KeiPair
    stop music2 fadeout 2.5
    play music3 "music/BGM/Dog Days.ogg" fadein 5.0
    scene KeiRoom
    show sa 1 c at fdis, two
    show al 1 u at eight
    show k 2 c gentle at fdis, five
    with fade
    "The hours seem to pass us by leisurely as we continue to play games and joke around."
    "It's surprising to see Kei-kun playing and laughing like this."
    "It's so rare for him to lower his guard in front of other people... or at least I myself don't see it often."
    "Maybe Alex is more used to these kinds of things... these two have known each other for quite a few years already."
    "When I think about it, I feel weirdly jealous of that..."
    "Despite how stuck up he can be at times, Kei-kun jokes around so freely with Alex. I wish he could act that way around me more often too..."
    show k 1 c smile at fdis
    k "\"[povFirstName]-san, you're spacing out again.\""
    mc 1 c shock "\"H-huh? Sorry, what were you saying?\""
    k "\"It was nothing super important. We were just trying to decide on what to have for dinner.\""
    show k 1 c at fdis
    k "\"I don't know if you noticed but it's already starting to get dark.\""
    mc 1 c talk "\"Wait, really?\""
    "I look out the window and sure enough, the sky has started to darken."
    mc 1 c curious "\"Huh... I didn't notice it at all.\""
    show k 1 c smile at fdis
    show sa 1 c think at fdis
    sa "\"Of course you didn't notice, you were spacing out as always.\""
    mc 1 c annoyed "\"As always? I take offense to that.\""
    show sa 1 c at fdis
    k "\"Mizoguchi-san is right, you space out all the time. Almost as much as Kobayashi.\""
    mc 1 c sigh2 "\"Of course you two would gang up on me.\""
    show k 1 c sigh2 at fdis
    k "\"Telling things how I see them is very different from ganging up...\""
    show k 1 c smile at fdis
    k "\"Either way, what were you thinking so hard about?\""
    mc 1 c shockb "\"O-oh, it was nothing much. I was just thinking of random stuff.\""
    show k 1 c at fdis
    k "\"Huh. That's less interesting than I thought.\""
    show k 1 c smile at fdis
    k "\"Well, not that it matters anyway. Do you have any idea what you want to have for dinner? I'll ask Kuroda-san to fetch us whatever you guys want.\""
    show sa 1 c laugh at fdis
    sa "\"I want sushi!\""
    show sa 1 c smile at fdis
    mc 1 c curious "\"Oh, uhm... I'll go for whatever you guys want. There's no real point in trying to pander to me anyway since I eat most things.\""
    show k 1 c calm at fdis
    k "\"Most things, huh? Except for anything that has tea, pepper or milk.\""
    mc 1 c talk "\"Wow, I'm surprised you know that.\""
    show k 1 c wry at fdis
    show sa 1 c happy at fdis
    k "\"I've learned my lesson. I'm making an effort to get to know my friends better. {size=-2}I also might have asked Mizoguchi-san a bunch of stuff about you.{/size}\""
    show sa 1 c at fdis
    mc 1 c smile "\"Heh. So you were serious about that stuff you said on being a more attentive friend and whatnot?\""
    show k 1 c annoyed at fdis
    k "\"Of course I was. I'm a man of my word. Besides, it's embarassing to not be able to treat the people who always take such good care of me with the same degree of care.\""
    mc 1 c considerate "\"I think you're exaggerating things just a tad.\""
    show sa 1 c laugh at fdis
    al "\"Yes. Besides, you're hardly a man yet. You're just seventeen.\""
    show k 1 c avoidb at fdis
    k "\"Wha- I don't have to be twenty to be a man. I'm already plenty responsible enough.\""
    al "\"Not according to the law you're not.\""
    show k 1 c annoyed at fdis
    show sa 1 c smile at fdis
    k "\"Sheesh, do you always have to burst my bubble?\""
    al "\"Yes. It's one of my favorite hobbies.\""
    "The wolf shows a hint of a smile as he says those words."
    "Even if he seems stern all the time, the way he talks to and treats Keisuke is almost... brotherly."
    show k 1 c sigh2 at fdis
    k "\"You're terrible.\""
    al "\"Thank you, I aim to be.\""
    show k 1 c at fdis
    k "\"Either way, should I order us sushi then?\""
    mc 1 c smile "\"Yeah, I'm fine with that. Sushi is pretty good.\""
    show sa 1 c happy at fdis, shake2
    sa "\"Yay, sushi!\""
    show k 2 c gentle at fdis
    k "\"You don't need to get so excited over something so simple.\""
    show sa 1 c laugh at fdis
    sa "\"But sushi is amazing!\""
    show k 1 c smile at fdis
    k "\"If you say so, I won't disagree. Let me just go c-\""
    show k 1 c shock at fdis
    show sa 1 c at fdis
    stop music3
    play sound "music/slidingdoor.ogg"
    "The door to Keisuke's room is suddenly opened without warning."
    show al 1 u at offscreenleft
    show sa 1 c at fdis, offscreenleft
    show k 1 c shock at three
    with move
    show kur 1 u smile at eight
    show chi 1 c at five
    with moveiridis
    kur "\"My apologies for the intrusion, Young Master.\""
    "Kuroda, one of Keisuke's butlers, walks into the room with another white hare that I don't recognize."
    "It's an older woman wearing some very expensive looking clothes. The scowl on her face is terrifying enough that I can imagine children crying just upon glancing at her."
    show k 1 c serious at fdis
    "As soon as she walks in through the door, Keisuke's entire body stiffens up."
    "Even Alex seems to respond in a similar way, although there is no change to his facial expression."
    "As I'm left wondering who this person might be, she looks over the room, her eyes pausing on Saya and I for just a second before moving on, an incredible measure of disgust on her face."
    chi2 "\"I see that the servants were not joking when they told me that you had... guests. It seems you didn't even seem to think of seeking permission before inviting these... people over to my house.\""
    "It almost felt like she was biting her tongue to avoid calling us something else."
    "Just the way she looked at me was already unfriendly enough that I dared not speak a word."
    k "\"These are my friends, grandmother. I hardly think I need permission to invite them to {i}my{/i} house.\""
    chi2 "\"{i}Your{/i} house? How odd. I don't remember seeing your name on the scripture for this estate.\""
    k "\"Last time I checked, it wasn't your name on it either. It was my {i}father's{/i} name. So I don't think I need to be asking {i}you{/i} for permission.\""
    "The woman narrows her eyes, pursing her lips so much that they start to look like a single thin line."
    "She glances at the TV, in which the last game we played is still being displayed for all to see."
    chi2 "\"And what about this? Wasting your time on games? Don't you have better, more productive things to do if you have so much free time?\""
    show k 1 c scorn at fdis
    k "\"So long as I produce acceptable results then the way I spend my time is my own business, grandmother. You'd do well to remember that.\""
    "The woman huffs, her eyes moving towards the wolf that stands behind us."
    chi2 "\"Drake.\""
    show kur 1 u smile at ten
    show chi 1 c at eight
    show k 1 c serious at fdis, five
    with move
    show al 1 u at one with moveiledis
    al "\"Yes, Master?\""
    "The way Alexander spoke his words was almost robotic, completely devoid of any emotion."
    "I had thought before that he didn't seem to put much emotion into his words before, but just now the difference was so obvious that even I could notice it."
    chi2 "\"I hardly think you're entitled to skip on your work to play games.\""
    al "\"My apologies, Master.\""
    chi2 "\"If you understand then get back to work. I'll see that your next paycheck reflects your poor attitude.\""
    al "\"Yes, Ma-\""
    show k 1 c angry at fdis, five with move
    k "\"Hang on just a second. Alex is {i}my{/i} personal butler. His job is to do what {i}I{/i} tell him to do. If I tell him to play games with me then he {i}is{/i} doing his job!\""
    "She huffs upon hearing his words, opening her mouth to speak again."
    show al 1 u at four with move
    play sound "music/tap.ogg"
    al "\"You don't have to cover for me. I failed to perform my duties in an acceptable manner. I'll take responsibility for it.\""
    show k 1 c shock at fdis
    k "\"Wha- but Alex...\""
    chi2 "\"Good. It seems that at least the {i}servant{/i} still knows his place here. Come with me then, we need to better discuss your punishment.\""
    al "\"Yes, Master.\""
    show al 1 u at offscreenright
    show chi 1 c at offscreenright
    with moveoridis
    show k 1 c scorn at fdis, five
    show sa 1 c bored at fdis, three
    show kur 1 u smile at eight
    with move
    "With one last look at us, the woman huffs once more, walking out of the room without another glance back."
    "Alex follows behind her, her eyes looking much more stern and menacing than normal."
    k "\"That... that b-\""
    kur "\"Young Master, please contain yourself. It would not do to insult your grandmother.\""
    show k 1 c avoid at fdis
    k "\"Yeah. Right...\""
    sa "\"What... what just happened?\""
    mc 1 c worried "\"Kei-kun... {i}that{/i} was your grandmother?\""
    show k 1 c sigh2 at fdis
    k "\"Yeah... she's a nightmare isn't she? I have no idea what she's even doing here. She was supposed to be out of the estate for the entire day.\""
    kur "\"I'm sorry, Young Master, it's my fault...\""
    "The fox looks away, his tail going between his legs as his shoulders slump."
    show k 1 c serious at fdis
    k "\"Your fault? What are you talking about?\""
    kur "\"In my... excitement to see you finally bringing friends over, I let it slip to one of the other servants that you had company. It seems that the information was passed along to one of your grandmother's spies.\""
    show k 1 c sigh at fdis
    k "\"And she went out of her way to come back here just to torment me? Ugh... I hate the fact that that makes sense.\""
    sa "\"You're... you're kidding, right? Spies? She has spies here?\""
    kur "\"Well, this {i}is{/i} also her house. Even if we are all servants hired by the Urushihara Corporation, not all of us have our... allegiances to the same members of the family.\""
    show k 1 c avoid at fdis
    k "\"The company is divided in factions that support different members of the family. My father's faction is nothing but puppets to my grandmother. She's the one that controls everything.\""
    kur "\"On the other hand, there are those of us who are loyal to the Young Master and wish to see him take control of the company... but he is unwilling to do so.\""
    show k 1 c sigh at fdis
    k "\"Kuroda, even if I wanted to do that, you know as well as I do that there's no way I could really do that. The company wouldn't be passed on to me until they were sure they have a way of controlling me.\""
    kur "\"Yes... that is also regrettably true.\""
    mc 1 c wince "\"I... I didn't know you had so many issues in your daily life.\""
    show k 1 c worried at fdis
    k "\"I try to keep my family drama away from my friends. No need to involve you guys in issues you have no way of helping me with.\""
    show k 1 c avoidb at fdis
    k "\"I'm... sorry you guys had to see this.\""
    show sa 1 c argue at fdis
    sa "\"You don't have to apologize. She's the one who did it. Seriously, what's her problem?!\""
    show k 1 c sigh2 at fdis
    show sa 1 c bored at fdis
    k "\"Grandmother hates me. She enjoys taking every opportunity she has to flaunt her power over me and make me miserable. She was probably beside herself with the prospect of humiliating me in front of friends.\""
    sa "\"That's horrible! Why would she go out of her way to make you feel unwelcome at your own home?\""
    k "\"Because this isn't my home. Not really. I'm just a bastard to her. You think she {i}wants{/i} to have me around? The only thing keeping me here is the fact that my father doesn't have other children. I'm pretty sure I said this before.\""
    show sa 1 c at fdis
    mc 1 c worried "\"To be honest, I didn't think you were serious about it...\""
    show k 1 c avoid at fdis
    k "\"Why would I make shit like this up? That'd be ridiculous.\""
    mc 1 c worried "\"Yeah, I'm sorry...\""
    show k 1 c worried at fdis
    k "\"Kuroda, please don't take this as me blaming you but why didn't you warn me she was coming?\""
    kur "\"I wanted to, but she made sure to order me to accompany her here just so I wouldn't have the opportunity to do so.\""
    show k 1 c sigh at fdis
    k "\"Ugh, she's sneakier than I thought...\""
    play sound "music/knock.ogg"
    $ renpy.pause(1.0)
    play sound "music/slidingdoor.ogg"
    show k 1 c at fdis, four
    show sa 1 c at fdis, one
    show kur 1 u smile at seven
    with move
    show sag 1 cu smile at ten with moveiridis
    sag2 "\"I'm coming in.\""
    show k 1 c serious at fdis
    k "\"Oh, father. To what do I owe the {i}pleasure{/i} of your visit?\""
    sag2 "\"Come on, there's no need for that sort of tone. I ran into your grandmother as I was getting home and was informed you had guests. From the look Alexander gave me, I imagined she came here.\""
    show k 1 c scorn at fdis
    k "\"So you also decided to come make your presence known to my friends? I'm touched.\""
    "The older hare's smile falters for a second. He awkwardly scratches the back of his neck, looking at the butler standing next to him."
    sag2 "\"Kuroda, could you go have dinner prepared for us? Make sure there is enough for our guests.\""
    kur "\"Very well, sir. Will your mother also be joining you for dinner?\""
    sag2 "\"No. I came up with an excuse to give her so she'd go back to her friend's place. I figured that'd give everyone some quiet time.\""
    show k 1 c serious at fdis
    k "\"How very kind. What are the strings attached to your favor this time?\""
    mc 1 c worried "\"Kei-kun, I-I don't think you need to talk to him like that. He seems to be trying to help.\""
    show k 1 c avoid at fdis
    k "\"Pfft, sure. His \"help\" always has strings attached to it.\""
    "His father looks away for a second, his gaze casting itself down to the floor."
    sag2 "\"That's... if we could just speak over dinner...\""
    show k 1 c serious at fdis
    k "\"There's no need. If you have something you want to ask of me then just do so already. I'll be having dinner with my friends in my own room, thank you very much. Kuroda, could you have some sushi prepared and sent here, please?\""
    "The fox looks between the two, hesitating for a second before speaking out."
    kur "\"As you wish, Young Master.\""
    show kur 1 u smile at offscreenright with move
    show sa 1 c bored at fdis, two
    show k 1 c serious at fdis, five
    show sag 1 cu smile at nine
    with move
    "Kuroda-san walks out of the room, giving us one last uncertain look before closing the door behind him."
    sag2 "\"That... that was unnecessary, Keisuke...\""
    show sa 1 c at four with move
    play sound "music/tap.ogg"
    sa "\"{size=-2}Kei-kun, I don't think you have to be so harsh on your dad. He doesn't look like he means anything bad.{/size}\""
    "Saya leans onto Keisuke's shoulder, whispering those words onto his ear."
    show sa 1 c bored at fdis, two with move
    "I see the older hare's ears twitch as he tries to listen to what she's saying, curiosity flashing in his eyes."
    mc 1 c wince "\"{size=-2}Yeah, can't you go a bit easy on him?{/size}\""
    "No matter how I look at him, I just see a man standing awkwardly in front of his son. I can't think badly of him like I do with Keisuke's grandmother."
    show k 1 c annoyed at fdis
    k "\"{size=-2}Please don't take offense to this but... you two are just outsiders looking in. You have no idea how he's like. He never comes to see me unless he has something to ask. And when I say ask, I mean {i}order{/i}.{/size}\""
    sag "\"Keisuke, I really don't think your friends need to see... this. Can't we please step outside for a second to talk?\""
    show k 1 c avoid at fdis
    "Keisuke looks at the two of us for a second, the anger in his eyes dissipating just a bit. He's probably arguing with himself about whether or not to act this way in front of us.\""
    k "\"Fine...\""
    show sag 1 cu smile at offscreenright
    show k 1 c avoid at offscreenright
    show sa 1 c bored at fdis, five
    with move
    "The two walk out of the room without saying another word, leaving Saya and I alone."
    sa "\"That... was surreal.\""
    mc 1 c avoid "\"I know. I feel like I shouldn't be here right now.\""
    show sa 1 c sigh at fdis
    sa "\"Yeah, I got that feeling too, although I'm sure Kei-kun would say we're crazy if we told him that...\""
    mc 1 c considerate "\"Unfortunately, I'm pretty sure you're right.\""
    show sa 1 c bored at fdis
    "Saya looks away, biting her lip. She sits herself down on Keisuke's bed, awkwardly kicking at the floor."
    sa "\"What do you think they're talking about out there?\""
    mc 1 c worried "\"I have no idea... I'm honestly surprised at this whole thing. I knew his family life was... \"tense\", but I never imagined it was this much.\""
    sa "\"Yeah. Usually when people talk about family issues they tend to exaggerate them a little because of anger or stuff like that... in his case, it seems like he was downplaying it instead.\""
    mc 1 c worried "\"Do you think we should say something to him?\""
    show sa 1 c at fdis
    sa "\"What is there to say? \"Hey, I'm sorry your grandma's a bitch. By the way, I think you're too harsh on your dad\"?\""
    mc 1 c considerate "\"Maybe we just don't word it like that...\""
    show sa 1 c bored at fdis
    sa "\"... You do agree with me, right?\""
    mc 1 c "\"On what?\""
    "Saya's ears flop down next to her face as she fidgets uncomfortably on her seat, clearing her throat multiple times before she speaks."
    sa "\"That... that he was kinda out of line? With the way he talked to his dad, I mean, not with his grandmother. Honestly, fuck that woman. She's an old hag.\""
    mc 1 c avoid "\"Yeah, I agree. It really looked to me like his dad was feeling pretty bad about the whole thing.\""
    "Saya nods, her eyes glued to her feet as she moves them forward and back on the air."
    sa "\"You think we should say something?\""
    mc 1 c sigh2 "\"Didn't we already do that? He wasn't exactly thrilled to hear it either.\""
    show sa 1 c argue at fdis
    sa "\"Yeah but... I don't know. It might sound stupid for me to say this since I never really had many issues growing up, but I really think that family should stick together. If his dad is offering him an olive branch, I really think he should take it...\""
    mc 1 c worried "\"His family problems have nothing to do with us though. We have no business saying anything.\""
    show sa 1 c sigh at fdis
    sa "\"No offense but you're a real pushover when it comes to this kind of thing.\""
    mc 1 c shock "\"Hey!\""
    show sa 1 c annoyed at fdis
    sa "\"It's true! \"Not our problem\"? \"None of our business\"? Kei-kun's our friend. If we see him doing something we think is wrong, isn't it our duty to say something? Especially if we think it might help him?\""
    mc 1 c avoid "\"It sounds a lot simpler when you put it in such terms but the reality is that he doesn't sound like he {i}wants{/i} us to say something. He doesn't even want us to know about it.\""
    show sa 1 c pout at fdis
    "Saya jumped off of the bed, landing on her two feet. She looks at me with a sudden fierce look in her eyes."
    sa "\"Well, too late for that, the cat's already out of the bag. \"All it takes for evil to prevail is for good men to do nothing\". I'm gonna say something with or without you.\""
    mc 1 c sigh "\"First of all, I'm surprised you can even quote something as philosophical as that at all.\""
    show sa 1 c considerate at fdis
    "She attempts to laugh, but only manages to elicit a dry, meek chuckle."
    mc 1 c sigh2 "\"You really do have a penchant for getting yourself mixed up with other people's businesses huh... Fine, I'll back you up.\""
    "Smiling, Saya walks up to me, giving me a soft pat on the shoulder."
    show sa 1 c wry at fdis
    sa "\"Thanks. I knew I could count on you. You're a good friend.\""
    mc 1 c worried "\"Yeah, well, I just hope being a good friend to you doesn't end up costing us another good friend.\""
    show sa 1 c talk at fdis
    sa "\"I don't think Kei-kun would break his friendship with us because we spoke up.\""
    mc 1 c sigh2 "\"Until today we also didn't know how bad his relationship was with his family or about their company being torn up. How much are you willing to bet on what we \"think\" of him?\""
    show sa 1 c think at fdis
    sa "\"That's... a fair point.\""
    play sound "music/slidingdoor.ogg"
    show sa 1 c shock at fdis, three, jumping
    show k 1 c sigh at seven
    with move
    "We both jump up in surprise at the sound of the door opening again, scrambling to try and pretend that we weren't talking to each other like two kids who were caught doing something bad until we realized we had no reason to do so in the first place."
    show sa 1 c at fdis
    mc 1 c worried "\"Are you alright?\""
    k "\"I think so... dealing with my family can be so exhausting at times... my head is spinning.\""
    show sa 1 c bored at fdis
    sa "\"I'm sorry to hear that... uhm, Kei-kun, there's something that we kinda wanted to say?\""
    show k 1 c at fdis
    k "\"What is it?\""
    "Saya and I both look at each other, swallowing multiple times and trying to come up with the courage to say what we wanted to say."
    sa "\"We don't think that... that the way you treated your dad was... erm... that it was right.\""
    show k 1 c serious at fdis
    k "\"Oh? How so?\""
    mc 1 c worried "\"It's just... we get that your grandma really is a bitch with a capital B... but your dad really looked like he was trying his hardest to be nice to you. I get that you might think he doesn't like you either but-\""
    show k 1 c scorn at fdis
    show sa 1 c shock at fdis
    k "\"{size=-2}I'll stop you two right here.{/size}\""
    "His voice came out surprisingly soft... his knuckles were pressed tightly against the palms of his hand and his nose was flared up with anger... but his voice still came out incredibly soft and low, to the point of being hard to hear."
    "That by itself somehow made him sound even scarier than he would if he had been yelling at us."
    k "\"I {i}think{/i} he doesn't like me? What do you know about me {i}or{/i} him to tell me what I do or do not think?\""
    mc 1 c wince "\"Okay... uhm... I think I might have expressed myself badly there-\""
    if day5 == "keisuke":
        k "\"No, you expressed yourself perfectly fine. You two don't know what my family is like but you still think you're entitled to give me your opinion about how I deal with them. You've seen my father... what, twice? And yet you think you know him?\""
    else:
        k "\"No, you expressed yourself perfectly fine. You two don't know what my family is like but you still think you're entitled to give me your opinion about how I deal with them. You've seen my father one time and you think you know what he's like?\""
    k "\"Well, here's a newsflash for you two. You don't. I've lived with him for most of my life. He would barely ever talk to me unless it was to tell me to do something or to censor me so I think I know what I'm talking about when I tell you what he's like.\""
    sa "\"W-we didn't mean to offend you or anything. We just assumed-\""
    k "\"Yes. That's the problem. You assumed. You have no idea what things are like here because {i}I{/i} make sure never to say anything about it. Because I don't want anyone else having to get involved with my problems or having to shoulder my burdens.\""
    show k 1 c avoid at fdis
    k "\"... You don't know what it's like here, you shouldn't assume. I know what I'm talking about okay? Believe me, I know.\""
    mc 1 c worried "\"Is your dad really that bad? He seemed like he was trying to be nice.\""
    show k 1 c serious at fdis
    k "\"Pfft. \"Seemed\". My family lives on appearances. Why do you think my grandmother hates me so much? How do you think it makes her feel that her precious company is to be inherited by a bastard child? That's not an image she wants for the company, yet she has no choice.\""
    k "\"Do you want to know why he came over today? It wasn't because he wanted to see me or have dinner with me or just enjoy family time with me. He came to \"ask\" me to drop out of the Light Music Club.\""
    show k 1 c scorn at fdis
    k "\"\"How is it going to look for us if the people find out you're involved with a rock band?\" or some crap like that. Because once again, what matters here is appearances.\""
    show sa 1 c bored at fdis
    "Saya bites her lip, crossing her arms and rubbing her elbows, her eyes glued to the floor."
    sa "\"Oh... I'm sorry. I... I really thought he was trying to be nice.\""
    show k 1 c sigh2 at fdis
    k "\"That's exactly the problem isn't it?\""
    "..."
    "Oh man, it's gotten really uncomfortable in here all of a sudden..."
    mc 1 c wince "\"Uhm... how did he even find out about that? The band I mean.\""
    show k 1 c sigh at fdis
    k "\"I'm not sure. I think he might have asked the principal to keep tabs on my activities in school. I wouldn't put that past either of them.\""
    show sa 1 c shock at fdis
    sa "\"So you're going to leave the club?\""
    show sa 1 c at fdis
    show k 1 c scorn at fdis
    k "\"Hell no. Screw him. I told him if he wanted to get me out of there then he'd have to have me dragged out kicking and screaming.\""
    mc 1 c considerate "\"That's a bit dramatic.\""
    show k 1 c at fdis
    k "\"Maybe, but it still serves my point. I'm not going to stop doing something perfectly normal and that I like to do just because of someone else's selfish desires. His \"image\" isn't my problem.\""
    sa "\"You think he's going try doing something to get you out?\""
    show k 1 c avoid at fdis
    k "\"Who knows. I've never known him to be much more than a spineless jerk but I don't know how much it takes to get him to snap.\""
    "I bite my tongue to keep myself from making an unkind comment towards... everything."
    k "\"I really don't need to deal with you two criticizing me on top of everything else.\""
    mc 1 c wince "\"Sor-\""
    show sa 1 c complain at fdis
    sa "\"Please don't blame [povFirstName]-kun. Talking to you was my idea. He didn't want to say anything.\""
    mc 1 c shock "\"Wha- Saya, what are you doing?\""
    show sa 1 c pout2 at fdis
    sa "\"Telling the truth. I don't want Kei-kun to get mad at you for something that I forced you into doing.\""
    mc 1 c worried "\"You didn't force me into anything.\""
    show k 2 c gentle at fdis
    show sa 1 c shock at fdis
    play music2 "music/BGM/Mischief Maker.ogg" fadein 5.0
    k "\"Pfft...\""
    mc 1 c fsmile "\"Wait... are you laughing at us?\""
    k "\"Sorry... it's just... you two are too paranoid.\""
    show sa 1 c shock at fdis, jumping
    sa "\"Paranoid?!\""
    show k 1 c wry at fdis
    k "\"Look, it does annoy me that you guys would give me shit for stuff you don't know about, but I'm not gonna be mad at you.\""
    show k 1 c considerate at fdis
    show sa 1 c bored at fdis
    k "\"I know you two were only trying to help me. I can appreciate {i}that{/i}, even if I don't appreciate how you tried to do it.\""
    sa "\"So... wait, you're... not mad at us?\""
    show k 1 c smile at fdis
    k "\"Annoyed but not mad. You don't have to worry about it.\""
    show sa 1 c sigh at fdis
    sa "\"Huh... so I was worrying over nothing here too.\""
    show k 1 c worried at fdis
    show sa 1 c at fdis
    k "\"I guess this is partly my fault. I should have at least given you guys a basic explanation of my family dynamics before bringing you into my house. It was stupid of me to think I could do it without my grandmother or father noticing.\""
    mc 1 c wince "\"Honestly, I'm slightly uncomfortable that you invited us over without their permission.\""
    show k 1 c annoyed at fdis
    k "\"I don't need anyone's permission to invite people here. The only reason I live here is because {i}they{/i} want me to so they have an easier time keeping tabs on me. I could move out if I wanted to but it's not worth the hassle.\""
    mc 1 c "\"Couldn't your father just stop giving you money if you tried that?\""
    show k 1 c smile at fdis
    k "\"He could, but with the amount I have saved up, I could live comfortably without a job for many many years.\""
    show sa 1 c talk at fdis
    sa "\"Are you kidding me? How much do you have saved up?\""
    show k 1 c avoid at fdis
    k "\"That's a question I'm not comfortable with answering.\""
    show sa 1 c pout2 at fdis, jumping
    sa "\"Jeez, you're such a tease!\""
    show k 1 c wince at fdis
    k "\"T-tease?\""
    mc 1 c considerate "\"Don't mind her, she's just being annoying for the sake of being annoying.\""
    sa "\"Hey!\""
    play sound "music/slap.ogg"
    mc 1 c wince "\"Ow!\"" with hpunch
    show k 1 c sigh at fdis
    k "\"You really don't think before you talk, do you? That was obviously going to end up like this.\""
    show sa 1 c pout at fdis
    sa "\"Are you calling me violent?!\""
    show k 1 c at fdis
    k "\"Is the sky blue?\""
    show sa 1 c shock at fdis, shake1
    sa "\"W-what?\""
    mc 1 c sigh "\"That means yes. He's calling you violent.\""
    show sa 1 c pout at fdis
    play sound "music/slap.ogg"
    show k 1 c wince at fdis, jumping
    k "\"Ouch!\""
    show k 1 c sigh2 at fdis
    k "\"You're lucky Alex isn't here anymore, otherwise he'd have already thrown you out the window.\""
    mc 1 c considerate "\"Is it bad that I can totally imagine him doing that?\""
    show sa 1 c sigh at fdis
    sa "\"... It's a terrifying thought now that I think about it. I think I'll refrain from hitting you again while we're here...\""
    show k 1 c worried at fdis
    k "\"I wish you'd refrain from hitting me at all, but baby steps I guess.\""
    show sa 1 c at fdis
    stop music2 fadeout 2.5
    play music3 "music/BGM/Autumn Day.ogg" fadein 5.0
    show k 1 c at fdis
    mc 1 c curious "\"Hey, Kei-kun... I know you said that you'll just ignore what your dad said, but aren't you in trouble with your grandmother?\""
    show k 1 c worried at fdis
    k "\"That's the thing I was worried about. I don't really care what she has to say about me but the fact that Alex got punished for it really pisses me off...\""
    mc 1 c wince "\"What kind of punishment would she inflict on him?\""
    k "\"She'll probably have him reassigned for a few days so I won't be able to talk to him much, not to mention a payment cut this month.\""
    show sa 1 c argue at fdis
    sa "\"That's just cruel!\""
    show k 1 c sigh at fdis
    show sa 1 c bored at fdis
    k "\"Unfortunately, \"cruel\" is just child's play for her."
    show k 1 c at fdis
    extend " I'm just going to pay Alex back the difference once I find out how much she discounted from his salary.\""
    sa "\"Jeez, the fact that you can afford to just say stuff like that is scary. Sometimes I forget that you really are a pampered rich boy.\""
    show k 1 c uncomfortable at fdis
    k "\"Pampered?\""
    show sa 1 c talk at fdis
    sa "\"Who else would just go around saying stuff like \"It doesn't matter if he got punished, I'll just pay him more\"?\""
    show k 1 c worried at fdis
    show sa 1 c at fdis
    k "\"And that makes me pampered? I thought I was being responsible here...\""
    mc 1 c smile "\"Again, don't mind her. She's just trying to annoy you.\""
    show sa 1 c talk at fdis
    sa "\"But I'm not! Sure, you can pay him back for the money he lost because of you, but that doesn't make up for all the other stuff.\""
    show k 1 c at fdis
    k "\"Other stuff?\""
    show sa 1 c sigh at fdis
    sa "\"Yeah. Getting berated by your bosses, getting blamed for something that wasn't your fault, stuff like that. Giving him money won't make him feel less crappy over that.\""
    show k 1 c shock at fdis
    k "\"Ah...\""
    show k 1 c sigh at fdis
    "Kei-kun's shoulders slump as he leans forward, rubbing the bridge of his nose."
    k "\"I... never thought of that.\""
    mc 1 c "\"Are you sure Alex would even care about that? No offense but the dude didn't look like the type to be bothered by it in the slightest.\""
    sa "\"You're just assuming he can't be hurt because he looks stoic? That's just rude, [povFirstName]-kun.\""
    mc 1 c fsmile "\"R-rude? How am I rude?\""
    show k 1 c worried at fdis
    k "\"Mizoguchi-san is right. Alex might look and act very detached but he's not made of stone, he has feelings of his own too. If he didn't, he wouldn't have bothered befriending me or putting up with my crap...\""
    mc 1 c worried "\"That's... I can't really argue with that.\""
    show k 1 c sigh at fdis
    show sa 1 c at fdis
    k "\"Ugh... every time I think I've made some progress on the way I act, I'm reminded that there's still stuff that I need to fix.\""
    show sa 1 c wry at fdis
    sa "\"No one's perfect, you just have to be aware of your own flaws.\""
    mc 1 c sigh "\"Said one of the least self-aware people I know.\""
    show sa 1 c at fdis
    sa "\"Hey, I'm aware of my problems, I just choose not to do anything about them.\""
    mc 1 c shock "\"What? Then what right do you have to chastise him?\""
    show sa 1 c laugh at fdis
    "Saya shrugs, shooting me a devious smile."
    sa "\"Do as I say, not as I do.\""
    mc 1 c sigh2 "\"You're impossible...\""
    show sa 1 c happy at fdis
    sa "\"Teehee~\""
    mc 1 c sigh "\"Don't try to play it off by acting cute.\""
    show k 1 c worried at fdis
    k "\"It's fine, I don't mind it much.\""
    sa "\"See? Kei-kun agrees with me!\""
    mc 1 c sigh "\"You're far too lenient with her.\""
    show k 1 c at fdis
    show sa 1 c smile at fdis
    k "\"I seem to remember you doing a lot more stuff that I let slide than Mizoguchi-san.\""
    mc 1 c worried "\"... No comment.\""
    show k 1 c sigh at fdis
    k "\"Ugh... there's a lot of things I'll have to think over after all...\""
    show sa 1 c at fdis
    sa "\"Should we just leave so you can be alone?\""
    show k 1 c wince at fdis, jumping
    k "\"What? God no, the last thing I want right now is to be alone.\""
    show k 1 c considerate at fdis
    k "\"I think you guys underestimate how much peace of mind it gives me having you around.\""
    show sa 1 c think at fdis
    sa "\"Huh? Really?\""
    show k 1 c worried at fdis
    k "\"Yeah... I've never really felt comfortable in here. This place might be my house but it's certainly not a home.\""
    show k 1 c smile at fdis
    k "\"Having you guys here makes it a lot more tolerable though."
    show k 2 c gentleb at fdis
    extend " I dare even say that it's fun.\""
    show sa 1 c laugh at fdis
    mc 1 c happy "\"Glad to hear we can help!\""
    sa "\"Yeah! If you ever need someone to talk to, you know we're always here for you.\""
    show k 1 c wry at fdis
    k "\"Thanks. I appreciate it.\""
    show k 1 c calm at fdis
    show sa 1 c at fdis
    k "\"Mushy stuff aside, how about we look for something else we can do until Kuroda comes back with the food.\""
    mc 1 c smile "\"How about you tell us a little more about the band you joined?\""
    show k 1 c worried at fdis
    k "\"The band? Why do you want to know about that?\""
    mc 1 c talk "\"I got to meet your bandmates and all that but I don't think Saya did.\""
    show sa 1 c talk at fdis
    sa "\"Yeah, that's true. I only heard about you joining a band. I have no idea what they're like.\""
    show k 1 c at fdis
    k "\"Well, I'm pretty sure you're in the same class as some of our members.\""
    show sa 1 c shock at fdis
    sa "\"Really? Who?!\""
    k "\"Ichigo-san and Kagaho-san. They're our vocalist and bassist.\""
    show sa 1 c at fdis
    sa "\"Wait, really? Ichigo-chan in a rock band? No way!\""
    show k 1 c smile at fdis
    k "\"It was really surprising to me too. None of the girls look like the type to be in a band but even so they are. And they're all good at it too.\""
    mc 1 c smile "\"It's true. I heard them playing once and I was blown away by it.\""
    show sa 1 c pout2 at fdis
    sa "\"No fair, I wanna see them playing too!\""
    show k 1 c worried at fdis
    k "\"I'll try asking them for permission to bring you later.\""
    mc 1 c think "\"I don't think Minazuki would be against it in the slightest.\""
    show sa 1 c laugh at fdis
    sa "\"Yeah! Ichigo-chan and I are friendly with each other!\""
    show k 1 c smile at fdis
    k "\"I guess that's fair.\""
    mc 1 c curious "\"Do you guys have any idea when you're going to perform your first show?\""
    k "\"They were wanting to do it at the festival. I've been trying to help organize it.\""
    show sa 1 c at fdis
    sa "\"Organize it? You're not performing with them?\""
    show k 1 c wince at fdis
    k "\"Me? God no. There's no way I'd stand in front of a crowd to sing or play.\""
    mc 1 c "\"And yet you're totally fine with doing it to play tennis?\""
    k "\"This and that are totally different things.\""
    mc 1 c "\"I'm not so sure about that. Besides, Minazuki already wanted you to sing with her, didn't she?\""
    show k 1 c worried at fdis
    k "\"Again, there's no way I'd do that.\""
    mc 1 c pout "\"Aww, but you have such a good voice!\""
    show k 1 c annoyed at fdis
    k "\"I already said no. \""
    mc 1 c talk "\"Minazuki really wants you to sing though.\""
    show k 1 c avoid at fdis
    k "\"I don't care what she wants, there's no way I'm standing on a stage.\""
    show sa 1 c think at fdis
    sa "\"Why not? I know I never heard you singing before but what's the harm in trying?\""
    k "\"It's embarrassing.\""
    show sa 1 c at fdis
    mc 1 c smile "\"So it's not because you don't think you're good enough, you're just embarrassed.\""
    show k 1 c sigh at fdis
    k "\"{size=-2}God, why are you two being so pushy with this...{/size}"
    show k 1 c avoid at fdis
    extend " Being embarrassed is just part of the reason. I honestly don't think I'm anywhere good enough to play in a band.\""
    mc 1 c "\"Oh come on. We've all already told you you're good. Minazuki also heard you sing and she also thinks you're good. What other confirmation do you need?\""
    k "\"It's not that simple...\""
    show k 1 c sigh at fdis
    if day5 == "keisuke":
        k "\"Besides, the others might have heard me sing, but you're the only one who heard me playing the guitar, remember?\""
    else:
        if day10 == "keisuke":
            k "\"Besides, the others might have heard me sing, but you're the only one who heard me playing the guitar, remember?\""
        else:
            k "\"Besides, they don't just want me to sing, they want to play guitar too.\""
            mc 1 c smile "\"Then play guitar.\""
            show k 1 c avoid at fdis
            k "\"You can't just tell me to play the guitar, you have no idea if I'm even good at it.\""
            mc 1 c happy "\"I'm sure you are.\""
            show k 1 c sigh at fdis
            k "\"You're being way too agreeable about this.\""
    mc 1 c smile "\"Look, all I know is that I really believe you can do this stuff. I think you should give it a try.\""
    show k 1 c avoidb at fdis
    k "\"I... I don't think I could.\""
    show sa 1 c bored at fdis
    sa "\"Jeez, stop being a wuss and just try already!\""
    mc 1 c shock "\"H-hey, Saya-chan, don't say it like that.\""
    show k 1 c sigh at fdis
    show sa 1 c at fdis
    k "\"What is this? Some kind of weird \"good friend, bad friend\" routine?\""
    sa "\"Oh, so I'm a bad friend huh?\""
    show k 1 c uncomfortable at fdis
    k "\"I-I mean, wow Mizoguchi-san, your words are so comforting!\""
    show sa 1 c happy at fdis
    sa "\"That's more like it!\""
    show k 1 c worried at fdis
    "Keisuke breathes out in relief after avoiding near-certain death."
    show k 1 c wince at fdis
    show sa 1 c at fdis
    k "\"I'm just not really comfortable putting myself out there with music, you know... Maybe if I were better with the guitar I would consider {i}that{/i}, but while I can always improve with guitar or tennis, I'm stuck with the voice I have.\""
    mc 1 c smile "\"The voice you have is amazing though.\""
    show k 1 c annoyed at fdis
    k "\"You're just saying that to make me feel better.\""
    mc 1 c sigh "\"Really? You really think I'm a nice enough guy that I'd put up with something I hate just to avoid hurting your feelings?\""
    show k 1 c avoid at fdis
    k "\"You do it with Urata and his cooking remember?\""
    "Oh. Oh shit. He's right about that."
    sa "\"You're the last person I'd imagine giving someone real criticism if it could hurt their feelings [povFirstName]-kun.\""
    mc 1 c avoidb "\"What? You're kidding. I would totally do that.\""
    show sa 1 c talk at fdis
    sa "\"Nuh-uh. You're kind of a wimp.\""
    mc 1 c shock "\"What? How can you just say something like that?\""
    show sa 1 c smile at fdis
    sa "\"Because, unlike you, I just tell people the truth.\""
    show k 1 c smile at fdis
    k "\"See? If Mizoguchi-san were to tell me I'm good at something, {i}then{/i} I'd believe it.\""
    mc 1 c sigh2 "\"So what you're saying is that you just don't trust me to be brutally honest?\""
    k "\"Exactly.\""
    mc 1 c sigh "\"You both suck...\""
    k "\"Perhaps.\""
    sa "\"It's possible.\""
    show k 1 c at fdis
    show sa 1 c at fdis
    play sound "music/knock.ogg"
    kur "\"Young Master, I've arrived with your food.\""
    show k 1 c smile at fdis
    k "\"Welp, time to have dinner.\""
    show sa 1 c happyb at fdis, shake2
    sa "\"Yaay, sushi!\""
    stop music3 fadeout 2.5
    play music "music/night.ogg" fadein 5.0
    scene KeiHouseN
    show k 1 c smile at fdis, five
    with fade
    "Kei-kun sits around on the corridor, looking up at the night sky."
    "Saya has gone home about half an hour ago. Something about needing to be back early."
    "I decided to stick around for a bit longer before heading back."
    k "\"Man, it used to be that you could see all of the stars from here. Nowadays they barely ever show up. I wonder what happened.\""
    mc 1 c think "\"It's probably from the pollution.\""
    show k 1 c worried at fdis
    k "\"Hmm... I guess that sounds about right.\""
    show k 1 c at fdis
    mc 1 c smile "\"I never really took you for the type to just sit around looking at the stars.\""
    show k 1 c smile at fdis
    k "\"Well, you'd be about right in assuming that. This isn't something I do often after all."
    show k 2 c gentle at fdis
    extend " I guess the mood just struck me today.\""
    mc 1 c smile "\"If nothing else, at least you seem to be feeling better.\""
    show k 1 c smile at fdis
    k "\"Much. Having you guys around definitely made my day a lot better.\""
    show k 1 c calm at fdis
    k "\"It's... it's really nice to have friends, huh.\""
    mc 1 c smile "\"Pfft. That should be an obvious thing already, bunny boy.\""
    show k 1 c smile at fdis
    k "\"I could correct you but I'm pretty sure you already know the difference between a rabbit and a hare anyway.\""
    show k 2 c gentle at fdis
    k "\"And yeah, I know it's supposed to be an obvious thing, but still..."
    show k 1 c wry at fdis
    extend " I was always afraid of letting people in because I was scared they'd be more interested in the perks that come with befriending a guy with my social status.\""
    show k 2 c gentle at fdis
    k "\"Now I just feel like I was worried over nothing.\""
    show k 1 c smile at fdis
    mc 1 c think "\"I wouldn't say it was over nothing. I still think you should be careful with the people you choose to spend time with. Just don't close yourself to the possibilities entirely.\""
    k "\"Yeah. I guess you're right.\""
    show k 1 c calm at fdis
    k "\"Thanks for encouraging me so much, [povFirstName]-san. I'm glad I decided to listen to you.\""
    mc 1 c happy "\"Great. You've finally come to the realization that I'm awesome and am always right.\""
    show k 2 c gentle at fdis
    k "\"Hahaha, I wouldn't go that far.\""
    show k 1 c smile at fdis
    k "\"Still, you were right in this case. I should have just been more open from the beginning.\""
    show k 1 c avoid at fdis
    k "\"It might sound silly to you but I've spent the past years of my life always worrying about how people saw me, what they thought of me, whether they treated me nicely because of who I am or where I'm from.\""
    show k 1 c calm at fdis
    k "\"It feels really good to be able to just let loose and have fun with friends.\""
    mc 1 c smile "\"We could have been doing this from the start if you weren't so reserved.\""
    mc 1 c think "\"I guess we should be thanking Kenma-san for this, huh?\""
    show k 1 c at fdis
    k "\"That cocky lynx? Why would we be thanking him?\""
    mc 1 c smile "\"I mean, think about it. The only reason I found out about your family and was able to give you advice was because he pissed you off so much that I had to calm you down.\""
    show k 1 c worried at fdis
    k "\"I... I guess that's true... {size=-2}I still don't like that guy though.{/size}\""
    mc 1 c happy "\"Haha, it's fine, you don't have to like him. Besides, I doubt this was his goal anyway.\""
    show k 1 c smile at fdis
    k "\"Good to see we at least agree on that.\""
    k "\"I hope you'll keep being patient with me. I know I have a lot of things I need to work on but I want to eventually become someone you can relax around and treat like just another member of the group.\""
    mc 1 c smile "\"Don't be ridiculous. You already are.\""
    show k 2 c gentleb at fdis
    k "\"Heh... you have no idea how happy it makes me to hear that. I enjoy spending time with you quite a bit.\""
    show k 1 c smile at fdis
    k "\"You should probably be heading home soon though. It's already getting pretty late.\""
    mc 1 c talk "\"I guess you're right.\""
    k "\"I'll go call a car for you.\""
    mc 1 c smile "\"Thanks, much appreciated.\""
    show k 2 c gentle at fdis
    k "\"But before that though.\""
    play sound "music/chu.ogg"
    show Black at fdis
    $ renpy.pause(0.4)
    hide Black at fdis
    "Before I can process what just happened, I feel something pressing against my cheek for only just a second."
    mc 1 c dismayb "\"Wha-\""
    show k 2 c gentleb at fdis
    "Keisuke stands a few feet away from me, chuckling."
    mc 1 c flustered "\"D-did you just...\""
    k "\"I gave you a small peck on the cheek, yes.\""
    mc 1 c avoidb "\"Why would you do something like that?\""
    show k 1 c smile at fdis
    k "\"It's just a way of saying thank you.\""
    mc 1 c avoidb "\"You don't say thank you by kissing...\""
    show k 2 c gentle at fdis
    k "\"They do in Europe. Victor told me so.\""
    "We're not in Europe though..."
    show k 1 c smile at fdis
    k "\"You shouldn't worry about it so much. It's just an innocent peck on the cheek out of gratefulness.\""
    mc 1 c flustered "\"If you say so...\""
    k "\"I'll go get a car now. Wait for me here.\""
    scene SkyN with fade
    "..."
    "Why is my heart beating so fast all of a sudden?"
    "Did he do that just to tease me? That does sound like a Kei-kun thing to do..."
    "Ugh... great, now my head's all tied up in knots..."
    stop music
    $ date = None
    jump Day14_Keisuke
