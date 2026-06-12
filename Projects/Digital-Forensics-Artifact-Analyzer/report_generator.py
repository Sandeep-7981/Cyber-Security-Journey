import os

#Report Printing
def print_report(results,threshold,top_n):
    print("=" * 40)
    print("DIGITAL FORENSICS ARTIFACT ANALYZER")
    print("=" * 40)

    print()
    print("Suspicious Failed Login Report:")
    print()

    print(f"{'IP Address':<20}{'Failed Attempts'}")
    print("-" * 35)

    for ip, count in results["failed_attempts"].items():
        print(f"{ip:<20}{count}")

    print("-" * 35)

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
    if not found:
      print("No suspicious IPs found.")



def save_report(results, filename, threshold=5, top_n=3):
    os.makedirs(os.path.dirname(filename), exist_ok=True)          #if directory doesn't exist create
    with open(filename, "w") as file:

        file.write("=" * 40 + "\n")
        file.write("DIGITAL FORENSICS ARTIFACT ANALYZER\n")
        file.write("=" * 40 + "\n")

        file.write("\n")
        file.write("Suspicious Failed Login Report:\n")
        file.write("\n")

        file.write(f"{'IP Address':<20}{'Failed Attempts'}\n")
        file.write("-" * 35+"\n")

        for ip, count in results["failed_attempts"].items():
            file.write(f"{ip:<20}{count}\n")

        file.write("-" * 35)

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
        