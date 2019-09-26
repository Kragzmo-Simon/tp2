
# Notations :
# Li / Ri : désigne le message de 6 bits Li ou Ri (itération i)
# Li_m1 / Ri_m1 : désigne Li et Ri à l'itération i-1
# Li_p1 / Ri_p1 : désigne Li et Ri à l'itération i+1

# transforme LiRi en Li+1/Ri+1 grâce à une clé K
def iterationDES(Li_m1, Ri_m1, Ki):
    Li = Ri_m1
    Ri = xor(Li_m1,f(Ri_m1, Ki))

    return 0

def f(Li_m1, Ki):
    #Li+_ =

    return 0

def expander(chaine6bits):
    chaine8bits = ''
    chaine8bits += chaine6bits[:2] + 2 * (chaine6bits[3] + chaine6bits[2]) + chaine6bits[4:]
    return chaine8bits

def xor(chaine1, chaine2):
    res_chaine = ''
    for index in range(0,len(chaine1)):
        bit1 = chaine1[index]
        bit2 = chaine2[index]
        if (bit1=='0' and bit2=='0') or (bit1=='1' and bit2=='1'):
            res_bit = '0'
        else:
            res_bit = '1'
        res_chaine += res_bit
    return res_chaine

# key is 9 bits
# iteration is the current iteration number (int)
def determineK_i(key, iteration):
    key_iteration = ''
    for i in range(iteration, min(len(key), iteration + 8 ) ) :
        key_iteration += key[i]
    i = 0
    while len(key_iteration != 8) :
        key_iteration += key[i]
        i += 1
    return key_iteration

determineK_i("010101010",0 )