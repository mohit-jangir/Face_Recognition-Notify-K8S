import os
from Communication.Sms import Sms
from Communication.WhatsApp import WhatsApp
from Communication.Email import Email

def msg():
    while True:
        os.system("clear")
        os.system("tput setaf 1")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        os.system("tput setaf 4")
        name = "\" Messaging TUI\""
        os.system("echo {0} | figlet -f cybermedium -d ./figletfonts40/".format(name))
        os.system("tput setaf 2")
        os.system("echo MSG TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
        os.system("tput setaf 2")
        print("\t\t\t\t\t\t\t\t...Do things of msg with a click")
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        os.system("tput setaf 6")
        print("\t\t\t\t\tMessaging Menu ")
        print("\t\t\t\t\t----")
        os.system("tput setaf 3")
        print("""
press 1 : To send SMS
press 2 : To WhatsApp
press 3 : To send E-mail
press 4 : To go back to the Previous/Back/Base Menu
press 5 : To Exit
""")

        os.system("tput setaf 6")
        p=input("Enter your choice : ")

        if int(p)==1:
            Sms.Sms()

        elif int(p)==2:
            WhatsApp.WhatsApp()
            
        elif int(p)==3:
            Email.Email()

        elif int(p)==4:
            break
        
        elif int(p)==5:
            os.system("tput setaf 7")
            exit()
        
        else :
            print("entered invalid option")
        
        os.system("tput setaf 2")
        input("press enter to keep using this sub-menu : ")
