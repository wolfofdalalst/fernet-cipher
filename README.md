# Fernet Cipher
Encrypt files using the command line and [cryptography](https://pypi.org/project/cryptography/) library.

## Installation
Clone this repository into your local machine using these commands and install the necessary dependencies
```bash
git clone https://github.com/GuptaAyush19/fernet-cipher.git
cd fernet-cipher
pip3 install -r requirements.txt
```
Or execute this remote bash script
```
wget -O - https://raw.githubusercontent.com/guptaayush19/fernet-cipher/master/scripts/install.sh | bash
```

## Execution
First to encrypt/decrypt files, we will need an encryption key. To generate an encryption run this python script present at the root of this repository. A new file with a unique ID is saved in *fernet_key_library/*
```
python3 generate_key.py
```
Finally to encrypt/decrypt refer to this command
```
~/fernet-cipher$ python3 main.py -h
usage: main.py [-h] --file FILE --key KEY --mode MODE

Encrypt Files using Fernet encryption

optional arguments:
  -h, --help   show this help message and exit
  --file FILE  file to be encrypted/decrypted
  --key KEY    file with fernet 32-bit key
  --mode MODE  encrypt/decrypt
```
Example use case
```
python3 main.py --file README.md --key fernet_key_library/<unique id> --mode encrypt
```

## Contribution
Contributions and improvements are welcome. If you have any suggestions or want to contribute, please feel free to open an issue or submit a pull request

## License
This repository falls under MIT License. Feel free to use, share, and modify this package as you see fit.
