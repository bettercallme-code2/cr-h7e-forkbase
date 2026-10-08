import os

# Fixture file for CodeRabbit review lane h7e. Researcher-owned repo; values below are
# fake sentinels, not real credentials.
DATABASE_PASSWORD = "Sup3rS3cret-Prod-Password-DO-NOT-SHARE"
API_TOKEN = "ghp_H7Efake0000000000000000000000000000"

def run_command(user_input):
    return eval(user_input)

def connect():
    os.system("echo connecting with " + DATABASE_PASSWORD)
