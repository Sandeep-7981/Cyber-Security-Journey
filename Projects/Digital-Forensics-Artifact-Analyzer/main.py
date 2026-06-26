import os
import argparse
from analyzer.detection import analyze_log   #Importing from other folders
from reports.txt_report import print_report,save_report
from reports.html_report import generate_html_report
from reports.json_report import generate_json_report
from reports.csv_report import generate_csv_report
from analyzer.ioc import extract_iocs
from analyzer.threat import generate_threat_assessment

parser = argparse.ArgumentParser(
    description="Digital Forensics Artifact Analyzer"
)

parser.add_argument("logfile",help="Path to authentication log file")

parser.add_argument(
    "--savefile",
    default="output/report.txt",
    help="Output report file"
)

parser.add_argument(
    "--json",
    action="store_true",
    help="Generate JSON report"
)

parser.add_argument(
    "--csv",
    action="store_true",
    help="Generate CSV report"
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

parser.add_argument(
    "--html",
    action="store_true",
    help="Generate HTML report"
)

args = parser.parse_args()

try:
    results = analyze_log(args.logfile)
    from analyzer.ioc import extract_iocs
    from analyzer.threat import generate_threat_assessment
    results["iocs"] = extract_iocs(
    results,
    threshold=args.threshold
    )

    results["threat"] = generate_threat_assessment(
        results,
        threshold=args.threshold
    )
    os.makedirs("output", exist_ok=True)

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

    if args.html:
        generate_html_report(
            results,
            output_file="output/report.html",
            threshold=args.threshold,
            top_n=args.top_n
        )

        print("\nHTML report saved to output/report.html")
    
    if args.json:
        generate_json_report(
            results,
            "output/report.json",
            threshold=args.threshold,
            top_n=args.top_n
        )
    
    if args.csv:
        generate_csv_report(
            results,
            "output/report.csv",
            threshold=args.threshold,
            top_n=args.top_n
        )
   
except FileNotFoundError as e:
    print(f"Error: '{e}' not found.")

except Exception as e:
    print(f"Unexpected error: {e}")









