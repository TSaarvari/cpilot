import os
import platform
import time

def get_uptime():
    system = platform.system()
    if system == "Windows":
        # On Windows, use uptime from system boot time
        import ctypes
        from ctypes import wintypes

        class SYSTEM_TIMEOFDAY_INFORMATION(ctypes.Structure):
            _fields_ = [("BootTime", wintypes.LARGE_INTEGER),
                        ("CurrentTime", wintypes.LARGE_INTEGER),
                        ("TimeZoneBias", wintypes.LARGE_INTEGER),
                        ("Reserved", wintypes.ULONG * 2)]
        ntdll = ctypes.WinDLL("ntdll")
        info = SYSTEM_TIMEOFDAY_INFORMATION()
        status = ntdll.NtQuerySystemInformation(3, ctypes.byref(info), ctypes.sizeof(info), None)
        if status == 0:
            uptime_seconds = (info.CurrentTime.value - info.BootTime.value) // 10000000
            return uptime_seconds
        else:
            return "Unable to determine uptime"
    elif system == "Linux":
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return int(uptime_seconds)
    elif system == "Darwin":
        # MacOS
        import subprocess
        output = subprocess.check_output(['sysctl', '-n', 'kern.boottime']).decode()
        boot_time_str = output.split('=')[1].split(',')[0].strip()
        boot_time = int(boot_time_str)
        now = int(time.time())
        return now - boot_time
    else:
        return "Unsupported OS"

def main():
    uptime = get_uptime()
    if isinstance(uptime, int):
        hours, remainder = divmod(uptime, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"System uptime: {hours} hours, {minutes} minutes, {seconds} seconds")
    else:
        print(f"Error: {uptime}")

if __name__ == "__main__":
    main()
