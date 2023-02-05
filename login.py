from . import error
import time, sys
from getpass import getpass


def check_login() -> None:
    with open("/Users/a2/.crypted/logs/pw.txt", "r") as f:
        t = int(f.read())
    if t != "":
        now = int(time.time())
        # cooldown
        d = 60
        # check for time
        if now - t < d:
            error.report_issue(f"Tried to access before cooldown ended: {now}\n")
            exit(0)
        # cooldown passed
        open("/Users/a2/.crypted/logs/pw.txt", "w").close()


def login() -> None:
    pw = getpass()
    if pw != "rotwein": # encrypt
        error.report_issue(f"Wrong password when authorizing: {int(time.time())}\n")
        error.failed()
        sys.exit(0)