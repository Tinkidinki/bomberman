import threading
import time
import inspect
import os
import sys


def check():
    sys.stdout.write("checking is being done"+"\n")

def display():
    sys.stdout.write("displaying is being done"+"\n")

class Thread(threading.Thread):
    def __init__(self, t, *args):
        threading.Thread.__init__(self, target=t, args=args)
        self.start()

lock = threading.Lock()

def stuff():
    with lock:
        caller = inspect.getouterframes(inspect.currentframe())[1][3]
        print ("Inside %s()\n" % caller)
        do_all_checks()
        display()
        time.sleep(2)
        os.system('clear')
        

def player_move():
    while True:
        x = getch()
        #x = sys.stdin.read(1)
        #x = input()      #If I give this instead of getch(), it works fine.
        print("player moves")
        stuff()

def enemy_move():
    while True:
        print("enemy move")
        stuff()

def main():
        p = Thread(player_move)
        e = Thread(enemy_move)

main()


    



