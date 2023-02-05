from . import crypto, error
import json, time

def get_data(person:str) -> None:  # possibly -> str
    hash_val = crypto.get_hash(person)
    # lookup
    dictionary_file = "/Users/a2/.cache/database/data/files.json"
    with open(dictionary_file, "r") as f:
        dictionary = json.load(f)
    try:
        val = dictionary[hash_val]
        data_path = f"/Users/a2/.cache/database/data/bin/{val}.bin"
        with open(data_path, "rb") as f:
            binary = f.read()
        crypto.decrypt(data=binary, key=None)
    except:
        # wrong handle provided
        error.report_issue(f"Tried to access unknown handle: {int(time.time())}\n")
        print("You have entered wrong input. Please log in again.")

def check(person="") -> None:
    # if exists, number of entries, first entry, last
    hash_val = crypto.get_hash(person)
    # lookup
    dictionary_file = "/Users/a2/.cache/database/data/files.json"
    with open(dictionary_file, "r") as f:
        dictionary = json.load(f)
    try:
        dictionary[hash_val]
    except:
        print("This person does not exist.")
        error.report_issue(f"Person they checked does not exist: {int(time.time())}\n")
