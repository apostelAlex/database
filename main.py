import entry, error, crypto, get, login
import time

# cache/db/data/files.json -> hashes for file data
# private key stored in a hard drive
# public key stored in .cache and .crypted folder.

# bin-filepaths in a json
# json with bin-filepaths named after key of the hash of the handle



def handler(enc_key):
    inn = input("Enter...\n")

    args = inn.split(" ")
    if args[0].lower() == "entry":
        if len(args)>=4:
            entry.entry(args.pop(0))
        else:
            error.report_issue(f"Wrong Syntax in entry call: {time.time()}\n")
            print("Syntax: entry %handle -f %pathoffile")
    elif args[0].lower() == "sd":
        error.selfdestruct()
    elif args[0].lower() == "get":
        dec_key = crypto.get_private_key()
        try:
            get.get_data(args[1])
        except IndexError:
            person = input("What handle do you want to have?")
            get.get_data(person)
    elif args[0].lower() == "errinfo":
        error.fetch_issues()  
    elif args[0].lower() == "check": # if exists: number of entries, first entry, last
        try:
            get.get_data(args[1])
        except IndexError:
            person = input("What handle do you want to have?")
            get.get_data(person)
    elif args[0].lower() == "exit":
        exit(0)
    else: #wrong input format
        error.report_issue(f"Tried to submit illegal input in handler: {int(time.time())}\n")
        print("Illegal input. ")
    handler(enc_key)



def main():
    crypto.selfcheck()
    login.check_login()
    login.login() # password

    pub_key = "/Users/a2/.cache/database/id_rsa.pub" # address for the key of the main database encryption

    # every entry is encrypted with its own AES session key.
    
    with open(pub_key, "rb") as f:
        enc_key = f.read() # needed for the encryption of the AES key
    
    handler(enc_key)



    
    

if __name__ == "__main__":
    MODE = "P"  # Personen; other: S (Secrets)
    main()




# log persons: 
#   encrypt temp.txt file
