# Python hashing code (MD5 + SHA-256)
import hashlib
text = input("Enter text: ")
md5_hash = hashlib.md5(text.encode()).hexdigest()
print("MD5:", md5_hash)
sha_hash = hashlib.sha256(text.encode()).hexdigest()
print("SHA-256:", sha_hash)
