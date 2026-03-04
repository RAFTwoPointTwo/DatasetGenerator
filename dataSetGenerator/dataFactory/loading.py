from sys import stdout
from time import sleep

def loading(string , time):
    for i in range(time):
        if i % 3 == 0:
            stdout.write(f"\r \033[33m {string} \033[0m .")
        if i % 3 == 1:
            stdout.write(f"\r \033[33m {string} \033[0m ..")
        if i % 3 == 2:
            stdout.write(f"\r \033[33m {string} \033[0m ...")
        sleep(0.4)
