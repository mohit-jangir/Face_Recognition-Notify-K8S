import os
import subprocess

def bucket_query():
          os.system("tput setaf 5")
          print("\n\t\t These are the available S3 Buckets  \n")
          os.system("tput setaf 6")
          query=subprocess.getoutput("""aws s3api list-buckets --query "Buckets[].{Name:Name}" --output yaml-stream""")
          print(query)
          os.system("tput setaf 3")
          global bucket
          bucket=input("plz enter ur Bucket Name : ")
          os.system("tput setaf 2")

def bucket():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"Bucket TUI\""
         os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo Bucket TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of Bucket with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tBucket Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : to create s3 bucket
press 2 : to upload some object file in this s3 bucket
press 3 : to go to the base menu
press 4 : to exit""")
         
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
          bucket_query()
          os.system("aws s3 mb s3://{} --region ap-south-1".format(bucket))
          os.system("tput setaf 2")
          print("\n\n s3 bucket created successfully ")
          os.system("tput setaf 7")

         elif int(p)==2:
          print("for ur convenience, i am listing all the files so that u can filter what to upload in bucket ")
          os.system("\nls\n")
          img=input("plz enter ur object name to upload to s3 bucket")
          os.system("aws s3 cp {} s3://{} --acl public-read ".format(img,bucket))
          os.system("tput setaf 2")
          print("\n\n succcesfully uploaded ur object to s3 bucket")
          os.system("tput setaf 7")

         elif int(p)==3:
             break
         elif int(p)==4:
            exit()
         else :
                os.system("tput setaf 1")
                print("entered invalid option")
         os.system("tput setaf 6")
         input("\n\tpress Enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
