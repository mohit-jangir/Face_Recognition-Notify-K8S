import os
import subprocess
import json

def updateJsonSimple(name,Type,value):
    with open("record.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        data["Changes"][0]["ResourceRecordSet"]["Name"] =f"{name}"
        data["Changes"][0]["ResourceRecordSet"]["Type"] =f"{Type}"
        data["Changes"][0]["ResourceRecordSet"]["ResourceRecords"][0]["Value"] =f"{value}"
        jsonFile.seek(0)  # rewind
        #json.dump(data, jsonFile)
        jsonFile.write(json.dumps(data,indent=4,sort_keys=True))
        jsonFile.truncate()

def updateJsonWeighted(name,Type,value,weight,identifier):
    with open("weighted.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        data["Changes"][0]["ResourceRecordSet"]["Name"] =f"{name}"
        data["Changes"][0]["ResourceRecordSet"]["Type"] =f"{Type}"
        data["Changes"][0]["ResourceRecordSet"]["ResourceRecords"][0]["Value"] =f"{value}"
        data["Changes"][0]["ResourceRecordSet"]["Weight"] =f"{weight}"
        data["Changes"][0]["ResourceRecordSet"]["SetIdentifier"] =f"{identifier}"
        jsonFile.seek(0)
        jsonFile.write(json.dumps(data,indent=4,sort_keys=True))
        jsonFile.truncate()

def updateJsonAlias(name,Type,hostedzone_id,DNSName):
    with open("alias.json", "r+") as jsonFile:
        data = json.load(jsonFile)
        data["Changes"][0]["ResourceRecordSet"]["Name"] =f"{name}"
        data["Changes"][0]["ResourceRecordSet"]["Type"] =f"{Type}"
        data["Changes"][0]["ResourceRecordSet"]["AliasTarget"]["HostedZoneId"] =f"{hostedzone_id}"
        data["Changes"][0]["ResourceRecordSet"]["AliasTarget"]["DNSName"] =f"{DNSName}"
        jsonFile.seek(0)
        jsonFile.write(json.dumps(data,indent=4,sort_keys=True))
        jsonFile.truncate()

def ec2ip_query():
    os.system("tput setaf 3")
    print("\n\t These are the Running Instances : ")
    os.system("tput setaf 6")
    query=subprocess.getoutput("""aws ec2 describe-instances --filters Name=instance-state-name,Values="running" --query "Reservations[].Instances[].{PublicIpAddress:PublicIpAddress,Instance_Tags:Tags[].[join(': ',[Key,Value])]}" --output yaml-stream""")
    print(query)
    os.system("tput setaf 4")
    public_ip=input("\n plz input Public IP : ")
    return public_ip

def hostedzone_query():
    os.system("tput setaf 4")
    print("\n\t\t These are the Available Hosted-Zones \n ")
    os.system("tput setaf 6")
    query=subprocess.getoutput("""aws route53 list-hosted-zones --query \
        "HostedZones[].{Id:Id,Name:Name,PrivateZone:Config.PrivateZone}" --output yaml-stream""")
    print(query)
    os.system("tput setaf 3")
    hostedzone_id=input("\n\tplz give HostedZone-Id : ")
    os.system("tput setaf 5")
    return hostedzone_id

def hostedzone():
     while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AWS HostedZone Services\""
         os.system("echo {0} | figlet -f cybermedium -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS HostedZone TERMINAL USER INTERFACE FOR COMPUTE | figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS HostedZone with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAWS HostedZone Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : to create a Route53 Public Hosted Zone
press 2 : to create a Route53 Private Hosted Zone
press 3 : to create a simple routing policy Record set
press 4 : to create a weighted routing policy Record set
press 5 : to create a GeoLocation routing policy Record set
press 6 : to create a Failover routing policy Record set
press 7 : to create a Latency routing policy Record set
press 8 : to create a Alias record set in RDS Hosted Zone
press 9 : to create CNAME/PTR/MX/AAA type record
press 10 : to go to the Base Menu
press 11 : to Exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
             os.system("tput setaf 4")
             name=input("\n\t\t plz give Hosted-Zone Name (example.com) : ")
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws route53 create-hosted-zone --name {name} \
                     --caller-reference 2021-02-01-18:47 \
                     --hosted-zone-config Comment="command-line version"')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t\t Your Public Hosted-Zone created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==2:
             os.system("tput setaf 3")
             name=input("\n\t\t plz give Hosted-Zone Name (example.com) : ")
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws route53 create-hosted-zone --name {name} \
                     --caller-reference 2021-02-01-18:47 \
                     --hosted-zone-config Comment="command-line version",PriateZone=true')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t\t Your Private Hosted-Zone created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==3:
             hostedzone_id=hostedzone_query()
             os.system("tput setaf 6")
             name=input("plz give record name : ")
             os.system("tput setaf 4")
             Type=input("plz give record type : ")
             ec2ip_query()
             value=public_ip
             updateJsonSimple(name,Type,value)
             os.system("tput setaf 5")
             cmd=subprocess.getoutput(f'aws route53 change-resource-record-sets \
                     --hosted-zone-id  {hostedzone_id}  --change-batch file://record.json')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t\t Your simple routing policy Record created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==4:
             hostedzone_id=hostedzone_query() 
             os.system("tput setaf 6")
             name=input("plz give record name : ")
             os.system("tput setaf 4")
             Type=input("plz give record type : ")
             ec2ip_query()
             value=public_ip
             os.system("tput setaf 3")
             weight=input("\nPlz give Weight for this Record : ")
             os.system("tput setaf 5")
             identifier=input("\n plz give Identifier/Description : ")
             updateJsonWeighted(name,Type,value,weight,identifier)
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f'aws route53 change-resource-record-sets \
                     --hosted-zone-id {hostedzone_id} --change-batch file://weighted.json')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t\t Your weighted routing policy Record created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==8:
             hostedzone_id=hostedzone_query()
             os.system("tput setaf 6")
             name=input("plz give record name : ")
             os.system("tput setaf 4")
             Type=input("plz give record type : ")
             os.system("tput setaf 3")
             DNSName=input("\n plz give DNSName(ALB-xxxxxxxx.us-west-2.elb.amazonaws.com) : ")
             updateJsonAlias(name,Type,hostedzone_id,DNSName)
             os.system("tput setaf 6")
             cmd=subprocess.getoutput('aws route53 change-resource-record-sets \
                     --hosted-zone-id {hostedzone_id} --change-batch file://alias.json')
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t\t Your Alias record set in RDS Hosted-Zone created successfully ..... ")
             os.system("tput setaf 7")

         elif int(p)==10:
                break
         elif int(p)==11:
            exit()
         else:
             os.system("tput setaf 4")
             print("entered invalid option")
             os.system("tput setaf 7")
         os.system("tput setaf 6")    
         input("\n\t\tpress enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
