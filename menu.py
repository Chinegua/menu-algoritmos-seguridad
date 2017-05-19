import RSA_
import fiatshamir_
import DiffieHellman
import algoritmoa5
import RC4_
import vigenere_
import vernam_

aux = 0;

print("SALIR         ------ 0");
print("RSA           ------ 1");
print("FIAT-SHAMIR   ------ 2");
print("DiffieHellman ------ 3");
print("A5            ------ 4");
print("RC4           ------ 5");
print("VIGENERE      ------ 6");
w = input("------Introduzca la opción: ")
if(int(w) == 1):
	RSA_.RSA(421,7,1619);
if(int(w) == 2):
	fiatshamir_.fiat_shamir(977,983,43215,3);
if(int(w) == 3):
	calculo(43,54,71,113);
if(int(w) == 4):
	algoritmoa5.a5_();
if(int(w) == 5):
	RC4_.generate();
if(int(w) == 6):
	vigenere_.vg();
if(int(w) == 7):
	vernam.ver();