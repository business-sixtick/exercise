string = input('입력 : ')
if "안녕" in string : 
    print('안녕하세요')
elif '지금' in string : 
    print('지금은 15시입니다')

print("안" == string[0])

num = int(input('정수를 입력해 주세요 : '))
print(f'{num}은 2로 나누어 떨어지는 숫자 {"입니다" if num % 2 == 0 else "가 아닙니다" }')
print(f'{num}은 3로 나누어 떨어지는 숫자 {"입니다" if num % 3 == 0 else "가 아닙니다" }')
print(f'{num}은 4로 나누어 떨어지는 숫자 {"입니다" if num % 4 == 0 else "가 아닙니다" }')
print(f'{num}은 5로 나누어 떨어지는 숫자 {"입니다" if num % 5 == 0 else "가 아닙니다" }')

for i in range(2, 6) :
    print(f'{num}은 {i}로 나누어 떨어지는 숫자 {"입니다" if num % i == 0 else "가 아닙니다" }')