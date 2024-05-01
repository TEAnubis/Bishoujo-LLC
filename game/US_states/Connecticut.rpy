label st_CT:

    t "Okay, a Connecticut LLC."

    t "I'll have to call Yayoi in for this one."

    t "This is one of the few states that requires a NAICS number for new LLCs."

    t "I'll have her explain."

    t "Yayoi, can we have your help, please?"

    y "I'll be right there!"

    

    y "Hello again!"

    t "Our client is starting a Connecticut LLC."

    y "Ohh, okay."

    menu:
        y "Do you know about the NAICS system?"

        "Yes":
            jump NAICS
        
        "No":
            jump NAICS_explain

    

        
    # This ends the game.

    return
