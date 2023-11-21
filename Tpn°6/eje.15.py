"""Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas moder-
nas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
uno en las naturales) y tipo (natural o arquitectónica); 
b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
la distancia que las separa;
c. hallar el árbol de expansión mínimo de cada tipo dinsert_ariste las maravillas;
d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
e. determinar si algún país tiene más de una maravilla del mismo tipo;
f. deberá utilizar un grafo no dirigido.
"""
from grafo1 import Grafo 

mi_grafo = Grafo(dirigido=False)
class maravilla:
    
    def __init__(self, nombre, pais, tipo):
        self.nombre = nombre
        self.pais = pais
        self.tipo = tipo
    
    def __str__(self):
        return f'{self.nombre}-{self.pais}-{self.tipo}'

#Arquitectonicas 
mi_grafo.insert_vertice(maravilla("Gran Muralla China",'China','Arquitectónica'),criterio='nombre')
mi_grafo.insert_vertice(maravilla("Machu Picchu","Perú","Arquitectónica"),criterio='nombre')
mi_grafo.insert_vertice(maravilla("Cristo Redentor", 'Brasil', 'Arquitectónica'), criterio='nombre')
mi_grafo.insert_vertice(maravilla("Coliseo Romano", 'Italia', 'Arquitectónica'),criterio='nombre')
mi_grafo.insert_vertice(maravilla("Chichén Itzá", 'México', 'Arquitectónica'), criterio='nombre')
mi_grafo.insert_vertice(maravilla("Petra", 'Jordania', 'Arquitectónica'), criterio='nombre')
mi_grafo.insert_vertice(maravilla("Estatua de la Libertad", 'Estados Unidos', 'Arquitectónica'), criterio='nombre')
mi_grafo.insert_vertice(maravilla("La Torre de Pizza", 'Italia', 'Arquitectónica'),criterio='nombre')
#Naturales
mi_grafo.insert_vertice(maravilla("Parque Nacional de Yellowstone", 'Estados Unidos', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(maravilla("Arrecifes de Veracruz", 'México', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(maravilla("Gran Barrera de Coral", 'Australia', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(maravilla("Monte Everest", 'Nepal', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(maravilla("Cataratas del Iguazú", 'Brasil', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(maravilla("Parque Nacional de Banff", 'Canadá', 'Natural'), criterio='nombre')
mi_grafo.insert_vertice(maravilla("Monte Kilimanjaro ","Tanzania","Natural"), criterio='nombre')
mi_grafo.insert_vertice(maravilla("Yanbaru ","Japon","Natural"), criterio='nombre')    
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;

#Arquitectonicas 
mi_grafo.insert_arist("Gran Muralla China", "Machu Picchu", 150, criterio_vertice='nombre')
mi_grafo.insert_arist("Gran Muralla China", "Cristo Redentor", 200, criterio_vertice='nombre')
mi_grafo.insert_arist("Gran Muralla China", "Coliseo Romano", 180, criterio_vertice='nombre')
mi_grafo.insert_arist("Gran Muralla China", "Chichén Itzá", 160, criterio_vertice='nombre')
mi_grafo.insert_arist("Gran Muralla China", "Petra", 220, criterio_vertice='nombre')
mi_grafo.insert_arist("Gran Muralla China", "Estatua de la Libertad", 250, criterio_vertice='nombre')
mi_grafo.insert_arist("Gran Muralla China", "La Torre de Pizza", 230, criterio_vertice='nombre')

mi_grafo.insert_arist("Machu Picchu", "Cristo Redentor", 190, criterio_vertice='nombre')
mi_grafo.insert_arist("Machu Picchu", "Coliseo Romano", 170, criterio_vertice='nombre')
mi_grafo.insert_arist("Machu Picchu", "Chichén Itzá", 180, criterio_vertice='nombre')
mi_grafo.insert_arist("Machu Picchu", "Petra", 200, criterio_vertice='nombre')
mi_grafo.insert_arist("Machu Picchu", "Estatua de la Libertad", 230, criterio_vertice='nombre')
mi_grafo.insert_arist("Machu Picchu", "La Torre de Pizza", 210, criterio_vertice='nombre')

mi_grafo.insert_arist("Cristo Redentor", "Coliseo Romano", 160, criterio_vertice='nombre')
mi_grafo.insert_arist("Cristo Redentor", "Chichén Itzá", 170, criterio_vertice='nombre')
mi_grafo.insert_arist("Cristo Redentor", "Petra", 190, criterio_vertice='nombre')
mi_grafo.insert_arist("Cristo Redentor", "Estatua de la Libertad", 220, criterio_vertice='nombre')
mi_grafo.insert_arist("Cristo Redentor", "La Torre de Pizza", 200, criterio_vertice='nombre')

mi_grafo.insert_arist("Coliseo Romano", "Chichén Itzá", 150, criterio_vertice='nombre')
mi_grafo.insert_arist("Coliseo Romano", "Petra", 170, criterio_vertice='nombre')
mi_grafo.insert_arist("Coliseo Romano", "Estatua de la Libertad", 200, criterio_vertice='nombre')
mi_grafo.insert_arist("Coliseo Romano", "La Torre de Pizza", 180, criterio_vertice='nombre')

mi_grafo.insert_arist("Chichén Itzá", "Petra", 160, criterio_vertice='nombre')
mi_grafo.insert_arist("Chichén Itzá", "Estatua de la Libertad", 190, criterio_vertice='nombre')
mi_grafo.insert_arist("Chichén Itzá", "La Torre de Pizza", 170, criterio_vertice='nombre')

mi_grafo.insert_arist("Petra", "Estatua de la Libertad", 220, criterio_vertice='nombre')
mi_grafo.insert_arist("Petra", "La Torre de Pizza", 200, criterio_vertice='nombre')

mi_grafo.insert_arist("Estatua de la Libertad", "La Torre de Pizza", 180, criterio_vertice='nombre')
#Naturales
mi_grafo.insert_arist("Parque Nacional de Yellowstone", "Arrecifes de Veracruz", 120, criterio_vertice='nombre')
mi_grafo.insert_arist("Parque Nacional de Yellowstone", "Gran Barrera de Coral", 140, criterio_vertice='nombre')
mi_grafo.insert_arist("Parque Nacional de Yellowstone", "Monte Everest", 160, criterio_vertice='nombre')
mi_grafo.insert_arist("Parque Nacional de Yellowstone", "Cataratas del Iguazú", 180, criterio_vertice='nombre')
mi_grafo.insert_arist("Parque Nacional de Yellowstone", "Parque Nacional de Banff", 200, criterio_vertice='nombre')
mi_grafo.insert_arist("Parque Nacional de Yellowstone", "Monte Kilimanjaro ", 220, criterio_vertice='nombre')
mi_grafo.insert_arist("Parque Nacional de Yellowstone", "Yanbaru ", 240, criterio_vertice='nombre')

mi_grafo.insert_arist("Arrecifes de Veracruz", "Gran Barrera de Coral", 260, criterio_vertice='nombre')
mi_grafo.insert_arist("Arrecifes de Veracruz", "Monte Everest", 280, criterio_vertice='nombre')
mi_grafo.insert_arist("Arrecifes de Veracruz", "Cataratas del Iguazú", 300, criterio_vertice='nombre')
mi_grafo.insert_arist("Arrecifes de Veracruz", "Parque Nacional de Banff", 320, criterio_vertice='nombre')
mi_grafo.insert_arist("Arrecifes de Veracruz", "Monte Kilimanjaro ", 340, criterio_vertice='nombre')
mi_grafo.insert_arist("Arrecifes de Veracruz", "Yanbaru ", 360, criterio_vertice='nombre')

mi_grafo.insert_arist("Gran Barrera de Coral", "Monte Everest", 380, criterio_vertice='nombre')
mi_grafo.insert_arist("Gran Barrera de Coral", "Cataratas del Iguazú", 400, criterio_vertice='nombre')
mi_grafo.insert_arist("Gran Barrera de Coral", "Parque Nacional de Banff", 420, criterio_vertice='nombre')
mi_grafo.insert_arist("Gran Barrera de Coral", "Monte Kilimanjaro ", 440, criterio_vertice='nombre')
mi_grafo.insert_arist("Gran Barrera de Coral", "Yanbaru ", 460, criterio_vertice='nombre')

mi_grafo.insert_arist("Monte Everest", "Cataratas del Iguazú", 480, criterio_vertice='nombre')
mi_grafo.insert_arist("Monte Everest", "Parque Nacional de Banff", 500, criterio_vertice='nombre')
mi_grafo.insert_arist("Monte Everest", "Monte Kilimanjaro ", 520, criterio_vertice='nombre')
mi_grafo.insert_arist("Monte Everest", "Yanbaru ", 540, criterio_vertice='nombre')

mi_grafo.insert_arist("Cataratas del Iguazú", "Parque Nacional de Banff", 560, criterio_vertice='nombre')
mi_grafo.insert_arist("Cataratas del Iguazú", "Monte Kilimanjaro ", 580, criterio_vertice='nombre')
mi_grafo.insert_arist("Cataratas del Iguazú", "Yanbaru ", 600, criterio_vertice='nombre')

mi_grafo.insert_arist("Parque Nacional de Banff", "Monte Kilimanjaro ", 620, criterio_vertice='nombre')
mi_grafo.insert_arist("Parque Nacional de Banff", "Yanbaru ", 640, criterio_vertice='nombre')

mi_grafo.insert_arist("Monte Kilimanjaro ", "Yanbaru ", 660, criterio_vertice='nombre')


# mi_grafo.insert_arist("Gran Barrera de Coral", "Parque Nacional de Yellowstone", 180, criterio_vertice='nombre')
# mi_grafo.insert_arist("Gran Barrera de Coral", "Monte Everest", 200, criterio_vertice='nombre')
# mi_grafo.insert_arist("Gran Barrera de Coral", "Cataratas del Iguazú", 250, criterio_vertice='nombre')
# mi_grafo.insert_arist("Gran Barrera de Coral", "Parque Nacional de Banff", 280, criterio_vertice='nombre')
# mi_grafo.insert_arist("Monte Everest", "Cataratas del Iguazú", 190, criterio_vertice='nombre')
# mi_grafo.insert_arist("Monte Everest", "Parque Nacional de Banff", 220, criterio_vertice='nombre')
# mi_grafo.insert_arist("Cataratas del Iguazú", "Parque Nacional de Banff", 260, criterio_vertice='nombre')
# mi_grafo.insert_arist("Monte Kilimanjaro", "Gran Barrera de Coral", 150, criterio_vertice='nombre')
# mi_grafo.insert_arist("Monte Kilimanjaro", "Monte Everest", 180, criterio_vertice='nombre')
# mi_grafo.insert_arist("Monte Kilimanjaro", "Cataratas del Iguazú", 210, criterio_vertice='nombre')
# mi_grafo.insert_arist("Monte Kilimanjaro", "Parque Nacional de Banff", 240, criterio_vertice='nombre')
# mi_grafo.insert_arist("Arrecifes de Veracruz", "Monte Kilimanjaro", 500, criterio_vertice='nombre')
# mi_grafo.insert_arist("Arrecifes de Veracruz", "Cataratas del Iguazú", 200, criterio_vertice='nombre')
mi_grafo.barrido()
# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
bosque_arq=mi_grafo.kruskal_tipo('Arquitectónica')
bosque_natu=mi_grafo.kruskal_tipo('Natural')

print()
print('bosque arquitectonico')
for arbol in bosque_arq:
    print("arbol")
    for nodo in arbol.split(';'):
        print(nodo)

print()
print('bosque natural')
for arbol in bosque_natu:
    print("arbol")
    for nodo in arbol.split(';'):
        print(nodo)    
    
# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
print()
print('Maravillas Arquitectonicas y Naturales')
mi_grafo.barrido_pais()

# e. determinar si algún país tiene más de una maravilla del mismo tipo;
print()
print('Pais con mas de una maravilla del mismo tipo')
mi_grafo.barrido_pais_tipo()

# f. deberá utilizar un grafo no dirigido.

