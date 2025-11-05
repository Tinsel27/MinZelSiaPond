# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Luxure")
define n = Character("Narrator")
define b = Character("Custos")
define u = Character("???")
define l = Character("Leona")
#IN = INACTIVE
image LuxRoom = "images/LuxRoom.png"
image Control_Panel = "images/Control_Panel.png"
image Luxure_normal = "images/characters/Lux_Neutral.png"
image Luxure_normalIN = "images/characters/Lux_Neutral_In.png"
image Luxure_blush = "images/characters/Lux_Blush.png"
image Luxure_blushIN = "images/characters/Lux_Blush_In.png"
image Boss_normal = "images/characters/Boss_Neutral.png"
image Boss_normalIN = "images/characters/Boss_Neutral_In.png"
image Boss_worry = "images/characters/Boss_Worry.png"
image Boss_worryIN = "images/characters/Boss_Worry_In.png"
image Boss_angry = "images/characters/Boss_Angry.png"
image Boss_angryIN = "images/characters/Boss_Angry_In.png"
image Boss_annoyed = "images/characters/Boss_Annoyed.png"
image Boss_annoyedIN = "images/characters/Boss_Annoyed_In.png"
image Leona_normal = "images/characters/Leona_neutral.png"
image Leona_normalIN = "images/characters/Leona_neutral_In.png"
image Leona_laugh = "images/characters/Leona_laugh.png"
image Leona_laughIN = "images/characters/Leona_laugh_In.png"
image Leona_awaken = "images/characters/Leona_awaken.png"
image Leona_awakenIN = "images/characters/Leona_awaken_In.png"
image TBD = "images/TBD.jpg"
# The game starts here.
#show use to show character sprite
#hide to hide png or char
#transform my_small_left:
#xalign           # position horizon
#yalign           # stick vertical
#zoom             #scale size
transform luxure_left:
    xalign 0.1       # position to the left
    yalign -0.25      # stick to the bottom
    zoom 1         # scale
transform luxure_middle:
    xalign 0.5       # horizontal center (0.0 = left, 1.0 = right)
    yalign -0.2       # align bottom of image to bottom of screen
    zoom 1.2         # scale
transform boss_right:
    xalign 0.8       # position to the left
    yalign 0.8       # stick to the bottom
    zoom 0.5         # scale 50%
transform Leona_right:
    xalign 1.0      # position to the left
    yalign 0.1      # stick to the bottom
    zoom 1         # scale

define shortfade = Fade(0.2, 0.0, 0.2)
#Fade for changing bg scene

