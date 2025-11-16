import getpass
import hashlib

print("=== Insecure Login System ===")
# X Insecure section (AI-generated style)
username = "admin"
password = "1234"
user = input("Enter username: ")
pwd = input("Enter password: ")
if user == username and pwd == password:
	print("Login successful! (Insecure system)")
else:
	print("Invalid credentials. (Insecure system)")

print("\n=== Secure Login System ===")
# Secure section (with hashing)
stored_user = "admin"
stored_pass_hash = hashlib.sha256("1234".encode()).hexdigest()
user2 = input("Enter username: ")
pwd2 = getpass.getpass("Enter password: ")
pwd_hash = hashlib.sha256(pwd2.encode()).hexdigest()
if user2 == stored_user and pwd_hash == stored_pass_hash:
	print("Login successful! (Secure system)")
else:
	print("Invalid credentials. (Secure system)")