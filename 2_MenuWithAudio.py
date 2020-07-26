""" Welcome to TUT World 
 -This Project is Implemeted in a python and RHCA
 -TUI is the name of Project. TUT means Terminal User Interface
 -The Project is for the user that doesn't have a knowledge about linux Command and Docker.
                                                             Develop By: Sumit Rasal"""
import os
import getpass
i=0
while i<=3: 
    i=i+1
    os.system("clear") 
    os.system("tput setaf 1")
    os.system('espeak-ng " Welcome to TUI Wold" | echo "\t\t\t\t Welcome to TUI Wold \t\t\t`tput setaf 14` [`date +%T`]"')
    os.system("tput setaf 4")
    os.system('espeak-ng "Please Enter The Password" | echo -n "Plz Enter The Password :" ')
    Pass=getpass.getpass("")
    if Pass != "sumit@301":
     print("\t\tPassword Is Wrong You Have 3 Attempt.You Use {} Attempt:".format(i))
     os.system('espeak-ng "password is wrong you have only three Attempt"')
     os.system('espeak-ng "Pess Enter Key To continue " | echo -n "Pree Enter Key To continue"')
     input("")
     os.system("clear")
     if i == 3:
      os.system("tput setaf 1")
      print("\t\t\tSorry,You Have Only Three Attempt")
      print("\t\t\t\t Try Again Plz")
      os.system("tput setaf 4")
      exit()
    elif Pass == "sumit@301":
     break;
os.system('espeak-ng "Please Enter Where You Want To Go local or remote " | echo "" ')
Location=input("Plz Enter Where You Want To Go (local/remote):") # Providing The Option To Uer Where He want to Login
os.system("clear")
if Location == 'local':	# Local-Uer If loop Start
 while True:            # while loop is running for the Local Menu
    # Menu Provide By TUI For A User For Local
    os.system("tput setaf 1")
    os.system(' echo "\t\t\t Welcome To TUI-Locally \t\t\t [`date +%T `] " ')
    os.system("tput setaf 4")
    print("""
    \t1.Linux Basic Operation Like(Create File, Remove File, Show Date )
    \t2.Partion Operation
    \t3.Create A user
    \t4.Install The Docker
    \t5.Docker Operation
    \t6.Insall The Web Server
    \t7.Exit From The TUI
    """)
    os.system("tput setaf 4")  # Changing The Color of Hedline To Red   
    print("\t\t\tPlz Enter Your Choise:",end='')
    ch=input()
    if int(ch) == 1: # Taking Input From user for choise
     os.system("clear")
     while True:    # while Loop is start For TUI-Linux Basic Operation
      os.system("tput setaf 1")
      os.system(' echo "\t\t\t Welcome To Linux Basic Operatiion \t\t\t [`date +%T `] " ')
      os.system("tput setaf 4")
      #Menu To TUI-Linux Basic Operation
      print("""                  
      \t1.Show The Date
      \t2.Show Calendar
      \t3.Create a File
      \t4.Check The File 
      \t5.Remove The File
      \t6.Read The File
      \t7.Check The Ip and Network Configuration 
      \t10.Exit From TUI-Linux
      \t11.Go To TUI-Local Page

      """)
      LinuxChoise=input("Plz Enter You Coise:")
      if int(LinuxChoise)== 1:
        os.system('tput setaf 15')
        os.system('date')  # Showing Date / date command
        os.system("tput setaf 4")
      elif int(LinuxChoise) == 2:
        os.system('tput setaf 15')
        os.system('cal')               #showing Calender
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 3:
        FileName=input("Plz Enter The File Name With Location Like (/Desktop/project/sumit.txt):")  # Creating File
        os.system('tput setaf 15')
        os.system('touch ~{0}'.format(FileName))
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 4:
        FileName1=input("Plz Enter The Location Where You Want Check File :")    # Checking The File
        os.system('tput setaf 15')
        os.system('ls ~{0}'.format(FileName1))
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 5:
        FileName2=input("Plz Entre The Location Of File For Delet. Like (/Desktop/project/sumit.txt)")   # Removing The File
        os.system('tput setaf 15')
        os.system('rm ~{0}'.format(FileName2))
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 6:
        FileName3=input("Plz Entre The Location Of File For Read. Like (/Desktop/project/sumit.txt)")    # Reding The File 
        os.system('tput setaf 15')
        os.system('cat ~{0}'.format(FileName3))
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 7:
        os.system('tput setaf 15')
        os.system('ifconfig')
        os.system('tput setaf 4')
      elif int(LinuxChoise) == 10:      #Exiting From TUI
        os.system('tput setaf 15')
        exit()
      elif int(LinuxChoise) == 11:      #Exiting From TUI-Linux Basic Operation 
        os.system('tput setaf 4')
        break;
      LinuxInput=input("\t\tDo You Want Continue? (y/n)")
      if LinuxInput == 'n':
         break; 
      os.system("clear")
      # while Loop of TUI-Linux Basic Operation Is End Here 
 
    elif int(ch) == 2:
     while True:
       os.system('clear')
       os.system("tput setaf 1")
       os.system('echo "\t\t\t Welcome To Partition Operatiion\t\t [`date +%T`]" ')  #Heading Of Partition Menu
       os.system("tput setaf 4")
       print("""
        1.Check The Partion
        2.Create A Partition
        3.Exit From TUI
        4.Go TUI-Menu Page   
       """)
       partitionCh=input("\t\tPlz Enter Your Choise :")
       if int(partitionCh) == 1:
          os.system("tput setaf 15")
          os.system('fdisk -l')
          os.system("tput setaf 4")
       elif int(partitionCh) == 2:
          help1=input("Get Information About Partition Plz Enter- h : ")
          if help1 =='h':
           os.system("tput setaf 15")
           print("""
		Help:
		  DOS (MBR)
		   a   toggle a bootable flag
		   b   edit nested BSD disklabel
		   c   toggle the dos compatibility flag

		  Generic
		   d   delete a partition
		   F   list free unpartitioned space
		   l   list known partition types
		   n   add a new partition
		   p   print the partition table
		   t   change a partition type
		   v   verify the partition table
		   i   print information about a partition

		  Misc
		   m   print this menu
		   u   change display/entry units
		   x   extra functionality (experts only)

		  Script
		   I   load disk layout from sfdisk script file
		   O   dump disk layout to sfdisk script file

		  Save & Exit
		   w   write table to disk and exit
		   q   quit without saving changes

		  Create a new label
		   g   create a new empty GPT partition table
		   G   create a new empty SGI (IRIX) partition table
		   o   create a new empty DOS partition table
		   s   create a new empty Sun partition table
		""")
           os.system("tput setaf 4")
           Disk=input("Plz Enter The Disk Name For Going To inside Like (/dev/sda) :")
           os.system('fdisk {}'.format(Disk))
           os.system("tput setaf 4")
       elif int(partitionCh) == 3:
           os.system('tput setaf 15')
           exit()
       elif int(partitionCh) == 4:
           break; 
       LinuxInput1=input("\t\tDo You Want Continue? (y/n)")
       if LinuxInput1 == 'n':
         break;
       os.system('clear')

    elif int(ch) ==3:
      UserName=input("Pls Enter The User Name:")
      os.system('useradd {}'.format(UserName)) # creating the user
    elif int(ch) ==4:
      os.system("tput setaf 15")
      os.system("yum install dokcer-ce --nobest")
      os.system("tput setaf 15")
    elif int(ch) == 5:
       while True:   # While Loop are starting fo Docker Operation
         #Menu for the Docker Operation
         os.system("clear")
         os.system("tput setaf 1")
         os.system('echo "\t\t\t Welcome To Docker Operation \t\t\t [`date +%T `]" ')   #Heading Of Docker Menu
         os.system("tput setaf 4")
         print("""
         1.Start The Docker Services/Compulsory
	 2.check The No Container are Lanuch
         3.Lanuch New The Docker Container
         4.Downloads The Docker Images
         5.Go Menu Page
         6.Exit From TUI
         """)
         os.system("tput setaf 14")
         os.system("echo '\t Note:If You Not Start The Docker Services First Run It Then Use The Other option:'")
         os.system("tput setaf 4")
         print("\t\t\tPlz Enter The Choise :",end='')
         os.system("tput setaf 4")
         DockerCh=input()
         os.system("tput setaf 4")
         if int(DockerCh)==1:
            os.system("tput setaf 15")
            os.system("systemctl start docker")  # Starting the Docker Services
            os.system("tput setaf 4")
         elif int(DockerCh)==2:
            os.system("tput setaf 15")
            os.system(" docker ps -a ")     # Checking the Runnig , ShutDown Container(OS)
            os.system("tput setaf 4")
            input("Plz Enter To Continue")
         elif int(DockerCh)==3:
            ContainerName=input("Plz Enter the container Name:")
            os.system("docker container run -it --name {} centos:latest".format(ContainerName))  # Lanuching New Container 
            os.system("tput setaf 4")
         elif int(DockerCh)==5:
            os.system("tput setaf 15")
            break;
         elif int(DockerCh)==6:
            os.system("tput setaf 15")
            exit()
         else:
           print("Plz Enter The Write Choise:")
         Forward=input("\t\t\tDo You Want Continue the Docker Operation ? (y/n) ")  # Taking Input for Continue or for Stop Program
         if Forward== 'n' or Forward== 'N' :
               break;
         # While Loop are Ending Of Docker operation
    elif int(ch)==6:
      os.system("tput setaf 15")
      os.system("yum install httpd") #Installing the Web server
      os.system("tput setaf 4")
    elif int(ch)==7:
      os.system("tput setaf 15")
      exit()
    else:
      print("Plz Choise Write Option")
      os.system("tput setaf 15")

    x=input("\t\t\tDo You Want Continue TUI-Locally ? (y/n) ")  # Taking Input For Continue Or For Stop Program
    if x== 'n' or x== 'N' :
      os.system("tput setaf 15")
      exit()
    os.system("clear")                  # Clearing The Screen For Holding The Menu at Fix Position

