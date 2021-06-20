import os
import subprocess
import json
import random

def volume(itag,ebsdb,devdb):
          ebs_size=input("give your ebs size(in GB) to create ebs volume : ")
          random1=random.randint(1,1000)
          ebsname="lvm_ebs_{}".format(random1)

          if len(ebsdb)==0:
              ebsdb.append(ebsname)
              os.system("tput setaf 6")
              os.system("aws ec2 create-volume --availability-zone ap-south-1a --volume-type gp2 --size {} --tag-specifications ResourceType=volume,Tags=['{{Key=Name,Value={}}}']".format(ebs_size,ebsname))
              os.system("tput setaf 2")
              print("\n\n\t\t your ebs volume has been created successfully")
              os.system("tput setaf 7")



          else:
                  if ebsname not in ebsdb:
                      ebsdb.append(ebsname)
                      os.system("tput setaf 6")
                      os.system("aws ec2 create-volume --availability-zone ap-south-1a --volume-type gp2 --size {} --tag-specifications ResourceType=volume,Tags=['{{Key=Name,Value={}}}']".format(ebs_size,ebsname))
                      os.system("tput setaf 2")
                      print("\n\n\t\t your ebs volume has been created successfully")
                      os.system("tput setaf 7")
            
          os.system("tput setaf 5")
          input("\n\n press enter to attach your newly created ebs volume : ")
          os.system("tput setaf 6")
          vol=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(ebsname))
          vol=json.loads(vol)
          vol=vol["Volumes"][0]["VolumeId"]
          dev=["xvdf","xvdg","xvdh","xvdi","xvdj","xvdk","xvdl","xvdm","xvdo","xvdp","xvdn","xvdq","xvdr","xvds","xvdt","xvdu","xvdw","xvdx","xvdy","xvdz"]
          devname=random.choice(dev)


          if len(devdb)==0:
              devdb.append(devname)
              os.system("tput setaf 3")
              x=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(itag))
              x=json.loads(x)
              osid=x["Reservations"][0]["Instances"][0]["InstanceId"]
              os.system("tput setaf 6")
              os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/{}".format(osid,vol,devname))
              os.system("tput setaf 2")
              print("\n\n\t\t your ebs created and attached  successfully" )
              os.system("tput setaf 7")

          else:
                  if devname not in devdb:
                      devdb.append(devname)
                      os.system("tput setaf 3")
                      x=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-key,Values=Name Name=tag-value,Values={}".format(itag))
                      x=json.loads(x)
                      osid=x["Reservations"][0]["Instances"][0]["InstanceId"]
                      os.system("tput setaf 6")
                      os.system("aws ec2 attach-volume --instance-id {} --volume-id {} --device /dev/{}   ".format(osid,vol,devname))
                      os.system("tput setaf 2")
                      print("\n\n\t\t your ebs created and attached  successfully" )
                      os.system("tput setaf 7")

def ebs():
  devname="xvdh"
  itag="myos"
  privatekey="slave1.pem"
  devdb=[]
  ebsdb=[]

  while True:
         os.system("clear")
         os.system("tput setaf 1")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 4")
         name = "\"EBS TUI\""
         os.system("echo {0} | figlet -f mono9 -d ./figletfonts40/".format(name))
         os.system("tput setaf 2")
         os.system("echo EBS TERMINAL USER INTERFACE| figlet -f wideterm -d ./figletfonts40/ ")
         os.system("tput setaf 2")
         print("\t\t\t\t\t\t\t\t...Do things of EBS with a click")
         print("----------------------------------------------------------------------------------------------------------------------------------------")
         os.system("tput setaf 6")
         print("\t\t\t\t\tEBS Menu ")
         print("\t\t\t\t\t----")
         os.system("tput setaf 3")
         print("""
\n\n
press 1 : to create and attach new ebs volume to new launched os
press 2 : to create and attach new ebs volume to local os
press 3 : to create new partition from newly attached ebs and format and mount it
press 4 : to extend static partition size without deleting data
press 5 : to create SnapShots
press 6 : to create Lifecycle Policy for Lifecycle Manager
press 7 : to go to the base menu
press 8 : to exit
""")
         os.system("tput setaf 7")
         p=input("Enter your choice :")

         if int(p)==1:
          volume(itag,ebsdb,devdb)

         elif int(p)==2:
          os.system("tput setaf 6")
          itag="RHEL_8.3_NextGen"
          volume(itag,ebsdb,devdb)
          os.system("tput setaf 7")


         elif int(p)==3:
             hd1=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[0]))
             hd1=json.loads(hd1)
             hd1=hd1["Volumes"][0]["Attachments"][0]["Device"]
             os.system("fdisk {}".format(hd1))
             print("\n\n successfully created partition")
             input("\n\n press Enter to format this partition : ")
             os.system("mkfs.ext4 {}1".format(hd1))
             print("\n\n successfully formatted partition")
             input("\n\n press Enter to mount this partition : ")
             folder=input("plz give ur folder name/path where u want to mount : ")
             os.system("mkdir /{}".format(folder))
             os.system("mount {}1 /{}".format(hd1,folder))
             os.system("tput setaf 2")
             print("\n\n partition mounted successfully and now u can store data in {} directory and all data will be persistent even if ur os/system/root hard disk get corrupt ".format(folder))
             os.system("tput setaf 7")
             os.system("df -h")
             print("here 'type' term means do you want to type : ")
             input1=input("what u have to put in  : file/type ")

             if input1=="file":
              source=input("plz give ur file name/path to copy in ur directory {}".format(folder))
              os.system("cp {} {}".format(source,folder))
              print("\n\n\t\t file copied successfully")

             else:
              print('here press Enter to go to next line and ctrl+d to stop writing and save code in "arth.txt"  ')
              os.system("cat > /{}/arth.txt".format(folder))
              print("\n\n\t\t ur code saved succesfully")



         elif int(p)==4:
          hd1=subprocess.getoutput("aws ec2 describe-volumes --filters Name=tag-value,Values={}".format(ebsdb[0]))
          hd1=json.loads(hd1)
          hd1=hd1["Volumes"][0]["Attachments"][0]["Device"]
          x=subprocess.getoutput("umount {}1".format(hd1))
          os.system("e2fsck -f  {}1".format(hd1))
          os.system("fdisk {}".format(hd1))
          print('give more size(in GIB) to extend partition and give no when it gives an option like "do u want to remove ur signature" so that we dont lose previous data ')
          print("\n\n press enter to check ur partition consistency like inode tables,references or some internal metadata is stable or giving some error")
          os.system("resize2fs {}1".format(hd1))
          folder=input("plz give ur folder name/path where u want to mount : ")
          os.system("mkdir /{}".format(folder))
          os.system("mount {}1 /{}".format(hd1,folder))
          os.system("cd /{};cat arth.txt".format(folder))
          print("see here,ur data is there and it has not been lost ")
          os.system("df -h")
          os.system("tput setaf 2")
          print("\n\n ur static partition size is also extended now with the same data ,see above")
          os.system("tput setaf 7")

         elif int(p)==7:
                break
         elif int(p)==8:
            exit()
         else :
                os.system("tput setaf 1")
                print("entered invalid option")
         os.system("tput setaf 6")
         input("\n\tpress Enter to keep using this sub-menu : ")
         os.system("tput setaf 7")
