### Error Types ###

# SyntaxError
# print "¡Hola Mundo!" # Descomentar para Error
from math import pi
import math
print("¡Hola Mundo!")

# NameError
language = "Spanish"  # Comentar para Error
print(language)

# IndexError
my_list = ["Python", "Java", "Kotlin", "C#", "JavaScript"]
print(my_list[0])
print(my_list[4])
print(my_list[-1])
# print(my_list[5]) # Descomentar para Error

# ModuleNotFoundError
# import maths # Descomentar para Error

# AttributeError
# print(math.PI) # Descomentar para Error
print(math.pi)

# KeyError
my_dict = {"Nombre": "Alexis", "Apellido": "Reyes", "Edad": 25, 1: "Python"}
print(my_dict["Edad"])
# print(my_dict["Apelido"]) # Descomentar para Error
print(my_dict["Apellido"])

# TypeError
# print(my_list["0"]) # Descomentar para Error
print(my_list[0])
print(my_list[False])

# ImportError
# from math import PI # Descomentar para Error
print(pi)

# ValueError
#my_int = int("10 Años")
my_int = int("10")  # Descomentar para Error
print(type(my_int))

# ZeroDivisionError
# print(4/0) # Descomentar para Error
print(4/2)
