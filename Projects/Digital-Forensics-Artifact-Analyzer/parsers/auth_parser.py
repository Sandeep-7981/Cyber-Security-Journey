import re

def parse_log(line):

    # Timestamp
    parts = line.split()
    time_stamp = " ".join(parts[:3])

    # Status
    if "Failed" in line:
        status = "Failed"
    elif "Successful" in line or "Accepted" in line:
        status = "Successful"
    else:
        status = "Unknown"

    # Username
    match = re.search(r"for (.*?) from", line)
    username = match.group(1) if match else "Unknown"

    # IP Address
    ip_match = re.search(r"\d+\.\d+\.\d+\.\d+", line)
    ip = ip_match.group(0) if ip_match else "Unknown"

    return {
        "timestamp": time_stamp,
        "status": status,
        "username": username,
        "ip": ip
    }