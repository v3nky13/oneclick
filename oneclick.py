import jenkins
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Jenkins credentials
JENKINS_URL = os.getenv("JENKINS_URL")
JENKINS_USERNAME = os.getenv("JENKINS_USERNAME")
JENKINS_PASSWORD = os.getenv("JENKINS_PASSWORD")

# Initialize Jenkins server connection
server = jenkins.Jenkins(JENKINS_URL, username=JENKINS_USERNAME, password=JENKINS_PASSWORD)

# Job name and configuration XML
JOB_NAME = "MyJob"
with open("job_config.xml", "r") as f:
    CONFIG_XML = f.read()

# Check if job exists
if server.job_exists(JOB_NAME):
    print(f"Updating existing job: {JOB_NAME}")
    server.reconfig_job(JOB_NAME, CONFIG_XML)
else:
    print(f"Creating new job: {JOB_NAME}")
    server.create_job(JOB_NAME, CONFIG_XML)

# Trigger a build
server.build_job(JOB_NAME)
print(f"Job {JOB_NAME} triggered!")
