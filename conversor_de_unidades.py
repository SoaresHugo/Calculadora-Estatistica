# Desenvolvi um programa que converte diferentes unidades de medida.
# O usuário poderá selecionar as unidades de origem e destino, e o programa realizará a conversão.

import math 
import os


# Funções para converter tempo

def hora_minuto (h):
    min = h*60
    return min

def hora_segundo (h):
    sec = h*math.pow(60,2)
    return sec

def minuto_segundo (min):
    sec = min*60
    return sec

def segundo_minuto (sec):
    min = sec/60
    return min

def segundo_hora (sec):
    h = sec/math.pow(60,2)
    return h

# Funções para converter velocidade

def kmh_ms(kmh):
    ms = kmh /3.6
    return ms

def ms_kmh(ms):
    kmh = ms * 3.6
    return kmh

# Funções para converter comprimento 

def metros_cm (m):
    cm = m*math.pow(10,2)
    return cm 

def cm_metros (cm):
    m = cm/math.pow(10,2)
    return m 

def m_km (m):
    km = m/math.pow(10,3)
    return km

def km_m (km):
    m = km*math.pow(10,3)
    return m

# Funções para converter massa

def kg_g (kg):
    g = kg*math.pow(10,3)
    return g

def g_kg (g):
    kg = g/math.pow(10,3)
    return kg

def g_mg (g):
    mg = g*math.pow(10,3)
    return mg

def mg_g (mg):
    g = mg/math.pow(10,3)
    return g

# Funções para converter temperatura

def c_f (c):
    f = 1.8*c + 32
    return f

def c_k (c):
    k = c + 273 
    return k

def f_c (f): 
    c = (f - 32)/1.8
    return c

def f_k (f):
    k = (5*(f-32)/9) + 273
    return k

def k_c (k):
    c = k - 273
    return c 

def k_f (k):
    f = ((k-273)*1.8) + 32
    return f

# Criei uma variavél para poder sair do laço

fazer_conversao = True

