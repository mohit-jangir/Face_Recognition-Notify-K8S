import os
import subprocess

def iam():
 while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\" IAM TUI\""
         os.system("echo {0} | figlet -f mono9 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS IAM USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of IAM with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tIAM Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : to create iam user
press 2 : to attach user-policy to newly created iam user
press 3 : to generate access key and secret key for this user
press 4 : to create IAM Role
press 5 : to go to the base menu
press 6 : to exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")
         
         if int(p)==1:
          os.system("tput setaf 4")
          username=input("plz give ur new iam user name")
          os.system("aws iam create-user --user-name {}".format(username))
          os.system("tput setaf 2")
          print("\n\n new iam user has been created successfully")
          os.system("tput setaf 7")

         elif int(p)==2:
          os.system("aws iam attach-user-policy --user-name {} --policy-arn arn:aws:iam::aws:policy/PowerUserAccess ".format(username))
          os.system("tput setaf 2")
          print("\n\n user policy has been attached successfully")
          os.system("tput setaf 7")

         elif int(p)==3:
          os.system("tput setaf 6 ")
          print('\n\n\t ATTENTION REQUIRED!!! YOU SHOULD KEEP THESE CREDENTIALS SAFE AND COPIED IN 1 FILE ,FOR UR CONVINIENCE THE OUTPUT IS BY DEFAULT SAVED IN "IAM_CRED_<iam username here(vary as per your choice)>.txt" ')
          os.system("tput setaf 7 ")
          username=input("plz give ur desired username to generate credentials : ")
          os.system("aws iam create-access-key --user-name {0} > IAM_CRED_{0}.pem".format(username))
          os.system("tput setaf 2")
          print("\n\n new access key for this user {} has been generated successfully".format(username))
          os.system("tput setaf 7")
         
         elif int(p)==4:
              cmd=subprocess.getoutput("aws iam create-role --role-name Test-Role \
--assume-role-policy-document file:///pythonws/AWS/SecurityIdentity/Test-Role-Trust-Policy.json")
              print(cmd)
              os.system("tput setaf 2")
              print("\n\n\t IAM Role created successfully")
              os.system("tput setaf 7")

         elif int(p)==5:
                break
         elif int(p)==6:
            exit()
         else :
                os.system("tput setaf 1")
                print("entered invalid option")
         os.system("tput setaf 6")
         input("\n\tpress enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
