import os
import time
import subprocess
import random


print("╔══╗╔══╗╔══╗╔══╗╔══╗╔═══╗╔════╗╔╗╔╗")
print("║╔═╝║╔═╝║╔╗║║╔═╝╚╗╔╝║╔══╝╚═╗╔═╝║║║║")
print("║╚═╗║╚═╗║║║║║║───║║─║╚══╗──║║──║╚╝║")
print("║╔═╝╚═╗║║║║║║║───║║─║╔══╝──║║──╚═╗║")
print("║║──╔═╝║║╚╝║║╚═╗╔╝╚╗║╚══╗──║║───╔╝║")
print("╚╝──╚══╝╚══╝╚══╝╚══╝╚═══╝──╚╝───╚═╝\n")


print("1 DDos Attack")
print("2 Doxbin page (Tor Browser)")
print("3 FSociety terminal spam\n")

choice = input("select: ")


if choice == "1":
    url = input("Enter target URL: ")
    if url.startswith("http://") or url.startswith("https://"):
        print(f"Preparing attack on {url}...")
        time.sleep(2)
        print("Initializing packet send...")
        time.sleep(1)
        print("Launching attack!\n")
        time.sleep(1)

        
        for i in range(100):
            packets = random.randint(1000, 5000)
            print(f"Sending {packets} packets to {url}...")
            time.sleep(0.05)
        
        print("\nBOOM! Attack finished. (This is a fake simulation)")
    else:
        print("Invalid URL! Make sure it starts with http:// or https://")


elif choice == "2":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    tor_path = os.path.join(desktop_path, "Tor Browser", "Browser", "firefox.exe")
    url = "http://doxbin.com"

    if os.path.exists(tor_path):
        subprocess.Popen([tor_path, url])
        print("Tor Browser started. It should automatically open Doxbin.")
    else:
        print("You don't have Tor Browser installed on your Desktop!")


elif choice == "3":
    for _ in range(100000):
        print("F S O C I E T Y")
        time.sleep(0.001)


else:
    print("Option not recognized!")
