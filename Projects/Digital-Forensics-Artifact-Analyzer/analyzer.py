from parsers.auth_parser import parse_log


def analyze_log(file_path):
    
    #Analyze authentication logs and return summary statistics.
    

    failed_attempts = {}
    successful_attempts = {}
    total_lines = 0

    with open(file_path, "r") as file:

        for line in file:

            parsed_data = parse_log(line)

            ip = parsed_data["ip"]
            total_lines += 1

            if parsed_data["status"] == "Failed":
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1

            elif parsed_data["status"] == "Successful":
                successful_attempts[ip] = successful_attempts.get(ip, 0) + 1

    total_failed = sum(failed_attempts.values())
    total_successful = sum(successful_attempts.values())

    sorted_failed = sorted(
        failed_attempts.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return {
        "total_lines": total_lines,
        "failed_attempts": failed_attempts,
        "successful_attempts": successful_attempts,
        "total_failed": total_failed,
        "total_successful": total_successful,
        "sorted_failed": sorted_failed,
    }