from string import ascii_lowercase
import time
key_gen_start = time.time()
start = time.time()
start2 = time.time()
from string import ascii_lowercase
''''
plaintext: hello
secret key: hi
ciphertext: kdmkk

ciphertext: kdmkk
secret key: hi
plaintext: hello
'''
def KSA(key):
	#This initialize the permutation in array S (The state).
	keylength = len(key)
    
	# 256 is the max keylength
	S = [*range(256)] 
	j = 0
    #perform key scheduling
	for i in range(256):
		j = (j + S[i] + key[i % keylength]) % 256
		#  swap values of S[i] and S[j]
		S[i], S[j] = S[j], S[i]  
        # swap the bits for each index until all of the bits of the keylength are swapped
    
	return S

'''
Example:
S[] length = 8
key = [1234]
key length = 4
After key scheduling [12341234]
'''


def PRGA(S):
	#Initialize the PRGA, which takes in values of S
    
	K_arr = []
    #Initialize temp arr
	i = 0
	j = 0
	while True:
		# increments i, and looks up the ith element of S, S[i]
		i = (i + 1) % 256
		# which it then adds to j
		j = (j + S[i]) % 256
		# swaps again
		S[i], S[j] = S[j], S[i]  # swap
		# use the sum S[i] + S[j] mod 256 as an index to find a third element of S
		K = S[(S[i] + S[j]) % 256]
		# similar to return, but used for generator functions 
		yield K
        # obtain the keystream


def RC4(key):
	# Calls the RC4 cipher and puts key into KSA to get variable S for the PRGA algorithm
	S = KSA(key)
    #keylength into PRGA
	return PRGA(S)



def convert_key(s):
	#Converts keys into unicode format.
	return [ord(c) for c in s]
    
key_gen_end = time.time()
    
    
def encrypt():
	#This is the encryption function.
    #Plaintext xor bits Keystream = Ciphertext
    #To encrypt, XOR the value k (keystream) with the next byte of plaintext.
	key = input("Input your encryption key : ")
	plaintext = input("Input your plaintext : ").replace(' ', '').lower()  # to remove input spaces
	while not plaintext.isalpha():
		print('Please only input letters!\n')
		plaintext = input("Input your plaintext : ").replace(' ', '').lower()
        
	plaintxt_arr = []

	for i in range(len(plaintext)):
		plaintxt_arr.append(ascii_lowercase.index(plaintext[i]))
    
	key = convert_key(key)
	keystream = RC4(key)

	for i in range(len(plaintxt_arr)):
		plaintxt_arr[i] = ascii_lowercase[(plaintxt_arr[i] + next(keystream)) % 26]
	print("This is your ciphertext : " + ''.join(plaintxt_arr))
end = time.time()

def decrypt():
	#This is the decryption function.
    #Ciphertext xor bits Keystream = Plaintext
    #To decrypt, XOR the value k (keystream) with the next byte of ciphertext.
	key = input("Input your encryption key : ")
	ciphertext = input("Input your ciphertext : ").replace(' ', '').lower()
        
	ciphertxt_arr = []
	for i in range(len(ciphertext)):
		ciphertxt_arr.append(ascii_lowercase.index(ciphertext[i]))
    
	key = convert_key(key)
	keystream = RC4(key)

	for i in range(len(ciphertxt_arr)):
		ciphertxt_arr[i] = ascii_lowercase[(ciphertxt_arr[i] - next(keystream)) % 26]
	print("This is your plaintext : " + ''.join(ciphertxt_arr))
end2 = time.time()


while True:	
    print("Welcome to my RC4 Algorithm")
    print('1. Encrypt\n2. Decrypt')
    choice = input('Please type in 1 or 2 if you want to encrypt or decrypt : ')
    print('')
    if choice == '1': # encryption
        encrypt()
        #print("This is your ciphertext : " + ''.join(plaint_arr))
        print("encryption time is: ", end - start, "seconds")
        print("key generation time is: ", key_gen_end - key_gen_start, "seconds")
        print('')
        continue
    elif choice == '2': # decryption
        decrypt()
        #print("This is your plaintext : " + ''.join(ciphertext_arr))
        print("decryption time is: ", end2 - start2, "seconds")
        print("key generation time is: ", key_gen_end - key_gen_start, "seconds")
        print('')
        continue
    else:
        print('Please choose either encrypt or decrypt')
        print('')
        continue