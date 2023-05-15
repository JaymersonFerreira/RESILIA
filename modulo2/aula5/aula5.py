def insereNaFila(fila, elemento):
    return fila.append(elemento)

def retiraNaFila(fila):
    return fila.pop(0)

fila = []

for i in range(10):
    insereNaFila(fila, i)

# print(fila)
# retiraNaFila(fila)
# print(fila)
# insereNaFila(fila, 15)

insereNaFila(fila, "thiago")
insereNaFila(fila, "luciana")
insereNaFila(fila, "joão")

retiraNaFila(fila)
print(fila)