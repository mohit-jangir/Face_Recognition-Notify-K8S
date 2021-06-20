def Ansible(): 
    import os
    import getpass
    import subprocess

    os.system("tput setaf 1")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    os.system("tput setaf 4")
    name = "\"ANSIBLE TUI\""
    os.system("echo {0} | figlet -f smmono12 -d ./figletfonts40/ ".format(name))
    os.system("tput setaf 118 ")
    os.system("echo   ANSIBLE TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
    os.system("tput setaf 10")
    print("\t\t\t\t\t\t\t\t...Do things of Ansible with a click")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    os.system("tput setaf 11")
    print("\t\t\t\t\tAnsible Menu ")
    print("\t\t\t\t\t----")
    os.system("tput setaf 120")
    print("""
    Press  1 : To configure WebServer
    Press  2 : Exit
    Press -2 : To exit to Main Menu 
    """)

    os.system("tput setaf 4")
    print("Enter Your Choice : ",end="")
    os.system("tput setaf 7")
    ch=input()
    if int(ch) == 1 :
        key= input("Enter your key : ")
        inst_type =  input("Enter Instance type : ")
        regionname =  input("Enter Region name : ")
        azname =  input("Enter Availability zone : ")
        voltype =  input("Enter Volume Type : ")
        volsize =  input("Enter Volume Size : ")
        cmd = 'ansible-playbook ./Ansible/test.yml -e "keyname={} inst_type={} regionname={} voltype={} volsize={} AZ={}"'.format(key,inst_type,regionname,voltype,volsize,azname)
        op = subprocess.getoutput(cmd)
        print(op)
    elif int(ch) == 2:
        exit()
    elif int(ch) == -2:
        print("Returning Back...")
        print("Press Enter: The Screen will be cleared")
        os.system("clear")
        import main
        main.main()
    else:
        print("You Entered Wrong Choice ...")
