import random
numbers = random.sample(range(1,10), random.randint(6, 9))
numbers += random.sample(range(1,10), random.randint(6, 9))
numbers += random.sample(range(1,10), random.randint(6, 9))
print(numbers)
counter = {}

for i in numbers : 
    if i in counter :
        counter[i] += 1
    else : 
        counter[i] = 1


print(counter)

counter2 = {num: numbers.count(num) for num in set(numbers)}
print(counter2)

# counter3 = {v : 0 for v in numbers}
# counter3 = { v : (counter3.get(v) + 1)  for v in numbers} # 컴프리헨션에서 누적식 안됨.
# print(counter3)
counter3 = {v : 0 for v in set(numbers)} 
for i in numbers:
    counter3[i] += 1
print(counter3)

strings = []
for i in range(10) :
    strings += random.sample(range(97,123), random.randint(6, 9))
strings = [ chr(i) for i in strings]

count_dict = { k : strings.count(k) for k in set(strings)}
print(dict(sorted(count_dict.items())))

import collections
cc = collections.Counter(strings)
print(dict(sorted(cc.items())))

for i, j in enumerate( range(500)) :    
    if i is j :
        # print(i, id(i), id(j))
        pass
    else :
        print(i, id(i), id(j))
        break

print(0, 0 is 1-1)
print(-1, -1 is 0-1)


for i in range(1, 20):
    if (i % 2 == 1) :
        str1 = '*' * i 
        print(f'{str1:^20}')


for i in range(2, 10):
    for j in range(1,10):
        print(f'{i} * {j} = {i * j:2}', end='   ')
    print()


for i in range(1, 6):
    print('*' * i)

for i in range(1, 6):
    for j in range(i):
        print('*', end='')
    print()

for i in range(5):
    for j in range(5):
        if j <= i:
            print("*", end=' ')
        else :
            break
    print()

for i in range(5):
    for j in range(5):
        if j <= i:
            print("*", end=' ')
        else :
            print(' ', end=' ')
    print()
print()
for i in range(5):
    for j in range(5):
        if j >= i:
            print("*", end=' ')
        else :
            print(' ', end=' ')
    print()
