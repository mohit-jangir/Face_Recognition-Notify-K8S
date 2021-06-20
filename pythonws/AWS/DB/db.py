import os
import subprocess

def db_query():
             os.system("tput setaf 4")
             print("\n\t\t These are the Available DB-Instances : ")
             os.system("tput setaf 6")
             query=subprocess.getoutput("""aws rds describe-db-instances --query "DBInstances[?DBInstanceStatus=='available'].{DBInstanceIdentifier:DBInstanceIdentifier,Engine:Engine}" --output yaml-stream""")
             print(query)
             os.system("tput setaf 5")
             global db_identifier
             db_identifier=input("plz give DB-Instance-Identifier : ")
             os.system("tput setaf 4")

def db():
    while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"DB TUI\""
         os.system("echo {0} | figlet -f mono9 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo DB TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of Databases with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tDatabase Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
\n\n
press 1 : To create DB Instance
press 2 : To create DB Instance Read Replica
press 3 : To delete/modify DB Instance
press 4 : To go to the Base Menu
press 5 : To Exit
""")
         os.system("tput setaf 7")
         p=input("plz Enter ur choice : ")

         if int(p)==1:
             os.system("tput setaf 4")
             identifier=input("plz give db-instance-identifier/description : ")
             os.system("tput setaf 5")
             dbclass=input("plz give db-instance-class : ")
             os.system("tput setaf 3")
             engine=input("plz give db-engine : ")
             os.system("tput setaf 6")
             master_username=input("plz give master-username : ")
             os.system("tput setaf 4")
             master_user_password=input("plz give master-user-password : ")
             os.system("tput setaf 5")
             allocated_storage=input("plz give allocated-storage : ")
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f"aws rds create-db-instance \
    --db-instance-identifier {identifier} \
    --db-instance-class {dbclass} \
    --engine {engine} \
    --master-username {master_username} \
    --master-user-password {master_user_password} \
    --allocated-storage {allocated_storage}")
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t\tDB Instance created successfully")
             os.system("tput setaf 7")
         
         elif int(p)==2:
             os.system("tput setaf 3")
             read_replica_name=input("plz input Read-Replica Name/Identifier : ")
             db_query()
             cmd=subprocess.getoutput(f"aws rds create-db-instance-read-replica \
    --db-instance-identifier {read_replica_name} \
    --source-db-instance-identifier {db_identifier}")
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t\tDB Instance-Read-Replica created successfully")
             os.system("tput setaf 7")

         elif int(p)==3:
             db_query()
             os.system("tput setaf 6")
             cmd=subprocess.getoutput(f"aws rds delete-db-instance \
                     --db-instance-identifier {db_identifier} ")
             print(cmd)
             os.system("tput setaf 2")
             print("\n\t\tDB Instance deleted successfully")
             os.system("tput setaf 7")

         elif int(p)==4:
                break
         elif int(p)==5:
            exit()
         
         else:
             os.system("tput setaf 4")
             print("entered invalid option")
             os.system("tput setaf 7")
         os.system("tput setaf 6")
         input("\n\t\tpress Enter to keep using this sub-menu : ")
         os.system("tput setaf 7") 
