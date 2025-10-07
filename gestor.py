class Película:
    # Indicamos los atributos de la película
    def __init__(self, nombre, descripcion, director, protagonista, valoración, prioridad=True, completada=False):
        
        # Creamos los atributos de la película
        self.id = None
        self.nombre = nombre
        self.descripcion = descripcion
        self.director = director
        self.protagonista = protagonista
        self.valoración = valoración
        self.prioridad = prioridad
        self.completada = completada

#Prueba del código

# 1. Creamos dos películas con sus parámetros
película1 = Película("Cars", "Infatil/Comedia", "John Lasseter", "Rayo Mcqueen", "5 estrellas", "Alta")
película2 = Película("The Notebook", "Romance", "Nick Cassavetes", "Ryan Gosling", "5 estrellas", "Alta")

# 2. Usamos print() con f-strings para mostrar los datos de la primera película
print("--- DATOS DE LA PELÍCULA 1 ---")
print(f"ID: {película1.id}")
print(f"Nombre: {película1.nombre}")
print(f"Descripción: {película1.descripcion}")
print(f"Director {película1.director}")
print(f"Protagonista {película1.protagonista}")
print(f"Valoración: {película1.valoración}")
print(f"Prioridad: {película1.prioridad}")
print(f"Completada: {película1.completada}")

# 3. Hacemos lo mismo para la segunda tarea
print("\n--- DATOS DE LA PELÍCULA 2 ---")
print(f"ID: {película2.id}")
print(f"Nombre: {película2.nombre}")
print(f"Descripción: {película2.descripcion}")
print(f"Director: {película2.director}")
print(f"Protagonista {película2.protagonista}")
print(f"Valoración: {película2.valoración}")
print(f"Prioridad: {película2.prioridad}")
print(f"Completada: {película2.completada}")