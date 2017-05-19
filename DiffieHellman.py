
def in_alpha():
	w = input("------Introduzca alpha: ")

	return int(w)

def in_module():
	w = input("------Introduzca el modulo: ")

	return int(w)

def in_xb():
	w = input("------Introduzca xB: ")

	return int(w)
def in_x():
    w = input("------Introduzca x: ")

    return int(w)
def in_xa():
	w = input("------Introduzca xA: ")

	return int(w)
def in_user():
    w = input("------Introduzca el numero de usuarios: ")

    return int(w)

def exponente(y,b,mod):
    x = 1
    while (b > 1):
        if( b%2 == 0):
            #print (str(y)+" | "+str(b)+ " | "+str(x))
            y = (y ** 2)%mod
            b = b/2
            #print("es par")


        if(b%2 == 1):
            #print (str(y)+" | "+str(b)+ " | "+str(x))
            b -= 1
            x = (x * y)%mod
            #print("es impar")

    return x

def calculo_mod(alfa,xa,xb,xc,modulo):

    ya = exponente(alfa,xa,modulo)
    yb = exponente(alfa,xb,modulo)
    yc = exponente(alfa,xc,modulo)

    zac = exponente(yc,xa,modulo)
    zba = exponente(ya, xb, modulo)
    zcb = exponente(yb,xc,modulo)

    k1 = exponente(zcb,xa,modulo);
    k2 = exponente(zac,xb,modulo);
    k3 = exponente(zba,xc,modulo);

    if(k1 == k2 == k3):
        print ("p = "+str(modulo)+", a = "+str(alfa)+", xa = "+str(xa)+", xb = "+str(xb)+", ya = "+str(ya)+", yb = "+str(yb)+", k = "+str(k1))
    else:
        print("No son iguales")

def ordenar(y_vector,user,count):
    print(y_vector);
    aux_vector = y_vector;
    z = 0;
    for i in range(count,user):
        y_vector[i] = aux_vector[z];
        z = z+ 1;
        print(z);
        print(y_vector)

    p = 0;
    for i in range(p,count-1): 
        y_vector[i] = aux_vector[z];
        z += 1;
        print(y_vector)
    print(y_vector)
    return y_vector;




def calculo_mod2(alfa,modulo):
    y_vector = [];
    aux_vector = [];

    x_vector = [];

    #Pillamos los datos para la x
    user = in_user();
    for i in list(range(user)):
        x_vector += [int(in_x())];

    #primera iteracion con alfa
    for i in range(0,user):
       
        y_vector += [exponente(alfa,x_vector[i],modulo)];
    print (y_vector);
    
    #resto de iteraciones desde 1 hasta usuario ç
    count = 1;
    for i in range(1,user):
        aux_vector = y_vector;
        y_vector = [];
        for b in range(0,user):

            if (b+count < user):

                y_vector += [exponente(aux_vector[b+count],x_vector[b],modulo)];
            else:
                y_vector += [exponente(aux_vector[count -1],x_vector[b],modulo)];

        y_vector = ordenar(y_vector,user,count);

        count += count;
        print (y_vector);

    

            





#    for i in range(0,user-1):
#        for i in range(0,user):




#    if(k1 == k2 == k3):
#        print ("p = "+str(modulo)+", a = "+str(alfa)+", xa = "+str(xa)+", xb = "+str(xb)+", ya = "+str(ya)+", yb = "+str(yb)+", k = "+str(k1))
#    else:
#        print("No son iguales")



def calculo(alfa,xa,xb,modulo):

    ya = exponente(alfa,xa,modulo)
    yb = exponente(alfa,xb,modulo)

    k1 = exponente(yb,xa,modulo)
    k2 = exponente(ya, xb, modulo)


    if(k1 == k2):
        print ("p = "+str(modulo)+", a = "+str(alfa)+", xa = "+str(xa)+", xb = "+str(xb)+", ya = "+str(ya)+", yb = "+str(yb)+", k = "+str(k1))
    else:
        print("No son iguales")


#calculo(in_alpha(),in_xa(),in_xb(),in_module());
#calculo_mod2(4,13);
calculo(43,54,71,113);
