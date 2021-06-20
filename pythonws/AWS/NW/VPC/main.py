import os
import subprocess

from AWS.compute.EC2 import lb

def igw_query():
    os.system("tput setaf 4")
    print("\n\t\t These are the Available Internet-Gateways ")
    os.system("tput setaf 6")
    query=subprocess.getoutput("""aws ec2 describe-internet-gateways --query "InternetGateways[?Attachments[?State=='available']].{InternetGatewayId:InternetGatewayId,Tags:Tags[].[join(': ',[Key,Value])],VpcId:Attachments[].VpcId}" --output yaml-stream""")
    print(query)
    os.system("tput setaf 5")
    global igw_id
    igw_id=input("\n\t plz give Internet-Gateway-ID : ")
    os.system("tput setaf 3")
    
def rtb_query():
    os.system("tput setaf 4")
    print("\n\t\t These are the Available Routing-Tables ")
    os.system("tput setaf 6")
    query=subprocess.getoutput("""aws ec2 describe-route-tables --query \
"RouteTables[].{Tags:Tags[].[join(': ',[Key,Value])],RouteTableId:RouteTableId,VpcId:VpcId}"  \
--output yaml-stream""")
    print(query)
    os.system("tput setaf 5")
    global rtb_id
    rtb_id=input("\n\t plz give Route-Table-ID : ")
    os.system("tput setaf 3")

def vpc():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AWS VPC Services\""
         os.system("echo {0} | figlet -f cybermedium -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS VPC TERMINAL USER INTERFACE FOR COMPUTE | figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS VPC with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAWS VPC Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : to create vpc
press 2 : to create subnet in newly created vpc
press 3 : to create internet gateway
press 4 : to attach internet gateway to vpc
press 5 : to create a custom route table and add route in it 
press 6 : to associate route table with subnet
press 7 : to create NAT gateway
press 8 : to modify/enable auto-assign-public-ip attribute for created subnet or to make subnet public
press 9 : to go to the Base Menu
press 10 : to Exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             os.system("tput setaf 5")
             vpcname=input("plz input vpc name/tag : ")
             os.system("tput setaf 3")
             cidr=input("\n\t\t plz give desired cidr-block : ")
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws ec2 create-vpc --cidr-block {cidr} \
            --tag-specifications ResourceType=vpc,Tags=["{{Key=Name,Value={vpcname}}}"]')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t Your VPC created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==2:
             lb.vpc_query()
             os.system("tput setaf 3")
             cidr=input("\n\t\t plz give desired cidr-block : ")
             os.system("tput setaf 5")
             az=input("plz give desired Availability-Zone : ")
             os.system("tput setaf 4")
             subnet_name=input("plz give Subnet-Name/tag : ")
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws ec2 create-subnet --vpc-id {vpc_id} \
    --cidr-block {cidr}--availablity-zone {az} \
    --tag-specifications ResourceType=subnet,Tags=["{{Key=Name,Value={subnet_name}}}"]')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t Your Subnet created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==3:
             os.system("tput setaf 4")
             igw_name=input("plz input Internet-Gateway Name : ")
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws ec2 create-internet-gateway --tag-specifications ResourceType=internet-gateway,Tags=["{{Key=Name,Value={igw_name}}}"]')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t Your Internet-Gateway created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==4:
             lb.vpc_query()
             igw_query()
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws ec2 attach-internet-gateway --vpc-id {vpc_id} --internet-gateway-id {igw_id}')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t Your Internet-Gateway attached successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==5:
             lb.vpc_query()
             os.system("tput setaf 5")
             name=input("\n\t plz give Routing-Table Name/Tag : ")
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws ec2 create-route-table --vpc-id {vpc_id} \
        --tag-specifications ResourceType=route-table,Tags=["{{Key=Name,Value={name}}}"]')
             print(cmd)
             rtb_query()
             os.system("tput setaf 3")
             dest_cidr=input("plz give Destination-Cidr-Block : ")
             igw_query()
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f"aws ec2 create-route --route-table-id {rtb_id} --destination-cidr-block {dest_cidr} --gateway-id {igw_id}")
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t Your Routing-Table created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==6:
             lb.subnet_query()
             rtb_query()
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws ec2 associate-route-table  --subnet-id {subnet_ids[0]} \
                     --route-table-id {rtb_id}')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t Your Routing-Table associated successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==7:
             lb.subnet_query()
             lb.eip_query()
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws ec2 create-nat-gateway --subnet-id {subnet_ids[0]} \
                     --allocation-id {eip_id}')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t Your NAT-GateWay created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==8:
             lb.subnet_query()
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws ec2 modify-subnet-attribute --subnet-id {subnet_ids[0]} --map-public-ip-on-launch')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t Your Subnet modified successfully And Now It's Public ..... ")
             os.system("tput setaf 7")

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
