import os
import subprocess

from AWS.EC2 import ec2

def cloudfront():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AWS CloudFront Services\""
         os.system("echo {0} | figlet -f cybermedium -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS CloudFront TERMINAL USER INTERFACE FOR COMPUTE | figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS CloudFront with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAWS CloudFront Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : Distributions
press 2 : Policies
press 3 : Telemetry
press 4 : Reports & analytics
press 5 : Security
press 6 : Key management
press 7 : to go to the Base Menu
press 8 : to Exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
          bucket_query()
          x=subprocess.getoutput("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(bucket))
          x=json.loads(x)
          x=x['Distribution']['DomainName']
          cloudfront_url="https://{}/{}".format(x,img)
          os.system("tput setaf 2")
          print("\n\n ur cloudfront distribution has been created successfully")
          print("\n\n ur cloudfront url is : {}".format(cloudfront_url))
          print("\n\n plz copy this url as u can use this url in ur web server to display this object by giving this url in webpages for faster content delivery and very less latency all across the world")
          os.system("tput setaf 7")

         elif int(p)==7:
                break
         elif int(p)==8:
            exit()
         else:
             os.system("tput setaf 4")
             print("entered invalid option")
             os.system("tput setaf 7")
         os.system("tput setaf 6")    
         input("\n\t\tpress enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
