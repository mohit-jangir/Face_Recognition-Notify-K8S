import os
import subprocess

from AWS.Storage.S3 import s3

def storage():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AWS Storage Services\""
         os.system("echo {0} | figlet -f cybermedium -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS Storage TERMINAL USER INTERFACE FOR COMPUTE | figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS Storage with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAWS Storage Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : S3
press 2 : EFS
press 3 : FSx
press 4 : S3 Glacier
press 5 : Storage Gateway
press 6 : AWS Backup
press 7 : to go to the Base Menu
press 8 : to Exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             s3.s3()

         elif int(p)==7:
                break
         elif int(p)==8:
            exit()
         else :
                os.system("tput setaf 1")
                print("entered invalid option")
         os.system("tput setaf 6")
         input("\n\tpress enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
