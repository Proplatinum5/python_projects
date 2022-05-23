def banner_text(text: str = " ", screen_width: int = 80) -> None:

    """
    Creates a banner with 2 "*" on both sides of text provided

    :param text: text that will be put into the banner function
        to create the banner.
     default spans "**" on either side
     Typing "*" will print astrics across the screen width
    :param screen_width: The overall width to print in.
    :raises an error if text is outside of screen width - 4
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger then specified width {1}"
                         .format(text, screen_width))
    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width -4)
        output_string = "**{0}**".format(centered_text)
        print(output_string)

banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There;s something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(" ", 60)
banner_text("When you're felling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 60)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)
