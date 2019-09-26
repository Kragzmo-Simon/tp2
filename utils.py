
from random import randint

# Notations :
# Li / Ri : designe le message de 6 bits Li ou Ri (iteration i)
# Li_m1 / Ri_m1 : designe Li et Ri a l'iteration i-1
# Li_p1 / Ri_p1 : designe Li et Ri a l'iteration i+1

S1 = ['101','010','001','110','011','100','111','000',
      '011','100','110','010','000','111','101','011']
S2 = ['100','000','110','101','111','001','011','010',
      '101','011','000','111','110','010','001','100']

def Ekprime(plaintext,key):
    iteration_text = plaintext
    for iteration in range(0,4):
        iteration_text = iterationDES(iteration_text, determineK_i(key, iteration))
        iteration_text = iteration_text[6:] + iteration_text[:6]
    return iteration_text

def Ek(plaintext,key):
    iteration_text = plaintext
    for iteration in range(0,4):
        iteration_text = iterationDES(iteration_text, determineK_i(key, iteration))
    return iteration_text

def decodeDES(ciphertext, key, iteration_number):
    iteration_text = ciphertext
    iteration_text = iteration_text[6:] + iteration_text[:6]
    for iteration in range(iteration_number,-1,-1):
        iteration_text = iterationDES(iteration_text, determineK_i(key, iteration))
    iteration_text = iteration_text[6:] + iteration_text[:6]
    return iteration_text

def iterationDES(Li_m1_Ri_m1, Ki):
    Li_m1 = Li_m1_Ri_m1[:6]
    Ri_m1 = Li_m1_Ri_m1[6:]

    Li = Ri_m1
    Ri = xor(Li_m1,f(Ri_m1, Ki))
    res = Li + Ri
    return res

def f(Ri_m1, Ki):
    chaine8bits = expander(Ri_m1)
    chaine8bits = additionModulo2(chaine8bits,Ki)
    chaine3bits1 = getSBox(chaine8bits[:4], S1)
    chaine3bits2 = getSBox(chaine8bits[4:], S2)
    chaine6bits = chaine3bits1 + chaine3bits2
    return chaine6bits

def getSBox(chaine4bits, Sbox):
    index = getbits_decimalrepr(chaine4bits)
    chaine3bits = Sbox[index]
    return chaine3bits

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

def additionModulo2(chaine1, chaine2):
    res = ''
    for index in range(0, len(chaine1)):
        bit1 = chaine1[index]
        bit2 = chaine2[index]
        if (bit1=='0' and bit2=='0') or (bit1=='1' and bit2=='1'):
            res += '0'
        else:
            res += '1'
    return res


def getbits_decimalrepr(chainebits):
    decimalrepr = 0
    number_of_bits = len(chainebits)
    for index in range(0, number_of_bits):
        decimalrepr += (2**(number_of_bits-index-1)) * int(chainebits[index])
    return decimalrepr

# key is 9 bits
# iteration is the current iteration number (int)
def determineK_i(key, iteration):
    key_iteration = ''
    for index in range(iteration, min(len(key), iteration + 8 ) ) :
        key_iteration += key[index]
    index = 0
    while len(key_iteration) != 8 :
        key_iteration += key[index]
        index += 1
    return key_iteration


def generate_random_key():
    res = ''
    for i in range(0,9):
        res += str(randint(0,1))
    return res

#from https://www.geeksforgeeks.org/generate-binary-number-0-n/
# return x in a 9 bits long string
def itobits(x):
    negative = False
    base = 2
    s = ""
    if (x == 0):
        s = "0"
    negative = (x < 0)
    if (negative):
        x = -1 * x
    while (x != 0):
        # add char to
        # front of s
        s = str(x % base) + s

        # integer division
        # gives quotient
        x = int(x / base)

    while (len(s) != 9):
        s = "0" + s

    return s
