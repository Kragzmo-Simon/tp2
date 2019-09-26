
from utils import *

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
print("Texte a coder : " + L0R0 + "    Cle : " + K)
L0R0Cypher = iterationDES(L0, R0, K )
print("Resultat d une iteration : " + L0R0Cypher )
decoding = iterationDES(L0R0Cypher[6:], L0R0Cypher[:6], determineK_i(K, 0) )
print("Resultat du decodage de l iteration : " + decoding[6:] + decoding[:6])

"""
Partie B

L0 = '011100'
R0 = '100110'

K = '01100101'

"""

"""
Partie C
"""

"""
Partie D
"""
