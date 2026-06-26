def generate_threat_assessment(results, threshold=5):
    iocs = results["iocs"]

    high = []
    medium = []
    low = []

    # High Priority
    successful_ips = {
        alert["ip"] for alert in results["success_after_failure"]
    }

    for ip in iocs["suspicious_ips"]:
        if ip in successful_ips:
            high.append(ip)
        else:
            medium.append(ip)

    # Enumeration attacks
    for ip in iocs["enumeration_ips"]:
        if ip not in high and ip not in medium:
            medium.append(ip)

    # Remaining failed IPs
    for ip in results["failed_attempts"]:
        if (
            ip not in high
            and ip not in medium
        ):
            low.append(ip)

    return {
        "high": high,
        "medium": medium,
        "low": low
    }