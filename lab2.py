import numpy as np    # Note you can also import functions as abbreviations
import matplotlib.pyplot as plt 
import csv
import pandas as pd

mb1 = pd.read_csv("mb1.csv")
xBarMetal1 = mb1["x"]
semMb1x = pd.DataFrame(xBarMetal1).sem()

zBarMetal1 = mb1["z"]
semMb1z = pd.DataFrame(zBarMetal1).sem()
print("\n X_bar metal ball 1 = " + str(np.mean(xBarMetal1)))
print("x_stdmean metal ball 1 = " + str(semMb1x))

print("z_bar metal ball 1 = " + str(np.mean(zBarMetal1)))
print("z_stdmean metal ball 1 = " + str(semMb1z))

##
print('')

mb2 = pd.read_csv("mb2.csv")
xBarMetal2 = mb2["x"]
semMb2x = pd.DataFrame(xBarMetal2).sem()

zBarMetal2 = mb2["z"]
semMb2z = pd.DataFrame(zBarMetal2).sem()
print("\n X_bar metal ball 2 = " + str(np.mean(xBarMetal2)))
print("x_stdmean metal ball 2 = " + str(semMb2x))

print("z_bar metal ball 2 = " + str(np.mean(zBarMetal2)))
print("z_stdmean metal ball 2 = " + str(semMb2z))



print("")
##
##
pb1 = pd.read_csv("pb1.csv")
xBarPlastic1 = pb1["x"]
semPb1x = pd.DataFrame(xBarPlastic1).sem()

zBarPlastic1 = pb1["z"]
semPb1z = pd.DataFrame(zBarPlastic1).sem()

print("\n X_bar plastic ball 1 = " + str(np.mean(xBarPlastic1)))
print("x_stdmean plastic ball 1 = " + str(semPb1x))

print("z_bar plastic ball 1 = " + str(np.mean(zBarPlastic1)))
print("z_stdmean plastic ball 1 = " + str(semPb1z))


print("")
##
##
pb2 = pd.read_csv("pb2.csv")
xBarPlastic2 = pb2["x"]
semPb2x = pd.DataFrame(xBarPlastic2).sem()

zBarPlastic2 = pb2["z"]
semPb2z = pd.DataFrame(zBarPlastic2).sem()

print("\n X_bar plastic ball 2 = " + str(np.mean(xBarPlastic2)))
print("x_stdmean plastic ball 2 = " + str(semPb2x))

print("z_bar plastic ball 2 = " + str(np.mean(zBarPlastic2)))
print("z_stdmean plastic ball 2 = " + str(semPb2z))
