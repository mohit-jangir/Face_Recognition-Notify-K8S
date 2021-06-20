import os
import subprocess
import json

from AWS.DB import db

def rds():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"RDS TUI\""
         os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo RDS TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of EC2 with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tRDS Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
\n\n
press 1 : Databases
press 2 : Query Editor
press 3 : Performance Insights
press 4 : Snapshots
press 5 : Automated backups
press 6 : Reserved instances
press 7 : Proxies
press 8 : Subnet groups
press 9 : Parameter groups
press 10 : Option groups
press 11 : Events
press 12 : Event subscriptions
press 13 : Recommendations
press 14 : Certificate update
press 15 : to go to the base menu
press 16 : to exit

""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             db.db()
        
         elif int(p)==15:
             break
         elif int(p)==16:
            exit()
         else :
                os.system("tput setaf 1")
                print("entered invalid option")
         os.system("tput setaf 6")
         input("\n\tpress enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
