try:
    import instaloader
    from instaloader import Instaloader
    import pyfiglet
    import sys
    from colorama import Fore as F
except:
    print("Some Dependencies are not install properly. Make Sure You Run build.py\nRunning build.py")
    exec(open('build.py').read())

ig = instaloader.Instaloader()
dp = input("Enter Profile username to download DP of: ")

def Start():
    result = pyfiglet.figlet_format("\t\tInstAstra")
    print(F.BLUE + result + F.WHITE)
    Download()

def Download():
    try:
        print(F.LIGHTYELLOW_EX+"\n\t\t\tDownloading..............")
        ig.download_profile(dp , profile_pic_only=True)
        print(F.CYAN+"\n\t\t\tDownloaded Successfully."+F.WHITE)
    except:
        print(F.RED+"The profile is invalid !"+F.WHITE)
        sys.exit(1)

Start()
