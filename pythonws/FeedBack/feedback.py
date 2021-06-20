import os
import subprocess
import random
import json

def feedback():
        pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave2")
        pubip=json.loads(pubip)
        pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
        os.system("tput setaf 1")
        print("it seems you have exited,hope to see u again ")
        os.system("tput setaf 3")
        print("\n\n\t\tREQUEST!!!!! U ARE OUR VALUABLE AND FOREMOST/PRIORITY CUSTOMER/USER ,YOUR FEEDBACK MATTERS FOR US ,PLZ GIVE UR SOME TIME TO GIVE FEEDBACK TO THIS MENU AS UR FEEDBACK WILL KEEP ON MAKING THIS MENU MORE AND MORE USER FRIENDLY : \n\t ")
        os.system("tput setaf 7")
        random1=random.randint(1,100)
        os.system("cat > feedback{}.txt".format(random1))
        print("\n\n\t")
        os.system("scp -i slave1.pem feedback{}.txt ec2-user@{}:/home/ec2-user".format(random1,pubip))
        print("\n\n\t\t your valuable feedback has been reached to us via network,thanks,\n we hope u will come again soon to give us one more chance to serve you more comparatively better")
        
