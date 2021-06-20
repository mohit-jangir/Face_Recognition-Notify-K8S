import os
import subprocess

from AWS.compute.EC2 import lb

def nwsec():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print('\n\n  REMINDER !!! YOU SHOULD RUN "aws configure" CMD ONCE BEFORE USING THIS AUTOMATED MENU SO THAT AWS CAN AUTHENTICATE U ')
         os.system("tput setaf 7")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AWS TUI\""
         os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/".format(name))
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
\n\n
press 1 : to create key pair
press 2 : to create security group
press 3 : to generate/allocate Elastic IP
press 4 : to release Elastic IP
press 5 : to associate/disassociate Elastic IP
press 6 : to create/delete/modify placement groups
press 7 : to create/delete/modify network interfaces
press 8 : to go to the base menu
press 9 : to exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             keypairname=input("plz enter ur key pair name : ")
             os.system('aws ec2 create-key-pair --key-name {0} --query "KeyMaterial" --output text > {0}.pem'.format(keypairname))
             os.system("chmod 400 {}.pem".format(keypairname))
             os.system("tput setaf 2")
             print("\n\n new key pair created successfully")
             os.system("tput setaf 7")

         elif int(p)==2:
          sg=input("plz enter your desired name to new security group : ")
          os.system('aws ec2 create-security-group --description "allow all" --group-name {} --tag-specifications ResourceType="security-group",Tags=["{{Key=Name,Value=menu-sg}}"]'.format(sg))
          os.system("tput setaf 2")
          print(" \n\n new security group created successfully")
          os.system("tput setaf 7")

         elif int(p)==3:
          os.system("tput setaf 3")
          eip_tag=input("plz give ur new EIP a tag : ")
          os.system("tput setaf 6")
          cmd=subprocess.getoutput(f"aws ec2 allocate-address --tag-specifications ResourceType=elastic-ip,Tags=['{{Key=Name,Value={eip_tag}}}']")
          print(cmd)
          os.system("tput setaf 2")
          print(" \n\n new EIP created successfully")
          os.system("tput setaf 7")

         elif int(p)==4:
             lb.eip_query()
             cmd=subprocess.getoutput(f"aws ec2 release-address --allocation-id {eip_id}")
             print(cmd)
             os.system("tput setaf 2")
             print(" \n\n EIP released successfully")
             os.system("tput setaf 7")

         elif int(p)==5:
             eip_id=lb.eip_query()
             instances=lb.instances_query()
             cmd=subprocess.getoutput(f"aws ec2 associate-address --instance-id {instances[0]} --allocation-id {eip_id}")
             print(cmd)
             os.system("tput setaf 2")
             print(" \n\n EIP associated successfully")
             os.system("tput setaf 7")

         elif int(p) ==8:
                break
         elif int(p)==9:
            exit()
         else :
                print("entered invalid option")
         input("press enter to keep using this sub-menu : ")
