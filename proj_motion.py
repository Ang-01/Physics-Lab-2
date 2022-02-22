import numpy as np    # Note you can also import functions as abbreviations
import matplotlib.pyplot as plt 
import csv
import pandas as pd


files = ["mb1.csv","mb2.csv","pb1.csv","pb2.csv"]


for file in files:
    file_data = pd.read_csv(file)
    print("\n"+ file)
    x = file_data["x"]
    z = file_data["z"]
    
    xmean = np.mean(x)
    xsem = x.sem()
    
    zmean = np.mean(z)
    zsem = z.sem()
    
    print("Mean X:" + str(xmean))
    print("Mean Error:" + str(xsem))
    print("Mean Z:" + str(zmean))
    print("Mean Error:" + str(zsem))
    
file_data = pd.read_csv("mb1.csv")
x = file_data["x"]
z = file_data["z"]
plt.hist(x, bins = 5)  # density=False would make counts
plt.ylabel(z)
plt.xlabel(x)
plt.show()

print("hello world")


