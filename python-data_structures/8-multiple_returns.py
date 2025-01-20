#!/usr/bin/python3


def multiple_returns(sentence):

    if (sentence == ""):
        first = "None"
        length = 0
    else:
        list_sent = list(sentence)
        first = list_sent[0]
        length = len(list_sent)
        # if (length == 0):
        # first = "None"
    return (length, first)
