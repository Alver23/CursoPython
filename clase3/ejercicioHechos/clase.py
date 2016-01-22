class Persona():
	def saludo_general(self):
		return "Hola Persona"

class Estudiante(persona):
	def __init__(self, nombre, edad):
		# super()
		self.nombre = nombre
		self.edad = edad
		def hola(self):
			return "Hola %s" %s self.nombre