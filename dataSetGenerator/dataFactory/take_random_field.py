from random import choice

def take_random_field(block):
    if block:
        return choice(block)
    return "NoDataFoundInThisBlock"