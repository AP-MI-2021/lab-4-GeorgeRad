# Problema 1
# Functie care citeste o lista de numere intregi
def read_the_list():
    lista = []
    nr_elemente = int(input("Dati numarul de elemente al listei: "))
    print("Elementele vor fi introduse unul sub celalalt, cu ajutorul lui ENTER!")
    for i in range(nr_elemente):
        element_lista = int(input())
        lista.append(element_lista)
    return lista


# Problema 2
def afiseaza_numere_negative(lista):
    """
    Afisarea tuturor numerelor negative din lista data
    :param lista: lista de numere intregi
    :return: o lista "lst", de numere intregi
    """
    lst = []
    for i in lista:
        if i < 0:
            lst.append(i)
    return lst



# Functia de test pentru Problema 2
def test_afiseaza_numere_negative():
    assert afiseaza_numere_negative([-1,-2,3]) == [-1, -2]
    assert afiseaza_numere_negative([-2, -13]) == [-2, -13]
    assert afiseaza_numere_negative([2,3]) == []



# Problema 3
def cel_mai_mic_numar(lista, n):
    """
    Afiseaza cel mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura
    :param lista: lista de numere intregi
    :param n: numar intreg
    :return: cel mai mic numar care are ultima cifra egala cu n
    """
    lista.sort()
    for i in lista:
        if i % 10 == n:
            return i



# Functia de test pentru Problema 3
def test_cel_mai_mic_numar():
    assert cel_mai_mic_numar([1,6,34,68,40,48,20], 8) == 48
    assert cel_mai_mic_numar([2,6,13,24,34], 6) == 6
    assert cel_mai_mic_numar([13,2435,34,47], 3) == 13



# Pentru problema 4
# Verificam daca un numar dat este prim
def is_prime(n):
    """
    Verificam daca un numar dat este prim
    :param n: numar intreg
    :return: True daca este prim sau False daca nu este prim
    """
    if n == 2:
        return True
    if n == 1 or n == 0 or n % 2 == 0:
        return False
    for i  in range(3, n // 2 + 1):
        if n % i == 0:
            return False
    return True

# Functia de test pentru is_prime
def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False


# Pentru problema 4
# Functie care verifica daca un numar este sau nu superprim
def numar_superprim(n):
    """
    Verificam daca n este numar superprim
    :param n: numar intreg
    :return: True daca numarul este superprim sau False daca nu este superprim
    """
    if n < 1:
        return False
    while n > 0:
        if is_prime(n) is False:
            return False
        n = n // 10
    return True


# Functia de test pentru numar_superprim
def test_numar_superprim():
    assert numar_superprim(173) is False
    assert numar_superprim(239) is True
    assert numar_superprim(124) is False


# Problema 4
def lista_superprime(lista):
    """
    Afisam toate numerele care sunt superprime din lista data
    :param lista: lista de numere intregi
    :return: o lista de superprime
    """
    lst = []
    for i in lista:
        if numar_superprim(i) is True:
            lst.append(i)
    return lst




# Functia de test pentru Problema 4
def test_lista_superprime():
    assert lista_superprime([239, 239]) == [239, 239]
    assert lista_superprime([173, 239, 124]) == [239]
    assert lista_superprime([124, 234]) == []

from math import gcd
from functools import reduce

# Pentru problema 5
# CMMDC
def get_cmmdc(lista):
    """
    Calculam cmmdc-ul tuturor numerelor din lista
    :param lista: lista de numere intregi pozitive
    :return: cmmdc
    """
    x = reduce(gcd, lista)
    return x

# Functia de test pentru get_cmmdc
def test_get_cmmdc():
    assert get_cmmdc([12, 24, 144]) == 12
    assert get_cmmdc([13, 17, 23]) == 1
    assert get_cmmdc([15, 30, 45]) == 15

# Pentru problema 5
# Oglindit
def reverse(x):
    ans = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
    return ans if -2**31 <= ans <= 2**31 - 1 else 0


# Functia de test pentru oglindit
def test_reverse():
    assert reverse(-234) == -432
    assert reverse(-123) == -321
    assert reverse(-112) == -211


# Problema 5
def inlocuieste_cu_cmmdc_si_invers(lista):
    """
    Inlocuim numerele pozitive si nenule cu cmmdc-ul lor iar pe cele negative cu inversul lor
    :param lista: lista de numere intregi
    :return: lista
    """
    lista_finala = []
    lst = []
    for i in lista:
        if i > 0:
            lst.append(i)
    for i in lista:
        if i > 0:
            lista_finala.append(get_cmmdc(lst))
        elif i < 0:
            lista_finala.append(reverse(i))
    return lista_finala


# Functia de test pentru Problema 5
def test_inlocuieste_cu_cmmdc_si_invers():
    assert inlocuieste_cu_cmmdc_si_invers([-76,12,24,-13,144]) == [-67, 12, 12, -31, 12]
    assert inlocuieste_cu_cmmdc_si_invers([15, 30, -234]) == [15, 15, -432]
    assert inlocuieste_cu_cmmdc_si_invers([20, 40, -123]) == [20, 20, -321]



# Functie care testeaza toate functiile de test
def test_all():
    test_afiseaza_numere_negative()
    test_cel_mai_mic_numar()
    test_is_prime()
    test_numar_superprim()
    test_lista_superprime()
    test_get_cmmdc()
    test_reverse()
    test_inlocuieste_cu_cmmdc_si_invers()




# Meniu
def menu():
    print("1.Citeste o lista de numere intregi")
    print("2.Afișarea tuturor numerelor negative nenule din listă")
    print("3.Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură")
    print("4.Afișarea tuturor numerelor din listă care sunt superprime.")
    print("5.Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu CMMDC-ul lor și numerele negative au cifrele în ordine inversă.")
    print("6. Iesire")



def main():
    test_all()
    lista = []
    while True:
        menu()
        optiune = input("Introduceti optiunea dumneavoastra: ")
        if optiune == "1":
            lista = read_the_list()
        elif optiune == "2":
            print(afiseaza_numere_negative(lista))
        elif optiune == "3":
            n = int(input("Dati cifra n = "))
            print(cel_mai_mic_numar(lista, n))
        elif optiune == "4":
            print(lista_superprime(lista))
        elif optiune == "5":
            print(inlocuieste_cu_cmmdc_si_invers(lista))
        elif optiune == "6":
            break
        else:
            print("Optiunea introdusa este gresita! Reincercati!")

main()
