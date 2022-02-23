import numpy as np    
import matplotlib.pyplot as plt 
import csv
import pandas as pd
import math
from sympy import symbols, diff 

# Equation needed in order to calculate partial derivatives
D, h2, he, L = symbols('D, h2, he, L', real = True) 
F = (D)*math.sqrt(2*(h2)*(he))/(L)

# This is where we calculate for the coeffcient of Restitution
# there are 10 values for the 10 trials we did




# Here we are calculating for the partial derivative of the equation

Fx = F.diff(D)
print("hello")
print(Fx)
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