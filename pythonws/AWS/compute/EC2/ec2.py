import os
import subprocess
import json

from AWS.compute.EC2 import instance
from AWS.compute.EC2 import lb
from AWS.compute.EC2 import autosg
from AWS.compute.EC2 import nwsec
from AWS.compute.EC2 import ebs

def ec2():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print('\n\n  REMINDER !!! YOU SHOULD RUN "aws configure" CMD ONCE BEFORE USING THIS AUTOMATED MENU SO THAT AWS CAN AUTHENTICATE U ')
         os.system("tput setaf 7")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"EC2 TUI\""
         os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo EC2 TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of EC2 with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tEC2 Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
\n\n
press 1 : Instances
press 2 : Images
press 3 : EBS
press 4 : Network & Security
press 5 : Load Balancing
press 6 : Auto Scaling
press 7 : to go to the base menu
press 8 : to exit

""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             instance.instance()
        
         elif int(p)==3:
             ebs.ebs()

         elif int(p)==4:
             nwsec.nwsec()

         elif int(p)==5:
             lb.lb()

         elif int(p)==6:
             autosg.autosg()

         elif int(p)==7:
             break
         elif int(p)==8 :
            exit()
         else :
                print("entered invalid option")
         input("press enter to keep using this sub-menu : ")

