label Day14_Keisuke:
    window hide
    scene May22 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    play music2 "music/BGM/Dazzling Sunlight.ogg" fadein 5.0
    scene SCorridor with fade
    window show
    $ date = "day14"
    "I sit around on the second floor hallway, waiting for a certain someone to finally come out of his class."
    "God, why does he spend so much time in there after class has already ended for the day?"
    play sound "music/slidingdoor.ogg"
    "Once I hear the sound of the door opening, my attention is dragged away from my phone and towards it."
    show k 1 u shock at fdis, five with dissolve
    "Keisuke stands in front of the door, looking at me with confusion."
    k "\"[povFirstName]-san? What are you doing here?\""
    mc 1 u smile "\"I go to school here, remember?\""
    show k 1 u sigh at fdis
    k "\"Not here in school. Here on my floor.\""
    mc 1 u happy "\"Damn, I know you're rich but I wasn't aware you had bought the whole floor.\""
    k "\"Haha, very funny.\""
    show k 1 u at fdis
    mc 1 u smile "\"But to properly answer your question, I came by to see you.\""
    k "\"Evidently. As far as I know, you don't know anyone else in this floor.\""
    mc 1 u smile "\"Then why did you ask me in the first place?\""
    show k 1 u sigh at fdis
    k "\"That's not what I was... ugh, never mind. You're just teasing me aren't you?\""
    mc 1 u smile "\"What was your first clue?\""
    show k 1 u at fdis
    k "\"So? To what do I owe the pleasure?\""
    mc 1 u curious "\"Given the look on your face it really doesn't sound like much of a pleasure.\""
    show k 1 u scorn at fdis
    k "\"Don't make me smack the answer out of you.\""
    mc 1 u laugh "\"Hahaha, okay okay. Sorry.\""
    show k 1 u at fdis
    mc 1 u smile "\"I came by to see what you were doing. I thought you might be going to your band today.\""
    show k 1 u worried at fdis
    k "\"It's not {i}my{/i} band. Besides...\""
    "His voice trails off without even finishing his sentence."
    mc 1 u curious "\"Is something up?\""
    show k 1 u sigh at fdis
    k "\"... No, it's nothing. I was just thinking some stuff over. I guess I'm gonna end up going today after all.\""
    "You could stand to sound a little more excited about it."
    "Didn't you choose to join their band because you wanted to be around music?"
    mc 1 u happy "\"Great! Can I come with you?\""
    "I attempt to distract him from whatever thoughts he's mulling over by being extra cheerful."
    "Hey, if it works for Jun then it might work for me too right?"
    show k 1 u uncomfortable at fdis
    k "\"Wha- You want to come with me? Why?\""
    mc 1 u smile "\"Why wouldn't I? It's a band. It's cool. Besides, I enjoyed hearing them play the last time I was there.\""
    show k 1 u sigh at fdis
    k "\"I... I can't just take you there without permission.\""
    mc 1 u "\"Why? Did they not like me being around last time?\""
    show k 1 u worried at fdis
    k "\"Well, not exactly. They said they liked having an audience...\""
    mc 1 u smile "\"Then what's the harm in taking me?\""
    show k 1 u sigh at fdis
    k "\"It's not about..."
    show k 1 u at fdis
    extend " Oh forget it. You're just gonna keep insisting until I agree aren't you?\""
    mc 1 u happy "\"Sounds like someone knows me well.\""
    show k 1 u sigh at fdis
    k "\"It really does, huh...\""
    scene SBand
    show k 1 u eyesc at fdis, five
    with fade
    "When we walk inside the room, I'm greeted to the cool and dry air-conditioned air."
    "The sensation of breathing it kinda makes the inside of my nose itch a little, but it's still pleasant nonetheless."
    k "\"Good afternoon.\""
    "Keisuke says a greeting out loud without even checking if anyone is in first."
    "It seems that the room is empty at a first glance. The instruments are all lying around haphazardly and everything seems to be in disarray."
    mc 1 u curious "\"There's no one here?\""
    show k 1 u at fdis
    k "\"Probably in the control room. Kagaho-san?\""
    show k 1 u at fdis, three with move
    show ka 1 c smile at fdis, seven with moveiridis
    "A head peeks out from the door on the far side of the room, looking at us with curiosity."
    "Once he recognizes Keisuke, the raven walks out, lifting an eyebrow."
    ka "\"Oh, Keisuke. I see you have a guest today. Hello, [povLastName].\""
    "I note his lack of an honorific inside of my head with a little bit of amusement."
    "I guess it's safe for me to drop it too in that case?"
    mc 1 u smile "\"Good afternoon. Sorry for the intrusion.\""
    "The raven crosses his arms, flashing me a polite smile."
    ka "\"It's no bother. If you're sticking around to watch us rehearse then I can already imagine some people would enjoy the opportunity to show off.\""
    mc 1 u smile "\"That's what I'm counting on.\""
    k "\"Kagaho-san, why aren't you in uniform?\""
    "The raven looks down at his clothes for a second before his eyes flicker back to the hare."
    ka "\"Well, class is over for the day so I didn't see any reason to keep them on.\""
    show k 1 u worried at fdis
    k "\"I can understand that sort of attitude from the others, but I've never seen you do something like that. Did something happen?\""
    "The raven lifts an eyebrow."
    ka "\"I think you're trying to read a little too much into something innocuous. Unless you have something on your mind that's worrying you?\""
    "Keisuke shifts and, for the first time today, I notice him hugging his arms extra close to his body."
    k "\"I just...\""
    mc 1 u curious "\"Is something going on?\""
    show k 1 u wince at fdis
    k "\"Not... not exactly.\""
    show k 1 u sigh at fdis
    k "\"Kagaho-san, do you mind talking to me alone for a second? There's something I need to ask you about.\""
    mc 1 u worried "\"Kei-kun, is everything alright?\""
    show k 1 u worried at fdis
    k "\"Yeah, just give me a second.\""
    "The raven nods, making a gesture with his head towards the separate booth."
    show ka 1 c smile at offscreenright
    show k 1 u worried at fdis, offscreenright
    with move
    "The two walk there and close the door, leaving me alone in this soundproof room."
    "... Or at least they think they did. I can see that the door was just {i}barely{/i} left ajar."
    "..."
    "I know I shouldn't but... I can't resist the urge to eavesdrop."
    "I confirm that I can't see them through the looking glass and decide that if I can't see them then they can't see me."
    "I stealthily make my way towards the door, ready to listen in on their conversation."
    ka "\"A rumor?\""
    "Kagaho's voice is the first I hear. I can't really make out what he's thinking just from his tone of voice, but he sounds somewhat amused when he asks."
    k 1 u worried "\"... I heard the girls murmuring to themselves when they thought I was out of earshot. Something about Ichigo-san moving away. Then I saw you in nothing but your daily clothes and no one else around so...\""
    ka "\"So?\""
    "His voice is calm and soothing, almost paternal."
    "Despite the two of us being in the same year and having studied in the same class once, we never interacted much."
    "Still, the little I know of him is that he's the responsible type."
    "I guess him and Shoichi would get along in that regard."
    "Although the dry sense of humor I saw the last time I came by definitely caught me by surprise."
    k "\"I was just... worried the band might disband.\""
    "?!"
    "Wait, their band might disband?"
    "But Keisuke just joined them not too long ago. Now they're dissolving?"
    ka "\"I can't really say much on the matter. Ichigo's business' is her own to disclose. You should ask her about it. I will say that we've no intention of dissolving the band though.\""
    "Kagaho's voice sounds really serious from where I stand. It's like his words are denying what was said but his voice seems inclined to agree... if that even makes any sense."
    "Ugh, I suck at reading people's mood from their voices..."
    "Wait, is this what Kei-kun was thinking about when I talked to you in front of your class?"
    show k 1 u sigh at fdis
    k "\"And... and the band would keep going even if she left?\""
    ka "\"You're asking me for information I'd have no way of giving you. I don't make decisions for the others, Keisuke. All I'm saying is that right now things are fine. You're reading too much into it.\""
    show k 1 u at fdis
    k "\"So there's really no underlying reason for you to be wearing those clothes?\""
    "I hear a dry chuckle. The raven's voice echoes, almost like a squawk (and yes, I know that's speciest)."
    ka "\"About as much reason I'd have for wearing any other type of clothes. If my clothes make you uncomfortable I could strip for you. Would that make you feel better?\""
    show k 1 u sigh at fdis
    k "\"No thanks. I already see my fair share of naked bodies in the locker room. I'm good.\""
    "I hear the sound of the door handle being rustled and immediately bolt back to where I was before."
    "Act natural, act natural."
    show k 1 u worried at fdis, three
    show ka 1 c smile at seven
    with move
    k "\"Huh? The door was open? I could have sworn I closed it.\""
    ka "\"Oh, this? Sorry, I forgot to say. The pin is kinda broken a little so you have to pull on it hard for it to actually go into its groove. Otherwise it just slides itself open again.\""
    show k 1 u sigh at fdis
    k "\"Seriously? How many issues have I had to have fixed just these past two weeks alone? How does all this stuff show up broken?\""
    ka "\"My guess is that the cleaning staff doesn't really know how to deal with all the equipment. A lot of the stuff here is really delicate. This door is bigger and heavier to help with the soundproofing but it uses a regular lock.\""
    show k 1 u worried at fdis
    k "\"It probably couldn't handle the weight is what you're saying?\""
    ka "\"It's as good a guess as any.\""
    mc 1 u considerate "\"Is everything alright?\""
    "I try acting as if I have no idea what they just discussed."
    "Good thing I'm not as crappy a liar as Shoichi is. He'd have been busted before even saying a word."
    show k 1 u sigh at fdis
    k "\"Oh, I forgot you were there for a second. Yeah, everything's fine. Just had some band matters to discuss, that's all.\""
    mc 1 u pout "\"Hey, don't just forget that I'm here!\""
    show k 1 u at fdis
    k "\"Anyway, I'll make sure to inform the faculty office so this can be fixed soon.\""
    ka "\"Thank you Keisuke.\""
    "Did he just ignore me?"
    mc 1 u curious "\"Where is everyone else by the way? Are they inside the booth or something like that?\""
    ka "\"Oh, no. They're just late. I've been listening to some recordings while I wait for them to arrive. Ichigo is supposed to be meeting with the council president. I have no idea where the others are though.\""
    mc 1 u shock "\"With Shoichi? Why?\""
    "He eyes me with curiosity, almost cracking a smile."
    ka "\"Ah, that's true, you're his best friend aren't you?\""
    mc 1 u curious "\"Yeah I am. Is something going on?\""
    show k 1 u at fdis
    k "\"Ichigo-san wanted to book the school auditorium for the band to perform in during the festival. She's probably negotiating with him.\""
    mc 1 u curious "\"Negotiating?\""
    ka "\"The student council allocates the common areas of the school for interested clubs. Not all of us are capable of using our rooms for our displays so we have to get spaces in other areas.\""
    ka "\"The auditorium is the only place where we could possibly do a show, but it's also one of the most popular areas. Lots of clubs set booths there every year. And we are basically asking for it all to ourselves.\""
    mc 1 u worried "\"Oh wow. That sounds like a difficult thing to get.\""
    ka "\"It is. Ichigo has been going at it for almost a month already but he still won't budge.\""
    ka "\"It's not like he's completely against giving it to us, it's just hard for him to reallocate the other clubs I'd imagine.\""
    mc 1 u smile "\"I could try asking for you guys if that would make things easier.\""
    ka "\"Thank you for the offer but... we don't really want to use personal connections to our advantage. If we wanted that, we'd have asked Keisuke a long time ago.\""
    show k 1 u sigh at fdis
    k "\"Not like I'd have agreed in the first place.\""
    ka "\"Also true.\""
    show k 1 u at fdis
    mc 1 u wince "\"Oh... sorry. I didn't know.\""
    ka "\"It's alright. Like I said, I appreciate the offer. We just want to do things properly.\""
    mc 1 u curious "\"So you guys are gonna be performing on the festival then? Do you have any original songs or will you be doing covers?\""
    ka "\"It's mostly covers. Even though the band has been together for quite some time, we haven't had much success with composing until recently. We only have two original songs written so far and only one of them rehearsed.\""
    show k 1 u worried at fdis
    k "\"Kagaho-san...\""
    ka "\"Keisuke is the one behind our compositions. Did you know he's quite a talented compo-\""
    show k 1 u avoidb at fdis, jumping
    k "\"Kagaho-san!\""
    "Kei-kun's voice goes up a few octaves when he interjects, trying to cut the raven off mid sentence."
    ka "\"Oh sorry, wasn't I supposed to tell him that?\""
    mc 1 u curious "\"Wow, I didn't know you also composed, Kei-kun.\""
    k "\"I... I...\""
    ka "\"I thought all he could do was compose until you and Ichigo told us he could sing and play too.\""
    k "\"Can we please stop talking about this?\""
    ka "\"Sure. If you're uncomfortable playing in front of us then that's your prerogative. We're just here to make music.\""
    show k 1 u sigh at fdis
    k "\"That's not what I... Never mind.\""
    play sound "music/door2.ogg"
    show ka 1 c smile at nine
    show k 1 u at fdis, seven
    with move
    show mi 1 u smile at four
    show sh 1 u at two
    with moveiledis
    mi "\"Heyo.\""
    sh "\"Good afternoon.\""
    "Two girls walk into the room, effectively interrupting the conversation we'd been having so far."
    "Not that I'm going to complain. The mood wasn't exactly the most comfortable here."
    "Their eyes immediately fall on me. The coyote immediately goes stiff, taking a step back once she notices my presence."
    mi "\"Oh, hi. It's you again. Kei-chan's friend?\""
    show k 1 u sigh at fdis
    k "\"Don't call me Kei-chan.\""
    mc 1 u smile "\"Yep, that's me. Kei-chan's friend.\""
    show k 1 u scorn at fdis
    k "\"I brought my tennis bag with me. I'll hit you with my racket, I swear.\""
    mc 1 u laugh "\"Alright, alright. Calm down, I was only joking.\""
    show k 1 u at fdis
    mi "\"Hey, Kagaho-san, what happened to your uniform?\""
    ka "\"Is everyone going to ask me that question?\""
    mi "\"You usually never get changed when we rehearse.\""
    ka "\"I just wanted to switch things up. There's no harm in that.\""
    mi "\"I suppose. Come on, Shoko-chan, let's get changed.\""
    show mi 1 u smile at offscreenright
    show sh 1 u at offscreenright
    show ka 1 c smile at seven
    show k 1 u at fdis, three
    with move
    "The coyote nods, following the other girl without a single word being said."
    mc 1 u curious "\"They're getting changed? Here?\""
    ka "\"We have a small bathroom adjoined with that control room. The girls tend to go get changed there instead of using the public bathroom on the floor.\""
    mc 1 u confused "\"I thought only the sports clubs had private bathrooms.\""
    ka "\"This room used to be used for the school's marching band's rehearsals. That's why it's so big. We just got lucky to be assigned it after the marching band was disbanded.\""
    mc 1 u "\"So that bathroom was supposed to be for the band's instructor to use.\""
    show k 1 u smile at fdis
    k "\"Pretty much. Now it's ours though.\""
    ka "\"They tried assigning us a regular club room at first but the noise complaints piled up pretty fast. And this was the only soundproof room they had.\""
    mc 1 u confused "\"What about the Classic Music club's room? Up until Jun transfered here, that was never used.\""
    show k 1 u at fdis
    k "\"It's not soundproof. I imagine that's because pianos, violins and the likes don't tend to be as loud as electric guitars, drums and other rock instruments.\""
    mc 1 u think "\"Oh... that does sound like a good point.\""
    play sound "music/door2.ogg"
    show k 1 u at fdis, five
    show ka 1 c smile at nine
    with move
    show ku 1 c smile at two with moveiledis
    "Once again, the sound of the door opening snaps our attention away from our conversation."
    ku "\"Hey hey. Sorry I'm a little late.\""
    "The monkey, who if I remember correctly is their guitarist, immediately looks at me, openly grinning at my sight."
    ku "\"Are we gonna have an audience today? Cool!\""
    "He then looks over at the other two members of his club currently present. His eyes linger on the raven as he raises an eyebrow."
    ku "\"Kagaho-san, how come you're not wea-\""
    ka "\"Is everyone seriously going to ask me that question?\""
    "The raven snaps, for a second dropping his composed attitude."
    "His face flashes with a scowl as his voice echoes his profound annoyance at the repeated questions."
    ku "\"Okay okay, forget I asked. Sheesh, someone's pissy today.\""
    ka "\"No. You just happen to be the third person asking me that question and I've already become fed up.\""
    ku "\"How is that my fault? Don't snap just at me.\""
    show k 1 u calm at fdis
    k "\"Sorry, I think I might have kicked off this issue.\""
    ku "\"If you're sorry then how come you're smiling?!\""
    "The monkey pouts, his face starting to get red."
    "From what I've seen last time I was here and what I'm seeing now, I guess he's not the most mature person around."
    "I mean, he did throw a temper tantrum when he thought I had dated their vocalist before."
    show k 1 u smile at fdis
    k "\"Kurusu, don't forget to breathe. I think your lips are starting to turn blue.\""
    ku "\"I am breathing!\""
    ka "\"Can we stop acting like children already? Both of you.\""
    show k 1 u haughty at fdis
    k "\"I don't see what about my behavior makes me a \"child\".\""
    ka "\"Of course you don't. You're too slick to be caught misbehaving aren't you?\""
    show k 1 u calm at fdis
    k "\"You're the one who said it.\""
    ka "\"Yes, what an odd coincidence isn't it? Now, can we focus on rehearsing?\""
    show k 1 u at fdis
    ku "\"Are the girls here already?\""
    ka "\"Miyu and Shoko are. Ichigo will probably still be a while. She's in the middle of negotiations.\""
    ku "\"What? Then how are we supposed to rehearse without her?\""
    ka "\"You know your riffs, don't you? That's all you need to rehearse.\""
    show ku 1 c smile at jumping
    ku "\"But it's just not the same without Ichigo-san!\""
    show ku 1 c smile at one
    show k 1 u at fdis, three
    show ka 1 c smile at five
    show mi 1 c smile at eight
    show sh 1 c at ten
    with move
    mi "\"What's not the same without Ichigo?\""
    "The girls walk out of the adjoining room, both changed out of their uniforms."
    "Since the monkey had been speaking so loudly, they both walk with their eyes glued to him, looks of curiosity plastered over their faces."
    ku "\"Kagaho-san wants us to rehearse without her!\""
    mi "\"Well, yeah. She said she was gonna be late today because of her negotiations with the council president. What's the problem with that?\""
    ku "\"What?! You don't think there's anything wrong with that? We can't rehearse without her!\""
    sh "\"I... actually don't see any problem either.\""
    "The coyote eyes me, her eyes lingering for a second before she finishes her sentence."
    "Damn, her eyes look really scary and unfriendly."
    "Does she... does she not like me or something?"
    "The raccoon, noticing my sudden discomfort, elbows her friend."
    mi "\"Shoko-chan, don't stare at him like that. He'll get the wrong idea.\""
    play sound "music/stab.ogg"
    show sh 1 c at shake1
    sh "\"O-oh. I'm s-sorry. I didn't mean to...\""
    "She stammers out her words, her eyes suddenly becoming fixed to her shoes."
    show k 1 u sigh at fdis
    k "\"Please try to have a little more tact, won't you?\""
    mi "\"What are you talking about? I'm all about tact.\""
    k "\"Sure...\""
    show k 1 u at fdis
    "Kagaho-san, the raven, leans up towards me, whispering on my ear."
    ka "\"{size=-4}Please don't mind her. She's really shy with newcomers and some people think she comes off as being standoffish.{/size}\""
    mc 1 u talk "\"{size=-4}Ohhh. I see. Message received.{/size}\""
    ka "\"Well, should we get to it?\""
    ku "\"But what about Ichigo-san?!\""
    show k 1 u sigh at fdis
    k "\"Look, I understand your reservations, but there's less than two weeks until the festival and you guys only have three hours a day to rehearse. Do you really wanna lose up to an entire hour because of that?\""
    ku "\"B-but...\""
    show k 1 u at fdis
    ka "\"It's as Keisuke says. We need to use our time to its fullest. We have two original songs to play and we haven't even finished learning the first one. Even I'm being optimistic, I still see us having a hard time getting them perfected by then.\""
    ka "\"We can't afford to be wasting time now. Unless you want our first show to be nothing more than song covers? In which case, good luck getting any attention with that.\""
    play sound "music/stab.ogg"
    show ku 1 c smile at shake1
    ku "\"Ugh...\""
    mi "\"Alright, let's get started then!\""
    show k 1 u avoid at fdis
    k "\"Right... I'm gonna be watching from inside the control room with [povFirstName]-san.\""
    ka "\"Alright. We'll do some warming up before we get into it. Feel free to call us out if we make any mistakes.\""
    show k 1 u sigh at fdis
    k "\"I don't think I'm qualified to do that sort of thing.\""
    ka "\"It's your song. You're the only one who can tell us if we're performing it correctly.\""
    show k 1 u avoidb at fdis
    k "\"That's... uhm...\""
    mi "\"Aww, what's wrong? Embarrassed to have your friend hearing your original composition?\""
    show k 1 u angryb at fdis
    k "\"S-shut up!\""
    mc 1 u smile "\"Nice job establishing your authority. You're getting teased by a freshman.\""
    show k 1 u sigh at fdis
    k "\"Don't you start too..."
    show k 1 u avoid at fdis
    extend " Come on. Just come with me to the control room.\""
    stop music2 fadeout 2.5
    scene ControlRoom
    show k 1 u at fdis, five
    with dissolve
    play music3 "music/BGM/Feelin Good.ogg" fadein 5.0
    "I walk into the so called \"control room\" for the first time."
    "The first thing that stands out to me is just how old the equipment inside looks."
    mc 1 u talk "\"Holy shit. Are these CRT monitors? Just how old is this stuff?\""
    show k 1 u sigh at fdis
    k "\"Most of it is unusable. I tried offering to buy new equipment for the band but they flat-out refused. All the instruments and amps they use are stuff they bought for themselves and they're all proud of that.\""
    show k 1 u at fdis
    k "\"Not that it would matter though. We don't really do any recording so the only thing that we need to have functional is the sound monitor.\""
    mc 1 u curious "\"You mean the CRTs?\""
    show k 1 u sigh at fdis
    k "\"No no. A sound monitor is something you use to monitor the sound frequencies. We plug a headphone to it so we can listen to what's going on inside as well as check each mic separately.\""
    show k 1 u at fdis
    k "\"Notice how we have more than one microphone inside? We're not just picking up the sum of the sounds inside. We have mics placed to record each instrument separately too.\""
    k "\"It allows the sound engineer to monitor every single player in the room. That's why it's called a monitor.\""
    show k 1 u sigh at fdis
    k "\"It's the only equipment in this room that isn't outdated past the point of uselessness.\""
    mc 1 u wince "\"O-oh... I didn't know any of that.\""
    "Damn, I feel so stupid with him having to explain all this stuff to me."
    "Doesn't help that he acts as if it was the most basic stuff in the world."
    show k 1 u at fdis
    k "\"Here. I'm gonna plug another headphone so you can listen too. Just don't touch anything else okay?\""
    mc 1 u considerate "\"S-sure.\""
    "Keisuke hands me a pair of earbuds and, at the same time, grabs another one for himself."
    "He puts one on his left ear, leaving the other off."
    "I assume he did it so he could still talk to me."
    "Regardless, I imitate him, trying my best not to look like too much of a novice with this stuff."
    mc 1 u curious "\"Earbuds? I thought you'd be using on-ear headphones.\""
    show k 1 u sigh at fdis
    k "\"There are no good models out there for hares. Our ears are too big and that causes the sound to bleed. A good pair of reference earbuds are better since they completely close the ear canal.\""
    mc 1 u talk "\"Damn, you really know a lot about this stuff!\""
    show k 1 u smile at fdis
    k "\"What? Mixing? Not at all. I had to research a lot of this stuff when I first joined so I could be useful. It wouldn't surprise me if I were wrong about some stuff.\""
    mc 1 u think "\"Well, in that case you sound really confident about something you don't really know anything about.\""
    show k 1 u calm at fdis
    k "\"Wouldn't be the first time.\""
    show k 1 u smile at fdis
    ka 1 c smile "\"Keisuke, can we start?\""
    "I hear someone's voice echoing inside my left ear."
    "Looking through the window to the next room, I see the raven looking directly at the two of us."
    "All of the band members are in their respective positions with their instruments."
    "I have to admit, even the meekest looking member of their band looks a hell of a lot more imposing once they have their instruments in hand."
    "They really look like people who know what they're doing. The air of confidence they all have is a little stifling if I'm being honest."
    "Kei-kun presses a button and talks into a microphone that is dangling from a pedestal near his mouth."
    k "\"Sure. Whenever you want.\""
    "The raven nods, sharing a knowing glance with the other members."
    "Almost as if on cue, their drummer, the raccoon girl, clacks her drumsticks a few times as if to make a countdown."
    "Then, they all start playing all at once. No one is even a beat late on their start."
    "The synchrony leaves me completely astounded."
    mc 1 u shock "\"W-whoa...\""
    "I have a hard time even trying to come up with words."
    "It's just... I can't even begin to put it into words."
    show k 1 u worried at fdis
    k "\"Hmm...\""
    "I look over to Kei-kun sitting next to me and see him frowning, staring at their performance with the complete opposite reaction of mine."
    mc 1 u curious "\"Is something wrong?\""
    k "\"... They're not playing like usual.\""
    mc 1 u talk "\"What do you mean?\""
    show k 1 u sigh at fdis
    k "\"Half of them are doing just fine, but... I think Ichigo-san not being here is making some of them uneasy.\""
    mc 1 u curious "\"Really? Who?\""
    show k 1 u avoid at fdis
    k "\"Guitar and keyboard. That's Kurusu and Shoko. Our bass and drums are fine, they're setting the rhythm just as they should be and are making sure no one goes too wild. I have to commend them for that.\""
    show k 1 u sigh at fdis
    k "\"But both the guitar and the keyboard are playing slightly off... It's not a huge difference, but any difference no matter how small can throw off the other members of the band too.\""
    show k 1 u avoid at fdis
    k "\"Look at Kagaho-san. He's definitely noticed.\""
    "I look through the window once more, seeing the raven looking between Kurusu and Shoko with a frown."
    "How can he concentrate on his playing and manage to keep an eye on them at the same time."
    k "\"Kagaho-san is pretty amazing like that.\""
    "As if he read my thoughts, Kei-kun starts talking about the raven, looking at bassist with what looks to me like envy."
    k "\"He's like the band's guardian or something like that. He keeps a death grip on their rhythm and always manages to keep the rowdier members from going too crazy. He's the only reason the band can play in synchrony.\""
    show k 1 u sigh at fdis
    k "\"In fact, he's probably the only reason this band can even function as a unit in the first place. He tends to act as a mediator for everyone all the time, and he's always keeping an eye on everything that's happening.\""
    show k 1 u avoid at fdis
    k "\"That guy is probably as close to having super powers as a person can be.\""
    mc 1 u smile "\"Really? Cause we know a bunch of really hard working people already. You sure he's the closest to having powers out of all the people we know?\""
    show k 1 u calm at fdis
    k "\"Maybe not more than Urata. But then again, Urata doesn't have powers. He has a problem.\""
    mc 1 u smile "\"Cheeky. I wonder how he'd react to hearing you say that.\""
    show k 1 u smile at fdis
    k "\"Probably fire a few choice expletives at me. You know, the usual.\""
    mc 1 u considerate "\"The fact that you can say that with a smile on your face is a little bit scary, I have to admit.\""
    k "\"How come? I enjoy our antagonistic to and fro. It's one of the most fun parts of my day.\""
    mc 1 u sigh2 "\"I think Shoichi isn't the only one with a problem.\""
    show k 2 u gentle at fdis
    k "\"Perhaps. But I admit to nothing.\""
    show k 1 u at fdis
    k "\"Hmm...\""
    "Despite the lighthearted conversation, Keisuke's eyes continued to be fixed on the band."
    "He watches them like a hawk, scrutinizing every minor movement and sound they make, constantly on the search for any mistakes."
    show k 1 u sigh at fdis
    k "\"Yup, this session is a bust alright...\""
    mc 1 u "\"Is it really that bad?\""
    show k 1 u avoid at fdis
    k "\"At this point, it'd be better for them to not play until Ichigo-san gets here. They're just gonna end up developing bad habits and having a hard time performing it right if they keep this up.\""
    mc 1 u wince "\"Oh, ouch. That's harsh.\""
    show k 1 u sigh at fdis
    k "\"I'm supposed to be their manager. If it means making sure they're doing well then I have to be harsh.\""
    mc 1 u smile "\"Sounds like a job you'd enjoy.\""
    show k 1 u at fdis
    k "\"I like hearing them play and helping them with their arrangements. I don't like being the ass that tells them they're awful.\""
    mc 1 u think "\"Well, that's your problem. You shouldn't be using the term \"awful\" in the first place. That's why you're an ass.\""
    show k 1 u smile at fdis
    k "\"You know what I meant, don't try to be smart with me.\""
    mc 1 u smile "\"I have no idea what you're talking about.\""
    play sound "music/flick.ogg"
    mc 1 u wince "\"Ow!\""
    "Kei-kun flicks me on the forehead, chuckling softly as I rub the spot where he just flicked me, a little stinging sensation throbbing on my head."
    k "\"That's cute, but we both know you're not slick enough to pull off a clueless act.\""
    mc 1 u sigh "\"I could do without the flicking you know.\""
    show k 1 u haughty at fdis
    k "\"What? It's my way of showing I care.\""
    mc 1 u suggestive "\"Sure it is.\""
    show k 1 u at fdis
    k "\"Hang on, they're about to finish it up.\""
    "He leans forward, pressing a button on the panel again."
    "I think that button might be so the microphone in this room transmits to the recording booth? Not really sure."
    k "\"Can you guys take five? Kagaho-san, I need to speak to you.\""
    "Barely five seconds after they finish their performance, Keisuke begins to speak, snapping everyone's attention towards the window."
    "The raven sighs, putting his bass back on the stand and speaking a few words towards the other band members that I can't hear since he's speaking away from the microphone."
    play sound "music/door2.ogg"
    show k 1 u at fdis, seven with move
    show ka 1 c smile at three with moveiledis
    ka "\"It was terrible wasn't it?\""
    "Before he's even had time to close the door, Kagaho-san asks that question."
    show k 1 u worried at fdis
    k "\"It wasn't the best, no. You and Miyu-san were doing a good job but the other two...\""
    ka "\"They're too used to following Ichigo's lead. Without her here, they get lost.\""
    show k 1 u sigh at fdis
    k "\"Yeah..."
    show k 1 u avoid at fdis
    extend " I don't know if it's the absence of Ichigo-san specifically or just the lack of vocals in general but they certainly weren't concentrating.\""
    ka "\"This is going to be a problem. I don't know how long Ichigo is going to take and I'd really rather not miss precious rehearsal time.\""
    "He crosses his arm, leaning his back against the door and letting out a big sigh."
    "Kagaho's black feathers are ruffled and messy. I can see a few beads of sweat glistening between them."
    "Is playing an instrument really that much work?"
    "Come to think of it, they're all a bit sweaty."
    "And they only played for, what, four minutes?"
    ka "\"What do you think we should do?\""
    show k 1 u at fdis
    k "\"Get Ichigo-san here.\""
    "He sighs again, a strained smile flashing over his beak."
    ka "\"Alright, let me rephrase. What do you think we {i}can{/i} do?\""
    show k 1 u worried at fdis
    k "\"Have just you and Miyu-san practice? If the other two continue trying, they're gonna end up just making things harder for themselves when they have to correct their mistakes.\""
    show k 1 u at fdis
    k "\"Alternatively, you could try to point out their mistakes and hope that they can fix it. I'm not very hopeful for that given how they've just played though.\""
    ka "\"Nah, you're right. Maybe Shoko could stand some chance of getting back on track, but Kurusu isn't the type to do well with corrections. He's gonna be thrown off his game no matter what.\""
    ka "\"If we try to correct him, he'll just get nervous trying to fix his mistake and end up making more.\""
    show k 1 u sigh at fdis
    k "\"That's what I thought too.\""
    "The both of them sigh at the same time."
    "Kagaho-san closes his eyes, letting his head hang back and lean against the wall."
    "Kei-kun on the other hand begins to rub his forehead, taking deep breaths."
    "Is he thinking? That's a very dramatic way to think."
    ka "\"Just throwing out a crazy suggestion, but... maybe you could fill in for Ichigo as a singer until she gets back?\""
    show k 1 u annoyed at fdis
    k "\"Don't be ridiculous. There's no way I could do that.\""
    ka "\"Isn't there? Ichigo seemed to think you could. She said you were a great singer.\""
    show k 1 u avoid at fdis
    k "\"That's not...\""
    mc 1 u happy "\"What's the harm in it? You did initially join this club because you wanted to sing and play guitar didn't you?\""
    show k 1 u sigh at fdis
    k "\"It's not that simple...\""
    mc 1 u confused "\"Why not?\""
    show k 1 u worried at fdis
    k "\"They're a band, not a computer. They're people who are used to working together with certain other people. You can't just swap a part out and have it work normally. Having me there would probably just throw them off even more.\""
    show k 1 u sigh at fdis
    k "\"And there's also the fact that I can't sing in public.\""
    play sound "music/tap.ogg"
    "Kagaho walks up to Keisuke, putting a hand on the hare's shoulder and smiling softly."
    ka "\"You won't know until you try. Come on, we really need to make good use of this rehearsal time.\""
    if day10 == "keisuke":
        mc 1 u smile "\"Besides, you already sang in public back at that lizard guy's store, remember? Everyone loved you.\""
        show k 1 u avoidb at fdis
        k "\"That's... that's different. I forgot there were people around. Plus, I was pressured by him into doing it.\""
        mc 1 u laugh "\"Alright. Then I'll pressure you to do it in his stead.\""
        show k 1 u sigh at fdis
    k "\"It... it doesn't work that way.\""
    ka "\"Come on. It would really help us if you could. Just for today? No one's asking you to take over for Ichigo forever. Just until she gets back.\""
    show k 1 u avoid at fdis
    k "\"...\""
    "Kagaho-san stares at Keisuke silently, his eyes glued to the hare's face, their eyes not meeting."
    show k 1 u annoyed at fdis
    k "\"Goddammit, peer pressure... fine, I'll do it.\""
    show k 1 u avoid at fdis
    ka "\"That's great. Thanks for the help.\""
    play sound "music/tap.ogg"
    play sound "music/tap.ogg"
    "The raven taps Kei-kun on the shoulder a few times, smiling."
    show ka 1 c smile at offscreenleft with moveoledis
    show k 1 u avoid at five with move
    k "\"{size=-4}Just don't blame me if I end up making things worse...{/size}\""
    mc 1 u happy "\"You'll be fine. Stop worrying so much!\""
    k "\"I hope Ichigo-san doesn't take much too long...\""
    "Could you at least try to pretend you're paying attention to me when I'm trying to encourage you?"
    mc 1 u curious "\"By the way, what should I do while you're over there with them?\""
    show k 1 u sigh at fdis
    k "\"Just... just listen to the rehearsal through the headphones and don't touch anything, okay?\""
    mc 1 u pout "\"How cold! You don't trust me not to break stuff?\""
    show k 1 u at fdis
    k "\"No.\""
    show k 1 u at offscreenleft with moveoledis
    play sound "music/stab.ogg"
    "Without even giving me time to react, he plainly utters the word \"no\" and walks out of the room."
    "Looking through the window, I see the other band members shooting him quizzical looks and starting to have a conversation."
    "I really hope this all goes well."
    stop music3 fadeout 2.5
    play music2 "music/BGM/Dog Days.ogg" fadein 5.0
    scene ControlRoom with fade
    " - 45 minutes later."
    ka "\"Alright, let's take a break for a bit.\""
    k 1 u wince "\"O-okay...\""
    "Despite Kei-kun's presence as a vocalist, the band was still having problems coordinating."
    "Having him around certainly lessened their issues, but I could tell from the faces Kagaho-san was making that things weren't anywhere near perfect yet."
    "Not only that, I could tell Kei-kun wasn't singing his best."
    "His voice sounded strained and at times I could hear him choking on notes I know he could easily hit before."
    "The whole thing was starting to leave a sour taste in my mouth by the time Kagaho-san called for a break."
    play sound "music/door2.ogg"
    show k 1 u sigh at fdis, five with moveiledis
    k "\"Finally.\""
    "Kei-kun walks into the room with a sigh, immediately flopping down on his chair."
    mc 1 u worried "\"You okay there?\""
    show k 1 u avoid at fdis
    k "\"I told him there was no way I could fill her shoes. I just screwed things up even more.\""
    mc 1 u wince "\"You think so? To me they definitely improved. Even though you were singing kinda weird there...\""
    show k 1 u sigh at fdis
    k "\"So you noticed too, huh? I was too nervous...\""
    show k 1 u at fdis, seven with move
    show ka 1 c smile at three with moveiledis
    ka "\"Keisuke?\""
    "Kei-kun immediately stands up, his whole body going stiff as soon as Kagaho-san walks into the room."
    k "\"Yes?\""
    ka "\"Are you alright? I could tell you were pretty tense over there.\""
    show k 1 u sigh at fdis
    k "\"You too? I know I was doing bad but was it really that terrible?\""
    ka "\"Actually, I wouldn't call you terrible by any stretch of the word. With that said, I did notice you looking pretty tense and uncomfortable so I figured that might be negatively impacting your performance.\""
    show k 1 u avoid at fdis
    k "\"I...\""
    mc 1 u considerate "\"It really was. I've seen Kei-kun sing before and he's much better than that.\""
    show k 1 u shock at fdis
    k "\"Wha- [povFirstName]-san!\""
    ka "\"So it's as I thought huh?\""
    "The raven crosses his arms, idly scratching at his chest and looking past us with a look of wonderment."
    show k 1 u worried at fdis
    k "\"Kagaho-san?\""
    ka "\"Oh, sorry. Did you say something?\""
    "His attention snaps back to Keisuke, his brow furrowing."
    k "\"Are you alright? You don't usually get lost in thought.\""
    ka "\"No, everything's alright. I was just... considering some things.\""
    k "\"May I ask what those things are?\""
    ka "\"You may not.\""
    show k 1 u wince at fdis, shake1
    play sound "music/stab.ogg"
    k "\"O-oh. Sorry...\""
    "Kagaho chuckles, giving the nervous hare a few friendly pats on the shoulder."
    ka "\"Don't worry, it's nothing major. I just prefer to keep my thoughts private, that's all.\""
    ka "\"Still, I enjoyed performing with you, even if it was just a rehearsal. Having your vocals definitely helped the other two concentrate, even if they weren't back to 100\% immediately. I'd like to do it again.\""
    show k 1 u avoid at fdis
    k "\"You said it was a one time thing, remember...\""
    ka "\"Right, right. I did say that.\""
    ku 1 c "\"Ah, Ichigo-san!\"" with hpunch
    show k 1 u shock at fdis
    "I hear someone's voice echoing loudly in my ear from the one earbud I still have on."
    "I immediately flinch and instinctively take it out."
    k "\"[povFirstName]-san, are you alright?\""
    mc 1 u wince "\"Y-yeah. Someone just shouted really loudly into the mic, that's all.\""
    "Kei-kun notices my sudden movement and walks up to me, examining me with a look of worry on his face."
    ka "\"Ah, it looks like Ichigo's here.\""
    show k 1 u at fdis
    "The three of us look out the window and see Ichigo's figure immediately getting mobbed by the three remaining members."
    ka "\"Let's go. We should see what was the result of the negotiations.\""
    show k 1 u worried at fdis
    k "\"Y-yeah...\""
    play sound "music/door2.ogg"
    scene SBand
    show k 1 u worried at fdis, ten
    show ka 1 c smile at eight
    show mi 1 c smile at six
    show sh 1 c at four
    show ku 1 c smile at two
    show i 1 u smile at zero
    with fade
    i "\"-nna wait until everyone's here.\""
    "As soon as we walk into the recording boot, Ichigo's eyes fall on us."
    i "\"Ah, there you two are! Oh, and we have a guest too. Hi there, [povLastName]-kun.\""
    mc 1 u considerate "\"Hi there, Minazuki. Sorry for the intrusion.\""
    i "\"It's no intrusion. If you're a friend of one of us, you're a friend of all of us.\""
    k "\"Ichigo-san, how was the meeting with Urata?\""
    "Kei-kun ignores all pleasantries and immediately asks the main question he's had on his mind."
    "The calico cat smiles knowingly."
    i "\"It went well. He's agreed to speak with the other clubs that had approached him for a spot in the gym building. He says if he can sort things out with them he'll let us use it for our concert.\""
    show ku 1 c smile at jumping
    ku "\"{size=+4}Yes! That's awesome!{/size}\"" with hpunch
    "I immediately cover my ears as the monkey's booming voice echoes inside the room."
    "I'm not even the only one to do it."
    show mi 1 c smile at jumping
    mi "\"Hey, use your inside voice you airhead! This is a closed soundproof room, you don't have to yell!\""
    ku "\"S-sorry...\""
    "His spirits immediately deflate as he begins to get chastized by his colleague."
    "The others in the room ignore their little show, focusing on their own conversations."
    sh "\"Ichigo-san, I got you the book you asked for in my bag.\""
    i "\"Oh, thanks. Give it to me once we're done with rehearsal for the day, \'kay?\""
    sh "\"\'Kay.\""
    i "\"Hey, Kagaho. Sorry I'm late. Did things go well without me around.\""
    ka "\"Not as well as I'd hoped. But I got Keisuke to do the vocals in your place while you were away and that made things slightly better.\""
    show k 1 u avoidb at fdis, jumping
    k "\"Kagaho-san!\""
    "Her eyes immediately turn to Kei-kun, a beaming smile on her face."
    i "\"Really?! Oh, thank you so much for the help, Kei-chan.\""
    k "\"I-it was nothing. {size=-2}Also, please don't call me Kei-chan.{/size}\""
    show k 1 u worried at fdis
    i "\"I'll just go get changed real quick and we can get back to rehearsal!\""
    ka "\"Alright. Try not to slip and break your neck in the bathroom.\""
    i "\"That would be one glorious way to die, wouldn't it?\""
    "The raven chuckles, crossing his eyes and looking her up and down with a raised eyebrow and a smile."
    ka "\"It sure would be. I can already picture the newspaper headlines.\""
    i "\"You're too old-fashioned, Kagaho. No one buys newspapers anymore.\""
    ka "\"I still do.\""
    i "\"Hence why I said old-fashioned. Anyway, I'll be right back.\""
    k "\"If you guys will excuse me, I'm gonna go outside for some air.\""
    ka "\"Alright. We'll start again in five. Make sure you're back by them.\""
    k "\"Sure thing.\""
    stop music2 fadeout 2.5
    play music3 "music/BGM/Reminiscing.ogg" fadein 5.0
    scene SCorridorE
    show k 1 u sigh at fdis, five
    with fade
    "Kei-kun grabs my arm and leads me out of the room with him in a rush."
    mc 1 u wince "\"H-hey, what's going on?\""
    k "\"Nothing, nothing. I just needed a little breather.\""
    show k 1 u avoid at fdis
    k "\"Singing for them was... really overwhelming.\""
    mc 1 u considerate "\"I can imagine. You still did good though.\""
    show k 1 u sigh at fdis
    k "\"I certainly hope so. One way or another, these are people who actually know about music. They're not just some rank amateurs that have no idea what they're doing. They're all good.\""
    mc 1 u sigh "\"You certainly have a way of being negative about everything.\""
    show k 1 u wince at fdis
    k "\"Sorry...\""
    show k 1 u at fdis
    mc 1 u confused "\"By the way, what was that conversation between Minazuki and Kagaho? The whole \"slip and break your neck\" thing?\""
    show k 1 u worried at fdis
    k "\"Oh, that? They always joke around with each other like that. Not always that morbid though...\""
    mc 1 u wince "\"Sounds weird if you ask me.\""
    show k 1 u at fdis
    k "\"Like you have any room to talk. Look at how you usually joke around with Urata, Saya-san and I.\""
    mc 1 u sigh2 "\"I don't think I've ever gone that far with my jokes though.\""
    show k 1 u smile at fdis
    k "\"You're only one step short of it though.\""
    mc 1 u sigh "\"Hell no.\""
    show k 2 u gentle at fdis
    k "\"Hahaha.\""
    mc 1 u sigh "\"Now {i}you're{/i} the one laughing at my expense.\""
    show k 1 u wry at fdis
    k "\"Sorry. I just found it funny. Thanks for the help though.\""
    show k 1 u at fdis
    mc 1 u confused "\"Help? What, if anything, did I do to help?\""
    show k 1 u smile at fdis
    k "\"You have no idea how nervous during the time I was singing there. Still, talking to you helped me calm down a bit. So thanks for that.\""
    mc 1 u confused "\"I still feel like I'm being thanked for not really doing anything.\""
    show k 1 u calm at fdis
    k "\"I'm just calling it how I see it.\""
    show k 1 u at fdis
    k "\"Anyway, we should probably head back inside.\""
    mc 1 u curious "\"Have the five minutes already passed?\""
    show k 1 u calm at fdis
    "I make a motion to grab my phone from my pocket, but Kei-kun puts his hand on top of mine and stops me."
    k "\"No, it's nothing like that. It's just that I've had enough time to recompose myself, so I think I should head back inside regardless.\""
    show k 1 u smile at fdis
    k "\"You're free to stay out here if you'd prefer it though.\""
    mc 1 u "\"Nah, there's no real point to that. I'd rather be inside with you. Plus, if my presence really is calming then I can do some good while at it.\""
    show k 1 u wry at fdis
    k "\"Thanks.\""
    scene SkyE with fade
    "We walk back into the club room, immediately being welcomed to the sight of the band amidst an enthusiastic discussion about what songs they should perform at the festival."
    "Kei-kun and I spend the rest of the afternoon inside the control room, listening to their rehearsal whilst also chatting amongst ourselves."
    "Once we finally finish for the day, we all head back home, wishing each other a good night."
    "All I know is that I now feel really excited about the festival for some reason."
    "I really want to see them performing in a real stage."
    stop music3 fadeout 2.5
    $ date = None
    jump Day15_Keisuke
