# script.py
# Desarrollado para analizar mediante un profiler

def suma(a,b):
	return a+b

def factorial(x):
	if x == 0:
		return 1
	else:
		return x * factorial(x - 1)
		
i=0

while i<20000:
	x=suma(10,i)
	print "La suma es %d." %(x)
	i+=1

j=0

while j<=20:
	y=factorial(j)
	print "El factorial de %d es %d." %(j, y)
	j+=1
