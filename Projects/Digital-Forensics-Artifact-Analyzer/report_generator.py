import os

#Report Printing
def print_report(results,threshold,top_n):
    print("=" * 40)
    print("DIGITAL FORENSICS ARTIFACT ANALYZER")
    print("=" * 40)

    print()
    print("Suspicious Failed Login Report:")
    print()

    print(f"{'IP Address':<20}{'Failed Attempts':<20}{'Unique Users':<20}{'Enumeration'}")
    print("-" * 75)
    
    for ip, count in results["failed_attempts"].items():
        unique_users = len(results["failed_users"][ip])
        Enumeration = "YES" if unique_users >= 3 else "NO"
        print(f"{ip:<20}{count:<20}{unique_users:<20}{Enumeration}")

    print("-" * 75)

    print()
    print("=" * 10, "Log Summary", "=" * 10)
    print()

    print("Total Lines :", results["total_lines"])
    print("Failed Logins :", results["total_failed"])
    print("Successful Logins :", results["total_successful"])
    print("Unique Failed IPs :", len(results["failed_attempts"]))

    print("\nTop Failed Attempts :")

    for ip, count in results["sorted_failed"][:top_n]:
        print(f"{ip:<20} -> {count}")
        
    print(f"\nSuspicious IPs (>= {threshold} Attempts)")
    found = False
    for ip, count in results["sorted_failed"]:

        if count < threshold:
            break
        found = True
        print(f"{ip:<20} -> {count}")
    print()
    if not found:
      print("No suspicious IPs found.\n")

    print("="*35)
    print("POTENTIAL ACCOUNT COMPROMISE ALERTS")
    print("="*35,"\n")
    print(f"{'IP Address':<20}{'User name':<20}{'Time Stamp'}")
    print("-" * 55)
    for alert in results["success_after_failure"]:
        found = True
        print(f'{alert["ip"]:<20}{alert["username"]:<20}{alert["timestamp"]:<20}')
    if not found:
        print("No alerts detected.\n")   
    
    


def save_report(results, filename, threshold=5, top_n=3):

    os.makedirs(os.path.dirname(filename), exist_ok=True)          #if directory doesn't exist create
    with open(filename, "w") as file:

        file.write("=" * 40 + "\n")
        file.write("DIGITAL FORENSICS ARTIFACT ANALYZER\n")
        file.write("=" * 40 + "\n")

        file.write("\n")
        file.write("Suspicious Failed Login Report:\n")
        file.write("\n")

        

        file.write(f"{'IP Address':<20}{'Failed Attempts':<20}{'Unique_IPs':<20}{'Enumeration'}\n")
        file.write("-" * 75+"\n")
    
        for ip, count in results["failed_attempts"].items():
            unique_users = len(results["failed_users"][ip])
            Enumeration = "YES" if unique_users >= 3 else "NO"
            file.write(f"{ip:<20}{count:<20}{unique_users:<20}{Enumeration}\n")
            
 
        file.write("-" * 75)
        

        file.write("\n\n")
        file.write("=" * 10 + " Log Summary " + "=" * 10 + "\n")
        file.write("\n")

        file.write(f"Total Lines : {results['total_lines']}\n")
        file.write(f"Failed Logins : {results['total_failed']}\n")
        file.write(f"Successful Logins : {results['total_successful']}\n")
        file.write(f"Unique Failed IPs : {len(results['failed_attempts'])}\n")
        file.write("\nTop Failed Attempts :\n")
        found = False
        for ip, count in results["sorted_failed"][:top_n]:
            file.write(f"{ip:<20} -> {count}\n")
            found = True
        if not found:
            file.write("No suspicious IPs found.")
        file.write(f"\nSuspicious IPs (>= {threshold} Attempts)\n")

        for ip, count in results["sorted_failed"]:

            if count < threshold:
                break

            file.write(f"{ip:<20} -> {count}\n")
        