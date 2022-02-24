import math
def predict(h1_p, h2_p, h1, h2, h3, D, L):
    delta_h_p = h1_p - h2_p
    delta_h = h1 - h2
    v_0 = math.sqrt((10/7)*9.806*(delta_h-delta_h_p))
    v_0x = v_0*D/L
    v_0y = v_0*(h2-h3)/L
    t = v_0y/9.806 + (math.sqrt(v_0y**2+2*9.806*h2))/9.806
    return t*v_0x

def test(a,b):
    return a**2 + b

e = predict(1.216	,1.167,	1.37,	1.045	,.996, .292	,	.294)


# New Trial 1 Metal Ball with premal values
f = predict(1.216	,1.167,	1.249,	1.137	,1.054, .292	,	.294)
# New Trial 2 Metal Ball with premal values
g = predict(1.205,	1.18,	1.271,	1.123,	1.045,	.298	,.294)
#^^ we changed D
i = predict(1.205,	1.18,	1.271,	1.123,	1.045,	.285	,.294)
# chnaging thr d to see if it matches
k = predict(1.205,	1.18,	1.271,	1.123,	1.045,	.290	,.294)
#regular Trial 2 with new h3
h = predict(1.205,	1.18,	1.283,	1.121,	1.05,	.298	,.294)
print(e)
print(str(f) + "hello")
print(str(g)+"metal trial 2")
print(str(i)+"better")
print(k)
print(h)
# first trial with metal ball
p = predict(1.205,	1.18,1.26,	1.144,	1.068,	.298,	.294)
print(str(p)+ "first trial metal ball")
t = predict(1.227,1.205,1.243,1.193,1.110,0.277,0.292)
print(t)

w = predict(1.205,	1.18,	1.283,	1.121,	1.05,	.298	,.294)
print(w)


#Plastic Ball Trial 1
pb1 = predict(1.216,1.167,	1.32,	1.074,	1.017,	.276,.294)
print("pb1: " + str(pb1))

#Plastic Ball Trial 2
pb2 = predict(1.216,1.167,	1.35,1.046,	.996,	.292,	.294)
print("pb2: " + str(pb2))

#292

#Metal Ball Trial 1
mb1 = predict(1.205,	1.18,	1.26,	1.144,	1.068,	.298,	.294)
print("mb1: " + str(mb1))

#Metal Ball Trial 2
mb2 = predict(1.205,	1.18,	1.271,	1.123,	1.045,	.298	,.294)
print("mb2: " + str(mb2))