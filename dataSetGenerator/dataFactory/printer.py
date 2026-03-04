from sys import stdout
from time import sleep

def printer(string):
    for char in string:
        stdout.write(char)
        stdout.flush()
        sleep(0.05)
    print()
