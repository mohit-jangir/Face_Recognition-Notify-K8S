import os
import subprocess
import json

from AWS.DB import rds

def db():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print('\n\n  REMINDER !!! YOU SHOULD RUN "aws configure" CMD ONCE BEFORE USING THIS AUTOMATED MENU SO THAT AWS CAN AUTHENTICATE U ')
         os.system("tput setaf 7")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AWS Database Services\""
         os.system("echo {0} | figlet -f cybermedium -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS DB TERMINAL USER INTERFACE FOR COMPUTE | figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS Database with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAWS Database Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
\n\n
press 1 : RDS
press 2 : DynamoDB
press 3 : ElastiCache
press 4 : Neptune
press 5 : Amazon QLDB
press 6 : Amazon DocumentDB
press 7 : Amazon Keyspaces
press 8 : Amazon Timestream 
press 9 : to go to the Base Menu
press 10 : to Exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             rds.rds()

         elif int(p) ==9 :
                break
         elif int(p)==10 :
            exit()
         else :
                print("entered invalid option")
         input("press enter to keep using this sub-menu : ")
