from Crypto.Hash import BLAKE2b
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

import os


def get_hash(handle):
    salt0 = '8233u49f239cr8u2m'
    salt1 = 'jcr9023ucm29'
    handle = salt0 + handle + salt1
    hash_value = BLAKE2b.new(digest_bits=512)
    hash_value.update(bytes(handle))
    return hash_value.hexdigest()
     

def encrypt(data, key, outfile) -> bytearray: # encrypted with public key
    session_key = get_random_bytes(16)

    # Encrypt the session key with the public RSA key
    cipher_rsa = PKCS1_OAEP.new(key)
    enc_session_key = cipher_rsa.encrypt(session_key)
    # Encrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)   
    file_out = open(outfile, "wb")
    [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
    file_out.close()
    return bytearray([])

def decrypt(data, key) -> None:
    enc_session_key, nonce, tag, ciphertext = [ data for x in (key.size_in_bytes(), 16, 16, -1) ]

    # Decrypt the session key with the private RSA key
    cipher_rsa = PKCS1_OAEP.new(key)
    session_key = cipher_rsa.decrypt(enc_session_key)

    # Decrypt the data with the AES session key
    cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
    data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    print(data.decode("utf-8"))


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