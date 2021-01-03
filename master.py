from cryptography.fernet import Fernet


def generate_key():
	"""
	Key generation and saving it into the file
	"""
	key = Fernet.generate_key()
	with open('secret.key', 'wb') as f:
		f.write(key)


def load_key():
	"""
	Loading key from file
	"""
	return open('secret.key', 'rb').read()


def encrypt_master(message):
	"""
	Encrypting new master password and set it (saving into file)
	"""
	key = load_key()
	message = message.encode()
	fer = Fernet(key)
	new_master = fer.encrypt(message)
	with open('master_password.txt', 'wb') as f:
		f.write(new_master)


def decrypt_master():
	"""
	Get master password to check user access (reading from file and decrypting)
	"""
	key = load_key()
	fer = Fernet(key)
	with open ('master_password.txt', 'rb') as f:
		master_pass = f.read()
	return fer.decrypt(master_pass)


def init_master():
	"""
	Initializing a password for first using as default (can be changed in future)
	"""
	generate_key()
	encrypt_master('default')
