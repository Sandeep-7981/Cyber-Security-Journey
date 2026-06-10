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
    else:
        status = "Unknown"
  
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

   

