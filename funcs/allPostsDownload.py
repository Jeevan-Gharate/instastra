try:
    import instaloader
    import sys, os
    from colorama import Fore as F
    import pyfiglet
except:
    print("Some Dependencies are not install properly. Make Sure You Run build.py")
    exec(open('build.py').read())

bot = instaloader.Instaloader()

def banner():
    result = pyfiglet.figlet_format("\t\tInstAstra")
    print(F.BLUE + result)
    login()

print("\n\t\t N.S: YOUR CREDENTIALS AREN'T GOING TO BE LEAKED!, A TEMPORARY SESSION COOKIE WILL BE CREATED FOR FURTHER PROGRAM FUNCTIONING")
print("\n\n\t\t\t\t Do make another instagram profile without 2FA using another phone number!\n")

user_id = input("Enter your instagram username: ")
user_pass = input("Enter your instagram password: ")
print()
insta_profile = input("Enter the Profile name to download posts of: ")
print()
print("This process might take time do co-operate..")

def login():
    try:
        you = bot.login(user=user_id, passwd=user_pass)
        print(F.WHITE+"Login Successful.\n")
        print("\tDownloading Posts.....................\n")
        main()
    except:
        print("Invalid Credentials or 2FA enabled on the ID!")
        sys.exit(1)

def main():
    try:
        bot.download_profile(profile_name=insta_profile)
        print("Downloaded Successfully.")
    except:
        print("Invalid Profile name or Private Profile!")

banner()
