#!/usr/bin/env python
# coding: utf-8

# <h1>Código para simular o programa porta dos desesperados</h1>
# 
# 223730 - Rafael Silva Cirino

# In[77]:


import random

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = (11,7)

#guarda a quantidade de vitória
gst = 0

#Guarda a qtd de vitória trocando a porta
gt = 0

b = 0
c = 0

#espaço amostral
a = 10000

#Listas para salvar resultados
lis2 = []
lisst = []
lisx = []
list = []

for x in range(1, a):
 lis = [1, 2, 3]
 #Pc escolhe da porta A=1 a porta C=3
 pc = random.choice(lis)

 #Porta escolhida pelo jogador
 jogador = random.choice(lis)

 if pc == jogador:
    lis.remove(pc)
    c = lis[0]
    lis.pop(0)
    lis2 = [pc, c]
 else:
    lis2 = [pc, jogador]

 #Não trocou de porta
 if jogador == pc :
     gst = gst + 1
 else:
    #troca de porta
     lis2.remove(jogador)
     jogador = lis2[0]
     if jogador == pc:
        gt = gt + 1
 
 #Criando a lista para plotar o gráfico
 b = gst/x
 c = gt/x   
 lisst.append(b)
 list.append(c)
 lisx.append(x)
 

#Plot do gráfico
plt.scatter(lisx, lisst, color='green')
plt.title("Proporção de vitórias sem trocar a porta")
plt.xlabel('Número de simulações')
plt.ylabel('Proporção de vitórias')
plt.show()

plt.scatter(lisx, list)
plt.title("Proporção de vitórias trocando a porta")
plt.xlabel('Número de simulações')
plt.ylabel('Proporção de vitórias')
plt.show()

print("% de Vitórias trocando a porta", gt/a)
print("% de Vitórias sem trocar a porta", gst/a)


# In[ ]:





# In[ ]:





# In[ ]:




