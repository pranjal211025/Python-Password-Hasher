import hashlib
import random
import string

print("=========================================")
print("  Random Password & Hasher - by Pranjal  ")
print("=========================================")

# 12 characters ka strong random password banane ki setting
length = 12
# Isme ABCD (letters), 1234 (digits), aur symbols (punctuation) mix kiye hain
chars = string.ascii_letters + string.digits + string.punctuation

# Loop chala kar ek-ek random character chunna aur password banana
random_pass = ''.join(random.choice(chars) for _ in range(length))

print("[+] Generated Password : " + random_pass)

# Naye password ko hash me convert karna
encoded_pass = random_pass.encode()
md5_hash = hashlib.md5(encoded_pass).hexdigest()
sha256_hash = hashlib.sha256(encoded_pass).hexdigest()

print("\n[+] Hashes for this password:")
print("MD5:     " + md5_hash)
print("SHA-256: " + sha256_hash)
print("=========================================")
