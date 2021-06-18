import sys
import os

print("\n\t\t\tMake Sure You Have Active Internet Connection and 'pip' installed...\n")
try:
    os.system('pip install -r requirements.txt --ignore-installed')
    os.system('pip3 install -r requirements.txt')
except:
    print("It seems Like There is No Internet Connection or something went wrong!! Here's what the error is:\n")
    print("\t\t"+Exception)
