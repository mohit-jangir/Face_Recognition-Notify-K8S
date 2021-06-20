import os

def OpenUrl():
     import webbrowser   
     while True:
        os.system("clear")

        print("""
          \n\n
          press 1:to open gmail
          press 2:to open linkedin
          press 3:to open google
          press 4:to open google drive
          press 5:to open github
          press 6:to open aws cloud console
          press 7:to open zoom
          press 8:to open hotstar
          press 9:to go to the base menu
          press 10:to exit
            """)
        ch1 = input("Enter your choice :")
     
        if int(ch1)==1:
            print("\n\n\t")
            webbrowser.open("https://mail.google.com")
        elif int(ch1)==2:
            print("\n\n\t")
            webbrowser.open("https://www.linkedin.com")
        elif int(ch1)==3:
            print("\n\n\t")
            webbrowser.open("https://www.google.com")
        elif int(ch1)==4:
            print("\n\n\t")
            webbrowser.open("https://drive.google.com")
        elif int(ch1)==5:
            print("\n\n\t")
            webbrowser.open("https://www.github.com")
        elif int(ch1)==6:
            print("\n\n\t")
            webbrowser.open("https://aws.amazon.com")
        elif int(ch1)==7:
            print("\n\n\t")
            webbrowser.open("https://zoom.us")
        elif int(ch1)==8:
            print("\n\n\t")
            webbrowser.open("https://www.hotstar.com")
        elif int(ch1)==10:
            exit()
        elif int(ch1)==9:
            break
        input("\n\n\t\tpress enter to keep using this sub-menu : ")

