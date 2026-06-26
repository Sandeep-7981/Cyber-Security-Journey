import csv


def generate_csv_report(results, output_file, threshold=5, top_n=5):

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "IP Address",
            "Failed Attempts",
            "Unique Users",
            "Enumeration"
        ])

        for ip, count in results["failed_attempts"].items():

            unique_users = len(results["failed_users"][ip])

            enumeration = "YES" if unique_users >= 3 else "NO"

            writer.writerow([
                ip,
                count,
                unique_users,
                enumeration
            ])

    print(f"CSV report saved to {output_file}")