
import math

from utils import *
from random import randint

# Exercice 2
print("Code par FERY Simon et DURAFFOURG Maud")
print('Exercice 2')

"""
Partie A
"""

print('\nPartie A :')

plaintext = ["011001111001",
             "101001011010",
             "010111010101",
             "100001000101"]
C0 = ''
for i in range(0,12):
    C0 += str(randint(0,1))
key = generate_random_key()

print("Le message a code est : " + " ".join(plaintext) )
print("On utilise CO = " + C0 + " et la cle aleatoire est : " + key)

# crypting
cypher = CBC_crypting(plaintext, C0, key)
print("Le cypher est : " + " ".join(cypher))

# decrypting
decode = CBC_decrypting(cypher, C0, key)
print("Le message decode est : " + " ".join(decode))


"""
Partie B
"""
print('\nPartie B :')

plaintext_1 = ["011000111111",
             "101001011010",
             "010010111101",
             "111010011101"]

# on change le 14 eme bit
plaintext_2 = ["011000111111",
             "111001011010",
             "010010111101",
             "111010011101"]

#On reprend les cles et C0 precedent

print("Le message 1 a code est : " + " ".join(plaintext_1) )
print("Le message 2 a code est : " + " ".join(plaintext_2) )
print("On utilise CO = " + C0 + " et la cle aleatoire est : " + key)

# crypting
cypher_1 = CBC_crypting(plaintext_1, C0, key)
cypher_2 = CBC_crypting(plaintext_2, C0, key)
print("Le cypher 1 est : " + " ".join(cypher_1))
print("Le cypher 2 est : " + " ".join(cypher_2))
print("On constate qu a partir du deuxieme paquet de donnees, le cypher 2 est tres different du cypher 1 avec "
      "un bit de difference.")


