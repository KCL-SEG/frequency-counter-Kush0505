"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    item1 = items
    for i in range(len(items)):
        if(isinstance(items[i],str)):
            if(can_conv(items[i])):
                j = int(items[i])
                items[i] = j
                print(items[i])
    frequencies = dict.fromkeys(items,0)

    keys = frequencies.keys()
    for i in range(len(items)):
        counter = 0
        if(items[i] in keys):
            key = items[i]
            counter = frequencies.get(key)
            counter+=1
            frequencies.update({key:counter})



    return frequencies

def can_conv(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

