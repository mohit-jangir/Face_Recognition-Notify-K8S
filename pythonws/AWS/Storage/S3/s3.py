import os
import subprocess
import json

from AWS.Storage.S3 import bucket

def s3():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\" S3 TUI\""
         os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo S3 TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of S3 with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tS3 Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : Buckets
press 2 : Access Points
press 3 : Batch Operations
press 4 : Access analyzer for S3
press 5 : Block Public Access settings for account
press 6 : Storage Lens
press 7 : Feature spotlight
press 8 : AWS Marketplace for S3
press 9 : to go to the base menu
press 10 : to exit

""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             bucket.bucket()
        
         elif int(p)==9:
             break
         elif int(p)==10:
             os.system("tput setaf 1")
             exit()
         else :
                print("entered invalid option")
         os.system("tput setaf 6")
         input("press enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
