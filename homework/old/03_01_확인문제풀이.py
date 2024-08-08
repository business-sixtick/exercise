print(10 == 100) # False
print(10 != 100) # True
print(10 > 100) # False
print(10 < 100) # True
print(10 <= 100) # True
print(10 >= 100) # False

x = 10
if x > 4 :
    print('True')

# 치킨이나 햄버거가 먹고 싶어서, 음식 주문 애플리케이션에서 치킨과 햄버거를 선택 했다 ( 치킨 and 햄버거 )
# H 브랜드가 출시한 10만원 이하의 가방을 구매하고 싶어서 H브랜드와 10만원 이하를 조건으로 선택해서 검색했다 ( H브랜드가격 < 10만원  and H브랜드 )
# 고궁에 입장하는데 , 65세 이상의 어르신과 5살 이하의 아동은 무료입장이었다 ( 65 <= age or 5 > age )

a = int(input('> 1 번째 숫자 : '))
b = int(input('> 2 번째 숫자 : '))
print()
if a > b:
    print('처음에 입력했던 {}가 {}보다 더 큽니다.'.format(a, b))
if b > a:
    print('두 번째로 입력했던 {}가 {}보다 더 큽니다.'.format(b, a))