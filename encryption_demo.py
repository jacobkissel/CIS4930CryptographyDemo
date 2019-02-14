import sys
from cryptography.fernet import Fernet
from Crypto.Signature import PKCS1_PSS as pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import base64

def clear() :
	cl = "\n" * 100
	print(cl)

def cyclically_adjust_number(number, min, max) :
	adjusted_num = number
	if number < min :
		diff = min - number
		adjusted_num = (max + 1) - diff
	elif number > max :
		diff = number - max
		adjusted_num = (min - 1) + diff
	return adjusted_num

def rot_ascii(character, rot_amt) :
	char_ascii = ord(character)
	newchar_ascii = 0;
	if char_ascii <= 90 and char_ascii >= 65 : # its an uppercase letter
		char_ascii += rot_amt
		newchar_ascii = cyclically_adjust_number(char_ascii, 65, 90)
	elif char_ascii <= 122 and char_ascii >= 97 : # its a lowercase letter
		char_ascii += rot_amt
		newchar_ascii = cyclically_adjust_number(char_ascii, 97, 122)
	return chr(newchar_ascii)

def rot_cipher(text, rot_amt) :
	encrypted_text = ""
	for letter in text :
		encrypted_text += rot_ascii(letter, rot_amt)
	return encrypted_text

def rot_cipher_decrypt(text,rot_amt) :
	decrypted_text = ""
	for letter in text :
		decrypted_text += rot_ascii(letter, (-1*rot_amt))
	return decrypted_text

def make_map(string1, string2) :
	length = len(string1)
	ret_map = {'' : ''}
	for i in range(0, length) :
		ret_map[string1[i]] = string2[i]
	return ret_map

def map_cipher(text, alpha_map) :
	lower_alpha_str = alpha_map.lower()
	upper_alpha_str = alpha_map.upper()
	cipher_map = make_map("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", lower_alpha_str + upper_alpha_str)
	encrypted_text = ""
	for char in text :
		if char in cipher_map :
			encrypted_text += cipher_map[char]
		else :
			encrypted_text += char
	return encrypted_text

