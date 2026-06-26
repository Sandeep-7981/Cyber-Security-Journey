from collections import Counter


def extract_iocs(results, threshold=5):

    suspicious_ips = []
    enumeration_ips = []
    compromised_accounts = set()
    targeted_accounts = Counter()

    # Suspicious IPs
    for ip, count in results["failed_attempts"].items():

        if count >= threshold:
            suspicious_ips.append(ip)

        if len(results["failed_users"][ip]) >= 3:
            enumeration_ips.append(ip)

    # Successful login after failures
    for alert in results["success_after_failure"]:

        compromised_accounts.add(alert["username"])

    # Targeted accounts
    for users in results["failed_users"].values():

        for user in users:
            targeted_accounts[user] += 1

    most_active = None

    if results["sorted_failed"]:
        most_active = {
            "ip": results["sorted_failed"][0][0],
            "failed_attempts": results["sorted_failed"][0][1]
        }

    return {

        "suspicious_ips": suspicious_ips,

        "enumeration_ips": enumeration_ips,

        "compromised_accounts": sorted(compromised_accounts),

        "targeted_accounts":
            dict(targeted_accounts.most_common()),

        "most_active_attacker": most_active,

        "ioc_count":
            len(suspicious_ips)
            + len(enumeration_ips)
            + len(compromised_accounts)
    }