label start:
    scene LuxRoom

    n "In the silence of the night when the world falls asleep, There's a young hard working girl alone in her workshop working tirelessly on something that resembles an engine of some sort."

    n "Suddenly there was a sudden flash of a blinding light coming from the machine followed by a voice that sounded similar yet haunting."
    
    u "“wa…ke …up”"

    n "the voice said, but before she had time to react..."

    n "She woke up in a cold sweat."
    
    show Luxure_normal at luxure_left

    e "“That dream again.”"
    
    n "She said as she began to get up from her bed and headed to the bathroom. The annoyed look in her eyes showed that this isn't her first time seeing that dream."

    e "“Man, my boss is gonna kill me for this”"

    n "she said while brushing her blonde silky hair and looked towards the clock beside the mirror. After that she put on her uniform and started talking to herself"

    e "“I should really get going before…”"

    show Luxure_normalIN at luxure_left

    u "“Are you kidding me right now!!!”"

    n "A loud voice came through the intercom outside her room and cut off her sentence."
    
    hide Luxure_normalIN
    show Luxure_normal at luxure_left

    e "“Oh shit”"

    n "she panicked before starting to rush outside her room and headed into some sort of control room. She found herself inside what looked like a train control room with an angry voice coming through the phone next to the intercom system."
 
    scene Control_Panel with fade

    hide Luxure_normal
    show Luxure_normalIN at luxure_left
    show Boss_annoyed at boss_right

    u "“Finally, you’re here” the voice calms down a bit but still fills with an annoyed tone." 

    hide Luxure_normalIN
    hide Boss_annoyed
    show Luxure_normal at luxure_left
    show Boss_annoyedIN at boss_right

    e "“Sorry, boss I was…”"

    n "before she can finish her sentence the boss cuts her off"

    hide Luxure_normal
    hide Boss_annoyedIN
    show Luxure_normalIN at luxure_left
    show Boss_annoyed at boss_right

    u "“I don’t wanna hear it”"

    n "after the boss finishes his sentence the screen on the control panel lights up."

    u "“I want you to pick up someone” the boss said."

    hide Luxure_normalIN
    hide Boss_annoyed
    show Luxure_normal at luxure_left
    show Boss_annoyedIN at boss_right

    e "“Who is it? A new crew or just a passenger?” she asked while fiddling around with the control panel."

    hide Luxure_normal
    hide Boss_annoyedIN
    show Luxure_normalIN at luxure_left
    show Boss_annoyed at boss_right

    u "A crew” the  boss answer annoyingly"

    hide Luxure_normalIN
    hide Boss_annoyed
    show Luxure_normal at luxure_left
    show Boss_annoyedIN at boss_right

    e "“Oh? Who are they? Some kind of historian figure? An alien? Or…”"

    hide Luxure_normal
    hide Boss_annoyedIN
    show Luxure_normalIN at luxure_left
    show Boss_normal at boss_right

    u "“I'll stop you right there” the boss cut in before she could ask more questions."

    hide Luxure_normalIN
    hide Boss_normal
    show Luxure_normal at luxure_left
    show Boss_normalIN at boss_right

    e "“But…”"

    hide Luxure_normal
    hide Boss_normalIN
    show Luxure_normalIN at luxure_left
    show Boss_normal at boss_right

    u "“No but or anything else. She’ll answer it when you get there”"

    hide Luxure_normalIN
    hide Boss_normal
    show Luxure_normal at luxure_left
    show Boss_normalIN at boss_right

    e "“Ay ay captain” she said as she fiddled around with the control a bit more and suddenly the whole room started to move onto the rail the kept building itself into some bubblelike object."

    hide Luxure_normal
    hide Boss_normalIN
    show Luxure_normalIN at luxure_left
    show Boss_annoyed at boss_right

    u "“Don’t call me that” the boss said annoyingly before the whole train disappeared into the bubblelike object."
 
    hide Luxure_normalIN
    hide Boss_annoyed
    show Luxure_normal at luxure_middle

    e "At this point you are probably wondering who I am and what we are traveling in exactly."

    e "Well my name is Luxure, a train conductor and right now we are traveling through space and time itself"

    e "and for the voice that kept scorching at me is Custos, My boss and the last conductor who are now duty of baby sitting me until I got my permit to run this whole thing on my own."

    e "We are the Gardiens. We travel around all over space and time to stop the Mesites, a crime organization that breaks into another universe and/or time to do their blinding and that causes locals to get lost in another space time or create the monster that we call Fisser.."

    e "Which leads to the universe falling apart and wiping everything in that universe from ever existing."

    e "Oh, look like we arrived. Well I guess it's time to hop back into the action. Hope we meet again, Bye."
    
    hide Luxure_normal

    scene TBD with fade
    show Luxure_normalIN at luxure_left

    n "After a really long amount of time filled by the voice of Luxure and the boss arguing they finally arrive at what looks like an old run down workshop that hasn't had anyone there for decades."

    hide Luxure_normalIN
    show Luxure_normal at luxure_left

    e "“Are we in the 1400s?” Luxure asked while walking out of the train and putting an earpiece on."

    b "“That right, and your new crew is in that building ahead” the boss answered through that earpiece."

    n "Luxure slowly walks up to the building ignoring any and everybody giving her weird looks as she walks by. She knocks on the door of the building before she starts fiddling around with the plant outside the building."
    
    u "“Are you here already?” a soft sulting voice came from the other side of the door before it slowly opened up revealing a small frail girl with long messy yet soft brown hair standing in front of Luxure."

    hide Luxure_normal
    show Luxure_blush at luxure_left
    show Leona_normalIN at Leona_right

    e "“O-Oh! I didn’t think you'd be this adorable” Luxure stuttering while blushing."

    hide Luxure_blush
    hide Leona_normalIN
    show Luxure_blushIN at luxure_left
    show Leona_normal at Leona_right

    l "“Thank you for the compliment. Also I’m Leona by the way” the cute girl answered before stepping forward and shaking Luxure’s hand."

    hide Luxure_blushIN
    hide Leona_normal
    show Luxure_blush at luxure_left
    show Leona_normalIN at Leona_right

    e "“I-I’m Luxure, Nice to be working together” Luxure face turns red while answering with a stuttering voice."

    hide Luxure_blush
    hide Leona_normalIN
    show Luxure_blushIN at luxure_left
    show Leona_normal at Leona_right

    l "“Well, I think we should go before your tail gathers more attention” Leona said before trying to poke Luxure’s tail."

    hide Luxure_blushIN
    hide Leona_normal
    show Luxure_blush at luxure_left
    show Leona_normalIN at Leona_right

    e "“Eep!!! Sor-ry. Le-let’s go then” Luxure jumps from the shock of realizing her surroundings before she grabs Leona's hands and starts heading to the training that is hiding just outside the village."

    hide Luxure_blush
    hide Leona_normalIN

    # — end of prologue —
    #chapter start image will be added in future
    #start of Chapter 1

    n "sometime after picking up leona..."

    show Luxure_normal at luxure_left

    e "I wonder how she’s doing right now."
    
    e "I should probably go check on her."

    hide Luxure_normal
    show Luxure_normalIN at luxure_left

    n "Luxure starts walking toward the guest room on the train and knocks on the door."

    hide Luxure_normalIN
    show Luxure_normal at luxure_left

    e "Hey Leona, I wonder if I can come in and talk for a sec?"

    hide Luxure_normal
    show Luxure_normalIN at luxure_left
    show Leona_normal at Leona_right

    l "Yeah, why not. I was just finished settling in"

    hide Leona_normal
    show Leona_normalIN at Leona_right

    n "Luxure opened the door revealing a room filled with blueprints and art supplies."

    hide Luxure_normalIN
    show Luxure_normal at luxure_left

    e "Nice room. How’s the train been treating you so far?"

    hide Luxure_normal
    hide Leona_normalIN
    show Luxure_normalIN at luxure_left
    show Leona_normal at Leona_right

    l "It is nice although I was not familiar with all of this technology. you know being in 1400s and all"

    l "Oh, and what do you want to talk to me about?"

    hide Luxure_normalIN
    hide Leona_normal
    show Luxure_normal at luxure_left
    show Leona_normalIN at Leona_right

    e "I just thought I could introduce myself again because… Well the first time we met I was… caught off guard a bit"

    hide Luxure_normal
    hide Leona_normalIN
    show Luxure_normalIN at luxure_left
    show Leona_normal at Leona_right

    l "Hahaha… you know that you looks really adorable when you blushing righ"

    hide Luxure_normalIN
    hide Leona_normal
    show Luxure_normal at luxure_left
    show Leona_normalIN at Leona_right

    e "Eh… don’t tease me like that please. I was trying to be formal for this"

    hide Luxure_normal
    hide Leona_normalIN
    show Luxure_normalIN at luxure_left
    show Leona_normal at Leona_right

    l "Sorry…sorry I stop. But I gotta admit it was kinda fun to tease you like that"

    hide Luxure_normalIN
    hide Leona_normal
    show Luxure_normal at luxure_left
    show Leona_normalIN at Leona_right

    e "Ahem…so, welcome to the Gardiens. My name is Luxure, the conductor of this train"

    e "Luxure “And you will be working as an officer for the Gardiens.”"
    
    hide Luxure_normal
    hide Leona_normalIN
    show Luxure_normalIN at luxure_left
    show Leona_normal at Leona_right

    l "So I will get a cool uniform too right?"

    l "I'm kinda bored with my outfit right now."

    hide Luxure_normalIN
    hide Leona_normal
    show Luxure_normal at luxure_left
    show Leona_normalIN at Leona_right

    e "Yep, the higher will provide you with a uniform that you can modifile to your liking"

    e "But first you need to go through a training program to see where you fit into the corp."

    hide Luxure_normal
    hide Leona_normalIN
    show Luxure_normalIN at luxure_left
    show Leona_normal at Leona_right

    l "Ooh…that sounds interesting. Can we do that today?"

    hide Luxure_normalIN
    hide Leona_normal
    show Luxure_normal at luxure_left
    show Leona_normalIN at Leona_right

    e "I mean… I can ask the boss to arrange that for you."

    e "Do you want to come along?"

    hide Luxure_normal
    hide Leona_normalIN
    show Luxure_normalIN at luxure_left
    show Leona_normal at Leona_right

    l "I can?"

    l "Yeah, Glad that I can speak with boss again"

    hide Leona_normal
    show Leona_normalIN at Leona_right

    n "The two start walking toward the control room while chatting along the way…"

    hide Luxure_normalIN
    hide Leona_normalIN
    show Luxure_normal at luxure_left

    e "“Hey boss, How you doing?” Luxure shouted while bursting through the door with Leona behind her."

    hide Luxure_normal
    show Luxure_normalIN at luxure_left
    show Boss_normal at boss_right

    b "What do you want this time?"
    
    hide Boss_normal
    hide Luxure_normalIN
    show Boss_normalIN at boss_right
    show Luxure_normal at luxure_left

    e "Rude… Ignoring my question like that"

    e "Anyway, It’s not me this time. Leona wants to go through a training program."

    hide Boss_normalIN
    hide Luxure_normal
    show Luxure_normalIN at luxure_left
    show Boss_normal at boss_right

    b "Well, Ok then. Set your destination to the HQ and we can start this right away."

    hide Boss_normal
    hide Luxure_normalIN
    show Luxure_normal at luxure_left

    e "“Sit tight alright girl.” Luxure speaks as she walks Leona to a chair in the room."

    hide Luxure_normal
    show Luxure_normalIN at luxure_left
    show Leona_normal at Leona_right

    l "“O…ok” Leona sits down and starts looking outside the train while Luxure sings in the background."

    hide Luxure_normalIN
    hide Leona_normal

    #*Start Tutorial Fight*
    #*End Tutorial Fight*

    n "After passing a training program Luxure and Leona get onto the train and go rest in their own room."

    n "The next moring…"

    show Luxure_normal at luxure_left

    e "*Yawn*"

    e "I wonder what HQ's gonna have in store for us today."

    e "“Well. I guess it's best to go wake Leona up for work.” Luxure dressed up and walked towards Leona’s room before inviting her to go look up details of their first operation together."

    hide Luxure_normal
    show Luxure_normalIN at luxure_left
    show Boss_normal at boss_right

    b "Glad to see you both excited for the job."

    hide Boss_normal
    hide Luxure_normalIN
    show Boss_normalIN at boss_right
    show Luxure_normal at luxure_left

    e "Well normally I didn’t get to do the operation that much."

    e "So it feels kinda like the highlight of my job"

    e "And this is the first operation with a partner too. So it was extra special."

    hide Boss_normalIN
    hide Luxure_normal
    show Boss_normal at boss_right
    show Luxure_normalIN at luxure_left

    b "Well then, your first operation together will be clearing out Fisser that are stuck in the void"

    hide Boss_normal
    hide Luxure_normalIN
    show Luxure_normal at luxure_left

    e "Looked like we got an interesting one."
    
    show Leona_normalIN at Leona_right

    e "Are you ready Leona?"

    hide Leona_normalIN
    hide Luxure_normal
    show Leona_normal at Leona_right
    show Luxure_normalIN at luxure_left

    l "Mm.. I just hope that I’m not gonna disappoint you."

    hide Leona_normal
    hide Luxure_normalIN
    show Leona_normalIN at Leona_right
    show Luxure_normal at luxure_left

    e "Trust me after what I saw yesterday, you’ll do great"

    hide Leona_normalIN
    hide Luxure_normal
    show Luxure_normalIN at luxure_left
    show Boss_annoyed at boss_right

    b "Enough chit-chat. Let’s head to the operation zone."

    hide Luxure_normalIN
    hide Boss_annoyed
    #*First Fight Start*
    #*First Fight End*

    show Luxure_normal at luxure_left
    show Leona_normalIN at Leona_right

    e "Well, that was quite something"

    e "How are you holding up leona?"

    hide Luxure_normal
    hide Leona_normalIN
    show Luxure_normalIN at luxure_left
    show Leona_normal at Leona_right

    l "I’m fine… just a bit exhausted."

    hide Luxure_normalIN
    hide Leona_normal
    show Luxure_normal at luxure_left
    show Leona_normalIN at Leona_right

    e "Well, I guess we should head back and get some rest."

    e "A warm shower sounds really good right now."

    n "After the Operation ended Luxure and Leona chatted while heading back to the train."

    # This ends the game.

    return
