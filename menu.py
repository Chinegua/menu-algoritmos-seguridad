import RSA
aux = 0;

while (aux == 0):
	print("SALIR ------ 0");
	print("RSA   ------ 1");

	w = input("------Introduzca la opción: ")
	if(w == 0):
		break;
	
	if(w == 1):
		RSA(421,7,1619);
	