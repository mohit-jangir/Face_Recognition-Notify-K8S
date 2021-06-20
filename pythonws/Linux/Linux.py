import os
def Linux():
 while True: 

        os.system("clear")
        print("""
            \n
            Press 1 :date
            Press 2 :cal
            Press 3 :list
            Press 4 :available Storage
            Press 5 :free Ram
            Press 6 :Cpu usage
            Press 7 :whoami
            Press 8 :jobs
            Press 9 :To add User
            Press 10 :To run any command of Linux
            press 11: to see all mounted devices/volumes
            Press 12 :To go to base menu
            press 13 :to exit
            """)
        
        p = input("Enter your Choice :")

        if int(p) == 1 :
                print("\n\n\t")
                os.system("date")
        elif int(p) == 2 :
                print("\n\n\t")
                os.system("cal")
        elif int(p) == 3 :
                path=input("Enter the path of the folder you want to see the list :")
                list_dir=subprocess.getoutput("ls "+path)
                print("\n")
                print(list_dir)

        elif int(p) == 4 :
                print("\n\n\t")
                os.system("df -h")
        elif int(p) == 5 :
                print("\n\n\t")
                os.system("free -m")
        elif int(p) == 6 :
                print("\n\n\t")
                os.system("lscpu")
        elif int(p) == 7 :
                print("\n\n\t")
                os.system("whoami")
        elif int(p) == 8 :
                print("\n\n\t")
                os.system("echo 'echo' & ")
                os.system("jobs")
                print("\n\n\t\t only echo is running ")
        elif int(p) == 9 :
                print("\n\n\t")
                user = input("Enter user name :")
                s=subprocess.getstatusoutput("useradd "+user)
                status=s[0]
                output=s[1]
                if status==0 :
                    os.system("passwd {}".format(user))
                    print("Password Created Successfully!!!")
                else :
                    print("Error : {}".format(output))
        elif int(p)==10:
                cmd = input("Enter your command :")
                s=subprocess.getstatusoutput(cmd)
                status=s[0]
                output=s[1]
                print(output)
        

        elif int(p)==11:
            print("\n\n\t")
            os.system("df -h")
        
        elif int(p) == 12 :
                break
        elif int(p)==13:
            exit()
        else :
                print("entered invalid option")        
        input("\n\n\t\t press enter to keep using this sub-menu : ")            
