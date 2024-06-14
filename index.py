lista = []

def agregar_elemento(elemento):
    lista.append(elemento)

def borrar_elemento(elemento):
    lista.remove(elemento)

def mostrar_lista():
    return lista

for i in range(5):
    agregar_elemento(i)

print(mostrar_lista())
borrar_elemento(3)
print(mostrar_lista())

