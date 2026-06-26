import json


def generate_json_report(results, output_file, threshold=5, top_n=5):

    report = {
        "summary": {
            "total_lines": results["total_lines"],
            "failed_logins": results["total_failed"],
            "successful_logins": results["total_successful"],
            "unique_failed_ips": len(results["failed_attempts"]),
            "iocs": results["iocs"],
        },

        "top_failed_attempts": [
            {
                "ip": ip,
                "failed_attempts": count
            }
            for ip, count in results["sorted_failed"][:top_n]
        ],

        "suspicious_ips": [
            {
                "ip": ip,
                "failed_attempts": count
            }
            for ip, count in results["sorted_failed"]
            if count >= threshold
        ],

        "account_compromise_alerts": results["success_after_failure"],

        "recent_timeline": results["event_timeline"][-5:]
    }

    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    print(f"JSON report saved to {output_file}")