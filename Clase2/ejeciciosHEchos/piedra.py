#!/usr/bin/env python
# -*-coding:utf-8-*-

import time
from time import sleep
import random

sus = "-" * 35

depo = ["piedra","papel","tijeras","lagarto","spock"]
cantInput = raw_input("Cuantas veces quires jugar?")



def numero(ingreso):
	while True:
		try:
			return int(ingreso)
			break
		except Exception, e:
			return 0
			break

valor = numero(cantInput)

if valor == 0:
	print "ATENCIÓN: Debe ingresar un número entero."
else:
	contador = 0;
	while contador < valor:
		x = raw_input("Que elijes? piedra, papel, tijeras, lagarto o spock : ")
		if x not in depo:
			print("no hagas trampa, elejistes {}, y esa opcion no existe").format(x)
			contador = contador + 1
			continue
		pc = random.choice(depo)
		sleep(0.5)
		print (("computadora elijio {}.").format(pc))
		if x == pc :
			print "\nEmpate."
		elif x == "piedra" and pc == "tijeras":
			print "\ Ganaste, {} aplasta {}".format(x,pc)
		elif x == "papel" and pc == "piedra":
			print "\n Ganaste, {} tapa a {}".format(x,pc)
		elif x == "tijeras" and pc == "papel":
			print "\n Ganaste, {} corta {}".format(x,pc)
		elif x == "piedra" and pc == "lagarto":
			print "\n Ganaste, {} aplasta a {}".format(x,pc)
		elif x == "lagarto" and pc == "spock":
			print "\n Ganaste, {} envenena a {}".format(x,pc)
		elif x == "spock" and pc == "tijeras":
			print "\n Ganaste, {} rompe a {}".format(x,pc)
		elif x == "tijeras" and pc == "lagarto":
			print "\n Ganaste, {} decapitan a {}".format(x,pc)
		elif x == "lagarto" and pc == "papel":
			print "\n Ganaste, {} devora {}".format(x,pc)
		elif x == "papel" and pc == "spock":
			print "\n Ganaste, {} desautoriza {}".format(x,pc)
		elif x == "spock" and pc == "piedra":
			print "\n Ganaste, {} vaporiza {}".format(x,pc)
		else:
			print "Perdimos. {} gana {}".format(pc,x)
		print sus
		contador = contador + 1
		print contador , cantInput

