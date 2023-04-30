import numpy as np
import random

names = ['Pree','Alfonso','Pierre']
balances = np.zeros((len(names),len(names)))


for i in range(len(balances)):
    for j in range(len(balances)):
        if i == j:
            continue
        balances[i][j] = random.randint(1,10)
    

# -> ows: alfonso owes pree
# # # # ^ owed: pree 
# balances = [[0., 7., 7.],
#             [2., 0., 6.],
#             [9., 3., 0.]]

print(balances)
for i in range(len(balances)):
    for j in range(len(balances)):
        if balances[i][j] >= balances[j][i]:
            balances[i][j] = balances[i][j] - balances[j][i]
            balances[j][i] = 0
        else:
            balances[j][i] = balances[j][i] - balances[i][j]
            balances[i][j] = 0
print(balances)
            # [0, 5, 0], alfonso owes pree 5
            # [0, 0, 3], pierre owes alfonso 3
            # [2, 0, 0] pree owes pierre 2

            # [0, 3, 0], alfonso owes pree 3
            # [0, 0, 3], pierre owes alfonso 3
            # [0, 0, 0] pree owes pierre 2 -- gone

            # [0, 3, 0], alfonso owes pree 3
            # [3, 0, 0], pierre owes pree 3
            # [0, 0, 0] pree owes pierre 0 
def find_max_owed(balances):
    max_person = 0
    max_owed = -1,
    count = 0
    for balance in balances:
        current_max = np.sum(balance,axis=0)
        if (current_max>max_owed):
            max_person = count
            max_owed = current_max
            print(names[max_person])
        count +=1
    return max_person

max_person = find_max_owed(balances)
lower_balances = np.delete(balances,max_person,0)
lower_balances = np.delete(lower_balances,max_person,1)

for i in range(len(balances)):
    for j in range(len(balances)):
        if balances[i][j] != 0:
            print(f"{names[j]} owes {names[i]} ${balances[i][j]}")


# for i in range(len(balances)):
#     for j in range(len(balances)):
#         if balances[j][max_person] and balances[max_person][i]>=balances[j][max_person]:
#             balances[max_person][i] = balances[max_person][i] - balances[j][max_person]
#             balances[j][max_person] = 0
print(balances)
# print(sum(balances[max_person]))
# print(sum(np.transpose(balances)[max_person]))