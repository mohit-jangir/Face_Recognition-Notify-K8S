import os
import subprocess
import json

from AWS.compute.EC2 import ebs

def LVM():
  vg="myvg"
  lvname="mylv"
  
  while True:
         os.system("clear")   
         os.system("tput setaf 1")
         print("\n\n REMINDER !!! ,IF U WANT TO EXTEND VG THEN FIRST ATTACH NEW EBS VOLUME ,FOR THAT GO TO OPTION 3 IF U HAVEN'T DONE YET")   
         os.system("tput setaf 7")
         os.system("tput setaf 2")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\" LVM  TUI\""
         os.system("echo {0} | figlet -f mono9 -d ./figletfonts40/ ".format(name))
         os.system("tput setaf 6")
         os.system("echo   LVM  TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 5")
         print("\t\t\t\t\t\t\t\t...Do things of LVM with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system(" tput setaf 2")
         print("...\t\t\t\t\tLVM Main Menu...")
         os.system(" tput setaf 3 ")
         print("""
\n
press 6 : to create LVM partition
press 7 : to extend lv size
press 8 : to reduce lv size
press 9 : to extend VG size
press 10 : to go to the base menu
press 11 : to exit
""")     
         os.system(" tput setaf 7")
         p=input("plz enter ur choice : ")


         if int(p) == 6:
          os.system("tput setaf 2")   
          hd1=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebs.ebsdb[0]))
          hd2=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebs.ebsdb[1]))
          hd1=json.loads(hd1)
          hd2=json.loads(hd2)
          hd1=hd1["Volumes"][0]["Attachments"][0]["Device"]
          hd2=hd2["Volumes"][0]["Attachments"][0]["Device"]
          os.system("tput setaf 5")
          os.system("pvcreate {}".format(hd1))
          os.system("pvdisplay {}".format(hd1))
          os.system("tput setaf 6")
          os.system("pvcreate {}".format(hd2))
          os.system("pvdisplay {}".format(hd2))
          os.system("tput setaf 3")
          vg=input("enter your vg name : ")
          os.system("tput setaf 4")
          os.system("vgcreate {} {} {}".format(vg,hd1,hd2))
          os.system("vgdisplay {}".format(vg))
          os.system("tput setaf 3")
          lvname=input("enter your lv name : ")
          lvsize=input("enter your lv size : ")
          os.system("tput setaf 3")
          os.system("lvcreate --size {}GB --name {} {}".format(lvsize,lvname,vg))
          os.system("tput setaf 2")
          print("successfully created logical volume")
          os.system("tput setaf 7")
          os.system("tput setaf 4")
          os.system("lvdisplay /dev/{}/{}".format(vg,lvname))
          os.system("tput setaf 3")
          input("press enter to format your lv {}  : ".format(lvname))
          os.system("mkfs.ext4 /dev/{}/{}".format(vg,lvname))
          os.system("tput setaf 3")
          print("your lv {} succesfully formatted".format(lvname))
          os.system("tput setaf 4")
          dir=input("enter new folder to create where this lv will be mounted : ")
          os.system("mkdir /{}".format(dir))
          os.system("mount /dev/{}/{} /{}".format(vg,lvname,dir))
          os.system("tput setaf 6")
          print("successfully mounted your lv {} to folder {}".format(lvname,dir))
          os.system("tput setaf 2")
          print("\n\n do you want to extend this lv size ,go for option 7")
          os.system("tput setaf 7")




         elif int(p) == 7:
          os.system("tput setaf 3")
          extended_size=input("plz enter how much size(in GB) U want to extend to ur lv : ")
          os.system("tput setaf 6")
          os.system("lvextend --size +{}GB /dev/{}/{}".format(extended_size,vg,lvname)) 
          os.system("resize2fs /dev/{}/{}".format(vg,lvname))
          os.system("tput setaf 2")
          print("\n\n successfully extended your lv")
          os.system("tput setaf 7")

     
         elif int(p) == 8:
          os.system("tput setaf 5")
          reduced_size=input("plz enter how much size(in GB) U want to reduce to ur lv : ")
          os.system("tput setaf 3")
          os.system("lvreduce --size -{}GB /dev/{}/{}".format(extended_size,vg,lvname))
          os.system("resize2fs /dev/{}/{}".format(vg,lvname))
          os.system("tput setaf 2")
          print("\n\n successfully reduced your lv")
          os.system("tput setaf 7")


         elif int(p) == 9:
          os.system("tput setaf 1")   
          print("REMINDER !!! ,IF U WANT TO EXTEND VG THEN FIRST ATTACH NEW EBS VOLUME ,FOR THAT GO TO OPTION 3 IF U HAVEN'T DONE YET")
          hd3=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[2]))
          hd3=json.loads(hd3)
          devname=hd3["Volumes"][0]["Attachments"][0]["Device"]
          vg=input("enter your old vg name : ")
          os.system("tput setaf 6")
          os.system("pvcreate {}".format(devname))
          os.system("pvdisplay {}".format(devname))
          os.system("vgextend {} {}".format(vg,devname))
          os.system("vgdisplay {}".format(vg))
          os.system("tput setaf 5")
          sizelv=input("plz enter ur size to extend in lv : ")
          os.system("lvextend --size +{}GB /dev/{}/{}".format(sizelv,vg,lvname))
          os.system("resize2fs /dev/{}/{}".format(vg,lvname))
          os.system("tput setaf 2")
          print("\n\n successsfully extended your vg and lv through new ebs volume")
          os.system("tput setaf 7")
         

         elif int(p) == 10 :
                break
         elif int(p)==11:
            exit()
         else : 
                os.system("tput setaf 1")
                print("entered invalid option")
         os.system("tput setaf 4")       
         input("press enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
