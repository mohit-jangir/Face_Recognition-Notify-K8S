import os
import getpass

from Linux import Linux
from AWS import AWS
from LVM import LVM
from Docker import Docker
from WEB import web
from ANSIBLE import Ansible
from ML import ML
from HADOOP import Hadoop
from OpenUrl import OpenUrl
from FeedBack import feedback
from Reboot import Reboot
from Communication import msg
from k8s import k8s

vg="myvg"
keypairname="mykey"
lvname="mylv"
privatekey="slave1.pem"

os.system(" tput setaf 6")
loc=input("where you want to run this menu ?(local/remote) : ")
os.system(" tput setaf 7")

os.system(" tput setaf 4")
passwd=getpass.getpass("enter file execution password for authentication(only once) : ")
os.system(" tput setaf 7")

if passwd!="12":
          print("incorrect password")
          exit()

while True:
  os.system("clear")
  os.system("tput setaf 5")
  os.system("echo 'Welcome to Python Menu' | figlet -f cybermedium -d ./figletfonts40/ ")
  os.system("tput setaf 7")
  print("\n\n\n-----------------------------------------------------------------------------------------------------------------------------------------")
  os.system("tput setaf 6")
  os.system("\n\n\n\t\t\t echo MAIN MENU | figlet -f wideterm -d ./figletfonts40/")
  os.system("tput setaf 3")

  print("""
    \n\n
    Press 1 : Linux Commands
    Press 2 : AWS Services
    Press 3 : LVM Partition
    Press 4 : Hadoop
    Press 5 : Configuration Of Web Server
    Press 6 : Docker
    press 7 : To predict through machine learning model(linear regression)
    Press 8 : To Reboot
    press 9 : To open any website to login like gmail & many more
    press 10 : To send SMS, E-mail, Whatsapp with Attached Documents
    press 11 : To Setup Multi-Node K8S Cluster
    Press 12 : To Exit
    """)
  os.system("tput setaf 7")

  if loc=="local":
   os.system("tput setaf 10")
   technology=int(input("Enter your choice : "))
   os.system("tput setaf 7")

  def main():
    if technology == 1:
        Linux.Linux()
    elif technology == 2:
        AWS.AWS()
    elif technology == 3:
        LVM.LVM()
    elif technology == 4:
        Hadoop.Hadoop()
    elif technology == 5:
        web.web()
    elif technology == 6:
        Docker.Docker()
    elif technology == 7:
        ML.ML()
    elif technology == 8:
        Reboot.Reboot()
    elif technology == 9:
        OpenUrl.OpenUrl()
    elif technology == 10:
        msg.msg()
    elif technology == 11:
        k8s.k8s()
    elif technology == 12:
        #feedback.feedback()
        exit()
    else :
        os.system("tput setaf 9")
        print("Enter Correct Technology...")
        os.system("tput setaf 1")
        print("\n\n you have entered an invalid option !!! ,don't worry try menu option correctly again, it is so easy to use ")
        os.system("tput setaf 7")



    os.system("tput setaf 6")
    input("\n\n press Enter to continue using BASE menu : ")
    os.system("tput setaf 7")

  if __name__ == "__main__":
     main()


