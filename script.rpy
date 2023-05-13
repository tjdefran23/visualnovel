# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

# only used once
define yu = Character("Yukkuri")

define y = Character("Yu")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show yu happy

    # These display lines of dialogue.

    yu "Hi, my name is Yukkuri, but you can call me Yu."

    y "Right now, I'm a sophomore in college, and I'm afraid about what move to make next."

    y "Simply put, I don't know what I want to do with my life."

    y "I mean, I have ideas, but I really don't want to act on them. I just like to think, you know?"

    y "It feels good."
    
    y "What comes next?"

    return
