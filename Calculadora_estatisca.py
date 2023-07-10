# uma calculadora que seja capaz de calcular várias estatísticas, como média
# mediana, desvio padrão, variância, a partir de um conjunto de dados fornecido pelo usuário.

import os
import math

# Criei essa variavel para que pudesse 'fechar' a calculadora
fazer_calculo = True

while fazer_calculo:
    conta = input('Bem vindo! O que deseja \n'
                  'Digite abaixo o que deseja: media, mediana, dp(desvio padrão), v(variância) ou [s]air: \n').lower()
    
    # Calculando média
    if conta == 'media':
        # Criei uma lista para adicionar os números dado pela pessoa
        lista_media = []
        # Criei uma variavél para poder sair do while
        fazer_media = True

        while fazer_media:
            # Criei uma variavél para saber se vai adicionar mais um número ou vai ver a sua lista ou saber a média
            adicionar_vl_vm = input('Deseja adicionar números a sua lista, ver a sua lista ou ver a média? \n'
                                  'Digite "a" para adicionar "vl" para ver lista ou "vm" para ver média: ').lower()
            
            # Verificamos se o mesmo vai adicionar um número a lista
            if adicionar_vl_vm == 'a':
                # Usei o try/except para poder transformar o número em float
                try:
                    os.system('cls')
                    nums = input('Digite um número para adicionar a sua lista: ')
                    nums_float = float(nums)
                    lista_media.append(nums_float)
                # Se colocasse uma string ao invés de dar um erro ele vai pedir um número    
                except:
                    os.system('cls')
                    print('Digite um número')
            # Verificamos se ele quer ver a lista
            elif adicionar_vl_vm == 'vl':
                os.system('cls')
                print(lista_media)
            # Verificamos se quer ver a média final
            elif adicionar_vl_vm == 'vm':
                # Uma variavél para ser o divisor
                divisor = sum(lista_media)
                # Uma variavél para ser o dividendo
                dividendo = len(lista_media)
                media = divisor/dividendo
                print(f'Sua lista é {lista_media}, \n'
                      f'Ela possui {dividendo} números e a sua média é de {media:.2f}')
                # Entrando na verificação de média mudamos a variavél do while para o mesmo sair e voltar ao menu da calculadora
                fazer_media = False
            else:
                print('Por favor digite uma das opções dada "a" "vl" "vm" ')
    # Calculando mediana
    elif conta == 'mediana':

        lista_mediana = []

        fazer_mediana = True

        while fazer_mediana:
            adicionar_vl_vm = input('Deseja adicionar números a sua lista, ver a sua lista ou ver a mediana? \n'
                                  'Digite "a" para adicionar "vl" para ver lista ou "vm" para ver mediana: ').lower()
            
            if adicionar_vl_vm == 'a':
                try:
                    os.system('cls')
                    nums = input('Digite um número para adicionar a sua lista: ')
                    nums_float = float(nums)
                    lista_mediana.append(nums_float)    
                except:
                    os.system('cls')
                    print('Digite um número')
            elif adicionar_vl_vm == 'vl':
                os.system('cls')
                print(lista_mediana)
            # Para ver a mediana
            elif adicionar_vl_vm == 'vm':
                # Para saber se a lista tem uma quantidade de numero par, temos que pegar os 2 numeros do meio e dividir por 2
                if len(lista_mediana)%2 == 0:
                    # Criei uma variavel para pegar o numero do meio da lista
                    x1 = len(lista_mediana)/2
                    # Criei uma variavel para pegar o segundo numero do meio da lista
                    x2 = x1 - 1
                    x1_int = int(x1)
                    x2_int = int(x2)
                    mediana = (lista_mediana[x1_int] + lista_mediana[x2_int])/2
                    print(f'A sua lista tem {len(lista_mediana)} números e sua mediana é de {mediana}')
                else:
                    x3 = math.floor(len(lista_mediana)/2)
                    x3_int = int(x3)
                    mediana = lista_mediana[x3_int]
                    print(f'A sua lista tem {len(lista_mediana)} números e sua mediana é de {mediana}')
                fazer_mediana = False
            else:
                print('Por favor digite uma das opções dada "a" "vl" "vm" ')
    # Calculando desvio padrão
    elif conta == 'dp':
        # Criei uma lista para desvio padrão
        lista_desvp = []
        # Criei uma variavel para saber se vai continuar rodando o while
        fazer_desvp = True

        while fazer_desvp:
            adicionar_vl_vdp = input('Deseja adicionar números a sua lista, ver a sua lista ou ver o desvio padrão? \n'
                                  'Digite "a" para adicionar "vl" para ver lista ou "vdp" para ver o desvio padrão: ').lower()
            
            if adicionar_vl_vdp == 'a':
                try:
                    os.system('cls')
                    nums = input('Digite um número para adicionar a sua lista: ')
                    nums_float = float(nums)
                    lista_desvp.append(nums_float)    
                except:
                    os.system('cls')
                    print('Digite um número')
            elif adicionar_vl_vdp == 'vl':
                os.system('cls')
                print(lista_desvp)
            elif adicionar_vl_vdp == 'vdp':
                # Fiz uma média da lista do desvio padrão
                media_para_desvp = sum(lista_desvp)/len(lista_desvp) 
                # Calculei a diferença de cada elemento da lista com a média e coloquei ao quadrado e armazenei em uma nova lista
                diff_media = [(media_para_desvp - x)**2 for x in lista_desvp]
                # Usando a biblioteca do math usei para fazer a raiz quadrada da soma da diferencça com o tamanho da lista 
                desv_p = math.sqrt(sum(diff_media)/len(diff_media))
                print(f'O desvio padrão da lista é de {desv_p:.2f}')
                fazer_desvp = False
            else:
                print('Por favor digite uma das opções dada "a" "vl" "vdp" ')
    # Calculando Variancia        
    elif conta == 'v':

        lista_variancia = []

        fazer_variancia = True

        while fazer_variancia:
            adicionar_vl_vv = input('Deseja adicionar números a sua lista, ver a sua lista ou ver a variancia? \n'
                                    'Digite "a" para adicionar "vl" para ver lista ou "vv" para ver a variancia: ').lower()
                
            if adicionar_vl_vv == 'a':
                try:
                    os.system('cls')
                    nums = input('Digite um número para adicionar a sua lista: ')
                    nums_float = float(nums)
                    lista_variancia.append(nums_float)    
                except:
                    os.system('cls')
                    print('Digite um número')
            elif adicionar_vl_vv == 'vl':
                os.system('cls')
                print(lista_variancia)
            elif adicionar_vl_vv == 'vv':
                # Usei o mesmo método do desvio padrão pois a variancia é o desvio padrão ao quadrado
                media_para_desvp = sum(lista_variancia)/len(lista_variancia) 
                diff_media = [(media_para_desvp - x)**2 for x in lista_variancia]
                desv_p = math.sqrt(sum(diff_media)/len(diff_media))
                # Coloquei em uma variavel o desvio padrão ao quadrado
                var = desv_p ** 2
                print(f'A variancia da lista é de {var:.2f}')
                fazer_variancia = False

            else:
                print('Por favor digite uma das opções dada "a" "vl" "vv" ')
    # Saindo da calculadora
    elif conta == 's':
        
        print('Obrigado por usar nossa calculadora')
        # Aqui podemos 'fechar' a calculadora
        fazer_calculo = False

    else:
        print('Por favor insira: media, mediana, dp, v ou s')
        