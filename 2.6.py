
# 2kpl erilaista numerolukon koodia:
# 3 numeroa väliltä 0-9
# 4 numeroa väliltä 1-6

import random
randomlist = []
for i in range(0,3):
    n = random.randint(0,9)
    randomlist.append(n)
print(randomlist)

import random
randomlist = []
for i in range(0,4):
    k = random.randint(1,6)
    randomlist.append(k)
print(randomlist)