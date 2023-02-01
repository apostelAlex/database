from . import main
from Crypto.Hash import BLAKE2b

import os


def get_hash(handle):
    salt0 = '8233u49f239cr8u2m'
    salt1 = 'jcr9023ucm29'
    handle = salt0 + handle + salt1
    hash_value = BLAKE2b.new(digest_bits=512)
    hash_value.update(bytes(handle))
    return hash_value.hexdigest()
     

def encrypt(data, key):
    pass

def decrypt(data, key):
    pass

def get_private_key():
    # check file on drive
    # check in volumes (might change for security reasons)
    volumes = os.listdir("/Volumes")
    for v in volumes:
        if v == 'Macintosh HD':
            continue
        if '.sec' in os.listdir(f'/Volumes/{v}'):
            if 'bin' in os.listdir(f'/Volumes/{v}'):
                exit(3) # file not found
            if 'cc.c' in os.listdir(f'/Volumes/{v}/bin'):
                exit(3) # file not found
            try:
                with open(f'/Volumes/{v}/.sec/id_rsa') as f:
                    return 
            except: exit(3)

def compute_checksum(path_of_file):
    pass
    # todo

def selfcheck():
    # checks if its right 
    file_path_checksum = ""
    pass