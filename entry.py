from . import main, crypto
import json, random, os


def entry(person=""):
    # check person
    hash_val = crypto.get_hash(person)
    with open("/Users/a2/.cache/database/data/files.json", "r") as f:
        dictionary = json.load(f)
    # check if handle exists in dictionary
    if hash_val in dictionary.keys():
        json_of_filepaths = dictionary[hash_val]
        files_path = f"/Users/a2/.crypted/database/bin/{json_of_filepaths}.json" # not encrypted
    else: # create new file for the handler
        temp_name = f"{random.randrange(10000000, 999999999)}.txt"
        while temp_name in os.listdir("/Users/a2/.crypted/database/bin"):
            temp_name = f"{random.randrange(10000000, 999999999)}.txt"
        # temp_name is new name of txt with filenames
        dictionary[hash_val] = temp_name
        with open("/Users/a2/.cache/database/data/files.json", "w") as f:
            json.dump(dictionary, f)
        # create empty json array file
        dd = []
        with open(f"/Users/a2/.crypted/database/bin/{temp_name}.json", "w") as f:
            json.dump(dd, f)
        files_path = f"/Users/a2/.crypted/database/bin/{temp_name}.json"
    # take input