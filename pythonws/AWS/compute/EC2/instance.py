import os
import subprocess
import json

def instance():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"INSTANCES TUI\""
         os.system("echo {0} | figlet -f mono9 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo INSTANCES TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of Instances with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tInstances Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
\n\n
press 1 : Create Instances
press 2 : Instance Types
press 3 : Launch Templates
press 4 : Spot Requests
press 5 : Savings Plans
press 6 : Reserved Instances
press 7 : Dedicated Hosts
press 8 : Capacity Reservations
press 9 : to launch new instance attaching newly created key pair and security group
press 10 : to go to the base menu
press 11 : to exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
          x=subprocess.getoutput("aws ec2 describe-security-groups --filters Name=tag-key,Values=Name Name=tag-value,Values=menu-sg")
          x=json.loads(x)
          keypairname=input("plz enter ur key pair name : ")
          gid=x["SecurityGroups"][0]["GroupId"]
          cnt=int(input("plz give input how many instances u want to launch : "))
          itag=input("plz give your new os a tag : ")
          os.system("aws ec2 run-instances --security-group-ids {} --instance-type t2.micro --count {} --image-id ami-0e306788ff2473ccb --key-name {} --tag-specifications ResourceType=instance,Tags=['{{Key=Name,Value={} }}'] ".format(gid,cnt,keypairname,itag))
          os.system("tput setaf 2")
          print("\n\n yay,ur new full flash aws instance is launched and ready to use")
          os.system("tput setaf 7")

         elif int(p)==10:
                break
         elif int(p)==11:
            exit()
         else :
                os.system("tput setaf 1")
                print("entered invalid option")
         os.system("tput setaf 6")
         input("\npress Enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
