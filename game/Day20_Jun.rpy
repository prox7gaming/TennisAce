label Day20_Jun:
    window hide
    scene June3 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    play music "music/crowd01.ogg" fadein 5.0
    scene Cafe
    show s 1 c at fdis, seven
    show sa 1 c at fdis, three
    with fade
    window show
    $ date = "day20"
    "It's the middle of the afternoon."
    "I've spent most of my day being distracted and spacing out."
    "There's been very little for me to focus my mind on recently so I've instead just been obsessing over recent events."
    "Let's see... what is there that I can say about today..."
    "It's hot. The first signs of summer rearing its ugly head are finally showing."
    "It's 24ºC today which is already six degrees higher than the average temperature the last month."
    "Thankfully, this cafe has some pretty nice AC for me to try to relax in."
    "Even if coming here wasn't really my own choice..."
    "Oh, and I also have two very unamused childhood friends staring pointedly at me while I space out and forget about their existence."
    "So... you know. More of the same old."
    "I'm surprised these people still put up with me."
    mc 1 c considerate "\"I'm sorry... where were we?\""
    s "\"Waiting for you to start talking for the past five minutes.\""
    sa "\"Being very bored?\""
    mc 1 c considerate "\"S-sorry. I kinda zoned out for a little bit.\""
    s "\"I can tell. You seem pretty out of it but you {i}were{/i} the one who called us here.\""
    mc 1 c worried "\"Right. Yeah, I know.\""
    "Just then I notice the two of them sipping on coffee and tea, raising an eyebrow at it."
    mc 1 c confused "\"Wait. Did you guys bring drinks with you to the café? That's kinda rude.\""
    sa 1 c bored "\"No. We ordered drinks while you were too busy ignoring us.\""
    mc 1 c shock "\"H-huh?! When was this?\""
    s 1 c sigh "\"We just said so. While you were spacing out like you always do.\""
    mc 1 c wince "\"I-it can't have been that bad that I didn't even notice you guys talking to a waiter.\""
    sa 1 c sigh "\"You're hopeless...\""
    play sound "music/stab.ogg"
    mc 1 c wince "\"T-that's kinda harsh.\"" with hpunch
    show s 1 c at fdis
    show sa 1 c at fdis
    s "\"Come on, just tell us what it is you wanted already.\""
    mc 1 c considerate "\"W-wanted? Who says I didn't just want to get together and have fun?\""
    sa "\"First of all, if you did you wouldn't have invited just the two of us. Also, you wouldn't be ignoring us.\""
    s 1 c think "\"While I agree with your first point, I think you're wrong on the second one, Saya-chan. He just has a tendency to space out regardless of what he's doing.\""
    sa 1 c think "\"Hmm... I guess that's true. [povFirstName]-kun just sucks at paying attention.\""
    "Can you guys not insult me when I'm sitting right here?!" with hpunch
    mc 1 c sigh3 "\"Yeah yeah, please continue to tell me all the reasons why I'm terrible.\""
    show s 1 c at fdis
    s "\"No one said you're terrible. Stop being so dramatic.\""
    sa "\"Hmm... I don't know about that.\""
    mc 1 c sigh "\"That's it. Maybe I should just leave you two and deal with my problems on my own.\""
    s 1 c sigh "\"I already told you to stop being so dramatic. If there's something going on just tell us already instead of dancing around the issue.\""
    mc 1 c sigh "\"Fine, fine. Get off my case already.\""
    show s 1 c at fdis
    sa 1 c "\"Actually, do tell me one other thing first. Why haven't you been answering your messages lately while having Aki-kun message us for you?\""
    mc 1 c considerate "\"Well... it kinda actually has to do with what I wanted to talk to you guys about. I just... kinda sorta maybe... broke my phone.\""
    s 1 c sigh "\"Kinda sorta maybe?\""
    mc 1 c worried "\"Alright, I definitely broke my phone. Happy?\""
    s 1 c "\"Why would I be happy over that?\""
    mc 1 c sigh2 "\"Anyway, so not the point. I just... I wanted to ask you guys for advice?\""
    show sa 1 c shock at fdis
    show s 1 c smile at fdis
    sa "\"{i}You{/i} want advice? What has the world come to?!\""
    s "\"Oh man, this is gonna be rich.\""
    "... Why do you two feel the need to be so... {i}you{/i} at times like these?"
    mc 1 c sigh "\"Yes, I am capable of accepting that I need help and advice sometimes. There's nothing funny about that.\""
    s 1 c "\"With how hard-headed and uptight you tend to be? Doesn't really happen often.\""
    sa 1 c smile "\"Yeah. And you also have a tendency to blow up whenever anyone gives you the slightest bit of criticism.\""
    mc 1 c sigh "\"What?! I absolutely don't do that. You're just being ridiculous.\""
    sa 1 c "\"Further proving my point.\""
    mc 1 c wince "\"J-just because I disagree with you doesn't make me disagreeable. That's not how it works.\""
    s 1 c think "\"And further proving the p-\""
    mc 1 c sigh2 "\"Alright alright, just shut up already!\""
    s 1 c smile "\"Whatever you say.\""
    "Ugh... Why do I need to have friends who derive so much pleasure out of annoying the crap out of me?"
    "Although I guess I tend to do the same pretty often too..."
    "Could it be... am I out of touch?"
    "... No, of course not. It's them who are wrong!"
    "... I need help..."
    mc 1 c sigh3 "\"Anyway, circling back to try and talk about the thing I actually need help with...\""
    s 1 c "\"Yeah, sure, what's up?\""
    mc 1 c worried "\"I... Erm... You guys might not be the right people to ask but... lately I think I've been feeling... somewhat different about... about a specific person mostly and...\""
    show sa 1 c shock at fdis
    s 1 c shock "\"W-whoa. I-it's that kind of talk?\""
    sa 1 c avoidb "\"C-come on, Shoichi, don't act so surprised. We both knew this day would come eventually.\""
    s 1 c wince "\"Y-yeah, I guess you're right.\""
    "... Huh?"
    sa "\"It's... you just have to know that it's natural for there to be... changes sometimes...\""
    "..... What?"
    s "\"Y-you see, [povFirstName]... The thing is... W-when a man and a woman really love each other-\""
    stop music
    show sa 1 c shock at fdis
    show s 1 c shock at fdis
    mc 1 c angry "\"{size=+2}Not that kind of talk you morons!{/size}\"" with hpunch
    sa "\"I-it's not?\""
    "I am not a child!"
    mc 1 c sigh2 "\"Are you two mocking me? You've got to be mocking me...\""
    s 1 c wince "\"U-uhm... s-sure... let's go with that...\""
    "... I hate you two so fucking much right now."
    "Waiter" "\"Excuse me, sir. Can you please not scream in the middle of the restaurant?\""
    "A nearby waiter immediately walks up to our table to censure me for losing my cool, making my face immediately go very red."
    show s 1 c laugh at fdis
    show sa 1 c laugh at fdis
    mc 1 c flustered "\"O-oh, r-right. I'm sorry. It won't happen again.\""
    play music "music/crowd01.ogg" fadein 5.0
    play music2 "music/BGM/Autumn Day.ogg" fadein 5.0
    s "\"Oh wow, you were told off pretty quick.\""
    mc 1 c sigh2 "\"Just shut up...\""
    sa "\"[povFirstName]-kun, you just can't help but draw attention to yourself all the time huh?\""
    "Must... not... bitch slap..."
    mc 1 c sigh "\"Can I just talk about the thing I wanted to talk about or should I walk away and give up on it?\""
    show s 1 c smile at fdis
    sa 1 c smile "\"Right right. Sorry. We're all ears.\""
    "... I will not comment on how ironic it is to hear that from a rabbit."
    "{i}I'd{/i} probably get bitch slapped if I did."
    mc 1 c worried "\"Well... It's just... I'm kinda confused about my feelings for a... certain person...\""
    s 1 c "\"Confused?\""
    mc 1 c wince "\"Y-yeah... Like... I'm not sure how I feel about them. Like... I obviously like them a lot but... do I like them as a friend or...\""
    show sa 1 c at fdis
    s 1 c sigh "\"... So you think you fell for someone?\""
    "For some reason, Shoichi sounds very annoyed when he asks me this question."
    mc 1 c wince "\"I... I don't know? M-maybe I did but I don't wanna do anything until I'm sure and... W-why do you look so upset?\""
    s "\"I'm not upset. I'm just... worried where this is going to go. You don't exactly have the best track record when it comes to dating.\""
    mc 1 c worried "\"... Right. Which is why I was so hesitant to accept the confession.\""
    sa 1 c shock "\"Whoa whoa whoa whoa whoa. Back up a bit. You got confessed to?!\""
    mc 1 c wince "\"R-right. Maybe I should have started the conversation with that.\""
    s "\"There's no reason for you to be so surprised. It's not like this isn't a common occurrence. And again, considering his track record, my guess is he'll be single again in a month and some girl will be broken-hearted.\""
    sa 1 c bored "\"Ugh. I hate that you're right. Makes it really hard to ship him with someone when he's like this.\""
    "Please don't ship me with other people. I'm a real person, not some kind of fictional character you can \"ship\" with others..."
    mc 1 c considerate "\"W-well... the thing is... I... kinda didn't answer yet.\""
    show sa 1 c shock at fdis
    show s 1 c at fdis
    sa "\"Seriously?!\""
    s "\"That's kind of a new development for you. Although if you still haven't worked up the nerve to say \"no\" then we still have a way to go.\""
    mc 1 c wince "\"I didn't want to say no! I just... I don't know what it is that I wanted to say.\""
    sa 1 c "\"What did the girl say to you?\""
    mc 1 c worried "\"I-I can't say... You guys might figure out who it is if I do.\""
    s 1 c sigh "\"I sincerely hope this isn't my sister we're talking about otherwise you and I are going to have words.\""
    "Shoichi cracks his knuckles in what I'm sure is not at all supposed to be a threatening gesture."
    mc 1 c considerate "\"Of course it's not her. Don't be ridiculous.\""
    sa 1 c think "\"Well... What did you say back to the confession? Did you tell her you needed time to answer?\""
    mc 1 c wince "\"I... I didn't say anything.\""
    sa 1 c shock "\"N-nothing? As in... you just stayed silent?!\""
    "..."
    "Unfortunately, this is one of those situations where silence speaks for itself."
    "... Unlike two days ago when Jun confessed to me..."
    s 1 c sigh "\"Dude, you suck. You really really {i}really{/i} suck.\""
    mc 1 c sigh "\"Thanks. Not like I haven't been feeling bad enough already here.\""
    sa 1 c sigh "\"[povFirstName]-kun, I'm not sure what kind of advice you expect us to give you if you won't even properly tell us what happened.\""
    mc 1 c wince "\"B-but if I do you guys will know who the person I'm talking about is.\""
    s "\"We'll also know who the girl is just by noticing who around you seems to be sad and heartbroken on Monday.\""
    sa 1 c think "\"Not if the girl's from another class...\""
    s 1 c "\"If she were then he wouldn't worry about not telling us who she is because then we wouldn't know her anyway.\""
    sa 1 c talk "\"That's a good point actually.\""
    "... Heh."
    "I don't know if I should be amused that they're assuming it's a girl."
    "I've even been careful enough to only use gender neutral terms to not give away the answer but they don't seem to have caught on."
    "At least my ability to derive amusement from awkward situations seems to be intact."
    "... Yay me."
    mc 1 c sigh3 "\"Are you two going to just keep insisting until I tell you who it is?\""
    sa 1 c "\"What? Why would we? I think you're overestimating how much we're supposed to care about this.\""
    s 1 c considerate "\"Saya-chan, that's a bit...\""
    mc 1 c sigh "\"... Why do I suddenly feel so insulted?\""
    sa 1 c sigh "\"What? It's true. You do this kind of thing all the time.\""
    s 1 c wince "\"That's... true. You seem to always have some kind of relationship drama around you because you just can't say no.\""
    mc 1 c sigh "\"I just told you I didn't agree to date them this time!\""
    s 1 c sigh "\"You also didn't say no either. You just said nothing. That's not any better. An answer is still better than no answer at all.\""
    mc 1 c wince "\"Wha- That's- I mean- I- What do you want from me?\""
    sa 1 c bored "\"You growing a pair would be a good start.\""
    s 1 c considerate "\"Oof. Even I felt that one.\""
    "... I wanna go home."
    mc 1 c sigh3 "You know, I came here to ask for help and advice from my friends, not to get insulted.\""
    sa "\"You want help and advice? Then actually tell us what the situation we're supposed to be giving you advice on is. I can't suggest anything if I have no idea what's going on.\""
    s 1 c sigh "\"That is very true.\""
    "Ugh... If you two are going to just calmly refute all my points with actual logic then I have no way to discuss this with you."
    "... Yes, I am aware I'm being unreasonable. I hate it too."
    mc 1 c worried "\"... Just... p-promise me you won't breathe a word of this to anyone?\""
    s "\"I thought that much was already a given.\""
    mc 1 c sigh2 "\"Not you. I'm talking about Miss Blabbermouth here.\""
    sa 1 c shock "\"Wha- Hey, I'm not a blabbermouth!\""
    s 1 c think "\"Respectfully disagree.\""
    play sound "music/punch.ogg"
    show s 1 c wince at fdis, shake1
    s "\"Ow!\""
    "Shoichi suddenly nearly jumps out of his seat but because they're sitting opposite of me on the table, I can't tell if something happened."
    mc 1 c shock "\"Are you okay?\""
    s "\"She just stomped on my foot!\""
    sa 1 c pout2 "\"I did no such thing.\""
    mc 1 c sigh3 "\"Saya-chan, please stop assaulting us just because we called you out on the things you do.\""
    sa "\"I don't know what you're talking about it.\""
    s 1 c sigh "\"So you're just going to act dumb now?\""
    mc 1 c considerate "\"You can't act as what you already a-{nw}"
    play sound "music/punch.ogg"
    show mc 1 c dismay at fdis, offscreenleft
    extend " Ow ow ow, for the love of God why?!\""
    "Pain jolts up my leg as I feel my shin being kicked hard under the booth."
    s 1 c sigh "\"[povFirstName], please just continue with your story before she tears our limbs off.\""
    mc 1 c wince "\"P-probably for the best...\""
    show sa 1 c at fdis
    show s 1 c at fdis
    "I take a few deep breaths, trying to summon the courage to talk openly about this."
    "Even if its these two I'm talking to, I still feel... nervous with what I'm about to say."
    "I have no idea how they'll react if I tell them I'm confused over my feelings for a guy..."
    "Not to mention that I don't want them treating Jun any different because they know he has a crush on me."
    "This whole situation is just... unpleasant."
    mc 1 c worried "\"... During the last day of the festival, Jun... confessed his feelings for me.\""
    stop music2 fadeout 2.5
    show sa 1 c shock at fdis
    show s 1 c blank at fdis
    play sound "music/tableknock.ogg"
    sa "\"{size=+4}Whaaaaaat?!{/size}\""
    mc 1 c wince "\"Shhhhhhhhhhh. Saya-chan, you're being too loud!\""
    "Saya jumped out of her seat, knocking both of her hands down on the table and nearly screaming out the top of her lungs."
    "With anyone else I would call this an overreaction with the intent to cause drama."
    "With Saya I call this a regular Monday."
    "... Or Saturday in this case. Anyway, semantics."
    sa 1 c bored "\"R-right. Sorry, I kinda lost it for a second.\""
    "Sheesh, I can see the waiter shooting us dirty looks..."
    sa 1 c complain "\"B...but... Jun-kun confessed to you?! That's... I mean... Are you sure? Maybe you misunderstood!\""
    mc 1 c sigh3 "\"He literally told me he liked me \"romantically as a man\" so I'm not sure what kind of other conclusion I could have drawn from that.\""
    sa "\"I-I mean, y-yeah but... that's just... I mean...\""
    mc 1 c considerate "\"Saya-chan, you're not making any sense.\""
    sa 1 c sigh "\"Maybe it's the world that's not making sense.\""
    "No, I'm pretty sure it's just you."
    sa 1 c bored "\"Still, I... wow, I just...\""
    sa 1 c shock "\"... Wait. Didn't you say you were confused about it because you thought you might like him back?!\""
    "Ah, and here's where realization dawns."
    show sa 1 c avoidb at fdis
    "I think the look on my face must have been way too transparent about my current feelings because next thing I know Saya-chan is avoiding my eyes and looking very apologetic."
    sa "\"I... Sorry that... that came out wrong.\""
    mc 1 c considerate "\"It's... alright. I can't feel any worse or more confused than I do right now.\""
    "That's most definitely a lie..."
    sa 1 c bored "\"So... uhm... I don't even know what to say here.\""
    mc 1 c considerate "\"Imagine how I feel.\""
    sa "\"Yeah, that's true. That's... wow. I just never pictured you being into men.\""
    mc 1 c worried "\"... You probably find it disgusting don't you?\""
    sa 1 c shock "\"W-what? No no no no no. Absolutely not!\""
    mc 1 c shock "\"N-no?\""
    sa 1 c bored "\"[povFirstName]-kun, I might not say this often but you're one of my best friends and I love you. Nothing's going to change that. Especially something silly like this.\""
    sa 1 c considerate "\"I mean... I guess it might have been a big deal to some people ten years ago or something but the younger generations don't really think anything of it.\""
    sa 1 c wry "\"... For the most part at least.\""
    "Huh... \"for the most part\". That doesn't sound ominous at all."
    sa 1 c happy "\"But hey, if that's the case, you don't have to worry about it changing anything about how I think of you okay? And I'm sure Shoichi is of the same mind on this, right, Shoichi-kun?\""
    play sound "music/tap.ogg"
    show s 1 c shock at fdis
    "Saya gives Shoichi a few enthusiastic taps on the back that nearly push him down against the table from how strong they were."
    "She's apparently using enthusiasm to try to mask her awkwardness at the subject, bless her heart."
    s "\"W-what? I-I'm sorry, what were you saying?\""
    sa 1 c shock "\"Wha-"
    show sa 1 c pout at fdis
    extend "You didn't pay attention to what I said?!\""
    s 1 c wince "\"S-sorry. I guess I kinda zoned out for a bit.\""
    mc 1 c worried "\"... Because of what I said?\""
    s 1 c considerate "\"I mean... I do have to admit it was... a little bit of a shock...\""
    sa 1 c bored "\"Shoichi-kun...\""
    "For some reason, Saya looks sadly at Shoichi, putting a hand on his shoulder and rubbing him gently."
    "The whole thing looks a bit weird to me."
    "Why does it look like he's getting comforted instead of me?"
    mc 1 c considerate "\"I-I mean, who knows. I just said that I'm confused over it, not that I definitely have feelings for him. I-It might turn out that I don't and this whole conversation was pointless, right? Hahaha...\""
    s 1 c worried "\"You... You should probably take some time to figure your feelings out for yourself...\""
    mc 1 c wry "\"That's what I'm trying to do. That's why I wanted to talk to you guys about it. To see if I can figure anything out by getting it out in the open. {size=-4}Although I didn't plan to give this many details.{/size}\""
    "Considering the fact that Aki already thought Jun and I were dating, I'm sure he'd be understanding of the whole thing if I tried to talk to him but..."
    play sound "music/disappointment.ogg"
    "I'd feel very pathetic having to get relationship advice from a 12-year old..."
    sa 1 c considerate "\"Well, if you like guys then it might explain why none of your previous relationships worked.\""
    "The fact that she can say something like that so nonchalantly scares me just a little bit."
    mc 1 c fsmile "\"That's... I guess...\""
    "Ugh... why does the mood feel so weird here right now?"
    "Saya is trying hard to act cheerful like nothing is happening at all while Shoichi is awkwardly twiddling his thumbs and looking out the window."
    "Even if they say nothing changes, it's kinda hard to believe it when their reactions are this."
    "Or... maybe I was expecting too much. Even if their opinions of me don't change, it would be naive of me to expect the status quo to remain exactly the same."
    "Because even if it's not a big deal to them, now they'll awkwardly go over the top to show me that it's not a big deal to try to comfort me."
    "It's hard to not make a big deal out of things when you're trying to show people that it's not a big deal."
    "That's a weird dichotomy..."
    s "\"So... erm... you think you might... have feelings for him too?\""
    mc 1 c worried "\"I... I don't know? Maybe? I... part of me was kinda happy when he said it but...\""
    mc 1 c wince "\"I remember how it went the last times I was in a relationship. And I remember you guys calling me out on how I hurt those girls by accepting when I didn't feel the same.\""
    mc 1 c worried "\"I was so scared of accepting without being sure of myself that I wound up freezing... and he took it badly.\""
    mc 1 c sigh3 "\"I tried swinging by his house first thing in the morning yesterday but no one was home\""
    mc 1 c worried "\"Then I tried going again this morning. His mom answered the door and said he was out of the house and wouldn't be back until tomorrow but didn't tell me where he was.\""
    s "\"Sounds like you gave this a lot of thought.\""
    mc 1 c considerate "\"I guess? I've been kinda obsessing over it for a while now.\""
    sa 1 c argue "\"Ugh. I've always knew you were indecisive but I never thought you'd actually freeze when trying to respond to a confession of all things.\""
    mc 1 c considerate "\"I know. I've been... really angry with myself over it. I kinda smashed my phone without even thinking of it because of that...\""
    s 1 c sigh "\"So that's how it broke, huh?\""
    mc 1 c wince "\"Y-yeah.\""
    sa 1 c confused "\"I have to admit I'm a bit curious though. Where would Jun-kun go if he's staying out of his house for two days? I thought he said he didn't have any other family in town at some point.\""
    mc 1 c worried "\"I was thinking the same. That... maybe the timing of it was a bit too convenient.\""
    sa 1 c bored "\"You think his mom knows about it and was covering for him?\""
    mc 1 c considerate "\"I don't know. Yui-san doesn't really strike me as someone who would lie like that but... then again, I've only met her a couple of times.\""
    s 1 c worried "\"Well... if she were trying to keep you from seeing him then she wouldn't have given you a day when he'd be back would she?\""
    mc 1 c wince "\"I... I guess that's actually a good point.\""
    s 1 c sigh "\"You guess?\""
    "My mind isn't working at normal speeds okay, you don't have to look at me with such disappointed eyes!"
    sa 1 c "\"Yeah, that's true. She wouldn't have bothered doing that if that were the case... Do you plan to drop by again tomorrow?\""
    mc 1 c wince "\"Y-yeah. I can't stand to leave things like this. Whether I have feelings for Jun or not, it won't change the fact that I don't want to hurt him.\""
    mc 1 c sigh3 "\"But... man, talking about potentially having feelings for a guy is... really weird.\""
    s 1 c considerate "\"You'll get used it.\""
    mc 1 c sigh "\"How would you know?\""
    show s 1 c sad at fdis
    show sa 1 c shock at fdis
    "The words roll out of my mouth before I even realize it, with much more venom than I'd ever want to use with a friend."
    "Shoichi flashes me a very pitiful look and my mind is left scrambling trying to come up with an apology."
    "To say that my brain isn't working normally would be an understatement at this point."
    mc 1 c shock "\"S-sorry, I-I didn't mean for it to come out like that!\""
    show sa 1 c bored at fdis
    s 1 c considerate "\"It's alright. I can understand. You have a lot on your mind right now so it's normal to lash out sometimes.\""
    s 1 c wry "\"But the reality is that, as with most things in life, you eventually get used to it. You don't need to have personal experience with it to know. That's just how things go.\""
    "God, please don't give me sagely advice with that look on your face. It makes my chest hurt..."
    mc 1 c worried "\"I guess...\""
    sa 1 c "\"Do you have any idea what you're going to say to Jun-kun tomorrow?\""
    "Saya quickly cuts back into conversation, whether on purpose to spare us the awkwardness or just because she'd been waiting to speak, I don't know."
    "I'm still thankful regardless because I feel so awkward every time we get silent again."
    mc 1 c wince "\"I... don't.\""
    s 1 c sigh "\"Then maybe you shouldn't go. If you're just going to walk up to him and stare at him without saying anything, it'd be better if you weren't even there at all.\""
    mc 1 c worried "\"I-I...\""
    sa 1 c argue "\"That's kind of a harsh way to put it but... I agree. If you're going to say something that will end up hurting him then it's better if you don't.\""
    mc 1 c worried "\"But isn't it better to have any kind of answer over none at all? Even if it's a vague one...\""
    s 1 c worried "\"I... I disagree with that. I think unless you're going there to give him a concrete yes or no, you really shouldn't go. If you're just going to say \"maybe\" and give him hope that might never come to pass...\""
    s 1 c considerate "\"It's easier if you tell yourself you never had a chance. If you go over there to tell him it could have been but wasn't, no matter what the reason is... that's going to hurt.\""
    sa 1 c bored "\"...\""
    "Goddamnit..."
    "I don't know what to do..."
    "I just..."
    mc 1 c avoid "\"I just... wanna see him...\""
    s 1 c worried "\"... Yeah.\""
    "Man, this is awkward."
    "To have all three of us in a bad, awkward mood at the same time is really rare."
    "The two of them look like they have things to say but can't bring themselves to say it."
    "And I already feel like I'm under a microscope as it is."
    "My thoughts are all tangled up in knots and I don't even know what it is that I'm thinking or feeling."
    "God, I really hate this..."
    sa 1 c considerate "\"Look, [povFirstName]-kun... we obviously can't tell you what to do. At the end of the day it's your decision, but... Just try to keep Jun-kun's feelings in mind, okay? Don't do something that would hurt him.\""
    mc 1 c worried "\"That's the last thing I want to do. I just... need time to figure myself out.\""
    sa "\"Man, you're painfully slow at making decisions with everything aren't you?\""
    mc 1 c sigh "\"Don't remind me.\""
    s 1 c "\"Just... try to do right by him, okay? He's already been through a lot so he doesn't deserve any more undue hardship.\""
    show sa 1 c at fdis
    mc 1 c confused "\"Been through a lot? What do you mean?\""
    s 1 c sigh "\"It's a figure of expression.\""
    mc 1 c sigh "\"No it's not. Do you know something you're not telling? Does it have to do with his health?\""
    s "\"I already told you I didn't mean anything by it.\""
    sa 1 c "\"Also, try not to coddle him too much. You have a habit of babying him and while he might not be the most mature person in the world, he's not a child either.\""
    s 1 c "\"That's a fair point too.\""
    mc 1 c sigh "\"What is this, \"Criticize [povFirstName] 101\"?\""
    sa 1 c smile "\"No but I'd pay to take that class.\""
    mc 1 c sigh "\"I hate you.\""
    sa 1 c laugh "\"No you don't. You loooooove me.\""
    mc 1 c sigh "\"... No comments.\""
    sa 1 c pout "\"Hey!\""
    play music2 "music/BGM/Dog Days.ogg" fadein 5.0
    "Thank God Saya is here here."
    "She's the only person actually making an effort to try to break through the awkward atmosphere."
    "If it were just me and Shoichi we'd be stuck making faces at each other without saying anything, I'm sure of it."
    mc 1 c "\"By the way, I have a question.\""
    show sa 1 c at fdis
    s "\"Shoot.\""
    mc 1 c sigh "\"How come you guys were so shocked at the {i}possibility{/i} that I might turn out to like Jun but no one acted all that surprised about Jun having feelings for me? Other than the initial outburst that is...\""
    sa 1 c considerate "\"Well... I was more shocked that he confessed to you than that he had feelings for you.\""
    s 1 c "\"Oh? Does that mean you figured it out he had a crush on [povFirstName] already?\""
    sa 1 c think "\"Well, I'm pretty good at picking up on people's body language and whatnot so I'd kinda suspected it for a while now.\""
    mc 1 c sigh "\"Jeez. Thanks for the heads-up.\""
    sa 1 c sigh "\"It's not my business to tell you. Besides, I never thought he said anything because... well, we all thought you were straight.\""
    mc 1 c wince "\"I still might be. I'm just unsure.\""
    sa 1 c talk "\"You're at least willing to entertain the possibility. A lot of people wouldn't be willing to do that much introspection.\""
    mc 1 c sigh "\"I don't know if that's any kind of merit on my part. Also, the idea that you can figure out who has a crush on whom is kinda terrifying.\""
    sa 1 c considerate "\"Sorry. I just tend to be really good at reading people.{nw}"
    show sa 1 c think at fdis
    extend " I mean, how do you think Kaito-kun and I ended up dating? It certainly wasn't because he had the courage to confess to me.\""
    "Ah, now that I think about it, that's true. She was able to figure out he had feelings for her and took the initiative."
    "She's always been very good at pursuing the things she wants. I have to give her props for that."
    s 1 c sigh "\"Must be nice knowing how the other person is going to answer before ever saying anything...\""
    sa 1 c bored "\"W-well, I can never be 100\% sure. I just tend to have really strong suspicions that almost always turn out to be correct.\""
    s "\"That's pretty much the same thing.\""
    show sa 1 c bored at fdis, shake1
    play sound "music/stab.ogg"
    sa "\"Guh...\""
    mc 1 c talk "\"What, do you have someone you wanted to confess to but was afraid to do it?\""
    s 1 c wince "\"H-huh?\""
    mc 1 c confused "\"I mean, why else would you say what you just said?\""
    s 1 c sigh "\"What, are we all now going to catch up about each other's love lives?\""
    sa 1 c considerate "\"That's a bit-{nw}\""
    mc 1 c considerate "\"Why not. I already told you guys about mine anyway. If I can tell you {i}this{/i} then I don't think you guys need to hold secrets from me either, right?\""
    s 1 c avoid "\"... That's not how this works.\""
    mc 1 c talk "\"But-{nw}\""
    show sa 1 c laugh at fdis, jumping
    sa "\"Ahaha, w-well, if we're gonna make revelations then I guess I can tell you. I had a date to the bonfire dance during the festival!\""
    mc 1 c shock "\"Wait, what?!\""
    sa 1 c considerate "\"Y-yeah. One of our underclassmen asked me out. We'd been talking for a bit for the past week or so but he kinda blew me off after the dance.\""
    s 1 c "\"Really? I saw you two dancing together but I didn't know he blew you off after. Do you need me to have words with him?\""
    sa "\"W-what? No no, of course not.\""
    mc 1 c confused "\"Why would {i}you{/i} talk to the guy about it?\""
    s 1 c sigh "\"He's a member of the volleyball team. One of our freshmen.\""
    mc 1 c shock "\"Whoa, seriously?\""
    show s 1 c at fdis
    sa 1 c think "\"Yeah. He said he'd seen me a few times since we share a building and that he thought I was really pretty and whatnot and that he had a crush on me. It was really cute.\""
    sa 1 c sigh "\"Then he blew me off saying that I spent far too much time with my friends, didn't pay him much attention and emasculated him when we were together. Can you believe it?\""
    show s 1 c worried at fdis
    mc 1 c considerate "\"...\""
    s "\"...\""
    sa 1 c bored "\"Y-you guys are really silent because you can hardly believe it... right?\""
    mc 1 c considerate "\"Saya-chan... I'm sorry...\""
    sa 1 c pout "\"I'm not emasculating!\""
    s 1 c considerate "\"W-we didn't say you were.\""
    sa "\"You also didn't say I wasn't.\""
    s 1 c wince "\"W-well...\""
    sa "\"Well?\""
    s "\"...\""
    mc 1 c considerate "\"...\""
    sa "\"...\""
    "..."
    play sound "music/tableknock.ogg"
    show s 1 c wince at fdis, shake1
    sa 1 c angry "\"{size=+2}Say something!{/size}\""
    "She slams her fists on the table. I can almost picture the word \"Objection\" popping up above her head in big red letters with an exclamation mark."
    s "\"A-at least you still have your health?\""
    sa 1 c happy "\"... Shoichi-kun?\""
    s "\"Y-yeah?\""
    sa 1 c doom2 "\"Do you want to die?\""
    s 1 c shock "\"I-I-I-I'm kidding. Y-you're as precious as a flower. V-very pretty and not at all scary!\""
    "... The fact that she's threatening him into calling her non-threatening is an irony that I wish I could point out."
    "Alas, {i}I{/i} don't want to be threatened."
    "Saya, you are fricking terrifying sometimes. This woman is definitely the devil."
    show s 1 c sigh at fdis
    sa 1 c laugh "\"Awww, thank you so much. That's so nice of you to notice my charms, hahaha.\""
    s "\"I... I feared for my life.\""
    mc 1 c considerate "\"At least you still have your health.\""
    s "\"Very funny.\""
    stop music fadeout 2.5
    show s 1 c at fdis
    show sa 1 c talk at fdis
    scene Street1E with fade
    show hours with dissolve
    $ renpy.pause (1.0)
    hide hours with dissolve
    "Heading home, my head is swimming with thoughts once again."
    "It took us a while to get past the initial awkwardness of the conversation but eventually we were able to chat and joke around almost like normal."
    "I say almost because Shoichi still seemed a bit out of it, even if he insisted it was nothing."
    "I guess... it might just be a shock to him considering how close we've always been."
    "I just really hope this doesn't affect our friendship going forward."
    "... But that's not really what's been bothering me."
    "Thanks to those two, I was able to keep myself distracted for a while and I'm definitely thankful about that, but my head is swimming in uncertainty once again now that I'm by myself."
    play sound "music/disappointment.ogg"
    "Once I'm left to my own devices, I can't help but obsess, huh?"
    "I know they said it's not a good idea to go see Jun when I haven't made up my mind but..."
    "I'm sorry, Saya-chan and Shoichi, I just can't bring myself to leave things as they are."
    $ date = None
    stop music2 fadeout 2.5
    jump Day21_Jun
