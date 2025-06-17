import platform
import time
import subprocess

def get_uptime_windows():
    try:
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
            return int(uptime_seconds)
        else:
            raise RuntimeError("NtQuerySystemInformation failed")
    except Exception as e:
        return f"Unable to determine uptime: {e}"

def get_uptime_linux():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return int(uptime_seconds)
    except Exception as e:
        return f"Unable to determine uptime: {e}"

def get_uptime_darwin():
    try:
        result = subprocess.run(['sysctl', '-n', 'kern.boottime'], capture_output=True, text=True, check=True)
        output = result.stdout
        boot_time_str = output.split('=')[1].split(',')[0].strip()
        boot_time = int(boot_time_str)
        now = int(time.time())
        return now - boot_time
    except Exception as e:
        return f"Unable to determine uptime: {e}"

def get_uptime():
    system = platform.system()
    if system == "Windows":
        return get_uptime_windows()
    elif system == "Linux":
        return get_uptime_linux()
    elif system == "Darwin":
        return get_uptime_darwin()
    else:
        return "Unsupported OS"

def format_uptime(uptime):
    if isinstance(uptime, int):
        hours, remainder = divmod(uptime, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"System uptime: {hours} hours, {minutes} minutes, {seconds} seconds"
    else:
        return f"Error: {uptime}"

def main():
    uptime = get_uptime()
    print(format_uptime(uptime))

if __name__ == "__main__":
    main()
