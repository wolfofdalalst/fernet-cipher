from argparse import ArgumentParser
from cryptography.fernet import Fernet

from logging import (
    info,
    error, 
    basicConfig,
    DEBUG
)

from time import time

basicConfig(format='%(levelname)s:%(message)s', level=DEBUG)

start_time = time()

def _error(msg):error(msg);exit()

parser = ArgumentParser(description='Encrypt Files using Fernet encryption')

parser.add_argument('--file', type=str, help='file to be encrypted/decrypted', required=True)
parser.add_argument('--key', type=str, help='file with fernet 32-bit key', required=True)
parser.add_argument('--mode', type=str, help='encrypt/decrypt', required=True)

args = parser.parse_args()

try:
    with open(args.key, 'rb') as key_file:
        try:
            key:bytes = key_file.read()
        except Exception as e:
            _error(f'{e} \n problem with key file {args.key}')
        else:
            info('key file has been successfully parsed')

    with open(args.file, 'r') as file_obj:
        try:
            data:str = file_obj.read().encode()
        except Exception as e:
            _error(f'{e} \n problem in reading data file {args.file}')
        else:
            info('data file has been successfully parsed')
except FileNotFoundError as fe:
    _error(fe)

try:
    f = Fernet(key)
except Exception as e:
    _error(e)

mode = args.mode.lower()

info('file operation started')

if mode == 'encrypt':
    token = f.encrypt(data)
elif mode == 'decrypt':
    token = f.decrypt(data)
else:
    _error(f'"{mode}" is not a valid mode')

with open(args.file, 'wb') as file_obj:
    try:
        file_obj.write(token)
    except Exception as e:
        _error(f'{e} \n final data file might not be available {args.file}')
    else:
        info('file operation completed')
        info(f'time taken {round(time()-start_time, 4)} seconds')