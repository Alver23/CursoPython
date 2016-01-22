"""def functionTest():
	return "Esta es mi primera funcion"
resultado = functionTest()
print (resultado)
"""

def saludo(nombre):
	return "Hola %s" % nombre

print (saludo("alver"))

ingreso = input("Como te llamas?")
print (saludo(ingreso))