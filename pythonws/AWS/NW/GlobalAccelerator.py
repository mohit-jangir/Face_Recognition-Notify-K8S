import os
import subprocess

from AWS.EC2 import ec2

def GlobalAccelerators_query():
             os.system("tput setaf 4")
             print("\n\t\t These are the Enabled Global Accelerators  ")
             os.system("tput setaf 6")
             query=subprocess.getoutput("""aws globalaccelerator list-accelerators \
    --region us-west-2 \
    --query "Accelerators[?Enabled=='true'].{AcceleratorArn:AcceleratorArn,Name:Name}" \
    --output yaml-stream""")
             print(query)
             os.system("tput setaf 5")
             global arn
             arn=input("plz give accelerator-arn : ")
             os.system("tput setaf 6")

def listeners_query():
             os.system("tput setaf 4")
             print("\n\t\t These are the Available Listeners : ")
             os.system("tput setaf 6")
             query=subprocess.getoutput("""aws globalaccelerator list-listeners \
    --accelerator-arn {} --region us-west-2 \
--query "Listeners[].{ListenerArn:ListenerArn,PortRanges:PortRanges[].[join('- ',[FromPort,ToPort])]}"\
                     """)
             print(query)
             os.system("tput setaf 3")
             global arn
             arn=input("\n\tplz give listener-arn : ")
             os.system("tput setaf 5")

def GlobalAccelerator():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AWS GlobalAccelerator Services\""
         os.system("echo {0} | figlet -f cybermedium -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS GlobalAccelerator TERMINAL USER INTERFACE FOR COMPUTE | figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS GlobalAccelerator with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAWS GlobalAccelerator Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : to create Global Accelerator
press 2 : to create listener for Global Accelerator
press 3 : to create EndPoint Group for Global Accelerator
press 4 : to go to the Base Menu
press 5 : to Exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             os.system("tput setaf 5")
             name=input("plz give Global Accelerator Name : ")
             os.system("tput setaf 4")
             tag=input("plz give Global Accelerator Tag : ")
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws globalaccelerator create-accelerator \
    --name {name} \
    --tags Key="Name",Value="{tag}" \
    --region us-west-2')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\n\t\t Global Accelerator created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==2:
             GlobalAccelerators_query()
             cmd=subprocess.getoutput(f'aws globalaccelerator create-listener \
    --accelerator-arn {arn} \
    --port-ranges FromPort=80,ToPort=80 \
    --protocol TCP \
    --region us-west-2')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\n\t\t Global Accelerator Listener created successfully ..... ")
             os.system("tput setaf 7")
             listeners_query()
             region=input("\n\t plz give endpoint-group-region : ")
             os.system("tput setaf 6")
             print("\n\n\t\t\t\t these are the Running Instances  \n")
             os.system("tput setaf 5")
             query=subprocess.getoutput("""aws ec2 describe-instances --query "Reservations[?Instances[?State.Name=='running']].Instances[*].{InstanceId:InstanceId,Tag:Tags[].[join(': ',[Key,Value])]}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 3")
             print("\n\t\t\tif u want to give multiple Instance IDs then give with space")
             os.system("tput setaf 4")
             EndpointId=input("plz give ur EndpointInstanceId : ")
             os.system("tput setaf 6")
             cmd=subprocess.getoutput('aws globalaccelerator create-endpoint-group \
    --listener-arn {arn} \
    --endpoint-group-region {region}\
    --endpoint-configurations EndpointId={EndpointId},Weight=1\
    --region us-west-2')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\n\t\t EndPoint-Group for Global Accelerator created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p) ==4 :
                break
         elif int(p)==5 :
            exit()
         else:
             os.system("tput setaf 4")
             print("entered invalid option")
         os.system("tput setaf 6")    
         input("\n\t\tpress enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
