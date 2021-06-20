import os
import subprocess

def vpc_query():
             os.system("tput setaf 6")
             print("\n\n\t\t\t\t these are the available VPCs  \n")
             os.system("tput setaf 3")
             query=subprocess.getoutput("""aws ec2 describe-vpcs --query \
                     "Vpcs[*].{vpcId:VpcId,state:State,default:IsDefault,Tags:Tags[*].[join(': ',[Key,Value])]}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 5")
             global vpc_id
             vpc_id=input("\n\t\t\tgive ur desired vpc-id :  ")
             os.system("tput setaf 6")

def TG_query():
             os.system("tput setaf 5")
             print("\n\n\t\t\t\t these are the available Target Groups  \n")
             os.system("tput setaf 4")
             query=subprocess.getoutput("aws elbv2 describe-target-groups --query 'TargetGroups[*].{TargetGroupName:TargetGroupName,TargetGroupArn:TargetGroupArn}' --output yaml-stream")
             print(query)
             os.system("tput setaf 3")
             global TargetGroupArn
             TargetGroupArn=input("\n\n\t\tplz input Your TargetGroupARN : ")
             os.system("tput setaf 6")

def instances_query():
             os.system("tput setaf 6")
             print("\n\n\t\t\t\t these are the Running Instances  \n")
             os.system("tput setaf 5")
             query=subprocess.getoutput("""aws ec2 describe-instances --query "Reservations[?Instances[?State.Name=='running']].Instances[*].{InstanceId:InstanceId,Tags:Tags[].[join(': ',[Key,Value])]}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 3")
             print("\n\t\t\tif u want to give multiple Instance IDs then give with space")
             os.system("tput setaf 4")
             global instances
             instances=input("\n\n\t\tplz give ur Instance IDs : ")
             os.system("tput setaf 6")
             instances=instances.split(" ")
             return instances
             os.system("tput setaf 3")

def subnet_query():
             os.system("tput setaf 6")
             print("\n\t\tThese are the Available Subnets \n")
             os.system("tput setaf 4")
             query=subprocess.getoutput("""aws ec2 describe-subnets --query "Subnets[?State=='available'].{Tags:Tags[].[join(': ',[Key,Value])],SubnetId:SubnetId,AvailabilityZone:AvailabilityZone}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 3")
             print("\n\t\t\tif u want to give multiple Subnet IDs then give with space")
             os.system("tput setaf 6")
             global subnet_ids
             subnet_ids=input("plz give subnet-id : ")
             subnet_ids=subnet_ids.split(" ")
             os.system("tput setaf 4")

def sg_query():
             os.system("tput setaf 4")
             print("\n\t\tThese are the Available Security-Groups \n")
             os.system("tput setaf 5")
             query=subprocess.getoutput("""aws ec2 describe-security-groups --query "SecurityGroups[].{GroupName:GroupName,GroupId:GroupId,Tags:Tags[].[join(': ',[Key,Value])]}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 3")
             global security_group_id
             security_group_id=input("plz give security-group-id : ")
             os.system("tput setaf 6")

def lbec2_query():
             os.system("tput setaf 4")
             print("\n\t\t These are the Available Load-Balancers : ")
             os.system("tput setaf 6")
             query=subprocess.getoutput("""aws elb describe-load-balancers --query "LoadBalancerDescriptions[].{LoadBalancerName:LoadBalancerName,Instances:Instances[].InstanceId}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 4")
             global lbname
             lbname=input("plz give load-balancer-name : ")
             os.system("tput setaf 6")

def lb_query():
             os.system("tput setaf 3")
             print("\n\t\tThese are the active Load-Balancers  \n")
             os.system("tput setaf 6")
             query=subprocess.getoutput("""aws elbv2 describe-load-balancers --query "LoadBalancers[?State.Code=='active'].{LoadBalancerName:LoadBalancerName,Type:Type,LoadBalancerArn:LoadBalancerArn}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 4")
             global lbarn
             lbarn=input("plz give load-balancer-arn : ")
             os.system("tput setaf 5")
         
