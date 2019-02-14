from Crypto import Random
from Crypto.PublicKey import RSA
import base64

modulus_length = 256*7
privatekey = RSA.generate(modulus_length, Random.new().read)
publickey = privatekey.publickey()
print(privatekey.exportKey().decode())
print(publickey.exportKey().decode())
