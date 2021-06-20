import os

from AWS.compute import compute
from AWS.DB import main
from AWS.Storage import storage
from AWS.SecurityIdentity import iam

def AWS():
 while True:
         os.system("clear")
         os.system("tput setaf 1")
         print('\n\n  REMINDER !!! YOU SHOULD RUN "aws configure" CMD ONCE BEFORE USING THIS AUTOMATED MENU SO THAT AWS CAN AUTHENTICATE U ')
         os.system("tput setaf 7")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\" AWS TUI\""
         os.system("echo {0} | figlet -f mono9 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAWS Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 0 : to configure AWS CLI\t\t    press 1 : Compute Services
press 2 : Storage Services    \t\t    press 3 : Database Services
press 4 : Migration & Transfer Services\t    press 5 : Networking & Content Delivery Services
press 6 : Developer Tools     \t\t    press 7 : Robotics Services
press 8 : Customer Enablement \t\t    press 9 : Blockchain
press 10 : Satellite           \t\t    press 11 : Quantum Technologies
press 12 : Management & Governance\t    press 13 : Media Services
press 14 : Machine Learning     \t    press 15 : Analytics
press 16 : Security, Identity, & Compliance
press 17 : Front-end Web & Mobile\t    press 18 : AR & VR 
press 19 : Application Integration\t    press 20 : AWS Cost Management 
press 21 : Customer Engagement  \t    press 22 : Business Applications 
press 23 : End User Computing   \t    press 24 : Internet of Things
press 25 : Game Development     \t    press 26 : Containers 
press 27 : to go to the base menu\t    press 28 : to exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")
         
         if int(p)==0:
          print("you should be ready with your credentials like access and secret key to use cli \n\n")
          os.system("aws configure")

         elif int(p)==1:
             compute.compute()
 
         elif int(p)==2:
             storage.storage()

         elif int(p)==3:
             main.db()

         elif int(p)==16:
             iam.iam()
         elif int(p) ==27:
                break
         elif int(p)==28:
            exit()
         else :
                print("entered invalid option")
         input("press enter to keep using this sub-menu : ")
