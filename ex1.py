
from utils import *
from random import randint

# Exercice 1

print('Exercice 1')


"""
Partie A
"""
# exemple vu dans le cours
L0 = '011100'
R0 = '100110'

K = '011001010'

L0R0 = L0 + R0
print("")
#print(iterationDES(L0, R0, determineK_i(K, 0) ))

# une iteration avec k0 + le dechiffrement avec k0

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

"""
Partie D
"""
