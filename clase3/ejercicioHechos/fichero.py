import string
import random
fo = open("foo.txt","wb")
fo.write("Es el mejor lenguaje.\nEs genial!!\n")
fo.close();

fo2 = open("foo.txt","r+")
srti = fo2.read()
print srti
fo2.close()