# Remote-user Loop is Starting
elif Location == 'remote':
 os.system("tput setaf 1")
 os.system('echo "\t\t\t Welcome To TUI-Remotly \t\t\t [`date +%T`] "')  #Heading Of Remote-Control menu
 os.system("tput setaf 4")
 RemoteUserName=input("Plz Enter User Name(root/sumit)")
 UserIp=input("Plz Enter The User Ip Befor Go To Menu :")
 os.system("clear")
 while True:   # While Loop Are Start For Remote TUI
      # Menu Provide By TUI For A User For Remote
      os.system("tput setaf 1")
      print("\t\t\t Welcome To TUI-Remotly")
      os.system("tput setaf 4")
      print("""
      \t1.Ping To User
      \t2.Today Date
      \t3.Show Calendar
      \t4.Create A User
      \t5.Give Me The User Terminal Access 
      \t6.Upload The File
      \t7.Download The File
      \t8.Exit From TUI
      """)
      RemoteChoise=input("Plz Enter The Choise :")
      if int(RemoteChoise) == 1:       # Ping To Remote Host Machine 
          os.system("ping {}".format(UserIp))
      elif int(RemoteChoise) == 2:     # Running The Date Command On Remote-Host Machine 
          os.system("ssh {0}@{1} date".format(RemoteUserName,UserIp))
      elif int(RemoteChoise) == 3:
          os.system("ssh {0}@{1} cal".format(RemoteUserName,UserIp))
      elif int(RemoteChoise) == 4:      # Creating The User On Remote Host Machine
          UserAdd=input("Plz Enter The User Name: ")
          os.system("ssh {0}@{1} useradd {2} ".format(RemoteUserName,UserIp , UserAdd))
      elif int(RemoteChoise) == 5:      # Connecting To Remote Host Machine
          os.system("ssh {0}@{1}".format(RemoteUserName,UserIp))
      elif int(RemoteChoise) == 6:      # Uploading The File 
          os.system("tput setaf 14")
          print("\tNote: If You Don`t Know File Name Then Plz Ref Option-5 And Check File Name")
          os.system("tput setaf 4")
          Option5=input("\tDo you Want to Go To The Option-5 ? (y/n)")
          if Option5 == 'y': 
            os.system("ssh {0}@{1}".format(RemoteUserName,UserIp))      # Connecting To Remote Host Machine
          os.system("tput setaf 4")
          RemoteHostFile=input("Ok Then Plz Enter The File Name:")          
          os.system("scp /root/Desktop/project/{2} {0}@{1}:/home/sumit/Desktop/".format(RemoteUserName,UserIp,RemoteHostFile))
      elif int(RemoteChoise) == 7:     #Downloading The File 
          os.system("tput setaf 4")
          print("\tNote: If You Don`t Know The File Name Plz Ref Option-5 And Check File Name")
          Option6=input("\tDo You Want To GO To The Option-5 ? (y/n)")
          if Option6 == 'y':
             os.system("ssh {0}@{1}".format(RemoteUserName,UserIp))
          os.system("tput setaf 4")
          DownloadHostFile=input("Plz Enter The File Name :")
          os.system("scp {0}@{1}:/home/sumit/Desktop/{2} /root/Desktop/".format(RemoteUserName,UserIp,DownloadHostFile))
      elif int(RemoteChoise) == 8:    # Exit From TUT
          os.system("tput setaf 15")
          exit()
      p=input("Do You Want To Continue TUI-Remotelly ? (y/n)")
      if p == 'n' or p=='N':
         exit() 
      os.system("clear")
      os.system("tput setaf 15")
      # While Loop Is Ending Here 
 
