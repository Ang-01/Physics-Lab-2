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
    plt.hist(x)  # density=False would make counts
    plt.ylabel("Z Data (cm)")
    plt.xlabel("X Data (cm)")
    split = file.split(".", 1)
    plt.title(hist_names[count])
    count += 1
    plt.savefig(split[0] +".jpg")
    plt.show()


