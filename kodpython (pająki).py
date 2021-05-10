import numpy as np
import matplotlib.pyplot as plt
import random

import scipy.stats as s

P = [[0.0, 1/6, 1/6, 1/6, 1/6, 1/6, 1/6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
     [1/4, 0.0, 1/4, 0.0, 0.0, 0.0, 1/4, 1/4, 0.0, 0.0, 0.0, 0.0, 0.0],
     [1/4, 1/4, 0.0, 1/4, 0.0, 0.0, 0.0, 0.0, 1/4, 0.0, 0.0, 0.0, 0.0],
     [1/4, 0.0, 1/4, 0.0, 1/4, 0.0, 0.0, 0.0, 0.0, 1/4, 0.0, 0.0, 0.0],
     [1/4, 0.0, 0.0, 1/4, 0.0, 1/4, 0.0, 0.0, 0.0, 0.0, 1/4, 0.0, 0.0],
     [1/4, 0.0, 0.0, 0.0, 1/4, 0.0, 1/4, 0.0, 0.0, 0.0, 0.0, 1/4, 0.0],
     [1/4, 1/4, 0.0, 0.0, 0.0, 1/4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1/4],
     [0.0, 1/3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1/3, 0.0, 0.0, 0.0, 1/3],
     [0.0, 0.0, 1/3, 0.0, 0.0, 0.0, 0.0, 1/3, 0.0, 1/3, 0.0, 0.0, 0.0],
     [0.0, 0.0, 0.0, 1/3, 0.0, 0.0, 0.0, 0.0, 1/3, 0.0, 1/3, 0.0, 0.0],
     [0.0, 0.0, 0.0, 0.0, 1/3, 0.0, 0.0, 0.0, 0.0, 1/3, 0.0, 1/3, 0.0],
     [0.0, 0.0, 0.0, 0.0, 0.0, 1/3, 0.0, 0.0, 0.0, 0.0, 1/3, 0.0, 1/3],
     [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1/3, 1/3, 0.0, 0.0, 0.0, 1/3, 0.0]]

def los(p):
    a=np.random.rand()
    if a<=p[0]:
        return 1
    elif a<p[0]+p[1]:
        return 2
    elif a<p[0]+p[1]+p[2]:
        return 3
    elif a<p[0]+p[1]+p[2]+p[3]:
        return 4
    elif a<p[0]+p[1]+p[2]+p[3]+p[4]:
        return 5
    elif a<p[0]+p[1]+p[2]+p[3]+p[4]+p[5]:
        return 6
    elif a<p[0]+p[1]+p[2]+p[3]+p[4]+p[5]+p[6]:
        return 7
    elif a<p[0]+p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]:
        return 8
    elif a<p[0]+p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]:
        return 9
    elif a<p[0]+p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]+p[9]:
        return 10
    elif a<p[0]+p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]+p[9]+p[10]:
        return 11
    elif a<p[0]+p[1]+p[2]+p[3]+p[4]+p[5]+p[6]+p[7]+p[8]+p[9]+p[10]+p[11]:
        return 12
    else:
        return 13  
    

def pajaczki(pozycja1,pozycja2):
    trasa1=[pozycja1]
    trasa2 =[pozycja2]
    krok = 0
    while trasa1[-1] != trasa2[-1]:
        x = los(P[trasa1[-1]-1])
        y = los(P[trasa2[-1]-1])
        trasa1.append(x)
        trasa2.append(y)
        krok = krok + 1
    return krok

Z = 100000
N=1000
#a
awartoscioczekiwane = []
for o in range(0,N):
    aliczbykrokow=[]
    asumaprzypadkow=0

    
    for k in range (0,Z):
        aliczbykrokow.append(pajaczki(8,11))
        asumaprzypadkow=asumaprzypadkow+aliczbykrokow[k] 

    awartoscoczekiwana=asumaprzypadkow/Z
    awartoscioczekiwane.append(round(awartoscoczekiwana,4))
    
#srednia wartosc oczekiwana
sa = sum(awartoscioczekiwane)/N
print('Oczekiwana liczba ruchów, aby pająki spotkały się w jednym węźle sieci, jesli pająki znajdują się na przeciwległych wierzchołkach sieci najbardziej zewnętrznej pętli: ', round(sa,4))


#b
bwartoscioczekiwane = []
for m in range(0,N):
    bsumaprzypadkow=0
    bliczbykrokow=[]
    
    for l in range (0,Z):
        bliczbykrokow.append(pajaczki(1,8))
        bsumaprzypadkow=bsumaprzypadkow+bliczbykrokow[l] 
    bwartoscoczekiwana=bsumaprzypadkow/Z
    bwartoscioczekiwane.append(round(bwartoscoczekiwana,4))   
#srednia wartosc oczekiwana
sb = sum(bwartoscioczekiwane)/N
print('Oczekiwana liczba ruchów, aby pająki spotkały się w jednym węźle sieci, jesli jeden pająk znajduje się w centrum sieci a drugi w jednym z węzłów sieci na najbardziej zewnętrznej pętli: ', round(sb,4))      

'''
#zgrywanie danych do pliku
with open('awartoscioczekiwane.txt', 'w') as f:
    for item in np.asarray(awartoscioczekiwane):
        f.write("%s\n" % item)

with open('bwartoscioczekiwane.txt', 'w') as f:
    for item in np.asarray(bwartoscioczekiwane):
        f.write("%s\n" % item) 

#histogramy ze sprawozdania, dla 1 wykonania symulacji
plt.subplot(1, 2, 1)
plt.hist(aliczbykrokow)
plt.subplot(1, 2, 2)
plt.hist(bliczbykrokow)
plt.show()


#zgranie plikow do txt aby uzyc ich w R, rowniez przy 1 wykonaniu symulacji
with open('aliczbykrokow.txt', 'w') as f:
    for item in np.asarray(aliczbykrokow):
        f.write("%s\n" % item)
    
with open('bliczbykrokow.txt', 'w') as f:
    for item in np.asarray(bliczbykrokow):
        f.write("%s\n" % item)
'''  

