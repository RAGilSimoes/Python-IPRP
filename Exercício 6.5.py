import random

lista_resultados = []
percentagem_soma_par = 0
soma_par = 0

def lancamentos(lista_resultados, percentagem_soma_par, soma_par):
    lancamentos = random.randint(0,50)
    for i in range(lancamentos):
        dado_1 = random.randint(1,6)
        dado_2 = random.randint(1,6)
        
        lista_resultados = lista_resultados + [dado_1, dado_2]
        
        if ((dado_1 + dado_2) %2 == 0):
            soma_par += 1
            
        percentagem_soma_par = round((soma_par/lancamentos) * 100) 
        
    return lista_resultados, percentagem_soma_par

print(lancamentos(lista_resultados, percentagem_soma_par, soma_par))
