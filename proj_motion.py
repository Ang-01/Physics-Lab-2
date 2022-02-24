import numpy as np    # Note you can also import functions as abbreviations
import matplotlib.pyplot as plt 
import csv
import pandas as pd


files = ["mb1.csv","mb2.csv","pb1.csv","pb2.csv"]
count = 0

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
    
    hist_names = ["Metal Ball Trial 1", "Metal Ball Trial 2", "Plastic Ball Trial 1", "Plastic Ball Trial 2"]
    w = 1
    plt.hist(x, bins = 12)
    #bins=np.arange(min(x), max(x) + w, w))  # density=False would make counts
    plt.ylabel("Frequency")
    plt.xlabel("Difference Between Measured and Expected x Position ($\mathregular{10^{-2}}$m)")
    split = file.split(".", 1)
    plt.title(hist_names[count] + ": Offset Between Measured and Expected x Position")
    plt.savefig(split[0] +"_x.jpg")
    plt.show()
    
    plt.hist(z, bins = 12)
    #bins=np.arange(min(x), max(x) + w, w))  # density=False would make counts
    plt.ylabel("Frequency")
    plt.xlabel("Difference Between Measured and Expected z Position ($\mathregular{10^{-2}}$m)")
    split = file.split(".", 1)
    plt.title(hist_names[count] + ": Offset Between Measured and Expected z Position")
    #plt.savefig(split[0] +"_z.jpg")
    plt.show()
    count += 1
    
    
    


