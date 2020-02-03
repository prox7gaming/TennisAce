label keisukestart_3:
    $ uihide = True
    stop music2 fadeout 2.5
    $ keisukehearts += 1
    scene Black with fade
    "I decided to skip the last class before lunch as I was feeling particularly bored today."
    "As soon as I got close to the rooftop's door, however, I began to hear something."
    mc 1 u shock "\"That voice...\""
    "It is, without a doubt, Keisuke's voice."
    "He's singing at the roof for some reason..."
    "It's a song I'd never heard before. A slow ballad that didn't fit in with the rock songs he likes so much."
    "I debate with myself whether I should open the door or not."
    "I don't think he'd like to be interrupted."
    "Hell, he might get really embarrassed that someone managed to hear him singing out here..."
    "But then again, he really shouldn't be skipping class to sing on the roof of all places."
    "... I know. Voice of hypocrisy speaking here."
    scene SRooftop
    show k 1 u shock at fdis, five
    with fade
    play sound "music/metaldoor.ogg"
    play music2 "music/BGM/Snowy Day.ogg" fadein 5.0
    "I open the door to the sight of the hare jumping in surprise, staring at me with shock."
    k "\"Who-"
    show k 1 u sigh at fdis
    extend " Oh, thank God, it's just you. I thought a teacher had heard me singing up here.\""
    mc 1 u "\"Lucky for you, no one can hear you downstairs.\""
    mc 1 u smile "\"Still, pretty ballsy of you to skip class to sing.\""
    show k 1 u avoid at fdis
    k "\"It's not like I'm skipping class {i}to{/i} sing. I just happened to be singing while skipping class.\""
    mc 1 u curious "\"Oh? Then why did you skip? I really can't imagine you of all people doing something like that.\""
    show k 1 u sigh at fdis
    k "\"What the hell kind of image do you have of me? I'm still only a person, you know. I also need a break sometimes.\""
    mc 1 u smile "\"Fair enough. So, what are you up to?\""
    show k 1 u avoid at fdis
    k "\"...\""
    mc 1 u sigh "\"Oh, come on, don't give me the silent treatment now. How much time did I spend helping you these past few days. Spit it out already.\""
    show k 1 u annoyed at fdis
    k "\"Jeez, you're so forceful.\""
    show k 1 u avoid at fdis
    k "\"I'm just... annoyed.\""
    mc 1 u curious "\"Annoyed? Why? Did something happen?\""
    k "\"No. That's the problem.\""
    mc 1 u confused "\"Huh? I think I'm gonna need a little more context here.\""
    show k 1 u sigh at fdis
    k "\"It's just... you've been so helpful to me lately. You've also been treating me so nicely too. Everyone's been treating me so nicely. It's starting to piss me off.\""
    mc 1 u confused "\"Huh? I'm sorry, what? You want us to treat you badly or something?\""
    show k 1 u avoid at fdis
    k "\"No.\""
    mc 1 u sigh2 "\"... I'm just gonna wait until you start making sense.\""
    show k 1 u worried at fdis
    k "\"It's not like... ugh... sorry, my mind's going all over the place. Give me a second to organize my thoughts.\""
    show k 1 u sigh at fdis
    $ renpy.pause(1.0)
    show k 1 u at fdis
    k "\"Okay... I think I'm good.\""
    mc 1 u "\"Great. Mind explaining to me what the hell is happening then?\""
    show k 1 u avoid at fdis
    k "\"... I'm annoyed that everyone has been so nice to me when I've been such a sucky friend. Especially you. You know exactly how much I've been failing as a friend. I know next to nothing about the people I call my friends.\""
    k "\"I just can't understand how you can be so understanding and nice to me after finding out about that.\""
    mc 1 u shock "\"...\""
    mc 1 u sigh2 "\"Jesus, you're a bigger idiot than I thought.\""
    show k 1 u wince at fdis
    k "\"H-huh? What do you mean?\""
    mc 1 u sigh "\"You really think we'd judge you because of that? I already told you, everyone has their own flaws.\""
    mc 1 u "\"All things considered, you're at least aware of it. The only thing that annoys me is that instead of putting in the effort to correct it, you're just sitting here and feeling sorry for yourself.\""
    show k 1 u avoid at fdis
    k "\"Not sparing the barbs now, huh?\""
    mc 1 u smile "\"When did I ever? Don't I always tend to speak my mind?\""
    show k 1 u smile at fdis
    k "\"Oh, really? Is it because you always speak your mind that we constantly have to deal with Urata's cooking?\""
    mc 1 u uncomfortable "\"... No comment.\""
    show k 2 u gentle at fdis
    k "\"Pfft. Didn't know it'd be this easy to defuse you.\""
    mc 1 u smile "\"Hey, you're smiling now. I guess my pep talk worked after all!\""
    show k 1 u smile at fdis
    k "\"You're really bad with words though. Thank God you're pretty.\""
    mc 1 u wince "\"W-what? I'm bad with words? And what do you mean I'm pretty.\""
    show k 2 u gentle at fdis
    k "\"Don't worry about it. I'm just teasing.\""
    show k 1 u at fdis
    k "\"But getting back to seriousness for a moment... are you really okay with me, even though I'm such a crappy friend?\""
    mc 1 u smile "\"You're not a crappy friend. There are lots of good things about you. A few minor flaws don't nullify that.\""
    show k 1 u avoid at fdis
    k "\"Good things? Like what?\""
    mc 1 u considerate "\"You're not really gonna make me list them, are you?\""
    show k 1 u sigh at fdis
    k "\"... No. Sorry. That was a weird question.\""
    mc 1 u smile "\"You worry too much sometimes. You're fun to spend time with and you actually care about other people. What does it matter that you're a bit self absorbed?\""
    show k 1 u avoid at fdis
    k "\"I think saying that I'm \"a bit\" self absorbed is putting it lightly.\""
    mc 1 u happy "\"You'll learn to deal with it.\""
    show k 1 u smile at fdis
    k "\"You're certainly more positive than I am.\""
    mc 1 u smile "\"A positive outlook is key in having a happy life.\""
    k "\"I'll take your word for it.\""
    show k 2 u gentle at fdis
    k "\"Still... thanks. I really feel like you've been cheering me up a lot more than usual recently.\""
    mc 1 u smile "\"That's just because you're finally opening up to me more. And I have to say, I enjoy spending time with the honest Kei-kun I've gotten to see recently.\""
    mc 1 u happy "\"You look a lot better when you're smiling like that. Certainly beats the perpetual scowl you used to have. Hahaha.\""
    show k 1 u avoidb at fdis
    k "\"W-wha? Don't say ridiculous stuff like that as if it were nothing.\""
    mc 1 u curious "\"Huh? I said something ridiculous?\""
    show k 1 u sigh at fdis
    k "\"Ugh... you can be just like Kobayashi sometimes.\""
    mc 1 u curious "\"I don't get it.\""
    show k 1 u avoid at fdis
    k "\"Just forget it.\""
    show k 1 u smile at fdis
    k "\"Still... thanks. Talking to you always makes me feel so much better.\""
    mc 1 u happy "\"You're welcome!\""
    show k 1 u calm at fdis
    "Keisuke looks up at the sky, happily humming a cheerful melody."
    "His voice carries easily through the air, making me feel as if the air around us has gotten lighter."
    "His mood is so infectious through his voice."
    "Even if he's not singing, I can easy see how much more relaxed he is through his humming."
    "Music really is a mysterious thing to me..."
    mc 1 u "\"Oh, I hate to interrupt but I actually have a question.\""
    show k 1 u smile at fdis
    k "\"Ask away.\""
    mc 1 u curious "\"Did you give Alex the present you bought for him yet?\""
    show k 1 u at fdis
    "Not a second after the words leave my mouth, his entire body stiffens up, his smile fading away in a second."
    mc 1 u wince "\"B-bad question?\""
    show k 1 u sigh at fdis
    k "\"No, no. You're fine. Sorry I reacted strangely."
    show k 1 u avoid at fdis
    extend " I did give him the present and apologized as profusely as I could.\""
    mc 1 u curious "\"And?\""
    show k 1 u sigh at fdis
    k "\"He... accepted it. Quite easily, in fact.\""
    mc 1 u happy "\"Oh! That's great news!\""
    show k 1 u avoid at fdis
    k "\"I guess.\""
    mc 1 u confused "\"At the risk of sounding rude... why the hell aren't you happy about it?\""
    show k 1 u sigh at fdis
    k "\"I don't know. I {i}should{/i} be happy. Hell, I should be beside myself that I didn't lose a precious friend of mine. But it was so... easy. It feels so anticlimactic.\""
    mc 1 u suggestive "\"What? Were you expecting for the two of you to start crying and talking about how much you mean to each other while hugging dramatically?\""
    show k 1 u avoidb at fdis
    k "\"...\""
    mc 1 u shock "\"!!!\""
    mc 1 u sigh2 "\"Oh my God, you {i}were{/i} actually expecting that!\""
    k "\"N-no! Not... not exactly at least...\""
    mc 1 u sigh "\"You're a dork.\""
    show k 1 u wince at fdis
    k "\"Guh...\""
    mc 1 u curious "\"So what {i}actually{/i} happened between you two?\""
    show k 1 u avoid at fdis
    k "\"...\""
    show k 1 u sigh at fdis
    k "\"Alex accepted the present, thanked me for it, said he didn't expect me to remember about his collection and told me he always wanted one like that.\""
    mc 1 u confused "\"And that's bad?\""
    show k 1 u avoid at fdis
    k "\"... He then told me that I didn't have to get him anything because it's the thought that counts and then told me he was never mad at me in the first place.\""
    mc 1 u worried "\"Oh... so that whole thing we did when we went looking for a present was... pointless?\""
    show k 1 u sigh at fdis
    k "\"It seems so.\""
    show k 1 u avoid at fdis
    k "\"Now you see why I'm so torn here?\""
    mc 1 u considerate "\"Yup. I'd also have a hard time figuring out what to feel in your shoes.\""
    show k 1 u sigh at fdis
    k "\"Ain't that the truth.\""
    show k 1 u avoid at fdis
    k "\"That's why I came here in the first place. I couldn't focus on my classes because I kept thinking about all of this.\""
    show k 1 u wry at fdis
    k "\"As silly as it may sound, singing usually helps me to calm down so...\""
    mc 1 u happy "\"I don't think it's silly at all.\""
    mc 1 u smile "\"We all have our own ways to decompress.\""
    show k 2 u gentle at fdis
    k "\"I guess that's true.\""
    mc 1 u smile "\"Did it help any? The singing, I mean.\""
    show k 1 u smile at fdis
    k "\"A bit.{w}"
    show k 2 u gentle at fdis
    extend " Not as much as talking to you, though.\""
    play sound "music/heartbeat.ogg"
    "!!!"
    "For some reason, I feel as if my heart suddenly just skipped a beat."
    mc 1 u flustered "\"That's... erm... that's great to hear. I-I'm glad I could help.\""
    show k 1 u at fdis
    k "\"Are you okay? Your voice sounds a bit shaky.\""
    mc 1 u dismayb "\"I-I'm good. I'm great. Better than great, I'm perfect. Yeah, perfect. Perfection!\""
    show k 1 u worried at fdis
    k "\"P-perfection? {size=-2}Are you sure you're okay?{/size}\""
    mc 1 u fsmile "\"Y-yeah. I'm great. I'm p-\""
    show k 1 u sigh at fdis
    k "\"Yeah yeah, perfection. Got it.\""
    "Why am I so nervous?"
    mc 1 u considerate "\"So... how fares the Light Music club?\""
    show k 1 u avoid at fdis
    k "\"That's quite a big leap in topic of conversation.\""
    mc 1 u considerate "\"Sorry...\""
    show k 1 u smile at fdis
    k "\"It's fine. Don't worry about it.\""
    show k 1 u at fdis
    k "\"To answer your question though... things are no different than usual.\""
    mc 1 u wry "\"Have you already worked up the courage to show them your skills?\""
    show k 1 u avoid at fdis
    k "\"... Not even close.\""
    mc 1 u considerate "\"You're as stubborn as ever, I see.\""
    show k 1 u sigh at fdis
    k "\"I'm not stubborn. I'm just not ready for this kind of thing.\""
    mc 1 u smile "\"You really should have more confidence in yourself. I think you're a great singer and guitarist.\""
    show k 1 u avoid at fdis
    k "\"I... thanks...\""
    mc 1 u happy "\"By the way, when do I get to meet your clubmates?\""
    show k 1 u sigh at fdis
    k "\"You're still on that?\""
    mc 1 u "\"What? You promised you'd introduce me to them!\""
    show k 1 u avoid at fdis
    k "\"Yeah, I did... {size=-4}unfortunately.{/size}\""
    mc 1 u sigh "\"I heard that.\""
    show k 1 u shock at fdis
    $ renpy.pause(1.0)
    show k 1 u sigh at fdis
    k "\"S-sorry...\""
    mc 1 u curious "\"What's the problem in letting me meet them?\""
    show k 1 u avoid at fdis
    k "\"I don't even know why you're interested in meeting them in the first place. Do you even know Urata's teammates?\""
    mc 1 u smile "\"Nope. But then again, Shoichi's team doesn't do something as awesome as playing in a band.\""
    show k 1 u sigh at fdis
    k "\"So this is just about the coolness factor?\""
    mc 1 u happy "\"Yup. Bands are super cool.\""
    show k 1 u avoid at fdis
    k "\"... {size=-4}I have to admit, some of them really are cool.{/size}\""
    mc 1 u curious "\"What?\""
    show k 1 u wince at fdis
    k "\"Nothing!\""
    show k 1 u sigh at fdis
    $ renpy.pause(1.0)
    show k 1 u avoid at fdis
    k "\"I... I'll invite you to meet soon. Let me mentally prepare for that first, okay?\""
    mc 1 u curious "\"Mentally prepare? Why do you have to do that?\""
    show k 1 u sigh at fdis
    k "\"Because I know you're gonna use that opportunity to tease me to hell and back.\""
    "Oh!"
    "... He's not wrong."
    mc 1 u considerate "\"Busted, huh?\""
    show k 1 u avoid at fdis
    k "\"You're nothing if not predictable. Sometimes that's not a good thing.\""
    mc 1 u pout "\"Me? Predictable? I take offense to that.\""
    show k 1 u smile at fdis
    k "\"Of course you do. Like I said. Predictable.\""
    mc 1 u shockb "\"Wha- You can't just insult someone and then take their annoyance as proof that they're predictable.\""
    show k 1 u calm at fdis
    k "\"Sure I can. Not only that, I just did~\""
    mc 1 u pout "\"Why you little-\""
    play sound "music/tap.ogg"
    show k 1 u shock at fdis, five:
        ease .2 zoom 1.5 xoffset -30 yoffset 200
    "I lunge at Kei-kun, grabbing him and-"
    mc 1 u happy "\"Feel my fury, rabbit!\""
    show k 2 u gentle at fdis
    k "\"W-wait, I-I'm not a r-rabbi-\""
    show k 2 u gentleb at fdis, shake1
    k "\"Ahahahahahahahaha, I-I can't- I can't b-breathe. Ahahahahaha.\""
    "I begin to tickle him furiously."
    "Something like this would have been unthinkable with the prim and proper Kei-kun from before."
    "But he's become so much more mellow and open with me lately that it doesn't feel weird at all for me to tease him like this."
    "Plus, I used to do this to Shoichi all the time when we were kids."
    "Hell, we still play-wrestle sometimes."
    mc 1 u happy "\"Someone's acting like a brat here. I'm gonna teach you to respect your seniors!\""
    k "\"Ahahahaha, I-I s-surrender. I surrende- Ahahahahaha.\""
    show k 2 u gentleb at fdis, five:
        ease .2 zoom 1.0 xoffset 0 yoffset 0
    "I let him go. Partly because he surrendered and partly because I don't want him to suffocate due to excess laughter."
    mc 1 u happy "\"Are you gonna stop being a brat about taking me to see your club?\""
    show k 1 u wry at fdis
    k "\"I was never acting like a brat, you just don't like the fact that I have reservations.\""
    mc 1 u smile "\"Fair enough. But still, should I give you another round of tickles for good measure?\""
    k "\"I take back what I said. Please spare me.\""
    mc 1 u happy "\"Hehehe.\""
    "Kei-kun and I continue to goof off on the rooftop until the bell sounds for lunch time."
    "I've been having so much fun spending time with him lately."
    "I'm glad he's become more open with me..."
    stop music2 fadeout 2.5
    $ date = None
    jump cs_final