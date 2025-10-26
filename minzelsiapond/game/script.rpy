# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Luxure")
define n = Character("Narrator")
define b = Character("Boss")
define u = Character("???")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene LuxRoom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    n "In the silence of the night when the world falls asleep, There's a young hard working girl alone in her workshop working tirelessly on something that resembles an engine of some sort."

    n "Suddenly there was a sudden flash of a blinding light coming from the machine followed by a voice that sounded similar yet haunting."
    
    u "“wa…ke …up”"

    n "the voice said, but before she had time to react..."

    n "She woke up in a cold sweat."

    e "“That dream again.”"

    n "She said as she began to get up from her bed and headed to the bathroom. The annoyed look in her eyes showed that this isn't her first time seeing that dream."

    e "“Man, my boss is gonna kill me for this”"

    n "she said while brushing her blonde silky hair and looked towards the clock beside the mirror. After that she put on her uniform and started talking to herself"

    e "“I should really get going before…”"

    u "“Are you kidding me right now!!!”"

    n "A loud voice came through the intercom outside her room and cut off her sentence."

    e "“Oh shit”"

    n "she panicked before starting to rush outside her room and headed into some sort of control room. She found herself inside what looked like a train control room with an angry voice coming through the phone next to the intercom system."
    hide LuxRoom
    screen Control_Panel

    u "“Finally, you’re here” the voice calms down a bit but still fills with an annoyed tone." 

    e "“Sorry, boss I was…”"

    n "before she can finish her sentence the boss cuts her off"

    u "“I don’t wanna hear it”"

    n "after the boss finishes his sentence the screen on the control panel lights up."

    u "“I want you to pick up someone” the boss said."

    e "“Who is it? A new crew or just a passenger?” she asked while fiddling around with the control panel."

    u "A crew” the  boss answer annoyingly"
    # This ends the game.

    return