def map_cipher_decrypt(text, alpha_map) :
	lower_alpha_str = alpha_map.lower()
	upper_alpha_str = alpha_map.upper()
	cipher_map = make_map(lower_alpha_str + upper_alpha_str, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
	decrypted_text = ""
	for char in text :
		if char in cipher_map :
			decrypted_text += cipher_map[char]
		else :
			decrypted_text += char
	return decrypted_text

def sym_encrypt(text, sym_key) :
	encoded_text = text.encode()
	key = Fernet(sym_key.encode())
	encrypted = key.encrypt(encoded_text)
	return encrypted.decode()

def sym_decrypt(text, sym_key) :
	key = Fernet(sym_key.encode())
	decrypted = key.decrypt(text.encode())
	decrypted_text = decrypted.decode()
	return decrypted_text

def asym_encrypt(text, in_pub_key) :
	pub_key = RSA.importKey(base64.b64decode(in_pub_key))
	encrypted_msg = pub_key.encrypt(text.encode(), 32)[0]
	encoded_encrypted_msg = base64.b64encode(encrypted_msg).decode()
	return encoded_encrypted_msg

def asym_decrypt(text, in_priv_key) :
	priv_key = RSA.importKey(base64.b64decode(in_priv_key))
	decoded_encrypted_msg = base64.b64decode(text.encode())
	decrypted_msg = priv_key.decrypt(decoded_encrypted_msg).decode()
	return decrypted_msg

def asym_dig_signature(text, priv_key) :
	private_key = RSA.importKey(base64.b64decode(priv_key))
	h = SHA256.new(text.encode())
	signature = pss.new(private_key).sign(h)
	return base64.b64encode(signature).decode()

def asym_dig_signature_verify(signature, text, pub_key) :
	public_key = RSA.importKey(base64.b64decode(pub_key))
	h = SHA256.new(text.encode())
	verifier = pss.new(public_key)
	ret_string = ""
	try :
		if verifier.verify(h, base64.b64decode(signature.encode())) :
			ret_string = "\nThe signature is VALID for the given sender's public key and message text"
		else :
			ret_string = "\nThe signature is INVALID for provided public key and message"
	except (ValueError, TypeError) as error:
		ret_string = "\n\nERROR: "
		ret_string += error
	return ret_string

def rotational_options() :
	while(True) :
		clear()
		print("\nType the number of the option you would like to choose and press ENTER\n")
		print ("0. Go back")
		print ("1. Use a rotation cipher to encrypt a message")
		print ("2. Use a rotation ciper to decrypt a message")
		selection = input()
		if(selection == "0") :
			return
		elif (selection == "1") :
			clear()
			print("\nEnter an integer rotation amount")
			rot_amt = int(input())
			print("\nEnter some text to encrypt")
			text = input()
			print("\n######## Begin encrypted text ########\n")
			print(rot_cipher(text,rot_amt))
			print("\n######### End encrypted text #########")
			print("\n(press ENTER to continue)")
			input()
		elif (selection == "2") :
			clear()
			print("\nEnter an integer rotation amount")
			rot_amt = int(input())
			print("\nEnter some text to decrypt")
			text = input()
			print("\n######## Begin decrypted text ########\n")
			print(rot_cipher_decrypt(text,rot_amt))
			print("\n######### End decrypted text #########")
			print("\n(press ENTER to continue)")
			input()
		else :
			return

def map_options() :
	while(True) :
		clear()
		print("\nType the number of the option you would like to choose and press ENTER\n")
		print ("0. Go back")
		print ("1. Use a map cipher to encrypt a message")
		print ("2. Use a map ciper to decrypt a message")
		selection = input()
		if(selection == "0") :
			return
		elif (selection == "1") :
			clear()
			print("\nEnter the 26 character map")
			alpha_map = input()
			print("\nEnter some text to encrypt")
			text = input()
			print("\n######## Begin encrypted text ########\n")
			print(map_cipher(text, alpha_map))
			print("\n######### End encrypted text #########")
			print("\n(press ENTER to continue)")
			input()
		elif (selection == "2") :
			clear()
			print("\nEnter the 26 character map")
			alpha_map = input()
			print("\nEnter some text to decrypt")
			text = input()
			print("\n######## Begin decrypted text ########\n")
			print(map_cipher_decrypt(text, alpha_map))
			print("\n######### End decrypted text #########")
			print("\n(press ENTER to continue)")
			input()
		else :
			return

def symmetric_options() :
	while(True) :
		clear()
		print("\nType the number of the option you would like to choose and press ENTER\n")
		print ("0. Go back")
		print ("1. Use a symmetric key to encrypt a message")
		print ("2. Use a symmetric key to decrypt a message")
		selection = input()
		if(selection == "0") :
			return
		elif (selection == "1") :
			clear()
			print("\nEnter the symmetric key to use for encryption")
			sym_key = input()
			print("\nEnter the text to encrypt")
			text = input()
			print("\n######## Begin encrypted text ########\n")
			print(sym_encrypt(text, sym_key))
			print("\n######### End encrypted text #########")
			print("\n(press ENTER to continue)")
			input()
		elif (selection == "2") :
			clear()
			print("\nEnter the symmetric key to use for decryption")
			sym_key = input()
			print("\nEnter the text to decrypt")
			text = input()
			print("\n######## Begin decrypted text ########\n")
			print(sym_decrypt(text, sym_key))
			print("\n######### End decrypted text #########")
			print("\n(press ENTER to continue)")
			input()
		else :
			return

def asymmetric_options() :
	while(True) :
		clear()
		print("\nType the number of the option you would like to choose and press ENTER\n")
		print ("0. Go back")
		print ("1. Use an asymmetric public key to encrypt a message")
		print ("2. Use an asymmetric private key to decrypt a message")
		print ("3. Use a private key and text to make a digital signature")
		print ("4. Use a public key and text to check a digital signature")
		selection = input()
		if(selection == "0") :
			return
		elif (selection == "1") : # asymmetric key
			clear()
			print("\nEnter the asymmetric public key to use for encryption (including the --begin key-- and --end key-- lines)")
			in_pub_key = ""
			while(True) :
				inpt = input()
				if(inpt == "-----BEGIN PUBLIC KEY-----") :
					continue
				elif(inpt == "-----END PUBLIC KEY-----" or inpt == "") : 
					break
				in_pub_key += inpt
			print("\nEnter the text to encrypt")
			text = input()
			print("\n######## Begin encrypted text ########\n")
			print(asym_encrypt(text, in_pub_key))
			print("\n######### End encrypted text #########")
			print("\n(press ENTER to continue)")
			input()
		elif (selection == "2") : # asymmetric key
			clear()
			print("\nEnter the asymmetric private key to use for decryption (including the --begin key-- and --end key-- lines)")
			in_priv_key = ""
			while(True) :
				inpt = input()
				if(inpt == "-----BEGIN RSA PRIVATE KEY-----") : 
					continue
				elif(inpt == "-----END RSA PRIVATE KEY-----" or inpt == "") : 
					break
				in_priv_key +=inpt
			print("\nEnter the text to decrypt")
			text = input()
			print("\n######## Begin decrypted text ########\n")
			print(asym_decrypt(text, in_priv_key))
			print("\n######### End decrypted text #########")
			print("\n(press ENTER to continue)")
			input()
		elif (selection == "3") : #sign with asymmetric key and text
			clear()
			print("\nEnter the private key to use to sign the text (including the --begin key-- and --end key-- lines)")
			in_priv_key = ""
			while(True) :
				inpt = input()
				if(inpt == "-----BEGIN RSA PRIVATE KEY-----") : 
					continue
				elif(inpt == "-----END RSA PRIVATE KEY-----" or inpt == "") : 
					break
				in_priv_key +=inpt
			print("\nEnter the text to sign")
			text = input()
			print("\n######## Begin text signature ########\n")
			print(asym_dig_signature(text, in_priv_key))
			print("\n######### End text signature #########")
			print("\n(press ENTER to continue)")
			input()
		elif (selection == "4") : #check with asymmetric key and text
			clear()
			print("\nEnter the signature to verify")
			signature = input()
			print("\nEnter the public key to use to check the signature (including the --begin key-- and --end key-- lines)")
			in_pub_key = ""
			while(True) :
				inpt = input()
				if(inpt == "-----BEGIN PUBLIC KEY-----") :
					continue
				elif(inpt == "-----END PUBLIC KEY-----" or inpt == "") : 
					break
				in_pub_key += inpt
			print("\nEnter the text to check")
			text = input()
			print(asym_dig_signature_verify(signature, text, in_pub_key))
			print("\n(press ENTER to continue)")
			input()
		else :
			return

# start execution here
running = True
while (running):
	clear()
	print ("\nType the number of the option you would like to choose and press ENTER\n")
	print ("0. Quit")
	print ("1. Rotational Encryption")
	print ("2. Map Encryption")
	print ("3. Symmetric Key Encryption")
	print ("4. Asymmetric Key Encryption and Digital Signatures")
	main_selection = input()
	if (main_selection == "0") :
		sys.exit()
	elif (main_selection == "1") :
		rotational_options()
	elif (main_selection == "2") :
		map_options()
	elif (main_selection == "3") :
		symmetric_options()
	elif (main_selection == "4") :
		asymmetric_options()
	else : 
		sys.exit()
