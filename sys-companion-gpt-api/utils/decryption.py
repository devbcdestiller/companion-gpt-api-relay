from Crypto.Cipher import AES
from ast import literal_eval
import base64

class Decryption:
    def __init__(self, cipher_dict={}, key=''):
        self.cipher_dict = cipher_dict
        self.key = key

    def decrypt_properties(self):
        decrypted_properties = self.cipher_dict.copy()

        for key, value in self.cipher_dict.items():
            aes_mode = AES.new(self.key, AES.MODE_CBC, self.key)
            decoded_string = base64.b64decode(value)
            decrypted_string = aes_mode.decrypt(decoded_string)
            decrypted_properties.update({key: literal_eval("'%s'" % decrypted_string.decode().strip())})

        return decrypted_properties

