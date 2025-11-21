#!/usr/bin/python3
def multiple_returns(sentence):
    d = len(sentence)
    if d == 0 :
        f = "None"
        print("Length: {:d} - First character: {}".format(d, f))
    else:
        f = sentence[0]
        print("Length: {:d} - First character: {}".format(d, f))
