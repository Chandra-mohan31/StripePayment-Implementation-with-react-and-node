# Pizza_0=["onion", "pepper","olive"]
# Pizza_1=["mushroom", "tomato", "basil","salt","peper"]
# Pizza_2=["chicken", "mushroom", "pepper"]
# Pizza_3=["tomato", "mushroom"]
# Pizza_4=["chicken","basil"]
# Types_of_pizzas = [Pizza_0,Pizza_1,Pizza_2,Pizza_3,Pizza_4]
# #print(Types_of_pizzas)
# max = 0

# for i in range(5):
#     for j in range(5):
        
#         test_set = (set().union(Types_of_pizzas[i], Types_of_pizzas[j]))
#         max_ing = len(test_set)
#         if(max < max_ing):
#             max=max_ing
#             wanted_set = test_set
            
# print(max) 
# print(wanted_set)     
# y- no of types of pizzas
# n- no of pizzas to be suplied
# l- no of pizzas to be delivered to per team  
# b 
# Pizza_0=["onion", "pepper","olive"]
# Pizza_1=["mushroom", "tomato", "basil"]
# Pizza_2=["chicken", "mushroom", "pepper"]
# Pizza_3=["tomato", "mushroom"]
# Pizza_4=["chicken","basil"]

from itertools import combinations
import itertools
def findcomb(y, n, l):
    #remove integer
    print("\n")
    for i in range(n):
        a=[]
        for j in range(1, int(y[i][0])+1):
            a.append(y[i][j])
        b.append(a)
    for i in b:
        print(i)
    #combinations
    c= list(combinations(b, l))
    for i in c:
        i=list(i)
        print(i)
    print("\n")
    #combine probablities into one
    p=[]    
    for i in range(len(c)):
        q=[]
        for j in range(l):
            q=q+c[i][j]
        q = list(dict.fromkeys(q))
        p.append(q)
    for i in p:
        i=list(i)
        print(i)
    m=0
    pos=-1
    for i in range(len(p)):
        if m<len(p[i]):
            m=len(p[i])
            pos=i
    print("\n")
    print(m)
    print(pos)
    last=[]
    print(b+list(c[pos]))
    print(last)
    for i in b:
        if i not in c[pos]:
            last.append(i)
    print(last)
n=int(input())
y=[]
b=[]
#input
for i in range(n):
    x = list(map(str, input().split(' ')))
    y.append(x)  

l=int(input())
findcomb(y, n, l)
            