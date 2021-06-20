import os
import subprocess

from AWS.compute.EC2 import lb

def LaunchTemplate_query():
             os.system("tput setaf 3")
             print("\n\t\t These are the Available LaunchTemplates \n")
             os.system("tput setaf 6")
             query=subprocess.getoutput("""aws ec2 describe-launch-templates --query "LaunchTemplates[].{LaunchTemplateName:LaunchTemplateName,Tags:Tags[].[join(': ',[Key,Value])]}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 5")
             global template_name
             template_name=input("plz give LaunchTemplate name : ")
             os.system("tput setaf 2")

def autosg():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AUTOSG TUI\""
         os.system("echo {0} | figlet -f mono9 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AUTOSG TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AUTOSG with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAuto-Security-Group Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
\n
press 1 : to create launch template
press 2 : to create auto scaling group
press 3 : to create launch configuration
press 4 : to go to the base menu
press 5 : to exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             os.system("tput setaf 5")
             name=input("plz give launch-template-name : ")
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f"aws ec2 create-launch-template \
                     --launch-template-name {name}  --launch-template-data file://AWS/compute/EC2/config.json")
             print(cmd)
             os.system("tput setaf 2")
             print("\n\n\t\t Launch Template created successfully ...... ")
             os.system("tput setaf 7")
         
         elif int(p)==2:
             os.system("tput setaf 4")
             asg_name=input("plz give auto-scaling-group-name : ")
             LaunchTemplate_query()
             version=input("plz give LaunchTemplate Version : ")
             os.system("tput setaf 5")
             print("\n\t\t These are the Active LoadBalancers \n")
             os.system("tput setaf 6")
             query=subprocess.getoutput("""aws elbv2 describe-load-balancers --query "LoadBalancers[?State.Code=='active'].{LoadBalancerName:LoadBalancerName,Type:Type}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 3")
             lbname=input("plz give LoadBalancer Name : ")
             lb.subnet_query()
             min_size=input("plz give Minimum Size : ")
             os.system("tput setaf 4")
             max_size=input("plz give Maximum Size : ")
             os.system("tput setaf 6")
             
             if len(subnet_ids)==1: 
              cmd=subprocess.getoutput(f"aws autoscaling create-auto-scaling-group \
                      --auto-scaling-group-name {name} \
                      --launch-template 'LaunchTemplateName=,Version={version}'  \
                      --load-balancer-names {lbname} --health-check-type ELB \
                      --health-check-grace-period 120 --min-size {min_size} --max-size {max_size} \
                      --vpc-zone-identifier 'subnet_ids[0]'")
             elif len(subnet_ids)==2:
              cmd=subprocess.getoutput(f"aws autoscaling create-auto-scaling-group \
                      --auto-scaling-group-name {name} \
                      --launch-template 'LaunchTemplateName=,Version={version}' \
                      --load-balancer-names {lbname} --health-check-type ELB \
                      --health-check-grace-period 120 --min-size {min_size} --max-size {max_size} \
                      --vpc-zone-identifier 'subnet_ids[0],subnet_ids[1]'")

             elif len(subnet_ids)==3:
              cmd=subprocess.getoutput(f"aws autoscaling create-auto-scaling-group \
                      --auto-scaling-group-name {name} \
                      --launch-template 'LaunchTemplateName=,Version={version}' \
                      --load-balancer-names {lbname} --health-check-type ELB \
                      --health-check-grace-period 120 --min-size {min_size} --max-size {max_size} \
                      --vpc-zone-identifier 'subnet_ids[0],subnet_ids[1],subnet_ids[2]'")
             
             print(cmd)
             os.system("tput setaf 2")
             print("\n\n\t\t Auto-Scaling Group created successfully ...... ")
             os.system("tput setaf 7")

         elif int(p)==4:
                break
         elif int(p)==5:
            exit()
         else :
                os.system("tput setaf 1")
                print("entered invalid option")
         os.system("tput setaf 2")
         input("press enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
