import pyjks
from Crypto.Cipher import AES


class CryptoUtil(Object):
	def read_secret_key(slef, keystore_path, key_password):

		pass

	def encrypt(self, message, secret_key, iv):
		'''
		IV must be 16 bytes long
		secret_key
		message must be a multiple of 16 in length
		(secret_key)AES key must be either 16, 24, or 32 bytes long
		'''
		AES.new(secret_key, AES.MODE_CBC, iv)
		pass

		def decrypt(self, secret_key):
			pass 