label Day15_Keisuke:
    window hide
    scene May23 with fade
    play sound "music/windchimes.ogg"
    show blossoms movie
    $ renpy.pause(5.5)
    play music "music/crowd01.ogg" fadein 5.0
    scene Station with fade
    window show
    $ date = "day15"
    "The area around the station is bustling with activity, lots of noise and bodies to go around."
    "Many students are heading home after class now, so the majority of this mass of people is composed of them."
    "For some reason, Kei-kun asked me during lunch hour to meet him here thirty minutes after class."
    "I have no idea why he called me but since he seemed to need help, I didn't hesitate to come."
    k 1 c smile "\"[povFirstName]-san, over here!\""
    show k 1 c smile at fdis, seven
    show vic 1 c smile at three
    with moveiledis
    "I hear Kei-kun's voice calling me from behind."
    "Once I turn around, I see the familiar white hare followed closely by a fox."
    play music2 "music/BGM/Hanging Out.ogg" fadein 5.0
    mc 1 c curious "\"Vic-kun? You're here too?\""
    vic "\"Oui... I mean, yes!\""
    k "\"He's actually the reason I called you over today.\""
    mc 1 c confused "\"He is? How so?\""
    show k 1 c at fdis
    k "\"He wanted my help navigating through the city so he could buy a few things. He wanted to join the tennis club once the festival is over so we're mainly going to the sporting goods store.\""
    k "\"Even though his spoken Japanese is pretty good, he still has problems reading the kanji so he wanted my help to know what's what.\""
    mc 1 c talk "\"That's pretty nice of you. Although I'm not sure why you called me over too.\""
    show k 1 c worried at fdis
    k "\"I think we've already established that I'm not very good at doing these sorts of things by myself, so I thought it'd be good to have you around in case things go wrong.\""
    show k 1 c at fdis
    mc 1 c smile "\"Pfft, is that so? Well, I'll be happy to help.\""
    vic "\"Merci! Oh, erm... that's \"thank you\" in my language.\""
    mc 1 c "\"Still trying to get used to speaking in Japanese?\""
    vic "\"Ou- Yes. I sometimes revert back to it out of habit.\""
    mc 1 c talk "\"I'm starting to understand why you asked Kei-kun to help you with this.\""
    vic "\"Yes. That way I have someone who understands me even if I'm speaking in French.\""
    show k 1 c smile at fdis
    k "\"Well, it certainly doesn't hurt to have a competent liaison.\""
    mc 1 c curious "\"What about Alex? Is he going to be coming with us?\""
    "After what happened the last time Kei-kun went out on his own, I certainly think he should."
    show k 1 c worried at fdis
    k "\"... If I had any say in this, he wouldn't.\""
    mc 1 c worried "\"What ab-\""
    show k 1 c smile at fdis
    k "\"Don't worry, I definitely still remember what happened last time. I asked Alex to meet us at the store. Having a guy that big walking through this crowd would be way too troublesome.\""
    mc 1 c talk "\"Oh. Huh. You actually thought things through. Good to see you chose to err on the side of caution.\""
    show k 1 c sigh at fdis
    k "\"What are you talking about? I always think things through and I {i}always{/i} err on the side of caution.\""
    "Explain to me how you got robbed then. Go on, I'll wait..."
    mc 1 c considerate "\"... If you say so.\""
    show k 1 c at fdis
    vic "\"Who's this Alex guy? Another student?\""
    show k 1 c worried at fdis
    k "\"Oh, right. You don't know Alex... he's... my personal bodyguard.\""
    vic "\"Wow, you even have a personal bodyguard? I'd been told that you're rich but I never thought you'd be that kind of stereotypical rich.\""
    show k 1 c sigh at fdis
    k "\"I thought you hated stereotypes.\""
    vic "\"I do. It's why this information leaves me so conflicted.\""
    mc 1 c happy "\"Alex is a massive wolf who I'm pretty sure could bench press me with one hand.\""
    vic "\"W-wow, really? D-damn...\""
    show k 1 c annoyed at fdis
    k "\"[povFirstName]-san, please don't make exaggerations like that. He's actually going to take you seriously.\""
    vic "\"O-oh. So it was just a joke? {size=-2}Shame.{/size}\""
    mc 1 c confused "\"What's the problem? I mean, he {i}is{/i} super tall and strong.\""
    show k 1 c avoid at fdis
    k "\"Maybe, but I very much doubt he could bench press you one-handed.\""
    mc 1 c happy "\"How about I ask him once we meet up?\""
    show k 1 c sigh at fdis
    k "\"... I'm not even gonna say anything to that.\""
    mc 1 c smile "\"Aww, it's no fun if you just roll over and take it.\""
    vic "\"I think that's highly dependent on the context of the situation.\""
    k "\"Please tell me that wasn't innuendo just now...\""
    vic "\"Alright... I won't tell you.\""
    show k 1 c avoid at fdis
    k "\"... Are you mocking me?\""
    mc 1 c happy "\"Damn, Vic-kun has a sharper tongue than I realized.\""
    k "\"He is a fox after all.\""
    vic "\"What did I say about stereotypes?\""
    show k 1 c smile at fdis
    k "\"Alright, fair enough."
    show k 1 c at fdis
    extend " By the way, shall we get going? The crowd over here is quite loud at this time of day.\""
    vic "\"Yes, I think that's a good idea.\""
    "I nod, making a gesture with my hand that tells Kei-kun to take the lead."
    show k 1 c smile at fdis
    "He flashes me an appreciative smile, leading the way to the store."
    stop music fadeout 2.5
    scene SportStore
    show k 1 c smile at fdis, seven
    show vic 1 c smile at three
    with fade
    k "\"Here you go, Victor. This is the sporting goods store I personally tend to shop at.\""
    mc 1 c suggestive "\"Oh please. You only come here because I introduced you to this place. You used to shop online before that.\""
    show k 1 c avoid at fdis
    k "\"T-that's irrelevant.\""
    mc 1 c happy "\"{i}Suuuure{/i} it is.\""
    vic "\"I didn't recognize the kanji in the letterboard so either way I wouldn't have realized what kind of store this was regardless.\""
    show k 1 c at fdis
    k "\"I mean... let's be honest. If you look at the display case on the entrance you can already see a bunch of sneakers, rackets and balls. I'm pretty sure you'd be able to tell.\""
    vic "\"Oh... huh... I guess that's true.\""
    mc 1 c smile "\"So you're basically saying that we were useless.\""
    show k 1 c smile at fdis
    k "\"Either that or Victor is clueless.\""
    play sound "music/stab.ogg"
    show vic 1 c smile at shake1
    vic "\"Guh...\""
    mc 1 c smile "\"Anyway, should we go look for Alex?\""
    show k 1 c at fdis
    k "\"Look? He's almost two meters tall. If he's inside, he's gonna be standing out.\""
    al 1 u "\"Or he's going to be standing right behind you.\""
    show k 1 c shock at fdis, five
    show vic 1 c smile at two
    with move
    show al 1 u at eight with moveiridis
    mc 1 c shock "\"Waaah!\"" with hpunch
    "The three of us jump in surprise at the sound of the wolf's deep voice echoing right behind our ears."
    show k 1 c sigh at fdis
    k "\"Jesus, Alex, don't do that. You almost gave me a heart attack.\""
    al "\"If a guy my size can sneak behind you then I'm really not surprised you were pick-pocketed.\""
    show k 1 c avoid at fdis
    k "\"Thanks for the vote of confidence.\""
    vic "\"Damn... you really are big...\""
    "Alex's attention snaps to Vic-kun, his eyes looking the fox up and down with suspicion."
    al "\"Yes. I seem to be getting that a lot lately.\""
    "Victor instinctively takes a step back, suddenly looking very unsure of himself."
    show k 1 c annoyed at fdis
    k "\"Alex, stop glaring at him like that.\""
    al "\"I have to make sure he doesn't represent a risk to you.\""
    k "\"For God's sake, Alex, he's my senior in school. What kind of risk do you think he can represent?\""
    al "\"I can't know until I've properly examined him.\""
    vic "\"E-examined?\""
    "The fox takes another step back."
    show k 1 c avoid at fdis
    k "\"This kind of crap is why I avoid taking you with me when I go out.\""
    al "\"And yet look how well that turned out. You got robbed.\""
    show k 1 c sigh at fdis
    k "\"You're never going to let me live that down are you?\""
    al "\"Not likely.\""
    mc 1 c "\"If you two don't mind, I'm gonna show Vic-kun around the store while you guys bicker.\""
    show k 1 c shock at fdis
    k "\"Wha- wait. Don't leave me alone with him!\""
    "I lead Victor away, mostly to give him a break from Alex's... intensity."
    show k 1 c worried at fdis
    "Kei-kun quickly follows behind, and the ever loyal Alexander accompanies him."
    mc 1 c talk "\"What kind of gear are you looking for here?\""
    vic "\"Well, I've never really played tennis before so I'd need a good racket. Maybe a duffel bag to carry my things in too.\""
    mc 1 c curious "\"Do you have any sneakers? Taping? Clothing for you to practice in?\""
    vic "\"I do have sneakers, though they're more like running shoes... And I should probably buy a few polos shouldn't I?\""
    mc 1 c smile "\"You don't necessarily have to use polos to play. Any sports shirt works.\""
    vic "\"Hmm...\""
    "The fox studies the shelves carefully, gently touching the items to get a feel for their weight and textures."
    "It definitely doesn't seem like this is his first time doing this kind of thing."
    show k 1 c smile at fdis
    k "\"You seem to know what you're doing.\""
    vic "\"Well yeah. I told you I used to play badminton in France. I'm the one who chose all the gear I used back then.\""
    k "\"That makes things easier.\""
    al "\"What led you to come to Japan of all places?\""
    show vic 1 c smile at jumping
    "As if he only just now remembered Alex's presence in the room, Victor yelps and jumps where he stands, surprised by the larger male's voice."
    show k 1 c worried at fdis
    k "\"Damn, you've really terrified him.\""
    al "\"Me? What did I do?\""
    show k 1 c wince at fdis
    k "\"How can you be that clueless?\""
    "Alex frowns, looking down at Kei-kun with confusion."
    show k 1 c at fdis
    vic "\"I-it's fine. I was just a bit surprised, that's all.\""
    "The fox takes a few deep breaths to calm himself."
    "Suddenly looking up and into Alex's eyes, he attempts to answer confidently."
    vic "\"I wanted to broaden my horizons. Immerse myself in a different culture. And I've always been curious about Japan, so...\""
    "Alexander nods to his words, as if he were silently approving of his reasons."
    vic "\"What about you? I mean, you don't look Japanese and your name definitely isn't Japanese.\""
    al "\"I got a job here.\""
    "He responds dryly, leaving a lot to be desired in his answer."
    k "\"Alex has been working for my family for years. I don't quite know how he ended up in our employ but he's been my personal butler and bodyguard for a long time.\""
    "The wolf nods in agreement."
    vic "\"Damn. So you guys have known each other for years then?\""
    al "\"I've watched Keisuke grow, yes.\""
    show k 1 c smile at fdis
    k "\"He's probably the closest thing I have to a childhood friend.\""
    mc 1 c confused "\"How long have you actually known Alex for? You never really specified. All you've ever said is that it's been years.\""
    show k 1 c at fdis
    al "\"I've been working for the Urushihara Corporation for nine years. I began my employ right after I turned eighteen.\""
    mc 1 c shock "\"Wha- really? Wait, then you're only twenty seven?\""
    al "\"Yes, why?\""
    show vic 1 c smile at jumping
    vic "\"No way! You're so... so large and bulky and mature looking. You look more like you're in your late thirties.\""
    "The wolf frowns."
    al "\"No. I'm only twenty seven. I'd appreciate if you didn't treat me like some old geezer. It displeases me.\""
    play sound "music/stab.ogg"
    vic "\"U-understood.\"" with hpunch
    show k 2 c gentle at fdis
    k "\"Pfft... ahahahahaha.\""
    mc 1 c pout "\"Stop laughing at us!\""
    k "\"Sorry, sorry. It's just... I can't believe you guys thought Alex was that old.\""
    mc 1 c sigh "\"Give me a break, okay? I mean... just look at him. He looks way too mature to be in his late twenties.\""
    show k 1 c smile at fdis
    k "\"Well, sorry to burst your bubble but he's telling the truth. He's not that much older than us.\""
    vic "\"He's still ten years older than you though.\""
    show k 1 c calm at fdis
    k "\"Maybe. But I grew up with Alex. There's no one I trust more in the world.\""
    "Upon hearing those words, a small smile makes its way into Alex's face, his tail beginning to sway sideways ever so slightly."
    "But then again, I think I'm the only one who noticed it."
    al "\"I appreciate it.\""
    k "\"You're welcome.\""
    show k 1 c smile at fdis
    k "\"So, Victor, do you have your eye on anything in particular?\""
    vic "\"Well... I know nothing about tennis rackets so I'm gonna need some help with that. Also, I think I'm gonna buy new shoes too.\""
    mc 1 c smile "\"Kei-kun can help you with the rackets. He's far more knowledgeable on those than I am. On the other hand, I can go around getting you my recommendation for shoes while you guys check the rackets.\""
    vic "\"Oh, really? That's super nice of you. Thanks.\""
    mc 1 c happy "\"No problem. What's your shoe size?\""
    vic "\"Erm... In Europe I'd be a 41. I don't know if you guys have different sizes here in Japan.\""
    mc 1 c smile "\"No worries. I'll look it up on my phone and see if there's any conversion that needs to be made. I'll be right back.\""
    show al 1 u at five
    show k 1 c smile at offscreenright
    show vic 1 c smile at offscreenright
    with move
    "I walk away from them to browse the shoes on display and check out which ones I'd recommend for Vic-kun."
    "I immediately notice Alex following me around the store."
    "Spinning around with my heels, I turn to look him in the eye."
    mc 1 c confused "\"Uhm... you do know Kei-kun is over there, right?\""
    "He nods."
    al "\"I'm aware. However, he already has someone with him, meaning that he's safe. You on the other hand would be walking around alone.\""
    mc 1 c considerate "\"This is a sporting good store two blocks away from the station. I think I'm safe in here.\""
    al "\"Still, it doesn't hurt to keep my eye on you.\""
    mc 1 c confused "\"Why though? I'm not your boss.\""
    al "\"True. But you're someone important to him, meaning that your safety is also important to me.\""
    mc 1 c considerate "\"I think you're taking your job way too serious here.\""
    "The wolf shrugs, continuing to follow me around."
    mc 1 c confused "\"You sure it's okay to be walking with me? What if something happens to Keisuke?\""
    al "\"Like I said, he already has someone with him. He'll be fine. Besides, if something happens, I can still keep my eye on him from here. It's not that big of a store.\""
    mc 1 c smile "\"Does this mean you trust Vic-kun won't do anything to him?\""
    al "\"Not yet, but I choose to give him the benefit of the doubt.\""
    mc 1 c considerate "\"Well, aren't you altruistic.\""
    "He smiles, shrugging once again."
    "I continue to walk around, checking all the shoes that catch my eye and making sure to read their specifications."
    mc 1 c curious "\"So you and Kei-kun have known each other for nine years, huh?\""
    al "\"Yes.\""
    mc 1 c talk "\"How did you end up working for his family so early? I mean, you were just eighteen and you weren't even Japanese.\""
    al "\"I was recommended to the position by my former teacher. He had ties to the Urushihara Corporation and showed them how competent I was.\""
    mc 1 c talk "\"Oh. That sounds easier than I thought it'd be.\""
    "Alex shakes his head sideway, looking down at me with a mournful smile."
    al "\"Make no mistake, it was still incredibly difficult. They were very keen on testing me to make sure I was good enough for the job. I was to be the personal bodyguard of the company's only heir after all.\""
    mc 1 c worried "\"Ah... I hadn't thought of that.\""
    al "\"Still, things worked out well in the end. Keisuke and I bonded over time and they choose to keep me in the position because of it.\""
    mc 1 c confused "\"No offense but... his family isn't exactly nice. I'm surprised they chose to hire someone who treated him well. I thought they'd want someone who'd make him miserable.\""
    "He chuckles, shaking his head in negative once again."
    al "\"They can be... difficult at times. But making the sole heir of the company miserable would be in no one's best interest.\""
    mc 1 c talk "\"I guess...\""
    al "\"I certainly faced my fair share of discrimination when I first started at my job. Most of the servants working at the estate are much older than I am. They were... mistrustful of me when I first started.\""
    mc 1 c talk "\"I've only ever interacted with you and one other butler when I visited so I don't really know what they'd be like.\""
    al "\"The other butler in question is Kuroda. He was one of the few people to treat me cordially when I began working here.\""
    mc 1 c curious "\"Has he been with the family for a long time?\""
    al "\"Much longer than I have. He's worked for the company since Keisuke's father first became CEO some twenty years ago.\""
    mc 1 c shock "\"W-wow. That long, huh?\""
    "Alex nods solemnly."
    al "\"Why the sudden interest in it? Are you planning on becoming a butler once you graduate?\""
    mc 1 c considerate "\"Hardly. I've already had my career decided a long time ago.\""
    al "\"Yes. Keisuke tells me you're quite talented. He believes you'll become a world renowned athlete in the near future.\""
    mc 1 c shock "\"What? Really?!\""
    al "\"Oh yes. He's been trying to convince his father to offer you a sponsorship before you make your debut. He says he wants to help once you do.\""
    mc 1 c worried "\"... I had no idea.\""
    al "\"He's a very secretive person so it doesn't really surprise me. He's the type to keep his feelings for people hidden deep inside. He really cares about you and your entire group, regardless of how he might act.\""
    mc 1 c worried "\"... I see.\""
    mc 1 c confused "\"...{w} Wait, why are you telling me this? Wouldn't it piss him off if he found out?\""
    "The wolf smiles, shrugging with a cheeky expression on his face. I'm not used to seeing him make this kind of expression."
    al "\"Probably. But he's a very awkward person. The last thing I want is for his reservedness to be misconstrued for callousness. I know how devastated he'd be if he lost any of you as his friends.\""
    mc 1 c worried "\"Does he really care about us that much?\""
    al "\"Yes. He talks about you and your friends all the time. You're the most talked about too.\""
    mc 1 c wince "\"M-me? Why me?\""
    "He shrugs."
    al "\"Hell if I know. Still, he seems to be quite fond of you. Much more than I initially imagined too.\""
    mc 1 c considerate "\"He's so gonna kill you if he finds out you're telling me this stuff.\""
    al "\"I'll run the risk. I just want to make sure you know how much you mean to him. Knowing him, it wouldn't surprise me if he gave people the wrong idea and ended up losing his friends for it.\""
    mc 1 c "\"I think you have too little faith on him. Kei-kun's not that awkward of a person. Besides, he fits right into our group.\""
    al "\"Perhaps now he does. But up until April I always heard about how he felt out of place and excluded. I don't want to hear him saying things like that anymore, nor do I want to see him hurt.\""
    mc 1 c happy "\"God, you almost sound like his older brother!\""
    al "\"Older brother, huh?\""
    "He pauses, looking suddenly lost in thought. After a few seconds of consideration, he nods, smiling."
    al "\"I suppose in a way I do think of him as a little brother that I must protect.\""
    if day10 == "keisuke":
        mc 1 c considerate "\"Just be careful that this \"protection\" of yours doesn't result on you choking any of his friends, okay?\""
        "Alex shifts where he stands, looking uncomfortable."
        al "\"Ah yes... that. I never did properly apologize for my actions that day, did I?\""
        mc 1 c smile "\"It's fine. I don't hold a grudge. You did scare the crap out of me though.\""
        "He chuckles."
        al "\"Good to hear. Perhaps me being scary will be sufficient deterrent to anyone who might wish to do him harm.\""
        mc 1 c smile "\"We can only hope.\""
    "I finish grabbing a few more pairs of shoes, enjoying a pleasant conversation with Alex along the way."
    hide vic 1 c smile
    show vic 1 c smile at offscreenright
    "I don't really understand why he suddenly felt the need to accompany me but I have to admit he is nice company."
    show al 1 u at two
    show vic 1 c smile at five
    show k 2 c annoyed at fdis, eight
    with move
    mc 1 c smile "\"I'm back. How's the racket shopping going?\""
    vic "\"We've managed to narrow it down to two. Keisuke is trying to decide between them.\""
    k "\"-on the other hand, this one is lighter and more flexible.\""
    "Keisuke seems to be completely ignoring us, muttering words to himself."
    "He's probably comparing the rackets in his head and trying to decide."
    mc 1 c talk "\"You wanna try the shoes I found in the meantime? This might take a while.\""
    vic "\"Oh, sure. Thanks!\""
    "I hand him around six different pairs of shoes that I brought along with me."
    "Thankfully Alex helped me to carry them around so it wasn't much trouble."
    vic "\"These ones are very comfortable!\""
    "Victor tries on the first pair, getting up and walking in circles with them."
    mc 1 c talk "\"They're supposed to help give you an impulse when you run. It's a very breathable material too so you don't have to worry about your feet getting too sweaty.\""
    vic "\"That's definitely a good thing.\""
    show k 1 c at fdis
    k "\"Oh, [povFirstName]-san? When did you get back?\""
    mc 1 c "\"Not too long ago. You seemed to be engrossed in your thoughts so we didn't want to distract you.\""
    show k 1 c calm at fdis
    k "\"Sorry about that."
    show k 1 c smile at fdis
    extend " How did the shoe shopping go?\""
    vic "\"I'm gonna try on the second pair now. I really liked this first one.\""
    k "\"You didn't pick anything overly pricey did you?\""
    mc 1 c "\"I tried to be conscious of the price when making my choices. Nothing too egregious.\""
    show k 1 c sigh at fdis
    k "\"That's good. Wouldn't want you to make the same mistake I did.\""
    mc 1 c happy "\"You mean at the ice cream store? Man, those prices almost gave me a heart attack.\""
    k "\"Exactly...\""
    show k 1 c at fdis
    k "\"By the way, Alex, you were walking around the store with [povFirstName]-san?\""
    al "\"Yes. I hope it wasn't a problem. I wanted to make sure he was safe and you already had company with you.\""
    show k 1 c smile at fdis
    k "\"Of course its no problem. Thanks for looking out for him.\""
    mc 1 c considerate "\"{size=-2}Not that it was needed.{/size}\""
    vic "\"Did you make a decision on the racket?\""
    k "\"Yes. I think this one will be ideal for you!\""
    "Kei-kun hands him a purple racket with black stripes and white finishing around the handle."
    "Victor grabs it, waving it around with curiosity."
    vic "\"Wow. It's lighter than I expected.\""
    k "\"It's a good all-rounder racket. You can buy a new one if you decide to specialize in a specific type of shot or something of the sorts, but for a beginner I would recommend this.\""
    vic "\"Alright, then this is the one I'm getting. Thanks!\""
    "He looks the racket up and down, examining it with a big smile on his face."
    "Vic-kun looks really pleased with it as he completely forgets to try on the rest of the shoes while waving the racket around."
    "I call over an attendant, taking the racket from Victor's hand and handing it to the man."
    vic "\"Wha- hey!\""
    mc 1 c talk "\"Can you hold onto this for when we check-out?\""
    "Clerk" "\"Certainly. I'll put it behind the register.\""
    mc 1 c smile "\"Thank you.\""
    "I wave as the worker walks away with the racket in his hands, feeling very pleased with myself."
    show vic 1 c smile at jumping
    vic "\"Why did you do that?\""
    "Vic-kun pouts."
    mc 1 c "\"Because you were distracted playing around with it and forgot to do the rest of your shopping. Plus, this way you don't have to carry it around while you choose what you're going to buy.\""
    vic "\"You could have just asked me to put it down you know.\""
    al "\"I believe this way was more efficient regardless.\""
    vic "\"Tch. Party pooper.\""
    mc 1 c "\"Yup. That's me. I'm Mister Anti-fun. Now get back to trying on those shoes.\""
    "Victor grumbles unhappily, sitting back down on the bench and proceeding to try on the next pair."
    show k 1 c at fdis
    k "\"Hmm... We also have to look at some shirts after he's picked a shoe.\""
    mc 1 c "\"Just make sure not to go too overboard. If he buys a bunch of stuff then the bill is gonna come out pretty scary.\""
    k "\"Yeah, I can already imagine that.\""
    stop music2 fadeout 2.5
    play music3 "music/BGM/Snowy Day.ogg" fadein 5.0
    scene Station
    show al 1 u at two
    show k 1 c at fdis, five
    show vic 1 c smile at eight
    with fade
    "Once we finish shopping for Victor's equipment, we walk back to the station area."
    "The excess movement has already begun to die down, making it so the area isn't as crowded anymore."
    vic "\"Man, I ended up buying a lot of stuff huh...\""
    "He's carrying five bags with him, constantly shifting them around in his hands in an attempt to get comfortable."
    vic "\"Why do they use bags with thin nylon handles. It feels like it's slicing my hand because of the weight.\""
    al "\"Here, let me.\""
    show al 1 u at six with move
    show al 1 u at two with move
    "Alex walks up to the fox, taking the bags from his hands and carrying it in his own."
    vic "\"Oh. T-thanks.\""
    al "\"You're welcome.\""
    show k 1 c smile at fdis
    k "\"So, Victor, is there anything else you'd like to see today?\""
    vic "\"Hmm... Maybe a bathhouse?\""
    mc 1 c sigh "\"Not even if you paid me would I go to one.\""
    vic "\"O-oh.\""
    show k 2 c gentle at fdis
    k "\"Sorry. [povFirstName]-san isn't a big fan of nudity.\""
    vic "\"Huh... I wasn't expecting that.\""
    show k 1 c smile at fdis
    k "\"Any other ideas?\""
    mc 1 c sigh "\"Preferably ones that don't involve nudity?\""
    vic "\"Well... there are a lot of touristic spots and historic monuments in Japan, right? Maybe we could go to one of those? I did come to the country primarily to learn the culture.\""
    show k 2 c annoyed at fdis
    k "\"Hmm... a touristic spot, huh?\""
    show k 1 c at fdis
    al "\"I know of one place where we could go.\""
    k "\"Really? I never took you for the touristy type.\""
    "Alex shrugs."
    al "\"Knowing about the layout of the city helps me do my job.\""
    show k 1 c smile at fdis
    k "\"Okay. I'm all ears. What's your idea?\""
    al "\"I'll take us there. Just follow me.\""
    mc 1 c think "\"A big, scary man asks you to follow to someplace unknown. This sounds like the set-up for some horror movie.\""
    al "\"Would you rather I leave you here by yourself?\""
    mc 1 c considerate "\"No no. I'll go. I'll go.\""
    stop music3 fadeout 2.5
    play music2 "music/BGM/The People Here.ogg" fadein 5.0
    scene Shrine
    show al 1 u at two
    show k 1 c at fdis, five
    show vic 1 c smile at eight
    with fade
    "It takes us nearly an hour to finally reach the place Alex was trying to lead us to."
    "We end up in a local shrine after crossing a bridge that goes over a little stream."
    "Multicolored leaves are fallen on the concrete steps at the entrance."
    "Unlike the station which was at the center of one of the town's busiest areas, this place is nearly deserted."
    al "\"Here we are.\""
    "Alex motions with his head, pointing at the large wooden gates and the different altars around us."
    vic "\"Wow. A bona fide Shinto shrine. I've always wanted to visit one.\""
    show k 1 c smile at fdis
    k "\"Really? I thought you weren't too big on religion.\""
    vic "\"I'm not, but this is a piece of history right here.\""
    mc 1 c curious "\"Alex, how do you even know this place? It's at one of the edges of the town. Not many people even come here in the first place.\""
    al "\"It's a touristic attraction. You wanted to go someplace \"touristy\" didn't you? This felt appropriate.\""
    k "\"It is appropriate. Thank you, Alex.\""
    "The wolf nods in response."
    vic "\"Wow. The architecture here is magnificent.\""
    k "\"It certainly is a looker. I'm surprised by how well preserved it is.\""
    mc 1 c smile "\"It's a historic monument. Not to mention the shrine still has priests looking after it to this day. It's in no danger of going downhill any time soon.\""
    k "\"That's good to know. People should care more about their history.\""
    "Victor nods enthusiastically, pulling his phone out of his pocket."
    play sound "music/camera.ogg"
    "A mechanical camera sound echoes from it as the fox takes a shot of the scenery."
    mc 1 c "\"Wow. That's an old school camera sound.\""
    vic "\"Oui. I thought it was pretty charming so I configured my camera to make that sound whenever I snap a picture.\""
    k "\"Huh, that's kinda amusing. In Japan our phones make camera sounds that cannot be turned off no matter what. You on the other hand {i}chose{/i} to have a noisy phone camera.\""
    vic "\"You can't? Why not?\""
    mc 1 c "\"It's to stop people from taking pictures of others without permission. The camera sound would let everyone know that a photo was snatched and that keeps people from being sneaky with them.\""
    show k 1 c at fdis
    k "\"I'm pretty sure its mostly to stop perverts from taking upskirt photos of women.\""
    mc 1 c smile "\"And yet some people are still stupid enough to think that a phone that makes no sound is taking a photo of them.\""
    k "\"People will believe whatever they want to believe.\""
    vic "\"That's interesting. I didn't know that.\""
    al "\"Not that it stops people from hacking their phones to turn them off.\""
    k "\"So long as it's not readily available, most people won't have the technical knowhow to do it.\""
    mc 1 c smile "\"Or the patience.\""
    al "\"That is true.\""
    "Victor continues taking pictures of the place, capturing everything from the main gate to the altars to the nearby trees."
    show k 1 c smile at fdis
    k "\"If you want, you can buy a fortune here.\""
    vic "\"I don't really believe that kind of stuff.\""
    mc 1 c considerate "\"I think most people don't believe it. They buy it to help support the temple. It takes money to keep a place like this functioning you know.\""
    vic "\"Oh. In that case then I guess I'm gonna buy one.\""
    "We walk up to a nearby priest in front of a box of fortunes."
    "Priest" "\"Good evening. What brings you all here?\""
    "The man, a tanuki, smiles warmly at us, making a small reverence to welcome us."
    k "\"We're showing our foreign classmate around.\""
    "Priest" "\"Ahhh. And you decided to bring him to our shrine. I am most grateful for that.\""
    vic "\"How does this fortune stuff work again?\""
    "Priest" "\"You make a payment of 5 yen and take a random fortune from the box.\""
    vic "\"5 yen? Wow, that's cheap.\""
    "He opens his wallet, fishing out a coin from inside and handing it to the priest."
    "Priest" "\"Thank you very much.\""
    "Victor puts his hand in the box, shuffling it around for a few seconds before pulling out a folded piece of paper."
    k "\"What does it say?\""
    vic "\"Let me see... Oh, I got a great blessing!\""
    show k 1 c shock at fdis
    k "\"Wow. Those are supposed to be really rare!\""
    mc 1 c curious "\"I've never met anyone who's drawn one.\""
    al "\"What does it say the blessing is for?\""
    vic "\"Let me see. Great blessing with...{w} wait... childbirth?! This can't be right!\""
    show k 2 c gentleb at fdis
    k "\"Pffft, ahahahahahahahaha!\"" with hpunch
    vic "\"Wha- don't laugh at me!\""
    al "\"You'll make a wonderful mother.\""
    vic "\"Not you too!\"" with hpunch
    "Even the priest is trying to keep himself from laughing. He's covering his mouth with his hand and looking away from us."
    vic "\"This is bullshit!\""
    mc 1 c smile "\"Now now, you shouldn't swear in a temple.\""
    vic "\"But...\""
    "Priest" "\"He's right. The shrine is a place of adoration, you should be respectful of it.\""
    play sound "music/disappointment.ogg"
    vic "\"Guh...\""
    show k 1 c smile at fdis
    k "\"After this one, I kinda want to draw a fortune too. See what comes out.\""
    al "\"I suppose I am also interested.\""
    k "\"What about you, [povFirstName]-san? Will you draw one too?\""
    menu:
        "I..."
        "Accept":
            mc 1 c smile "\"Sure. We should all draw one. Hopefully our fortunes don't end up making us pregnant.\""
            vic "\"Hey!\""
            "The three of us hand the priest a 5 yen coin each and grab a piece of paper from inside the box."
            k "\"Alex, why don't you go first?\""
            al "\"Alright.\""
            "He neatly unfolds the piece of paper that is almost too small for his hands."
            al "\"Hmm... I drew a curse for my wishes and future business.\""
            show k 1 c worried at fdis
            k "\"Oh, ouch. That's gotta suck.\""
            "The wolf shrugs, folding the paper back up and putting it in his pocket."
            al "\"You just have to do the best you can with what you have. My fortune is my own to make.\""
            show k 1 c smile at fdis
            k "\"Isn't that a mature outlook to have.\""
            mc 1 c smile "\"Alright, me next!\""
            k "\"Sure. Knock yourself out.\""
            "I check out what is written in my paper."
            "Even though I don't consider myself a religious person, I can't help but feel a little superstitious when it comes to these."
            mc 1 c smile "\"Hey, cool. I drew a great blessing for my love life and my business.\""
            k "\"Wow, two great blessings in one day? Maybe these aren't as rare as we thought.\""
            al "\"Plus, it's good that he drew one that actually makes sense for him.\""
            vic "\"I somehow feel jealous... and I don't even believe in these in the first place.\""
            k "\"It's the rarity effect.\""
            vic "\"What about yours, Keisuke?\""
            show k 1 c at fdis
            k "\"Let's see...\""
            "Kei-kun looks at what is written in his paper."
            show k 1 c shock at fdis
            k "\"Oh wow. I drew the same one as [povFirstName]-san!\""
            mc 1 c shock "\"What? Really?\""
            show k 1 c smile at fdis
            k "\"Yeah. Look. \"Great blessing for your love life and future business\". That's what it says.\""
            al "\"Huh. So I'm the only unlucky one.\""
            show k 2 c gentle at fdis
            k "\"Sorry, Alex.\""
        "Refuse":
            mc 1 c "\"I'll pass. I don't really believe in fortunes.\""
            show k 1 c worried at fdis
            k "\"Aww. That's a shame.\""
            show k 1 c at fdis
            "Kei-kun and Alex both pay the priest and draw their respective fortunes regardless."
            k "\"Alex, why don't you go first?\""
            al "\"Alright.\""
            "He neatly unfolds the piece of paper that is almost too small for his hands."
            al "\"Hmm... I drew a curse for my wishes and future business.\""
            show k 1 c worried at fdis
            k "\"Oh, ouch. That's gotta suck.\""
            "The wolf shrugs, folding the paper back up and putting it in his pocket."
            al "\"You just have to do the best you can with what you have. My fortune is my own to make.\""
            show k 1 c smile at fdis
            k "\"Isn't that a mature outlook to have.\""
            vic "\"At least I'm no longer the worse fortune in the group.\""
            al "\"I'll take a failed business over pregnancy any day.\""
            play sound "music/stab.ogg"
            show vic 1 c smile at shake1
            vic "\"Guh...\""
            vic "\"W-what about yours, Keisuke?\""
            show k 1 c at fdis
            k "\"Let's see...\""
            "Kei-kun looks at what is written in his paper."
            show k 1 c shock at fdis
            k "\"Oh wow. I drew a great fortune too!\""
            mc 1 c shock "\"What? Really?\""
            show k 1 c smile at fdis
            k "\"Yeah. Look. \"Great blessing for your love life and future business\". That's what it says.\""
            al "\"Huh. So I'm the only unlucky one.\""
            show k 2 c gentle at fdis
            k "\"Sorry, Alex.\""
    vic "\"Only unlucky? Hello? Did you even look at my fortune?!\""
    al "\"Don't worry. I'm sure your children will be smart and beautiful.\""
    show vic 1 c smile at jumping
    vic "\"Quit mocking me!\""
    "The wolf smiles deviously. I guess even he has a sense of humor."
    "Priest" "\"You kids can also make a prayer at the altar if you'd like.\""
    vic "\"I think I've had it with religious stuff for the day...\""
    al "\"Don't be like that. If you pray hard enough then maybe the man of your dreams will show up sooner.\""
    show vic 1 c smile at jumping
    show k 2 c gentle at fdis
    vic "\"Shut up, shut up, shut up!\""
    k "\"Hahahaha.\""
    "Victor's face is starting to go red. Whether that's from embarrassment or anger I don't really know."
    mc 1 c smile "\"Careful, Alex. You keep that up and his head might explode.\""
    vic "\"Guh...\""
    show k 1 c smile at fdis
    k "\"How about we go around the temple so you can take a few more pictures of the scenery? The nearby stream is quite pretty too.\""
    vic "\"Yes please...\""
    "We wave goodbye to the priest and walk back out of the temple, going through the entrance arch once again."
    al "\"This place would have been much prettier during the cherry blossom season.\""
    show k 1 c sigh at fdis
    k "\"Ugh, no. I still can't stand those.\""
    al "\"Too bad we're not here for you, are we?\""
    show k 1 c avoid at fdis
    k "\"Fair enough.\""
    show k 1 c at fdis
    vic "\"Oh hey, there are fish in the stream!\""
    show k 1 c smile at fdis
    k "\"I wouldn't be surprised. Everything around here is really well kept. That water is crystal clear, see? It's all very clean.\""
    vic "\"I didn't think you could get so much nature this close to a major city.\""
    k "\"It really depends where you visit. Some organizations are more gung-ho about nature preservation than others.\""
    al "\"The estate is also surrounded by nature.\""
    show k 1 c at fdis
    k "\"That's true. You can't see any other buildings around us. It's a bit lonely, actually.\""
    al "\"I agree. It's why I have an apartment in the city.\""
    vic "\"I don't know. I think I'd prefer a quieter place. I love the countryside.\""
    k "\"I wouldn't really call the estate \"countryside\", but I guess it is far enough removed from the hustle and bustle of the city.\""
    al "\"Yes. I have a hard time relaxing there.\""
    show vic 1 c smile at jumping
    vic "\"Oh, hey, I just remembered. Is there a koi fish pond around here or something of the sorts?\""
    k "\"There might be. Why?\""
    vic "\"Can we go there? I wanna see it. I wanna take a picture of the fish.\""
    show k 1 c smile at fdis
    k "\"Sure. Whatever floats your boat.\""
    "We have fun exploring the temple and its surroundings for a few more hours, leisurely enjoying the company as we go along."
    "Alex's decision to come here certainly paid off as Victor seemed to be entertained the whole time."
    stop music2 fadeout 2.5
    play music "music/night.ogg" fadein 5.0
    scene StationN
    show al 1 u at two
    show k 1 c smile at fdis, five
    show vic 1 c smile at eight
    with fade
    "By the time we reach the station again, the sun has already fully set."
    "The bustle of night life has already begun to increase as more people begin showing up in the area."
    vic "\"Thanks again for the help. I really appreciate it.\""
    k "\"It's no problem. We had fun. Right, guys?\""
    mc 1 c smile "\"Yeah, for sure.\""
    al "\"It was an entertaining day.\""
    "Alex hands the fox the bags he'd been carrying the whole time."
    "Victor beams at him."
    vic "\"Thank you. Sorry for making you carry these for me.\""
    al "\"You did no such thing. I carried them out of my own free will.\""
    vic "\"Anyway, I should get going to my apartment. See you guys again tomorrow.\""
    k "\"Alright. Have a safe trip home.\""
    mc 1 c talk "\"Be careful.\""
    vic "\"I will. Bye bye!\""
    show vic 1 c smile at offscreenright with moveoridis
    show al 1 u at three
    show k 1 c smile at fdis, eight
    with move
    "The fox continues waving at us until he disappears into the crowd and vanishes from our sight."
    mc 1 c smile "\"I should probably get going too. My family is going to worry if I arrive too late at home.\""
    k "\"It would probably be for the best, yeah.\""
    al "\"Keisuke, do you want me to call for the car?\""
    k "\"Yeah, sure.\""
    al "\"I will be right back. I have to go someplace with less noise to make the call. Don't go anywhere.\""
    k "\"Wouldn't dream of it.\""
    show al 1 u at offscreenleft with moveoledis
    show k 1 c smile at fdis, five with move
    "We are suddenly left alone amidst the crowd. Even Alex with all his height soon disappears into the masses."
    k "\"How about we go someplace more quiet too?\""
    mc 1 c fsmile "\"What about Alex?\""
    show k 2 c gentle at fdis
    k "\"He'll be fine. He's a big boy, he can take care of himself.\""
    "You really are sneaky when you want to be, huh?"
    show k 1 c smile at fdis
    "Kei-kun grabs me by the arm, leading me away from the giant group of people."
    "We don't walk very far. Just enough to get us out of the huge crowd in front of the station."
    k "\"This should be enough. My ears were already starting to ring with all those voices.\""
    mc 1 c considerate "\"It's certainly an assault on the senses at times.\""
    show k 1 c wry at fdis
    k "\"Thank you for your help today by the way.\""
    mc 1 c smile "\"Not that you needed it. You did just fine at showing him around without me.\""
    show k 1 c calm at fdis
    k "\"Maybe, but having you around to fall back on definitely helped me stay calm.\""
    show k 1 c worried at fdis
    k "\"I'm pretty sure I'd have gotten lost if you and Alex weren't around so I really appreciate it.\""
    mc 1 c smile "\"Maybe you should be thanking him for it too then.\""
    show k 1 c smile at fdis
    k "\"I will. But Alex also had no choice in the matter. He has to accompany me. You could have very well said no and enjoyed your day by yourself.\""
    mc 1 c happy "\"Pfft. As if I'm the kind of person to do that.\""
    show k 2 c gentle at fdis
    k "\"I suppose that's true.\""
    show k 1 c smile at fdis
    mc 1 c curious "\"By the way, has there been any news on whether your band will get the gym or not?\""
    show k 1 c worried at fdis
    k "\"No. And Urata is being tight-lipped about it too. I tried asking him where we stand and he refused to answer.\""
    mc 1 c "\"Well, he's a stickler for the rules so it's no surprise.\""
    show k 1 c sigh at fdis
    k "\"Having a little flexibility every now and again wouldn't hurt.\""
    mc 1 c suggestive "\"Looks who's talking.\""
    show k 1 c smile at fdis
    k "\"Heh. Yeah, I suppose that's suspicious coming from me.\""
    mc 1 c smile "\"Well, if you'll excuse me, I should be going.\""
    k "\"Alright. I should probably get back before Alex comes back and throws a fit.\""
    mc 1 c considerate "\"Try not to make things too difficult for him will you.\""
    k "\"I make no promises.\""
    mc 1 c smile "\"Good night.\""
    show k 2 c gentle at fdis
    k "\"Good night. See you tomorrow.\""
    scene SkyN with fade
    "I begin my walk home with Kei-kun seeing me off."
    "I can't stop looking at the night sky on the way. For some reason, it really calls my attention today."
    "In this area of the city, it's hard to see the stars at night. Even so, today they really seem to be shining a lot."
    "I feel oddly relaxed on my way home."
    "Guess I had a lot more fun today than I expected."
    "Hmm... I wonder about that stuff Alex said to me at the store."
    "So I mean a lot to Kei-kun huh?"
    "For some reason, the thought of that makes me really happy."
    stop music fadeout 2.5
    $ date = None
    jump Day16_Keisuke
