import os
import json
import subprocess

def web():
          pubip=subprocess.getoutput("aws ec2 describe-instances --filters Name=tag-value,Values=slave1")
          pubip=json.loads(pubip)
          pubip=pubip['Reservations'][0]['Instances'][0]['PublicIpAddress']
          print("here 'type' term means do you want to type : ")
          input1=input("what u have to put in web server : file/type :  ")
          if input1=="file":
              print("wait till the time respective software is downloading ")
              os.system("yum install httpd -y")
              input1=input("plz input ur file/path to show as web pages in web server : ")
              os.system("chmod 777 /var/www/html/")
              os.system("cp {} /var/www/html/".format(input1))
              os.system("systemctl start httpd")
              os.system("systemctl enable httpd")
              print("ur web server configured successfully")
              input("press enter to connect to ur new webserver while it is working or not : ")
              os.system("curl http://{}:/{}".format(pubip,input1))
          else:
              os.system("cat > web1.html")
              os.system("yum install httpd -y")
              os.system("chmod 777 /var/www/html/")
              os.system("cp web1.html /var/www/html/")
              os.system("systemctl start httpd")
              print("ur web server configured successfully")
              input("press enter to connect to ur new webserver while it is working or not : ")
              os.system("curl http://{}:/{}".format(pubip,input1))
