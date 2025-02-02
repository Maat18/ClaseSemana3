# Serie sumatoria de n

def sumatoria(n):
    suma = 0
    l=[]
    for i in range(1,n+1):
        suma += i
        l.append(suma)
    return l


#s Serie fibonacci 
def fibonacci(n):
    a = 1
    b = 1
    l=[]
    if(n==1):
        l.append(a)
    elif(n==2):
        l.append(b)
    else:
        a,b=b,a+b
        l.append(b)
    return l
    

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