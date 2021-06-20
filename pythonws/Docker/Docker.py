import os

def function(req):
    if req==1:
        osname = input("Enter the container name :")
        oimage = input("Enter the container image :")
        os.system("tput setaf 2")
        print("\t\t----------------------")
        os.system("tput setaf 7")
        cmd= "sudo docker run -dit --name {} {}".format(osname,oimage)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status==0:
            print("\n")
            print("Docker OS launched..!!")
            print("Container  Name : {}".format(osname))
            print("Container  Image : {}".format(oimage))
            os.system("tput setaf 2")
            print("\t\t------------------------")
            os.system("tput setaf 7")
            s = os.system("sudo docker ps -a")
            print(s)

        else:
            print("error : {}".format(out))

    elif req == 2 :
        print("All Containers which are stopped and running currently : \n")
        os.system("sudo docker ps -a")
        os.system("tput setaf 3")
        print("\t\t\****************")
        os.system("tput setaf 7 ")
        print("\n")
        osname = input ("Enter the container name which you want to start : ")
        cmd="sudo docker start {}".format(osname)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]
        if status==0:
            print ("Container {}  Started...!!".format(osname))
        else:
            print("error : {}".format(out))

    elif req == 3:
        print("Containers already running :\n")
        os.system("sudo docker ps")
        os.system("tput setaf 3")
        print("\t\t\t\t--------------------")
        os.system("tput setaf 7")
        print("\n")
        osname = input("Enter the container name which you want to stop :")
        cmd= "sudo docker stop {}".format(osname)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status==0:
            print("Container {} Stopped..!!!".format(osname))
        else:
            print("error : {}".format(out))

    elif req ==4:
        print("Container Available:  \n")
        os.system("sudo docker ps -a")
        os.system("tput setaf 3")
        print("\t\t\t******************")
        os.system("tput setaf 7")
        print("\n")
        osname = input("Enter the container name which you want to delete :")
        cmd= "sudo docker container rm -f {}".format(osname)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status==0:
            print("{} Container Removed..!!".format(osname))

        else:
            print("error : {}".format(out))

    elif req ==5:
        cmd= "sudo docker rm -f $(docker ps -aq)"
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status == 0:
            print("All Containers removed Successfully...!!")

        else:
            print("Error :{}".format(out))

    elif req == 6:
        cmd = "sudo docker ps"
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status == 0:
            print(out)

        else:
            print("error : {}".format(out))

    elif req == 7:
        cmd = "sudo docker ps -a"
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print(out)

        else:
            print("Error :{}".format(out))

    elif req ==8:
        oimage = input("Enter the image name and it's version which you want to pull :")
        cmd = "docker pull {}".format(oimage)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print("Image Pulled Successfully..!!")
        else:
            print("error : {}".format(out))


    elif req == 9:
        cmd = "sudo docker images"
        output = subprocess.getstatusoutput(cmd)

        status=output[0]
        out = output[1]

        if status==0:
            print(out)

        else:
            print("error :{}".format(out))

    elif req ==10:
        print("\n\n\t\t please run minimum 1 container to create your docker image ")
        print()
        osname=input("Enter the Container name of which you want to create image:")
        iname = input("Enter the Image Name :")
        iversion= input("Enter the Image Version :")
        os.system("tput setaf 2")
        print("--------------------")
        os.system("tput setaf 7")
        print("--------------------")
        cmd = "sudo docker commit {} {}:{}".format(osname,iname,iversion)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print("\n")
            print("Image Created...!!!")
            print("Image Name : {}".format(iname))
            print("Image Version : {}".format(iversion))

        else:
            print("error :{}".format(out))

    elif req == 11:
        print("Images Available :\n")
        os.system("sudo docker images")
        os.system("tput setaf 3")
        print("\t\t\t***********************")
        os.system("tput setaf 7")
        print("\n")
        oimage=input("Enter the Image name and it's version which you want to delete :")
        cmd = "docker rmi -f {}".format(oimage)
        output = subprocess.getstatusoutput(cmd)

        status = output[0]
        out = output[1]

        if status ==0:
            print("Image deleted Successfully...!!")

        else:
            print("error :{}".format(out))
    

    
    elif req==13:
            exit()
    else :
            print("entered invalid option")


def Docker():
    while True:
        os.system("clear")

        print("""
            Press 1  : To Launch docker Container
            Press 2  : To Start docker  Container
            Press 3  : To Stop docker Container
            Press 4  : To Delete docker Container
            Press 5  : To Delete all  docker Container at once
            Press 6  : To Show all docker running Containers
            Press 7  : To Stop all docker Container
            Press 8  : To Pull docker Images
            Press 9  : To Show docker Images
            Press 10 : To Create docker Images
            Press 11 : To delete docker Images
            press 12 : To go to the base menu
            press 13 : To exit
            """)
        ch1 = input("Enter your choice :")
        os.system("tput setaf 2 ")
        print("\t\t\t\t\t********************")
        print("\n")
        os.system("tput setaf 7")
        if int(ch1)==12:
            break
        function(int(ch1))
        input("press enter to keep using this sub-menu : ")
