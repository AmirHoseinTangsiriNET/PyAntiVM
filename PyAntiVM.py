import os
import sys
import time
import psutil

sys.stdout.write("\x1b[8;{rows};{cols}t".format(rows=35, cols=170))

def clean():
    os.system('cls' if os.name=='nt' else 'clear')

clean()

print ("""
               AAA                                        tttt            iiii                   VVVVVVVV           VVVVVVVVMMMMMMMM               MMMMMMMM
              A:::A                                    ttt:::t           i::::i                  V::::::V           V::::::VM:::::::M             M:::::::M
             A:::::A                                   t:::::t            iiii                   V::::::V           V::::::VM::::::::M           M::::::::M
            A:::::::A                                  t:::::t                                   V::::::V           V::::::VM:::::::::M         M:::::::::M
           A:::::::::A         nnnn  nnnnnnnn    ttttttt:::::ttttttt    iiiiiii                   V:::::V           V:::::V M::::::::::M       M::::::::::M
          A:::::A:::::A        n:::nn::::::::nn  t:::::::::::::::::t    i:::::i                    V:::::V         V:::::V  M:::::::::::M     M:::::::::::M
         A:::::A A:::::A       n::::::::::::::nn t:::::::::::::::::t     i::::i                     V:::::V       V:::::V   M:::::::M::::M   M::::M:::::::M
        A:::::A   A:::::A      nn:::::::::::::::ntttttt:::::::tttttt     i::::i  ---------------     V:::::V     V:::::V    M::::::M M::::M M::::M M::::::M
       A:::::A     A:::::A       n:::::nnnn:::::n      t:::::t           i::::i  -:::::::::::::-      V:::::V   V:::::V     M::::::M  M::::M::::M  M::::::M
      A:::::AAAAAAAAA:::::A      n::::n    n::::n      t:::::t           i::::i  ---------------       V:::::V V:::::V      M::::::M   M:::::::M   M::::::M
     A:::::::::::::::::::::A     n::::n    n::::n      t:::::t           i::::i                         V:::::V:::::V       M::::::M    M:::::M    M::::::M
    A:::::AAAAAAAAAAAAA:::::A    n::::n    n::::n      t:::::t    tttttt i::::i                          V:::::::::V        M::::::M     MMMMM     M::::::M
   A:::::A             A:::::A   n::::n    n::::n      t::::::tttt:::::ti::::::i                          V:::::::V         M::::::M               M::::::M
  A:::::A               A:::::A  n::::n    n::::n      tt::::::::::::::ti::::::i                           V:::::V          M::::::M               M::::::M
 A:::::A                 A:::::A n::::n    n::::n        tt:::::::::::tti::::::i                            V:::V           M::::::M               M::::::M
AAAAAAA                   AAAAAAAnnnnnn    nnnnnn          ttttttttttt  iiiiiiii                             VVV            MMMMMMMM               MMMMMMMM
                                                                                                                                                           
""")
print ("Anti-VM For Testing The System  Is VM Our Not")
print ("Developer: AmirHosein Tangsiri Nezhad")
print ("-----------------------------------------------------------------------")
if os.name =='nt':
    print ("This Script For Windows OS")
def printer(Print):
    for c in Print + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)


def Anti_VM_With_VMProcess():
    print ("Start System For Detect VM Process")
    time.sleep(2)
    VmCehck1 = "vmsrvc.exe"
    VmCehck2 = "vmusrvc.exe"
    VmCehck3 = "vboxtray.exe"
    VmCehck4 = "vmtoolsd.exe"
    VmCehck5 = "df5serv.exe"
    VmCehck6 = "vboxservice.exe"
    for process in psutil.process_iter():
        try:

            if process.name().lower() == VmCehck1.lower():
                printer ("Detected The VM Process ")
                printer ("Exit..")

            else:
                print ("Not Found vmsrvc.exe Process")

            if process.name().lower() == VmCehck2.lower():
                printer ("Detected The VM Process.. ")
                printer ("Exit..")

            else:
                print ("Not Found vmusrvc.exe Process")

            if process.name().lower() == VmCehck3.lower():
                printer ("Detected The VM Process.. ")
                printer ("Exit..")                

            else:
                print ("Not Found vboxtray.exe Process")

            if process.name().lower() == VmCehck4.lower():
                printer ("Detected The VM Process.. ")
                printer ("Exit..")

            else:
                print ("Not Found vmtoolsd.exe Process")

            if process.name().lower() == VmCehck5.lower():
                printer ("Detected The VM Process.. ")
                printer ("Exit..")

            else:
                print ("Not Found df5serv.exe Process")

            if process.name().lower() == VmCehck6.lower():
                printer ("Detected The VM Process.. ")
                printer ("Exit..")
            else:
                print ("Not Found vboxservice.exe Process")

        except AccessDenid():
            print ("[-]Perimission Denid")
def Anti_VM_With_VMDrivers():
    print ("Scanning System For VM Drivers")
    vmci = os.path.exists("C:\WINDOWS\system32\drivers\vmci.sys")
    vmhgfs = os.path.exists("C:\WINDOWS\system32\drivers\vmhgfs.sys")
    vmmouse = os.path.exists("C:\WINDOWS\system32\drivers\vmmouse.sys")
    vmsci = os.path.exists("C:\WINDOWS\system32\drivers\vmsci.sys")
    vmusbmouse = os.path.exists("C:\WINDOWS\system32\drivers\vmusbmouse.sys")
    vmx_svga = os.path.exists("C:\WINDOWS\system32\drivers\vmx_svga.sys")
    VBoxMouse = os.path.exists("C:\WINDOWS\system32\drivers\VBoxMouse.sys")
    
    
    if vmci == True:
            printer ("Detected The VM Drivers: vmci.sys" )
            printer ("Exit..")
            sys.exit()
    else:
        printer ("Not Found vmx_svga.sys")
    
    if vmhgfs == True:
            printer ("Detected The VM Drivers: vmhgfs.sys" )
            printer ("Exit..")
            sys.exit()
    else:
        printer ("Not Found vmhgfs.sys")
   
    if vmmouse == True:
            printer ("Detected The VM Drivers: vmmouse.sys")
            printer ("Exit..")
            sys.exit()
    else:
        printer ("Not Found vmmouse.sys")
    
    if vmsci == True:
            printer ("Detected The VM Drivers: vmsci.sys")
            printer ("Exit..")
            sys.exit()
    else:
        printer ("Not Found vmsci.sys")
    
    if vmusbmouse == True:
            printer ("Detected The VM Drivers: vmusbmouse.sys")
            printer ("Exit..")
            sys.exit()
    else:
        printer ("Not Found vmusbmouse.sys")
    
    if vmx_svga == True:
            printer ("Detected The VM Drivers: vmx_svga.sys")
            printer ("Exit..")
            sys.exit()
    else:
        printer ("Not Found vmx_svga.sys")
    
    if VBoxMouse == True:
            printer ("Detected The VM Drivers: VBoxMouse.sys")
            printer ("Exit..")
            sys.exit()
    else:
            printer ("Not Found VBoxMouse.sys")

