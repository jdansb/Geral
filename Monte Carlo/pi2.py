## Raio do Círculo por Monte Carlo #2
## Desenvolvido por:    Jhordan Silveira de Borba
## E-mail:              jhordandecacapava@gmail.com
## Website:             https://github.com/SapoGitHub
##                      https://alkasl.wordpress.com   
## 2019

import random       # Biblioteca com números pseudo aleatórios
import numpy as np  # Biblioteca para trabalhar com funções matemáticas
import matplotlib.pyplot as plt     # Biblioteca pra plotar gráfico


#Listas com as coordenadas dos pontos dentro e fora
x_fora=[]
x_dentro=[]
y_fora=[]
y_dentro=[] 

dentro=0                            # Quantidade de pontos dentro
N=1000000                            # Quantidade de pontos gerados

for i in range(N):
    x = random.random()
    y = random.random()
    d=np.sqrt(x*x+y*y)
    
    if (d<=1):                       # Checamos se caiu dentro do círculo
        dentro= dentro+1            # E anotamos
        x_dentro.append(x)
        y_dentro.append(y)
    else:
        x_fora.append(x)
        y_fora.append(y)

pi = 4*(float(dentro)/float(N))
print(str (pi) + ' - Erro: '+ str(abs(1-pi/np.pi)) + '% do valor correto.')


n=1000                              # Fração que vamos plotar N/n

# Listas das coordenadas dos pontos que vamos plotar
px_den=[]   
py_den=[]
px_for=[]
py_for=[]

for i in range(int(N/n)):
    den = random.randint(0,len(x_dentro))   # Sorteamos um elemento dentro
    # Guardamos o ponto
    px_den.append(x_dentro[den])
    py_den.append(y_dentro[den])
    # Fazemos o mesmo com 
    den = random.randint(0,len(x_fora)) 
    px_for.append(x_fora[den])
    py_for.append(y_fora[den])

# Plotamos os pontos 
plt.plot(py_den, px_den, 'ro' ,label='Dentro')      # Pontos dentro
plt.plot(py_for, px_for, 'bo' ,label='Fora')        # Pontos fora

x=np.linspace(0, 1, 1000)                           # x
plt.plot(np.sqrt(1-x*x),x, 'black')               # Parte positiva da raíz

# Configurações                 
plt.xlabel('x')                 # Legenda eixo X
plt.ylabel('y')                 # Legenda eixo y
plt.title("Monte Carlo")        # Título
plt.show()                      # Mostramos o gráfico
