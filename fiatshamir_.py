from math import *
def in_p():
    w = input("------Introduzca p: ")

    return w

def in_q():
    w = input("------Introduzca q: ")

    return w

def in_s():
    w = input("------Introduzca s: ")

    return w


def in_it():
    w = input("------Introduzca el numero de it: ")

    return w

def in_x():
    w = input("------Introduzca x: ")

    return w
def in_e():
    w = input("------Introduzca e(0|1): ")

    return w


def get_n(p,q):
	return int(p)*int(q);

def fiat_shamir(p,q,s,it):

	n = int(p)*int(q);

	it_e = [];

	it_val = [];

	x = in_x();
	it_val += [x];
	for i in range(0,int(it)):
		e = in_e();
		it_e += [e];

	for i in range(0,int(it)):
		a = (int((it_val[i]))**2)%n;
		it_val += [a];
		v = (s ** 2)%n;
		print("N: "+str(n));
		print("V: "+str(v));
		print("X: "+str(it_val[i]));

		if(int(it_e[i]) == 0):

			y = int(it_val[i]) % n;
	
			print("COMPROBAMOS: "+str((y**2)%n)+"="+str(a));
		else:
			y = (int(it_val[i]) * int(s))%n;
			print("COMPROBAMOS: "+str((y**2)%n)+"="+str((a * v)%n)); 


			


#Entrada:
#a. p=7, q=5
#b. s=3
#c. i=2 (número de iteraciones)
#d. 1ª iteración: x=16, e=0
#e. 2ª iteración: x=2, e=1