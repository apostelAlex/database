from . import crypto
import json

def get_data(person:str):
    hash_key = crypto.get_hash(person)
    # lookup
    dictionary_file = "/Users/a2/.cache/database/data/files.json"
    with open(dictionary_file, "r") as f:
        dictionary = json.load(f)
    val = dictionary[hash_key]
    data_path = f"/Users/a2/.cache/database/data/bin/{val}.bin"
    with open(data_path, "rb") as f:
        binary = f.read()
    crypto.decrypt(data=binary, key=None)