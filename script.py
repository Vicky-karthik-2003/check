import os
from datetime import datetime

print("I am from workflow 1")
print(f"Workflow name : {os.getenv('GITHUB_WORKFLOW')}")
print(f"Run ID        : {os.getenv('GITHUB_RUN_ID')}")
print(f"Run Number    : {os.getenv('GITHUB_RUN_NUMBER')}")
print(f"Repository    : {os.getenv('GITHUB_REPOSITORY')}")
print(f"Triggered by  : {os.getenv('GITHUB_ACTOR')}")
print(f"Timestamp     : {datetime.utcnow()} UTC")
