import pyxxtea, hashlib, base64

## Simple class to move crypto code away from convo.py
## Experimental, not guaranteed to be consistent between versions

class cryptoManager:
	def __init__(self, presharedSecret, extraSalt=""):
		self.mainSalt = "MSPA_HOMESTUCK_PESTERCHUM_SALTY_SALT_"
		self.extraSalt = extraSalt
		self.iterations = 256
		self.setSecret(presharedSecret)
	def setSecret(self, presharedSecret):
		self.key = self.kdf(presharedSecret)
		self.algo = pyxxtea.XXTEA(self.key)
	def getKey(self):
		return self.key
	def kdf(self, presharedSecret):
		## key derivation function
		key = hashlib.sha512(self.mainSalt + self.extraSalt + presharedSecret).digest()
		for i in range(self.iterations):
			key = hashlib.sha512(self.mainSalt + self.extraSalt + str(i) + key).digest()
		return key[:16]
	def encrypt(self, msg):    
		self.algo.initCTR()
		return self.algo.encryptCTR(msg)
	def decrypt(self, msg):
		self.algo.initCTR()
		return self.algo.decryptCTR(msg)
	def encode(self, msg):
		return base64.b64encode(msg)
	def decode(self, msg):
		return base64.b64decode(msg)