import sys
import fcntl
import os
import termios
import time


def get_char_keyboard():
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    c = None
    try:
      c = sys.stdin.read(1)
    except IOError: pass

    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)

    return c

def get_char_keyboard_nonblock():
    fd = sys.stdin.fileno()

    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)

    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

    c = None

    try:
      c = sys.stdin.read(1)
    except IOError: pass

    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

    return c

def func():
    for i in range(100):
        print(i)

if __name__ == "__main__":
    while True:
        time.sleep(1)
        print("Woken Up")
        func()
        char = get_char_keyboard_nonblock()
        if char != None and char != "" and char != "\n":
            print(char)
