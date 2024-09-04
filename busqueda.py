print("en que posicion esta la caja")
cinta = ["vacio", "vacio", "vacio", "caja", "vacio", "vacio", "caja", "vacio", "caja", "vacio", ]
posicion = cinta.index("caja")
print("aqui esta la caja: ", posicion)
posiciones = [i for i, valor in enumerate(cinta) if valor == "caja"]

print("Las cajas están en las posiciones:", posiciones)

posicionesx = []
for i, valor in enumerate(cinta):
    if valor == "caja":
        posicionesx.append(i)
print("Las cajas están en las posiciones:", posicionesx)

cinta1 = ["vacio", "vacio", "vacio", "caja", "vacio", "vacio", "caja", "vacio", "vacio", "vacio", "vacio", "vacio", "vacio", "caja", "vacio", "vacio", "caja", "vacio", "vacio", "vacio"]

# Verificamos si "caja" está en la lista
existe_caja = "caja" in cinta1

print(existe_caja)
