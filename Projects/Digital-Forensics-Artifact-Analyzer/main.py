import argparse
from analyzer import analyze_log   #Importing from other folders
from report_generator import print_report,save_report


parser = argparse.ArgumentParser(
    description="Digital Forensics Artifact Analyzer"
)

parser.add_argument("logfile",help="Path to authentication log file")

parser.add_argument(
    "--savefile",
    default="reports/report.txt",
    help="Output report file"
)


parser.add_argument(
    "--top_n",
    type=int,
    default=3,
    help="Number of top failed IPs to display"
)

parser.add_argument(
    "--threshold",
    type=int,
    default=5,
    help="Minimum failed attempts to mark as suspicious"
)

args = parser.parse_args()

try:
    results = analyze_log(args.logfile)

    print_report(
        results,
        threshold=args.threshold,
        top_n=args.top_n
    )
    save_report(
        results,
        filename=args.savefile,
        threshold=args.threshold,
        top_n=args.top_n
    )
except FileNotFoundError as e:
    print(f"Error: '{e}' not found.")

except Exception as e:
    print(f"Unexpected error: {e}")









