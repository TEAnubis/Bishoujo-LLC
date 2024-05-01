label st_KS:

    t "Okay, a Kansas LLC."

    t "This one's very straightforward."

    t "We can get started immediately."

    $ client_name = renpy.input("What's your full name?")

    $ client_name = client_name.strip()

    t "Okay, so that's %(client_name)s."

    $ LLC_name = renpy.input("What's the name for the company you're establishing?")

    $ LLC_name = LLC_name.strip()

    t "Okay, that's %(LLC_name)s. I like it!"

    t "In case you didn't know, your company's name is legally required to have 'LLC' or 'Limited Liability Company' at the end."

    t "And if you haven't already, be sure to check if it's available!"

    t "Next we need your address."

    $ LLC_street = renpy.input("Start with the street address.")

    $ LLC_street = LLC_street.strip()

    t "Okay, that's %(LLC_street)s."

    $ LLC_city = renpy.input("Next, the city it's in.")

    $ LLC_city = LLC_city.strip()

    t "Okay, that's %(LLC_city)s."

    $ LLC_zip = renpy.input("And then finally, the zip code.")

    $ LLC_zip = LLC_zip.strip()

    t "Okay, that's %(LLC_zip)s."

    t "So the full address is %(LLC_street)s in %(LLC_city)s, Kansas, zip code %(LLC_zip)s."

    t "And we're done filling out the form!"

    t "Would you believe it's that easy?"

    python:
        
        import os
        from pypdf import PdfReader, PdfWriter
                
        current_dir = renpy.config.gamedir
        file_path = os.path.join(current_dir, 'forms', 'KansasLLC.pdf')

        reader = PdfReader(file_path)
        writer = PdfWriter()

        page = reader.pages[0]
        fields = reader.get_fields()

        writer.append(reader)

        writer.update_page_form_field_values(
            writer.pages[0],
            {
                "Name of resident agent": client_name,
                "Name of limited liability company": LLC_name,
                "Registered office address": LLC_street,
                "Registered office city": LLC_city,
                "Registered office ip": LLC_zip
            }
        )

        with open("Kansas LLC - filled.pdf", "wb") as output_stream:
            writer.write(output_stream)

        
    t "Now all you need to do is print out this form, sign it, and send it."

    # This ends the game.

    return
