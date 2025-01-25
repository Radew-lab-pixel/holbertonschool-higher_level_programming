#!/usr/bin/python3
""" 5-text_indentation.py """


def text_indentation(text):
    """
    function prints a text with 2 new lines after each of these 
    characters: ., ? and :
    
    
    Args: 
    text : string input
    
    Returns: 
    None
    """
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # text_list = list(text.stript())
    text_list = list(text)
    length = len(text_list)
    
    ref_char = [".", "?", ":"]

    for i in range(0, length, 1):
        print("{}".format(text_list[i]), end="")
        if text_list[i] in ref_char:
            print()  # print two newline
            print()
            # print("\n\n")
            # if (text_list[i + 1]) and (text_list[i + 1] == " "):  # next char is space
            #    text_list[i + 1] = ""  # remove space
               # i += 2
            while (i + 1) < length and text[i + 1] == " ":
                text_list[i + 1] = ""
                i += 1
    # print()

