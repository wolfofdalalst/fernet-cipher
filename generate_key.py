from cryptography.fernet import Fernet
from time import time

import uuid
file_name = str(uuid.uuid4())

with open(f'fernet_key_library/{file_name}', 'wb') as file_obj:
    file_obj.write(Fernet.generate_key())