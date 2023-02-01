from getpass import getpass
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import sys
import os
import random
import json
import time


from . import entry, error, crypto, get


# cache/db/data/files.json -> hashes for file data
# private key stored in a hard drive
# public key stored in .cache and .crypted folder.

# bin-filepaths in a json
# json with bin-filepaths named after key of the hash of the handle



def check_login():
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




def main():
    crypto.selfcheck()
    pw = getpass()
    pub_key = "/Users/a2/.cache/database/id_rsa.pub" # address for the key of the main database encryption
    check_login()

    # every entry is encrypted with its own AES session key.

    if pw != "rotwein": # encrypt
        error.report_issue(f"Wrong password when authorizing: {int(time.time())}")
        error.failed()
        sys.exit(0)
    
    with open(pub_key, "rb") as f:
        enc_key = f.read()
    
    inn = input("Enter...\n")

    args = inn.split(" ")
    if args[0].lower() == "entry":
        if len(args)>1:
            entry.entry(args.pop(0))
        entry.entry()
    if args[0].lower() == "get":
        dec_key = crypto.get_private_key()
        get.get_data(args[1])
    if args[0].lower() == "append":
        pass
        #append to a handle


    
    

if __name__ == "__main__":
    MODE = "P"  # Personen; other: S (Secrets)
    main()




# log persons: 
#   encrypt temp.txt file
