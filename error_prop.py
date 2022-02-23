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

for file in files:
    file_data = pd.read_csv(file)
    print("\n"+ file)
    h1 = file_data["h1 (cm)"][0]
    h2 = file_data["h2 (cm)"][0]
    h1p = file_data["h1' (cm)"][0]
    h2p = file_data["h2' (cm)"][0]

    #print(int(h1)/100)
    delta_h = h1 - h2
    delta_p = h1p - h2p

    he_val = (10/7)*(delta_h - delta_p)

# Here we are calculating for the partial derivative of the equation
sigma = 0.05
d_val = [.298, .298, .276, .292]
h2_val = [1.144,1.123,1.076, 1.046]
he_val = []
L_val = [0.294,0.294,0.294,0.294]

F_D = F.diff(D)
print(F_D)


F_h = F.diff(h)
print(F_h)


F_he = F.diff(he)
print(F_he)


F_L = F.diff(L)
print(F_L)

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