import sys
from time import sleep
import os
from colorama import Fore as F
import pyfiglet
import platform
import subprocess

clear = lambda: os.system('clear')
cls = lambda: os.system('cls')

def Clear():
    if platform.system() == 'Windows':
        _ = cls()
    else:
        _ = clear()


def start():
    poster = pyfiglet.figlet_format("\t\t\tInstAstra")
    print(F.BLUE + poster)
    print(F.GREEN+"\n\t\t[⁜] Instagram Scraper. All You Need From Instagram Profile")
    print("\t\t\t[⁜] System Info:~", platform.system(), platform.release(), "\n")
    menu()

def menu():
    while True:
        print(F.LIGHTMAGENTA_EX+'''\n
            \t\t1> Instagram Profile Details Extractor.
            \t\t2> Instagram Profile DP Downloader.
            \t\t3> Instagram Profile Stories Downloader.
            \t\t4> Instagram Profile All_Posts Downloader.
            \t\t5> Help.
            \t\t6> Exit.
        \n''')

        operation = input(F.CYAN+"InstAstra >> "+F.WHITE)

        if operation == "1":
            sleep(1)
            Clear()
            os.system("python3 funcs/ProfileDetails.py")

        elif operation == "2":
            sleep(1)
            Clear()
            os.system("python3 funcs/ProfileDPDownload.py")

        elif operation == "3":
            sleep(1)
            Clear()
            os.system("python3 funcs/ProfileStoriesDownload.py")

        elif operation == "4":
            sleep(1)
            Clear()
            os.system("python3 funcs/allPostsDownload.py")

        elif operation == "5":
            sleep(1)
            Clear()
            help()
        elif operation == "6":
            print("See You Again...... :-D ")
            sleep(2)
            sys.exit(1)
        else:
            print("Invlid Options!!")


def help():
    print(F.WHITE+"\n\t[⁜] Type 1 if you want to " + F.YELLOW + "Get Profile Details.." + F.WHITE)
    print("\n\t[⁜] Type 2 if you want to " + F.YELLOW + "Download Profile DP.."+F.WHITE)
    print("\n\t[⁜] Type 3 if you want to " + F.YELLOW + "Download Profile's Stories.."+F.WHITE)
    print("\n\t[⁜] Type 4 if you want to " + F.YELLOW + "Download Profile's all Posts.."+F.WHITE)
    print("\n\t[⁜] Type 6 to exit Program.."+F.WHITE)

start()
