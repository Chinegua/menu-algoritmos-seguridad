import random
from random import randint
from decimal import *
abecedario = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
tam = 26;
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
def in_p():
	w = input("------Introduzca p: ")

def encontrar_indice(a):
	for i in range (0,tam):
		if abecedario[i] == a:
			return i;

	return int(w)
def in_cadena():
	w = input("------Introduzca cadena: ")

	return w
def in_q():
	w = input("------Introduzca q: ")

	return int(w)
def mcd (m, n):
	if m % n == 0:
		return n;
	else:
		return mcd(n, m%n);
        #SON COPRIMOS SI EL MCD es 1
def primo(n):
	a=0
	for i in range(1,n+1):
		if(n % i==0):
			a=a+1;
	if a!=2:
		return 0;
	else:
		return 1; #pasa

def lehman(n,l):
	comp = 0;
	b = [];
	for it in range(1,l):
		#print(n-1)
		a = random.randint(1, (n-1));
		#print(a);
		c = exponente(a,(n-1)/2,n);
		if (c != 1) and (c != n-1):
			return 1;
		else:
			b.insert(it, c);
	#print (b);
	#print(len(b));
	for it in range(1,len(b)):
		#print(it);
		if(b[int(it)] != 1):
			#print("Hay alguno que no es igual a 1")
			comp = 1;

	if comp == 1:
		return 0;
	else:
		return 1;
def ecluides(a,b):
	while b!=0:
		t = b;
		b = a % b;
		a = t;
	return a;
def calcular_j(base,n):
	count = 0;
	while (base ** count) < n:
		count = count +1 
	return count -1;
def calcular_bloques(vector_cadena,j, base):
	count = 0;
	vector_res = [];

	i = 0;	
	#print(len(vector_cadena));
	while (i < len(vector_cadena)-1):
		resultado = 0;
		aux = j-1
		#print("BLOQUE------------------------")
		while (aux >= 0):
			#print(str(vector_cadena[i])+" * ("+str(base)+" ** "+str(aux));
			resultado += vector_cadena[i] * (base ** aux);
			#print (resultado);
			aux -= 1;
			i += 1;
		#print(resultado);
		vector_res += [resultado];
	return vector_res;

def cifrar(vector,e,n):
	c = [];
	for i in range (0,len(vector)):
		#print("e"+e);
		c += [(vector[i]**e)%n]
	return c;

def inver(a,n):
	t = 0;
	newt = 1;
	r = n;
	newr = a;
	while newr != 0:

		quotient = int(r / newr);


		t, newt = newt, t - quotient * newt
		
		r, newr = newr, r - quotient * newr
		
		
		
	if r > 1:
		return "a is not invertible";
	if t < 0:
		t = t+n;
	return t;


def RSA(p,q,d):
	if(lehman(p,35) != 0):
		print("p");
		return -1;
	if(lehman(q,35) != 0):
		print("q");
		return -1;
	On = (p-1)*(q-1);
	n = p*q
	if(ecluides(d,On) != 1):
		print("ecluides");
		return -1;
	cadena = in_cadena();
	vector_cadena = [];
	for i in range (0,len(cadena)):
		if(cadena[i] != " "):
			vector_cadena += [encontrar_indice(cadena[i].lower())];
	vector_bloques = calcular_bloques(vector_cadena,calcular_j(tam,n),tam);
	e = inver(d,On);
	#print(e);
	vector_cifrado = []
	vector_cifrado = cifrar(vector_bloques,e,n);

	print(vector_cifrado);


	


#RSA(421,7,1619);
#print(mcd(4,5));



#print(inver(1619,2520))
#calcular_j(26,2947);
#print(calcular_bloques([12,0,12,0,12,0],2,26));

