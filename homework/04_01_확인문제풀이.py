list_a = [0,1,2,3,4,5,6,7]
list_a.extend(list_a) # [0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
list_a.append(10) # [0,1,2,3,4,5,6,7,10]
list_a.insert(3, 0) # [0,1,2,0,3,4,5,6,7]
list_a.remove(3) # [0,1,2,4,5,6,7]
list_a.pop(3) #[0,1,2,4,5,6,7]
list_a.clear() # []


# 다음 반복문 내부에 if 조건문의 조건시을 채워서 100이상의 숫자만 출력하게 만들어보세요
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
for i in numbers:
    if i >= 100:
        print('100 이상의 수 : ', i)




# 빈칸을 채워서 실행 결과에 해당하는 프로그램들을 완성하세요
for i in numbers:
    if i % 2 == 0 :
        print(f'{i}는 짝수 입니다')
    else : 
        print(f'{i}는 홀수 입니다')

temp = None
for i in numbers:
    temp = str(i)
    print(f'{i}는 {len(temp)} 자리수 입니다')


# 다음 코드의 빈칸을 채워서 실행 결과처럼 출력되도록 완성해 보세요
numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for i in numbers:
    output[i % 3 - 1].append(i) # (i - 1) % 3 , (i + 2) % 3
print(output)

# 다음 코드의 빈칸을 채워서 실행 결과처럼 출력되도록 완성해 보세요. 짝수 번째 요소를 제곱하는 것입니다

for i in range(0, len(numbers)//2):
    #j 가 1,3,5,7 dl 나오려면 어떤 식을 사용해야 할까요?
    j = (i * 2) + 1
    print(f'i = {i}, j = {j}')
    numbers[j] = numbers[j] ** 2
print(numbers)