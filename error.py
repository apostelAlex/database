from . import main
import time


def report_issue(string):
    with open("/Users/a2/.crypted/logs/temp.txt", "a") as f:
        f.write(string)   


def fetch_issues():
    with open("/Users/a2/.crypted/logs/temp.txt", "r") as f:
        fi = f.read()
    if fi != "":
        print(fi)
        # remove_issues
        open("/Users/a2/.crypted/logs/temp.txt", "w").close()


def failed():
    with open("/Users/a2/.crypted/logs/pw.txt", "w") as f:
        f.write(str(int(time.time())))