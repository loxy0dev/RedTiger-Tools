

import subprocess

def protection_tool():
    print("Disabling tracking and microphone access...")
    
    try:
        subprocess.run(['powershell', '-Command', 'Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\CapabilityAccessManager\\ConsentStore\\microphone" -Name "State" -Value 0 -Force'], check=True)
        print("Microphone access disabled.")
    except Exception as e:
        print(f"Error disabling microphone: {e}")

if __name__ == "__main__":
    protection_tool()
