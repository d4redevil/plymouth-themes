import os
import time
import sys
import subprocess

#Getting System Argument 
try:
    config=sys.argv[1]
    print("Installing :)...")
except:
    config=None

#To Installing Themes Inside the /usr/share/plymouth/themes/ Directory
if config == "install":

    #copying Themes to plymouth themes Directory
    os.system("sudo cp -r ./themes/* /usr/share/plymouth/themes/")
    print("Installed Themes.")

try:
    while True:
        #List Of themes available as a dictionary with number as Key.
        themeslist={"1":"godofwar","2":"harleyquinn", "3":"daredevil"}
        print("""
__________.__                               __  .__            ___________.__                                  
\______   \  | ___.__. _____   ____  __ ___/  |_|  |__         \__    ___/|  |__   ____   _____   ____   ______
|     ___/  |<   |  |/     \ /  _ \|  |  \   __\  |  \   ______ |    |   |  |  \_/ __ \ /     \_/ __ \ /  ___/
|    |   |  |_\___  |  Y Y  (  <_> )  |  /|  | |   Y  \ /_____/ |    |   |   Y  \  ___/|  Y Y  \  ___/ \___ \ 
|____|   |____/ ____|__|_|  /\____/|____/ |__| |___|  /         |____|   |___|  /\___  >__|_|  /\___  >____  >
            \/          \/                        \/                        \/     \/      \/     \/     \/ 


Github Page:https://github.com/d4redevil/plymouth-themes


I am D4redEvil

Github:https://github.com/d4redevil
instagram:https://instagram.com/x.x_daredevil_x.x
        """)
        print("Press Ctrl+C to exit.\n")
        print("1.Change Plymouth.\n2.Preview Plymouth.\n0.Quit")

        action=int(input("Choose a Action:"))

        os.system("clear")

        if action == 1:
            for i in themeslist.keys():
                print(i,".",themeslist[i],sep="")

            choice=int(input("Enter your choice:"))
            print("Processing wait...")
            
            #linux Command to configure New Theme.
            os.system(f"sudo plymouth-set-default-theme -R {themeslist[str(choice)]}")

        if action == 2:

            # Best Way to preview plymouth since we are using os.system It will terminate after 10 seconds
            # Sometime it will struck on the splash screen if you use these commands directly in Command Line Interface
            os.system("sudo plymouth quit")
            os.system("sudo plymouthd")
            os.system("sudo plymouth --show-splash")
            time.sleep(10)
            os.system("sudo plymouth quit")
        if action == 0:
            raise KeyboardInterrupt()
        os.system("clear")

except KeyboardInterrupt:
    os.system("clear")
    print("\n Checkout My Github page:https://github.com/d4redevil \n")
    