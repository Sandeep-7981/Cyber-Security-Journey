from parsers.auth_parser import parse_log
failed_attempts = {}
with open("samples/auth.log", "r") as file:
 for line in file:
    parsed_data = parse_log(line)
    ip = parsed_data["ip"] 

    if parsed_data["status"] == "Failed":
        if ip in failed_attempts:
            failed_attempts[ip] += 1
        else:
            failed_attempts[ip] = 1
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
total_failed_attempts = sum(failed_attempts.values())
print("-" * 35)
print("Unique IPs :",len(failed_attempts))
print("Total failed attempts :",total_failed_attempts)
print("-" * 35)