label junstart_0:
    $ uihide = True
    stop music2 fadeout 2.5
    $ junhearts += 1
    scene MusicRoom with fade
    play music2 "music/BGM/On My Way.ogg" fadein 5.0
    play sound "music/slidingdoor.ogg"
    mc 1 u smile "\"Pardon my intrusion!\""
    "I enter the music room without even bothering to knock once."
    "Usually I'd mind my manners but I already know Jun is the only person using this place."
    show j 1 u shock at fdis, five
    j "\"Ah, [povFirstName]-san!\""
    "The small tiger turns around as soon as I announce my presence, looking over his back whilst sitting on the piano's chair."
    show j 1 u watch at fdis
    "Well, I did at least bother to listen outside to see if I wouldn't interrupt him while he's playing."
    "I waited a few minutes until he took a break."
    j "\"What are you doing here?\""
    mc 1 u smile "\"I was feeling a bit bored and decided to drop by.\""
    show j 1 u considerate at fdis
    j "\"You were feeling bored?\""
    mc 1 u happy "\"Yeah. Is that a problem?\""
    show j 1 u watch at fdis
    j "\"No, I'm just surprised. Wouldn't you normally be at practice right now.\""
    mc 1 u curious "\"Oh, you didn't hear? Our courts are being repurposed for the school festival so practice has been canceled until them.\""
    show j 1 u shock at fdis
    j "\"W-wow, I had no idea they did that.\""
    mc 1 u considerate "\"They've been announcing that club activities are being halted all over school for the past week...\""
    show j 1 u wince at fdis
    j "\"O-oh... I didn't know.\""
    "All you had to do was pay attention..."
    mc 1 u smile "\"Anyway, since I don't have anything else to do and I don't feel like heading home so early, I was thinking of coming over to watch you practice.\""
    mc 1 u think "\"Well, if that's okay with you at least.\""
    show j 1 u happy at fdis
    j "\"Of course. I don't mind it at all."
    show j 1 u smile at fdis
    extend " It's fun having you as my audience. I always feel like giving my all!\""
    mc 1 u happy "\"Heh, I'm glad to hear. I guess that makes me your muse, huh?\""
    show j 1 u think at fdis
    j "\"My muse? Hmm...\""
    mc 1 u wince "\"... I was joking. You're not supposed to agree with that!\""
    show j 1 u shock at fdis, jumping
    j "\"Oh!\""
    show j 1 u considerate at fdis
    j "\"O-of course I knew that. Hahaha.\""
    "Seriously, how gullible can you be?"
    "I mean... how embarrassing would it be if someone were to call you their muse?"
    mc 1 u smile "\"Anyway, I just felt like it'd be fun to watch you playing.\""
    mc 1 u happy "\"I'm glad you didn't kick me out. Hehehe.\""
    show j 1 u watch at fdis
    j "\"Why would I kick you out?\""
    mc 1 u considerate "\"I don't know. Some people are very finnicky about their creative process. They don't like being watched while they work or something like that.\""
    show j 1 u think at fdis
    j "\"If I were like that, I wouldn't have invited you guys to watch my performance at the competition either.\""
    mc 1 u think "\"Huh... good point.\""
    mc 1 u curious "\"Actually, about that, there is one thing that I've been sort of curious about lately.\""
    show j 1 u watch at fdis
    j "\"What is it?\""
    mc 1 u curious "\"When's your next competition? I remember you saying that you needed to take part in a lot of them to qualify for the school you want to get into, right?\""
    show j 1 u considerate at fdis
    j "\"... Right.\""
    show j 1 u wince at fdis
    j "\"My next competition is at the end of May... just a little after the school festival...\""
    mc 1 u shock "\"No way. That soon?!\""
    show j 1 u considerate at fdis
    j "\"Yeah... there are five competitions I need to win before the end of the year to have a fighting chance at the school I want to get into. The first two are back to back at the beginning of the year...\""
    show j 1 u wince at fdis
    j "\"I'll have some more breathing room once I've dealt with this second one but until then, I don't have much time to slack off.\""
    mc 1 u wince "\"No wonder you've been so busy lately. I'm sorry, I had no idea.\""
    show j 1 u considerate at fdis
    j "\"It's alright. You don't need to feel bad about it. I'm the one who didn't tell you.\""
    show j 1 u think at fdis
    j "\"To be honest, I'm still nervous about it. Even though I won the last one, I still have the feeling that I just barely made it.\""
    show j 1 u considerate at fdis
    j "\"I didn't really expect to find an incredibly good player in the last competition... and I already know he'll be taking part in this next one too.\""
    mc 1 u curious "\"You mean that lion guy? What was his name again... Akashiro?\""
    show j 1 u watch at fdis
    j "\"Akutagawa.\""
    mc 1 u smile "\"Yeah, that's the one!\""
    mc 1 u "\"You really think he'll be that much of a problem for you?\""
    show j 1 u considerate at fdis
    j "\"You were at the last competition, weren't you? I barely managed to win that one. I don't think I'll be that lucky again...\""
    "I wouldn't really call it luck..."
    mc 1 u "\"But your performance was really great back then and, as far as I'm concerned, I didn't see anyone that I thought was better than you. Even that Akutagawa guy.\""
    j "\"You're giving me too much praise...\""
    show j 1 u wry at fdis
    j "\"To be perfectly honest, I think Akutagawa-kun is already better than me at a technical level.\""
    show j 1 u wince at fdis
    j "\"The only reason I managed to win was because I got lucky enough to have all the judges like my interpretation of the songs.\""
    show j 1 u wry at fdis
    j "\"If we were to clash against each other using only the standard interpretations of our set lists, he'd probably beat me.\""
    mc 1 u shock "\"Is he really that good?\""
    show j 1 u considerate at fdis
    j "\"He's crazy good... believe me, I can tell.\""
    show j 1 u at fdis
    j "\"That's why I've been practicing so much lately. I need to cover the gap between us if I want to have any chance of winning. What matters most in these is technical skill after all.\""
    mc 1 u happy "\"Then why don't you just do the thing you did last time?\""
    show j 1 u shock at fdis
    $ renpy.pause(1.0)
    stop music2 fadeout 2.5
    play music3 "music/BGM/Mischief Maker.ogg" fadein 5.0
    show j 1 u sigh at fdis
    j "\"... Are you stupid?\""
    mc 1 u dismay "\"Huh?\""
    "Did I just get called stupid?"
    "... By Jun of all people?!" with hpunch
    mc 1 u wince "\"I-I don't get it. Is there something wrong about what I said?\""
    j "\"There's nothing {i}right{/i} about what you said.\""
    show j 1 u wince at fdis
    j "\"Individuality is frowned upon on competitions. The fact that all three judges liked my interpretation was just a fluke. If even a single one of them had disliked it, I'd have placed among the bottom barrel.\""
    j "\"That thing I did was just an act of desperation because I knew I wouldn't have any chance of winning otherwise if he played his piece even halfway decent... and he did.\""
    mc 1 u worried "\"Damn... the world of music competitions is a lot more rigid than I thought.\""
    show j 1 u considerate at fdis
    j "\"Tell me about it...\""
    stop music3 fadeout 2.5
    play music2 "music/BGM/Little by Little I Walk.ogg" fadein 5.0
    mc 1 u worried "\"Are you sure you're going to be okay like this? You're not overworking yourself or anything are you?\""
    show j 1 u wry at fdis
    j "\"Please don't give me that... you're sounding just like my parents.\""
    mc 1 u wince "\"You can't blame me for caring...\""
    show j 1 u considerate at fdis
    j "\"I don't. Don't take me wrong, I'm really glad to have people who worry about me. but..."
    show j 1 u wry at fdis
    extend " I'm not made of glass, you know. I'm not gonna break just because of a little stress.\""
    mc 1 u worried "\"... Fair enough.\""
    "I'm still not sure if I'm convinced but... I don't think pushing it would get me anywhere... at least not now."
    "At most, it would just make him mad at me."
    mc 1 u wry "\"Do make sure to take breaks every now and then though. If you don't, I'm gonna bug you about it.\""
    show j 1 u wince at fdis
    j "\"How would you even know if I'm not?\""
    mc 1 u happy "\"Isn't it obvious? I'm gonna be secretly watching you like a ninja. If I catch you overdoing it, I'm gonna drop from the ceiling and give you an earful.\""
    show j 1 u happy at fdis
    j "\"Oh, is that how it is then? Hahaha.\""
    "I'm glad I can still make him laugh."
    "Jun is far too pure to have such a weary look on his face all the time!"
    "I'm gonna make sure he takes care of himself, even if I have be extra fussy to do it."
    mc 1 u smile "\"Oh, right, there was something else I've been meaning to talk to you ab-\""
    "I hear a small thumping sound. When I look for the source of it, I see Jun's fingers drumming his fingers on the piano keys."
    mc 1 u happy "\"Sorry, I'm keeping you from playing aren't I?\""
    show j 1 u shock at fdis
    j "\"Huh?\""
    "Jun's eyes follow my gaze and he notices the way he'd been moving his hand."
    show j 1 u considerate at fdis
    j "\"O-oh, I didn't even notice..."
    show j 1 u wry at fdis
    extend " It's not like I don't enjoy talking to you, it's just...\""
    show j 1 u considerate at fdis
    j "\"I kinda got in the groove a while ago so it feels weird to not be playing right now.\""
    mc 1 u laugh "\"Hahaha, don't worry about it, I totally understand.\""
    mc 1 u smile "\"I came here to watch you play, talking is just a bonus. You don't have to keep chatting if you'd rather play.\""
    show j 1 u wry at fdis
    j "\"But I don't want to blow you off...\""
    mc 1 u smile "\"Don't worry about it. My feelings won't be hurt or anything if you decide that you want to play right now.\""
    show j 1 u think at fdis
    j "\"But...\""
    mc 1 u considerate "\"Seriously, you don't need to fuss over the smallest things. I already told you I'm fine.\""
    show j 1 u watch at fdis
    j "\"Are you sure? I don't mind talking for a bit if you want to.\""
    show j 1 u happy at fdis
    j "\"It's not every day that you come over to visit me after all.\""
    mc 1 u happy "\"Jeez, you're such a good kid. It's liable to bring me to tears.\""
    show j 1 u sigh at fdis
    j "\"[povFirstName]-san, could you not call me a kid? {size=-2}I am older than you, you know...{/size}\""
    mc 1 u considerate "\"Sorry, sorry. I tend to forget about that.\""
    "To be honest, the times when I remember it are few and far between..."
    mc 1 u smile "\"Either way, just continue playing already. You know I'm gonna enjoy watching you play anyway.\""
    show j 1 u wince at fdis
    j "\"Are you sure?\""
    mc 1 u happy "\"Of course I'm sure. I already told you. I love watching you play!\""
    show j 1 u happy at fdis
    j "\"Okay!\""
    show j 1 u smile at fdis
    j "\"I've been practicing the song I'm gonna be playing at my next competition.\""
    show j 1 u happy at fdis
    j "\"I'm not gonna bother telling you the name since you've already proven you don't care to remember them anyway.\""
    "Oh, ouch. Rude."
    "... Or at least it would be if it weren't true."
    "Heh. Not much I can say against that."
    show j 1 u smile at fdis
    j "\"It's a song I've never played in front of you before so I don't think you'd know of it.\""
    show j 1 u happy at fdis
    j "\"Still, I hope you'll enjoy hearing it!\""
    stop music2 fadeout 2.5
    show cg2 with fade
    "Jun adjusts himself in his seat, placing his fingers on the piano keys and preparing himself to start playing."
    "He looks back at me once, as if to ask for confirmation."
    "\"Is it really okay for me to play?\""
    "That's what his eyes are asking me."
    "I smile at him and nod."
    "Nodding back at me, he adjusts himself one more time..."
    play music3 "music/BGM/Classical/Fantaisie Impromptu.ogg" fadein 2.5
    "Jun's fingers begin dancing on top of the keys."
    "It still astounds me how he can be sitting perfectly still one second and then hammering the keys madly on the next."
    "He was right when he said I'd never heard this song before though."
    "Even so, I can already tell that I like it."
    "It's so full of energy and grace. It definitely feels like I'm watching a master practicing his craft."
    "Or... well, at least that's the feeling that I get."
    "I've never seen a real professional pianist before... but I still have a hard time believing there can be someone better than Jun at this."
    "Maybe it's just blatant favoritism but I truly believe he's amazing."
    "From the way he acts all the time, I think I can be forgiven for forgetting that he's also like this."
    "But when he's going at it on the piano... it's hard to think of something more beautiful."
    "I take an empty chair on the first row and merely sit, content to watch the spectacle unfolding in front of my eyes."
    "A spectacle made just for me."
    stop music3 fadeout 2.5
    $ date = None
    jump cs_final