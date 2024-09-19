from cryptography.hazmat.primitives.asymmetric import rsa , dsa
from cryptography.hazmat.primitives import serialization , hashes 
from cryptography.hazmat.primitives.asymmetric.padding import PKCS1v15
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend


plainText = b"hello i am the secret key for the secret accounts "
# def rsa_private_key ():
#     PrivateKey = rsa.generate_private_key(
#         public_exponent = 65537,
#         key_size = 2048,
#          backend = default_backend()
#     )
#     public_key = PrivateKey.public_key()
    
#     return PrivateKey, public_key  
   
# print( rsa_private_key ())


# PrivateKey, publicKey = rsa_private_key()

# def RsaEncryptor(publicKey , plainText):
#     cipher_text = publicKey.encrypt(
#         plainText, 
#         padding.PKCS1v15()
#     )
        
#     return cipher_text
# cipher_text = RsaEncryptor (publicKey , plainText)
# print(cipher_text)

# # DSA KEY
# def new_dsa_key() :
#     dsa_public_key = dsa.generate_private_key(
#         key_size = 1024,
#         backend = default_backend()
#     )
#     dsa_private_key = dsa_public_key.public_key()
    
#     return dsa_public_key ,dsa_private_key
# print(new_dsa_key())

# dsa_private_key, dsa_public_key = new_dsa_key()

# def verify_dsa_key(dsa_public_key, dsa_private_key):
#     signature = dsa_private_key.sign(
#         plainText,
#         hashes.SHA256()
#     )
#     try:
#         dsa_public_key.verify(
#             signature,
#             plainText,
#             hashes.SHA256()
#         )
#         print("Verified signature")
#     except :
#         print("Failed to verify signature:")

#     return signature

# print(new_dsa_key())
# signature = verify_dsa_key(dsa_public_key, dsa_private_key)


     



# find the keys of private keys

rsa_private_key = rsa.generate_private_key(
    public_exponent = 65537,
    key_size = 2048,
)

# find the key of public key 

rsa_public_key = rsa_private_key.public_key()

# create a cipher text to encrypt the data

cipher_text = rsa_public_key.encrypt(
    plainText ,
    padding.PKCS1v15()
)

print(cipher_text)

# them decript the cipher text into plain text 
cipher_plainText = rsa_private_key.decrypt(
    cipher_text ,
    padding.PKCS1v15()
)
print(cipher_plainText)


# dsa generator private key and public key : 
dsa_public_key = dsa.generate_private_key(
    key_size= 1024
)
print(dsa_public_key , "dsa private key")

dsa_private_key = dsa_public_key.public_key()

signature = dsa_public_key.sign(
    plainText , 
    hashes.SHA256()
)
print ("signature: ", signature)
try:
    dsa_private_key.verify(
        signature,
        plainText , 
    hashes.SHA256()
    )
    print("verification is successful")
except:
    print("verification is not successful")
        
    
