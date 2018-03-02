'''
fibonacci(6) => [1, 1, 2, 3, 5, 8]
fibonacci(7) => [1, 1, 2, 3, 5, 8, 13]
'''

def fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        lista = fibonacci(n-1)
        suma = lista[len(lista)-1] + lista[len(lista)-2]
        lista.append(suma)
        return lista

def main():
    resultado = fibonacci(6)
    print(resultado)

if __name__ == '__main__':
    main()
