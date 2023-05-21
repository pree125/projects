import numpy as np
import pandas as pd

parameters = {
    'ego_velocity':[1,2,3],
    'actor_velocity':[4,5],
    # 'actor_distance':[6,7,8]
}
parameters = [[1,2,3],
            [4,5],
            [6,7,8]]
# parameter2 = 
# print(parameters["ego_velocity"])

# total_var = 1
# for key in parameters:
#     total_var = total_var*len(parameters[key])

def _helper(parameter1, parameter2,ie):
    arr = []
    for i in range(len(parameter1)):
        for j in range(len(parameter2)):
            if ie == 0:
                arr.append([parameter1[i], parameter2[j]])
            else:
                # print(str(parameter1[i])[1:-1])
                arr.append([str(parameter1[i])[1:-1], parameter2[j]])
                # print

    return arr


for i in range(len(parameters)-1):
    if(i==0):
        a = _helper(parameters[i],parameters[i+1],i)
    else:
        a = (_helper(a,parameters[i+1],i))
        
# print(a[0])
# print([1,2].tolist())

# def _helper()


island = [[1,1,1,1,0],
          [1,1,0,1,0],
          [1,1,0,0,0],
          [0,0,0,1,0],
          [0,0,0,0,1]]
# print(island[5][4])
length  = np.size(island,axis=0)
width  = np.size(island,axis=1)

def boundary(island, i,j):
    print(i,j,i>np.size(island,axis=0),j>np.size(island,axis=1) )
    if(i<0 or j<0 or i>np.size(island,axis=0)-1 or j>np.size(island,axis=1)-1 or island[i][j]==0):
        return
    
    island[i][j] = 0
    boundary(island, i+1,j)
    boundary(island, i-1,j)
    boundary(island, i,j+1)
    boundary(island, i,j-1)

count = 0
for i in range(length):
    for j in range(width):
        if island[i][j] == 1:
            count +=1
            boundary(island, i,j)
print(count)



def find_sum(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if(arr[i]+arr[j]==target):
                return ([i+1,j+1])
arr = [2,7,11,12,13,16,20]
target = 9

print(find_sum(arr, target))