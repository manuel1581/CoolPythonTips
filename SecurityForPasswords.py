"""
This file is to show how to secure our passwords.

Content:
  Examples
  References
  
Examples:
  * Using cryptography
  

"""



"""
Example using cryptography
"""

#Load library
from cryptography.fernet import Fernet
#Generate Key
key = Fernet.generate_key()
#Print key (this is only a string shown, but key is binary).
print(key)
#Create object to encrypt or decipher text.
cipher_suite = Fernet(key)
#Encrypt text
ciphered_text = cipher_suite.encrypt(b"STRINGTOENCRYPT")   #required to be bytes
#Print text encrypted, again this is a string viz, this is binary
print(ciphered_text) 

#Saving encrypted text
with open('./WHATEVERNAM.bin', 'wb') as file_object:  
    file_object.write(ciphered_text)
#Saving key
with open('./key_WHATEVERNAME.bin', 'wb') as file_object:  
    file_object.write(key)
    
#Loading text encrypted
with open('./WHATEVERNAM.bin', 'rb') as file_object:  
    for line in file_object:
        encryptedpwd = line
#Loading key
with open('./key_WHATEVERNAME.bin', 'rb') as file_object:  
    for line in file_object:
        key2 = line
#Creatin new object to decrypt
cipher_suite2 = Fernet(key2)
#Text decrypted.
unciphered_text = (cipher_suite2.decrypt(encryptedpwd))


"""
Ref

* http://theautomatic.net/2020/04/28/how-to-hide-a-password-in-a-python-script/
* https://www.mssqltips.com/sqlservertip/5173/encrypting-passwords-for-use-with-python-and-sql-server/
"""
