import psutil

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        print(f"Alert: High CPU Usage - {cpu_usage}%")

def check_memory():
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > MEMORY_THRESHOLD:
        print(f"Alert: High Memory Usage - {memory_usage}%")

def check_disk():
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > DISK_THRESHOLD:
        print(f"Alert: High Disk Usage - {disk_usage}%")

def check_processes():
    processes = psutil.process_iter()
    for process in processes:
        pass

if __name__ == "__main__":
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
