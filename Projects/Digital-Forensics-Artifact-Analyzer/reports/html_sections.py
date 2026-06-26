def summary_section(results):
    return f"""
<div class="summary">

    <div class="card total">
        <h3>Total Lines</h3>
        <p>{results["total_lines"]}</p>
    </div>

    <div class="card failed">
        <h3>Failed Logins</h3>
        <p>{results["total_failed"]}</p>
    </div>

    <div class="card success-card">
        <h3>Successful Logins</h3>
        <p>{results["total_successful"]}</p>
    </div>

    <div class="card unique">
        <h3>Unique Failed IPs</h3>
        <p>{len(results["failed_attempts"])}</p>
    </div>

</div>
"""

def failed_analysis_section(results):

    rows = ""

    for ip, count in results["failed_attempts"].items():

        users = len(results["failed_users"][ip])

        badge = (
            '<span class="badge danger">YES</span>'
            if users >= 3
            else '<span class="badge success">NO</span>'
        )

        rows += f"""
<tr>
<td>{ip}</td>
<td>{count}</td>
<td>{users}</td>
<td>{badge}</td>
</tr>
"""

    return f"""
<h2>Suspicious Failed Login Analysis</h2>

<table>

<tr>

<th>IP Address</th>

<th>Failed Attempts</th>

<th>Unique Users</th>

<th>Enumeration</th>

</tr>

{rows}

</table>
"""

def top_failed_section(results, top_n):

    rows = ""

    for ip, count in results["sorted_failed"][:top_n]:
        rows += f"""
<tr>
    <td>{ip}</td>
    <td>{count}</td>
</tr>
"""

    return f"""
<h2>Top Failed Attempts</h2>

<table>

<tr>
<th>IP Address</th>
<th>Failed Attempts</th>
</tr>

{rows}

</table>
"""

def suspicious_section(results, threshold):

    rows = ""

    for ip, count in results["sorted_failed"]:

        if count < threshold:
            break

        rows += f"""
<tr>
    <td>{ip}</td>
    <td>{count}</td>
</tr>
"""

    if rows == "":
        rows = """
<tr>
<td colspan="2">No suspicious IPs found.</td>
</tr>
"""

    return f"""
<h2>Suspicious IPs (≥ {threshold} Attempts)</h2>

<table>

<tr>
<th>IP Address</th>
<th>Failed Attempts</th>
</tr>

{rows}

</table>
"""

def alerts_section(results):

    rows = ""

    if results["success_after_failure"]:

        for alert in results["success_after_failure"]:

            rows += f"""
<tr>
<td>{alert["ip"]}</td>
<td>{alert["username"]}</td>
<td>{alert["timestamp"]}</td>
</tr>
"""

    else:

        rows = """
<tr>
<td colspan="3">No alerts detected.</td>
</tr>
"""

    return f"""
<h2>Potential Account Compromise Alerts</h2>

<table>

<tr>
<th>IP Address</th>
<th>Username</th>
<th>Timestamp</th>
</tr>

{rows}

</table>
"""

def timeline_section(results):

    rows = ""

    for event in results["event_timeline"][-5:]:

        status = (
            '<span class="badge success">Successful</span>'
            if event["status"] == "Successful"
            else '<span class="badge danger">Failed</span>'
        )

        rows += f"""
<tr>
<td>{event["timestamp"]}</td>
<td>{status}</td>
<td>{event["username"]}</td>
<td>{event["ip"]}</td>
</tr>
"""

    return f"""
<h2>Recent Event Timeline</h2>

<table>

<tr>
<th>Timestamp</th>
<th>Status</th>
<th>Username</th>
<th>IP Address</th>
</tr>

{rows}

</table>
"""

def recommendation_section():

    return """
<h2>Security Analyst Recommendations</h2>

<ul>

<li>Investigate IPs exceeding the failed login threshold.</li>

<li>Review accounts with successful logins after multiple failures.</li>

<li>Enable Multi-Factor Authentication (MFA).</li>

<li>Consider blocking repeated offending IP addresses.</li>

</ul>
"""

def ioc_section(results):

    iocs = results["iocs"]

    suspicious = "<br>".join(iocs["suspicious_ips"]) or "None"
    enumeration = "<br>".join(iocs["enumeration_ips"]) or "None"
    compromised = "<br>".join(iocs["compromised_accounts"]) or "None"

    attacker = iocs["most_active_attacker"]

    attacker_text = (
        f'{attacker["ip"]} ({attacker["failed_attempts"]} Attempts)'
        if attacker
        else "None"
    )

    return f"""
<h2>Indicators of Compromise (IOCs)</h2>

<table>

<tr>
<th>Category</th>
<th>Details</th>
</tr>

<tr>
<td><span class="badge danger">Suspicious IPs</span></td>
<td>{suspicious}</td>
</tr>

<tr>
<td><span class="badge warning">Enumeration IPs</span></td>
<td>{enumeration}</td>
</tr>

<tr>
<td><span class="badge success">Compromised Accounts</span></td>
<td>{compromised}</td>
</tr>

<tr>
<td>Most Active Attacker</td>
<td>{attacker_text}</td>
</tr>

<tr>
<td><strong>Total IOC Count</strong></td>
<td><strong>{iocs["ioc_count"]}</strong></td>
</tr>

</table>
"""

def threat_section(results):

    high = "<br>".join(results["threat"]["high"]) or "None"
    medium = "<br>".join(results["threat"]["medium"]) or "None"
    low = "<br>".join(results["threat"]["low"]) or "None"

    return f"""
<h2>Threat Assessment</h2>

<table>

<tr>
<th>Priority</th>
<th>IP Addresses</th>
</tr>

<tr>
<td><span class="badge danger">HIGH</span></td>
<td>{high}</td>
</tr>

<tr>
<td><span class="badge warning">MEDIUM</span></td>
<td>{medium}</td>
</tr>

<tr>
<td><span class="badge success">LOW</span></td>
<td>{low}</td>
</tr>

</table>
"""