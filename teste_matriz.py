


# Matriz é uma lista de listas

# Entrada do exemplo 
matriz_exemplo = [
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,0,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1]
]

# Saida esperada do exemplo
matriz_exemplo_solucao = [
    [1,0,1,1,1,1],
    [1,0,1,1,1,1],
    [0,0,0,0,0,0],
    [1,0,1,1,1,1],
    [1,0,1,1,1,1]
]

''' Função converte_zero recebe uma matriz(lista de listas) e retorna uma matriz com zero em todas as linhas e colunas que tenham zero na matriz de entrada. 
    A complexidade dessa solução se dá da seguinte forma:
        Tempo:      O(m * n) + O(m * n) + O(m * n) =    O(mn)
        Espaço:     O(m * n) + O(m + n)             =   O(mn)
 '''
def converte_zero(matriz):
    dict_coords = {'x':set(),'y':set()}                                         # complexidade de espaco:   O(m+n)
    for  index_y, value_y in enumerate(matriz):                                 # complexidade de tempo:    O(m)
        for index_x, value_x in enumerate(value_y):                             # complexidade de tempo:    O(n)    
            if(value_x==0): 
                dict_coords['x'].add(index_x)                                   # complexidade de tempo:    O(1)
                dict_coords['y'].add(index_y)                                   # complexidade de tempo:    O(1)    portanto O(mn) no primeiro for()
                                                                                
    res = matriz.copy()                                                         # complexidade de Espaco:   O(mn)
                                                                                # complexidade de tempo:    O(mn)   no copy()

    for  index_y, value_y in enumerate(res):                                    # complexidade de tempo:    O(m)
        for index_x, value_x in enumerate(value_y):                             # complexidade de tempo:    O(n)
            if(index_x in dict_coords['x'] or index_y in dict_coords['y']):     # complexidade de tempo:    O(1)
                res[index_y][index_x] = 0                                       # complexidade de tempo:    O(1)    portanto O(mn) no segundo for()

    return res

# Aqui comeca a main
res = converte_zero(matriz_exemplo)

for i in res:
    print(i)


print("\nIs correct:")
if(res==matriz_exemplo_solucao):
    print("True")
else:
    print("False")
