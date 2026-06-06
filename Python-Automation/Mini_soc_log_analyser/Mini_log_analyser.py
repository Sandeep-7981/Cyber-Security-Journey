import re

logs = [
    "Failed login from 192.168.1.10",
    "Failed login from 192.168.1.11",
    "Successful login from 192.168.1.10",
    "Failed login from 192.168.1.10"
]
print("IP's Found:")
for log in logs:
    ip = re.findall(r"\d+\.\d+\.\d+\.\d+",log)[0]
    print(ip)
print("")
failed=0
suc=0
for log in logs:
    if "Failed" in log:
        failed+=1
    elif "Successful" in log:
         suc += 1
print("Failed Logins : ",failed)

print("Succesful Logins : ",suc,"\n")

count = {}
for log in logs:
    if "Failed" in log:
        ip = re.findall(r"\d+\.\d+\.\d+\.\d+",log)[0]
        if ip in count:
            count[ip]+=1
        else:
            count[ip] = 1
print("Frequencies :")
for ip, freq in count.items():
    
    print(ip,"->",freq)

alert = False
for ip,freq in count.items():
    
    if freq>=3:
        print("ALERT!\n",ip,"has",freq,"login attempts.\n","Possible brute-force attack.")
        alert = True
if alert == False :
    print("No Brute Force Attack Detected")  
