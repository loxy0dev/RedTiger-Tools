import psutil

def monitor_active_applications():
    print("Active Applications:")
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")

def main():
    input("Press Enter to list all active applications...")
    monitor_active_applications()

if __name__ == "__main__":
    main()
