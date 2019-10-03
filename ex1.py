import math

from utils import *
from random import randint

# Exercice 1
print("Code par FERY Simon et DURAFFOURG Maud")
print('Exercice 1')

"""
Partie A
"""
print('\nPartie A')
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
print('\nPartie B')
plaintext = '010111010110'
key = generate_random_key()

print('Voici la cle de cryptage :                           ', key)
print('Voici le plaintext a crypter :                    ', plaintext)
print('Voici les textes cryptes a chaque iteration')
iteration_text = plaintext
for iteration in range(0,4):
    iteration_text = iterationDES(iteration_text, determineK_i(key, iteration))
    decode_text = decodeDES(iteration_text, key, iteration)
    print('Iteration ', iteration, ' : ', iteration_text, ' / message decode : ', decode_text)
    

"""
Partie C
"""
print("Partie C :")
plaintext = '010111000110'
print("Le texte a code est " + plaintext + ". On le code avec tous les cles possibles pour verifier qu aucune n est "
        "faible.")

comptClesFaibles = 0

for index in range(0, int(math.pow(2, 9)) ) :
    key = itobits(index,9)
    iteration_text = Ek(plaintext, key)
    iteration_text = Ek(iteration_text, key)
    if (iteration_text == plaintext):
        print("Cle faible")
        comptClesFaibles +=1
print("Le nombre de cle faibles trouvees est de : " , comptClesFaibles)

"""
Partie d dans le fichier ex1D.py
"""