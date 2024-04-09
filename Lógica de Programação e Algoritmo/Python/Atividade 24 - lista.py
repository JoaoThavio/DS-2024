""""
gremio = []
gremio.append("v1")
gremio.append("v2")
gremio.append("v3")
print(gremio)
"""

frutas = []
frutas.append("Maçã")
frutas.append("bergamota")
frutas.append("Banana")
frutas.append("Melão")
frutas.append("Laranja")
print(len(frutas))
frutas.pop(0)
print(frutas)
frutas.pop(-1)
print(frutas)
print(len(frutas[0]))
frutas.clear()
print(frutas)
#print(f"frutas selecionadas: {frutas[0]} e {frutas [2]}")