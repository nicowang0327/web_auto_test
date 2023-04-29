import subprocess
from datetime import datetime

def generate_report():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = f"report/report_{timestamp}.html"
    cmd = f"pytest --html={report_path} --self-contained-html"
    subprocess.run(cmd, shell=True, check=True)

if __name__ == "__main__":
    generate_report()
