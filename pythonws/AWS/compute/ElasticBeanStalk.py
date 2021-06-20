import os
import subprocess

def app_query():
    os.system("tput setaf 3")
    print("\n These are the Available Applications .... ")
    os.system("tput setaf 6")
    query=subprocess.getoutput("""aws elasticbeanstalk describe-applications \
        --query "Applications[].{ApplicationName:ApplicationName,Description:Description}" \
        --output yaml-stream""")
    print(query)
    os.system("tput setaf 6")

def appversion_query():
    os.system("tput setaf 2")
    print("\n These are the Available App-Versions .... ")
    os.system("tput setaf 6")
    query=subprocess.getoutput("""aws elasticbeanstalk describe-application-versions \
    --query "ApplicationVersions[].{ApplicationName:ApplicationName,VersionLabel:VersionLabel}" \
    --output yaml-stream""")
    print(query)
    os.system("tput setaf 3")

def eb():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"AWS ElasticBeanStalk Services\""
         os.system("echo {0} | figlet -f mono9 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo AWS ElasticBeanStalk TERMINAL USER INTERFACE FOR COMPUTE | figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of AWS ElasticBeanStalk with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tAWS ElasticBeanStalk Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
press 1 : abort-environment-update                  press 2 : apply-environment-managed-action
press 3 : associate-environment-operations-role     press 4 : check-dns-availability
press 5 : compose-environments                      press 6 : create-application
press 7 : create-application-version                press 8 : create-configuration-template
press 9 : create-environment                        press 10 : create-platform-version
press 11 : create-storage-location                  press 12 : delete-application
press 13 : delete-application-version               press 14 : delete-configuration-template
press 15 : delete-environment-configuration         press 16 : delete-platform-version
press 17 : describe-account-attributes              press 18 : describe-application-versions
press 19 : describe-applications                    press 20 : describe-configuration-options
press 21 : describe-configuration-settings          press 22 : describe-environment-health
press 23 : describe-environment-managed-action-history press 24 : describe-environment-managed-actions
press 25 : describe-environment-resources           press 26 : describe-environments
press 27 : describe-events                          press 28 : describe-instances-health
press 29 : describe-platform-version            press 30 : disassociate-environment-operations-role
press 31 : list-available-solution-stacks           press 32 : list-platform-branches
press 33 : list-platform-versions                   press 34 : list-tags-for-resource
press 35 : rebuild-environment                      press 36 : request-environment-info
press 37 : restart-app-server                       press 38 : retrieve-environment-info
press 39 : swap-environment-cnames                  press 40 : terminate-environment
press 41 : update-application                   press 42 : update-application-resource-lifecycle
press 43 : update-application-version               press 44 : update-configuration-template
press 45 : update-environment                       press 46 : update-tags-for-resource
press 47 : validate-configuration-settings          press 48 : wait 
press 49 : to go to the Base Menu                   press 50 : to Exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==6:
            os.system("tput setaf 4") 
            appname=input("\t plz give Application-Name : ")
            os.system("tput setaf 5")
            description=input("\n plz input Application-Description : ")
            os.system("tput setaf 6")
            cmd=subprocess.getoutput(f'aws elasticbeanstalk create-application \
            --application-name {appname} --description {description}')
            print(cmd)
            os.system("tput setaf 2")
            print(f"\n Your Application {appname} created successfully .... ")
            os.system("tput setaf 7")

         elif int(p)==7:
            app_query()
            appname=input("\t plz give Application-Name : ")
            os.system("tput setaf 4")
            version=input("\n plz give Version-Label : ")
            os.system("tput setaf 5")
            description=input("\n plz input App-Version-Description(e.g. MyAppV1) : ")
            os.system("tput setaf 6")
            cmd=subprocess.getoutput(f"aws elasticbeanstalk create-application-version \
            --application-name {appname} --version-label {version} --description {description}")
            print(cmd)
            os.system("tput setaf 2")
            print(f"\n Your Application-Version {appname}:{version} created successfully .... ")
            os.system("tput setaf 7")

         elif int(p)==9:
            app_query()
            appname=input("\t plz give Application-Name : ")
            os.system("tput setaf 4")
            appversion_query()
            version=input("\n plz give Version-Label : ")
            os.system("tput setaf 5")
            env_name=input("\n plz give Environment-Name : ")
            os.system("tput setaf 6")
            cmd=subprocess.getoutput(f'aws elasticbeanstalk create-environment \
            --environment-name {env_name} --application-name {appname} --version-label {version} \
            --solution-stack-name "64bit Amazon Linux 2 v3.1.5 running PHP 7.4"')
            print(cmd)
            os.system("tput setaf 2")
            print(f"\n Your Application-Environment {env_name} created successfully .... ")
            os.system("tput setaf 7")

         elif int(p)==49:
                break
         elif int(p)==50:
            exit()
         else:
             os.system("tput setaf 4")
             print("entered invalid option")
         os.system("tput setaf 6")    
         input("\n\t\tpress enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