def eip_query():
             os.system("tput setaf 6")
             print("\n\t\tThese are the Elastic IPs \n")
             os.system("tput setaf 4")
             query=subprocess.getoutput("""aws ec2 describe-addresses --query "Addresses[*].{AllocationId:AllocationId,Tags:Tags[].[join(': ',[Key,Value])]}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 3")
             global eip_id
             eip_id=input("plz give ur desired Elastic-AllocationId : ")
             return eip_id
             os.system("tput setaf 5")

def lb():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"LB TUI\""
         os.system("echo {0} | figlet -f mono9 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo LB TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of LB with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tLoad Balancer Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : to create target group
press 2 : to register target group with ec2
press 3 : create a Classic Load Balancer
press 4 : Register or deregister EC2 instances for your Classic Load Balancer
press 5 : create a Application Load Balancer
press 6 : create a Network Load Balancer
press 7 : Specify an Elastic IP address for your load balancer
press 8 : to create listener for Load Balancer
press 9 : Add an HTTPS listener with Load Balancer
press 10 : to delete your load balancer
press 11 : to delete your Target Group
press 12 : to go to the base menu
press 13 : to exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             os.system("tput setaf 4")
             TG_tag=input("\n\n\t\tplz give tag name for target group : ")
             os.system("tput setaf 5")
             port=input("\n\nplz give ur target group port number on which the Services are running : ")
             vpc_query()
             cmd=subprocess.getoutput(f"aws elbv2 create-target-group --name {TG_tag} --protocol TCP --port {port} --vpc-id {vpc_id}")
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t\t\tyour target group has been created successfully .... \n")
             os.system("tput setaf 7")

         elif int(p)==2:
             TG_query()
             instances_query()
             for i in instances:
              cmd=subprocess.getoutput(f"\naws elbv2 register-targets --target-group-arn {TargetGroupArn} --targets Id={i}")
             os.system("tput setaf 2")
             print("\n\t\t\tyour targets have been registered successfully with ur target group .... \n")
             os.system("tput setaf 7")

         elif int(p)==3:
             os.system("tput setaf 3")
             lbname=input("\tplz give ur load balancer name : ")
             os.system("tput setaf 5")
             LoadBalancerPort=input("plz give input for LoadBalancerPort : ")
             os.system("tput setaf 2")
             InstancePort=input("plz give input for InstancePort : ")
             sg_query()
             if len(subnet_ids)==1:
              cmd=subprocess.getoutput(f"aws elb create-load-balancer --load-balancer-name {lbname} --listeners 'Protocol=HTTP,LoadBalancerPort={LoadBalancerPort},InstanceProtocol=HTTP,InstancePort={InstancePort}' --subnets {subnet_ids[0]} --security-groups {security_group_id}")
             elif len(subnet_ids)==2:
              cmd=subprocess.getoutput(f"aws elb create-load-balancer --load-balancer-name {lbname} --listeners 'Protocol=HTTP,LoadBalancerPort={LoadBalancerPort},InstanceProtocol=HTTP,InstancePort={InstancePort}' --subnets {subnet_ids[0]} {subnet_ids[1]} --security-groups {security_group_id}")
             elif len(subnet_ids)==3:
              cmd=subprocess.getoutput(f"aws elb create-load-balancer --load-balancer-name {lbname} --listeners 'Protocol=HTTP,LoadBalancerPort={LoadBalancerPort},InstanceProtocol=HTTP,InstancePort={InstancePort}' --subnets {subnet_ids[0]} {subnet_ids[1]} {subnet_ids[2]} --security-groups {security_group_id}")
             print(cmd)
             os.system("tput setaf 2")
             print("Your Classic Load Balancer Has been created successfully .....")
             os.system("tput setaf 7")
         
         elif int(p)==4:
             lbec2_query()
             instances_query()
             if len(instances)==1:
              cmd=subprocess.getoutput(f"aws elb register-instances-with-load-balancer --load-balancer-name {lbname} --instances {instances[0]}")
             elif len(instances)==2:
              cmd=subprocess.getoutput(f"aws elb register-instances-with-load-balancer --load-balancer-name {lbname} --instances {instances[0]} {instances[1]}")
             elif len(instances)==3:
              cmd=subprocess.getoutput(f"aws elb register-instances-with-load-balancer --load-balancer-name {lbname} --instances {instances[0]} {instances[1]} {instances[2]}")
             print(cmd)
             os.system("tput setaf 2")
             print("Your Instances have been registerd with Classic Load Balancer successfully .....")
             os.system("tput setaf 7")
         
         elif int(p)==5:
             os.system("tput setaf 5")
             lbname=input("plz give ALB a name : ")
             subnet_query()
             if len(subnet_ids)==1:
              cmd=subprocess.getoutput(f"aws elbv2 create-load-balancer --name {lbname}  --subnets {subnet_ids[0]} --security-groups {security_group_id}")
             elif len(subnet_ids)==2:
              cmd=subprocess.getoutput(f"aws elbv2 create-load-balancer --name {lbname}  --subnets {subnet_ids[0]} {subnet_ids[1]} --security-groups {security_group_id}")
             elif len(subnet_ids)==3:
              cmd=subprocess.getoutput(f"aws elbv2 create-load-balancer --name {lbname}  --subnets {subnet_ids[0]} {subnet_ids[1]} {subnet_ids[2]} --security-groups {security_group_id}")
             print(cmd)
             os.system("tput setaf 2")
             print("Your Application Load Balancer created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==6:
             os.system("tput setaf 5")
             lbname=input("plz give NLB a name : ")
             subnet_query()
             if len(subnet_ids)==1: 
              cmd=subprocess.getoutput(f"aws elbv2 create-load-balancer --name {lbname} --type network       --subnets {subnet_ids[0]}")
             elif len(subnet_ids)==2:
              cmd=subprocess.getoutput(f"aws elbv2 create-load-balancer --name {lbname} --type network       --subnets {subnet_ids[0]} {subnet_ids[1]}")
             elif len(subnet_ids)==3:
              cmd=subprocess.getoutput(f"aws elbv2 create-load-balancer --name {lbname} --type network       --subnets {subnet_ids[0]} {subnet_ids[1]} {subnet_ids[2]}")
             print(cmd)
             os.system("tput setaf 2")
             print("Your Network Load Balancer created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==7:
             os.system("tput setaf 5")
             lbname=input("plz give NLB a name : ")
             subnet_query()
             eip_query()
             cmd=subprocess.getoutput(f"aws elbv2 create-load-balancer --name {lbname} --type network --subnet-mappings SubnetId={subnet_ids[0]},AllocationId={eip_id}")
             print(cmd)
             os.system("tput setaf 2")
             print("Your Network Load Balancer with specified EIP created successfully ..... ")
             os.system("tput setaf 7")
         
         elif int(p)==8:
             lb_query()
             listener_port=input("plz give listener-port : ")
             TG_query()
             cmd=subprocess.getoutput(f"aws elbv2 create-listener --load-balancer-arn {lbarn} --protocol  TCP --port {listener_port} --default-actions Type=forward,TargetGroupArn={TargetGroupArn}")
             print(cmd)
             os.system("tput setaf 2")
             print("Your HTTP Listener created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==9:
             os.system("aws elbv2 create-listener --load-balancer-arn loadbalancer-arn --protocol HTTPS --port 443  --certificates CertificateArn=certificate-arn --default-actions Type=forward,TargetGroupArn=targetgroup-arn")
 
         elif int(p)==10:
             lb_query()
             cmd=subprocess.getoutput(f"aws elbv2 delete-load-balancer --load-balancer-arn {lbarn}")
             print(cmd)
             os.system("tput setaf 2")
             print("Your Load Balancer deleted successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==11:
             TG_query()
             cmd=subprocess.getoutput(f"aws elbv2 delete-target-group --target-group-arn {TargetGroupArn}")
             print(cmd)
             os.system("tput setaf 2")
             print("Your TargetGroup deleted successfully ..... ")
             os.system("tput setaf 7")

         elif int(p) == 12 :
                break
         elif int(p)==13 :
            exit()
         else :
                os.system("tput setaf 5")
                print("\n\t\tentered invalid option")
                os.system("tput setaf 7")
         os.system("tput setaf 6")
         input("\n\n\tpress enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
