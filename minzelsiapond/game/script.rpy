# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Luxure")
define n = Character("Narrator")
define b = Character("Boss")
define u = Character("???")
define l = Character("Leona")
image LuxRoom = "images/LuxRoom.png"
image Control_Panel = "images/Control_Panel.png"
image Luxure_normal = "images/Luxure.png"
image Boss_normal = "images/Boss.png"
image Leona_normal = "images/Leona.png"
image TBD = "images/TBD.jpg"
# The game starts here.
#show use to show character sprite
#hide to hide png or char
#transform my_small_left:
#xalign           # position horizon
#yalign           # stick vertical
#zoom             #scale size
transform luxure_left:
    xalign 0.2       # position to the left
    yalign 0.2       # stick to the bottom
    zoom 0.75         # scale to 70% of original size
transform luxure_middle:
    xalign 0.5       # horizontal center (0.0 = left, 1.0 = right)
    yalign 0.2       # align bottom of image to bottom of screen
    zoom 0.75         # scale to 50% of original size
transform boss_right:
    xalign 0.8       # position to the left
    yalign 0.8       # stick to the bottom
    zoom 0.35         # scale to 70% of original size
transform Leona_right:
    xalign 0.8       # position to the left
    yalign 0.8       # stick to the bottom
    zoom 0.8         # scale to 70% of original size

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

    u "“Are you kidding me right now!!!”"

    n "A loud voice came through the intercom outside her room and cut off her sentence."

    e "“Oh shit”"

    n "she panicked before starting to rush outside her room and headed into some sort of control room. She found herself inside what looked like a train control room with an angry voice coming through the phone next to the intercom system."
 
    scene Control_Panel with fade

    show Luxure_normal at luxure_left
    show Boss_normal at boss_right

    u "“Finally, you’re here” the voice calms down a bit but still fills with an annoyed tone." 

    e "“Sorry, boss I was…”"

    n "before she can finish her sentence the boss cuts her off"

    u "“I don’t wanna hear it”"

    n "after the boss finishes his sentence the screen on the control panel lights up."

    u "“I want you to pick up someone” the boss said."

    e "“Who is it? A new crew or just a passenger?” she asked while fiddling around with the control panel."

    u "A crew” the  boss answer annoyingly"

    e "“Oh? Who are they? Some kind of historian figure? An alien? Or…”"

    u "“I'll stop you right there” the boss cut in before she could ask more questions."

    e "“But…”"

    u "“No but or anything else. She’ll answer it when you get there”"

    e "“Ay ay captain” she said as she fiddled around with the control a bit more and suddenly the whole room started to move onto the rail the kept building itself into some bubblelike object."

    u "“Don’t call me that” the boss said annoyingly before the whole train disappeared into the bubblelike object."
 
    hide Boss_normal
    show Luxure_normal at luxure_middle

    e "At this point you are probably wondering who I am and what we are traveling in exactly."

    e "Well my name is Luxure, a train conductor and right now we are traveling through space and time itself"

    e "and for the voice that kept scorching at me is [[]], My boss and the last conductor who are now duty of baby sitting me until I got my permit to run this whole thing on my own."

    e "We are the [[]]. We travel around all over space and time to stop the [[]], a crime organization that breaks into another universe and/or time to do their blinding and that causes locals to get lost in another space time or create the monster that we call [[]]."

    e "Which leads to the universe falling apart and wiping everything in that universe from ever existing."

    e "Oh, look like we arrived. Well I guess it's time to hop back into the action. Hope we meet again, Bye."
    
    scene TBD with fade
    show Luxure_normal at luxure_left

    n "After a really long amount of time filled by the voice of [[]] and the boss arguing they finally arrive at what looks like an old run down workshop that hasn't had anyone there for decades."

    e "“Are we in the 1400s?” Luxure asked while walking out of the train and putting an earpiece on."

    b "“That right, and your new crew is in that building ahead” the boss answered through that earpiece."

    n "Luxure slowly walks up to the building ignoring any and everybody giving her weird looks as she walks by. She knocks on the door of the building before she starts fiddling around with the plant outside the building."

    u "“Are you here already?” a soft sulting voice came from the other side of the door before it slowly opened up revealing a small frail girl with long messy yet soft brown hair standing in front of Luxure."

    show Leona_normal at Leona_right

    e "“O-Oh! I didn’t think you'd be this adorable” Luxure stuttering while blushing."

    l "“Thank you for the compliment. Also I’m Leona by the way” the cute girl answered before stepping forward and shaking Luxure’s hand."

    e "“I-I’m Luxure, Nice to be working together” Luxure face turns red while answering with a stuttering voice."

    l "“Well, I think we should go before your tail gathers more attention” Leona said before trying to poke Luxure’s tail."

    e "“Eep!!! Sor-ry. Le-let’s go then” Luxure jumps from the shock of realizing her surroundings before she grabs Leona's hands and starts heading to the training that is hiding just outside the village."

    # — end of prologue —


    # This ends the game.

    return
