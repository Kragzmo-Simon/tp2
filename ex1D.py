
import math

from utils import *
from random import randint


# Exercice 1
print("Code par FERY Simon et DURAFFOURG Maud")
print('Exercice 1 (Suite)')

"""
Partie D
"""
print("Partie D :")
plaintext = '010111000110'
print("Le texte a code est " + plaintext + ". On le code avec tous les cles possibles pour verifier qu aucune n est "
        "faible.")

number_of_combinations = math.pow(2,9)
progress_percentage_step = 2
progress_step = get_progress_step(number_of_combinations, progress_percentage_step)
compteClefsPasFaibles = 0
for key_index in range(0, int(math.pow(2, 9)) ) :
    key = itobits(key_index, 9)
    for plaintext_index in range(0, int(math.pow(2, 12)) ) :
        plaintext = itobits(plaintext_index, 12)
        iteration_text = Ekprime(plaintext, key)
        iteration_text = Ekprime(iteration_text, key)
        if (iteration_text != plaintext):
            compteClefsPasFaibles +=1
            break
    
    if key_index%progress_step == 0:
        print('Progress~ : ', (key_index//progress_step) * progress_percentage_step, '% finished', key_index)

compteClesFaibles = math.pow(2,9) - compteClefsPasFaibles
print("Le nombre de cle faibles trouvees est de : " , compteClesFaibles)
print("Donc pour Ekprime, toutes les clés sont faibles")



