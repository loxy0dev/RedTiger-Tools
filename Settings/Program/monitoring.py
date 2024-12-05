import psutil

def monitor_active_applications():
    print("Active Applications:")
    for proc in psutil.process_iter(['pid', 'name']):
        print(f"PID: {proc.info['pid']}, Name: {proc.info['name']}")

if __name__ == "__main__":
    monitor_active_applications()
