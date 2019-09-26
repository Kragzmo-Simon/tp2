import math

from utils import *
from random import randint

# Exercice 1

print('Exercice 1')


"""
Partie A
"""
print('Partie A :')
# exemple vu dans le cours
L0 = '011100'
R0 = '100110'

K = '011001010'

L0R0 = L0 + R0
print("Texte a coder : " + L0R0 + "    Cle : " + K)
L0R0Cypher = iterationDES(L0R0, K )
print("Resultat d une iteration : " + L0R0Cypher )
decoding = iterationDES(L0R0Cypher[6:] + L0R0Cypher[:6], determineK_i(K, 0) )
print("Resultat du decodage de l iteration : " + decoding[6:] + decoding[:6])

"""
Partie B
"""
plaintext = '010111010110'
key = generate_random_key()

#for iteration in range(0,4):
#    ciphertext = iterationDES()
print('key : ', key)

"""
Partie C
"""
print("Partie C :")
plaintext = '010111000110'
print("Le texte a code est " + plaintext + ". On le code avec tous les clés possibles pour verifier qu aucune n est "
        "faible")
for index in range(0, int(math.pow(2, 9)) ) :
    key = itobits(index)


"""
Partie D
"""
print("Partie D :")
