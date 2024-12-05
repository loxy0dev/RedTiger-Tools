# /Settings/Program/spoofer.py

import subprocess

def spoof_mac_address(interface):
    new_mac = "00:11:22:33:44:55"  # Example MAC address
    print(f"Changing MAC address for {interface} to {new_mac}")
    
    # Disable the network interface
    subprocess.run(["ifconfig", interface, "down"])
    
    # Change the MAC address
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    
    # Enable the network interface
    subprocess.run(["ifconfig", interface, "up"])
    
    print("MAC address changed.")

def main():
    interface = input("Enter the network interface (e.g., eth0): ").strip()
    spoof_mac_address(interface)

if __name__ == "__main__":
    main()
