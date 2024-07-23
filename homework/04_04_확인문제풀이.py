#28 페이지 : 2번 enumerate(리스트), 3번 딕셔너리.items()
#28 페이지 : 
print("{:b}".format(10))
print(int('1010', 2))

print("{:o}".format(10))
print(int('12', 8))

print("{:x}".format(10))
print(int('10', 16))

print('안녕안녕하세요'.count('안'))

# 이를 활용해서 1~100 사이의 있는 숫자중 2진수로 변환했을때 0이 하나만 포함된 숫자를 찾고 , 그 숫자들의 합을 구하는 코드를 만들어보세요

output = [ x for x in range(1, 101) if f'{x:b}'.count('0') == 1]
print(output)

for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print('합계:', sum(output))

# 숫자의 종류
num_list = [1,2,3,4,1,2,3,1,4,1,2,3]
num_dict = { x: num_list.count(x) for x in set(num_list)}
print(num_dict, len(num_dict))


# 염기의 개수
data = 'ctacaatgtcagtatacccattgcattagccgg'
print(data.count('a'))
print(list(data))


# 염기 코돈 개수
#data_list = [ i, v for i, v in enumerate(data) if i % 3 == ]

data_list = []
for i in range(0,len(data),3):
    data_list.append(data[i:i+3])
print(data_list)
print({ x: data_list.count(x) for x in set(data_list)})

# 2차원 리스트 평탄화
test_list = [1,2,[3,4],5,[6,7],[8,9]]
temp_list = []
if type(test_list) == list :
    for i in test_list :
        if type(i) == list:
            for j in i :
                temp_list.append(j)    
        else :
            temp_list.append(i)
print(temp_list)