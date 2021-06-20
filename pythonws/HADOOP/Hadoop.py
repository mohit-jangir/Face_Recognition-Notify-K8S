import os
import subprocess
import random
import json

def Hadoop():
 while True:
         os.system("clear")
         print("""
\n\n
press 11 : to configure hadoop master node
press 12 : to configure hadoop slave node
press 13 : to configure hadoop client node
press 14 : to leave hadoop safe mode
press 15 : to upload file from client
press 16 : to read file from client
press 17 : to run tcpdump to save packets coming to your ip in a file
press 18 : to see packets coming to your ip
press 19 : to go to the base menu
press 20 : to exit
""")
         p=input("plz enter ur choice : ")

         if int(p)==12:
          os.system("rpm -ivh jdk-8u171-linux-x64.rpm ")
          os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ")
          randomnumber=random.randint(1,100)
          os.system("mkdir /dn{}".format(randomnumber))
          pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave2")
          pubip=json.loads(pubip)
          pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
          os.system("sed -i 's/dn/dn{}/g' hdfs-site.xml".format(randomnumber))
          os.system("cat hdfs-site.xml")
          os.system("sed -i 's/masterip/{}/g' core-site.xml".format(pubip))
          os.system("cat core-site.xml")
          os.system("cp hdfs-site.xml /etc/hadoop/hdfs-site.xml  ")
          os.system("cp core-site.xml /etc/hadoop/core-site.xml  ")
          os.system("hadoop-daemon.sh start datanode")
          os.system("jps")
          os.system("tput setaf 2")
          print("\n\n\t\t succesfully configured slave node")
          os.system("tput setaf 7")
          input("press enter to see how many slaves are connected to master")
          os.system("hadoop dfsadmin -report")
     
    




         elif int(p)==11:   
          os.system("rpm -ivh jdk-8u171-linux-x64.rpm ")
          os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ")
          randomnumber=random.randint(1,100)
          os.system("mkdir /nn{}".format(randomnumber))
          os.system("sed -i 's/masterip/0.0.0.0/g' core-site-master.xml")
          os.system("sed -i 's/data/name/2' hdfs-site-master.xml")
          os.system("sed -i 's/dn/nn{}/g' hdfs-site-master.xml".format(randomnumber))
          os.system("cp hdfs-site-master.xml /etc/hadoop/hdfs-site.xml")
          os.system("cp core-site-master.xml /etc/hadoop/core-site.xml")
          os.system("hadoop namenode -format")
          os.system("hadoop-daemon.sh start namenode")
          os.system("jps")
          os.system("tput setaf 2")
          print("\n\n\t\t succesfully configured master node")
          os.system("tput setaf 7")
          input("press enter to see how many slaves are connected to master")
          os.system("hadoop dfsadmin -report")

      

         elif int(p)==13:
          pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave1")
          pubip=json.loads(pubip)
          pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
          
          os.system("rpm -ivh jdk-8u171-linux-x64.rpm ")
          os.system("rpm -ivh hadoop-1.2.1-1.x86_64.rpm --force ")
          os.system("sed -i 's/masterip/{}/g' core-site-client.xml".format(pubip))
          os.system("cp core-site-client.xml /etc/hadoop/core-site.xml")
          os.system("tput setaf 2")
          print("\n\n\t\t succesfully configured client node")
          os.system("tput setaf 7")




                  
         elif int(p)==9:
          os.system("tput setaf 1")
          print("it seems you have exited,see u again")
          os.system("tput setaf 7")
          exit()


      

         elif int(p)==15:
          print("here 'type' term means do you want to type : ")
          input1=input("what u have to put in web server : file/type ")
          if input1=="file":
              file=input("plz enter your file name/path to upload from client : ")
              os.system("hadoop fs -put {} /".format(file))
              print("file uploaded successfully")
          
          else:
              print('press "Enter" to go to next line and "ctrl+d" to stop writing and save ur code')
              os.system("cat > web.html")
              os.system("hadoop fs -put {} /".format(web.html))
              print("file uploaded successfully")
         elif int(p)==16:
          file=input("plz enter your file name/path to upload from client : ")
          os.system("hadoop fs -cat /{}".format(file))
      
         elif int(p)==14:
          os.system("hadoop dfsadmin -safemode get")
          os.system("hadoop dfsadmin -safemode leave")
          print("successfully left safe mode")
      

         elif int(p)==17:
          os.system("tcpdump -i eth0 -n tcp port not 22 > pkt.txt")
          print("press ctrl+c to stop this cmd")
      
         elif int(p)==18:
          os.system("vim pkt.txt")
         
         elif int(p) == 19 :
          break
         elif int(p)==20:
          exit()
         else :
          print("entered invalid option")
         input("press enter to keep using this sub-menu : ")
