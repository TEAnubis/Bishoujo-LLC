# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Tomoko")
define n = Character("Nanami")
define y = Character("Yayoi")
define me = Character("Me")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    "Today's the day!"

    "My first day as an entrepreneur!"

    "Financial freedom, here I come!"

    "Time freedom, here I come!"

    "Business tax write-offs, here I come!"

    scene black

    "Train's not too packed. I think I just missed rush hour."

    "Oh!"

    scene black

    "What a lovely sight..."

    "Three young office ladies, just across the car from me!"

    "They must be on their way to work."

    ""

    scene black

    "Well, that didn't go as planned..."

    "I guess you can't just go into the bank and start a business account."

    "I guess I'll go back and..."

    "Woah!"

    scene black

    "Ow! What happaned?"

    "Oops! I think I ran into someone."

    "Wait a second..."

    "That's one of those office ladies from the train!"

    me "Sorry, miss. Are you alright?"

    t "I'm okay. Sorry, I should watch where I'm going."

    scene black
    show tomoko neutral

    t "Are you hurt at all?"

    me "No, I'm good."

    t "What a relief!"

    t "Sorry I was in such a hurry. I had some forms to drop off at the bank."

    me "Oh, I was just coming from there."

    me "Was gonna start a business account, but I guess I jumped the gun."

    t "Jumped the gun?"

    me "Yeah. They asked me for a bunch of documents I didn't have."

    t "Are you starting a business?"

    me "That was my plan, yeah."

    "Woah!"

    "She has an intense look all of a sudden."

    t "I can help!"
    
    t "Wait here, I'll be just a minute!"

    "She took off running."

    "I hope she doesn't smack into someone else."

    scene black

    t "Okay!"

    t "I'm sorry, I never gave you my name!"

    t "I'm Tomoko, and I help people start businesses!"

    t "If you'd like, we can sit down and talk about your business plans."

    t "It's probably easier than you think."

    t "And our office isn't far away."

    me "I didn't have any other plans today. Sure, why not?"

    scene Office1

    t "Here we are. Welcome to Bishoujo, LLC!"

    show nanami neutral

    n "Tomoko, you're back!"

    "Another one of the ladies from the train!"

    n "And you brought a client?!"

    t "Yep!"

    t "This gentleman is starting a business!"

    n "Welcome!"

    t "This is Nanami. She's our receptionist."

    t "Nanami, is Yayoi around?"

    n "I think went to get some more printer paper from the supply closet."

    n "She's been in there a while..."

    t "Oh, jeez..."

    scene Office2

    show tomoko neutral

    t "Let me go help her out..."



    y "Oh, Nanami! You're back!"

    y "I reorganized the whole supply closet, but I can't find the printer paper."

    t "We moved it out by the printer, remember?"

    y "Oh, you're right, we did!"

    t "But forget that for now, we have a client!"

    y "We do?!"



    t "This is Yayoi. She handles a lot of the special cases."

    "That's the third lady from the train!"

    show yayoi neutral

    y "Welcome! We look forward to helping you."

    scene Office3

    show tomoko neutral

    t "So, let's get started."

    t "First things first..."

    menu:
        t "What time zone do you live in?"

        "Eastern":
            jump tz_est

        "Central":
            jump tz_cen
        
        "Mountain":
            jump tz_mtn

        "Pacific":
            jump tz_pac

        "Alaska":
            jump tz_ask

        "Hawaii":
            jump tz_hwi


    
    # This ends the game.

    return
