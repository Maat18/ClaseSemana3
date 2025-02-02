#Función Estudiante Steven Guayara

def potencia(base, exponente):

    if exponente == 0:
        return 1  # Cualquier número elevado a 0 es 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)  # Exponentes negativos
    else:
        resultado = 1
        for _ in range(exponente):
            resultado *= base
        return resultado

# Ejemplos de uso
print(potencia(2, 3))  # Output: 8
print(potencia(5, 0))  # Output: 1
print(potencia(10, -2)) # Output: 0.01