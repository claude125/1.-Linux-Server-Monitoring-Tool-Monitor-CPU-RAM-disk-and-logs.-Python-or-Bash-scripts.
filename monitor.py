import psutil
import shutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
    return used / total * 100

def get_uptime():
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = uptime_seconds // 3600
    return uptime_hours

def monitor():
    print("Linux Server Monitoring Tool")
    print("-----------------------------")

    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()
    uptime = get_uptime()

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk:.2f}%")
    print(f"Server Uptime: {uptime} hours")

if __name__ == "__main__":
    monitor()
