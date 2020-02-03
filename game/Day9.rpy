label Day9:
    window hide
    scene April18 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    scene ConcertLobby with fade
    $ date = "day9"
    window show
    play music "music/crowd01.ogg" fadein 5.0
    "April 18, Tuesday."
    "Such a beautiful day."
    "The sun is bright, the sky is blue, the weather is mild, the breeze outside ruffles the leaves of the trees, covering the parks and streets in green and pink, carrying the scent of greenery in the air."
    "It is, without a doubt, a wonderful day. Nothing could possibly ruin it."
    "No one could possibly be sad or upset or preoccupied on a day like this."
    "Well... except for..."
    show j 1 c fluster at fdis, five, shake with dissolve
    j "\"Awawawawawa...\""
    "Jun..."
    mc 1 c sigh "\"Jun, seriously, sit down!\""
    "I try repeating it for the umpteenth time, hoping that this time he'll actually register what I'm saying."
    "Or that he won't disregard me at least."
    j "\"I-I-I can't sit down, I can't keep myself sat down, I just can't!\""
    "His voice is two keys higher than usual and he's stuttering so much that I can barely make out what he's saying."
    "His entire body is shivering. Is this adrenaline coursing through him or is he just quaking in fear?"
    "Honestly, I have no idea."
    mc 1 c sigh "\"Come on, why are you so nervous? Didn't you say you've performed live before? Didn't you used to take part in competitions?\""
    j "\"Y-Y-Yeah, but it's been so long since the last time.\""
    mc 1 c curious "\"... How long, exactly?\""
    j "\"A-About seven years?\""
    mc 1 c sigh "\"Are you asking me or telling me?\""
    j "\"... I-I'm not sure?\""
    "Great, he's not making sense."
    mc 1 c sigh "\"Come on, Jun, you have experience with this. You should have learned to believe in yourself by now.\""
    j "\"H-H-Having experience doesn't mean I can't screw up. A single mistake could stop me from getting to the next stage!\""
    mc 1 c sigh2 "\"Look, just... just sit down for a minute and try to compose yourself, okay?\""
    "I put my hands on both of his shoulders and force him down on one of the benches they have in the lobby."
    "Honestly, though. This place is massive. It's so full of people that even I feel a bit on edge. I can definitely understand why Jun would be bothered."
    mc 1 c wry "\"Just breathe, okay? Nice, long, deep breaths.\""
    "I try showing him some breathing exercises, but he fails pathetically at all of them."
    "His breathing is so rapid and ragged that I'm afraid he just might give himself a heart attack."
    "Actually, could he be having a panic attack?"
    if day5 == "jun":
        "Wait, could it be that what he had last time was a panic attack? I've never had one, but aren't the symptoms something like this?"
        "Agh, great. It's at times like these that I wish I knew something about medicine."
    else:
        "Rapid, shallow breathing, stuttering, pacing round nervously. It does sound like the descriptions I've heard... but then again, I'm no doctor so I can't really tell."
    "I kneel down to stay eye level with him, putting one hand on his shoulder and the other on his chest."
    "I immediately start to feel awkward as memories of what happened yesterday flash in my mind. Still, I try to ignore them as best as I can."
    "Right now I need to help Jun!"
    "Alright, first thing's first, what was it that I learned about panic attacks. I remember Shoichi telling me about times..."
    mc 1 c wry "\"Jun, look at me, okay. Look me in the eyes. Can you do that for me?\""
    "Jun sets his eyes on my face. His eyes are bloodshot and scared, but he does as I say, slowly nodding for me."
    mc 1 c curious "\"Good, now, focus on my hand on your chest. Can you feel my hand on your chest? Can you feel it moving when you breathe?\""
    "Jun looks down at my hand, making me move it to his chin and raise his head so he only looks at my face."
    mc 1 c wry "\"No, you don't need to look at it. Just feel my hand on your chest.\""
    j "\"O-Okay...\""
    mc 1 c considerate "\"Now, I want you to breathe for me, okay. Just focus on moving my hand around when you do it. Four seconds in, two seconds out. Four seconds in, two seconds out. Can you do that for me?\""
    j "\"I-I'll try.\""
    "Jun starts to take deep breaths."
    show j 1 c wince at fdis
    "He struggles a bit at first, but his breathing starts to become more and more regular."
    show j 1 c sigh at fdis, five
    "It takes a couple of minutes, but I can feel his body relaxing with my hands."
    "I make sure to smile at him the whole time, reminding him that I'm here to help."
    "I feel a bit awkward about doing this in such a public place, but my number one priority should be Jun."
    mc 1 c smile "\"There we go, you're doing a lot better already. Do you feel any better?\""
    show j 1 c wince at fdis
    play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    j "\"A-A little. I don't feel like I'm going to suffocate anymore...\""
    show j 1 c watch at fdis
    mc 1 c happy "\"That's good. See, there's nothing for you to be afraid of. This is just a day like any other. You're fine.\""
    show j 1 c considerate at fdis
    "He swallows hard and nods."
    "It makes me feel a bit better to be able to help him in some way."
    "At least I don't have to stand around and feel helpless."
    show j 1 c watch at fdis
    mc 1 c smile "\"Now, how about we talk about something more pleasant, huh? Is there anything you'd like to talk about?\""
    show j 1 c think at fdis
    j "\"Not really.\""
    mc 1 c smile "\"Come on, there must be something! Just say the first thing that comes to mind.\""
    show j 1 c wince at fdis
    j "\"W-Well... there's this book series I really like. The new book came out just last week, but I don't have the money to buy it yet.\""
    mc 1 c happy "\"Oh, that's cool. What's this series about?\""
    "I was just looking to distract him with some pleasant conversation, but this might actually be interesting."
    show j 1 c think at fdis
    j "\"It's called \"The Murderous Queen Trilogy\". It's a story set in a fantasy world about a former queen who escapes death after her husband is overthrown and killed in a rebellion and then goes around looking for vengeance.\""
    mc 1 c shock "\"That... doesn't sound at all like something I'd expect you to read.\""
    show j 1 c annoyed at fdis
    j "\"Why? You think I can't enjoy a mature, complex story?\""
    mc 1 c considerate "\"W-what?! No, no!\""
    "... Yes."
    mc 1 c wince "\"W-Well, it's just that you tend to go for more... uhm, happier stories. I've heard you talking about some games before, and they were all very teen friendly. This one sounds like something that wouldn't be recommended for a 17 year old.\""
    show j 1 c think at fdis
    j "\"Well, the rating is 17+. And I'm nineteen, I don't see the issue here.\""
    mc 1 c wince "\"... True enough.\""
    "If a bit out of character... at least in my opinion."
    show j 1 c watch at fdis
    mc 1 c "\"And the book that was just released was... what, the second one?\""
    "Jun shakes his head in negative."
    show j 1 c think at fdis
    j "\"It's the last one. I read the first two and they were really good."
    show j 1 c considerate at fdis
    extend " Although, I'll admit, I was just fourteen when the first one came out, so I wasn't actually supposed to read it. My dad was just feeling very tired when he took me out to buy a birthday present and didn't look at what book I picked.\""
    "Sounds like lousy parenting at its finest..."
    j "\"Hehe, mom was really mad when she found the book. Poor dad got the brunt of it.\""
    "As he should, letting a fourteen year old kid read something like that... but then again, I've played games that were like that when I was a kid so I guess I'm one to talk."
    show j 1 c watch at fdis
    mc 1 c considerate "\"Well, it sounds like you like it a lot. What was the name of his third book? Just for curiosity's sake.\""
    "I might just end up buying it for him later."
    show j 1 c wince at fdis
    j "\"Uhh... what was it called again?"
    show j 1 c gentle at fdis
    extend " Ah, \"The Red Keep\"!\""
    mc 1 c smile "Huh, that's an interesting name."
    "... I might end up picking up a copy of these for myself."
    mc 1 c happy "\"Well, what else? Tell me more about it.\""
    show j 1 c wince at fdis
    j "\"U-uhm... I'd rather not. You might want to read them in the future and I don't want to spoil you.\""
    mc 1 c smile "\"Psshh, spoilers are my bread and butter, I don't care about spoilers. Come on, tell me more!\""
    "Anything that keeps you talking and stops you from freaking out."
    show j 1 c blush at fdis
    j "\"W-Well, okay... But first... can you take your hand from my chest, there's some people looking and it's a bit embarrassing.\""
    mc 1 c shockb "\"Ah!\""
    "I only notice it when he points out, but I pull away immediately and get up on my feet."
    "I try looking slyly around and see that there are a couple heads turned in our direction."
    "Damn, my cheeks feel hot right now."
    "I guess Jun wasn't the only one being distracted by our conversation."
    mc 1 c avoidb "\"I'll just... Ahem... I'll just sit right here.\""
    "I take a seat next to Jun on the bench. All the awkwardness that I was feeling because of what happened yesterday has now come back full force."
    "Damn, it feels weird all of sudden."
    "No no! Power through it! I've gotten this far, I can't allow him to start moping again!"
    mc 1 c considerate "\"W-well, anyway, you were going to tell me more about those books?\""
    show j 1 c happy at fdis
    "Jun smiles and it immediately sets my heart at ease."
    "It's so good to see a smile back on his face."
    show j 1 c smile at fdis
    j "\"Well, the story starts with Ella, that's the protagonist's name by the way, Ella Rishal, in a tavern. A man sits next to her and tells her she looks pretty and starts flirting with her and she asks him to buy her a drink.\""
    j "\"When he's not looking, she slips a bit of viper venom in his ale and excuses herself to go to the bathroom after she sees him drink it, then she escapes the tavern while he dies.\""
    j "\"Then we get taken to a flashback about how she was forced to go on exile after her husband was dethroned and murdered and their children were killed. She talks about making a deal with a witch to grant her a new face that she wants to use to kill the ones who masterminded the rebellion. Then she-"
    scene ConcertLobby
    show j 1 c think at fdis, five
    with fade
    "As the minutes start to pass, I see that Jun's body has already stopped twitching entirely."
    "I finally begin to rest a bit easy knowing that he's calmed down immensely."
    "He continues to talk to me about his book, enthusiastically describing the story to me while still keeping himself very vague at certain points (I guess he really doesn't want to spoil me after all)."
    "He starts to perk up considerably, his gestures become more full of energy and his smile becomes wider."
    "After what I assume have been fifteen minutes, he's almost back to his usual self, which makes me sigh in relief."
    show j 1 c shock at fdis
    j "\"Huh? Are you alright, [povFirstName]-san? I'm not boring you, am I?\""
    mc 1 c considerate "\"No no, nothing like that! I'm just relieved.\""
    show j 1 c think at fdis
    j "\"Relieved? About what?\""
    "He cocks his head to the side, like a curious little puppy. It's adorable to see him behaving like this again."
    "I decide that there's no harm in telling him."
    show j 1 c watch at fdis
    mc 1 c considerate "\"Well, look at how much you've calmed down. You're acting like yourself again.\""
    show j 1 c shock at fdis
    "Jun blinks a couple of time, his eyes becoming wider."
    show j 1 c happy at fdis
    j "\"Hey, you're right. I {i}do{/i} feel better!\""
    play sound "music/fabric.ogg"
    show j 1 c happy at fdis:
        ease .2 zoom 1.5 xoffset -50 yoffset 230
    mc 1 c shock "\"See? I'm just glad I managed to calm you do- Agh!\""
    "I'm suddenly wrapped in a mass of orange fur when Jun pounces on me out of nowhere, enveloping me in a warm, tight hug."
    j "\"Thank you so much! I didn't even realize it, but you were worrying about me all this time!\""
    "While the feeling is certainly nice, the first thing I worry about is the people around us seeing... well, this."
    play sound "music/tap.ogg"
    "I give him a few taps on his arm."
    mc 1 c considerate "\"Okay okay, easy there, tiger. We're still in public, remember?\""
    show j 1 c blush at fdis, five:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    j "\"Ah, right!\""
    "His tail immediately stands upright as he pulls back from me, scratching his reddened cheeks in embarrassment."
    show j 1 c considerate at fdis
    j "\"Sorry. I just kinda lost control.\""
    mc 1 c happy "\"It's alright. I don't mind, it's a nice feeling. Just not when we're in public, okay?\""
    show j 1 c happy at fdis
    j "\"Okay!\""
    "Oh man, he's just too precious."
    "Please, Jun, never change."
    "?" "\"Jun Kobayashi?!\""
    show j 1 c watch at fdis
    "A voice calls Jun's name. We both turn our heads to search for it at the same time."
    show j 1 c watch at fdis, three with move
    show aku 1 c smile at seven with moveiridis
    "We both see a lion dressed in a red shirt and a pair of cargo pants."
    "The lion stares at Jun with wide eyes, his mouth open in an \"o\" shape."
    "?" "\"Oh my God, I didn't believe it when I saw your name in the list of participants but it really is you!\""
    show j 1 c wince at fdis
    j "\"U-Uhm... I'm sorry, but... Who are you?\""
    "?" "\"Oh, right. It's been seven years, no wonder you wouldn't recognize me. I grew a lot taller and I didn't even have a mane back then.\""
    show j 1 c shock at fdis
    j "\"Wait... Akutagawa-kun?!\""
    "The lion smiles, putting a hand on his waist, making the bracelets he has on his wrist clink."
    aku "\"You haven't changed much, all things considered. Well, you grew a bit... in both directions. Still, I heard you gave up the piano after that incident seven years ago. What brought you back?\""
    show j 1 c wince at fdis
    j "\"...\""
    "Noticing the change in Jun's demeanor, the lion awkwardly scratches the back of his neck."
    aku "\"Sorry, I let curiosity get the better of me. I understand if you don't want to talk about it. Still, it's good to see you again. Maybe I'll finally have my revenge!\""
    mc 1 c curious "\"Uhh... I'm sorry to intrude in your conversation, but... what's going on? What's this talk about vengeance?\""
    show j 1 c cshock at fdis, jumping
    "My sudden interjection makes Jun jump up from his seat."
    "He apparently completely forgot that I was here."
    show j 1 c wince at fdis
    j "\"Oh, that's right!"
    show j 1 c smile at fdis
    extend " [povFirstName]-san, this is Shinji Akutagawa. He used to be a friend of mine back when I still participated in competitions.\""
    aku "\"Oh, please, let's just call it what it is. No need to play friends with me. You and I were bitter rivals!\""
    show j 1 c think at fdis
    j "\"Huh? We were?\""
    "He falters, gasping and gaping in shock."
    aku "\"H-Hey, are you kidding me?! Of course we were rivals, I always had to share the podium with you, you have no idea how bitter about it I was!\""
    j "\"Wait, we shared the podium? I don't remember that.\""
    "Jun scratches at his cheek as the lion looks at him, completely flabbergasted."
    aku "\"Are you seriously telling me you forgot about me?!\""
    show j 1 c wince at fdis
    j "\"W-Well, I didn't forget. I remember talking to you before and after the competitions, but I don't remember how you played or where you placed. I wasn't really paying attention.\""
    aku "\"Wha- You self absorbed prick! I spent all this time thinking about you and you didn't even remember me?!\""
    "Big, comical tears start forming around his eyes as he begins to pout."
    show j 1 c shock at fdis
    j "\"Ah, s-sorry. I didn't mean it like tha-\""
    aku "\"Forget it! You and I will square off on the stage and I will destroy you.\""
    aku "\"Just make sure that weak set list of yours doesn't spell your doom! I'll make sure the name Shinji Akutagawa is one you'll never forget!\""
    show aku 1 c smile at offscreenright with moveoridis
    show j 1 c shock at fdis, five with move
    play sound "music/jogging.ogg"
    "He runs off without a second glance, leaving us to eat dust."
    show j 1 c wince at fdis
    j "\"W-Well, that was a bit...\""
    mc 1 c sigh "\"Weird?\""
    "Jun nods in affirmative, still looking confused."
    show j 1 c watch at fdis
    j "\"By the way, [povFirstName]-san, when are the others getting here? It's already...\""
    play sound "music/phonebeep.ogg"
    show j 1 c shock at fdis
    j "\" 9:35?!\""
    mc 1 c "\"Well, Kei-kun and Saya said they'd arrive at about 9:40, so they should be getting here soon. Shoichi will probably still take at least an hour since he's dealing with some issues at school.\""
    show j 1 c think at fdis
    j "\"Issues?\""
    mc 1 c avoid "\"Yeah. I, uh... kinda forgot to get excused to come here today. Shoichi's at school right now trying to set things straight so I won't get punished for skipping.\""
    show j 1 c shock at fdis
    j "\"Wait... don't you need parental permission for that? How is he gonna get you excused?\""
    mc 1 c avoid "\"Well... he'll just work his magic. He's student council president, I'm sure he'll manage.\""
    show j 1 c wince at fdis
    j "\"I-I see...\""
    show j 1 c at fdis
    j "\"Wait...\""
    show j 1 c shock at fdis, shake1
    j "\"{size=+2}Why is he the one getting you excused?!{/size}\""
    "Guh..."
    mc 1 c avoidb "\"W-Well... It was his choice to go in my place.\""
    show j 1 c at fdis
    j "\"Why would he do that?\""
    mc 1 c avoidb "\"Well, he was a bit worried that I'd... err...\""
    "Jun stares at me with inquisitive eyes."
    show j 1 c watch at fdis
    j "\"Yes?\""
    mc 1 c wince "\"... He was a bit worried that I'd say something I shouldn't and end up getting in trouble.\""
    show j 1 c judge at fdis
    j "\"...\""
    mc 1 c avoidb "\"...\""
    show j 1 c sigh at fdis
    j "\"So...\""
    show j 1 c bored at fdis
    j "\"He basically said you were too incompetent to do it.\""
    mc 1 c annoyed "\"{size=+4}That is not what he said!{/size}\"" with hpunch
    j "\"But it's what he meant.\""
    "Ugh..."
    mc 1 c avoid "\"When did you get so snarky?\""
    show j 1 c happy at fdis
    j "\"I learned from watching you guys talking to each other. Isn't this what you do?\""
    "Oh boy, I suddenly feel like a bad influence..."
    show j 1 c smile at fdis
    j "\"Hehe, don't worry, I'm just pulling your leg. It was funny seeing that look on your face.\""
    "We've created a monster."
    show j 1 c think at fdis
    j "\"Anyway... can you try calling Shoichi-san and ask him if he's gonna take long. I kinda need him to be here soon.\""
    mc 1 c curious "\"Why? Your performance isn't due until 12:30.\""
    show j 1 c wince at fdis
    j "\"W-Well, yeah, but all of the performers need to go backstage to prepare half an hour before the first performance starts, and then we just stay there to concentrate on our performance.\""
    mc 1 c shock "\"Wait... isn't the first performance in an hour?\""
    j "\"Yeah.\""
    mc 1 c shock "\"...\""
    j "\"W-What?\""
    mc 1 c annoyed "\"{size=+4}Why didn't you say this sooner?!{/size}\"" with hpunch
    show j 1 c wince at fdis, fidget, jumping
    j "\"Waaah! Y-You didn't ask!\""
    mc 1 c annoyed "\"So if I don't ask you something you just won't tell me?!\""
    mc 1 c annoyed "\"Crap, I have to call Shoichi and tell him to hurry!\""
    j "\"Sor-\""
    stop music2 fadeout 2.5
    mc 1 c annoyed "\"Later!\""
    hide j 1 c wince with dissolve
    "I walk away from Jun, going to the entrance of the concert hall, where the phone signal is a bit better."
    play sound "music/phonebeep.ogg"
    "Two bars... That should be plenty."
    "Now to see if I can actually call him."
    play sound "music/calling.ogg"
    "..."
    "....."
    s 1 c think "\"[povFirstName]?\""
    mc 1 c annoyed "\"{size=+4}Get here now!{/size}\""
    s 1 c wince "\"...\""
    s 1 c sigh "\"Jeez, are you trying to make me deaf or something? What's going on, is everything okay?\""
    mc 1 c "\"Are you still in school?!\""
    s 1 c "\"I just left. I'm heading to the train station now. Why?\""
    mc 1 c wince "\"Run to it, you must get the first train that comes by!\""
    s 1 c shock "\"What?! The next train is in five minutes, there's no way I can catch it. What's this even about?\""
    mc 1 c "\"Jun has to go backstage in half an hour. If you don't hurry here, you won't be able to see him until after his performance.\""
    s 1 c "\"...\""
    mc 1 c curious "\"... Shoich-\""
    s 1 c scorn "\"{size=+4}Why didn't you tell me this sooner?!{/size}\"" with hpunch
    "I have to pull the phone away from my face as I'm at risk of going deaf."
    "Jeez, this isn't my fault, why am I the one getting yelled at?\""
    mc 1 c wince "\"Didn't you just complain about me doing just tha-\""
    s 1 c scorn "\"I don't care! Why wasn't I informed sooner?!\""
    mc 1 c avoid "\"Because I didn't know myself. Jun only told me about it now.\""
    "I hear groaning on the other side, followed by the sound of running steps."
    s 1 c scorn "\"Forget it, I'm gonna try to make it to the station in time for the next train. Don't let him go anywhere until I get there!\""
    mc 1 c think "\"I'll try but I don't know if I c-\""
    s 1 c scorn "\"{size=+2}Don't let him go anywhere until I get there!{/size}\""
    play sound "music/phonebeep.ogg"
    "Just like that, he shuts the call off and I'm left with ringing in my ear."
    "Well, I guess that takes care of that..."
    show k 1 c at fdis, five with moveiridis
    "Now, to go back to J-"
    show k 1 c smile at fdis
    k "\"Boo!\""
    mc 1 c cshock "\"Ahhh!\"" with hpunch
    "I nearly fall on my ass when Keisuke suddenly jumps in front of me, scaring the crap out of me."
    show k 2 c gentle at fdis
    k "\"Heh, gotcha.\""
    mc 1 c wince "\"W-What the hell?!\""
    k "\"Sorry, I saw you on your phone and I couldn't resist.\""
    mc 1 c sigh "\"When did you even get here?\""
    show k 1 c smile at fdis
    k "\"Oh, about thirty seconds ago. I came in with Saya, but she left to look for Kobayashi.\""
    show k 1 c calm at fdis
    k "\"And, like I said, I couldn't resist, so I stayed behind.\""
    "Keisuke chuckles, puffing up his chest with satisfaction."
    "I sigh."
    show k 1 c smile at fdis
    mc 1 c sigh "\"That's... that's just great for you. Can we please get back to Jun and, apparently, Saya?\""
    show k 1 c at fdis
    k "\"Wow, someone's in a bad mood.\""
    mc 1 c sigh2 "\"Yeah, I didn't have a very good day.\""
    k "\"What happened?\""
    mc 1 c sigh "\"Well, it was crazy, really. You wouldn't believe me if I told you.\""
    show k 2 c think at fdis
    "Keisuke scratches at his chin, obviously curious."
    k "\"Try me.\""
    mc 1 c think "\"Okay, then...\""
    mc 1 c smile "Well, I came here to the Concert Hall today and met up with Jun. Then, something happened and I had to step away for a second...\""
    show k 1 c at fdis
    k "\"Yeah?\""
    "Keisuke's always been a sucker for dramatic stories, so I make sure to make a dramatic pause."
    "He gobbles it up like a rabbit with carrots... or a hare."
    "Eh, doesn't matter."
    mc 1 c judge "\"... Then, all of a sudden...\""
    show k 1 c shock at fdis
    k "\"...\""
    mc 1 c annoyed "\"This crazy, lunatic hare jumps out of nowhere and screams at my face!\""
    show k 1 c avoid at fdis
    "His face immediately deflates."
    "I see the twinkle of humor and curiosity in his eyes die out."
    k "\"Har har. Very funny.\""
    mc 1 c smile "\"You think so too? Great! I myself thought it was hysterical.\""
    show k 1 c sigh at fdis
    k "\"You really are an idiot.\""
    mc 1 c "\"Well, consider that payback for nearly giving me a heart attack.\""
    show k 1 c avoid at fdis
    k "\"Fine, fine, I get it. Let's just go join the others already...\""
    show k 1 c avoid at fdis, offscreenright with moveoridis
    "Without waiting for a response, Kei-kun walks away from me."
    mc 1 c wince "\"H-Hey, don't just leave me hanging!\""
    show sa 1 c at offscreenright
    show j 1 c at offscreenright
    play sound "music/jogging.ogg"
    show k 1 c sigh at fdis, three
    show j 1 c wince at fdis, five
    show sa 1 c laugh at fdis, eight
    with dissolve
    play music2 "music/BGM/Hanging Out.ogg" fadein 5.0
    "Jeez, did Kei-kun run towards them? How did he get there so much quicker than I did?"
    "The first thing I notice when I reach them is that Saya seems to be talking very excitedly."
    "... Wait, what's with the look on those two's faces?"
    sa "\"-the ball went ~gyuuun, and then I hit it with my racket like ~zoooom, then it hit the ground and made a huge ~paaaaah-\""
    "..."
    k "\"... Is... is that an actual conversation?\""
    mc 1 c wince "\"... I'm not sure if that's even Japanese...\""
    show sa 1 c smile at fdis
    sa "\"Ah, [povFirstName]-kun!\""
    show j 1 c wince behind sa
    show sa 1 c laugh at fdis:
        ease .2 zoom 1.5 xoffset -50 yoffset 230
    "Saya quickly hops towards me, waving."
    show j 1 c watch at fdis
    show k 1 c at fdis
    mc 1 c "\"Hey, Sa-\""
    show j 1 c shock at fdis
    show k 1 c wince at fdis
    play sound "music/stab.ogg"
    "!" with hpunch
    sa "\"Good morning!\""
    "She jabs me in the torso with her outstretched hand, hitting me right between the ribs."
    mc 1 c cshock "\"Agh...\""
    play sound "music/tap.ogg"
    "I have to hold onto Kei-kun's shoulder to keep myself from falling down."
    "She completely knocked the air out of me with that."
    mc 1 c cshock "\"I- I can't breathe...\""
    show sa 1 c at fdis
    sa "\"Hm?\""
    "Saya stands in her spot, looking innocent."
    sa "\"Are you alright, [povFirstName]? You don't look so good.\""
    mc 1 c annoyed "\"Of course I don't look good, you just knocked the air out of me!\""
    show sa 1 c bored at fdis behind j:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    sa "\"What? I didn't hit you that hard! It was just a friendly poke.\""
    show j 1 c wince at fdis
    show k 1 c worried at fdis
    j "\"N-No, Mizoguchi-san, that was a bit...\""
    k "\"Remind me never to walk within arms reach of you...\""
    sa "\"Oh, come on, I was just wishing him a good morning...\""
    "She stares guiltily at me as I gasp for air."
    j "\"If you do that to someone when you're trying to be nice to them, I'm afraid of what you'd do when you're angry...\""
    k "\"I've heard some stories.\""
    show j 1 c watch at fdis
    j "\"Oh, really? Do tell.\""
    show k 1 c avoid at fdis
    k "\"Well, there's the time wh-\""
    show sa 1 c pout at fdis
    sa "\"Hey! Quit it!\""
    show k 1 c wince at fdis, shake1
    show j 1 c cshock at fdis, shake1
    "Jun and Keisuke" "\"Y-Yes, ma'am!\""
    "Ah..."
    mc 1 c sigh "\"Oh boy, I wasn't ready to get stabbed in the gut first thing in the morning.\""
    show sa 1 c bored at fdis
    sa "\"I already said I was sorry for that...\""
    show k 1 c worried at fdis
    show j 1 c watch at fdis
    k "\"Actually, you di-\""
    show sa 1 c doom at fdis
    show k 1 c shock at fdis
    "She gives him a frightening, murderous glance."
    show k 1 c avoid at fdis
    k "\"K-Kobayashi-kun, she said she already apologized for it!\""
    show j 1 c cshock at fdis
    j "\"Wha-?!\""
    "Seriously, you're trying to deflect the blame to someone else now?!"
    mc 1 c sigh "\"Great, the day has barely started and you're already terrorizing the community.\""
    show sa 1 c pout2b at fdis, shake1
    sa "\"Nuuh...\""
    show k 1 c at fdis
    show j 1 c watch at fdis
    "Well, I feel like I can finally stand on my own two feet again..."
    mc 1 c avoid "\"Man, I thought I was gonna puke my guts out after that one.\""
    show sa 1 c complain at fdis
    sa "\"S-Sorry...\""
    "At least now she's apologizing."
    k "\"What were you two talking about anyway?\""
    show sa 1 c laugh at fdis
    sa "\"Oh! I watched a video of a Challenger level tournament yesterday, it was amazing!\""
    k "\"You mean the one that happened in Miami?\""
    show sa 1 c smile at fdis
    sa "\"You saw it too?!\""
    show k 1 c calm at fdis
    k "\"A little. I watched about fifteen minutes of it before it made me want to go outside and practice.\""
    show j 1 c think at fdis
    j "\"Must be nice being able to watch the things you like on TV. Concerts and orchestras don't get nearly as much attention as sports do.\""
    show k 1 c at fdis
    k "\"Not many people like classical music to begin with, so it'd be a tough sell. But there are still some channels dedicated to that sort of content.\""
    show j 1 c wince at fdis
    j "\"And they're usually premium channels that you have to pay top dollar to watch.\""
    show k 1 c worried at fdis
    k "\"That's... true.\""
    show sa 1 c laugh at fdis
    sa "\"You won't have to worry about that sort of thing for long! You'll be going to a music academy next year, you'll see tons of concerts and orchestras.\""
    show j 1 c wince at fdis, shake1
    show k 1 c at fdis
    play sound "music/stab.ogg"
    j "\"Ugh...\""
    "Aaahhh, damn it, Saya!"
    "Do you have any idea how long it took me to calm him down?"
    "Now you had to go and remind him of it!"
    show sa 1 c at fdis
    j "\"It's... not that easy. Unless I graduate from a very prestigious academy, finding a job as composer would be hard.\""
    j "\"And those are really expensive. I need a scholarship to be able to attend, and I need an impeccable record to get one.\""
    show j 1 c sigh at fdis
    j "\"I basically have to join every piano competition possible and have to win them all just to have a chance.\""
    show k 1 c worried at fdis
    k "\"Yeesh... sounds rough...\""
    show j 1 c wry at fdis
    j "\"That's what I get for being out of the stages for seven years.\""
    show k 1 c at fdis
    show j 1 c watch at fdis
    mc 1 c think "\"Oh yeah, this reminds me..."
    mc 1 c think "\"Jun apparently has a rival. What was his name again... err...\""
    "T-Teruyama? Akiyama? What was the lion called again?"
    show j 1 c think at fdis
    j "\"Akutagawa-kun?\""
    "Ah, yes, that's his name!"
    "Boy, I was way off the mark on this one."
    mc 1 c smile "\"Yeah. It's this big lion guy. He said he was Jun's biggest rival back when they still performed in competitions. Apparently, Jun beat him every single time.\""
    mc 1 c happy "\"You should have seen it. He came here swearing vengeance and all that.\""
    show sa 1 c think at fdis
    sa "\"Wow, sounds a bit cliche.\""
    show j 1 c considerate at fdis
    show sa 1 c at fdis
    "Jun lets out a nervous laugh."
    j "\"Ahaha, yeah. Akutagawa-kun was always pretty... intense. He had a penchant for being dramatic, even when we were kids.\""
    show j 1 c think at fdis
    j "\"I guess that hasn't changed even now.\""
    show k 1 c smile at fdis
    k "\"Well, this could be fun. That means we actually get to watch some competition.\""
    show k 1 c calm at fdis
    k "\"Oh, I know! I have the list of participants here with me, we could check out what he's performing!\""
    show j 1 c happy at fdis
    j "\"Ooh, that's a great idea. I haven't checked it yet!\""
    "Kei-kun pulls a flyer from his pocket and unfolds it."
    "In it are the pictures of many kids, with some details written next to them."
    "It seems that these are their set lists."
    show j 1 c smile at fdis
    show k 1 c at fdis
    k "\"Each player is alloted fifteen minutes to perform, and they can perform as many songs as they want in that time.\""
    k "\"Let's see, Kobayashi-kun, you're going with... \"Allegro Apassionato\" and Chopin's \"Étude Op. 25, No. 12\". Hmm, not quite hitting the fifteen minutes mark.\""
    show j 1 c considerate at fdis
    j "\"Haha, yeah. I was afraid stamina might be an issue, so I chose to keep my set list a bit on the short side.\""
    show j 1 c watch at fdis
    j "\"I'm actually surprised you know these songs.\""
    show k 1 c sigh at fdis
    k "\"Really? Son of a rich house? I was force-fed this kind of music since I was seven. My grandmother tried to force me to play the violin.\""
    show j 1 c wince at fdis
    j "\"Doesn't sound like it was very fun.\""
    show j 1 c watch at fdis
    show k 1 c wry at fdis
    k "\"It wasn't, but I survived."
    show k 1 c at fdis
    extend " Anyway, let's see... Akutagawa, Akutagawa.\""
    k "\"Ah, there he i-"
    show k 1 c shock at fdis
    extend " ...!!?\""
    "Kei-kun nearly buries his face in the paper."
    show j 1 c wince at fdis
    show sa 1 c shock at fdis
    k "\"{size=+4}Huuuuhhh?!{/size}\"" with hpunch
    "His voice is so loud that it leaves my ears ringing."
    show sa 1 c bored at fdis
    sa "\"Jesus, give us a warning before you do that!\""
    mc 1 c wince "\"Is there something wrong with him?\""
    show k 1 c avoid at fdis
    show sa 1 c at fdis
    k "\"W-Well... He's performing... Franz Liszt...\""
    show j 1 c shock at fdis
    "I stare at him in confusion."
    mc 1 c curious "\"Is that name supposed to mean something to u-\""
    "When I look to the side, I see Jun's face has nearly lost all its color."
    mc 1 c shock "\"J-Jun?! Are you okay?\""
    j "\"W-What song?\""
    "His voice came out crackly and incredibly small."
    k "\"... \"Grande Fantaisie de bravoure sur La Clochette\"\""
    mc 1 c sigh "\"... The who of what now?\""
    show j 1 c wince at fdis
    "Jun swallows audibly."
    "I am sure his face has gone at least three tones whiter."
    "His voice comes out almost in a monotone."
    j "\"Franz Liszt is a world renowned composer. His works are said to be some of the most technically difficult in existence.\""
    j "\"That song... \"Grande Fantaisie\" is considered one of his most difficult pieces. Not many pianists attempt to play it because of how difficult and demanding it is.\""
    j "\"That song is exactly fourteen minutes and fifty-nine seconds long. Even for an easier piece, stamina would be a concern.\""
    j "\"For that song though... If he plays it mildly well, he's going to almost certainly win the competition. If he plays it well enough, he could even get world recognition. That's how difficult that piece is.\""
    show sa 1 c shock at fdis
    mc 1 c shock "\"W-Wait, the way you're saying it, sounds like he's already got this in the bag... Do you think he can even pull it off?\""
    sa "\"Yeah, I mean... didn't you say that even professionals tend to stay away from that song? What makes you think a high schooler can play it?\""
    k "\"Why would he submit it as his set list if he can't play it?\""
    show sa 1 c annoyed at fdis
    sa "\"Kei-kuuun, you're not helping!\""
    show k 1 c worried at fdis
    k "\"W-Well, I'm sorry. I'm just trying to be realistic...\""
    j "\"I...\""
    j "\"Seven years ago, I don't think he could have... If he were good enough to do this song, then I'd remember it, but...\""
    j "\"I-I need to talk to the organizers!\""
    show j 1 c wince at fdis, ten
    show sa 1 c bored at fdis, five
    with move
    "I cut Jun off before he's able to walk away, putting myself in his path."
    mc 1 c shock "\"Whoa whoa whoa. Don't tell me you're going to be dropping out because of this!\""
    show j 1 c annoyed at fdis
    "I notice Jun clenching his fist so hard that I'm afraid his claws are going to puncture the palm of his hand."
    j "\"I'm going to increase the difficulty of my own set list.\""
    show k 1 c shock at fdis
    show sa 1 c shock at fdis
    k "\"W-whoa, calm down for just a second there! Didn't you say just a second ago that you chose your songs because stamina was a concern? If you increase the difficulty even further, then-\""
    j "\"I have to fight fire with fire. Now I understand the comment he made on my set list. It isn't bold enough. He's gonna completely bury me unless I take a risk.\""
    mc 1 c shock "\"And what are you even going to perform? You haven't practiced any other songs.\""
    j "\"... There are two I already know by heart. I used to perform them a lot when I was younger.\""
    show k 1 c at fdis
    show sa 1 c at fdis
    k "\"... Which ones?\""
    if jun_met == True:
        show j 1 c at fdis
        j "\"Beethoven's Moonlight Sonata 3rd Movement, \"Presto Agitato\" and-\""
        mc 1 c shock "\"Wait, I remember that name...\""
        "!"
        mc 1 c shock "\"Isn't that the song you were playing when we met?!\""
        show j 1 c smile at fdis
        "He nods."
        show j 1 c happy at fdis
        j "\"It was the song I played the most. It was almost always in my set list for all the competitions I took part in.\""
        "I still remember walking into the Music Room that day."
        show j 1 c at fdis
        j "\"The other one is Chopin's \"Etude Opus 25 No. 11, Winter Wind\".\""
    else:
        show j 1 c at fdis
        j "\"Beethoven's Moonlight Sonata 3rd Movement, \"Presto Agitato\" and Chopin's \"Etude Opus 25 No. 11, Winter Wind\".\""
    show j 1 c wince at fdis
    j "\"They might not be as difficult as the song Akutagawa-kun chose, but they're both very technical.\""
    show j 1 c at fdis
    j "\"If I play the two of them together, I might have a chance at winning.\""
    show k 1 c worried at fdis
    k "\"They're also incredibly fast paced and demanding. Are you sure you can even handle playing the two together? You'd be mashing the keys almost non-stop for ten minutes.\""
    show j 1 c wince at fdis
    j "\"If Akutagawa-kun is willing to take this much risk with his song selection, then I have to do the same.\""
    show k 1 c at fdis
    k "\"The difference is that he had time to practice his song, you didn't. You were too busy practicing your old set list!\""
    "Jun purses his lips, shoving his hand down his pockets and looking down at the floor."
    j "\"I know that, but... but I have to try. Like I said, I know these two songs by heart. I performed them so many times, I can play them in my sleep!\""
    show k 1 c avoid at fdis
    k "\"But can you play them as well as you need to? If this guy's performance is even remotely {i}decent{/i}, then yours is going to be absolutely perfect to be able to win!\""
    show j 1 c annoyed at fdis
    j "\"{size=+2}I know that!{/size}\""
    show k 1 c shock at fdis
    "Jun raises his voice, making both Saya and I jump back a step."
    "Keisuke stares at him, bewildered."
    "I even notice a few heads turning our way."
    show j 1 c wince at fdis
    "Jun, realizing the sudden attention coming our way, crosses his arms, looking back down at the floor."
    j "\"I know that... but if I don't do it, then I'm just going to guarantee a loss. You said it yourself, even with those two songs, I'd need to be absolutely perfect to stand a chance.\""
    show k 1 c nervous at fdis
    j "\"What chance do you think I have with my current list?\""
    "Kei-kun crosses his arms, rubbing his right elbow with his hand as he looks away, biting his lip."
    k "\"... None.\""
    show j 1 c wry at fdis
    j "\"Exactly.\""
    "The two just stand awkwardly rooted to their spots, not looking at each other."
    "The atmosphere has suddenly become so weird and awkward that it's hard for me to say anything."
    show j 1 c watch at fdis
    show k 1 c at fdis
    show sa 1 c smile at fdis
    sa "\"Well, if that's how it is, then you should just get to it already.\""
    "That's when Saya speaks up, drawing everyone's attention to herself."
    "She stands there, smiling, looking either completely oblivious of the weird mood surrounding all of us, or just simply not caring about it."
    show j 1 c wince at fdis
    j "\"I'm not even sure if they're going to allow me. The set lists are decided weeks in advance...\""
    show sa 1 c laugh at fdis
    sa "\"Well, you won't know if they will until you try. Nothing's gonna happen if you don't try.\""
    show j 1 c happy at fdis
    show sa 1 c at fdis
    j "\"You're right! I'm gonna be right back!\""
    show j 1 c smile at fdis, offscreenright with moveoridis
    show k 1 c at fdis, three
    show sa 1 c at fdis, seven
    with move
    "Jun walks away, looking for the competition's organizers."
    "Now that I think about it, one of us should probably go with him, huh?"
    "I exchange glances with Saya, who apparently picks right up on what I'm thinking."
    sa "\"I'm gonna go after Kobayashi-kun. Make sure he doesn't get lost.\""
    show k 1 c smile at fdis
    "Kei-kun nods in agreement."
    k "\"Probably for the best. Let's not forget he still gets lost at school. I wouldn't put it past him getting lost here.\""
    show sa 1 c happy at fdis
    sa "\"Alright. I'll catch up to you guys later.\""
    play sound "music/running.ogg"
    show sa 1 c at fdis, offscreenright with moveoridis
    show k 1 c smile at fdis, five with move
    sa 1 c sigh "\"Kobayashi-kun, wait up!\""
    "With that, Kei-kun and I are left alone in the middle of the busy lobby."
    k "\"Well, I guess that's that. Hopefully he doesn't end up in that much trouble.\""
    mc 1 c think "\"Yeah... I'm still surprised you know classical music though.\""
    show k 1 c calm at fdis
    k "\"What, really, you too? Come on! Rich kid from a traditional family? You really doubted for even a second that I wouldn't be exposed to classical music?\""
    mc 1 c "\"You said your grandmother forced you to practice the violin. Does that mean you play?\""
    show k 1 c at fdis
    k "\"A little. I was forced to practice for three years, but I purposely did badly whenever she came to watch just to spite her. Eventually she just gave up saying I was \"horrid\" at it.\""
    show k 1 c calm at fdis
    k "\"I was never forced to touch an instrument again.\""
    if day5 == "keisuke":
        show k 2 c gentle at fdis
        k "\"That only made her even more furious when I started practicing guitar and turned out to be good at it.\""
        show k 1 c smile at fdis
        k "\"\"Why didn't you put that much effort into the violin?!\" she kept asking. It was very amusing, although after that she became even more insufferable to deal with.\""
    else:
        show k 1 c smile at fdis
        k "\"Heh, if only she knew I was just faking it. I was actually kinda decent at it, I just hated the damn thing.\""
    show k 1 c avoid at fdis
    k "\"Dad got the raw end of the deal, though. From what he tells me, she was much more relentless when he was a kid. She forced him to pick up the piano because she wanted the prestige of having her son be a pianist.\""
    show k 1 c sigh at fdis
    k "\"Then he fell in love with the piano and decided to become a professional pianist. She, of course, was all too happy to oblige since he was only the second child and was never going to inherit the business anyway.\""
    k "\"{i}Then{/i} right when he landed his dream offer to play for a prestigious orchestra in France, his brother died and she forced him to take up the business.\""
    mc 1 c shock "\"W-wait, so she-\""
    show k 1 c avoid at fdis
    k "\"She forced him to play the instrument when he didn't want to, then when he decided that he actually liked it and wanted to make his life about it, she took it away from him and forced him to become a businessman. Only one of the many reasons I hate my grandmother.\""
    mc 1 c wince "\"That's... really awful. I'm surprised you even told me this, you never said much about your home life.\""
    show k 1 c at fdis
    k "\"No one's ever asked and I never really had any reason to say it. This time it just kinda came up as an interesting tidbit on the conversation we were already having.\""
    mc 1 c "\"So you won't volunteer any information about yourself unless someone asks you?\""
    show k 1 c eyesc at fdis
    k "\"Nope. I'm not that interesting a person to just start talking about myself for no reason.\""
    show k 1 c at fdis
    k "\"Unless it's something that can be relevant to the conversation, that is.\""
    mc 1 c smile "\"So... you're saying if I asked some questions about you, you'd answer them?\""
    show k 1 c eyesc at fdis
    k "\"Maybe later.\""
    mc 1 c smile "\"Why later? So you {i}are{/i} evading this after all.\""
    show k 1 c at fdis
    k "\"No, it's just that I see Urata coming our way and it looks like he might drop any second now.\""
    play sound "music/jogging.ogg"
    mc 1 c shock "\"Wha-\""
    show s 1 c wince at fdis, seven with moveiridis
    show k 1 c smile at fdis, three with move
    s "\"Ha... ha... Jun-kun... where...\""
    k "\"He went over to the organizer's office.\""
    show s 1 c scorn at fdis
    s "\"W-What?! I told you to keep him from leaving until I got here!\""
    play sound "music/tap.ogg"
    "Shoichi grabs my shoulders, baring his fangs at me in anger."
    mc 1 c think "\"Uhh... as much as I {i}love{/i} getting blamed for everything...\""
    "I pull both of his hands away from my arms."
    mc 1 c "\"He hasn't gone backstage. He just went to have a word with the organizers of the competition to see if he could change his set list.\""
    show s 1 c shock at fdis
    s "\"Oh!\""
    show s 1 c avoid at fdis
    "He stares at me awkwardly, slinking back to a less threatening position and scratching at the back of his neck."
    "I cross my arms and shift all my weight to my left leg, giving him a smug look."
    show s 1 c annoyedb at fdis
    "Shoichi looks down at the floor, embarrassed."
    s "\"Sorry.\""
    "I laugh, having some innocent fun at his expense."
    show s 1 c annoyed at fdis
    show k 1 c at fdis
    k "\"By the way, why are you so sweaty? You smell like you just ran a marathon.\""
    "Kei-kun pinches his nose mid sentence, making his voice come out all nasally and funny."
    show s 1 c sigh at fdis
    s "\"That's because I {i}did{/i}. I had to run from our school to the station in under five minutes if I wanted to catch the closest train. Then I had to run from the station all the way over here!\""
    "I give him a thumbs up."
    mc 1 c smile "\"Good job!\""
    s "\"I can barely even stand, don't praise me as if I were a kid who finally learned to clear the table!\""
    mc 1 c think "\"Alright...\""
    mc 1 c smile "\"Who's a good boy? Who's a good b-\""
    play sound "music/tap.ogg"
    show s 1 c scorn:
        ease .2 zoom 1.5 xoffset -30 yoffset 200
    s "\"{size=+4}What am I, a dog?!{/size}\""
    "Shoichi grabs my shoulders again, giving me a firm shake."
    show k 1 c worried at fdis
    k "\"Well, techni-\""
    s "\"Shut uuuuuuup!\""
    show k 1 c calm at fdis
    "Kei-kun's lips quiver up in another half smile, full of smugness and satisfaction."
    mc 1 c think "\"Well, what else do you expect me to say? I didn't know I had to praise you every time you did something nice. Like you said, you're not a kid or a dog.\""
    show k 1 c worried at fdis
    k "\"Well, techni\""
    "Shoichi and [povFirstName]" "\"Shut up!\""
    show k 2 c gentle at fdis
    "Kei-kun chuckles, seemingly very happy with himself."
    show s 1 c avoidb at fdis
    s "\"You don't have to praise me, it's just... it feels nice when you do, okay?\""
    mc 1 c smile "\"Alright, alright, I get it.\""
    menu:
        "Praise Shoichi":
            $ praiseshoichi = True
            "I reach upwards to put my hand on top of his head, petting affably a few times, even scratching at the back of his ears a little bit."
            mc 1 c smile "\"You did good, Sho. Jun is going to be very happy that you made it."
            s "\"I-I...\""
            "He blushes furiously, looking down at his feet instead of at me."
            show s 1 c blush at fdis
            s "\"T-Thank you.\""
            mc 1 c happy "\"Yeah, you did great, man. It was really nice that you went through all that trouble for Jun.\""
            show s 1 c avoidb at fdis
            s "\"W-Well, it wasn't that much trouble...\""
            show k 2 c gentle at fdis
            "From the corner of my eye, I can see Keisuke stifling a laugh."
            "Heh, he's never seen Shoichi being bashful before."
            "I'll admit, it's quite a 180 from his usual attitude."
            "A devious idea shines in my mind and I don't hesitate to try it."
            mc 1 c happy "\"Yeah, you did good. You did very good. Who's a good boy? Who's a good boy?\""
            show s 1 c blush at fdis
            "He blushes further, muttering out his words almost incoherently."
            s "\"I a-"
            show s 1 c scorn at fdis
            extend " Hey, wait a second!\""
            show s 1 c scorn:
                ease .2 zoom 1.0 xoffset 0 yoffset 0
            "He steps away from me, looking super pissed."
            s "\"What did you almost make me say?!\""
            show k 2 c gentleb at fdis
            "Unable to hold it any longer, Kei-kun bursts into laughter, making Shoichi finally remember that he was actually there."
            k "\"I have no idea what it is I just saw, but I'm glad to have seen it.\""
            show s 1 c shock at fdis
            s "\"W-Wha-\""
            show s 1 c avoidb at fdis
            "Shoichi blushes something fierce. Even the tips of his ears go red as they both flop downwards on his face."
            s "\"You'll pretend you never saw this!\""
            show k 1 c smile at fdis
            k "\"Ha! We both know that that's going to be impossible.\""
            s "\"You suck...\""
            show k 2 c gentle at fdis
            k "\"I'm well aware of that. What else is new?\""
            mc 1 c smile "\"You already had your fun, Kei-kun. Lay off him a little.\""
            show k 1 c smile at fdis
            k "\"Aww, I was just getting started.\""
            mc 1 c "\"Well, just stop, okay?\""
            show k 1 c calm at fdis
            k "\"Alright, alright. I won't tease him about it anymore.\""
            s "\"Thank you.\""
            show s 1 c sigh at fdis
            "Shoichi breathes a sigh of relief as his entire body relaxes."
        "Don't":
            $ praiseshoichi = False
            show s 1 c:
                ease .2 zoom 1.0 xoffset 0 yoffset 0
            mc 1 c smile "\"Still, it's not up to me to say anything. I'm not the one who has to feel grateful for that. It's Jun.\""
            show s 1 c avoid at fdis
            s "\"I suppose you're right.\""
            show k 1 c smile at fdis
            k "\"Aww, what a waste. You could have made him whine and beg like a dog for some attention.\""
            show s 1 c doom at fdis
            s "\"Are you trying to pick a fight with me?\""
            mc 1 c sigh "\"Are you two really going to start this in the middle of the Lobby?\""
            show s 1 c wince at fdis
            s "\"Ugh, you're right. Don't want to call too much attention to ourselves.\""
            show k 1 c at fdis
            k "\"I think he's more worried about being seen with us.\""
            show s 1 c smile at fdis
            s "\"What? There's no way he'd be embarrassed by us. I'm sure he just doesn't want us to make fools out of ourselves for our sakes. Right, [povFirstName]?\""
            mc 1 c think "\"Pfft, it's like you don't know me at all. Of course I don't want to be seen with two people who just start yelling at random in public.\""
            show s 1 c wince at fdis, shake1
            play sound "music/stab.ogg"
            s "\"Guh... so cruel.\""
            mc 1 c sigh "\"Quit being so melodramatic, it's not like I told you I hate you or something.\""
            show k 1 c sigh at fdis
            k "\"Honestly, Urata. You should have gone into theater instead of volleyball. What with how dramatic you can be.\""
            show s 1 c scorn at fdis
            s "\"You two suck!\""
            mc 1 c think "\"Kei-kun is right, you can really be super dramatic when you want to.\""
            mc 1 c think "\"I guess that's something you have in common with that friend of Jun.\""
            show s 1 c sigh at fdis
            "Shoichi sighs, rubbing his temples with the tip of his fingers."
    s "\"Alright alright, fine. Enough with the \"tease Shoichi\" game.\""
    show k 1 c sigh at fdis
    k "\"Sure. Let's play the \"Please go pat yourself dry in the bathroom\" game instead. I heard it's very fun.\""
    show k 1 c at fdis
    k "\"And while you're at it, please use some deodorant. This strong smell of sweaty dog is offensive to my nose.\""
    show s 1 c scorn at fdis
    s "\"Wha- Now you're just going out of your way to insult me!\""
    show k 1 c avoid at fdis
    "Kei-kun pinches his nose again and starts breathing through his mouth."
    k "\"I'm doing no such thing. My nose is just really sensitive and the smell is starting to make me nauseous.\""
    show s 1 c shock at fdis
    s "\"Wha- [povFirstName], you don't mind it, right?!\""
    menu:
        "I don't mind it.":
            mc 1 c think "\"I don't really mind your smell.\""
            show k 1 c uncomfortable at fdis
            k "\"What?!\""
            show s 1 c smile at fdis
            s "\"See, I to-\""
            show k 1 c at fdis
            mc 1 c think "\"{i}But{/i} that doesn't change the fact that you're in public, you should take other people into consideration.\""
            mc 1 c "\"Even if Kei-kun and I don't mind it, there are other people who are going to be sitting next to us. You should do it so as to not bother {i}them{/i}.\""
            show s 1 c wince at fdis
            s "\"Ugh...\""
            show s 1 c sigh at fdis
            s "\"Why is it that you're only reasonable when being reasonable is something that would annoy me?\""
            show k 1 c sigh at fdis
            k "\"Why are you being so against this in the first place? I can't believe you'd be okay with being sweaty and smelly in public.\""
            show s 1 c avoid at fdis
            s "\"I'm not! I just...\""
            "Shoichi kicks up some dust from the floor, looking down at his feet."
            mc 1 c sigh "\"Oh God, I'm not gonna wait fifteen minutes for you to finally admit this.\""
            "I turn to Kei-kun."
        "I mind it.":
            mc 1 c think "\"Well, Shoichi, let me remember the words that a wise man once said. What was it again? Hmm... Ah, that's right!\""
            mc 1 c smile "\"Dude, you fucking stink. Don't you shower?\""
            show s 1 c smile at fdis
            s "\"Sheesh, that bad?\""
            mc 1 c think "\"You smell like wet dog. And, believe me, I know what wet dog smells like.\""
            show s 1 c laugh at fdis
            "Shoichi laughs, covering up his mouth in an attempt to stifle it."
            show k 1 c sigh at fdis
            k "\"You two might be used to it by now, but I'm not a dog, nor do I live with a dog. I'm not used to this.\""
            mc 1 c wry "\"Nah, the smell is a bit strong even for me. Shoichi, you should definitely go clean yourself up.\""
            mc 1 c think "\"Plus, you don't want to offend the other people who are going to be sitting next to us, right?\""
            show s 1 c sigh at fdis
            s "\"You're right. The last thing I want to do is bother other people.\""
            show s 1 c wry at fdis
            s "\"But...\""
            "He gives me a meaningful, pitiful look."
            mc 1 c sigh "\"You're gonna have to get over that at some point.\""
            show s 1 c sigh at fdis
            s "\"I know! Still...\""
            show k 1 c at fdis
            k "\"Uh...\""
            "Kei-kun curves his body, leaning toward us."
            "He lifts his hand and waves."
            k "\"Hello? Person who has no idea what you two are talking about here.\""
            show s 1 c wince at fdis
            s "\"Oh, r-right. W-well...\""
            s "\"How can I say this... I, uhm...\""
            "He looks away, pretending to think about something."
            "In reality, he's just hoping that Kei-kun will forget about it and change the subject."
            "I sigh."
    mc 1 c sigh "\"Shoichi's afraid of public bathrooms.\""
    stop music2 fadeout 2.5
    play music3 "music/BGM/Mischief Maker.ogg" fadein 5.0
    show k 1 c shock at fdis
    show s 1 c shock at fdis
    k "\"What?!\""
    s "\"You are such a tattletale!\""
    k "\"Wha- Whe- Ho- Wh- Why?! Why would you be afraid of public bathrooms?!\""
    show s 1 c avoidb at fdis
    s "\"I'm not {i}afraid{/i} of them! Not... not exactly. I just think they're really, really gross and I'd rather not go inside one. I feel like I can catch an STD just by breathing the air inside them.\""
    show k 1 c sigh at fdis
    k "\"Wha- This building is national property, the whole place is spotless! You could eat off of the bathrooms' counters.\""
    show s 1 c sigh at fdis
    s "\"Eww no, don't say that even as a joke. I think I can feel my stomach crawling up and curling itself into a ball.\""
    k "\"You're weird! I guess this explains why I never saw you going to the bathroom whenever we go out.\""
    show k 1 c at fdis
    k "\"But wait. What about school? Doesn't that count as a public bathroom?\""
    show s 1 c at fdis
    s "\"Are you kidding. I spend more time at school than I do my own home, that place is already a second home to me.\""
    show k 1 c sigh at fdis
    k "\"What? But that doesn't make any sense!\""
    show s 1 c avoid at fdis
    "Shoichi scratches his neck, looking away."
    mc 1 c smile "\"In essence, Shoichi is basically just weird.\""
    show s 1 c sigh at fdis
    s "\"How cruel of you to say this to my face...\""
    mc 1 c "\"Oh, please! I didn't say anything that you yourself haven't said before.\""
    s "\"Wha- But I- Ah, screw it. You're right.\""
    show k 2 c gentle at fdis
    "Kei-kun and I laugh at his reaction, making him shoot us a death glare."
    show k 1 c smile at fdis
    show s 1 c annoyed at fdis
    s "\"So I don't like dirty places. So what? Everyone's got something they don't like.\""
    k "\"Yeah, but people don't usually have fears that keep them from doing something as basic as going to the bathroom.\""
    show s 1 c avoid at fdis
    s "\"I already told you, I'm not {i}afraid{/i} of going in the bathroom, I just...\""
    show k 1 c at fdis
    k "\"Just?\""
    show s 1 c sigh at fdis
    s "\"I'd just rather stay away from it because it makes me feel uneasy and uncomfortable, okay?\""
    show k 1 c sigh at fdis
    k "\"... Dude, that's the textbook definition of fear.\""
    show k 2 c gentle at fdis
    show s 1 c scorn at fdis
    "Keisuke laughs, making Shoichi shoot him yet another death glare."
    s "\"Bite me.\""
    show k 1 c smile at fdis
    k "\"Are you sure? Hares have pretty strong teeth.\""
    "He opens his mouth a little, pointing at his teeth."
    show s 1 c sigh at fdis
    s "\"What? I didn't mean literally!\""
    show k 2 c gentle at fdis
    k "\"Too late!\""
    "Kei-kun lunges at Shoichi with his mouth open, going for his neck."
    "... Are you a hare or a vampire?"
    show s 1 c scorn at fdis
    play sound "music/fall.ogg"
    "Shoichi reacts fast, pushing him away."
    s "\"What?! No!\""
    "Kei-kun falls back, laughing."
    k "\"I'm sorry, your reaction was just too funny. I couldn't resist.\""
    show s 1 c sigh at fdis
    s "\"You do realize we're in public, right?\""
    show k 1 c smile at fdis
    k "\"Eh, so we're horsing around a little. Big deal.\""
    s "\"You have the weirdest sense of humor... {i}and{/i} of timing.\""
    "... It's the pot calling the kettle black."
    if praiseshoichi == True:
        mc 1 c sigh "\"Okay, you two, behave. I don't want to be seen with two guys acting like complete lunatics in a public place.\""
        show k 1 c at fdis
        k "\"Why do you even care? It's not like you're going to meet these people again. You're an athelete, you're part of a completely different circle.\""
        k "\"People who go to tennis games don't usually attend classical music competitions so it's not like any of them know you.\""
        mc 1 c sigh "\"Oh, really? Because you, me, Shoichi and Saya all go to tennis games... And yet we're here.\""
        show k 1 c avoid at fdis
        k "\"Well, yeah. But that's because we know Jun and he's competing.\""
        mc 1 c sigh "\"Yes. And if it's possible for those circumstances to exist for us, doesn't it also stand to reason that it can be true for someone else?\""
        mc 1 c "\"Besides, you yourself admitted that you like classical music.\""
        show k 2 c think at fdis
        k "\"I... suppose you're right. I guess I went a little bit overboard.\""
        s "\"Yeah... Besides, if [povFirstName] is the one lecturing you about this sort of thing, then you should take that as a clear sign that you need to rein it in a little.\""
        mc 1 c annoyed "\"Hey!\""
        show k 1 c at fdis
        k "\"That's true.\""
        mc 1 c avoid "\"Wha- I'm not {i}that{/i} bad.\""
        mc 1 c scorn "\"You're the ones who keep arguing in public and end up getting people complaining about you.\""
        mc 1 c sigh "\"Remember that time in the diner a while back?\""
        show k 1 c worried at fdis, shake1
        show s 1 c wince at fdis, shake1
        play sound "music/stab.ogg"
        "Keisuke and Shoichi" "\"Ugh...\" \ \"Uu...\""
        "I give them a smug smile."
    else:
        mc 1 c sigh "\"... You two remember what I said about going away to not be seen with two crazies, right?\""
        show k 1 c worried at fdis
        k "\"Tch. Come on, you're being no fun.\""
        mc 1 c sigh "\"I'm not trying to have fun. We're in public.\""
        mc 1 c "\"If Saya were here, she'd slap this nonsense out of the both of you.\""
        show s 1 c scorn at fdis
        s "\"Hang on, what did I do? He's the one playing around.\""
        mc 1 c "\"I don't care.\""
        s "\"Sounds a bit unfair to me...\""
        show k 1 c at fdis
        "Kei-kun gives him a mock punch on the arm."
        k "\"Oh, just give up. This is what it means to have equal treatment.\""
        show s 1 c sigh at fdis
        s "\"Sure. Suddenly I feel like I'm back in elementary school, where the teacher punishes the whole class because some students are making too much noise.\""
        show k 1 c smile at fdis
        k "\"We've all been there.\""
        s "\"Yeah. Some of us just were on the other side of the situation.\""
        "He looks over to me with an accusatory look."
        "I shrug."
        mc 1 c smile "\"Hey, I was a happy kid. You were the one with an attitude problem.\""
        "He crosses both of his arms, looking away, groaning."
        s "\"Yeah yeah, no need to remind me. Young me was an ass.\""
        show k 1 c at fdis
        k "\"I don't get it. Was Urata any different when you two were kids?\""
        mc 1 c think "\"Well-\""
        show s 1 c scorn at fdis
        s "\"Don't you dare!\""
        "He cuts me off with an angry, murderous look."
        mc 1 c "\"Yeah, sorry. It looks like I'm not allowed to discuss this.\""
        show k 1 c calm at fdis
        k "\"Heh, sure. Whatever.\""
    stop music3 fadeout 2.5
    hide j 1 c
    hide sa 1 c
    play music2 "music/BGM/On My Way.ogg"
    show s 1 c at four
    show k 1 c smile at two
    with move
    show sa 1 c smile at fdis, six
    show j 1 c at eight
    with moveiridis
    sa "\"Yo, we're back!\""
    k "\"So I see. Did everything go okay?\""
    show j 1 c happy at fdis
    j "\"Yeah. They opened an exception for me since I was actually increasing the difficulty of my performance.\""
    show j 1 c think at fdis
    j "\"Although they did say that they'll double the amount of points deducted for each mistake I make.\""
    show s 1 c shock at fdis
    s "\"What? That's crazy! Why would you agree to that?\""
    show j 1 c annoyed at fdis
    j "\"I'm not planning on making any mistakes.\""
    show sa 1 c laugh at fdis
    sa "\"Haha, see? I asked him the same question and he answered me with the same thing.\""
    show j 1 c wince at fdis, shake1
    "Saya gives him a few enthusiastic slaps on the back, laughing."
    "She nearly sends him down to the floor."
    sa "\"When did you get so bold, Kobayashi-kun?\""
    j "\"Ow, ow! Mizoguchi-san, please stop slapping me!\""
    show sa 1 c pout at fdis
    sa "\"Wha- not you too\""
    show sa 1 c bored at fdis
    sa "\"I'm not even that strong, I'm not Shoichi!\""
    show s 1 c smile at fdis
    s "\"It's not about being strong, Saya-chan. It's about not knowing how to control your strength.\""
    show sa 1 c pout at fdis
    sa "\"Oh, like I want to hear that from {i}you{/i}.\""
    "Saya gives him a cold stare."
    show s 1 c sigh at fdis
    s "\"Wha- I don't hurt people at random.\""
    mc 1 c think "\"Anymore.\""
    "I add to his sentence.\""
    s "\"Yeah yeah, anymore.\""
    show sa 1 c argue at fdis
    "Saya huffs, unamused."
    show j 1 c watch at fdis
    sa "\"Alright, I won't touch anyone ever again. I'll spend the rest of my cold, sad existence without knowing what the warmth of another person's touch is. Happy now?\""
    "She starts being melodramatic in an attempt to state her displeasure."
    j "\"Yes.\""
    "Without batting an eye and giving no attention whatsoever to her drama, Jun answers her with a single word."
    show sa 1 c bored at fdis
    sa "\"Jeez, that's cruel, Kobayashi-kun.\""
    show j 1 c happy at fdis
    j "\"Any time.\""
    "He answers with feigned ignorance."
    show sa 1 c at fdis
    "The reason I can tell it's not legit ignorance is because his mouth is quivering with an attempt to suppress laughter."
    if praiseshoichi == False:
        "Shoichi leans close to my ear."
        show s 1 c think at fdis
        s "\"And you say {i}I'm{/i} dramatic.\""
        mc 1 c smile "\"You're both dramatic. It's why you get along so well.\""
        show s 1 c smile at fdis
        "He leans back away from me and just stares at Saya and Jun's exchange with amusement."
    show k 1 c calm at fdis
    k "\"You know, you two could definitely form a comedy duo. Kobayashi-kun could be the straight man and Mizoguchi-san could be the funny girl.\""
    "A comedy duo or double act is a traditional form of humor in which a duo has completely different personalities, where the straight man is usually serious and down-to-earth and the funny man is ridiculous and a tad crazy."
    show s 1 c think at fdis
    show k 1 c smile at fdis
    s "\"The same could also be said of the following pairings: Me and You, You and Saya, [povFirstName] and Jun-kun and Me and [povFirstName].\""
    mc 1 c annoyed "\"Hey, I disagree with that. I am {i}clearly{/i} the straight man in our pairing.\""
    show k 1 c calm at fdis
    k "\"Who are you trying to fool here? You're barely qualified to be the straight man in your pairing with Kobayashi-kun.\""
    mc 1 c annoyed "\"Hey, rude!\""
    show s 1 c sigh at fdis
    s "\"The only thing worse than a fool is a fool in denial.\""
    mc 1 c shock "\"H-Hey!\""
    show j 1 c considerate at fdis
    show sa 1 c sigh at fdis
    j "\"Guys, please don't start arguing. I have to leave to go backstage in two minutes and I'd very much prefer if you didn't kill each other while I was gone.\""
    show s 1 c smile at fdis
    show k 1 c smile at fdis
    "Kei-kun and Shoichi fist bump, smiling smugly at me."
    "I stare at them, exasperated."
    show sa 1 c at fdis
    sa "\"When does your performance start again?\""
    show j 1 c think at fdis
    j "\"12:30. But I still need to go backstage to prepare. All participants are supposed to wait back there for their performances.\""
    show sa 1 c bored at fdis
    sa "\"Ugh... sounds like waiting for your performance to come up will be boring.\""
    show j 1 c bored at fdis
    j "\"No offense, Mizoguchi-san, but why did you come if you dislike classical music that much?\""
    show sa 1 c laugh at fdis
    sa "\"To cheer you on, of course!{nw}"
    show sa 1 c pout2 at fdis
    extend " I was actually gonna bring a bunch of bandanas and a cheering flag I had made at home, but Kei-kun said I wasn't allowed to.\""
    "She pouts."
    show k 1 c sigh at fdis
    k "\"I already told you, this is classical music. Making any sort of noise during the performances is in bad form. You might distract the competitors.\""
    sa "\"Boo, that's boring.\""
    show k 1 c at fdis
    k "\"If you don't want to watch it, then just go home.\""
    show sa 1 c complain at fdis
    sa "\"Noooo, then I won't be able to watch Jun-kun perform.\""
    show k 1 c annoyed at fdis
    k "\"Then stop whining!\""
    show sa 1 c pout2 at fdis
    sa "\"You don't have to say it like that.\""
    show k 1 c sigh at fdis
    k "\"Mizoguchi-san, you already knew this was going to be a classical music performance, you knew other people would be performing and you knew you didn't like this sort of music. So why did you choose to only complain {i}now{/i}? Why even show up at all?\""
    show sa 1 c laugh at fdis
    sa "\"Because I have to encourage Kobayashi-kun, of course!\""
    show k 1 c at fdis
    show sa 1 c at fdis
    "Kei-kun looked over to Jun and snapped his fingers, calling his attention."
    k "\"Hey, Kobayashi.\""
    show j 1 c shock at fdis
    j "\"Wha- Yeah?\""
    k "\"How do you feel about somebody coming to watch who hates the music and is only here because they think they have to.\""
    show j 1 c wince at fdis
    j "\"Wha- w-well...\""
    "Jun glances over at Saya, sheepishly rubbing his cheek."
    show j 1 c wry at fdis
    j "\"I want people to appreciate my music, so... it makes me feel a bit uncomfortable if someone is coming over against their will.\""
    show sa 1 c shock at fdis, shake1
    play sound "music/stab.ogg"
    show sa 1 c sigh at fdis
    sa "\"Guh...\""
    show j 1 c considerate at fdis
    j "\"Ah, B-But I'm really happy to have you all here. I'm really touched that you'd come all the way here to see me perform, even more so knowing that you don't really like classical music!\""
    show s 1 c think at fdis
    show sa 1 c pout2 at fdis
    s "\"So are you happy about it or not, which one is it?\""
    mc 1 c "\"Yeah, you're 100\% contradicting yourself.\""
    show j 1 c wince at fdis
    j "\"U-Uhm...\""
    show k 1 c sigh at fdis
    k "\"I might have gone a little too far, sorry. I was only trying to make the point that complaining about being here in front of Kobayashi would only make him feel bad.\""
    show k 1 c smile at fdis
    k "\"Sorry for putting you on the spot, Kobayashi.\""
    "As if on cue, Saya bows down."
    sa "\"I'm sorry if I've been complaining too much!\""
    show j 1 c shockb at fdis, shake1
    j "\"Awawa, n-no it's fine.\""
    show j 1 c think at fdis
    j "\"It doesn't bother me... too much.\""
    show j 1 c considerate at fdis
    j "\"Honestly, I'm just happy you all cared enough to come see me.\""
    show sa 1 c laugh at fdis
    sa "\"Of course we'd show up. You're one of us now!\""
    "Saya gives him a thumbs up, smiling widely."
    show sa 1 c smile at fdis
    show k 1 c calm at fdis
    k "\"Yes, you're one of us now... My condolences.\""
    show s 1 c happy at fdis
    s "\"Honestly, I wouldn't lose this for anything. Just go kick some ass, okay?\""
    play sound "music/tap.ogg"
    "Shoichi gives him a few light taps on the back."
    show s 1 c smile at fdis
    show k 1 c smile at fdis
    show j 1 c watch at fdis
    "After they all say their piece, all four of them turn over to me, looking at me with expectation."
    mc 1 c curious "\"... What?\""
    sa "\"Come on, [povFirstName], give him some words of encouragement!\""
    mc 1 c wince "\"Oh, uh... well...\""
    show j 1 c wry at fdis
    j "\"It's okay, [povFirstName]-san. You don't need to say anything.\""
    show j 1 c watch at fdis
    play sound "music/announcement.ogg"
    "A beeping noise echoes throughout the lobby's sound system."
    "Announcer" "\"Competitors in the 12th Sakura University Piano Competition, please move backstage for preparations.\""
    show j 1 c considerate at fdis
    j "\"I have to go.\""
    show sa 1 c argue at fdis
    sa "\"Already?! Can't you stay a little longer?\""
    show j 1 c wry at fdis
    j "\"No, it's easier for the organizers if we're all already backstage. Plus, I need to change and I need time to focus, so...\""
    show sa 1 c bored at fdis
    sa "\"Nuuu...{nw}"
    show sa 1 c wry at fdis
    extend " Good luck, Kobayashi-kun.\""
    show j 1 c considerate at fdis, ten with move
    "Jun nods, turning around to join the mass of people who started going towards the backstage."
    show sa 1 c at fdis
    mc 1 c shock "\"Jun!\""
    "I don't know why, but I suddenly had an urge to speak up. I called out to him after he took a few steps away from us."
    show j 1 c watch at fdis
    "Jun turned around, looking at me with curiosity."
    mc 1 c happy "\"I believe in you!\""
    show j 1 c shock at fdis
    "Jun looked dazed for a second, as if he didn't quite grasp my words."
    show j 1 c happyb at fdis
    j "\"Thank you!\""
    show j 1 c happyb at offscreenright with moveoridis
    show s 1 c smile at fdis, five
    show k 1 c smile at fdis, two
    show sa 1 c pout2 at fdis, eight
    with move
    play sound "music/running.ogg"
    "This time, he ran away, quickly joining the others and disappearing from our sights."
    s "\"Well, I guess we already know who his favorite is.\""
    mc 1 c shock "\"Huh?\""
    show k 1 c sigh at fdis
    sa "\"Why was he so much happier when you encouraged him?! You didn't even say five words!\""
    mc 1 c wince "\"Wha-\""
    k "\"When did the two of you get so close that you'd be able to lift his spirits that much?\""
    mc 1 c shock "\"Even you?!\""
    show sa 1 c argue at fdis
    sa "\"Ahh! Whatever, I don't care anymore. I'm gonna go to the bathroom.\""
    show k 1 c at fdis
    k "\"Shouting out \"Ahh, I don't care anymore!\" isn't the sort of thing a person does when they, quote unquote, don't care.\""
    show sa 1 c annoyed at fdis
    sa "\"Shut up!\"" with hpunch
    show k 1 c smile at fdis
    k "\"Yes ma'am.\""
    show sa 1 c annoyed at fdis, offscreenright with moveoridis
    show k 1 c smile at fdis, three
    show s 1 c smile at fdis, seven
    with move
    play sound "music/jogging.ogg"
    mc 1 c wince "\"Uh... I've known her for twelve years and I still have no clue how her mind operates.\""
    show s 1 c think at fdis
    s "\"And you'll know her for seventy years more and {i}still{/i} won't understand it. Just roll with it.\""
    play sound "music/tap.ogg"
    "Shoichi puts a hand on my shoulder."
    show s 1 c wry at fdis
    s "\"Well, as much as I dread the idea, I have to go freshen up a bit. Can't exactly sit down to watch the performances smelling like a musky husky.\""
    show k 1 c at fdis
    k "\"They'll be opening the sitting area now, so I'm gonna go get us some seats.\""
    stop music fadeout 2.5
    stop music2 fadeout 2.5
    stop music3 fadeout 3.0
    show ConcertHall with fade
    "A girl gets up from the piano, bowing to the crowd and walking out of the stage."
    "She gets a very lukewarm reception, with only a few claps here and there."
    k 1 c "\"Weak.\""
    "Kei-kun has criticized every single performance that has been put out so far."
    sa 1 c bored "\"I know classical tends to be boring, but I can barely stay awake right now.\""
    s 1 c think "\"Hey, Urushihara, have they all been that bad? You haven't had a single good thing to say about their performances.\""
    k 1 c avoid "\"Not bad per se, but... Not good either. None of them stands out.\""
    k 1 c "\"Hey, [povFirstName]-san, you're the only one who's seen Kobayashi perform. Do you think he's better than them?\""
    mc 1 c think "\"Well...\""
    "None of their performances has made me feel the same way as Jun's did."
    "When I saw him play, I felt like the music was calling to me, tugging at my heartstrings."
    "I felt like I needed to get closer, to feel all the keys pounding with my whole body."
    "But these kids... I don't feel anything."
    "No rush, no excitement."
    "Nothing."
    mc 1 c think "\"I don't really know much about music, but I know that they don't really do anything for me. I think Jun is much better.\""
    k 1 c eyesc "\"Hm...\""
    "Announcer" "\"And now the next performer will be Shinji Akutagawa, performing Franz Liszt's \"Grande Fantaisie de bravoure sur La Clochette\".\""
    "!"
    "The crowd stats clapping as a lion walks into the stage donning a black suit, waving at the audience with a confident smile on his face."
    k 1 c "\"That's him...\""
    s 1 c think "\"How do you think his performance will go?\""
    k 1 c avoid "\"I don't know... I hope for Kobayashi's sake that he's not good...\""
    "The lion sits down in front of the piano. The audience goes dead silent almost by instinct."
    "Suddenly, I feel very on edge. The few seconds of silence before he begins his performance start to fill me with a sense of dread."
    "What if he's good? What then?"
    "I feel like my heart is going to explode."
    "If I'm like this, how must Jun be feeling right about now?"
    "... I hope he's okay."
    play music2 "music/BGM/Classical/Grande Fantaisie 1.ogg"
    "He starts performing and I instinctively hold my breath."
    "The keys echo softly, slowly beginning to weave a slow melody."
    "This doesn't seem as amazing as Kei-kun mentioned."
    "I start feeling angry at him and Jun for making me feel so on edge for nothing."
    mc 1 c smile "\"This is what you're afraid of? This is no-\""
    k 1 c avoid "\"No. He's good.\""
    mc 1 c wince "\"But this song sounds so... easy.\""
    k 1 c worried "\"Grande Fantaisie starts off really slow. It suddenly speeds up at about three minutes.\""
    k 1 c "\"That's what will make or break his performance. If he can do that part correctly, then...\""
    k 1 c avoid "\"! Here it comes...\""
    play music2 "music/BGM/Classical/Grande Fantaisie 2.ogg"
    "!"
    "He suddenly speeds up his performance so much that I can barely recognize it as the same song."
    "He's not just fast. He's oppressively fast."
    "I feel as if I'm suddenly being pounded into submission. I instinctively hold my breath, my heart rate increases exponentially."
    "I feel like the sheer magnitude of his performance forbids me from uttering a single word."
    "There's so much I want to say, but my body is frozen in place and refuses to listen."
    "The words are caught in my throat, unable to be let out."
    "If it's like this... if he's this good..."
    "Shit, please don't let Jun be watching this performance. Please God, don't let him watch this."
    "If he does... I'm pretty sure his spirit will break."
    stop music2 fadeout 5.0
    "He finally stops his performance. It feels as if the enormous weight that was pressing down on the audience is suddenly lifted as everyone breathes a collective sigh of relief."
    "Akutagawa-kun gets up from his seat, panting heavily. His legs wobble a bit, but he makes his way to the front of the stage, bowing down to the audience."
    show ConcertHall with hpunch
    play sound "music/crowdcheer2.ogg"
    "The crowd immediately erupts in cheers, giving Akutagawa-kun a standing ovation."
    "The sound is so loud that it almost shakes the entire Concert Hall."
    "His was without a doubt the best performance so far, and you can tell that from how the crowd reacts."
    play sound "music/announcement.ogg"
    "After bowing down to the crowd, he walks out of the stage as there is another beep followed by the announcer's voice."
    "Announcer" "\"There will now be a fifteen minute interval."
    "Audience members are advised to not be away from their seats for more than ten minutes, as they might miss some of the ensuing performance.\""
    k 1 c worried "\"Shit...\""
    "Kei-kun was the first to break the deathly silence that had fallen on us."
    sa 1 c sigh "\"... When's Kobayashi-kun's performance?\""
    "I swallow hard, trying to steady myself."
    mc 1 c wince "\"He's next...\""
    s 1 c wince "\"Double shit.\""
    sa 1 c bored "\"Yeah...\""
    "Having to follow up on a performance like that... I don't think he'd be able to."
    "If he watched this..."
    "Something in my heart tells me that he watched that performance. And I {i}know{/i} he wouldn't be able to go out on stage after that."
    mc 1 c "\"Save my seat for me...\""
    s 1 c shock "\"Wha-\""
    "I get up from my seat and run out of the hall..."
    scene ConcertBackstage with fade
    "I run to the backstage entrance. When I try walking through the door, a ram dressed in a uniform stops me."
    "Employee" "\"Excuse me, sir. Only competitors are allowed backstage.\""
    mc 1 c scorn "\"I need to see my friend!\""
    "Employee" "\"I'm sorry, but like I said, only competitors are al-\""
    mc 1 c scorn "\"{size=+2}Like I care!{/size}\"" with hpunch
    "I push him to the side, nearly knocking him against the corridor wall and run past him."
    "Employee" "\"Wait, stop!\""
    "It isn't hard at all for me to bolt past him."
    "As soon as I'm in, I start looking for Jun."
    "Where could he- Ah!"
    "I stop dead in my tracks as I see a familiar figure wearing a white suit sitting down on the floor, his face buried in his knees and his entire body shaking as very quiet sobs come out of him."
    mc 1 c shock "\"... Jun?\""
    "I timidly reach out to him, putting a hand on his shoulder."
    show j 1 s flustert at fdis, five with dissolve
    "He looks up at me, tears streaming down his face."
    j "\"W-wh... [povFirstName]-san?\""
    "It takes him a while to recognize me. As soon as he does, he wipes his tears away with the cuff of his suit."
    show j 1 s wince at fdis
    j "\"W-what are you doing here?\""
    mc 1 c worried "\"I-\""
    "Employee" "\"Hey!\""
    "The employee I knocked aside when I barged my way into the backstage comes up to us, looking furious."
    "Employee" "\"You, kid, come back here!\""
    "Shit."
    play sound "music/tap.ogg"
    "He grabs my arm and starts pulling me away from Jun."
    mc 1 c annoyed "\"N-no, wait! I need to stay here!\""
    "Employee" "\"I don't give a flying rat's ass, I'm kicking you out o-\""
    show j 1 s shock at fdis
    j "\"W-Wait...\""
    "Jun calls out to the man holding me. He stops and looks back."
    show j 1 s pout at fdis
    j "\"I-I'm a competitor. Aren't I allowed by the rules to have someone with me for support?\""
    "Jun gets up from the floor, staring down the employee (which is quite a feat, considering the man is taller than even me)."
    "Employee" "\"Wha- that's usually reserved for family, and you have to declare them beforehand.\""
    show j 1 s wince at fdis
    j "\"I-I understand, but... my parents couldn't attend today due to... personal reasons. So I asked my friends to come with me. I'm sorry, could you please let him stay?\""
    "Employee" "\"Wha- This kid nearly threw me against the wall trying to bust his way in! You're asking me to let that slide?\""
    show j 1 s sigh at fdis
    j "\"I'm deeply sorry!\""
    "Jun bows, his face going so low that I'm afraid he'll just keep going and will hit the floor."
    mc 1 c shock "\"W-Wait, Jun, you don't have to apologize for my s-\""
    j "\"I'm so sorry, he was just worried about me. He didn't know what he was doing. I'll take full responsibility for his actions!\""
    mc 1 c avoid "\"Jun...\""
    "The ram looks from me towards Jun, who is still bowing. His expression seems to have softened a bit, but he still looks very angry."
    j "\"I'll get on my knees and beg if you want me to.\""
    mc 1 c shock "\"What?! No, Jun, that's going too far! I should be the one apologizi-\""
    "Employee" "\"There's no need.\""
    "?!"
    "The ram lets go of my hand, his eyes fixed on Jun."
    "Employee" "\"Lift your head, kid. If it's that important to you, I'll let your friend stay. I won't report this, otherwise you could end up being penalized due to him.\""
    show j 1 s gentle at fdis
    "Jun straightens himself back up, smiling at the employee."
    j "\"Thank you, sir!\""
    "He nods."
    "Employee" "\"Don't mention it. And you-\""
    "He turns to look at me, and that sharp, angry look flashes again in his eyes."
    "Employee" "\"Behave! And thank your lucky stars no one else was here to see this or you could have hurt your friend's chances!\""
    "He turns around and walks away, turning at the corridor disappearing from our sight."
    show j 1 s sigh at fdis
    j "\"Haaa...\""
    "Jun lets out a sigh of relief as he leans his back against the wall and slumps back down to the ground."
    mc 1 c wince "\"J-Jun, I'm so sorry, I didn't mean t-\""
    show j 1 s considerate at fdis
    j "\"I know...\""
    show j 1 s watch at fdis
    j "\"What are you doing here, [povFirstName]-san?\""
    mc 1 c avoid "\"I... I came to check up on you. I was worried...\""
    show j 1 s wry at fdis
    j "\"{size=-2}Thought so...{/size}\""
    "He hugs his knees, resting his chin on them and looking straight ahead."
    show j 1 s considerate at fdis
    j "\"Akutagawa-kun was... something else. After I saw his performance I... I just felt like it was impossible for me to beat him.\""
    "So it's like I thought... He really did watch that performance and it really did crush his spirit..."
    "I sit down next to Jun, as close as I can without actually touching him."
    "He seems to hold his breath for a second, unsure of what I'm doing."
    "Then, he relaxes."
    show j 1 s wry at fdis
    j "\"I'm sorry to have worried you...\""
    mc 1 c wry "\"It's okay. It's what friends are for. What about now? How do you feel...\""
    play music2 "music/BGM/I'm Sorry.ogg" fadein 5.0
    show j 1 s considerate at fdis
    j "\"I...\""
    "His body starts shaking again."
    j "\"I- I shouldn't have come here. This was a mistake, I should have just stayed out of the competitions.\""
    "I shift my body and kneel next to him, reaching out my hand to touch his face."
    show j 1 s shock at fdis
    "Jun freezes, looking at me like a deer in the headlights."
    show j 1 s shockb at fdis
    "I wipe away the tears that are beginning with my right hand, caressing his cheek as I do so."
    mc 1 c wry "\"That's not true, Jun. You've been practicing day and night for this. You're more than ready.\""
    show j 1 s blush2 at fdis
    j "\"No, I... I can't play...\""
    "His voice sounded so distant and lonely."
    "There has to be a way for me to console him."
    menu:
        "Maybe..."
        "Hug Jun.":
            "Before I even have time to properly think about it, I wrap my arms around Jun, pulling him close to me and placing his head on my chest."
            show j 1 s shockb at fdis
            j "\"W-what are you... [povFirstName]-san?!\""
            mc 1 c smile "\"It's okay.\""
            "I start stroking the back of his head, doing my best to sound warm and welcoming."
            show j 1 s cry at fdis
            "Soon enough, the dam bursts."
            "Jun clings tightly to my shirt and buries his head in my chest, sobbing."
            "I hold him there for what feels like many minutes, waiting for him to calm down."
            "Little by little, his sobs become quieter and less numerous."
            "When it seems that his sobbing has finally died down, I speak up."
            mc 1 c wry "\"Why do you think you can't play?\""
            show j 1 s avoid at fdis
            "Jun pulls away from me, looking down at the floor."
            "Once again, I wipe the tears from his face and smile at him."
            j "\"My hands... they feel cold.\""
            "I realize that his hands are still shaking."
            "I grab hold of one of his hands and give it a squeeze."
            mc 1 c happy "\"You mean this hand?\""
            show j 1 s blush2 at fdis
            "He pulls his hand away from me, looking down at the floor and nodding."
            show j 1 s wince at fdis
            j "\"They feel so... so cold. I can barely even move them. I just... I don't know what to do. I can't play like this.\""
            "His voice is so small and sad, I'm afraid he might start crying again at any second."
        "Don't.":
            "No, I don't think that'd work."
            "If anything, it could just make him even more uncomfortable."
            mc 1 c curious "\"What's wrong, Jun? Why can't you play?\""
            show j 1 s avoid at fdis
            j "\"... My hands...\""
            mc 1 c talk "\"Your hands?\""
            "I look down at his hands and realize that he's had them tucked inside his suit this whole time."
            j "\"They feel so cold. I can barely move them... I just...\""
            show j 1 s cry at fdis
            "He starts sobbing, his entire body shaking even more."
    "He's so nervous that his hands and maybe feet are feeling cold..."
    "I remember I used to feel the same when I had just started playing competitively."
    mc 1 c wry "\"Jun, give me your hand.\""
    "Even when stressed, he diligently does what I ask of him."
    "I grab his wrists and put both of his hands together, palm against palm."
    "Then, I wrap my hands around his."
    show j 1 s shockb at fdis
    j "\"Wha-\""
    "I gently pulls his hands towards me and exhale on them."
    j "\"[povFirstName]-san, what are you doing?!\""
    stop music2 fadeout 5.0
    "I look him in the eye, making sure to give him the gentlest, warmest smile I can."
    mc 1 c happy "\"I'm warming your hands up so you can play.\""
    "I know his hands aren't actually cold, but I'm just hoping I can somehow get him past whatever block has him like this."
    "I've managed to defuse his last panic attack, I won't be giving up with this one."
    play music3 "music/BGM/Little by Little I Walk - Piano.ogg" fadein 5.0
    mc 1 c considerate "\"Hey, Jun-kun, don't you think this is alright?\""
    "I speak in a soft voice."
    "My use of the honorific seems to have caught his attention."
    "I caress the back of his hands with my thumbs, trying to seem as encouraging as I can."
    mc 1 c happy "\"You've been working your hardest so far, wanting to show everyone your performance. A performance only you can make. Isn't that true?\""
    j "\"... A performance only I can make?\""
    "I nod, slowly."
    mc 1 c smile "\"I don't understand much about music myself, but shouldn't your music get your feelings across? Then why don't you, instead of worrying about getting a perfect performance, just try to show everyone how you feel?\""
    if jun_met == True:
        mc 1 c happy "\"I loved watching that first performance of yours. I know I've seen you perform once or twice after that, but that one really struck a chord with me.\""
        mc 1 c smile "\"I felt as if your song was calling out to me. It was warm and gentle and passionate. I'm sure you weren't trying to show people how good your skills were. You were just happy to play and wanted to pour your feelings into the piano.\""
        mc 1 c happy "\"So... Why can't you do that again?\""
        show j 1 s avoid at fdis
        j "\"I... If I did that, I wouldn't be able to win.\""
        "I shake my head in negative."
        mc 1 c happy "\"I don't believe that for even just a second. No one in this hall has managed to touch me the way your playing did, Jun. I believe in you. No matter what you do, I'm sure you'll be doing your best. So isn't this alright?\""
        mc 1 c smile "\"Can't you just play how you want to play? I don't know how these competitions are judged, but wouldn't it be better if you put out the best performance you can instead of just worrying about getting everything completely perfect?\""
    else:
        mc 1 c smile "\"I haven't watched many of your rehearsals, but every time I did, I always felt like you were holding back. As if you were so focused on getting the technique down to perfection that you didn't try letting your feelings seep into your music.\""
        mc 1 c happy "\"Why don't you just try to do that?\""
        show j 1 s avoid at fdis
        j "\"I... If I did that, I wouldn't be able to win.\""
        "I shake my head in negative."
        mc 1 c smile "\"I don't believe that for even a second. You said it yourself, didn't you? You've been playing these songs for years. So don't you think that if you just let your body take control and focus on pouring your heart out, it'll listen?\""
        mc 1 c happy "\"I think if you focused only on making your feelings be heard, your body would take care of the rest. Trust the senses that you've built for so long.\""
    "Jun stares at me. His fur is matted from his tears and his eyes are red, but he looks calm."
    j "\"I...\""
    "I hold his hands a little bit tighter, trying to encourage him anyway I can."
    "Jun nods."
    show j 1 s wry at fdis
    j "\"I'll try. I'll try to put my feelings in my music. Hopefully...\""
    stop music3 fadeout 5.0
    "He doesn't finish his sentence, but I already know he can do it."
    "As long as he can stay calm, there's no reason he wouldn't be able to."
    "Employee" "\"Jun Kobayashi?\""
    show j 1 s shockb at fdis
    "The worker from before peeks his head through the hallway, calling out Jun's name."
    "Jun pulls away from me and immediately gets up."
    j "\"Y-Yes?\""
    "Employee" "\"The interval is about to end. You have two minutes.\""
    show j 1 s happy at fdis
    j "\"Alright!\""
    "Jun nods, suddenly full of energy."
    "The ram smiles and walks away."
    show j 1 s smile at fdis
    j "\"Alright, [povFirstName]-san, I'm going now. Please watch over my performance.\""
    mc 1 c smile "\"Right. I have to hurry back to my seat, then. See you later.\""
    show j 1 s happy at fdis
    j "\"See you later.\""
    "I turn to walk away."
    j "\"Oh, and one more thing.\""
    mc 1 c curious "\"What is it?\""
    show j 1 s happyb at fdis
    j "\"... Thank you.\""
    "Caught by surprise, I don't react for a few seconds."
    "Then I nod and start running back to my seat."
    scene ConcertHall with fade
    "By the time I reach my seat, Jun is already halfway to the piano."
    s 1 c sigh "\"Where the hell were you?\""
    "Shoichi leans up to me, frowning."
    mc 1 c "\"I went to see Jun.\""
    s 1 c shock "\"What?! Why would you-\""
    "Spectator" "\"Shhh!\""
    "Someone shushes us from behind."
    "Shoichi glares at me and leans back into his own seat."
    "Jun sits in front of the piano, putting one of his hands on his knee and the other on his chest."
    "He seems to be holding something... a pendant? Even if I have good eyesight, I can barely make it out."
    "After what seems to be a full minute, he finally adjusts himself on his seat and places his hands on the keys."
    play music2 "music/BGM/Classical/Winter Wind.ogg"
    "The song starts very slow."
    "Jun plays the initial keys with only one hand."
    "The few whispers that could be heard in the audience seem to have died down the instant he started to play."
    "Even though his movement seems to be tense and robotic, the melody comes out easily and is pleasing to hear."
    "As he continues to play, Jun seems to relax."
    "He starts swaying back and forth to the rhythm of the melody, his tail begins to move slowly in the air."
    "He's definitely getting into it."
    "Looking to the side, I see Kei-kun tapping his feet to the sound of the music."
    "Saya looks for the first time like she's completely awake and not about to doze off."
    "Shoichi's lips are curved in a proud smile, as if he were a dad watching his son's first ball game."
    k 1 c smile "\"Here it comes...\""
    "Kei-kun murmurs just as the song seems to slow down to a halt."
    "Then..."
    "The song immediately picks up the pace, completely switching gears and becoming insanely fast."
    k 1 c shock "\"No way...\""
    "Kei-kun's reaction mirrors that of the entire audience. Surprise, perplexity, admiration. It is without a doubt that Jun is playing this song flawlessly, even a layman like me can tell."
    "As he continues to hammer out the keys with practiced skill, Jun's entire body moves along to the melody, creating a vivid performance that fills the halls with a rich, confident sound."
    if jun_met == True:
        "I feel it echoing deep inside my chest."
        "This is the same feeling as when I saw him playing for the first time."
    else:
        "I feel it echoing deep inside my chest."
        "A sound so nostalgic and sentimental, I can already feel it pulling at my heartstrings. I feel like I could cry..."
    "It takes every fiber of self-control I have to keep myself from getting up and walking towards the stage."
    "I want to get even closer..."
    "It's so moving that I feel like I could cry..."
    stop music2 fadeout 5.0
    scene ConcertLobby with fade
    play music "music/crowd01.ogg" fadein 5.0
    "With the performances already over for the day, all that is left is to wait for the results to be posted."
    show j 1 c pout at fdis, five with dissolve
    j "\"Nuuuh...\""
    "Jun has been pouting ever since he came out to the lobby, already changed into his regular clothes."
    show j 1 c pout at fdis, three with move
    show k 1 c at fdis, seven with moveiridis
    k "\"I already told you to cheer up. Your performance was amazing, stop sulking.\""
    show j 1 c pout at fdis, two
    show k 1 c at fdis, five
    with move
    show s 1 c sigh at fdis, eight with moveiridis
    s "\"Just telling him to cheer up isn't going to magically cheer him up, you know.\""
    "The three of us have been trying to up Jun's spirits since he re-joined us, unfortunately, results have been very mixed."
    "Meanwhile, Saya is waiting by the notice board to see the results when they finally get posted."
    j "\"I just feel like I bombed it...\""
    show k 1 c sigh at fdis
    k "\"You didn't bomb it. I'm telling you, your performance was amazing. There's no doubt in my mind that you'll snag second place.\""
    j "\"But I need first place. If I don't get it, there's no chance for me to go to Germany.\""
    show k 1 c at fdis
    k "\"I know that... I just can't tell you that you'll win because I'm not so sure.\""
    show k 1 c eyesc at fdis
    k "\"I think it'll be very close.\""
    show s 1 c at fdis
    s "\"I don't really understand much about music, but I thought Jun-kun's performance was better, didn't you?\""
    k "\"It depends. Kobayashi didn't go with the standard interpretation and that might not fly well with the judges. Regardless, I know that in technical terms, he was number one, but...\""
    show k 1 c avoid at fdis
    k "\"It basically comes down to whether or not the judges like his interpretation of the song. Even if Akutagawa's performance was higher in technical skill due to the duration of that piece, Kobayashi's was faster and more refined.\""
    show s 1 c sigh at fdis
    s "\"It comes down to the judge's personal tastes, then? That doesn't sound too good...\""
    show j 1 c wry at fdis
    j "\"It's not... That's why everyone tends to only play the standard interpretation. You won't charm any judges with your individuality, but you'll make sure none will dislike you so much that they fail you.\""
    mc 1 c wince "\"I-I didn't know that...\""
    "I suddenly feel very awkward for suggesting that he do that."
    "If Jun ends up failing because of this, I'll feel incredibly guilty for a long time..."
    mc 1 c wince "\"I'm sorry, Jun. I shouldn't have suggested you play like that...\""
    show k 1 c shock at fdis
    k "\"Wait, you're the one who suggested he do that?! Of all the reckless th-\""
    "Jun lifts a hand up in the air, cutting Kei-kun off mid-sentence."
    show j 1 c happy at fdis
    j "\"It's alright, [povFirstName]-san. That was good advice for me. If I had gotten fixated on playing the song perfectly instead of just playing how I wanted, I would have been crushed by my own anxiety.\""
    show j 1 c smile at fdis
    j "\"Playing it like that is the only reason I was able to play at all. If they fail me for that then so be it.\""
    "!"
    "W-What is this adorable creature?!"
    show k 1 c at fdis, four
    show s 1 c at fdis, six
    with move
    show aku 1 s smile at nine with moveiridis
    "Before my impulses can take me over and force me to hug the shit out of Jun, Shinji Akutagawa approaches us."
    aku "\"There you are, I've been looking for you for almost ten minutes!\""
    "The look on his face is both angry and scary."
    "Even I suddenly feel like taking a step back."
    show j 1 c blank at fdis
    "Jun, on the other hand, doesn't retreat."
    "He stares back at the lion with an intensity that I never thought he was capable of."
    j "\"It's a big lobby after all. How are you doing, Akutagawa-kun?\""
    aku "\"Honestly, of all the stupid things you could have done... Why didn't you go with the standard interpretation?! You basically threw in the towel the moment you did that!\""
    show j 1 c judge at fdis
    "It's very subtle, but I can notice Jun's body shifting a little bit when he hears that."
    "Maybe he's not as confident as he's trying to portray himself..."
    "Jun looks down at the floor for just a second."
    mc 1 c annoyed "\"I-\""
    aku "\"At least that's what I'd like to say.\""
    "Akutagawa sighs, lifting both of his hands to the air and shrugging."
    show j 1 c shock at fdis
    aku "\"I never thought you could do that well. I thought you'd be rusty after being out of the stages for seven years. Instead, you came back sharper than before.\""
    "Akutagawa's penetrating gaze softens considerably as he looks over the perplexed tiger."
    aku "\"Congratulations, Kobayashi-kun. No matter what the judges say, you're the victor today. But I won't lose next time.\""
    show aku 1 s smile at offscreenright with moveoridis
    show s 1 c at fdis, eight
    show k 1 c at fdis, five
    with move
    "Without even giving him time to answer, the lion turns and walks away, leaving Jun gaping in his spot."
    show k 1 c worried at fdis
    k "\"... Well, that was something.\""
    show s 1 c sigh at fdis
    s "\"That guy's weird, for sure.\""
    show j 1 c gentle at fdis
    j "\"Pfft. Hahahahaha!\""
    show k 1 c shock at fdis
    show s 1 c shock at fdis
    "Jun catches everyone by surprise when he suddenly hunches and starts laughing loudly."
    k "\"W-What the...\""
    j "\"S-Sorry, sorry.\""
    show j 1 c happy at fdis
    "He takes a few seconds to calm himself, wiping away a small tear from his left eye."
    show j 1 c smile at fdis
    show k 1 c at fdis
    show s 1 c at fdis
    "How can he laugh so carefree like that?"
    j "\"Akutagawa-kun really hasn't changed at all. He was always pretty blunt about stuff like that.\""
    show k 1 c sigh at fdis
    k "\"You're telling me he was always like that?\""
    "Jun nods."
    j "\"Akutagawa-kun is very demanding of himself. He's always quick to praise people when he thinks they deserve it and always admits his own shortcomings when he thinks they exist.\""
    j "\"He always admits defeat if he thinks that he's been defeated. Even if the judges give him first place, he'll still consider himself the loser. That's the kind of pianist he is.\""
    show s 1 c sigh at fdis
    s "\"Talk about a serious attitude.\""
    show s 1 c at fdis
    show k 1 c at fdis
    j "\"It's what you'd expect from someone aiming for the pros. He doesn't have time to make excuses for himself, he just takes in everything that he can and moves on.\""
    "..."
    show k 1 c calm at fdis
    k "\"Heh. I guess we could all stand to learn a few things from that guy, then.\""
    sa 1 c shock "\"Guuuuuuys!\""
    show j 1 c watch at fdis
    play sound "music/running.ogg"
    show k 1 c at fdis, four
    show s 1 c at fdis, six
    with move
    show sa 1 c sigh at fdis, eight with moveiridis
    "Saya comes running towards us, yelling so loudly that everyone in earshot turns to look at the source of this sudden noise."
    sa "\"T-The results!\""
    "!"
    show s 1 c shock at fdis
    show k 1 c worried at fdis
    "Shoichi and Keisuke" "\"How did it go?!\" \ \"What were they?!\""
    "Saya is hunching over, her hands on her knees, panting and gasping desperately for air."
    sa "\"F-\""
    mc 1 c shock "\"F?\""
    play music2 "music/BGM/Little by Little I Walk - Piano.ogg" fadein 5.0
    show sa 1 c laugh at fdis
    sa "\"F-First place!\""
    show j 1 c shockb at fdis
    j "\"{size=+4}Really?!{/size}\""
    play sound "music/tap.ogg"
    "Jun immediately latches onto her, grabbing her arms with both of his hands and looking her in the eye."
    "Saya swallows once and nods emphatically."
    sa "\"You got first place!\""
    "Jun stares at her, wide-eyed."
    "His hands start to shake and he stumbles backwards, collapsing on a nearby bench."
    show j 1 c tears at fdis
    show s 1 c wry at fdis
    show k 1 c wry at fdis
    "Big droplets start welling up in his eyes. He pulls out a pendant from his pocket and holds it tightly in his hands, touching it to his forehead."
    j "\"T-Thank God...\""
    "He then starts sobbing uncontrollably."
    stop music fadeout 2.5
    stop music2 fadeout 2.5
    $ date = None
    jump Day10
