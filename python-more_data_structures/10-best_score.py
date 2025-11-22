#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    values = []
    keys = []
    for k, v in a_dictionary.items():
        keys.append(k)
        values.append(v)
    mvalue = max(values)
    max_index = values.index(mvalue)
    return keys[max_index]
    