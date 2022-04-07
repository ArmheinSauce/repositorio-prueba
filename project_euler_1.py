from re import X
import numpy as np
n = 1000
x = np.arange(n)

a = 3
b = 5

y = []

sum1 = 0
sum2 = 0


for i in range(len(x)):
    if x[i] % a == 0:
        y.append(x[i])
        sum1 = sum1 + x[i]
        #print (sum1)
    elif x[i] % b == 0:
        y.append(x[i])
        sum2 = sum2 + x[i]
        #print (sum2)

sum = sum1 + sum2

print(y)
print(sum)


# for i in range(len(x)):
#   if x[i]
#  print(x[i])

result = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result = result + i
#print (result)
