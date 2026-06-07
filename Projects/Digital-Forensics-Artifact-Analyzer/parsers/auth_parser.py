import re

def parse_log(line):

    #For time_stamp
    parts = line.split()
    time_stamp = " ".join(parts[:3])
   
   #For Status
    if "Failed" in line:
        status = "Failed"
    elif "Successful" in line:
        status = "Accepted"
  
   #For Username
    match = re.search(r"for (.*?) from", line)
    username = match.group(1)

    #For IP address
    ip = re.search(r"\d+\.\d+\.\d+\.\d+",line).group(0)

    #Dictionary
    parse_data = {
        "timestamp" : time_stamp,
        "status" : status,
        "username" : username,
        "ip" : ip
    }
    return parse_data


line = "Jun 07 09:15:10 server sshd[1234]: Failed password for admin from 192.168.1.10 port 54321 ssh2"
print(parse_log(line))
