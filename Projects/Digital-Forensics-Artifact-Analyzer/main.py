from parsers.auth_parser import parse_log    #Importing from other folders
failed_attempts = {}                         #Stores as Dictionary fo failed attempts
successful_attempts = {}                     #Stores as Dictionary fo failed attempts
total_lines = 0
THRESHOLD = 5                                #Value for Constant suspicious count
with open("samples/auth.log", "r") as file:
 for line in file:
    parsed_data = parse_log(line)            
    ip = parsed_data["ip"] 
    total_lines +=1

    if parsed_data["status"] == "Failed":
        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1
    elif parsed_data["status"] == "Successful":
        if ip in successful_attempts:
            successful_attempts[ip] += 1
        else:
            successful_attempts[ip] = 1
total_failed_attempts = sum(failed_attempts.values())
total_successful_attempts = sum(successful_attempts.values())

sorted_failed = sorted(                                        #Gets sorted failed ID's in desc order
    failed_attempts.items(),
    key=lambda x: x[1],
    reverse=True
)


#Report Printing
print("=" * 40)
print("DIGITAL FORENSICS ARTIFACT ANALYZER")
print("=" * 40)
print()
print("Suspicious Failed Login Report")
print()
print(f"{'IP Address':<20}{'Failed Attempts'}")
print("-" * 35)
for ip, count in failed_attempts.items():
   print(f"{ip:<20}{count}")

print("-" * 35)
print()
print("="*10,"Log Summary","="*10,"\n")
print("Total Lines :",total_lines)
print("Failed Logins :",total_failed_attempts)
print("Successful Logins :",total_successful_attempts)
print("Unique Failed IPs :",len(failed_attempts))
print("\nTop Failed Attempts :")
for ip, count in sorted_failed[:3]:
    print(f"{ip:<20} -> {count}")

print(f"\nSuspicious IPs (>= {THRESHOLD} Attempts)")

for ip, count in sorted_failed:
    if count < THRESHOLD:
        break
    print(f"{ip:<20} -> {count}")

print()
print("-" * 35)







