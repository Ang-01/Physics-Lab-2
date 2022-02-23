import numpy as np    
import matplotlib.pyplot as plt 
import csv
import pandas as pd
import math
from sympy import symbols, diff 

# Equation needed in order to calculate partial derivatives
# Dont use sqrt use **(1/2) instead
D, h, he, L = symbols('D, h, he, L', real = True) 
#he = (10/7)*(4*0.005**2)**(1/2)
F = (D*(2*h*he)**(1/2))/L

# This is where we calculate for the coeffcient of Restitution
# there are 10 values for the 10 trials we did


files = ["mb1.csv","mb2.csv","pb1.csv","pb2.csv"]
count = 0
error_list = []
for file in files:
    file_data = pd.read_csv(file)
    h1 = file_data["h1 (cm)"][0]
    h2 = file_data["h2 (cm)"][0]
    h1p = file_data["h1' (cm)"][0]
    h2p = file_data["h2' (cm)"][0]

    #print(int(h1)/100)
    delta_h = h1 - h2
    delta_p = h1p - h2p

    he_val = (10/7)*(delta_h - delta_p)
    sigma_he = (10/7)*(4*0.005**2)**(1/2)
    sigma = 0.005
    
    d_val = file_data["D (cm)"][0]
    l_val = file_data["L (cm)"][0]


# Here we are calculating for the partial derivative of the equation
    F_D = F.diff(D)
    partial_D = F_D.evalf(subs= {D:d_val, h: h2, he: he_val, L: l_val})

    F_h = F.diff(h)
    partial_h = F_h.evalf(subs= {D:d_val, h: h2, he: he_val, L: l_val})

    F_he = F.diff(he)
    partial_he = F_he.evalf(subs= {D:d_val, h: h2, he: he_val, L: l_val})

    F_L = F.diff(L)
    partial_L = F_L.evalf(subs= {D:d_val, h: h2, he: he_val, L: l_val})

    error = math.sqrt((partial_D)*(sigma**2)+(partial_h)*(sigma**2)+(partial_he)*(sigma**2)+(partial_L)*(sigma**2))
    error_list.append(error)
    print("\n"+ file)
    print("Error: "+ str(error))
    
   
print(error_list)
    #sigma_ej_list.append(sigma_ej)
#partial = Fx(final_vel,initial_vel)
#partial_x = Fx.evalf(subs = {x:list(final_vel)[trial], y:list(initial_vel)[trial]})
#print(Fx)

    #New_Fx = Fx.evalf(subs = {a:final_vel, b:initial_vel})
    #Fx_list.append(partial_x)
    
    #Fy = F.diff(y)
    #partial = Fx(final_vel,initial_vel)
    #partial_y = Fy.evalf(subs = {x:list(final_vel)[trial], y:list(initial_vel)[trial]})
    #New_Fx = Fx.evalf(subs = {a:final_vel, b:initial_vel})
    #Fy_list.append(partial_y)
  
# Calculating the unertainty by propogating the errors sigma vi and sigma vf by using
# the partial derivatives made and their calculations
#sigma_ej_list = []
#for trial in range(len(initial_vel)):
    #sigma_ej = math.sqrt((Fx_list[trial]**2)*(sigma_vi[trial]**2)+(Fy_list[trial]**2)*(sigma_vf[trial]**2))
    #sigma_ej_list.append(sigma_ej)