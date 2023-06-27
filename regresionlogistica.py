import numpy as np
import matplotlib.pyplot as plt
##generar un numero al azar para conseguir gvalores optimos 
def logistic_regression(x,b):
    exponente=b[0]
    for i in range(len(x)):
        #print(b)
        exponente=exponente+b[i+1]*x[i]
    return (2.71**exponente)/(1+2.71**exponente)


def multivar_log_reg(x,b):
    y=[]
    for i in range(len(x[0])):
        x0=[]
        for z in range(len(x)):
            x0.append(x[z][i])
        y0=logistic_regression(x0,b)
        y.append(y0)
    return y
    

def mse(y_real,y_calculated):
    r=0
    for i in range(len(y_real)):
        r=r+(y_real[i]-y_calculated[i])**2
    r=r/len(y_real)
    return r

def b_arriba(b,indice):
    new_b=[]
    for i in range(len(b)):
        if i==indice:
            new_b.append(b[i]+.01)
        else:
            new_b.append(b[i])
    return new_b

def b_abajo(b,indice):
    new_b=[]
    for i in range(len(b)):
        if i==indice:
            new_b.append(b[i]-.01)
        else:
            new_b.append(b[i])
    return new_b
            
        

def neigh_search(x,y,b):
    b_vecino=[]
    best_b=b
    lowest_cost=mse(y,multivar_log_reg(x,b))
    for i in range(len(b)):
        b_vecino.append(b_arriba(b,i))
        b_vecino.append(b_abajo(b,i))
    for z in b_vecino:
        mse_zith=mse(y,multivar_log_reg(x,z))
        print(mse_zith,lowest_cost)
        if mse_zith<lowest_cost:
            best_b=z
    return best_b
        
        
        
    
        

def local_search(x,y,it_max):
    b_size=len(x)+1
    b0=np.random.randint(0,1,b_size)
    print(b0)
    y1=multivar_log_reg(x,b0)
    error=mse(y,y1)
    it=0
    while error>0.01 and it_max>it:
        print(b0)
        b0=neigh_search(x,y,b0)
        y1=multivar_log_reg(x,b0)
        error=mse(y,y1)
        it=it+1
        print(it,error)
    return b0


        
        
        
    
        
x1=[[5,2,7,10,8],[23,20,24,45,23]]
y1=[0,0,1,0,1]
l1=local_search(x1,y1,1000)

x2=[[4,9,8],[23,45,24]]
newpred=multivar_log_reg(x2,l1)
print(newpred)

#x1=[3,7]
#b1=[-2.869,0.0698,0.1694]
#y=logistic_regression(x1,b1)
#print(y)
	
