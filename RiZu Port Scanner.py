
print("Port Scanner [version - 1.2]")
print("Created By: WarBringerLT")
print("\n[ + ] Importing modules...")
import socket
import ipaddress
ip = ""
port = ""
PortsScanned = []
Open = []
print("[ + ] Done!")
print("[ + ] Prepairing settings... *may take a while*")

def scan(ip,start,end,timeout,Verbose):
    host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host.settimeout(timeout)

    for i in range(start,end,1):
        
        try:
            host.connect((ip, i))
            print("[ + ] Port '{0}' Is ONLINE!".format(i))
            host.send("32 Test bytes".encode())
            host.close()
            Open.append(i)
            PortsScanned.append(i)
        except ConnectionRefusedError:
                print("[ - ] Port '{0}' IS OFFLINE(REFUSED) #ONLINE, but Connection was Rejected!".format(i))
                PortsScanned.append(i)
        except OSError:
            if Verbose:
                print("[ + ] Port '{0}' Is OFFLINE (Timeout)".format(i))
                PortsScanned.append(i)
        except host.timeout():
            print("[ - ] Port '{0}' Is OFFLINE!".format(i))
            PortsScanned.append(i)
        


print("[ + ] Done! Starting Bash...\n\n")
ip = input("Please Enter IP to scan ports: ")
port = input("Please enter PORTS to scan, separate by spaces - e.g.: 54 76 will scan from 54 to 76 by going 54..55..56..57 etc..\n\nEnter Ports: ")
Verbose = input("Would you like to suppress \"OFFLINE\" Messages? (Y/N/[ENTER=Y]").lower()
while not (Verbose == "y" or Verbose == ""):
    if Verbose == "n":
        Verbose = False
        break
    else:
        Verbose = input("Would you like to suppress \"OFFLINE\" Messages? (Y/N/[ENTER=Y]").lower()

tm = 0
while not ((tm >= 1) and (tm <= 10)):
    tm = int(input("Enter timeout (Bigger = Longer; [1-10] Default = 2): "))

start,end = port.split()
scan(ip,int(start),int(end),tm,not bool(Verbose))
print(f"[!] Scan Complete: Total Found ({len(Open)}) Open Ports @ '{ip}'! [Total Scanned: {len(PortsScanned)}] - Exit Code: 0 - FINISHED SUCCESSFULLY.")
