from itertools import zip_longest

def zzip(*iterables):
    return zip_longest(*iterables, fillvalue=0)