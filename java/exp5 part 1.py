from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
key = b'mysecretkey'  # Key must be bytes
data = b'HelloWorld'  # Data must be bytes
cipher = Blowfish.new(key, Blowfish.MODE_ECB)
ciphertext = cipher.encrypt(pad(data, 8))
print("Encrypted:", ciphertext.hex())
decrypted = unpad(cipher.decrypt(ciphertext), 8)
print("Decrypted:", decrypted.decode())
