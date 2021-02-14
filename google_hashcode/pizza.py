#input of 5 1 2 1

from itertools import combinations
import itertools


#input_data = "5 1 2 1"
input_data = input("enter the no of pizzas available in the pizzeria,no of 2-person teams,no of 3 person teams , no of 4 person teams:   ")

x = input_data.split(" ")# list of input data required is stored in the list here ie)M,T2,T3,T4
if(len(x)!=4):
    print("Please enter all the values")
    exit()
  




def scoring(x,y,z):
    return x*x + y*y + z*z

def get_best_pizza_combo(n_pizza,n_2,n_3,n_4):
    print("evaluating")
    n_2_members = n_2 * 2
    n_3_members = n_3 * 3
    n_4_members = n_4 * 4
    total_members = n_2_members + n_3_members + n_4_members
    ## n_pizza should be sum of multiples of 2,3,4
    #range till 4 as we have multiples till 4 are possible
    #check for range
    #range of no_pizza
    score_max = 0
    for i in range(n_pizza):
        for j in range(n_pizza):
            for k in range(n_pizza):
                if((i<=n_2 and j<=n_3 and k<=n_4) and (2*i + 3*j + 4*k)==n_pizza):
                    
                    #print(i,j,k)
                    
                    #i-group of 2,j-group of 3,k-group of 4
                    score  = scoring(i,j,k)
                    
                   
                    
                    if(score>score_max):
                        score_max = score
                        group_list = [i,j,k]
                    

                    #print(scoring(i,j,k))
                    #store the i,j,k and based on score choose the best
    #print(score_max) 
    print(" [two-member-teams,three-member-teams,four-member-teams] : ",group_list)  
    no_teams_pizza_supplied = sum(group_list)        
    print("No of teams Pizzas are supplied : ",no_teams_pizza_supplied)
    print("Combination of pizzas to be supplied")
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
    #l=int(input())
    # l - commbination of what 2 or 3 or what
    
    findcomb(y, n, no_teams_pizza_supplied) 

    
#using scoring we can choose the best combo

a=int(x[0])
b=int(x[1])
c=int(x[2])
d=int(x[3])


get_best_pizza_combo(a,b,c,d)

#----------------------------------------------------

# Pizza_0=["onion", "pepper","olive"]
# Pizza_1=["mushroom", "tomato", "basil"]
# Pizza_2=["chicken", "mushroom", "pepper"]
# Pizza_3=["tomato", "mushroom"]
# Pizza_4=["chicken","basil"]
# Types_of_pizzas = [Pizza_0,Pizza_1,Pizza_2,Pizza_3,Pizza_4]
# print(Types_of_pizzas)
# for i in range(4):
#     for j in range(4):
#         max = 0
#         print (set().union(Types_of_pizzas[i], Types_of_pizzas[j]))

#best types of pizza supply

# a team recieving a no of pizzas must contribute for max no of ingredients


# # consider 2 pizzas for a two member team,we need to deliver 2 pizzas to the team such that more of the ingredients are used in the two pizzas that we are supplying.




# def get_best_ingredient_combo(no_pizzas):
#     for i in range(no_pizzas):
#         for j in range(no_pizzas -1):

    

print("best pizza combo")










 