while fazer_conversao:

    # Aqui será onde o usuário irá decidir qual tipo de conversão o mesmo vai querer ou sair

    print('Bem vindo para o conversor de medidas! Você pode escolher converter tempo, velocidade \n'
          'comprimento, massa, temperatura e sair' )
    tipo_conversao = input('Escolha entre tempo, velocidade, comprimento, massa, temperatura ou sair: ').lower()
    # Convertendo tempo
    if tipo_conversao == 'tempo':
        # Criei uma variavél para poder sair do laço
        converte_tempo = True
        while converte_tempo:
            # Com o mesmo escolhendo tempo, fiz umas abreviações para poder fazer a conversão
            print('Deseja converter de hora para minuto(hpm), hora para segundo(hps), minuto para segundo(mps) \n'
                  'segundo para minuto(spm), segundo para hora(sph) ou digite sair para mudar o tipo de conversão')
            decisao = input('Digite a conversão que deseja: ').lower()


            # Para todas as respostas fiz as mesmas ações (inclusive de outras medidas)

            if decisao == 'hpm':
                # O codigo vai tentar converter o valor em número float e se caso fosse string pediria um erro
                # Caso contrario ele retornaria o valor da conversão das respecitivas funções (Se repete para todas as outras connversões)
                try:
                    h = input('Digite a hora que deseja transformar em minuto: ')
                    h_float = float(h)
                    print(f'A conversão é de {hora_minuto(h_float):.2f} minutos')
                except:
                    print('Digite um número')

            elif decisao == 'hps':
                try:
                    h = input('Digite a hora que deseja transformar em segundo: ')
                    h_float = float(h)
                    print(f'A conversão é de {hora_segundo(h_float):.2f} segundos')
                except:
                    print('Digite um número')

            elif decisao == 'mps':
                try:
                    min = input('Digite o minuto que deseja transformar em segundo: ')
                    min_float = float(min)
                    print(f'A conversão é de {minuto_segundo(min_float):.2f} segundos')
                except:
                    print('Digite um número')

            elif decisao == 'spm':
                try:
                    sec = input('Digite o segundo que deseja transformar em minuto: ')
                    sec_float = float(sec)
                    print(f'A conversão é de {segundo_minuto(sec_float):.2f} minutos')
                except:
                    print('Digite um número')
            
            elif decisao == 'sph':
                try:
                    sec = input('Digite o segundo que deseja transformar em hora: ')
                    sec_float = float(sec)
                    print(f'A conversão é de {segundo_hora(sec_float):.4f} horas')
                except:
                    print('Digite um número')

            # Se a pessoa quiser sair da conversão escolhida, o mesmo vai mudar a variavel converte tempo e vai voltar pro menu principal

            elif decisao == 'sair':
                os.system('cls')
                print('Você está indo para o menu de conversão onde pode escolher entre outras conversões')
                converte_tempo = False

            # Se o usuário escolher uma ação que não foi dada ele printará para escolher uma opção

            else:
                print('Por favor escolha uma das opções dada')
    # Convertendo velocidade
    elif tipo_conversao == 'velocidade':

        # Criei uma variavél para poder sair do laço
        converte_velocidade = True

        while converte_velocidade:
            print('Deseja converter de hm/h para m/s(kpm) ou m/s para km/h(mpk) ou digite sair para mudar o tipo de conversão')
            decisao = input('Digite a conversão que deseja: ').lower()

            if decisao == 'kpm':
                try:
                    kmh = input('Digite o km/h que deseja transformar em m/s: ')
                    kmh_float = float(kmh)
                    print(f'A conversão é de {kmh_ms(kmh_float):.2f} m/s')
                except:
                    print('Digite um número')
                
            elif decisao == 'mpk':
                try:
                    ms = input('Digite o m/s que deseja transformar em km/s: ')
                    ms_float = float(ms)
                    print(f'A conversão é de {ms_kmh(ms_float):.2f} km/h')
                except:
                    print('Digite um número')
            
            elif decisao == 'sair':
                os.system('cls')
                print('Você está indo para o menu de conversão onde pode escolher entre outras conversões')
                converte_velocidade = False
            
            else:
                print('Por favor escolha uma das opções dada')
    # Convertendo comprimento
    elif tipo_conversao == 'comprimento':
        converte_comprimento = True
        while converte_comprimento:
            print('Deseja converter de m para cm(mpc), cm para m(cpm), m para km(mpk), km para m(kpm) \n'
                  'ou digite sair para mudar o tipo de conversão')
            
            decisao = input('Digite a conversão desejada: ').lower()

            if decisao == 'mpc':
                try:
                    m = input('Digite o m que deseja transformar em cm: ')
                    m_float = float(m)
                    print(f'A conversão é de {metros_cm(m_float)} cm')
                except:
                    print('Digite um número')

            elif decisao == 'cpm':
                try:
                    cm = input('Digite o cm que deseja transformar em m: ')
                    cm_float = float(cm)
                    print(f'A conversão é de {cm_metros(cm_float)} m')
                except:
                    print('Digite um número')

            elif decisao == 'mpk':
                try:
                    m = input('Digite o m que deseja transformar em km: ')
                    m_float = float(m)
                    print(f'A conversão é de {m_km(m_float)} km')
                except:
                    print('Digite um número')
            
            elif decisao == 'kpm':
                try:
                    k = input('Digite o km que deseja transformar em m: ')
                    k_float = float(k)
                    print(f'A conversão é de {km_m(k_float)} m')
                except:
                    print('Digite um número')
            
            elif decisao == 'sair':
                os.system('cls')
                print('Você está indo para o menu de conversão onde pode escolher entre outras conversões')
                converte_comprimento = False
                
            
            '''else:
                print('Por favor escolha uma das opções dada')'''
    # Convertendo massa
    elif tipo_conversao == 'massa':
        converte_massa = True
        while converte_massa:
            print('Deseja converter de kg para g(kpg), g para kg(gpk), g para mg(gpm), mg para g(mpg) \n'
                  'ou digite sair para mudar o tipo de conversão')
            decisao = input('Digite a conversão desejada: ').lower()

            if decisao == 'kpg':
                try:
                    kg = input('Digite o kg que deseja converter em g: ')
                    kg_float = float(kg)
                    print(f'A conversão é de {kg_g(kg_float)} g')
                except:
                    print('Digite um número')

            elif decisao == 'gpk':
                try:
                    g = input('Digite o g que deseja converter em kg: ')
                    g_float = float(g)
                    print(f'A conversão é de {g_kg(g_float)} kg')
                except:
                    print('Digite um número')
            
            elif decisao == 'gpm':
                try:
                    g = input('Digite o g que deseja converter em mg: ')
                    g_float = float(g)
                    print(f'A conversão é de {g_mg(g_float)} mg')
                except:
                    print('Digite um número')
            
            elif decisao == 'mpg':
                try:
                    mg = input('Digite o mg que deseja converter em g: ')
                    mg_float = float(mg)
                    print(f'A conversão é de {mg_g(mg_float)} g')
                except:
                    print('Digite um número')

            elif decisao == 'sair':
                os.system('cls')
                print('Você está indo para o menu de conversão onde pode escolher entre outras conversões')
                converte_massa = False
                
            
            else:
                print('Por favor escolha uma das opções dada')
    # Convertendo temperatura            
    elif tipo_conversao == 'temperatura':
        converte_temperatura = True
        while converte_temperatura:
            print('Deseja converter de c° para f°(cpf), c° para k(cpk), f° para c°(fpc), f° para k(fpk) \n'
                  'k para c°(kpc), k para f° ou ou digite sair para mudar o tipo de conversão')  
            decisao = input('Digite a conversão desejada: ').lower()

            if decisao == 'cpf':
                try:
                    c = input('Digite o valor em c° para converter em f°: ')
                    c_float = float(c)
                    print(f'A conversão é de {c_f(c_float)} f°')
                except:
                    print('Digite um número')
            
            elif decisao == 'cpk':
                try:
                    c = input('Digite o valor em c° para converter em k: ')
                    c_float = float(c)
                    print(f'A conversão é de {c_k(c_float)} k')
                except:
                    print('Digite um número')
            
            elif decisao == 'fpc':
                try:
                    f = input('Digite o valor em f° para converter em c°: ')
                    f_float = float(f)
                    print(f'A conversão é de {f_c(f_float)} c°')
                except:
                    print('Digite um número')

            elif decisao == 'fpk':
                try:
                    f = input('Digite o valor em f° para converter em k: ')
                    f_float = float(f)
                    print(f'A conversão é de {f_k(f_float):.2f} k°')
                except:
                    print('Digite um número')

            elif decisao == 'kpc':
                try:
                    k = input('Digite o valor em k para converter em c°: ')
                    k_float = float(k)
                    print(f'A conversão é de {k_c(k_float)} k')
                except:
                    print('Digite um número')

            elif decisao == 'kpf':
                try:
                    k = input('Digite o valor em k para converter em f°: ')
                    k_float = float(k)
                    print(f'A conversão é de {k_f(k_float)} f°')
                except:
                    print('Digite um número')

            elif decisao == 'sair':
                os.system('cls')
                print('Você está indo para o menu de conversão onde pode escolher entre outras conversões')
                converte_temperatura = False
                
            
            else:
                print('Por favor escolha uma das opções dada')
    # Fechando o programa
    elif tipo_conversao == 'sair':
        print('Obrigado por usar nosso conversor, volte sempre!')
        fazer_conversao = False 

    else:
        print('Digite uma das opções dadas')           