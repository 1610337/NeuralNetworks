import numpy as np

print("Hallo Welt")

'''
W = np.array([[1.,2,3], [3,4,5]])
print(W.shape)
print(W.shape[0])
print(W.shape[1])
print(W.T.shape)
'''

M=np.arange(12).reshape(3,4)
print("Basic Array")
print(M)
print("*"*40)

print(M[:1])


'''
print(M[1,:])
print(M[1])
print(M[:,1])
print(M[:,[1]])
print(M[:,[3,0,1,1]])
print("x")
print(M[:,2:4])
print(M[-2,:])
print(M[-2:,:])
# M[:,2]=2
# print(M)

#########
print("*"*20)
print(M)
print("-")
print(M.shape)
print(M.shape[0])
print(M.shape[1])

s=0
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        s+=M[i,j]
        print(s, ',', sep='', end='')
print(s)

##########
print("*"*20)

def func(x):
    print(x*x)
    return x

func(3)

'''


































