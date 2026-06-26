from parsers.auth_parser import parse_log


def analyze_log(file_path):
    
    #Analyze authentication logs and return summary statistics.
    

    failed_attempts = {}
    failed_users = {}
    successful_attempts = {}
    total_lines = 0
    failed_ips = set()
    success_after_failure = []
    event_timeline = []

    with open(file_path, "r") as file:

        for line in file:

            parsed_data = parse_log(line)
            event_timeline.append(parsed_data)

            ip = parsed_data["ip"]
            username = parsed_data["username"]
            total_lines += 1

            if parsed_data["status"] == "Failed":
                failed_attempts[ip] = failed_attempts.get(ip, 0) + 1
                if ip not in failed_users:
                    failed_users[ip] = set()
                failed_users[ip].add(username)  
                failed_ips.add(ip)
            

            elif parsed_data["status"] == "Successful":
                successful_attempts[ip] = successful_attempts.get(ip, 0) + 1
                failed_count = failed_attempts.get(ip, 0)

                if failed_count >= 3:
                    alert = {
                                "ip": ip,
                                "username": username,
                                "timestamp": parsed_data["timestamp"]
                            }
                    success_after_failure.append(alert)
            
    total_failed = sum(failed_attempts.values())
    total_successful = sum(successful_attempts.values())

    sorted_failed = sorted(
        failed_attempts.items(),
        key=lambda item: item[1],
        reverse=True
    )
    
   
    event_timeline = sorted(event_timeline,key=lambda event: event["timestamp"])
    return {
        "total_lines": total_lines,
        "failed_attempts": failed_attempts,
        "successful_attempts": successful_attempts,
        "total_failed": total_failed,
        "total_successful": total_successful,
        "sorted_failed": sorted_failed,
        "failed_users" : failed_users,
        "success_after_failure" : success_after_failure,
        "event_timeline": event_timeline
    }