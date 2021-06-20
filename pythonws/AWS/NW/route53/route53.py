import os
import subprocess

from AWS.EC2 import ec2

def route53():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AWS Route53 Services\""
         os.system("echo {0} | figlet -f cybermedium -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS ROUTE53 TERMINAL USER INTERFACE FOR COMPUTE | figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS Route53 with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAWS ROUTE53 Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : Hosted zones
press 2 : Health checks
press 3 : Traffic flow
press 4 : Domains
press 5 : Resolver
press 6 : to go to the Base Menu
press 7 : to Exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             hostedzone.hostedzone()

         elif int(p) ==9 :
                break
         elif int(p)==10 :
            exit()
         else:
             os.system("tput setaf 4")
             print("entered invalid option")
             os.system("tput setaf 7")
         os.system("tput setaf 6")    
         input("\n\t\tpress enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
