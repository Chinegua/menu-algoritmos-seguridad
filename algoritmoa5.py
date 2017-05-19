import sys

tam_sem = [19, 22, 23]


# tam_sem = [3,5,7]
def binarizar(numero):
    return "%08d" % int(bin(int(numero))[2:])


def des_binarizar(numero):
    int(bin(25)[2:])
    str1 = ''.join(str(e) for e in numero)
    return int(str(str1), 2)



def in_semilla():
    var = [];
    for i in range(0, 3):
        w = input("------Introduzca la semilla: ")
        if tam_sem[i] != len(w):
            print(tam_sem[i])
            print(len(w))
            print("Error en la Semilla")
            sys.exit(0)
        else:
            var += [w]
    return var


def in_data():
    w = input("------Introduzca el valor a cifrar: ")

    return w


def insertado(r1, new):
    r1_copia = []
    for i in range(1, len(r1)):
        r1_copia += [r1[i]]
    r1_copia += [new]
    return r1_copia


def mayoria(a, b, c):
    if a == b:
        return a;
    elif a == c:
        return a;
    elif b == c:
        return b;


def to_vector(mensaje, tam):
    mensaje_v = []
    mensaje = str(mensaje)
    for i in range(0, tam):
        mensaje_v += [int(mensaje[i])]
    return mensaje_v

def a52(r1, r2, r3, cad):
    may_r1_pos = 10
    may_r2_pos = 11
    may_r3_pos = 12
    resultado = []
    resultado_fin = []

    for i in range(0, 10):
        mayor = mayoria(r1[may_r1_pos], r2[may_r2_pos], r3[may_r3_pos])
        resultado += [(r1[0] ^ r2[0] ^ r3[0])]
        if r1[may_r1_pos] == mayor:
            new = r1[0] ^ r1[1] ^ r1[2] ^ r1[5]
            r1 = insertado(r1, new)
        if r2[may_r2_pos] == mayor:
            new = r2[0] ^ r2[1]
            r2 = insertado(r2, new)
        if r3[may_r3_pos] == mayor:
            new = r3[0] ^ r3[1] ^ r3[2] ^ r3[15]
            r3 = insertado(r3, new)


    for i in range(0, len(cad)):
        mayor = mayoria(r1[may_r1_pos], r2[may_r2_pos], r3[may_r3_pos])
        resultado += [(r1[0] ^ r2[0] ^ r3[0])]
        if r1[may_r1_pos] == mayor:
            new = r1[0] ^ r1[1] ^ r1[2] ^ r1[5]
            r1 = insertado(r1, new)
        if r2[may_r2_pos] == mayor:
            new = r2[0] ^ r2[1]
            r2 = insertado(r2, new)
        if r3[may_r3_pos] == mayor:
            new = r3[0] ^ r3[1] ^ r3[2] ^ r3[15]
            r3 = insertado(r3, new)
        resultado_fin += [resultado[i] ^ cad[i]]
    print(resultado_fin)
    print(des_binarizar(resultado_fin))


def a5(r1, r2, r3, cad):
    may_r1_pos = 10
    may_r2_pos = 11
    may_r3_pos = 12
    resultado = []
    resultado_fin = []
    ##NUMERO DE ITERACIONES???????????
    for i in range(0, len(cad)):
        mayor = mayoria(r1[may_r1_pos], r2[may_r2_pos], r3[may_r3_pos])
        resultado += [(r1[0] ^ r2[0] ^ r3[0])]
        if r1[may_r1_pos] == mayor:
            new = r1[0] ^ r1[1] ^ r1[2] ^ r1[5]
            r1 = insertado(r1, new)
        if r2[may_r2_pos] == mayor:
            new = r2[0] ^ r2[1]
            r2 = insertado(r2, new)
        if r3[may_r3_pos] == mayor:
            new = r3[0] ^ r3[1] ^ r3[2] ^ r3[15]
            r3 = insertado(r3, new)
        resultado_fin += [resultado[i] ^ cad[i]]
    print(resultado_fin)
    print(des_binarizar(resultado_fin))


def a5_():
    entrada = in_semilla();
    # print(entrada[1])
    r1 = to_vector(entrada[0], len(entrada[0]))
    r2 = to_vector(entrada[1], len(entrada[1]))
    r3 = to_vector(entrada[2], len(entrada[2]))

    cadena = binarizar(in_data())
    cadena = to_vector(cadena, len(cadena))
    a5(r1, r2, r3, cadena)
    
